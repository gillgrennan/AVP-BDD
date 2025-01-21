#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.0),
    on Thu Dec 12 10:23:50 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from EyelinkCode
import pylink
import platform
import time
import random as randomITI
from hardware.EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy import monitors
from string import ascii_letters, digits
# Run 'Before Experiment' code from code_start
upright_flag=0
inverted_flag=0
msg=""
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.0'
expName = 'inversion_effect'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '',
    'order': [1,2,3,4],
    'EEG': False,
    'EyeLink': False,
    'EyeTribe': False,
    'Calibrate': False,
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('debug')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/sub-%s_task-%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/gilliangrennan/Downloads/inverted-faces-psychopy-main/inversion_effect.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1440, 900], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_practice') is None:
        # initialise key_resp_practice
        key_resp_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_practice',
        )
    if deviceManager.getDevice('key_resp_up_prac') is None:
        # initialise key_resp_up_prac
        key_resp_up_prac = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_up_prac',
        )
    if deviceManager.getDevice('key_resp_inv_prac') is None:
        # initialise key_resp_inv_prac
        key_resp_inv_prac = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_inv_prac',
        )
    if deviceManager.getDevice('key_resp_endPractice') is None:
        # initialise key_resp_endPractice
        key_resp_endPractice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_endPractice',
        )
    if deviceManager.getDevice('key_resp_upright') is None:
        # initialise key_resp_upright
        key_resp_upright = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_upright',
        )
    if deviceManager.getDevice('key_resp_inverted') is None:
        # initialise key_resp_inverted
        key_resp_inverted = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_inverted',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Start" ---
    # Run 'Begin Experiment' code from EyelinkCode
    # Set this variable to True if you use the built-in retina screen as your
    # primary display device on macOS. If have an external monitor, set this
    # variable True if you choose to "Optimize for Built-in Retina Display"
    # in the Displays preference settings.
    use_retina = False
    
    # Set this variable to True to run the script in "Dummy Mode"
    #dummy_mode = True
    
    # Set this variable to True to run the task in full screen mode
    # It is easier to debug the script in non-fullscreen mode
    full_screen = True
    
    # Set up EDF data file name and local data folder
    #
    # The EDF data filename should not exceed 8 alphanumeric characters
    # use ONLY number 0-9, letters, & _ (underscore) in the filename
    participant_id = expInfo['participant'][:5]  # Limit participant ID to 5 chars
    session_num = expInfo['session'][:1]  # Assume session info is provided in expInfo
    edf_fname = f'{participant_id}IE{session_num}'
    
    if expInfo['EyeLink']:
        # Validate filename: Only keep allowed characters
        allowed_char = ascii_letters + digits + '_'
        edf_fname = ''.join([c for c in edf_fname if c in allowed_char])
    
        if len(edf_fname) == 0:
            print("ERROR: Invalid or empty participant ID for EDF filename.")
            core.quit()  # Exit if no valid filename is generated
    
    # Set up a folder to store the EDF data files and the associated resources
    # e.g., files defining the interest areas used in each trial
    results_folder = 'data'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
    
    # We download EDF data file from the EyeLink Host PC to the local hard
    # drive at the end of each testing session, here we rename the EDF to
    # include session start date/time
    time_str = time.strftime("_%Y-%m-%dT%H%M", time.localtime())
    session_sname=u'sub-%s' % (expInfo['participant'])
    session_edfname = session_sname + '_task-IET_eyetrack'
    session_identifier = session_edfname + time_str
    
    # create a folder for the current testing session in the "results" folder
    session_folder = os.path.join(results_folder, session_sname, 'eyetrack')
    if not os.path.exists(session_folder):
        os.makedirs(session_folder)
    
    # Step 1: Connect to the EyeLink Host PC
    #
    # The Host IP address, by default, is "100.1.1.1".
    # the "el_tracker" objected created here can be accessed through the Pylink
    # Set the Host PC address to "None" (without quotes) to run the script
    # in "Dummy Mode"
    #if dummy_mode:
    if not expInfo['EyeLink']:
        dummy_mode = True
        el_tracker = pylink.EyeLink(None)
    else:
        dummy_mode = False
        try:
            el_tracker = pylink.EyeLink("100.1.1.1")
        except RuntimeError as error:
            print('ERROR:', error)
            core.quit()
            sys.exit()
    
    # Step 2: Open an EDF data file on the Host PC
    edf_file = edf_fname + ".edf"
    try:
        el_tracker.openDataFile(edf_file)
    except RuntimeError as err:
        print('ERROR:', err)
        # close the link if we have one open
        if el_tracker.isConnected():
            el_tracker.close()
        core.quit()
        sys.exit()
    
    # Add a header text to the EDF file to identify the current experiment name
    # This is OPTIONAL. If your text starts with "RECORDED BY " it will be
    # available in DataViewer's Inspector window by clicking
    # the EDF session node in the top panel and looking for the "Recorded By:"
    # field in the bottom panel of the Inspector.
    preamble_text = 'RECORDED BY %s' % os.path.basename(__file__)
    el_tracker.sendCommand("add_file_preamble_text '%s'" % preamble_text)
    
    # Step 3: Configure the tracker
    #
    # Put the tracker in offline mode before we change tracking parameters
    el_tracker.setOfflineMode()
    
    # Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
    # 5-EyeLink 1000 Plus, 6-Portable DUO
    eyelink_ver = 0  # set version to 0, in case running in Dummy mode
    if not dummy_mode:
        vstr = el_tracker.getTrackerVersionString()
        eyelink_ver = int(vstr.split()[-1].split('.')[0])
        # print out some version info in the shell
        print('Running experiment on %s, version %d' % (vstr, eyelink_ver))
    
    # File and Link data control
    # what eye events to save in the EDF file, include everything by default
    file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
    # what eye events to make available over the link, include everything by default
    link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
    # what sample data to save in the EDF data file and to make available
    # over the link, include the 'HTARGET' flag to save head target sticker
    # data for supported eye trackers
    if eyelink_ver > 3:
        # add "HTARGET" to record possible target data for EyeLink Remote.
        # HMARKER (originally for Eyelink2's infrared head tracking markers) and
        # INPUT (originally for the TTL lines) are jury-rigged to hold the extra data.
        # You can also set file_sample_data to collect raw samples in the .edf file.
        # CAUTION: It may or may not work on your setup with your tracker.
        file_sample_flags = 'LEFT,RIGHT,GAZE,AREA,GAZERES,HREF,PUPIL,STATUS,HTARGET,INPUT,HMARKER'
        #file_sample_flags = 'LEFT,RIGHT,GAZE,AREA,GAZERES,HREF,PUPIL,STATUS,INPUT,HMARKER'
        link_sample_flags = 'LEFT,RIGHT,GAZE,AREA,GAZERES,HREF,PUPIL,STATUS,INPUT,HMARKER'
    else:
        file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
        link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
    el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
    el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
    el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
    el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)
    
    # Optional tracking parameters
    # Sample rate, 250, 500, 1000, or 2000, check your tracker specification
    if eyelink_ver > 2:
        el_tracker.sendCommand("sample_rate 500")
    # Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
    el_tracker.sendCommand("calibration_type = HV13")
    # Set a gamepad button to accept calibration/drift check target
    # You need a supported gamepad/button box that is connected to the Host PC
    #el_tracker.sendCommand("button_function 5 'accept_target_fixation'")
    
    # Optional -- Shrink the spread of the calibration/validation targets
    # if the default outermost targets are not all visible in the bore.
    # The default <x, y display proportion> is 0.88, 0.83 (88% of the display
    # horizontally and 83% vertically)
    #el_tracker.sendCommand('calibration_area_proportion 0.88 0.83')
    #el_tracker.sendCommand('validation_area_proportion 0.88 0.83')
    
    # Step 4: set up a graphics environment for calibration
    #
    # Open a window, be sure to specify monitor parameters
    mon = monitors.Monitor('myMonitor', width=24.0, distance=75.0)
    
    # Setup the Window
    #win = visual.Window(
    #    size=[1920, 1080], fullscr=full_screen, screen=1,
    #    winType='pyglet', allowGUI=True, allowStencil=False,
    #    monitor=mon, color=[0.300,0.300,0.300], colorSpace='rgb',
    #    blendMode='avg', useFBO=True,
    #    units='pix')
    
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # get the native screen resolution used by PsychoPy
    scn_width, scn_height = win.size
    # resolution fix for Mac retina displays
    if 'Darwin' in platform.system():
        if use_retina:
            scn_width = int(scn_width/2.0)
            scn_height = int(scn_height/2.0)
    
    # Pass the display pixel coordinates (left, top, right, bottom) to the tracker
    # see the EyeLink Installation Guide, "Customizing Screen Settings"
    el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
    el_tracker.sendCommand(el_coords)
    
    # Write a DISPLAY_COORDS message to the EDF file
    # Data Viewer needs this piece of info for proper visualization, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
    el_tracker.sendMessage(dv_coords)
    
    
    # Configure a graphics environment (genv) for tracker calibration
    genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
    print(genv)  # print out the version number of the CoreGraphics library
    
    # Set background and foreground colors for the calibration target
    # in PsychoPy, (-1, -1, -1)=black, (1, 1, 1)=white, (0, 0, 0)=mid-gray
    foreground_color = (1, 1, 1)
    background_color = win.color
    genv.setCalibrationColors(foreground_color, background_color)
    
    # Set up the calibration target
    #
    
    # Use the default calibration target ('circle')
    genv.setTargetType('circle')
    
    # Configure the size of the calibration target (in pixels)
    # this option applies only to "circle" and "spiral" targets
    genv.setTargetSize(28)
    
    # Beeps to play during calibration, validation and drift correction
    # parameters: target, good, error
    #     target -- sound to play when target moves
    #     good -- sound to play on successful operation
    #     error -- sound to play on failure or interruption
    # Each parameter could be ''--default sound, 'off'--no sound, or a wav file
    genv.setCalibrationSounds('off', 'off', 'off')
    
    # resolution fix for macOS retina display issues
    if use_retina:
        genv.fixMacRetinaDisplay()
    
    # Request Pylink to use the PsychoPy window we opened above for calibration
    pylink.openGraphicsEx(genv)
    
    # ##############################################################################
    # define a few helper functions for trial handling
    # ##############################################################################
    
    def clear_screen(win):
        """ clear up the PsychoPy window"""
    
        win.fillColor = genv.getBackgroundColor()
        win.flip()
    
    
    def show_msg(win, text, wait_for_keypress=True):
        """ Show task instructions on screen"""
    
        msg = visual.TextStim(win, text,
                              font='Arial',
                              pos=(0, 0), height=0.03, ori=0,
                              color='black', colorSpace='rgb', opacity=1,
                              languageStyle='LTR', depth=0.0,
                              wrapWidth=scn_width/2,
                              units='height')
    
        clear_screen(win)
        msg.draw()
        win.flip()
    
        # wait indefinitely, terminates upon any key press
        if wait_for_keypress:
            event.waitKeys()
            clear_screen(win)
    
    
    def terminate_task():
        """
        Terminate the task gracefully and retrieve the EDF data file
    
        file_to_retrieve: The EDF on the Host that we would like to download
        win: the current window used by the experimental script
        """
    
        el_tracker = pylink.getEYELINK()
    
        if el_tracker.isConnected():
            # Terminate the current trial first if the task terminated prematurely
            error = el_tracker.isRecording()
            if error == pylink.TRIAL_OK:
                abort_trial()
    
            # Put tracker in Offline mode
            el_tracker.setOfflineMode()
    
            # Clear the Host PC screen and wait for 500 ms
            el_tracker.sendCommand('clear_screen 0')
            pylink.msecDelay(500)
    
            # Close the edf data file on the Host
            el_tracker.closeDataFile()
    
            # Show a file transfer message on the screen
            msg = 'EDF data is transferring from EyeLink Host PC...'
            show_msg(win, msg, wait_for_keypress=False)
    
            # Download the EDF data file from the Host PC to a local data folder
            # parameters: source_file_on_the_host, destination_file_on_local_drive
            local_edf = os.path.join(session_folder, session_identifier + '.edf')
            try:
                el_tracker.receiveDataFile(edf_file, local_edf)
            except RuntimeError as error:
                print('ERROR:', error)
    
            # Close the link to the tracker.
            el_tracker.close()
    
    
    def abort_trial():
        """Ends recording"""
    
        el_tracker = pylink.getEYELINK()
    
        # Stop recording
        if el_tracker.isRecording():
            # add 100 ms to catch final trial events
            pylink.pumpDelay(100)
            el_tracker.stopRecording()
    
        # clear the screen
        clear_screen(win)
        # Send a message to clear the Data Viewer screen
        bgcolor_RGB = (116, 116, 116)
        el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)
    
        # send a message to mark trial end
        el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_ERROR)
    
        return pylink.TRIAL_ERROR
    
    
    if expInfo['Calibrate']:
        # Show the task instructions
        if not dummy_mode:
            task_msg = 'In a moment, we will calibrate the eye tracker.\n' + \
                       'Please look at the dots whenever they appear on the screen.\n\n' + \
                       'Press ENTER twice to open the calibration menu.'
            show_msg(win, task_msg)
            # Set up the camera and calibrate the tracker, if not running in dummy mode
            try:
                el_tracker.doTrackerSetup()
            except RuntimeError as err:
                print('ERROR during calibration:', err)
                el_tracker.exitCalibration()
    
    # ------Start EyeLink Recording-------
    # put tracker in idle/offline mode before recording
    el_tracker.setOfflineMode()
    
    # Start recording, at the beginning of a new run
    # arguments: sample_to_file, events_to_file, sample_over_link,
    # event_over_link (1-yes, 0-no)
    try:
        el_tracker.startRecording(1, 1, 1, 1)
    except RuntimeError as error:
        print("ERROR:", error)
        terminate_task()
    
    # Allocate some time for the tracker to cache some samples
    pylink.pumpDelay(100)
    
    # --- Initialize components for Routine "instrPractice" ---
    text_practice = visual.TextStim(win=win, name='text_practice',
        text="In this task, you will see images of faces." + "\n During each trial, one image will flash before you—this is the target image. Afterward, two images will appear side by side. Your task is to select the image that looks exactly like the target image." + "\n\n Please press the LEFT BUTTON to choose the image on the left, or press the RIGHT BUTTON to choose the image on the right. Try to make your choice as quickly and accurately as possible." + "\n\n Press SPACEBAR to practice.",
        font='Arial',
        units='norm', pos=(0, 0), height=0.08, wrapWidth=1.8, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_practice = keyboard.Keyboard(deviceName='key_resp_practice')
    
    # --- Initialize components for Routine "getReady" ---
    text_countdown = visual.TextStim(win=win, name='text_countdown',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Fixation" ---
    # Run 'Begin Experiment' code from code_fixation
    # index trials for eyetracking
    trial_index=0
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "EncodingUpright" ---
    image_target_upright = visual.ImageStim(
        win=win,
        name='image_target_upright', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "ISI" ---
    text_isi = visual.TextStim(win=win, name='text_isi',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ProbeUpPractice" ---
    image_probePrac_up_left = visual.ImageStim(
        win=win,
        name='image_probePrac_up_left', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(-0.2, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    image_probePrace_up_right = visual.ImageStim(
        win=win,
        name='image_probePrace_up_right', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0.2, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    key_resp_up_prac = keyboard.Keyboard(deviceName='key_resp_up_prac')
    
    # --- Initialize components for Routine "ITI" ---
    text_iti = visual.TextStim(win=win, name='text_iti',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Fixation" ---
    # Run 'Begin Experiment' code from code_fixation
    # index trials for eyetracking
    trial_index=0
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "EncodingInverted" ---
    image_target_inverted = visual.ImageStim(
        win=win,
        name='image_target_inverted', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=True,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "ISI" ---
    text_isi = visual.TextStim(win=win, name='text_isi',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ProbeInvPractice" ---
    image_probePrac_inv_left = visual.ImageStim(
        win=win,
        name='image_probePrac_inv_left', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(-0.2, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=True,
        texRes=128, interpolate=True, depth=-1.0)
    image_probePrace_inv_right = visual.ImageStim(
        win=win,
        name='image_probePrace_inv_right', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0.2, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=True,
        texRes=128, interpolate=True, depth=-2.0)
    key_resp_inv_prac = keyboard.Keyboard(deviceName='key_resp_inv_prac')
    
    # --- Initialize components for Routine "ITI" ---
    text_iti = visual.TextStim(win=win, name='text_iti',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "FB_Practice" ---
    text_Practice = visual.TextStim(win=win, name='text_Practice',
        text='',
        font='Arial',
        units='norm', pos=(0, 0.05), height=0.06, wrapWidth=1.8, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_endPractice = keyboard.Keyboard(deviceName='key_resp_endPractice')
    
    # --- Initialize components for Routine "getReady" ---
    text_countdown = visual.TextStim(win=win, name='text_countdown',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Fixation" ---
    # Run 'Begin Experiment' code from code_fixation
    # index trials for eyetracking
    trial_index=0
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "EncodingUpright" ---
    image_target_upright = visual.ImageStim(
        win=win,
        name='image_target_upright', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "ISI" ---
    text_isi = visual.TextStim(win=win, name='text_isi',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ProbeUpright" ---
    image_probe_upright_left = visual.ImageStim(
        win=win,
        name='image_probe_upright_left', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(-0.25, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    image_probe_upright_right = visual.ImageStim(
        win=win,
        name='image_probe_upright_right', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0.25, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    key_resp_upright = keyboard.Keyboard(deviceName='key_resp_upright')
    
    # --- Initialize components for Routine "ITI" ---
    text_iti = visual.TextStim(win=win, name='text_iti',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Fixation" ---
    # Run 'Begin Experiment' code from code_fixation
    # index trials for eyetracking
    trial_index=0
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "EncodingInverted" ---
    image_target_inverted = visual.ImageStim(
        win=win,
        name='image_target_inverted', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=True,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "ISI" ---
    text_isi = visual.TextStim(win=win, name='text_isi',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ProbeInverted" ---
    image_probe_inverted_left = visual.ImageStim(
        win=win,
        name='image_probe_inverted_left', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(-0.25, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=True,
        texRes=128, interpolate=True, depth=-1.0)
    image_probe_inverted_right = visual.ImageStim(
        win=win,
        name='image_probe_inverted_right', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0.25, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=True,
        texRes=128, interpolate=True, depth=-2.0)
    key_resp_inverted = keyboard.Keyboard(deviceName='key_resp_inverted')
    
    # --- Initialize components for Routine "ITI" ---
    text_iti = visual.TextStim(win=win, name='text_iti',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "IBI" ---
    text_ibi = visual.TextStim(win=win, name='text_ibi',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ThankYou" ---
    text_thanks = visual.TextStim(win=win, name='text_thanks',
        text="Thank you for your participation!" + "\n\n Please wait until the task is complete before exiting the browser.",
        font='Arial',
        units='norm', pos=(0, 0), height=0.08, wrapWidth=1.8, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Start" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Start.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code_start
    win.mouseVisible = False
    
    # determine block order
    if expInfo['order']==1:
        order_list="stimuli/faces_blockList1.csv"
    elif expInfo['order']==2:
        order_list="stimuli/faces_blockList2.csv"
    elif expInfo['order']==3:
        order_list="stimuli/faces_blockList3.csv"
    elif expInfo['order']==4:
        order_list="stimuli/faces_blockList4.csv"
    # keep track of which components have finished
    StartComponents = []
    for thisComponent in StartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Start" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Start" ---
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Start.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instrPractice" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instrPractice.started', globalClock.getTime(format='float'))
    key_resp_practice.keys = []
    key_resp_practice.rt = []
    _key_resp_practice_allKeys = []
    # keep track of which components have finished
    instrPracticeComponents = [text_practice, key_resp_practice]
    for thisComponent in instrPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instrPractice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_practice* updates
        
        # if text_practice is starting this frame...
        if text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_practice.frameNStart = frameN  # exact frame index
            text_practice.tStart = t  # local t and not account for scr refresh
            text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_practice.status = STARTED
            text_practice.setAutoDraw(True)
        
        # if text_practice is active this frame...
        if text_practice.status == STARTED:
            # update params
            pass
        
        # *key_resp_practice* updates
        waitOnFlip = False
        
        # if key_resp_practice is starting this frame...
        if key_resp_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice.frameNStart = frameN  # exact frame index
            key_resp_practice.tStart = t  # local t and not account for scr refresh
            key_resp_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_practice.started')
            # update status
            key_resp_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_practice_allKeys.extend(theseKeys)
            if len(_key_resp_practice_allKeys):
                key_resp_practice.keys = _key_resp_practice_allKeys[-1].name  # just the last key pressed
                key_resp_practice.rt = _key_resp_practice_allKeys[-1].rt
                key_resp_practice.duration = _key_resp_practice_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrPractice" ---
    for thisComponent in instrPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instrPractice.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_practice.keys in ['', [], None]:  # No response was made
        key_resp_practice.keys = None
    thisExp.addData('key_resp_practice.keys',key_resp_practice.keys)
    if key_resp_practice.keys != None:  # we had a response
        thisExp.addData('key_resp_practice.rt', key_resp_practice.rt)
        thisExp.addData('key_resp_practice.duration', key_resp_practice.duration)
    thisExp.nextEntry()
    # the Routine "instrPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks_practice = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli/practice_blockList.csv'),
        seed=None, name='blocks_practice')
    thisExp.addLoop(blocks_practice)  # add the loop to the experiment
    thisBlocks_practice = blocks_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_practice.rgb)
    if thisBlocks_practice != None:
        for paramName in thisBlocks_practice:
            globals()[paramName] = thisBlocks_practice[paramName]
    
    for thisBlocks_practice in blocks_practice:
        currentLoop = blocks_practice
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlocks_practice.rgb)
        if thisBlocks_practice != None:
            for paramName in thisBlocks_practice:
                globals()[paramName] = thisBlocks_practice[paramName]
        
        # --- Prepare to start Routine "getReady" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('getReady.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        getReadyComponents = [text_countdown]
        for thisComponent in getReadyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "getReady" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_countdown* updates
            
            # if text_countdown is starting this frame...
            if text_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_countdown.frameNStart = frameN  # exact frame index
                text_countdown.tStart = t  # local t and not account for scr refresh
                text_countdown.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_countdown.status = STARTED
                text_countdown.setAutoDraw(True)
            
            # if text_countdown is active this frame...
            if text_countdown.status == STARTED:
                # update params
                text_countdown.setText(str(5-int(t)), log=False)
            
            # if text_countdown is stopping this frame...
            if text_countdown.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_countdown.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_countdown.tStop = t  # not accounting for scr refresh
                    text_countdown.tStopRefresh = tThisFlipGlobal  # on global time
                    text_countdown.frameNStop = frameN  # exact frame index
                    # update status
                    text_countdown.status = FINISHED
                    text_countdown.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in getReadyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "getReady" ---
        for thisComponent in getReadyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('getReady.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # set up handler to look after randomisation of conditions etc
        trials_practice_up = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(block_list, selection='0:1'),
            seed=None, name='trials_practice_up')
        thisExp.addLoop(trials_practice_up)  # add the loop to the experiment
        thisTrials_practice_up = trials_practice_up.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice_up.rgb)
        if thisTrials_practice_up != None:
            for paramName in thisTrials_practice_up:
                globals()[paramName] = thisTrials_practice_up[paramName]
        
        for thisTrials_practice_up in trials_practice_up:
            currentLoop = trials_practice_up
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice_up.rgb)
            if thisTrials_practice_up != None:
                for paramName in thisTrials_practice_up:
                    globals()[paramName] = thisTrials_practice_up[paramName]
            
            # --- Prepare to start Routine "Fixation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Fixation.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_fixation
            EEGtriggerSent = False
            EYEtriggerSent = False
            trial_index += 1
            
            # log a TRIALID message to mark trial start, before starting to record.
            # EyeLink Data Viewer defines the start of a trial by the TRIALID message.
            if expInfo['EyeLink']:
                el_tracker.sendMessage("TRIALID %d" % trial_index)
            if expInfo['EyeTribe']:
                tracker.log_message("TRIALID %d" % trial_index)
            # keep track of which components have finished
            FixationComponents = [text_fixation]
            for thisComponent in FixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fixation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_fixation
                if expInfo['EEG'] and text_fixation.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event, event_type="FXN+",label="FXN+",duration=float(fix_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"FXN+") # fixation marker
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"FXN+") # fixation marker
                    EYEtriggerSent = True
                
                # *text_fixation* updates
                
                # if text_fixation is starting this frame...
                if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_fixation.frameNStart = frameN  # exact frame index
                    text_fixation.tStart = t  # local t and not account for scr refresh
                    text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.started')
                    # update status
                    text_fixation.status = STARTED
                    text_fixation.setAutoDraw(True)
                
                # if text_fixation is active this frame...
                if text_fixation.status == STARTED:
                    # update params
                    pass
                
                # if text_fixation is stopping this frame...
                if text_fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_fixation.tStartRefresh + fix_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_fixation.tStop = t  # not accounting for scr refresh
                        text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        text_fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                        # update status
                        text_fixation.status = FINISHED
                        text_fixation.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fixation" ---
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Fixation.stopped', globalClock.getTime(format='float'))
            # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "EncodingUpright" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('EncodingUpright.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_encode_upright
            EEGtriggerSent = False
            EYEtriggerSent = False
            orient = "upright" # trial categorization 
            # Add the variable to a new column in the output file
            thisExp.addData("orient", orient)
            image_target_upright.setSize(stim_size)
            image_target_upright.setImage(target_list)
            # keep track of which components have finished
            EncodingUprightComponents = [image_target_upright]
            for thisComponent in EncodingUprightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EncodingUpright" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_encode_upright
                if expInfo['EEG'] and image_target_upright.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_target_upright.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,target_list)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_target_upright.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,target_list)
                    EYEtriggerSent = True
                
                # *image_target_upright* updates
                
                # if image_target_upright is starting this frame...
                if image_target_upright.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_target_upright.frameNStart = frameN  # exact frame index
                    image_target_upright.tStart = t  # local t and not account for scr refresh
                    image_target_upright.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_target_upright, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_target_upright.started')
                    # update status
                    image_target_upright.status = STARTED
                    image_target_upright.setAutoDraw(True)
                
                # if image_target_upright is active this frame...
                if image_target_upright.status == STARTED:
                    # update params
                    pass
                
                # if image_target_upright is stopping this frame...
                if image_target_upright.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_target_upright.tStartRefresh + target_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_target_upright.tStop = t  # not accounting for scr refresh
                        image_target_upright.tStopRefresh = tThisFlipGlobal  # on global time
                        image_target_upright.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_target_upright.stopped')
                        # update status
                        image_target_upright.status = FINISHED
                        image_target_upright.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EncodingUprightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EncodingUpright" ---
            for thisComponent in EncodingUprightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('EncodingUpright.stopped', globalClock.getTime(format='float'))
            # the Routine "EncodingUpright" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ISI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ISI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_isi
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # isi_dur + random number between 0 and 0.2
            isi_jittered=isi_dur+randomITI.uniform(0, 0.2)
            thisExp.addData("isi_jittered", isi_jittered)
            text_isi.setText('+')
            # keep track of which components have finished
            ISIComponents = [text_isi]
            for thisComponent in ISIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_isi
                if expInfo['EEG'] and text_isi.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ISI+",label=ISI,duration=float(maint_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ISI+")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ISI+") # fixation marker
                    EYEtriggerSent = True
                
                
                # *text_isi* updates
                
                # if text_isi is starting this frame...
                if text_isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_isi.frameNStart = frameN  # exact frame index
                    text_isi.tStart = t  # local t and not account for scr refresh
                    text_isi.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_isi, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_isi.started')
                    # update status
                    text_isi.status = STARTED
                    text_isi.setAutoDraw(True)
                
                # if text_isi is active this frame...
                if text_isi.status == STARTED:
                    # update params
                    pass
                
                # if text_isi is stopping this frame...
                if text_isi.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_isi.tStartRefresh + isi_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_isi.tStop = t  # not accounting for scr refresh
                        text_isi.tStopRefresh = tThisFlipGlobal  # on global time
                        text_isi.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_isi.stopped')
                        # update status
                        text_isi.status = FINISHED
                        text_isi.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ISI.stopped', globalClock.getTime(format='float'))
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ProbeUpPractice" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ProbeUpPractice.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_probePrac_up
            EEGtriggerSent = False
            EYEtriggerSent = False
            image_probePrac_up_left.setSize(stim_size)
            image_probePrac_up_left.setImage(probe_L)
            image_probePrace_up_right.setSize(stim_size)
            image_probePrace_up_right.setImage(probe_R)
            key_resp_up_prac.keys = []
            key_resp_up_prac.rt = []
            _key_resp_up_prac_allKeys = []
            # keep track of which components have finished
            ProbeUpPracticeComponents = [image_probePrac_up_left, image_probePrace_up_right, key_resp_up_prac]
            for thisComponent in ProbeUpPracticeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ProbeUpPractice" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_probePrac_up
                if expInfo['EEG'] and image_probePrac_up_left.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    #win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_probePrac_up_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,probe_L)
                    win.callOnFlip(el_tracker.sendMessage,probe_R)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_probePrac_up_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,probe_L)
                    win.callOnFlip(tracker.log_message,probe_R)
                    EYEtriggerSent = True
                
                # *image_probePrac_up_left* updates
                
                # if image_probePrac_up_left is starting this frame...
                if image_probePrac_up_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probePrac_up_left.frameNStart = frameN  # exact frame index
                    image_probePrac_up_left.tStart = t  # local t and not account for scr refresh
                    image_probePrac_up_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probePrac_up_left, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probePrac_up_left.started')
                    # update status
                    image_probePrac_up_left.status = STARTED
                    image_probePrac_up_left.setAutoDraw(True)
                
                # if image_probePrac_up_left is active this frame...
                if image_probePrac_up_left.status == STARTED:
                    # update params
                    pass
                
                # if image_probePrac_up_left is stopping this frame...
                if image_probePrac_up_left.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probePrac_up_left.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probePrac_up_left.tStop = t  # not accounting for scr refresh
                        image_probePrac_up_left.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probePrac_up_left.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probePrac_up_left.stopped')
                        # update status
                        image_probePrac_up_left.status = FINISHED
                        image_probePrac_up_left.setAutoDraw(False)
                
                # *image_probePrace_up_right* updates
                
                # if image_probePrace_up_right is starting this frame...
                if image_probePrace_up_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probePrace_up_right.frameNStart = frameN  # exact frame index
                    image_probePrace_up_right.tStart = t  # local t and not account for scr refresh
                    image_probePrace_up_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probePrace_up_right, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probePrace_up_right.started')
                    # update status
                    image_probePrace_up_right.status = STARTED
                    image_probePrace_up_right.setAutoDraw(True)
                
                # if image_probePrace_up_right is active this frame...
                if image_probePrace_up_right.status == STARTED:
                    # update params
                    pass
                
                # if image_probePrace_up_right is stopping this frame...
                if image_probePrace_up_right.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probePrace_up_right.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probePrace_up_right.tStop = t  # not accounting for scr refresh
                        image_probePrace_up_right.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probePrace_up_right.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probePrace_up_right.stopped')
                        # update status
                        image_probePrace_up_right.status = FINISHED
                        image_probePrace_up_right.setAutoDraw(False)
                
                # *key_resp_up_prac* updates
                waitOnFlip = False
                
                # if key_resp_up_prac is starting this frame...
                if key_resp_up_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_up_prac.frameNStart = frameN  # exact frame index
                    key_resp_up_prac.tStart = t  # local t and not account for scr refresh
                    key_resp_up_prac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_up_prac, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_up_prac.started')
                    # update status
                    key_resp_up_prac.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_up_prac.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_up_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp_up_prac is stopping this frame...
                if key_resp_up_prac.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_up_prac.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_up_prac.tStop = t  # not accounting for scr refresh
                        key_resp_up_prac.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_up_prac.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_up_prac.stopped')
                        # update status
                        key_resp_up_prac.status = FINISHED
                        key_resp_up_prac.status = FINISHED
                if key_resp_up_prac.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_up_prac.getKeys(keyList=['1','left','2','right','s'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_up_prac_allKeys.extend(theseKeys)
                    if len(_key_resp_up_prac_allKeys):
                        key_resp_up_prac.keys = _key_resp_up_prac_allKeys[0].name  # just the first key pressed
                        key_resp_up_prac.rt = _key_resp_up_prac_allKeys[0].rt
                        key_resp_up_prac.duration = _key_resp_up_prac_allKeys[0].duration
                        # was this correct?
                        if (key_resp_up_prac.keys == str(correct_resp)) or (key_resp_up_prac.keys == correct_resp):
                            key_resp_up_prac.corr = 1
                        else:
                            key_resp_up_prac.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ProbeUpPracticeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ProbeUpPractice" ---
            for thisComponent in ProbeUpPracticeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ProbeUpPractice.stopped', globalClock.getTime(format='float'))
            # check responses
            if key_resp_up_prac.keys in ['', [], None]:  # No response was made
                key_resp_up_prac.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   key_resp_up_prac.corr = 1;  # correct non-response
                else:
                   key_resp_up_prac.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_practice_up (TrialHandler)
            trials_practice_up.addData('key_resp_up_prac.keys',key_resp_up_prac.keys)
            trials_practice_up.addData('key_resp_up_prac.corr', key_resp_up_prac.corr)
            if key_resp_up_prac.keys != None:  # we had a response
                trials_practice_up.addData('key_resp_up_prac.rt', key_resp_up_prac.rt)
                trials_practice_up.addData('key_resp_up_prac.duration', key_resp_up_prac.duration)
            # the Routine "ProbeUpPractice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ITI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_iti
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # iti_dur + random number between 0 and 0.3
            iti_jittered=iti_dur+randomITI.uniform(0, 0.3)
            thisExp.addData("iti_jittered", iti_jittered)
            text_iti.setText('')
            # keep track of which components have finished
            ITIComponents = [text_iti]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_iti
                if expInfo['EEG'] and text_iti.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ITI+",label="ITI+",duration=float(isi_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ITI")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ITI")
                    EYEtriggerSent = True
                
                # *text_iti* updates
                
                # if text_iti is starting this frame...
                if text_iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_iti.frameNStart = frameN  # exact frame index
                    text_iti.tStart = t  # local t and not account for scr refresh
                    text_iti.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_iti, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_iti.started')
                    # update status
                    text_iti.status = STARTED
                    text_iti.setAutoDraw(True)
                
                # if text_iti is active this frame...
                if text_iti.status == STARTED:
                    # update params
                    pass
                
                # if text_iti is stopping this frame...
                if text_iti.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_iti.tStartRefresh + iti_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_iti.tStop = t  # not accounting for scr refresh
                        text_iti.tStopRefresh = tThisFlipGlobal  # on global time
                        text_iti.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_iti.stopped')
                        # update status
                        text_iti.status = FINISHED
                        text_iti.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ITI.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_iti
            if expInfo['EyeLink']:
                # record trial variables to the EDF data file, for details, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('!V TRIAL_VAR condition %s' % cond)
                el_tracker.sendMessage('!V TRIAL_VAR orientation %s' % orient)
                el_tracker.sendMessage('!V TRIAL_VAR image_target %s' % target_list)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_left %s' % probe_L)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_right %s' % probe_R)
                #el_tracker.sendMessage('!V TRIAL_VAR RT %d' % RT)
                # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials_practice_up'
        
        # get names of stimulus parameters
        if trials_practice_up.trialList in ([], [None], None):
            params = []
        else:
            params = trials_practice_up.trialList[0].keys()
        # save data for this loop
        trials_practice_up.saveAsExcel(filename + '.xlsx', sheetName='trials_practice_up',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trials_practice_up.saveAsText(filename + 'trials_practice_up.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        trials_practice_inv = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(block_list, selection='2:3'),
            seed=None, name='trials_practice_inv')
        thisExp.addLoop(trials_practice_inv)  # add the loop to the experiment
        thisTrials_practice_inv = trials_practice_inv.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice_inv.rgb)
        if thisTrials_practice_inv != None:
            for paramName in thisTrials_practice_inv:
                globals()[paramName] = thisTrials_practice_inv[paramName]
        
        for thisTrials_practice_inv in trials_practice_inv:
            currentLoop = trials_practice_inv
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice_inv.rgb)
            if thisTrials_practice_inv != None:
                for paramName in thisTrials_practice_inv:
                    globals()[paramName] = thisTrials_practice_inv[paramName]
            
            # --- Prepare to start Routine "Fixation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Fixation.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_fixation
            EEGtriggerSent = False
            EYEtriggerSent = False
            trial_index += 1
            
            # log a TRIALID message to mark trial start, before starting to record.
            # EyeLink Data Viewer defines the start of a trial by the TRIALID message.
            if expInfo['EyeLink']:
                el_tracker.sendMessage("TRIALID %d" % trial_index)
            if expInfo['EyeTribe']:
                tracker.log_message("TRIALID %d" % trial_index)
            # keep track of which components have finished
            FixationComponents = [text_fixation]
            for thisComponent in FixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fixation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_fixation
                if expInfo['EEG'] and text_fixation.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event, event_type="FXN+",label="FXN+",duration=float(fix_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"FXN+") # fixation marker
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"FXN+") # fixation marker
                    EYEtriggerSent = True
                
                # *text_fixation* updates
                
                # if text_fixation is starting this frame...
                if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_fixation.frameNStart = frameN  # exact frame index
                    text_fixation.tStart = t  # local t and not account for scr refresh
                    text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.started')
                    # update status
                    text_fixation.status = STARTED
                    text_fixation.setAutoDraw(True)
                
                # if text_fixation is active this frame...
                if text_fixation.status == STARTED:
                    # update params
                    pass
                
                # if text_fixation is stopping this frame...
                if text_fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_fixation.tStartRefresh + fix_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_fixation.tStop = t  # not accounting for scr refresh
                        text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        text_fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                        # update status
                        text_fixation.status = FINISHED
                        text_fixation.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fixation" ---
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Fixation.stopped', globalClock.getTime(format='float'))
            # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "EncodingInverted" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('EncodingInverted.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_encode_inverted
            EEGtriggerSent = False
            EYEtriggerSent = False
            orient = "inverted" # trial categorization
            # Add the variable to a new column in the output file
            thisExp.addData("orient", orient)
            image_target_inverted.setSize(stim_size)
            image_target_inverted.setImage(target_list)
            # keep track of which components have finished
            EncodingInvertedComponents = [image_target_inverted]
            for thisComponent in EncodingInvertedComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EncodingInverted" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_encode_inverted
                if expInfo['EEG'] and image_target_inverted.status == STARTED and not EEGtriggerSent:
                    win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_target_inverted.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,target_list)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_target_inverted.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,target_list)
                    EYEtriggerSent = True
                
                # *image_target_inverted* updates
                
                # if image_target_inverted is starting this frame...
                if image_target_inverted.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_target_inverted.frameNStart = frameN  # exact frame index
                    image_target_inverted.tStart = t  # local t and not account for scr refresh
                    image_target_inverted.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_target_inverted, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_target_inverted.started')
                    # update status
                    image_target_inverted.status = STARTED
                    image_target_inverted.setAutoDraw(True)
                
                # if image_target_inverted is active this frame...
                if image_target_inverted.status == STARTED:
                    # update params
                    pass
                
                # if image_target_inverted is stopping this frame...
                if image_target_inverted.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_target_inverted.tStartRefresh + target_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_target_inverted.tStop = t  # not accounting for scr refresh
                        image_target_inverted.tStopRefresh = tThisFlipGlobal  # on global time
                        image_target_inverted.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_target_inverted.stopped')
                        # update status
                        image_target_inverted.status = FINISHED
                        image_target_inverted.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EncodingInvertedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EncodingInverted" ---
            for thisComponent in EncodingInvertedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('EncodingInverted.stopped', globalClock.getTime(format='float'))
            # the Routine "EncodingInverted" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ISI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ISI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_isi
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # isi_dur + random number between 0 and 0.2
            isi_jittered=isi_dur+randomITI.uniform(0, 0.2)
            thisExp.addData("isi_jittered", isi_jittered)
            text_isi.setText('+')
            # keep track of which components have finished
            ISIComponents = [text_isi]
            for thisComponent in ISIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_isi
                if expInfo['EEG'] and text_isi.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ISI+",label=ISI,duration=float(maint_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ISI+")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ISI+") # fixation marker
                    EYEtriggerSent = True
                
                
                # *text_isi* updates
                
                # if text_isi is starting this frame...
                if text_isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_isi.frameNStart = frameN  # exact frame index
                    text_isi.tStart = t  # local t and not account for scr refresh
                    text_isi.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_isi, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_isi.started')
                    # update status
                    text_isi.status = STARTED
                    text_isi.setAutoDraw(True)
                
                # if text_isi is active this frame...
                if text_isi.status == STARTED:
                    # update params
                    pass
                
                # if text_isi is stopping this frame...
                if text_isi.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_isi.tStartRefresh + isi_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_isi.tStop = t  # not accounting for scr refresh
                        text_isi.tStopRefresh = tThisFlipGlobal  # on global time
                        text_isi.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_isi.stopped')
                        # update status
                        text_isi.status = FINISHED
                        text_isi.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ISI.stopped', globalClock.getTime(format='float'))
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ProbeInvPractice" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ProbeInvPractice.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_probePrac_inv
            EEGtriggerSent = False
            EYEtriggerSent = False
            image_probePrac_inv_left.setSize(stim_size)
            image_probePrac_inv_left.setImage(probe_L)
            image_probePrace_inv_right.setSize(stim_size)
            image_probePrace_inv_right.setImage(probe_R)
            key_resp_inv_prac.keys = []
            key_resp_inv_prac.rt = []
            _key_resp_inv_prac_allKeys = []
            # keep track of which components have finished
            ProbeInvPracticeComponents = [image_probePrac_inv_left, image_probePrace_inv_right, key_resp_inv_prac]
            for thisComponent in ProbeInvPracticeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ProbeInvPractice" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_probePrac_inv
                if expInfo['EEG'] and image_probePrac_inv_left.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    #win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_probePrac_inv_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,probe_L)
                    win.callOnFlip(el_tracker.sendMessage,probe_R)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_probePrac_inv_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,probe_L)
                    win.callOnFlip(tracker.log_message,probe_R)
                    EYEtriggerSent = True
                
                # *image_probePrac_inv_left* updates
                
                # if image_probePrac_inv_left is starting this frame...
                if image_probePrac_inv_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probePrac_inv_left.frameNStart = frameN  # exact frame index
                    image_probePrac_inv_left.tStart = t  # local t and not account for scr refresh
                    image_probePrac_inv_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probePrac_inv_left, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probePrac_inv_left.started')
                    # update status
                    image_probePrac_inv_left.status = STARTED
                    image_probePrac_inv_left.setAutoDraw(True)
                
                # if image_probePrac_inv_left is active this frame...
                if image_probePrac_inv_left.status == STARTED:
                    # update params
                    pass
                
                # if image_probePrac_inv_left is stopping this frame...
                if image_probePrac_inv_left.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probePrac_inv_left.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probePrac_inv_left.tStop = t  # not accounting for scr refresh
                        image_probePrac_inv_left.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probePrac_inv_left.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probePrac_inv_left.stopped')
                        # update status
                        image_probePrac_inv_left.status = FINISHED
                        image_probePrac_inv_left.setAutoDraw(False)
                
                # *image_probePrace_inv_right* updates
                
                # if image_probePrace_inv_right is starting this frame...
                if image_probePrace_inv_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probePrace_inv_right.frameNStart = frameN  # exact frame index
                    image_probePrace_inv_right.tStart = t  # local t and not account for scr refresh
                    image_probePrace_inv_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probePrace_inv_right, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probePrace_inv_right.started')
                    # update status
                    image_probePrace_inv_right.status = STARTED
                    image_probePrace_inv_right.setAutoDraw(True)
                
                # if image_probePrace_inv_right is active this frame...
                if image_probePrace_inv_right.status == STARTED:
                    # update params
                    pass
                
                # if image_probePrace_inv_right is stopping this frame...
                if image_probePrace_inv_right.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probePrace_inv_right.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probePrace_inv_right.tStop = t  # not accounting for scr refresh
                        image_probePrace_inv_right.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probePrace_inv_right.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probePrace_inv_right.stopped')
                        # update status
                        image_probePrace_inv_right.status = FINISHED
                        image_probePrace_inv_right.setAutoDraw(False)
                
                # *key_resp_inv_prac* updates
                waitOnFlip = False
                
                # if key_resp_inv_prac is starting this frame...
                if key_resp_inv_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_inv_prac.frameNStart = frameN  # exact frame index
                    key_resp_inv_prac.tStart = t  # local t and not account for scr refresh
                    key_resp_inv_prac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_inv_prac, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_inv_prac.started')
                    # update status
                    key_resp_inv_prac.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_inv_prac.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_inv_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp_inv_prac is stopping this frame...
                if key_resp_inv_prac.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_inv_prac.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_inv_prac.tStop = t  # not accounting for scr refresh
                        key_resp_inv_prac.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_inv_prac.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_inv_prac.stopped')
                        # update status
                        key_resp_inv_prac.status = FINISHED
                        key_resp_inv_prac.status = FINISHED
                if key_resp_inv_prac.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_inv_prac.getKeys(keyList=['1','left','2','right','s'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_inv_prac_allKeys.extend(theseKeys)
                    if len(_key_resp_inv_prac_allKeys):
                        key_resp_inv_prac.keys = _key_resp_inv_prac_allKeys[0].name  # just the first key pressed
                        key_resp_inv_prac.rt = _key_resp_inv_prac_allKeys[0].rt
                        key_resp_inv_prac.duration = _key_resp_inv_prac_allKeys[0].duration
                        # was this correct?
                        if (key_resp_inv_prac.keys == str(correct_resp)) or (key_resp_inv_prac.keys == correct_resp):
                            key_resp_inv_prac.corr = 1
                        else:
                            key_resp_inv_prac.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ProbeInvPracticeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ProbeInvPractice" ---
            for thisComponent in ProbeInvPracticeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ProbeInvPractice.stopped', globalClock.getTime(format='float'))
            # check responses
            if key_resp_inv_prac.keys in ['', [], None]:  # No response was made
                key_resp_inv_prac.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   key_resp_inv_prac.corr = 1;  # correct non-response
                else:
                   key_resp_inv_prac.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_practice_inv (TrialHandler)
            trials_practice_inv.addData('key_resp_inv_prac.keys',key_resp_inv_prac.keys)
            trials_practice_inv.addData('key_resp_inv_prac.corr', key_resp_inv_prac.corr)
            if key_resp_inv_prac.keys != None:  # we had a response
                trials_practice_inv.addData('key_resp_inv_prac.rt', key_resp_inv_prac.rt)
                trials_practice_inv.addData('key_resp_inv_prac.duration', key_resp_inv_prac.duration)
            # the Routine "ProbeInvPractice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ITI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_iti
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # iti_dur + random number between 0 and 0.3
            iti_jittered=iti_dur+randomITI.uniform(0, 0.3)
            thisExp.addData("iti_jittered", iti_jittered)
            text_iti.setText('')
            # keep track of which components have finished
            ITIComponents = [text_iti]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_iti
                if expInfo['EEG'] and text_iti.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ITI+",label="ITI+",duration=float(isi_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ITI")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ITI")
                    EYEtriggerSent = True
                
                # *text_iti* updates
                
                # if text_iti is starting this frame...
                if text_iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_iti.frameNStart = frameN  # exact frame index
                    text_iti.tStart = t  # local t and not account for scr refresh
                    text_iti.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_iti, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_iti.started')
                    # update status
                    text_iti.status = STARTED
                    text_iti.setAutoDraw(True)
                
                # if text_iti is active this frame...
                if text_iti.status == STARTED:
                    # update params
                    pass
                
                # if text_iti is stopping this frame...
                if text_iti.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_iti.tStartRefresh + iti_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_iti.tStop = t  # not accounting for scr refresh
                        text_iti.tStopRefresh = tThisFlipGlobal  # on global time
                        text_iti.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_iti.stopped')
                        # update status
                        text_iti.status = FINISHED
                        text_iti.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ITI.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_iti
            if expInfo['EyeLink']:
                # record trial variables to the EDF data file, for details, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('!V TRIAL_VAR condition %s' % cond)
                el_tracker.sendMessage('!V TRIAL_VAR orientation %s' % orient)
                el_tracker.sendMessage('!V TRIAL_VAR image_target %s' % target_list)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_left %s' % probe_L)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_right %s' % probe_R)
                #el_tracker.sendMessage('!V TRIAL_VAR RT %d' % RT)
                # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials_practice_inv'
        
        # get names of stimulus parameters
        if trials_practice_inv.trialList in ([], [None], None):
            params = []
        else:
            params = trials_practice_inv.trialList[0].keys()
        # save data for this loop
        trials_practice_inv.saveAsExcel(filename + '.xlsx', sheetName='trials_practice_inv',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trials_practice_inv.saveAsText(filename + 'trials_practice_inv.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
    # completed 1.0 repeats of 'blocks_practice'
    
    
    # --- Prepare to start Routine "FB_Practice" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('FB_Practice.started', globalClock.getTime(format='float'))
    text_Practice.setText(msg + "\n\n Please remember to press the LEFT BUTTON to choose the image on the left, or press the RIGHT BUTTON to choose the image on the right. Try to make your choice as quickly and accurately as possible." + "\n\n Press SPACEBAR to start." )
    key_resp_endPractice.keys = []
    key_resp_endPractice.rt = []
    _key_resp_endPractice_allKeys = []
    # keep track of which components have finished
    FB_PracticeComponents = [text_Practice, key_resp_endPractice]
    for thisComponent in FB_PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "FB_Practice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Practice* updates
        
        # if text_Practice is starting this frame...
        if text_Practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Practice.frameNStart = frameN  # exact frame index
            text_Practice.tStart = t  # local t and not account for scr refresh
            text_Practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Practice, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Practice.status = STARTED
            text_Practice.setAutoDraw(True)
        
        # if text_Practice is active this frame...
        if text_Practice.status == STARTED:
            # update params
            pass
        
        # *key_resp_endPractice* updates
        waitOnFlip = False
        
        # if key_resp_endPractice is starting this frame...
        if key_resp_endPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_endPractice.frameNStart = frameN  # exact frame index
            key_resp_endPractice.tStart = t  # local t and not account for scr refresh
            key_resp_endPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_endPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_endPractice.started')
            # update status
            key_resp_endPractice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_endPractice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_endPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_endPractice.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_endPractice.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_endPractice_allKeys.extend(theseKeys)
            if len(_key_resp_endPractice_allKeys):
                key_resp_endPractice.keys = _key_resp_endPractice_allKeys[-1].name  # just the last key pressed
                key_resp_endPractice.rt = _key_resp_endPractice_allKeys[-1].rt
                key_resp_endPractice.duration = _key_resp_endPractice_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FB_PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FB_Practice" ---
    for thisComponent in FB_PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('FB_Practice.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_endPractice.keys in ['', [], None]:  # No response was made
        key_resp_endPractice.keys = None
    thisExp.addData('key_resp_endPractice.keys',key_resp_endPractice.keys)
    if key_resp_endPractice.keys != None:  # we had a response
        thisExp.addData('key_resp_endPractice.rt', key_resp_endPractice.rt)
        thisExp.addData('key_resp_endPractice.duration', key_resp_endPractice.duration)
    thisExp.nextEntry()
    # the Routine "FB_Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "getReady" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('getReady.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    getReadyComponents = [text_countdown]
    for thisComponent in getReadyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "getReady" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_countdown* updates
        
        # if text_countdown is starting this frame...
        if text_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_countdown.frameNStart = frameN  # exact frame index
            text_countdown.tStart = t  # local t and not account for scr refresh
            text_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_countdown.status = STARTED
            text_countdown.setAutoDraw(True)
        
        # if text_countdown is active this frame...
        if text_countdown.status == STARTED:
            # update params
            text_countdown.setText(str(5-int(t)), log=False)
        
        # if text_countdown is stopping this frame...
        if text_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_countdown.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_countdown.tStop = t  # not accounting for scr refresh
                text_countdown.tStopRefresh = tThisFlipGlobal  # on global time
                text_countdown.frameNStop = frameN  # exact frame index
                # update status
                text_countdown.status = FINISHED
                text_countdown.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in getReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "getReady" ---
    for thisComponent in getReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('getReady.stopped', globalClock.getTime(format='float'))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    blocks_order = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(order_list),
        seed=None, name='blocks_order')
    thisExp.addLoop(blocks_order)  # add the loop to the experiment
    thisBlocks_order = blocks_order.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_order.rgb)
    if thisBlocks_order != None:
        for paramName in thisBlocks_order:
            globals()[paramName] = thisBlocks_order[paramName]
    
    for thisBlocks_order in blocks_order:
        currentLoop = blocks_order
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlocks_order.rgb)
        if thisBlocks_order != None:
            for paramName in thisBlocks_order:
                globals()[paramName] = thisBlocks_order[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_upright = data.TrialHandler(nReps=upright_flag, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(block_list),
            seed=None, name='trials_upright')
        thisExp.addLoop(trials_upright)  # add the loop to the experiment
        thisTrials_upright = trials_upright.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_upright.rgb)
        if thisTrials_upright != None:
            for paramName in thisTrials_upright:
                globals()[paramName] = thisTrials_upright[paramName]
        
        for thisTrials_upright in trials_upright:
            currentLoop = trials_upright
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_upright.rgb)
            if thisTrials_upright != None:
                for paramName in thisTrials_upright:
                    globals()[paramName] = thisTrials_upright[paramName]
            
            # --- Prepare to start Routine "Fixation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Fixation.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_fixation
            EEGtriggerSent = False
            EYEtriggerSent = False
            trial_index += 1
            
            # log a TRIALID message to mark trial start, before starting to record.
            # EyeLink Data Viewer defines the start of a trial by the TRIALID message.
            if expInfo['EyeLink']:
                el_tracker.sendMessage("TRIALID %d" % trial_index)
            if expInfo['EyeTribe']:
                tracker.log_message("TRIALID %d" % trial_index)
            # keep track of which components have finished
            FixationComponents = [text_fixation]
            for thisComponent in FixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fixation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_fixation
                if expInfo['EEG'] and text_fixation.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event, event_type="FXN+",label="FXN+",duration=float(fix_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"FXN+") # fixation marker
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"FXN+") # fixation marker
                    EYEtriggerSent = True
                
                # *text_fixation* updates
                
                # if text_fixation is starting this frame...
                if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_fixation.frameNStart = frameN  # exact frame index
                    text_fixation.tStart = t  # local t and not account for scr refresh
                    text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.started')
                    # update status
                    text_fixation.status = STARTED
                    text_fixation.setAutoDraw(True)
                
                # if text_fixation is active this frame...
                if text_fixation.status == STARTED:
                    # update params
                    pass
                
                # if text_fixation is stopping this frame...
                if text_fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_fixation.tStartRefresh + fix_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_fixation.tStop = t  # not accounting for scr refresh
                        text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        text_fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                        # update status
                        text_fixation.status = FINISHED
                        text_fixation.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fixation" ---
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Fixation.stopped', globalClock.getTime(format='float'))
            # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "EncodingUpright" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('EncodingUpright.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_encode_upright
            EEGtriggerSent = False
            EYEtriggerSent = False
            orient = "upright" # trial categorization 
            # Add the variable to a new column in the output file
            thisExp.addData("orient", orient)
            image_target_upright.setSize(stim_size)
            image_target_upright.setImage(target_list)
            # keep track of which components have finished
            EncodingUprightComponents = [image_target_upright]
            for thisComponent in EncodingUprightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EncodingUpright" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_encode_upright
                if expInfo['EEG'] and image_target_upright.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_target_upright.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,target_list)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_target_upright.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,target_list)
                    EYEtriggerSent = True
                
                # *image_target_upright* updates
                
                # if image_target_upright is starting this frame...
                if image_target_upright.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_target_upright.frameNStart = frameN  # exact frame index
                    image_target_upright.tStart = t  # local t and not account for scr refresh
                    image_target_upright.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_target_upright, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_target_upright.started')
                    # update status
                    image_target_upright.status = STARTED
                    image_target_upright.setAutoDraw(True)
                
                # if image_target_upright is active this frame...
                if image_target_upright.status == STARTED:
                    # update params
                    pass
                
                # if image_target_upright is stopping this frame...
                if image_target_upright.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_target_upright.tStartRefresh + target_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_target_upright.tStop = t  # not accounting for scr refresh
                        image_target_upright.tStopRefresh = tThisFlipGlobal  # on global time
                        image_target_upright.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_target_upright.stopped')
                        # update status
                        image_target_upright.status = FINISHED
                        image_target_upright.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EncodingUprightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EncodingUpright" ---
            for thisComponent in EncodingUprightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('EncodingUpright.stopped', globalClock.getTime(format='float'))
            # the Routine "EncodingUpright" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ISI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ISI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_isi
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # isi_dur + random number between 0 and 0.2
            isi_jittered=isi_dur+randomITI.uniform(0, 0.2)
            thisExp.addData("isi_jittered", isi_jittered)
            text_isi.setText('+')
            # keep track of which components have finished
            ISIComponents = [text_isi]
            for thisComponent in ISIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_isi
                if expInfo['EEG'] and text_isi.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ISI+",label=ISI,duration=float(maint_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ISI+")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ISI+") # fixation marker
                    EYEtriggerSent = True
                
                
                # *text_isi* updates
                
                # if text_isi is starting this frame...
                if text_isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_isi.frameNStart = frameN  # exact frame index
                    text_isi.tStart = t  # local t and not account for scr refresh
                    text_isi.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_isi, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_isi.started')
                    # update status
                    text_isi.status = STARTED
                    text_isi.setAutoDraw(True)
                
                # if text_isi is active this frame...
                if text_isi.status == STARTED:
                    # update params
                    pass
                
                # if text_isi is stopping this frame...
                if text_isi.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_isi.tStartRefresh + isi_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_isi.tStop = t  # not accounting for scr refresh
                        text_isi.tStopRefresh = tThisFlipGlobal  # on global time
                        text_isi.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_isi.stopped')
                        # update status
                        text_isi.status = FINISHED
                        text_isi.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ISI.stopped', globalClock.getTime(format='float'))
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ProbeUpright" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ProbeUpright.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_probe_upright
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            EEGrspprobe=0
            EYErspprobe=0
            image_probe_upright_left.setSize(stim_size)
            image_probe_upright_left.setImage(probe_L)
            image_probe_upright_right.setSize(stim_size)
            image_probe_upright_right.setImage(probe_R)
            key_resp_upright.keys = []
            key_resp_upright.rt = []
            _key_resp_upright_allKeys = []
            # keep track of which components have finished
            ProbeUprightComponents = [image_probe_upright_left, image_probe_upright_right, key_resp_upright]
            for thisComponent in ProbeUprightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ProbeUpright" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_probe_upright
                if expInfo['EEG'] and image_probe_upright_left.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="PRB+",label=PRB,duration=float(probe_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_probe_upright_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,probe_L)
                    win.callOnFlip(el_tracker.sendMessage,probe_R)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_probe_upright_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,probe_L)
                    win.callOnFlip(tracker.log_message,probe_R)
                    EYEtriggerSent = True
                
                ## Look for Key Response
                if key_resp_upright:
                    if key_resp_upright.keys=='1':
                        if expInfo['EEG'] and EEGrspprobe==0:
                            #ns.send_event(event_type="RESP",label="RSPL")
                            EEGrspprobe=1
                        if expInfo['EyeLink'] and EYErspprobe==0:
                            win.callOnFlip(el_tracker.sendMessage,'RSPL')
                            EYErspprobe=1
                        if expInfo['EyeTribe'] and EYErspprobe==0:
                            win.callOnFlip(tracker.log_message,'RSPL')
                            EYErspprobe=1
                    elif key_resp_upright.keys=='2':
                        if expInfo['EEG'] and EEGrspprobe==0:
                            #ns.send_event(event_type="RESP",label="RSPR")
                            EEGrspprobe=1
                        if expInfo['EyeLink'] and EYErspprobe==0:
                            win.callOnFlip(el_tracker.sendMessage,'RSPR')
                            EYErspprobe=1
                        if expInfo['EyeTribe'] and EYErspprobe==0:
                            win.callOnFlip(tracker.log_message,'RSPR')
                            EYErspprobe=1
                
                # *image_probe_upright_left* updates
                
                # if image_probe_upright_left is starting this frame...
                if image_probe_upright_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probe_upright_left.frameNStart = frameN  # exact frame index
                    image_probe_upright_left.tStart = t  # local t and not account for scr refresh
                    image_probe_upright_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probe_upright_left, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probe_upright_left.started')
                    # update status
                    image_probe_upright_left.status = STARTED
                    image_probe_upright_left.setAutoDraw(True)
                
                # if image_probe_upright_left is active this frame...
                if image_probe_upright_left.status == STARTED:
                    # update params
                    pass
                
                # if image_probe_upright_left is stopping this frame...
                if image_probe_upright_left.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probe_upright_left.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probe_upright_left.tStop = t  # not accounting for scr refresh
                        image_probe_upright_left.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probe_upright_left.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probe_upright_left.stopped')
                        # update status
                        image_probe_upright_left.status = FINISHED
                        image_probe_upright_left.setAutoDraw(False)
                
                # *image_probe_upright_right* updates
                
                # if image_probe_upright_right is starting this frame...
                if image_probe_upright_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probe_upright_right.frameNStart = frameN  # exact frame index
                    image_probe_upright_right.tStart = t  # local t and not account for scr refresh
                    image_probe_upright_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probe_upright_right, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probe_upright_right.started')
                    # update status
                    image_probe_upright_right.status = STARTED
                    image_probe_upright_right.setAutoDraw(True)
                
                # if image_probe_upright_right is active this frame...
                if image_probe_upright_right.status == STARTED:
                    # update params
                    pass
                
                # if image_probe_upright_right is stopping this frame...
                if image_probe_upright_right.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probe_upright_right.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probe_upright_right.tStop = t  # not accounting for scr refresh
                        image_probe_upright_right.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probe_upright_right.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probe_upright_right.stopped')
                        # update status
                        image_probe_upright_right.status = FINISHED
                        image_probe_upright_right.setAutoDraw(False)
                
                # *key_resp_upright* updates
                waitOnFlip = False
                
                # if key_resp_upright is starting this frame...
                if key_resp_upright.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_upright.frameNStart = frameN  # exact frame index
                    key_resp_upright.tStart = t  # local t and not account for scr refresh
                    key_resp_upright.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_upright, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_upright.started')
                    # update status
                    key_resp_upright.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_upright.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_upright.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp_upright is stopping this frame...
                if key_resp_upright.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_upright.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_upright.tStop = t  # not accounting for scr refresh
                        key_resp_upright.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_upright.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_upright.stopped')
                        # update status
                        key_resp_upright.status = FINISHED
                        key_resp_upright.status = FINISHED
                if key_resp_upright.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_upright.getKeys(keyList=['1','left','2','right','s'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_upright_allKeys.extend(theseKeys)
                    if len(_key_resp_upright_allKeys):
                        key_resp_upright.keys = _key_resp_upright_allKeys[0].name  # just the first key pressed
                        key_resp_upright.rt = _key_resp_upright_allKeys[0].rt
                        key_resp_upright.duration = _key_resp_upright_allKeys[0].duration
                        # was this correct?
                        if (key_resp_upright.keys == str(correct_resp)) or (key_resp_upright.keys == correct_resp):
                            key_resp_upright.corr = 1
                        else:
                            key_resp_upright.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ProbeUprightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ProbeUpright" ---
            for thisComponent in ProbeUprightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ProbeUpright.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_probe_upright
            if expInfo['EEG'] and rspprobe==0:
                #ns.send_event(event_type="RESP",label="MISS")
                EEGrspprobe=1
            if expInfo['EyeLink'] and rspprobe==0:
                win.callOnFlip(el_tracker.sendMessage,'MISS')
                EYErspprobe=1
            if expInfo['EyeTribe'] and rspprobe==0:
                win.callOnFlip(tracker.log_message,'MISS')
                EYErspprobe=1
            # check responses
            if key_resp_upright.keys in ['', [], None]:  # No response was made
                key_resp_upright.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   key_resp_upright.corr = 1;  # correct non-response
                else:
                   key_resp_upright.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_upright (TrialHandler)
            trials_upright.addData('key_resp_upright.keys',key_resp_upright.keys)
            trials_upright.addData('key_resp_upright.corr', key_resp_upright.corr)
            if key_resp_upright.keys != None:  # we had a response
                trials_upright.addData('key_resp_upright.rt', key_resp_upright.rt)
                trials_upright.addData('key_resp_upright.duration', key_resp_upright.duration)
            # the Routine "ProbeUpright" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ITI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_iti
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # iti_dur + random number between 0 and 0.3
            iti_jittered=iti_dur+randomITI.uniform(0, 0.3)
            thisExp.addData("iti_jittered", iti_jittered)
            text_iti.setText('')
            # keep track of which components have finished
            ITIComponents = [text_iti]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_iti
                if expInfo['EEG'] and text_iti.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ITI+",label="ITI+",duration=float(isi_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ITI")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ITI")
                    EYEtriggerSent = True
                
                # *text_iti* updates
                
                # if text_iti is starting this frame...
                if text_iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_iti.frameNStart = frameN  # exact frame index
                    text_iti.tStart = t  # local t and not account for scr refresh
                    text_iti.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_iti, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_iti.started')
                    # update status
                    text_iti.status = STARTED
                    text_iti.setAutoDraw(True)
                
                # if text_iti is active this frame...
                if text_iti.status == STARTED:
                    # update params
                    pass
                
                # if text_iti is stopping this frame...
                if text_iti.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_iti.tStartRefresh + iti_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_iti.tStop = t  # not accounting for scr refresh
                        text_iti.tStopRefresh = tThisFlipGlobal  # on global time
                        text_iti.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_iti.stopped')
                        # update status
                        text_iti.status = FINISHED
                        text_iti.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ITI.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_iti
            if expInfo['EyeLink']:
                # record trial variables to the EDF data file, for details, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('!V TRIAL_VAR condition %s' % cond)
                el_tracker.sendMessage('!V TRIAL_VAR orientation %s' % orient)
                el_tracker.sendMessage('!V TRIAL_VAR image_target %s' % target_list)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_left %s' % probe_L)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_right %s' % probe_R)
                #el_tracker.sendMessage('!V TRIAL_VAR RT %d' % RT)
                # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed upright_flag repeats of 'trials_upright'
        
        # get names of stimulus parameters
        if trials_upright.trialList in ([], [None], None):
            params = []
        else:
            params = trials_upright.trialList[0].keys()
        # save data for this loop
        trials_upright.saveAsExcel(filename + '.xlsx', sheetName='trials_upright',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trials_upright.saveAsText(filename + 'trials_upright.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        trials_inverted = data.TrialHandler(nReps=inverted_flag, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(block_list),
            seed=None, name='trials_inverted')
        thisExp.addLoop(trials_inverted)  # add the loop to the experiment
        thisTrials_inverted = trials_inverted.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_inverted.rgb)
        if thisTrials_inverted != None:
            for paramName in thisTrials_inverted:
                globals()[paramName] = thisTrials_inverted[paramName]
        
        for thisTrials_inverted in trials_inverted:
            currentLoop = trials_inverted
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_inverted.rgb)
            if thisTrials_inverted != None:
                for paramName in thisTrials_inverted:
                    globals()[paramName] = thisTrials_inverted[paramName]
            
            # --- Prepare to start Routine "Fixation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Fixation.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_fixation
            EEGtriggerSent = False
            EYEtriggerSent = False
            trial_index += 1
            
            # log a TRIALID message to mark trial start, before starting to record.
            # EyeLink Data Viewer defines the start of a trial by the TRIALID message.
            if expInfo['EyeLink']:
                el_tracker.sendMessage("TRIALID %d" % trial_index)
            if expInfo['EyeTribe']:
                tracker.log_message("TRIALID %d" % trial_index)
            # keep track of which components have finished
            FixationComponents = [text_fixation]
            for thisComponent in FixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fixation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_fixation
                if expInfo['EEG'] and text_fixation.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event, event_type="FXN+",label="FXN+",duration=float(fix_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"FXN+") # fixation marker
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_fixation.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"FXN+") # fixation marker
                    EYEtriggerSent = True
                
                # *text_fixation* updates
                
                # if text_fixation is starting this frame...
                if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_fixation.frameNStart = frameN  # exact frame index
                    text_fixation.tStart = t  # local t and not account for scr refresh
                    text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.started')
                    # update status
                    text_fixation.status = STARTED
                    text_fixation.setAutoDraw(True)
                
                # if text_fixation is active this frame...
                if text_fixation.status == STARTED:
                    # update params
                    pass
                
                # if text_fixation is stopping this frame...
                if text_fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_fixation.tStartRefresh + fix_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_fixation.tStop = t  # not accounting for scr refresh
                        text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        text_fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                        # update status
                        text_fixation.status = FINISHED
                        text_fixation.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fixation" ---
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Fixation.stopped', globalClock.getTime(format='float'))
            # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "EncodingInverted" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('EncodingInverted.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_encode_inverted
            EEGtriggerSent = False
            EYEtriggerSent = False
            orient = "inverted" # trial categorization
            # Add the variable to a new column in the output file
            thisExp.addData("orient", orient)
            image_target_inverted.setSize(stim_size)
            image_target_inverted.setImage(target_list)
            # keep track of which components have finished
            EncodingInvertedComponents = [image_target_inverted]
            for thisComponent in EncodingInvertedComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EncodingInverted" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_encode_inverted
                if expInfo['EEG'] and image_target_inverted.status == STARTED and not EEGtriggerSent:
                    win.callOnFlip(ns.send_event,event_type="STIM",label=TRG,duration=float(target_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_target_inverted.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,target_list)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_target_inverted.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,target_list)
                    EYEtriggerSent = True
                
                # *image_target_inverted* updates
                
                # if image_target_inverted is starting this frame...
                if image_target_inverted.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_target_inverted.frameNStart = frameN  # exact frame index
                    image_target_inverted.tStart = t  # local t and not account for scr refresh
                    image_target_inverted.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_target_inverted, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_target_inverted.started')
                    # update status
                    image_target_inverted.status = STARTED
                    image_target_inverted.setAutoDraw(True)
                
                # if image_target_inverted is active this frame...
                if image_target_inverted.status == STARTED:
                    # update params
                    pass
                
                # if image_target_inverted is stopping this frame...
                if image_target_inverted.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_target_inverted.tStartRefresh + target_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_target_inverted.tStop = t  # not accounting for scr refresh
                        image_target_inverted.tStopRefresh = tThisFlipGlobal  # on global time
                        image_target_inverted.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_target_inverted.stopped')
                        # update status
                        image_target_inverted.status = FINISHED
                        image_target_inverted.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EncodingInvertedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EncodingInverted" ---
            for thisComponent in EncodingInvertedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('EncodingInverted.stopped', globalClock.getTime(format='float'))
            # the Routine "EncodingInverted" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ISI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ISI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_isi
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # isi_dur + random number between 0 and 0.2
            isi_jittered=isi_dur+randomITI.uniform(0, 0.2)
            thisExp.addData("isi_jittered", isi_jittered)
            text_isi.setText('+')
            # keep track of which components have finished
            ISIComponents = [text_isi]
            for thisComponent in ISIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_isi
                if expInfo['EEG'] and text_isi.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ISI+",label=ISI,duration=float(maint_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ISI+")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_isi.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ISI+") # fixation marker
                    EYEtriggerSent = True
                
                
                # *text_isi* updates
                
                # if text_isi is starting this frame...
                if text_isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_isi.frameNStart = frameN  # exact frame index
                    text_isi.tStart = t  # local t and not account for scr refresh
                    text_isi.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_isi, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_isi.started')
                    # update status
                    text_isi.status = STARTED
                    text_isi.setAutoDraw(True)
                
                # if text_isi is active this frame...
                if text_isi.status == STARTED:
                    # update params
                    pass
                
                # if text_isi is stopping this frame...
                if text_isi.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_isi.tStartRefresh + isi_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_isi.tStop = t  # not accounting for scr refresh
                        text_isi.tStopRefresh = tThisFlipGlobal  # on global time
                        text_isi.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_isi.stopped')
                        # update status
                        text_isi.status = FINISHED
                        text_isi.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ISI.stopped', globalClock.getTime(format='float'))
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ProbeInverted" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ProbeInverted.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_probe_inverted
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            EEGrspprobe=0
            EYErspprobe=0
            image_probe_inverted_left.setSize(stim_size)
            image_probe_inverted_left.setImage(probe_L)
            image_probe_inverted_right.setSize(stim_size)
            image_probe_inverted_right.setImage(probe_R)
            key_resp_inverted.keys = []
            key_resp_inverted.rt = []
            _key_resp_inverted_allKeys = []
            # keep track of which components have finished
            ProbeInvertedComponents = [image_probe_inverted_left, image_probe_inverted_right, key_resp_inverted]
            for thisComponent in ProbeInvertedComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ProbeInverted" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_probe_inverted
                if expInfo['EEG'] and image_probe_inverted_left.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="PRB+",label=PRB,duration=float(probe_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and image_probe_inverted_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,probe_L)
                    win.callOnFlip(el_tracker.sendMessage,probe_R)
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and image_probe_inverted_left.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,probe_L)
                    win.callOnFlip(tracker.log_message,probe_R)
                    EYEtriggerSent = True
                
                ## Look for Key Response
                if key_resp_inverted:
                    if key_resp_inverted.keys=='1':
                        if expInfo['EEG'] and EEGrspprobe==0:
                            #ns.send_event(event_type="RESP",label="RSPL")
                            EEGrspprobe=1
                        if expInfo['EyeLink'] and EYErspprobe==0:
                            win.callOnFlip(el_tracker.sendMessage,'RSPL')
                            EYErspprobe=1
                        if expInfo['EyeTribe'] and EYErspprobe==0:
                            win.callOnFlip(tracker.log_message,'RSPL')
                            EYErspprobe=1
                    elif key_resp_inverted.keys=='2':
                        if expInfo['EEG'] and EEGrspprobe==0:
                            ns.send_event(event_type="RESP",label="RSPR")
                            EEGrspprobe=1
                        if expInfo['EyeLink'] and EYErspprobe==0:
                            win.callOnFlip(el_tracker.sendMessage,'RSPR')
                            EYErspprobe=1
                        if expInfo['EyeTribe'] and EYErspprobe==0:
                            win.callOnFlip(tracker.log_message,'RSPR')
                            EYErspprobe=1
                
                # *image_probe_inverted_left* updates
                
                # if image_probe_inverted_left is starting this frame...
                if image_probe_inverted_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probe_inverted_left.frameNStart = frameN  # exact frame index
                    image_probe_inverted_left.tStart = t  # local t and not account for scr refresh
                    image_probe_inverted_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probe_inverted_left, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probe_inverted_left.started')
                    # update status
                    image_probe_inverted_left.status = STARTED
                    image_probe_inverted_left.setAutoDraw(True)
                
                # if image_probe_inverted_left is active this frame...
                if image_probe_inverted_left.status == STARTED:
                    # update params
                    pass
                
                # if image_probe_inverted_left is stopping this frame...
                if image_probe_inverted_left.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probe_inverted_left.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probe_inverted_left.tStop = t  # not accounting for scr refresh
                        image_probe_inverted_left.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probe_inverted_left.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probe_inverted_left.stopped')
                        # update status
                        image_probe_inverted_left.status = FINISHED
                        image_probe_inverted_left.setAutoDraw(False)
                
                # *image_probe_inverted_right* updates
                
                # if image_probe_inverted_right is starting this frame...
                if image_probe_inverted_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_probe_inverted_right.frameNStart = frameN  # exact frame index
                    image_probe_inverted_right.tStart = t  # local t and not account for scr refresh
                    image_probe_inverted_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_probe_inverted_right, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_probe_inverted_right.started')
                    # update status
                    image_probe_inverted_right.status = STARTED
                    image_probe_inverted_right.setAutoDraw(True)
                
                # if image_probe_inverted_right is active this frame...
                if image_probe_inverted_right.status == STARTED:
                    # update params
                    pass
                
                # if image_probe_inverted_right is stopping this frame...
                if image_probe_inverted_right.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_probe_inverted_right.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        image_probe_inverted_right.tStop = t  # not accounting for scr refresh
                        image_probe_inverted_right.tStopRefresh = tThisFlipGlobal  # on global time
                        image_probe_inverted_right.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_probe_inverted_right.stopped')
                        # update status
                        image_probe_inverted_right.status = FINISHED
                        image_probe_inverted_right.setAutoDraw(False)
                
                # *key_resp_inverted* updates
                waitOnFlip = False
                
                # if key_resp_inverted is starting this frame...
                if key_resp_inverted.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_inverted.frameNStart = frameN  # exact frame index
                    key_resp_inverted.tStart = t  # local t and not account for scr refresh
                    key_resp_inverted.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_inverted, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_inverted.started')
                    # update status
                    key_resp_inverted.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_inverted.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_inverted.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp_inverted is stopping this frame...
                if key_resp_inverted.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_inverted.tStartRefresh + probe_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_inverted.tStop = t  # not accounting for scr refresh
                        key_resp_inverted.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_inverted.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_inverted.stopped')
                        # update status
                        key_resp_inverted.status = FINISHED
                        key_resp_inverted.status = FINISHED
                if key_resp_inverted.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_inverted.getKeys(keyList=['1','left','2','right','s'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_inverted_allKeys.extend(theseKeys)
                    if len(_key_resp_inverted_allKeys):
                        key_resp_inverted.keys = _key_resp_inverted_allKeys[0].name  # just the first key pressed
                        key_resp_inverted.rt = _key_resp_inverted_allKeys[0].rt
                        key_resp_inverted.duration = _key_resp_inverted_allKeys[0].duration
                        # was this correct?
                        if (key_resp_inverted.keys == str(correct_resp)) or (key_resp_inverted.keys == correct_resp):
                            key_resp_inverted.corr = 1
                        else:
                            key_resp_inverted.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ProbeInvertedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ProbeInverted" ---
            for thisComponent in ProbeInvertedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ProbeInverted.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_probe_inverted
            if expInfo['EEG'] and rspprobe==0:
                #ns.send_event(event_type="RESP",label="MISS")
                EEGrspprobe=1
            if expInfo['EyeLink'] and rspprobe==0:
                win.callOnFlip(el_tracker.sendMessage,'MISS')
                EYErspprobe=1
            if expInfo['EyeTribe'] and rspprobe==0:
                win.callOnFlip(tracker.log_message,'MISS')
                EYErspprobe=1
            # check responses
            if key_resp_inverted.keys in ['', [], None]:  # No response was made
                key_resp_inverted.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   key_resp_inverted.corr = 1;  # correct non-response
                else:
                   key_resp_inverted.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_inverted (TrialHandler)
            trials_inverted.addData('key_resp_inverted.keys',key_resp_inverted.keys)
            trials_inverted.addData('key_resp_inverted.corr', key_resp_inverted.corr)
            if key_resp_inverted.keys != None:  # we had a response
                trials_inverted.addData('key_resp_inverted.rt', key_resp_inverted.rt)
                trials_inverted.addData('key_resp_inverted.duration', key_resp_inverted.duration)
            # the Routine "ProbeInverted" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ITI.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_iti
            EEGtriggerSent = False
            EYEtriggerSent = False
            
            # iti_dur + random number between 0 and 0.3
            iti_jittered=iti_dur+randomITI.uniform(0, 0.3)
            thisExp.addData("iti_jittered", iti_jittered)
            text_iti.setText('')
            # keep track of which components have finished
            ITIComponents = [text_iti]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_iti
                if expInfo['EEG'] and text_iti.status == STARTED and not EEGtriggerSent:
                    #win.callOnFlip(ns.send_event,event_type="ITI+",label="ITI+",duration=float(isi_dur)) #Send the trigger, synced to the screen refresh
                    EEGtriggerSent = True
                if expInfo['EyeLink'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(el_tracker.sendMessage,"ITI")
                    EYEtriggerSent = True
                if expInfo['EyeTribe'] and text_iti.status == STARTED and not EYEtriggerSent:
                    win.callOnFlip(tracker.log_message,"ITI")
                    EYEtriggerSent = True
                
                # *text_iti* updates
                
                # if text_iti is starting this frame...
                if text_iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_iti.frameNStart = frameN  # exact frame index
                    text_iti.tStart = t  # local t and not account for scr refresh
                    text_iti.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_iti, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_iti.started')
                    # update status
                    text_iti.status = STARTED
                    text_iti.setAutoDraw(True)
                
                # if text_iti is active this frame...
                if text_iti.status == STARTED:
                    # update params
                    pass
                
                # if text_iti is stopping this frame...
                if text_iti.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_iti.tStartRefresh + iti_jittered-frameTolerance:
                        # keep track of stop time/frame for later
                        text_iti.tStop = t  # not accounting for scr refresh
                        text_iti.tStopRefresh = tThisFlipGlobal  # on global time
                        text_iti.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_iti.stopped')
                        # update status
                        text_iti.status = FINISHED
                        text_iti.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ITI.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_iti
            if expInfo['EyeLink']:
                # record trial variables to the EDF data file, for details, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('!V TRIAL_VAR condition %s' % cond)
                el_tracker.sendMessage('!V TRIAL_VAR orientation %s' % orient)
                el_tracker.sendMessage('!V TRIAL_VAR image_target %s' % target_list)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_left %s' % probe_L)
                el_tracker.sendMessage('!V TRIAL_VAR image_probe_right %s' % probe_R)
                #el_tracker.sendMessage('!V TRIAL_VAR RT %d' % RT)
                # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
                # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
                el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed inverted_flag repeats of 'trials_inverted'
        
        # get names of stimulus parameters
        if trials_inverted.trialList in ([], [None], None):
            params = []
        else:
            params = trials_inverted.trialList[0].keys()
        # save data for this loop
        trials_inverted.saveAsExcel(filename + '.xlsx', sheetName='trials_inverted',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trials_inverted.saveAsText(filename + 'trials_inverted.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "IBI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('IBI.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        IBIComponents = [text_ibi]
        for thisComponent in IBIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "IBI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_ibi* updates
            
            # if text_ibi is starting this frame...
            if text_ibi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_ibi.frameNStart = frameN  # exact frame index
                text_ibi.tStart = t  # local t and not account for scr refresh
                text_ibi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_ibi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_ibi.started')
                # update status
                text_ibi.status = STARTED
                text_ibi.setAutoDraw(True)
            
            # if text_ibi is active this frame...
            if text_ibi.status == STARTED:
                # update params
                pass
            
            # if text_ibi is stopping this frame...
            if text_ibi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_ibi.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_ibi.tStop = t  # not accounting for scr refresh
                    text_ibi.tStopRefresh = tThisFlipGlobal  # on global time
                    text_ibi.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_ibi.stopped')
                    # update status
                    text_ibi.status = FINISHED
                    text_ibi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IBIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "IBI" ---
        for thisComponent in IBIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('IBI.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
    # completed 1.0 repeats of 'blocks_order'
    
    
    # --- Prepare to start Routine "ThankYou" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ThankYou.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    ThankYouComponents = [text_thanks]
    for thisComponent in ThankYouComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ThankYou" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_thanks* updates
        
        # if text_thanks is starting this frame...
        if text_thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_thanks.frameNStart = frameN  # exact frame index
            text_thanks.tStart = t  # local t and not account for scr refresh
            text_thanks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_thanks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_thanks.started')
            # update status
            text_thanks.status = STARTED
            text_thanks.setAutoDraw(True)
        
        # if text_thanks is active this frame...
        if text_thanks.status == STARTED:
            # update params
            pass
        
        # if text_thanks is stopping this frame...
        if text_thanks.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_thanks.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_thanks.tStop = t  # not accounting for scr refresh
                text_thanks.tStopRefresh = tThisFlipGlobal  # on global time
                text_thanks.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_thanks.stopped')
                # update status
                text_thanks.status = FINISHED
                text_thanks.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYouComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ThankYou" ---
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ThankYou.stopped', globalClock.getTime(format='float'))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    # Run 'End Experiment' code from EyelinkCode
    if expInfo['EyeLink']:
        # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
        el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
    
        # stop recording; add 100 msec to catch final events before stopping
        pylink.pumpDelay(100)
        el_tracker.stopRecording()
    
        terminate_task() # EyeLink exit
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
