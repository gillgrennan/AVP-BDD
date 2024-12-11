from psychopy import visual, core, event, gui, data
import random
import os
import csv

# Create a window
win = visual.Window(size=(800, 800), color='gray', units='pix')

# Popup to enter Subject ID, Run #, and Stimulus Category
info = {"Subject ID": "", "Run #": "", "Stimulus Category": ["House", "Face", "Body"]}
dlg = gui.DlgFromDict(dictionary=info, title="Task Info")
if not dlg.OK:
    core.quit()  # Exit if user cancels dialog

subject_id = info["Subject ID"]
run_number = info["Run #"]
stimulus_category = info["Stimulus Category"]

# Determine folder based on stimulus category
stimuli_folder = f"/Users/gilliangrennan/Desktop/CONNECTLab/AVP-BDD/fMRI-tasks/SF-task/high-level/{stimulus_category.lower()}_stimuli"  # e.g., "house_stimuli", "face_stimuli", "body_stimuli"

# Define fixation cross
fixation = visual.TextStim(win, text='+', color='white', height=30)

# Define instructions screen
instructions = visual.TextStim(win, text=(
    "Keep your gaze focused on the cross at the center of the screen.\n"
    "Occasionally, the fixation cross at the center will turn GREEN.\n"
    "When this happens, press the button as quickly as possible.\n\n\n"
    "Waiting for scanner..."
), color='white', height=20, wrapWidth=700, alignText='center')

# Function to load images by type
def load_images(folder, filter_type):
    return [os.path.join(folder, img) for img in os.listdir(folder) if img.endswith(f"-{filter_type}.jpg")]

# Load stimuli images for each condition
stimuli_images = {
    "LSF": load_images(stimuli_folder, "LSF"),
    "HSF": load_images(stimuli_folder, "HSF"),
    "NSF": load_images(stimuli_folder, "NSF")
}

# Define task parameters
n_blocks = 15
trials_per_block = 20
block_fixation_time = 10  # seconds
oddball_probability = 0.1  # 10% chance of green fixation

# Randomize the order of conditions across blocks
block_conditions = random.sample(["LSF", "HSF", "NSF"] * 5, n_blocks)

# Initialize data storage
data_file = f"Subject_{subject_id}_Run_{run_number}_{stimulus_category}_RT.csv"
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

        # Select a random image for the current condition
        stimulus_image = random.choice(stimuli_images[condition])
        stim = visual.ImageStim(win, image=stimulus_image, size=(300, 300))

        # Draw image with fixation cross (green if oddball)
        if green_fixation:
            fixation.color = 'green'
        else:
            fixation.color = 'white'

        stim.draw()
        fixation.draw()
        stimulus_onset = global_clock.getTime()  # Record onset time
        win.flip()

        # Record reaction times
        rt = None
        response = event.getKeys(keyList=["space"], timeStamped=global_clock)
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
        response_during_fixation = event.getKeys(keyList=["space"], timeStamped=global_clock)
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