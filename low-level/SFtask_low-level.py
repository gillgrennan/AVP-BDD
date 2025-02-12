from psychopy import visual, core, event, gui, data
import random
import os
import csv

# Create a window
win = visual.Window(size=(1920, 1080), color='gray', units='pix', fullscr=True, screen=1)

# Popup to enter Subject ID and Run #
info = {"Subject ID": "", "Run #": ""}
dlg = gui.DlgFromDict(dictionary=info, title="Task Info")
if not dlg.OK:
    core.quit()  # Exit if user cancels dialog

subject_id = info["Subject ID"]
run_number = info["Run #"]

# Create a "data" folder if it doesn't exist
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

# Define fixation cross
fixation = visual.TextStim(win, text='+', color='white', height=65)

# Define instructions screen
instructions = visual.TextStim(win, text=(
    "Keep your gaze focused on the cross at the center of the screen.\n"
    "Occasionally, the fixation cross at the center will turn GREEN.\n"
    "When this happens, press the button as quickly as possible.\n\n\n"
    "Waiting for scanner..."
), color='white', height=50, wrapWidth=1500, alignText='center')

# Define Gabor patches for each condition
gabor_conditions = {
    "Condition 1": {"sf": 0.004, "contrast": 1}, #1 cpd: [cpd / num pixels = sf val for psychopy] 
    "Condition 2": {"sf": 0.032, "contrast": 1}, #16 cpd: [cpd / num pixels = sf val for psychopy] 
    "Condition 3": {"sf": 0.004, "contrast": 0.04}, #1 cpd 
    "Condition 4": {"sf": 0.032, "contrast": 0.04}, #16 cpd
}

# Create Gabor stimuli
gabor_stimuli = {
    cond: visual.GratingStim(win, tex="sin", mask="gauss", units="pix",
                             size=(500, 500), sf=params["sf"],
                             contrast=params["contrast"])
    for cond, params in gabor_conditions.items()
}

# Define task parameters
n_blocks = 16
trials_per_block = 20
block_fixation_time = 10  # seconds
oddball_probability = 0.1  # 10% chance of green fixation

# Function to generate or load block order
def get_block_order(subject_id, n_blocks):
    file_name = f"Subject_{subject_id}_block_order.csv"
    
    # Check if the file exists
    if os.path.exists(file_name):
        print(f"Block order file found: {file_name}")
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            block_order = next(reader)  # Read the first row as block order
    else:
        print(f"No block order file found for Subject {subject_id}. Generating a new order.")
        block_order = random.sample(list(gabor_conditions.keys()) * 4, n_blocks)
        
        # Save the block order to a CSV file
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(block_order)
    
    return block_order

# Generate or load the block order
block_conditions = get_block_order(subject_id, n_blocks)

# Randomize the order of conditions across blocks
#block_conditions = random.sample(list(gabor_conditions.keys()) * 4, n_blocks)

# Initialize data storage
data_file = os.path.join(data_folder, f"Subject_{subject_id}_Run_{run_number}_RT.csv")
with open(data_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Block", "Trial", "Condition", "Oddball", 
                     "Reaction Time (s)", "Stimulus Onset (s)", "Stimulus Offset (s)"])

# Function to check for force quit
def check_quit():
    if 'escape' in event.getKeys():
        win.close()
        core.quit()

# Wait for the 't' key press to synchronize with the fMRI scanner
def wait_for_scanner():
    instructions.draw()
    win.flip()
    print("Waiting for the 't' key press to start the task.")
    while True:
        keys = event.getKeys()
        if 't' in keys:
            print("Task starting!")
            return
        check_quit()  # Allow quitting anytime

# Display instructions and wait for scanner trigger
wait_for_scanner()

# Initialize a clock for timing
global_clock = core.Clock()

# Run the task
for block_num, condition in enumerate(block_conditions, start=1):
    print(f"Block {block_num}: {condition}")  # To keep track of conditions during testing

    for trial in range(trials_per_block):
        check_quit()  # Check for escape key before each trial

        # Decide randomly if the fixation cross should turn green (~10% of trials)
        green_fixation = random.random() < oddball_probability

        # Inter-stimulus fixation (always white cross)
        fixation.color = 'white'
        fixation.draw()
        win.flip()
        core.wait(0.1)  # 100 ms inter-stimulus fixation

        # Draw Gabor patch with fixation cross (green if oddball)
        if green_fixation:
            fixation.color = 'green'
        else:
            fixation.color = 'white'

        gabor_stimuli[condition].draw()
        fixation.draw()
        stimulus_onset = global_clock.getTime()  # Record onset time
        win.flip()

        # Record reaction times
        rt = None
        response = event.getKeys(keyList=["y"], timeStamped=global_clock)
        if response:
            rt = response[0][1]  # Capture the timestamp of the response

        core.wait(0.4)  # 400 ms stimulus duration
        stimulus_offset = global_clock.getTime()  # Record offset time

        # Inter-stimulus fixation
        fixation.color = 'white'  # Reset fixation color
        fixation.draw()
        win.flip()
        core.wait(0.1)  # 100 ms fixation interval

        # Record any responses during the inter-stimulus interval
        response_during_fixation = event.getKeys(keyList=["y"], timeStamped=global_clock)
        if response_during_fixation and rt is None:
            rt = response_during_fixation[0][1]  # Record reaction time if no earlier response

        # Save trial data
        with open(data_file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([block_num, trial + 1, condition, green_fixation, 
                             rt, stimulus_onset, stimulus_offset])

    # Inter-block fixation (always white cross)
    fixation.color = 'white'
    fixation.draw()
    win.flip()
    core.wait(block_fixation_time)
    
# Display plain screen for the last 5 seconds
win.color = 'gray'
win.flip()
core.wait(5)

# Close the window
win.close()
core.quit()
