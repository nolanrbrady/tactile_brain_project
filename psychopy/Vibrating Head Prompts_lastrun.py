#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Mon Jun  5 14:42:06 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'Vibrating Head Prompts'  # from the Builder filename that created this script
expInfo = {
    'participant': [f"{randint(0, 999999):06.0f}"],
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nolanbrady/Desktop/Tactile_Brain/Vibrating Head Prompts_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Begin"
BeginClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Beginning instructiuons.....',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Tapping_Prompt"
Tapping_PromptClock = core.Clock()
tPrompt = visual.TextStim(win=win, name='tPrompt',
    text='For this task, you will be asked to tap your left index finger to your left thumb repeatedly at a steady pace for 30 seconds. You will then receive a 30 second break before tapping your right index finger to your right thumb, then you will take another 30 second break. You will do this task 3 times.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Tapping"
TappingClock = core.Clock()
TapL = visual.TextStim(win=win, name='TapL',
    text='Tap left fingers for 30 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break1 = visual.TextStim(win=win, name='break1',
    text='take 30 second break.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TapR = visual.TextStim(win=win, name='TapR',
    text='Tap right fingers for 30 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
break2 = visual.TextStim(win=win, name='break2',
    text='Take a 30 second break. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Countdown_Prompt"
Countdown_PromptClock = core.Clock()
CD_Prompt = visual.TextStim(win=win, name='CD_Prompt',
    text='For the next task, count backwards from 100 in decrements of 7. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Count_down"
Count_downClock = core.Clock()
Count_back_from_onehundred = visual.TextStim(win=win, name='Count_back_from_onehundred',
    text='Begin counting back from 100.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Take a 30 second break.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='End of Trial\n\nThank you for participating',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Begin"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
BeginComponents = [instructions]
for thisComponent in BeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Begin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions, 'tStopRefresh')  # time at next scr refresh
            instructions.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Begin"-------
for thisComponent in BeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)

# ------Prepare to start Routine "Tapping_Prompt"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
Tapping_PromptComponents = [tPrompt]
for thisComponent in Tapping_PromptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Tapping_PromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Tapping_Prompt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Tapping_PromptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Tapping_PromptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tPrompt* updates
    if tPrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tPrompt.frameNStart = frameN  # exact frame index
        tPrompt.tStart = t  # local t and not account for scr refresh
        tPrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tPrompt, 'tStartRefresh')  # time at next scr refresh
        tPrompt.setAutoDraw(True)
    if tPrompt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tPrompt.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            tPrompt.tStop = t  # not accounting for scr refresh
            tPrompt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tPrompt, 'tStopRefresh')  # time at next scr refresh
            tPrompt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Tapping_PromptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Tapping_Prompt"-------
for thisComponent in Tapping_PromptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tPrompt.started', tPrompt.tStartRefresh)
thisExp.addData('tPrompt.stopped', tPrompt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
tappingTrials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='tappingTrials')
thisExp.addLoop(tappingTrials)  # add the loop to the experiment
thisTappingTrial = tappingTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTappingTrial.rgb)
if thisTappingTrial != None:
    for paramName in thisTappingTrial:
        exec('{} = thisTappingTrial[paramName]'.format(paramName))

for thisTappingTrial in tappingTrials:
    currentLoop = tappingTrials
    # abbreviate parameter names if possible (e.g. rgb = thisTappingTrial.rgb)
    if thisTappingTrial != None:
        for paramName in thisTappingTrial:
            exec('{} = thisTappingTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Tapping"-------
    continueRoutine = True
    routineTimer.add(120.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    TappingComponents = [TapL, break1, TapR, break2]
    for thisComponent in TappingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TappingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Tapping"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TappingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TappingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TapL* updates
        if TapL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TapL.frameNStart = frameN  # exact frame index
            TapL.tStart = t  # local t and not account for scr refresh
            TapL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TapL, 'tStartRefresh')  # time at next scr refresh
            TapL.setAutoDraw(True)
        if TapL.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TapL.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                TapL.tStop = t  # not accounting for scr refresh
                TapL.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TapL, 'tStopRefresh')  # time at next scr refresh
                TapL.setAutoDraw(False)
        
        # *break1* updates
        if break1.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
            # keep track of start time/frame for later
            break1.frameNStart = frameN  # exact frame index
            break1.tStart = t  # local t and not account for scr refresh
            break1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
            break1.setAutoDraw(True)
        if break1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break1.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                break1.tStop = t  # not accounting for scr refresh
                break1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break1, 'tStopRefresh')  # time at next scr refresh
                break1.setAutoDraw(False)
        
        # *TapR* updates
        if TapR.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            TapR.frameNStart = frameN  # exact frame index
            TapR.tStart = t  # local t and not account for scr refresh
            TapR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TapR, 'tStartRefresh')  # time at next scr refresh
            TapR.setAutoDraw(True)
        if TapR.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TapR.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                TapR.tStop = t  # not accounting for scr refresh
                TapR.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TapR, 'tStopRefresh')  # time at next scr refresh
                TapR.setAutoDraw(False)
        
        # *break2* updates
        if break2.status == NOT_STARTED and tThisFlip >= 90.0-frameTolerance:
            # keep track of start time/frame for later
            break2.frameNStart = frameN  # exact frame index
            break2.tStart = t  # local t and not account for scr refresh
            break2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break2, 'tStartRefresh')  # time at next scr refresh
            break2.setAutoDraw(True)
        if break2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break2.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                break2.tStop = t  # not accounting for scr refresh
                break2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break2, 'tStopRefresh')  # time at next scr refresh
                break2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TappingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Tapping"-------
    for thisComponent in TappingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tappingTrials.addData('TapL.started', TapL.tStartRefresh)
    tappingTrials.addData('TapL.stopped', TapL.tStopRefresh)
    tappingTrials.addData('break1.started', break1.tStartRefresh)
    tappingTrials.addData('break1.stopped', break1.tStopRefresh)
    tappingTrials.addData('TapR.started', TapR.tStartRefresh)
    tappingTrials.addData('TapR.stopped', TapR.tStopRefresh)
    tappingTrials.addData('break2.started', break2.tStartRefresh)
    tappingTrials.addData('break2.stopped', break2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'tappingTrials'


# ------Prepare to start Routine "Countdown_Prompt"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
Countdown_PromptComponents = [CD_Prompt]
for thisComponent in Countdown_PromptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Countdown_PromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Countdown_Prompt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Countdown_PromptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Countdown_PromptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CD_Prompt* updates
    if CD_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CD_Prompt.frameNStart = frameN  # exact frame index
        CD_Prompt.tStart = t  # local t and not account for scr refresh
        CD_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CD_Prompt, 'tStartRefresh')  # time at next scr refresh
        CD_Prompt.setAutoDraw(True)
    if CD_Prompt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > CD_Prompt.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            CD_Prompt.tStop = t  # not accounting for scr refresh
            CD_Prompt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CD_Prompt, 'tStopRefresh')  # time at next scr refresh
            CD_Prompt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Countdown_PromptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Countdown_Prompt"-------
for thisComponent in Countdown_PromptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('CD_Prompt.started', CD_Prompt.tStartRefresh)
thisExp.addData('CD_Prompt.stopped', CD_Prompt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
countdownTrials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='countdownTrials')
thisExp.addLoop(countdownTrials)  # add the loop to the experiment
thisCountdownTrial = countdownTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCountdownTrial.rgb)
if thisCountdownTrial != None:
    for paramName in thisCountdownTrial:
        exec('{} = thisCountdownTrial[paramName]'.format(paramName))

for thisCountdownTrial in countdownTrials:
    currentLoop = countdownTrials
    # abbreviate parameter names if possible (e.g. rgb = thisCountdownTrial.rgb)
    if thisCountdownTrial != None:
        for paramName in thisCountdownTrial:
            exec('{} = thisCountdownTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Count_down"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Count_downComponents = [Count_back_from_onehundred, text_2]
    for thisComponent in Count_downComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Count_downClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Count_down"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Count_downClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Count_downClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Count_back_from_onehundred* updates
        if Count_back_from_onehundred.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Count_back_from_onehundred.frameNStart = frameN  # exact frame index
            Count_back_from_onehundred.tStart = t  # local t and not account for scr refresh
            Count_back_from_onehundred.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Count_back_from_onehundred, 'tStartRefresh')  # time at next scr refresh
            Count_back_from_onehundred.setAutoDraw(True)
        if Count_back_from_onehundred.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Count_back_from_onehundred.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                Count_back_from_onehundred.tStop = t  # not accounting for scr refresh
                Count_back_from_onehundred.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Count_back_from_onehundred, 'tStopRefresh')  # time at next scr refresh
                Count_back_from_onehundred.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count_downComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Count_down"-------
    for thisComponent in Count_downComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    countdownTrials.addData('Count_back_from_onehundred.started', Count_back_from_onehundred.tStartRefresh)
    countdownTrials.addData('Count_back_from_onehundred.stopped', Count_back_from_onehundred.tStopRefresh)
    countdownTrials.addData('text_2.started', text_2.tStartRefresh)
    countdownTrials.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'countdownTrials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
