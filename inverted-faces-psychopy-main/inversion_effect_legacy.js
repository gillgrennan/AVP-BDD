/************************* 
 * Inversion_Effect *
 *************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.1.0.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'inversion_effect';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '',
    'order': [1, 2, 3, 4],
    'EEG': false,
    'EyeLink': false,
    'EyeTribe': false,
    'Calibrate': false,
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(StartRoutineBegin());
flowScheduler.add(StartRoutineEachFrame());
flowScheduler.add(StartRoutineEnd());
flowScheduler.add(instrPracticeRoutineBegin());
flowScheduler.add(instrPracticeRoutineEachFrame());
flowScheduler.add(instrPracticeRoutineEnd());
const blocks_practiceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocks_practiceLoopBegin(blocks_practiceLoopScheduler));
flowScheduler.add(blocks_practiceLoopScheduler);
flowScheduler.add(blocks_practiceLoopEnd);
















flowScheduler.add(FB_PracticeRoutineBegin());
flowScheduler.add(FB_PracticeRoutineEachFrame());
flowScheduler.add(FB_PracticeRoutineEnd());
flowScheduler.add(getReadyRoutineBegin());
flowScheduler.add(getReadyRoutineEachFrame());
flowScheduler.add(getReadyRoutineEnd());
const blocks_orderLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocks_orderLoopBegin(blocks_orderLoopScheduler));
flowScheduler.add(blocks_orderLoopScheduler);
flowScheduler.add(blocks_orderLoopEnd);
















flowScheduler.add(ThankYouRoutineBegin());
flowScheduler.add(ThankYouRoutineEachFrame());
flowScheduler.add(ThankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stimuli/practice_blockList.csv', 'path': 'stimuli/practice_blockList.csv'},
    {'name': 'stimuli/practice_stimuli.csv', 'path': 'stimuli/practice_stimuli.csv'},
    {'name': 'stimuli/inverted_faces/M125.png', 'path': 'stimuli/inverted_faces/M125.png'},
    {'name': 'stimuli/inverted_faces/M125morph.png', 'path': 'stimuli/inverted_faces/M125morph.png'},
    {'name': 'stimuli/inverted_faces/M128.png', 'path': 'stimuli/inverted_faces/M128.png'},
    {'name': 'stimuli/inverted_faces/M128morph.png', 'path': 'stimuli/inverted_faces/M128morph.png'},
    {'name': 'stimuli/inverted_faces/F10.png', 'path': 'stimuli/inverted_faces/F10.png'},
    {'name': 'stimuli/inverted_faces/F10morph.png', 'path': 'stimuli/inverted_faces/F10morph.png'},
    {'name': 'stimuli/inverted_faces/F12.png', 'path': 'stimuli/inverted_faces/F12.png'},
    {'name': 'stimuli/inverted_faces/F12morph.png', 'path': 'stimuli/inverted_faces/F12morph.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.0';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/sub-${expInfo["participant"]}_task-${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var StartClock;
var instrPracticeClock;
var text_practice;
var key_resp_practice;
var getReadyClock;
var text_countdown;
var FixationClock;
var text_fixation;
var EncodingUprightClock;
var image_target_upright;
var ISIClock;
var text_isi;
var ProbeUpPracticeClock;
var image_probePrac_up_left;
var image_probePrace_up_right;
var key_resp_up_prac;
var ITIClock;
var text_iti;
var EncodingInvertedClock;
var image_target_inverted;
var ProbeInvPracticeClock;
var image_probePrac_inv_left;
var image_probePrace_inv_right;
var key_resp_inv_prac;
var FB_PracticeClock;
var text_Practice;
var key_resp_endPractice;
var ProbeUprightClock;
var image_probe_upright_left;
var image_probe_upright_right;
var key_resp_upright;
var ProbeInvertedClock;
var image_probe_inverted_left;
var image_probe_inverted_right;
var key_resp_inverted;
var IBIClock;
var text_ibi;
var ThankYouClock;
var text_thanks;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  // Initialize components for Routine "instrPractice"
  instrPracticeClock = new util.Clock();
  text_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_practice',
    text: ((("In this task, you will see images of faces." + "\n During each trial, one image will flash before you\u2014this is the target image. Afterward, two images will appear side by side. Your task is to select the image that looks exactly like the target image.") + "\n\n Please press the LEFT BUTTON to choose the image on the left, or press the RIGHT BUTTON to choose the image on the right. Try to make your choice as quickly and accurately as possible.") + "\n\n Press SPACEBAR to practice."),
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: 1.8, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_practice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "getReady"
  getReadyClock = new util.Clock();
  text_countdown = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_countdown',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Fixation"
  FixationClock = new util.Clock();
  text_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "EncodingUpright"
  EncodingUprightClock = new util.Clock();
  image_target_upright = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_target_upright', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  text_isi = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_isi',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ProbeUpPractice"
  ProbeUpPracticeClock = new util.Clock();
  image_probePrac_up_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probePrac_up_left', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [(- 0.2), 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_probePrace_up_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probePrace_up_right', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0.2, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  key_resp_up_prac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  text_iti = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_iti',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "EncodingInverted"
  EncodingInvertedClock = new util.Clock();
  image_target_inverted = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_target_inverted', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : true,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "ProbeInvPractice"
  ProbeInvPracticeClock = new util.Clock();
  image_probePrac_inv_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probePrac_inv_left', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [(- 0.2), 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : true,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_probePrace_inv_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probePrace_inv_right', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0.2, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : true,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  key_resp_inv_prac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FB_Practice"
  FB_PracticeClock = new util.Clock();
  text_Practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Practice',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.05], height: 0.06,  wrapWidth: 1.8, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_endPractice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ProbeUpright"
  ProbeUprightClock = new util.Clock();
  image_probe_upright_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probe_upright_left', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [(- 0.25), 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_probe_upright_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probe_upright_right', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0.25, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  key_resp_upright = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ProbeInverted"
  ProbeInvertedClock = new util.Clock();
  image_probe_inverted_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probe_inverted_left', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [(- 0.25), 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : true,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_probe_inverted_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_probe_inverted_right', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0.25, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : true,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  key_resp_inverted = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "IBI"
  IBIClock = new util.Clock();
  text_ibi = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_ibi',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ThankYou"
  ThankYouClock = new util.Clock();
  text_thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_thanks',
    text: ("Thank you for your participation!" + "\n\n Please wait until the task is complete before exiting the browser."),
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: 1.8, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var StartComponents;
function StartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Start' ---
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Start.started', globalClock.getTime());
    // keep track of which components have finished
    StartComponents = [];
    
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Start' ---
    // get current time
    t = StartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Start' ---
    for (const thisComponent of StartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Start.stopped', globalClock.getTime());
    // the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_practice_allKeys;
var instrPracticeComponents;
function instrPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instrPractice' ---
    t = 0;
    instrPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instrPractice.started', globalClock.getTime());
    key_resp_practice.keys = undefined;
    key_resp_practice.rt = undefined;
    _key_resp_practice_allKeys = [];
    // keep track of which components have finished
    instrPracticeComponents = [];
    instrPracticeComponents.push(text_practice);
    instrPracticeComponents.push(key_resp_practice);
    
    for (const thisComponent of instrPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instrPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instrPractice' ---
    // get current time
    t = instrPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_practice* updates
    if (t >= 0.0 && text_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_practice.tStart = t;  // (not accounting for frame time here)
      text_practice.frameNStart = frameN;  // exact frame index
      
      text_practice.setAutoDraw(true);
    }
    
    
    // *key_resp_practice* updates
    if (t >= 0.0 && key_resp_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_practice.tStart = t;  // (not accounting for frame time here)
      key_resp_practice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_practice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_practice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_practice.clearEvents(); });
    }
    
    if (key_resp_practice.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_practice.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_practice_allKeys = _key_resp_practice_allKeys.concat(theseKeys);
      if (_key_resp_practice_allKeys.length > 0) {
        key_resp_practice.keys = _key_resp_practice_allKeys[_key_resp_practice_allKeys.length - 1].name;  // just the last key pressed
        key_resp_practice.rt = _key_resp_practice_allKeys[_key_resp_practice_allKeys.length - 1].rt;
        key_resp_practice.duration = _key_resp_practice_allKeys[_key_resp_practice_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instrPractice' ---
    for (const thisComponent of instrPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instrPractice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_practice.corr, level);
    }
    psychoJS.experiment.addData('key_resp_practice.keys', key_resp_practice.keys);
    if (typeof key_resp_practice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_practice.rt', key_resp_practice.rt);
        psychoJS.experiment.addData('key_resp_practice.duration', key_resp_practice.duration);
        routineTimer.reset();
        }
    
    key_resp_practice.stop();
    // the Routine "instrPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blocks_practice;
function blocks_practiceLoopBegin(blocks_practiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks_practice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stimuli/practice_blockList.csv',
      seed: undefined, name: 'blocks_practice'
    });
    psychoJS.experiment.addLoop(blocks_practice); // add the loop to the experiment
    currentLoop = blocks_practice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlocks_practice of blocks_practice) {
      snapshot = blocks_practice.getSnapshot();
      blocks_practiceLoopScheduler.add(importConditions(snapshot));
      blocks_practiceLoopScheduler.add(getReadyRoutineBegin(snapshot));
      blocks_practiceLoopScheduler.add(getReadyRoutineEachFrame());
      blocks_practiceLoopScheduler.add(getReadyRoutineEnd(snapshot));
      const trials_practice_upLoopScheduler = new Scheduler(psychoJS);
      blocks_practiceLoopScheduler.add(trials_practice_upLoopBegin(trials_practice_upLoopScheduler, snapshot));
      blocks_practiceLoopScheduler.add(trials_practice_upLoopScheduler);
      blocks_practiceLoopScheduler.add(trials_practice_upLoopEnd);
      const trials_practice_invLoopScheduler = new Scheduler(psychoJS);
      blocks_practiceLoopScheduler.add(trials_practice_invLoopBegin(trials_practice_invLoopScheduler, snapshot));
      blocks_practiceLoopScheduler.add(trials_practice_invLoopScheduler);
      blocks_practiceLoopScheduler.add(trials_practice_invLoopEnd);
      blocks_practiceLoopScheduler.add(blocks_practiceLoopEndIteration(blocks_practiceLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_practice_up;
function trials_practice_upLoopBegin(trials_practice_upLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_practice_up = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, block_list, '0:1'),
      seed: undefined, name: 'trials_practice_up'
    });
    psychoJS.experiment.addLoop(trials_practice_up); // add the loop to the experiment
    currentLoop = trials_practice_up;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_practice_up of trials_practice_up) {
      snapshot = trials_practice_up.getSnapshot();
      trials_practice_upLoopScheduler.add(importConditions(snapshot));
      trials_practice_upLoopScheduler.add(FixationRoutineBegin(snapshot));
      trials_practice_upLoopScheduler.add(FixationRoutineEachFrame());
      trials_practice_upLoopScheduler.add(FixationRoutineEnd(snapshot));
      trials_practice_upLoopScheduler.add(EncodingUprightRoutineBegin(snapshot));
      trials_practice_upLoopScheduler.add(EncodingUprightRoutineEachFrame());
      trials_practice_upLoopScheduler.add(EncodingUprightRoutineEnd(snapshot));
      trials_practice_upLoopScheduler.add(ISIRoutineBegin(snapshot));
      trials_practice_upLoopScheduler.add(ISIRoutineEachFrame());
      trials_practice_upLoopScheduler.add(ISIRoutineEnd(snapshot));
      trials_practice_upLoopScheduler.add(ProbeUpPracticeRoutineBegin(snapshot));
      trials_practice_upLoopScheduler.add(ProbeUpPracticeRoutineEachFrame());
      trials_practice_upLoopScheduler.add(ProbeUpPracticeRoutineEnd(snapshot));
      trials_practice_upLoopScheduler.add(ITIRoutineBegin(snapshot));
      trials_practice_upLoopScheduler.add(ITIRoutineEachFrame());
      trials_practice_upLoopScheduler.add(ITIRoutineEnd(snapshot));
      trials_practice_upLoopScheduler.add(trials_practice_upLoopEndIteration(trials_practice_upLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_practice_upLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_practice_up);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_practice_upLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_practice_inv;
function trials_practice_invLoopBegin(trials_practice_invLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_practice_inv = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, block_list, '2:3'),
      seed: undefined, name: 'trials_practice_inv'
    });
    psychoJS.experiment.addLoop(trials_practice_inv); // add the loop to the experiment
    currentLoop = trials_practice_inv;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_practice_inv of trials_practice_inv) {
      snapshot = trials_practice_inv.getSnapshot();
      trials_practice_invLoopScheduler.add(importConditions(snapshot));
      trials_practice_invLoopScheduler.add(FixationRoutineBegin(snapshot));
      trials_practice_invLoopScheduler.add(FixationRoutineEachFrame());
      trials_practice_invLoopScheduler.add(FixationRoutineEnd(snapshot));
      trials_practice_invLoopScheduler.add(EncodingInvertedRoutineBegin(snapshot));
      trials_practice_invLoopScheduler.add(EncodingInvertedRoutineEachFrame());
      trials_practice_invLoopScheduler.add(EncodingInvertedRoutineEnd(snapshot));
      trials_practice_invLoopScheduler.add(ISIRoutineBegin(snapshot));
      trials_practice_invLoopScheduler.add(ISIRoutineEachFrame());
      trials_practice_invLoopScheduler.add(ISIRoutineEnd(snapshot));
      trials_practice_invLoopScheduler.add(ProbeInvPracticeRoutineBegin(snapshot));
      trials_practice_invLoopScheduler.add(ProbeInvPracticeRoutineEachFrame());
      trials_practice_invLoopScheduler.add(ProbeInvPracticeRoutineEnd(snapshot));
      trials_practice_invLoopScheduler.add(ITIRoutineBegin(snapshot));
      trials_practice_invLoopScheduler.add(ITIRoutineEachFrame());
      trials_practice_invLoopScheduler.add(ITIRoutineEnd(snapshot));
      trials_practice_invLoopScheduler.add(trials_practice_invLoopEndIteration(trials_practice_invLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_practice_invLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_practice_inv);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_practice_invLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function blocks_practiceLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(blocks_practice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function blocks_practiceLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var blocks_order;
function blocks_orderLoopBegin(blocks_orderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks_order = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: order_list,
      seed: undefined, name: 'blocks_order'
    });
    psychoJS.experiment.addLoop(blocks_order); // add the loop to the experiment
    currentLoop = blocks_order;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlocks_order of blocks_order) {
      snapshot = blocks_order.getSnapshot();
      blocks_orderLoopScheduler.add(importConditions(snapshot));
      const trials_uprightLoopScheduler = new Scheduler(psychoJS);
      blocks_orderLoopScheduler.add(trials_uprightLoopBegin(trials_uprightLoopScheduler, snapshot));
      blocks_orderLoopScheduler.add(trials_uprightLoopScheduler);
      blocks_orderLoopScheduler.add(trials_uprightLoopEnd);
      const trials_invertedLoopScheduler = new Scheduler(psychoJS);
      blocks_orderLoopScheduler.add(trials_invertedLoopBegin(trials_invertedLoopScheduler, snapshot));
      blocks_orderLoopScheduler.add(trials_invertedLoopScheduler);
      blocks_orderLoopScheduler.add(trials_invertedLoopEnd);
      blocks_orderLoopScheduler.add(IBIRoutineBegin(snapshot));
      blocks_orderLoopScheduler.add(IBIRoutineEachFrame());
      blocks_orderLoopScheduler.add(IBIRoutineEnd(snapshot));
      blocks_orderLoopScheduler.add(blocks_orderLoopEndIteration(blocks_orderLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_upright;
function trials_uprightLoopBegin(trials_uprightLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_upright = new TrialHandler({
      psychoJS: psychoJS,
      nReps: upright_flag, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: block_list,
      seed: undefined, name: 'trials_upright'
    });
    psychoJS.experiment.addLoop(trials_upright); // add the loop to the experiment
    currentLoop = trials_upright;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_upright of trials_upright) {
      snapshot = trials_upright.getSnapshot();
      trials_uprightLoopScheduler.add(importConditions(snapshot));
      trials_uprightLoopScheduler.add(FixationRoutineBegin(snapshot));
      trials_uprightLoopScheduler.add(FixationRoutineEachFrame());
      trials_uprightLoopScheduler.add(FixationRoutineEnd(snapshot));
      trials_uprightLoopScheduler.add(EncodingUprightRoutineBegin(snapshot));
      trials_uprightLoopScheduler.add(EncodingUprightRoutineEachFrame());
      trials_uprightLoopScheduler.add(EncodingUprightRoutineEnd(snapshot));
      trials_uprightLoopScheduler.add(ISIRoutineBegin(snapshot));
      trials_uprightLoopScheduler.add(ISIRoutineEachFrame());
      trials_uprightLoopScheduler.add(ISIRoutineEnd(snapshot));
      trials_uprightLoopScheduler.add(ProbeUprightRoutineBegin(snapshot));
      trials_uprightLoopScheduler.add(ProbeUprightRoutineEachFrame());
      trials_uprightLoopScheduler.add(ProbeUprightRoutineEnd(snapshot));
      trials_uprightLoopScheduler.add(ITIRoutineBegin(snapshot));
      trials_uprightLoopScheduler.add(ITIRoutineEachFrame());
      trials_uprightLoopScheduler.add(ITIRoutineEnd(snapshot));
      trials_uprightLoopScheduler.add(trials_uprightLoopEndIteration(trials_uprightLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_uprightLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_upright);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_uprightLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_inverted;
function trials_invertedLoopBegin(trials_invertedLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_inverted = new TrialHandler({
      psychoJS: psychoJS,
      nReps: inverted_flag, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: block_list,
      seed: undefined, name: 'trials_inverted'
    });
    psychoJS.experiment.addLoop(trials_inverted); // add the loop to the experiment
    currentLoop = trials_inverted;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_inverted of trials_inverted) {
      snapshot = trials_inverted.getSnapshot();
      trials_invertedLoopScheduler.add(importConditions(snapshot));
      trials_invertedLoopScheduler.add(FixationRoutineBegin(snapshot));
      trials_invertedLoopScheduler.add(FixationRoutineEachFrame());
      trials_invertedLoopScheduler.add(FixationRoutineEnd(snapshot));
      trials_invertedLoopScheduler.add(EncodingInvertedRoutineBegin(snapshot));
      trials_invertedLoopScheduler.add(EncodingInvertedRoutineEachFrame());
      trials_invertedLoopScheduler.add(EncodingInvertedRoutineEnd(snapshot));
      trials_invertedLoopScheduler.add(ISIRoutineBegin(snapshot));
      trials_invertedLoopScheduler.add(ISIRoutineEachFrame());
      trials_invertedLoopScheduler.add(ISIRoutineEnd(snapshot));
      trials_invertedLoopScheduler.add(ProbeInvertedRoutineBegin(snapshot));
      trials_invertedLoopScheduler.add(ProbeInvertedRoutineEachFrame());
      trials_invertedLoopScheduler.add(ProbeInvertedRoutineEnd(snapshot));
      trials_invertedLoopScheduler.add(ITIRoutineBegin(snapshot));
      trials_invertedLoopScheduler.add(ITIRoutineEachFrame());
      trials_invertedLoopScheduler.add(ITIRoutineEnd(snapshot));
      trials_invertedLoopScheduler.add(trials_invertedLoopEndIteration(trials_invertedLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_invertedLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_inverted);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_invertedLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function blocks_orderLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(blocks_order);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function blocks_orderLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var getReadyComponents;
function getReadyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'getReady' ---
    t = 0;
    getReadyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('getReady.started', globalClock.getTime());
    // keep track of which components have finished
    getReadyComponents = [];
    getReadyComponents.push(text_countdown);
    
    for (const thisComponent of getReadyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function getReadyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'getReady' ---
    // get current time
    t = getReadyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (text_countdown.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_countdown.setText((5 - Number.parseInt(t)).toString(), false);
    }
    
    // *text_countdown* updates
    if (t >= 0.0 && text_countdown.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_countdown.tStart = t;  // (not accounting for frame time here)
      text_countdown.frameNStart = frameN;  // exact frame index
      
      text_countdown.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_countdown.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_countdown.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of getReadyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function getReadyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'getReady' ---
    for (const thisComponent of getReadyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('getReady.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FixationComponents;
function FixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fixation' ---
    t = 0;
    FixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Fixation.started', globalClock.getTime());
    // keep track of which components have finished
    FixationComponents = [];
    FixationComponents.push(text_fixation);
    
    for (const thisComponent of FixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fixation' ---
    // get current time
    t = FixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fixation* updates
    if (t >= 0.0 && text_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fixation.tStart = t;  // (not accounting for frame time here)
      text_fixation.frameNStart = frameN;  // exact frame index
      
      text_fixation.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fix_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fixation.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fixation' ---
    for (const thisComponent of FixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Fixation.stopped', globalClock.getTime());
    // the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EncodingUprightComponents;
function EncodingUprightRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EncodingUpright' ---
    t = 0;
    EncodingUprightClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('EncodingUpright.started', globalClock.getTime());
    image_target_upright.setSize(stim_size);
    image_target_upright.setImage(target_list);
    // keep track of which components have finished
    EncodingUprightComponents = [];
    EncodingUprightComponents.push(image_target_upright);
    
    for (const thisComponent of EncodingUprightComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EncodingUprightRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EncodingUpright' ---
    // get current time
    t = EncodingUprightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_target_upright* updates
    if (t >= 0.0 && image_target_upright.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_target_upright.tStart = t;  // (not accounting for frame time here)
      image_target_upright.frameNStart = frameN;  // exact frame index
      
      image_target_upright.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_target_upright.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_target_upright.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EncodingUprightComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EncodingUprightRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EncodingUpright' ---
    for (const thisComponent of EncodingUprightComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EncodingUpright.stopped', globalClock.getTime());
    // the Routine "EncodingUpright" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ISIComponents;
function ISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ISI' ---
    t = 0;
    ISIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ISI.started', globalClock.getTime());
    text_isi.setText('+');
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(text_isi);
    
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ISIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ISI' ---
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_isi* updates
    if (t >= 0.0 && text_isi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_isi.tStart = t;  // (not accounting for frame time here)
      text_isi.frameNStart = frameN;  // exact frame index
      
      text_isi.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + isi_jittered - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_isi.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_isi.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ISI' ---
    for (const thisComponent of ISIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ISI.stopped', globalClock.getTime());
    // the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_up_prac_allKeys;
var ProbeUpPracticeComponents;
function ProbeUpPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ProbeUpPractice' ---
    t = 0;
    ProbeUpPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ProbeUpPractice.started', globalClock.getTime());
    image_probePrac_up_left.setSize(stim_size);
    image_probePrac_up_left.setImage(probe_L);
    image_probePrace_up_right.setSize(stim_size);
    image_probePrace_up_right.setImage(probe_R);
    key_resp_up_prac.keys = undefined;
    key_resp_up_prac.rt = undefined;
    _key_resp_up_prac_allKeys = [];
    // keep track of which components have finished
    ProbeUpPracticeComponents = [];
    ProbeUpPracticeComponents.push(image_probePrac_up_left);
    ProbeUpPracticeComponents.push(image_probePrace_up_right);
    ProbeUpPracticeComponents.push(key_resp_up_prac);
    
    for (const thisComponent of ProbeUpPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ProbeUpPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ProbeUpPractice' ---
    // get current time
    t = ProbeUpPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_probePrac_up_left* updates
    if (t >= 0.0 && image_probePrac_up_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probePrac_up_left.tStart = t;  // (not accounting for frame time here)
      image_probePrac_up_left.frameNStart = frameN;  // exact frame index
      
      image_probePrac_up_left.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probePrac_up_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probePrac_up_left.setAutoDraw(false);
    }
    
    
    // *image_probePrace_up_right* updates
    if (t >= 0.0 && image_probePrace_up_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probePrace_up_right.tStart = t;  // (not accounting for frame time here)
      image_probePrace_up_right.frameNStart = frameN;  // exact frame index
      
      image_probePrace_up_right.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probePrace_up_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probePrace_up_right.setAutoDraw(false);
    }
    
    
    // *key_resp_up_prac* updates
    if (t >= 0.0 && key_resp_up_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_up_prac.tStart = t;  // (not accounting for frame time here)
      key_resp_up_prac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_up_prac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_up_prac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_up_prac.clearEvents(); });
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_up_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_up_prac.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_up_prac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_up_prac.getKeys({keyList: ['1', 'left', '2', 'right', 's'], waitRelease: false});
      _key_resp_up_prac_allKeys = _key_resp_up_prac_allKeys.concat(theseKeys);
      if (_key_resp_up_prac_allKeys.length > 0) {
        key_resp_up_prac.keys = _key_resp_up_prac_allKeys[0].name;  // just the first key pressed
        key_resp_up_prac.rt = _key_resp_up_prac_allKeys[0].rt;
        key_resp_up_prac.duration = _key_resp_up_prac_allKeys[0].duration;
        // was this correct?
        if (key_resp_up_prac.keys == correct_resp) {
            key_resp_up_prac.corr = 1;
        } else {
            key_resp_up_prac.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ProbeUpPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var s_key;
var thisExp;
var correctKey;
function ProbeUpPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ProbeUpPractice' ---
    for (const thisComponent of ProbeUpPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ProbeUpPractice.stopped', globalClock.getTime());
    s_key = key_resp_prac.keys;
    if ((s_key === "s")) {
        trials_practice.finished = true;
    }
    
    thisExp=psychoJS.experiment;
    
    if ((correct_resp === 1) || (correct_resp === "1")) {
        correctKey = ["1","left"];
    }
    if ((correct_resp === 2) || (correct_resp === "2")) {
        correctKey = ["2","right"];
    }
    
    if ((key_resp_prac.keys === correctKey[0]) || (key_resp_prac.keys === correctKey[1])) {
        key_resp_prac.corr = true;
    } else {
        key_resp_prac.corr = false;
    }
    
    thisExp.addData("correctKey", correctKey);
    thisExp.addData("key_resp_corr", key_resp_prac.corr)
    // was no response the correct answer?!
    if (key_resp_up_prac.keys === undefined) {
      if (['None','none',undefined].includes(correct_resp)) {
         key_resp_up_prac.corr = 1;  // correct non-response
      } else {
         key_resp_up_prac.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_up_prac.corr, level);
    }
    psychoJS.experiment.addData('key_resp_up_prac.keys', key_resp_up_prac.keys);
    psychoJS.experiment.addData('key_resp_up_prac.corr', key_resp_up_prac.corr);
    if (typeof key_resp_up_prac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_up_prac.rt', key_resp_up_prac.rt);
        psychoJS.experiment.addData('key_resp_up_prac.duration', key_resp_up_prac.duration);
        }
    
    key_resp_up_prac.stop();
    // the Routine "ProbeUpPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var iti_jittered;
var ITIComponents;
function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ITI.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_iti
    // iti_dur + random number between 0 and 0.2
    iti_jittered = (iti_dur + Math.random()* 0.2);  
    
    text_iti.setText('');
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(text_iti);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_iti* updates
    if (t >= 0.0 && text_iti.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_iti.tStart = t;  // (not accounting for frame time here)
      text_iti.frameNStart = frameN;  // exact frame index
      
      text_iti.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + iti_jittered - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_iti.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_iti.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ITI.stopped', globalClock.getTime());
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EncodingInvertedComponents;
function EncodingInvertedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EncodingInverted' ---
    t = 0;
    EncodingInvertedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('EncodingInverted.started', globalClock.getTime());
    image_target_inverted.setSize(stim_size);
    image_target_inverted.setImage(target_list);
    // keep track of which components have finished
    EncodingInvertedComponents = [];
    EncodingInvertedComponents.push(image_target_inverted);
    
    for (const thisComponent of EncodingInvertedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EncodingInvertedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EncodingInverted' ---
    // get current time
    t = EncodingInvertedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_target_inverted* updates
    if (t >= 0.0 && image_target_inverted.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_target_inverted.tStart = t;  // (not accounting for frame time here)
      image_target_inverted.frameNStart = frameN;  // exact frame index
      
      image_target_inverted.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_target_inverted.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_target_inverted.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EncodingInvertedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EncodingInvertedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EncodingInverted' ---
    for (const thisComponent of EncodingInvertedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EncodingInverted.stopped', globalClock.getTime());
    // the Routine "EncodingInverted" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_inv_prac_allKeys;
var ProbeInvPracticeComponents;
function ProbeInvPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ProbeInvPractice' ---
    t = 0;
    ProbeInvPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ProbeInvPractice.started', globalClock.getTime());
    image_probePrac_inv_left.setSize(stim_size);
    image_probePrac_inv_left.setImage(probe_L);
    image_probePrace_inv_right.setSize(stim_size);
    image_probePrace_inv_right.setImage(probe_R);
    key_resp_inv_prac.keys = undefined;
    key_resp_inv_prac.rt = undefined;
    _key_resp_inv_prac_allKeys = [];
    // keep track of which components have finished
    ProbeInvPracticeComponents = [];
    ProbeInvPracticeComponents.push(image_probePrac_inv_left);
    ProbeInvPracticeComponents.push(image_probePrace_inv_right);
    ProbeInvPracticeComponents.push(key_resp_inv_prac);
    
    for (const thisComponent of ProbeInvPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ProbeInvPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ProbeInvPractice' ---
    // get current time
    t = ProbeInvPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_probePrac_inv_left* updates
    if (t >= 0.0 && image_probePrac_inv_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probePrac_inv_left.tStart = t;  // (not accounting for frame time here)
      image_probePrac_inv_left.frameNStart = frameN;  // exact frame index
      
      image_probePrac_inv_left.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probePrac_inv_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probePrac_inv_left.setAutoDraw(false);
    }
    
    
    // *image_probePrace_inv_right* updates
    if (t >= 0.0 && image_probePrace_inv_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probePrace_inv_right.tStart = t;  // (not accounting for frame time here)
      image_probePrace_inv_right.frameNStart = frameN;  // exact frame index
      
      image_probePrace_inv_right.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probePrace_inv_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probePrace_inv_right.setAutoDraw(false);
    }
    
    
    // *key_resp_inv_prac* updates
    if (t >= 0.0 && key_resp_inv_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_inv_prac.tStart = t;  // (not accounting for frame time here)
      key_resp_inv_prac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_inv_prac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_inv_prac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_inv_prac.clearEvents(); });
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_inv_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_inv_prac.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_inv_prac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_inv_prac.getKeys({keyList: ['1', 'left', '2', 'right', 's'], waitRelease: false});
      _key_resp_inv_prac_allKeys = _key_resp_inv_prac_allKeys.concat(theseKeys);
      if (_key_resp_inv_prac_allKeys.length > 0) {
        key_resp_inv_prac.keys = _key_resp_inv_prac_allKeys[0].name;  // just the first key pressed
        key_resp_inv_prac.rt = _key_resp_inv_prac_allKeys[0].rt;
        key_resp_inv_prac.duration = _key_resp_inv_prac_allKeys[0].duration;
        // was this correct?
        if (key_resp_inv_prac.keys == correct_resp) {
            key_resp_inv_prac.corr = 1;
        } else {
            key_resp_inv_prac.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ProbeInvPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ProbeInvPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ProbeInvPractice' ---
    for (const thisComponent of ProbeInvPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ProbeInvPractice.stopped', globalClock.getTime());
    s_key = key_resp_prac.keys;
    if ((s_key === "s")) {
        trials_practice.finished = true;
    }
    
    thisExp=psychoJS.experiment;
    
    if ((correct_resp === 1) || (correct_resp === "1")) {
        correctKey = ["1","left"];
    }
    if ((correct_resp === 2) || (correct_resp === "2")) {
        correctKey = ["2","right"];
    }
    
    if ((key_resp_prac.keys === correctKey[0]) || (key_resp_prac.keys === correctKey[1])) {
        key_resp_prac.corr = true;
    } else {
        key_resp_prac.corr = false;
    }
    
    thisExp.addData("correctKey", correctKey);
    thisExp.addData("key_resp_corr", key_resp_prac.corr)
    // was no response the correct answer?!
    if (key_resp_inv_prac.keys === undefined) {
      if (['None','none',undefined].includes(correct_resp)) {
         key_resp_inv_prac.corr = 1;  // correct non-response
      } else {
         key_resp_inv_prac.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_inv_prac.corr, level);
    }
    psychoJS.experiment.addData('key_resp_inv_prac.keys', key_resp_inv_prac.keys);
    psychoJS.experiment.addData('key_resp_inv_prac.corr', key_resp_inv_prac.corr);
    if (typeof key_resp_inv_prac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_inv_prac.rt', key_resp_inv_prac.rt);
        psychoJS.experiment.addData('key_resp_inv_prac.duration', key_resp_inv_prac.duration);
        }
    
    key_resp_inv_prac.stop();
    // the Routine "ProbeInvPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_endPractice_allKeys;
var FB_PracticeComponents;
function FB_PracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FB_Practice' ---
    t = 0;
    FB_PracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('FB_Practice.started', globalClock.getTime());
    text_Practice.setText(((msg + "\n\n Please remember to press the LEFT BUTTON to choose the image on the left, or press the RIGHT BUTTON to choose the image on the right. Try to make your choice as quickly and accurately as possible.") + "\n\n Press SPACEBAR to start."));
    key_resp_endPractice.keys = undefined;
    key_resp_endPractice.rt = undefined;
    _key_resp_endPractice_allKeys = [];
    // keep track of which components have finished
    FB_PracticeComponents = [];
    FB_PracticeComponents.push(text_Practice);
    FB_PracticeComponents.push(key_resp_endPractice);
    
    for (const thisComponent of FB_PracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FB_PracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FB_Practice' ---
    // get current time
    t = FB_PracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Practice* updates
    if (t >= 0.0 && text_Practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Practice.tStart = t;  // (not accounting for frame time here)
      text_Practice.frameNStart = frameN;  // exact frame index
      
      text_Practice.setAutoDraw(true);
    }
    
    
    // *key_resp_endPractice* updates
    if (t >= 0.0 && key_resp_endPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_endPractice.tStart = t;  // (not accounting for frame time here)
      key_resp_endPractice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_endPractice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_endPractice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_endPractice.clearEvents(); });
    }
    
    if (key_resp_endPractice.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_endPractice.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_endPractice_allKeys = _key_resp_endPractice_allKeys.concat(theseKeys);
      if (_key_resp_endPractice_allKeys.length > 0) {
        key_resp_endPractice.keys = _key_resp_endPractice_allKeys[_key_resp_endPractice_allKeys.length - 1].name;  // just the last key pressed
        key_resp_endPractice.rt = _key_resp_endPractice_allKeys[_key_resp_endPractice_allKeys.length - 1].rt;
        key_resp_endPractice.duration = _key_resp_endPractice_allKeys[_key_resp_endPractice_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FB_PracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FB_PracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FB_Practice' ---
    for (const thisComponent of FB_PracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('FB_Practice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_endPractice.corr, level);
    }
    psychoJS.experiment.addData('key_resp_endPractice.keys', key_resp_endPractice.keys);
    if (typeof key_resp_endPractice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_endPractice.rt', key_resp_endPractice.rt);
        psychoJS.experiment.addData('key_resp_endPractice.duration', key_resp_endPractice.duration);
        routineTimer.reset();
        }
    
    key_resp_endPractice.stop();
    // the Routine "FB_Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_upright_allKeys;
var ProbeUprightComponents;
function ProbeUprightRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ProbeUpright' ---
    t = 0;
    ProbeUprightClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ProbeUpright.started', globalClock.getTime());
    image_probe_upright_left.setSize(stim_size);
    image_probe_upright_left.setImage(probe_L);
    image_probe_upright_right.setSize(stim_size);
    image_probe_upright_right.setImage(probe_R);
    key_resp_upright.keys = undefined;
    key_resp_upright.rt = undefined;
    _key_resp_upright_allKeys = [];
    // keep track of which components have finished
    ProbeUprightComponents = [];
    ProbeUprightComponents.push(image_probe_upright_left);
    ProbeUprightComponents.push(image_probe_upright_right);
    ProbeUprightComponents.push(key_resp_upright);
    
    for (const thisComponent of ProbeUprightComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prbL;
function ProbeUprightRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ProbeUpright' ---
    // get current time
    t = ProbeUprightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_probe_upright
    if (key_resp_upright) {
        if ((key_resp_upright.keys === "1") || (key_resp_upright.keys === "left")) {
            prbL = "blue";
        } else {
            if ((key_resp_upright.keys === "2") || (key_resp_upright.keys === "right")) {
                prbR = "blue";
            }
        }
    }
    
    
    // *image_probe_upright_left* updates
    if (t >= 0.0 && image_probe_upright_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probe_upright_left.tStart = t;  // (not accounting for frame time here)
      image_probe_upright_left.frameNStart = frameN;  // exact frame index
      
      image_probe_upright_left.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probe_upright_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probe_upright_left.setAutoDraw(false);
    }
    
    
    // *image_probe_upright_right* updates
    if (t >= 0.0 && image_probe_upright_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probe_upright_right.tStart = t;  // (not accounting for frame time here)
      image_probe_upright_right.frameNStart = frameN;  // exact frame index
      
      image_probe_upright_right.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probe_upright_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probe_upright_right.setAutoDraw(false);
    }
    
    
    // *key_resp_upright* updates
    if (t >= 0.0 && key_resp_upright.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_upright.tStart = t;  // (not accounting for frame time here)
      key_resp_upright.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_upright.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_upright.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_upright.clearEvents(); });
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_upright.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_upright.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_upright.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_upright.getKeys({keyList: ['1', 'left', '2', 'right', 's'], waitRelease: false});
      _key_resp_upright_allKeys = _key_resp_upright_allKeys.concat(theseKeys);
      if (_key_resp_upright_allKeys.length > 0) {
        key_resp_upright.keys = _key_resp_upright_allKeys[0].name;  // just the first key pressed
        key_resp_upright.rt = _key_resp_upright_allKeys[0].rt;
        key_resp_upright.duration = _key_resp_upright_allKeys[0].duration;
        // was this correct?
        if (key_resp_upright.keys == correct_resp) {
            key_resp_upright.corr = 1;
        } else {
            key_resp_upright.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ProbeUprightComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ProbeUprightRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ProbeUpright' ---
    for (const thisComponent of ProbeUprightComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ProbeUpright.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_probe_upright
    s_key = key_resp.keys;
    if ((s_key === "s")) {
        trials.finished = true;
    }
    
    thisExp=psychoJS.experiment;
    
    if ((correct_resp === 1) || (correct_resp === "1")) {
        correctKey = ["1","left"];
    }
    if ((correct_resp === 2) || (correct_resp === "2")) {
        correctKey = ["2","right"];
    }
    
    if ((key_resp.keys === correctKey[0]) || (key_resp.keys === correctKey[1])) {
        key_resp.corr = true;
    } else {
        key_resp.corr = false;
    }
    
    thisExp.addData("correctKey", correctKey);
    thisExp.addData("key_resp_corr", key_resp.corr)
    // was no response the correct answer?!
    if (key_resp_upright.keys === undefined) {
      if (['None','none',undefined].includes(correct_resp)) {
         key_resp_upright.corr = 1;  // correct non-response
      } else {
         key_resp_upright.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_upright.corr, level);
    }
    psychoJS.experiment.addData('key_resp_upright.keys', key_resp_upright.keys);
    psychoJS.experiment.addData('key_resp_upright.corr', key_resp_upright.corr);
    if (typeof key_resp_upright.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_upright.rt', key_resp_upright.rt);
        psychoJS.experiment.addData('key_resp_upright.duration', key_resp_upright.duration);
        }
    
    key_resp_upright.stop();
    // the Routine "ProbeUpright" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_inverted_allKeys;
var ProbeInvertedComponents;
function ProbeInvertedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ProbeInverted' ---
    t = 0;
    ProbeInvertedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ProbeInverted.started', globalClock.getTime());
    image_probe_inverted_left.setSize(stim_size);
    image_probe_inverted_left.setImage(probe_L);
    image_probe_inverted_right.setSize(stim_size);
    image_probe_inverted_right.setImage(probe_R);
    key_resp_inverted.keys = undefined;
    key_resp_inverted.rt = undefined;
    _key_resp_inverted_allKeys = [];
    // keep track of which components have finished
    ProbeInvertedComponents = [];
    ProbeInvertedComponents.push(image_probe_inverted_left);
    ProbeInvertedComponents.push(image_probe_inverted_right);
    ProbeInvertedComponents.push(key_resp_inverted);
    
    for (const thisComponent of ProbeInvertedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ProbeInvertedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ProbeInverted' ---
    // get current time
    t = ProbeInvertedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_probe_inverted
    if (key_resp_inverted) {
        if ((key_resp_inverted.keys === "1") || (key_resp.keys === "left")) {
            prbL = "blue";
        } else {
            if ((key_resp_inverted.keys === "2") || (key_resp.keys === "right")) {
                prbR = "blue";
            }
        }
    }
    
    
    // *image_probe_inverted_left* updates
    if (t >= 0.0 && image_probe_inverted_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probe_inverted_left.tStart = t;  // (not accounting for frame time here)
      image_probe_inverted_left.frameNStart = frameN;  // exact frame index
      
      image_probe_inverted_left.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probe_inverted_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probe_inverted_left.setAutoDraw(false);
    }
    
    
    // *image_probe_inverted_right* updates
    if (t >= 0.0 && image_probe_inverted_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_probe_inverted_right.tStart = t;  // (not accounting for frame time here)
      image_probe_inverted_right.frameNStart = frameN;  // exact frame index
      
      image_probe_inverted_right.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_probe_inverted_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_probe_inverted_right.setAutoDraw(false);
    }
    
    
    // *key_resp_inverted* updates
    if (t >= 0.0 && key_resp_inverted.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_inverted.tStart = t;  // (not accounting for frame time here)
      key_resp_inverted.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_inverted.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_inverted.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_inverted.clearEvents(); });
    }
    
    frameRemains = 0.0 + probe_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_inverted.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_inverted.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_inverted.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_inverted.getKeys({keyList: ['1', 'left', '2', 'right', 's'], waitRelease: false});
      _key_resp_inverted_allKeys = _key_resp_inverted_allKeys.concat(theseKeys);
      if (_key_resp_inverted_allKeys.length > 0) {
        key_resp_inverted.keys = _key_resp_inverted_allKeys[0].name;  // just the first key pressed
        key_resp_inverted.rt = _key_resp_inverted_allKeys[0].rt;
        key_resp_inverted.duration = _key_resp_inverted_allKeys[0].duration;
        // was this correct?
        if (key_resp_inverted.keys == correct_resp) {
            key_resp_inverted.corr = 1;
        } else {
            key_resp_inverted.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ProbeInvertedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ProbeInvertedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ProbeInverted' ---
    for (const thisComponent of ProbeInvertedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ProbeInverted.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_probe_inverted
    s_key = key_resp_inverted.keys;
    if ((s_key === "s")) {
        trials.finished = true;
    }
    
    thisExp=psychoJS.experiment;
    
    if ((correct_resp === 1) || (correct_resp === "1")) {
        correctKey = ["1","left"];
    }
    if ((correct_resp === 2) || (correct_resp === "2")) {
        correctKey = ["2","right"];
    }
    
    if ((key_resp_inverted.keys === correctKey[0]) || (key_resp_inverted.keys === correctKey[1])) {
        key_resp_inverted.corr = true;
    } else {
        key_resp_inverted.corr = false;
    }
    
    thisExp.addData("correctKey", correctKey);
    thisExp.addData("key_resp_corr", key_resp.corr)
    // was no response the correct answer?!
    if (key_resp_inverted.keys === undefined) {
      if (['None','none',undefined].includes(correct_resp)) {
         key_resp_inverted.corr = 1;  // correct non-response
      } else {
         key_resp_inverted.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_inverted.corr, level);
    }
    psychoJS.experiment.addData('key_resp_inverted.keys', key_resp_inverted.keys);
    psychoJS.experiment.addData('key_resp_inverted.corr', key_resp_inverted.corr);
    if (typeof key_resp_inverted.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_inverted.rt', key_resp_inverted.rt);
        psychoJS.experiment.addData('key_resp_inverted.duration', key_resp_inverted.duration);
        }
    
    key_resp_inverted.stop();
    // the Routine "ProbeInverted" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var IBIComponents;
function IBIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'IBI' ---
    t = 0;
    IBIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('IBI.started', globalClock.getTime());
    // keep track of which components have finished
    IBIComponents = [];
    IBIComponents.push(text_ibi);
    
    for (const thisComponent of IBIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function IBIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'IBI' ---
    // get current time
    t = IBIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_ibi* updates
    if (t >= 0.0 && text_ibi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_ibi.tStart = t;  // (not accounting for frame time here)
      text_ibi.frameNStart = frameN;  // exact frame index
      
      text_ibi.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_ibi.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_ibi.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of IBIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function IBIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'IBI' ---
    for (const thisComponent of IBIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('IBI.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ThankYouComponents;
function ThankYouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ThankYou' ---
    t = 0;
    ThankYouClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('ThankYou.started', globalClock.getTime());
    // keep track of which components have finished
    ThankYouComponents = [];
    ThankYouComponents.push(text_thanks);
    
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ThankYouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ThankYou' ---
    // get current time
    t = ThankYouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_thanks* updates
    if (t >= 0.0 && text_thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_thanks.tStart = t;  // (not accounting for frame time here)
      text_thanks.frameNStart = frameN;  // exact frame index
      
      text_thanks.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_thanks.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ThankYouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ThankYou' ---
    for (const thisComponent of ThankYouComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ThankYou.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  // Run 'End Experiment' code from code_hardware
  document.body.style.cursor='auto';
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
