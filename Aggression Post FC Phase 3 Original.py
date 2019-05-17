#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on May 17, 2019, at 16:47
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
import psychopy
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'AggPrototype'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\sumsh86\\OneDrive - Linköpings universitet\\New Psychopy aggression\\AggPrototypeRetaliationTest_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text="Phase 3:\n\nPress 'Spacebar' to continue",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instruction1"
Instruction1Clock = core.Clock()
IRText = visual.TextStim(win=win, name='IRText',
    text='In the next screen, the program will randomly select one of you to start the interaction\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RConnect"
RConnectClock = core.Clock()
WaitingText = visual.TextStim(win=win, name='WaitingText',
    text='Waiting for the participants...',
    font='Arial',
    pos=(0, 0.3), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
P1 = visual.TextStim(win=win, name='P1',
    text='P1',
    font='Arial',
    pos=(-0.6, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
P2 = visual.TextStim(win=win, name='P2',
    text='P2',
    font='Arial',
    pos=(-0.2, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
User = visual.TextStim(win=win, name='User',
    text='P3 (YOU)',
    font='Arial',
    pos=(0.2, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
P4 = visual.TextStim(win=win, name='P4',
    text='P4',
    font='Arial',
    pos=(0.6, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
P1G = visual.Polygon(
    win=win, name='P1G',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(-0.6, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
P1R = visual.Polygon(
    win=win, name='P1R',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(-0.6, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
P2G = visual.Polygon(
    win=win, name='P2G',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(-0.2, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
P2R = visual.Polygon(
    win=win, name='P2R',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(-0.2, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
UserG = visual.Polygon(
    win=win, name='UserG',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(0.2, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
P4G = visual.Polygon(
    win=win, name='P4G',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(0.6, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
P4R = visual.Polygon(
    win=win, name='P4R',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(0.6, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)

# Initialize components for Routine "SelectionConfirmation"
SelectionConfirmationClock = core.Clock()
Selection = visual.TextStim(win=win, name='Selection',
    text='You got selected to give shocks to the other three participants\n\nPress the spacebar to continue!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstructionShockDelivery"
InstructionShockDeliveryClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="How to deliver shocks:\n\nUse the NumPad\nPress '0' for ZERO shocks\nPress '1' for ONE shock\nPress '2' for TWO shocks\n\nPress the'Spacebar' when you are ready to continue",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
Cross = visual.ShapeStim(
    win=win, name='Cross', vertices='cross',
    size=(0.02, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Retaliation"
RetaliationClock = core.Clock()
RetaliationImages = visual.ImageStim(
    win=win,
    name='RetaliationImages', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(360, 450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
RetaliationReminder = visual.TextStim(win=win, name='RetaliationReminder',
    text="Press '0' for NO shocks\nPress '1' for ONE shock\nPress '2' for TWO shocks",
    font='Arial',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text='Thank you for the participation\n\nPlease contact the researcher',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
t = 0
WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WelcomeContinue = keyboard.Keyboard()
# keep track of which components have finished
WelcomeScreenComponents = [WelcomeText, WelcomeContinue]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if t >= 0.0 and WelcomeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeText.tStart = t  # not accounting for scr refresh
        WelcomeText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeContinue* updates
    if t >= 0.0 and WelcomeContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeContinue.tStart = t  # not accounting for scr refresh
        WelcomeContinue.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WelcomeContinue, 'tStartRefresh')  # time at next scr refresh
        WelcomeContinue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(WelcomeContinue.clock.reset)  # t=0 on next screen flip
        WelcomeContinue.clearEvents(eventType='keyboard')
    if WelcomeContinue.status == STARTED:
        theseKeys = WelcomeContinue.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            WelcomeContinue.keys = theseKeys.name  # just the last key pressed
            WelcomeContinue.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)
# check responses
if WelcomeContinue.keys in ['', [], None]:  # No response was made
    WelcomeContinue.keys = None
thisExp.addData('WelcomeContinue.keys',WelcomeContinue.keys)
if WelcomeContinue.keys != None:  # we had a response
    thisExp.addData('WelcomeContinue.rt', WelcomeContinue.rt)
thisExp.addData('WelcomeContinue.started', WelcomeContinue.tStartRefresh)
thisExp.addData('WelcomeContinue.stopped', WelcomeContinue.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
t = 0
Blank500Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [BlankText]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BlankText* updates
    if t >= 0.0 and BlankText.status == NOT_STARTED:
        # keep track of start time/frame for later
        BlankText.tStart = t  # not accounting for scr refresh
        BlankText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(BlankText, 'tStartRefresh')  # time at next scr refresh
        BlankText.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if BlankText.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        BlankText.tStop = t  # not accounting for scr refresh
        BlankText.frameNStop = frameN  # exact frame index
        win.timeOnFlip(BlankText, 'tStopRefresh')  # time at next scr refresh
        BlankText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BlankText.started', BlankText.tStartRefresh)
thisExp.addData('BlankText.stopped', BlankText.tStopRefresh)

# ------Prepare to start Routine "Instruction1"-------
t = 0
Instruction1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
IRContinue = keyboard.Keyboard()
# keep track of which components have finished
Instruction1Components = [IRText, IRContinue]
for thisComponent in Instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction1"-------
while continueRoutine:
    # get current time
    t = Instruction1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IRText* updates
    if t >= 0.0 and IRText.status == NOT_STARTED:
        # keep track of start time/frame for later
        IRText.tStart = t  # not accounting for scr refresh
        IRText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(IRText, 'tStartRefresh')  # time at next scr refresh
        IRText.setAutoDraw(True)
    
    # *IRContinue* updates
    if t >= 0.0 and IRContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        IRContinue.tStart = t  # not accounting for scr refresh
        IRContinue.frameNStart = frameN  # exact frame index
        win.timeOnFlip(IRContinue, 'tStartRefresh')  # time at next scr refresh
        IRContinue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(IRContinue.clock.reset)  # t=0 on next screen flip
        IRContinue.clearEvents(eventType='keyboard')
    if IRContinue.status == STARTED:
        theseKeys = IRContinue.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            IRContinue.keys = theseKeys.name  # just the last key pressed
            IRContinue.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction1"-------
for thisComponent in Instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IRText.started', IRText.tStartRefresh)
thisExp.addData('IRText.stopped', IRText.tStopRefresh)
# check responses
if IRContinue.keys in ['', [], None]:  # No response was made
    IRContinue.keys = None
thisExp.addData('IRContinue.keys',IRContinue.keys)
if IRContinue.keys != None:  # we had a response
    thisExp.addData('IRContinue.rt', IRContinue.rt)
thisExp.addData('IRContinue.started', IRContinue.tStartRefresh)
thisExp.addData('IRContinue.stopped', IRContinue.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
t = 0
Blank500Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [BlankText]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BlankText* updates
    if t >= 0.0 and BlankText.status == NOT_STARTED:
        # keep track of start time/frame for later
        BlankText.tStart = t  # not accounting for scr refresh
        BlankText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(BlankText, 'tStartRefresh')  # time at next scr refresh
        BlankText.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if BlankText.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        BlankText.tStop = t  # not accounting for scr refresh
        BlankText.frameNStop = frameN  # exact frame index
        win.timeOnFlip(BlankText, 'tStopRefresh')  # time at next scr refresh
        BlankText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BlankText.started', BlankText.tStartRefresh)
thisExp.addData('BlankText.stopped', BlankText.tStopRefresh)

# ------Prepare to start Routine "RConnect"-------
t = 0
RConnectClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
# keep track of which components have finished
RConnectComponents = [WaitingText, P1, P2, User, P4, P1G, P1R, P2G, P2R, UserG, P4G, P4R]
for thisComponent in RConnectComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "RConnect"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = RConnectClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WaitingText* updates
    if t >= 0.0 and WaitingText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WaitingText.tStart = t  # not accounting for scr refresh
        WaitingText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WaitingText, 'tStartRefresh')  # time at next scr refresh
        WaitingText.setAutoDraw(True)
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if WaitingText.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        WaitingText.tStop = t  # not accounting for scr refresh
        WaitingText.frameNStop = frameN  # exact frame index
        win.timeOnFlip(WaitingText, 'tStopRefresh')  # time at next scr refresh
        WaitingText.setAutoDraw(False)
    
    # *P1* updates
    if t >= 0.0 and P1.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1.tStart = t  # not accounting for scr refresh
        P1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P1, 'tStartRefresh')  # time at next scr refresh
        P1.setAutoDraw(True)
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P1.tStop = t  # not accounting for scr refresh
        P1.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P1, 'tStopRefresh')  # time at next scr refresh
        P1.setAutoDraw(False)
    
    # *P2* updates
    if t >= 0.0 and P2.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2.tStart = t  # not accounting for scr refresh
        P2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P2, 'tStartRefresh')  # time at next scr refresh
        P2.setAutoDraw(True)
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P2.tStop = t  # not accounting for scr refresh
        P2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P2, 'tStopRefresh')  # time at next scr refresh
        P2.setAutoDraw(False)
    
    # *User* updates
    if t >= 0.0 and User.status == NOT_STARTED:
        # keep track of start time/frame for later
        User.tStart = t  # not accounting for scr refresh
        User.frameNStart = frameN  # exact frame index
        win.timeOnFlip(User, 'tStartRefresh')  # time at next scr refresh
        User.setAutoDraw(True)
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if User.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        User.tStop = t  # not accounting for scr refresh
        User.frameNStop = frameN  # exact frame index
        win.timeOnFlip(User, 'tStopRefresh')  # time at next scr refresh
        User.setAutoDraw(False)
    
    # *P4* updates
    if t >= 0.0 and P4.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4.tStart = t  # not accounting for scr refresh
        P4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P4, 'tStartRefresh')  # time at next scr refresh
        P4.setAutoDraw(True)
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P4.tStop = t  # not accounting for scr refresh
        P4.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P4, 'tStopRefresh')  # time at next scr refresh
        P4.setAutoDraw(False)
    
    # *P1G* updates
    if t >= 5.5 and P1G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1G.tStart = t  # not accounting for scr refresh
        P1G.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P1G, 'tStartRefresh')  # time at next scr refresh
        P1G.setAutoDraw(True)
    frameRemains = 5.5 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1G.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P1G.tStop = t  # not accounting for scr refresh
        P1G.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P1G, 'tStopRefresh')  # time at next scr refresh
        P1G.setAutoDraw(False)
    
    # *P1R* updates
    if t >= 0.0 and P1R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1R.tStart = t  # not accounting for scr refresh
        P1R.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P1R, 'tStartRefresh')  # time at next scr refresh
        P1R.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1R.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P1R.tStop = t  # not accounting for scr refresh
        P1R.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P1R, 'tStopRefresh')  # time at next scr refresh
        P1R.setAutoDraw(False)
    
    # *P2G* updates
    if t >= 6 and P2G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2G.tStart = t  # not accounting for scr refresh
        P2G.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P2G, 'tStartRefresh')  # time at next scr refresh
        P2G.setAutoDraw(True)
    frameRemains = 6 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2G.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P2G.tStop = t  # not accounting for scr refresh
        P2G.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P2G, 'tStopRefresh')  # time at next scr refresh
        P2G.setAutoDraw(False)
    
    # *P2R* updates
    if t >= 0.0 and P2R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2R.tStart = t  # not accounting for scr refresh
        P2R.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P2R, 'tStartRefresh')  # time at next scr refresh
        P2R.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2R.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P2R.tStop = t  # not accounting for scr refresh
        P2R.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P2R, 'tStopRefresh')  # time at next scr refresh
        P2R.setAutoDraw(False)
    
    # *UserG* updates
    if t >= 0.0 and UserG.status == NOT_STARTED:
        # keep track of start time/frame for later
        UserG.tStart = t  # not accounting for scr refresh
        UserG.frameNStart = frameN  # exact frame index
        win.timeOnFlip(UserG, 'tStartRefresh')  # time at next scr refresh
        UserG.setAutoDraw(True)
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if UserG.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        UserG.tStop = t  # not accounting for scr refresh
        UserG.frameNStop = frameN  # exact frame index
        win.timeOnFlip(UserG, 'tStopRefresh')  # time at next scr refresh
        UserG.setAutoDraw(False)
    
    # *P4G* updates
    if t >= 2 and P4G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4G.tStart = t  # not accounting for scr refresh
        P4G.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P4G, 'tStartRefresh')  # time at next scr refresh
        P4G.setAutoDraw(True)
    frameRemains = 2 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4G.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P4G.tStop = t  # not accounting for scr refresh
        P4G.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P4G, 'tStopRefresh')  # time at next scr refresh
        P4G.setAutoDraw(False)
    
    # *P4R* updates
    if t >= 0.0 and P4R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4R.tStart = t  # not accounting for scr refresh
        P4R.frameNStart = frameN  # exact frame index
        win.timeOnFlip(P4R, 'tStartRefresh')  # time at next scr refresh
        P4R.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4R.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        P4R.tStop = t  # not accounting for scr refresh
        P4R.frameNStop = frameN  # exact frame index
        win.timeOnFlip(P4R, 'tStopRefresh')  # time at next scr refresh
        P4R.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RConnectComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RConnect"-------
for thisComponent in RConnectComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WaitingText.started', WaitingText.tStartRefresh)
thisExp.addData('WaitingText.stopped', WaitingText.tStopRefresh)
thisExp.addData('P1.started', P1.tStartRefresh)
thisExp.addData('P1.stopped', P1.tStopRefresh)
thisExp.addData('P2.started', P2.tStartRefresh)
thisExp.addData('P2.stopped', P2.tStopRefresh)
thisExp.addData('User.started', User.tStartRefresh)
thisExp.addData('User.stopped', User.tStopRefresh)
thisExp.addData('P4.started', P4.tStartRefresh)
thisExp.addData('P4.stopped', P4.tStopRefresh)
thisExp.addData('P1G.started', P1G.tStartRefresh)
thisExp.addData('P1G.stopped', P1G.tStopRefresh)
thisExp.addData('P1R.started', P1R.tStartRefresh)
thisExp.addData('P1R.stopped', P1R.tStopRefresh)
thisExp.addData('P2G.started', P2G.tStartRefresh)
thisExp.addData('P2G.stopped', P2G.tStopRefresh)
thisExp.addData('P2R.started', P2R.tStartRefresh)
thisExp.addData('P2R.stopped', P2R.tStopRefresh)
thisExp.addData('UserG.started', UserG.tStartRefresh)
thisExp.addData('UserG.stopped', UserG.tStopRefresh)
thisExp.addData('P4G.started', P4G.tStartRefresh)
thisExp.addData('P4G.stopped', P4G.tStopRefresh)
thisExp.addData('P4R.started', P4R.tStartRefresh)
thisExp.addData('P4R.stopped', P4R.tStopRefresh)

# ------Prepare to start Routine "SelectionConfirmation"-------
t = 0
SelectionConfirmationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp = keyboard.Keyboard()
# keep track of which components have finished
SelectionConfirmationComponents = [Selection, key_resp]
for thisComponent in SelectionConfirmationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "SelectionConfirmation"-------
while continueRoutine:
    # get current time
    t = SelectionConfirmationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Selection* updates
    if t >= 0.0 and Selection.status == NOT_STARTED:
        # keep track of start time/frame for later
        Selection.tStart = t  # not accounting for scr refresh
        Selection.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Selection, 'tStartRefresh')  # time at next scr refresh
        Selection.setAutoDraw(True)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SelectionConfirmationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SelectionConfirmation"-------
for thisComponent in SelectionConfirmationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Selection.started', Selection.tStartRefresh)
thisExp.addData('Selection.stopped', Selection.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "SelectionConfirmation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionShockDelivery"-------
t = 0
InstructionShockDeliveryClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
space = keyboard.Keyboard()
# keep track of which components have finished
InstructionShockDeliveryComponents = [text, space]
for thisComponent in InstructionShockDeliveryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstructionShockDelivery"-------
while continueRoutine:
    # get current time
    t = InstructionShockDeliveryClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *space* updates
    if t >= 0.0 and space.status == NOT_STARTED:
        # keep track of start time/frame for later
        space.tStart = t  # not accounting for scr refresh
        space.frameNStart = frameN  # exact frame index
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        space.clearEvents(eventType='keyboard')
    if space.status == STARTED:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            space.keys = theseKeys.name  # just the last key pressed
            space.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionShockDeliveryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionShockDelivery"-------
for thisComponent in InstructionShockDeliveryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructionShockDelivery" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RetaliationLoop = data.TrialHandler(nReps=6, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageFiles.xlsx'),
    seed=None, name='RetaliationLoop')
thisExp.addLoop(RetaliationLoop)  # add the loop to the experiment
thisRetaliationLoop = RetaliationLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetaliationLoop.rgb)
if thisRetaliationLoop != None:
    for paramName in thisRetaliationLoop:
        exec('{} = thisRetaliationLoop[paramName]'.format(paramName))

for thisRetaliationLoop in RetaliationLoop:
    currentLoop = RetaliationLoop
    # abbreviate parameter names if possible (e.g. rgb = thisRetaliationLoop.rgb)
    if thisRetaliationLoop != None:
        for paramName in thisRetaliationLoop:
            exec('{} = thisRetaliationLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    t = 0
    Blank500Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [BlankText]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankText* updates
        if t >= 0.0 and BlankText.status == NOT_STARTED:
            # keep track of start time/frame for later
            BlankText.tStart = t  # not accounting for scr refresh
            BlankText.frameNStart = frameN  # exact frame index
            win.timeOnFlip(BlankText, 'tStartRefresh')  # time at next scr refresh
            BlankText.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if BlankText.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            BlankText.tStop = t  # not accounting for scr refresh
            BlankText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(BlankText, 'tStopRefresh')  # time at next scr refresh
            BlankText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RetaliationLoop.addData('BlankText.started', BlankText.tStartRefresh)
    RetaliationLoop.addData('BlankText.stopped', BlankText.tStopRefresh)
    
    # ------Prepare to start Routine "FixCross"-------
    t = 0
    FixCrossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCrossComponents = [Cross]
    for thisComponent in FixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "FixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # not accounting for scr refresh
            Cross.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Cross.tStop = t  # not accounting for scr refresh
            Cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
            Cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross"-------
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RetaliationLoop.addData('Cross.started', Cross.tStartRefresh)
    RetaliationLoop.addData('Cross.stopped', Cross.tStopRefresh)
    
    # ------Prepare to start Routine "Retaliation"-------
    t = 0
    RetaliationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.500000)
    # update component parameters for each repeat
    RetaliationImages.setImage(ImageFile)
    RetaliationKey = keyboard.Keyboard()
    # keep track of which components have finished
    RetaliationComponents = [RetaliationImages, RetaliationReminder, RetaliationKey]
    for thisComponent in RetaliationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Retaliation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RetaliationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RetaliationImages* updates
        if t >= 0.75 and RetaliationImages.status == NOT_STARTED:
            # keep track of start time/frame for later
            RetaliationImages.tStart = t  # not accounting for scr refresh
            RetaliationImages.frameNStart = frameN  # exact frame index
            win.timeOnFlip(RetaliationImages, 'tStartRefresh')  # time at next scr refresh
            RetaliationImages.setAutoDraw(True)
        frameRemains = 0.75 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if RetaliationImages.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            RetaliationImages.tStop = t  # not accounting for scr refresh
            RetaliationImages.frameNStop = frameN  # exact frame index
            win.timeOnFlip(RetaliationImages, 'tStopRefresh')  # time at next scr refresh
            RetaliationImages.setAutoDraw(False)
        
        # *RetaliationReminder* updates
        if t >= 3 and RetaliationReminder.status == NOT_STARTED:
            # keep track of start time/frame for later
            RetaliationReminder.tStart = t  # not accounting for scr refresh
            RetaliationReminder.frameNStart = frameN  # exact frame index
            win.timeOnFlip(RetaliationReminder, 'tStartRefresh')  # time at next scr refresh
            RetaliationReminder.setAutoDraw(True)
        frameRemains = 3 + 5.00- win.monitorFramePeriod * 0.75  # most of one frame period left
        if RetaliationReminder.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            RetaliationReminder.tStop = t  # not accounting for scr refresh
            RetaliationReminder.frameNStop = frameN  # exact frame index
            win.timeOnFlip(RetaliationReminder, 'tStopRefresh')  # time at next scr refresh
            RetaliationReminder.setAutoDraw(False)
        
        # *RetaliationKey* updates
        if t >= 0.75 and RetaliationKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            RetaliationKey.tStart = t  # not accounting for scr refresh
            RetaliationKey.frameNStart = frameN  # exact frame index
            win.timeOnFlip(RetaliationKey, 'tStartRefresh')  # time at next scr refresh
            RetaliationKey.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(RetaliationKey.clock.reset)  # t=0 on next screen flip
            RetaliationKey.clearEvents(eventType='keyboard')
        frameRemains = 0.75 + 7.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if RetaliationKey.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            RetaliationKey.tStop = t  # not accounting for scr refresh
            RetaliationKey.frameNStop = frameN  # exact frame index
            win.timeOnFlip(RetaliationKey, 'tStopRefresh')  # time at next scr refresh
            RetaliationKey.status = FINISHED
        if RetaliationKey.status == STARTED:
            theseKeys = RetaliationKey.getKeys(keyList=['num_0', 'num_1', 'num_2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                RetaliationKey.keys = theseKeys.name  # just the last key pressed
                RetaliationKey.rt = theseKeys.rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetaliationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Retaliation"-------
    for thisComponent in RetaliationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RetaliationLoop.addData('RetaliationImages.started', RetaliationImages.tStartRefresh)
    RetaliationLoop.addData('RetaliationImages.stopped', RetaliationImages.tStopRefresh)
    RetaliationLoop.addData('RetaliationReminder.started', RetaliationReminder.tStartRefresh)
    RetaliationLoop.addData('RetaliationReminder.stopped', RetaliationReminder.tStopRefresh)
    # check responses
    if RetaliationKey.keys in ['', [], None]:  # No response was made
        RetaliationKey.keys = None
    RetaliationLoop.addData('RetaliationKey.keys',RetaliationKey.keys)
    if RetaliationKey.keys != None:  # we had a response
        RetaliationLoop.addData('RetaliationKey.rt', RetaliationKey.rt)
    RetaliationLoop.addData('RetaliationKey.started', RetaliationKey.tStartRefresh)
    RetaliationLoop.addData('RetaliationKey.stopped', RetaliationKey.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6 repeats of 'RetaliationLoop'


# ------Prepare to start Routine "EndScreen"-------
t = 0
EndScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [EndText]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndText* updates
    if t >= 0.0 and EndText.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndText.tStart = t  # not accounting for scr refresh
        EndText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(EndText, 'tStartRefresh')  # time at next scr refresh
        EndText.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndText.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        EndText.tStop = t  # not accounting for scr refresh
        EndText.frameNStop = frameN  # exact frame index
        win.timeOnFlip(EndText, 'tStopRefresh')  # time at next scr refresh
        EndText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndText.started', EndText.tStartRefresh)
thisExp.addData('EndText.stopped', EndText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
