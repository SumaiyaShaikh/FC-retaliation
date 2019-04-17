#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.4),
    on March 06, 2019, at 15:35
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.4'
expName = 'AggPrototype'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='C:\\Users\\sumsh86\\Desktop\\aggression\\AggPrototypeConditioning_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "codeInit"
codeInitClock = core.Clock()
import random

#randomise the seed
random.seed()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Part 2: Start of Pairing experiment',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WelcomeProceed = visual.TextStim(win=win, name='WelcomeProceed',
    text="Press 'Spacebar' to continue",
    font='Arial',
    pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstructionConditioning1"
InstructionConditioning1Clock = core.Clock()
ICText1 = visual.TextStim(win=win, name='ICText1',
    text='You will now see images of thoer players interacting with you in this experiment.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ICProceed1 = visual.TextStim(win=win, name='ICProceed1',
    text="Press 'Spacebar' to continue",
    font='Arial',
    pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstructionConditioning2"
InstructionConditioning2Clock = core.Clock()
ICText2 = visual.TextStim(win=win, name='ICText2',
    text='This part of the experiment has two phases.\n\nOne out of the four players will randomly be assigned to start the experiment. \n\nThe selected payer will start the experiment first.\n\nIn phase two the randomised selection will start all over again',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ICProceed2 = visual.TextStim(win=win, name='ICProceed2',
    text="Press 'Enter' when ready",
    font='Arial',
    pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ICConnect"
ICConnectClock = core.Clock()
WaitingText = visual.TextStim(win=win, name='WaitingText',
    text='Waiting for the randomised assignment ',
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
P2R = visual.Polygon(
    win=win, name='P2R',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(-0.2, -0.1),
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
UserG = visual.Polygon(
    win=win, name='UserG',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(0.2, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
P4R = visual.Polygon(
    win=win, name='P4R',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(0.6, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
P4G = visual.Polygon(
    win=win, name='P4G',
    edges=16, size=(0.09, 0.14),
    ori=0, pos=(0.6, -0.1),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankText = visual.TextStim(win=win, name='BlankText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ConditioningStart"
ConditioningStartClock = core.Clock()
CSText = visual.TextStim(win=win, name='CSText',
    text='YOU have been selected by the system to start the experiment.\n\nYou will play against the four other players.\n ',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
CSProceed = visual.TextStim(win=win, name='CSProceed',
    text="Press 'Spacebar' when ready to start the session",
    font='Arial',
    pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

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

# Initialize components for Routine "Conditioning"
ConditioningClock = core.Clock()
p_port = parallel.ParallelPort(address='0x0378')
ConditionImages = visual.ImageStim(
    win=win, name='ConditionImages',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(360, 450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

textZap = visual.TextStim(win=win, name='textZap',
    text='Shock trigger!',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text='Thank you for participating.\nThe last phase will begin shortly.\n\nPlease contact the staff to assist you.',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "codeInit"-------
t = 0
codeInitClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
codeInitComponents = []
for thisComponent in codeInitComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "codeInit"-------
while continueRoutine:
    # get current time
    t = codeInitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in codeInitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "codeInit"-------
for thisComponent in codeInitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "codeInit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen"-------
t = 0
WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WelcomeContinue = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeScreenComponents = [WelcomeText, WelcomeContinue, WelcomeProceed]
for thisComponent in WelcomeScreenComponents:
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
        WelcomeText.tStart = t
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeContinue* updates
    if t >= 0.0 and WelcomeContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeContinue.tStart = t
        WelcomeContinue.frameNStart = frameN  # exact frame index
        WelcomeContinue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(WelcomeContinue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if WelcomeContinue.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            WelcomeContinue.keys = theseKeys[-1]  # just the last key pressed
            WelcomeContinue.rt = WelcomeContinue.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *WelcomeProceed* updates
    if t >= 0.0 and WelcomeProceed.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeProceed.tStart = t
        WelcomeProceed.frameNStart = frameN  # exact frame index
        WelcomeProceed.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if WelcomeContinue.keys in ['', [], None]:  # No response was made
    WelcomeContinue.keys=None
thisExp.addData('WelcomeContinue.keys',WelcomeContinue.keys)
if WelcomeContinue.keys != None:  # we had a response
    thisExp.addData('WelcomeContinue.rt', WelcomeContinue.rt)
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
        BlankText.tStart = t
        BlankText.frameNStart = frameN  # exact frame index
        BlankText.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if BlankText.status == STARTED and t >= frameRemains:
        BlankText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

# ------Prepare to start Routine "InstructionConditioning1"-------
t = 0
InstructionConditioning1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ICContinue1 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionConditioning1Components = [ICText1, ICContinue1, ICProceed1]
for thisComponent in InstructionConditioning1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstructionConditioning1"-------
while continueRoutine:
    # get current time
    t = InstructionConditioning1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ICText1* updates
    if t >= 0.0 and ICText1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ICText1.tStart = t
        ICText1.frameNStart = frameN  # exact frame index
        ICText1.setAutoDraw(True)
    
    # *ICContinue1* updates
    if t >= 0.0 and ICContinue1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ICContinue1.tStart = t
        ICContinue1.frameNStart = frameN  # exact frame index
        ICContinue1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ICContinue1.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ICContinue1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ICContinue1.keys = theseKeys[-1]  # just the last key pressed
            ICContinue1.rt = ICContinue1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *ICProceed1* updates
    if t >= 0.0 and ICProceed1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ICProceed1.tStart = t
        ICProceed1.frameNStart = frameN  # exact frame index
        ICProceed1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionConditioning1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionConditioning1"-------
for thisComponent in InstructionConditioning1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ICContinue1.keys in ['', [], None]:  # No response was made
    ICContinue1.keys=None
thisExp.addData('ICContinue1.keys',ICContinue1.keys)
if ICContinue1.keys != None:  # we had a response
    thisExp.addData('ICContinue1.rt', ICContinue1.rt)
thisExp.nextEntry()
# the Routine "InstructionConditioning1" was not non-slip safe, so reset the non-slip timer
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
        BlankText.tStart = t
        BlankText.frameNStart = frameN  # exact frame index
        BlankText.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if BlankText.status == STARTED and t >= frameRemains:
        BlankText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

# ------Prepare to start Routine "InstructionConditioning2"-------
t = 0
InstructionConditioning2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ICContinue2 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionConditioning2Components = [ICText2, ICContinue2, ICProceed2]
for thisComponent in InstructionConditioning2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstructionConditioning2"-------
while continueRoutine:
    # get current time
    t = InstructionConditioning2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ICText2* updates
    if t >= 0.0 and ICText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ICText2.tStart = t
        ICText2.frameNStart = frameN  # exact frame index
        ICText2.setAutoDraw(True)
    
    # *ICContinue2* updates
    if t >= 0.0 and ICContinue2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ICContinue2.tStart = t
        ICContinue2.frameNStart = frameN  # exact frame index
        ICContinue2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ICContinue2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ICContinue2.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ICContinue2.keys = theseKeys[-1]  # just the last key pressed
            ICContinue2.rt = ICContinue2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *ICProceed2* updates
    if t >= 0.0 and ICProceed2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ICProceed2.tStart = t
        ICProceed2.frameNStart = frameN  # exact frame index
        ICProceed2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionConditioning2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionConditioning2"-------
for thisComponent in InstructionConditioning2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ICContinue2.keys in ['', [], None]:  # No response was made
    ICContinue2.keys=None
thisExp.addData('ICContinue2.keys',ICContinue2.keys)
if ICContinue2.keys != None:  # we had a response
    thisExp.addData('ICContinue2.rt', ICContinue2.rt)
thisExp.nextEntry()
# the Routine "InstructionConditioning2" was not non-slip safe, so reset the non-slip timer
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
        BlankText.tStart = t
        BlankText.frameNStart = frameN  # exact frame index
        BlankText.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if BlankText.status == STARTED and t >= frameRemains:
        BlankText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

# ------Prepare to start Routine "ICConnect"-------
t = 0
ICConnectClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
ICConnectComponents = [WaitingText, P1, P2, User, P4, P1G, P2R, P2G, UserG, P4R, P4G]
for thisComponent in ICConnectComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ICConnect"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ICConnectClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WaitingText* updates
    if t >= 0.0 and WaitingText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WaitingText.tStart = t
        WaitingText.frameNStart = frameN  # exact frame index
        WaitingText.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if WaitingText.status == STARTED and t >= frameRemains:
        WaitingText.setAutoDraw(False)
    
    # *P1* updates
    if t >= 0.0 and P1.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1.tStart = t
        P1.frameNStart = frameN  # exact frame index
        P1.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1.status == STARTED and t >= frameRemains:
        P1.setAutoDraw(False)
    
    # *P2* updates
    if t >= 0.0 and P2.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2.tStart = t
        P2.frameNStart = frameN  # exact frame index
        P2.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2.status == STARTED and t >= frameRemains:
        P2.setAutoDraw(False)
    
    # *User* updates
    if t >= 0.0 and User.status == NOT_STARTED:
        # keep track of start time/frame for later
        User.tStart = t
        User.frameNStart = frameN  # exact frame index
        User.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if User.status == STARTED and t >= frameRemains:
        User.setAutoDraw(False)
    
    # *P4* updates
    if t >= 0.0 and P4.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4.tStart = t
        P4.frameNStart = frameN  # exact frame index
        P4.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4.status == STARTED and t >= frameRemains:
        P4.setAutoDraw(False)
    
    # *P1G* updates
    if t >= 0.0 and P1G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1G.tStart = t
        P1G.frameNStart = frameN  # exact frame index
        P1G.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1G.status == STARTED and t >= frameRemains:
        P1G.setAutoDraw(False)
    
    # *P2R* updates
    if t >= 0.0 and P2R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2R.tStart = t
        P2R.frameNStart = frameN  # exact frame index
        P2R.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2R.status == STARTED and t >= frameRemains:
        P2R.setAutoDraw(False)
    
    # *P2G* updates
    if t >= 4 and P2G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2G.tStart = t
        P2G.frameNStart = frameN  # exact frame index
        P2G.setAutoDraw(True)
    frameRemains = 4 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2G.status == STARTED and t >= frameRemains:
        P2G.setAutoDraw(False)
    
    # *UserG* updates
    if t >= 0.0 and UserG.status == NOT_STARTED:
        # keep track of start time/frame for later
        UserG.tStart = t
        UserG.frameNStart = frameN  # exact frame index
        UserG.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if UserG.status == STARTED and t >= frameRemains:
        UserG.setAutoDraw(False)
    
    # *P4R* updates
    if t >= 0.0 and P4R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4R.tStart = t
        P4R.frameNStart = frameN  # exact frame index
        P4R.setAutoDraw(True)
    frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4R.status == STARTED and t >= frameRemains:
        P4R.setAutoDraw(False)
    
    # *P4G* updates
    if t >= 2.5 and P4G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4G.tStart = t
        P4G.frameNStart = frameN  # exact frame index
        P4G.setAutoDraw(True)
    frameRemains = 2.5 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4G.status == STARTED and t >= frameRemains:
        P4G.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ICConnectComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ICConnect"-------
for thisComponent in ICConnectComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
        BlankText.tStart = t
        BlankText.frameNStart = frameN  # exact frame index
        BlankText.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if BlankText.status == STARTED and t >= frameRemains:
        BlankText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

# ------Prepare to start Routine "ConditioningStart"-------
t = 0
ConditioningStartClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
CSContinue = event.BuilderKeyResponse()
# keep track of which components have finished
ConditioningStartComponents = [CSText, CSContinue, CSProceed]
for thisComponent in ConditioningStartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ConditioningStart"-------
while continueRoutine:
    # get current time
    t = ConditioningStartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CSText* updates
    if t >= 0.0 and CSText.status == NOT_STARTED:
        # keep track of start time/frame for later
        CSText.tStart = t
        CSText.frameNStart = frameN  # exact frame index
        CSText.setAutoDraw(True)
    
    # *CSContinue* updates
    if t >= 0.0 and CSContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        CSContinue.tStart = t
        CSContinue.frameNStart = frameN  # exact frame index
        CSContinue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(CSContinue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if CSContinue.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            CSContinue.keys = theseKeys[-1]  # just the last key pressed
            CSContinue.rt = CSContinue.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *CSProceed* updates
    if t >= 0.0 and CSProceed.status == NOT_STARTED:
        # keep track of start time/frame for later
        CSProceed.tStart = t
        CSProceed.frameNStart = frameN  # exact frame index
        CSProceed.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ConditioningStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ConditioningStart"-------
for thisComponent in ConditioningStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if CSContinue.keys in ['', [], None]:  # No response was made
    CSContinue.keys=None
thisExp.addData('CSContinue.keys',CSContinue.keys)
if CSContinue.keys != None:  # we had a response
    thisExp.addData('CSContinue.rt', CSContinue.rt)
thisExp.nextEntry()
# the Routine "ConditioningStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ConditioningLoop = data.TrialHandler(nReps=6, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageFiles.xlsx'),
    seed=None, name='ConditioningLoop')
thisExp.addLoop(ConditioningLoop)  # add the loop to the experiment
thisConditioningLoop = ConditioningLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConditioningLoop.rgb)
if thisConditioningLoop != None:
    for paramName in thisConditioningLoop:
        exec('{} = thisConditioningLoop[paramName]'.format(paramName))

for thisConditioningLoop in ConditioningLoop:
    currentLoop = ConditioningLoop
    # abbreviate parameter names if possible (e.g. rgb = thisConditioningLoop.rgb)
    if thisConditioningLoop != None:
        for paramName in thisConditioningLoop:
            exec('{} = thisConditioningLoop[paramName]'.format(paramName))
    
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
            BlankText.tStart = t
            BlankText.frameNStart = frameN  # exact frame index
            BlankText.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if BlankText.status == STARTED and t >= frameRemains:
            BlankText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
            Cross.tStart = t
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Cross.status == STARTED and t >= frameRemains:
            Cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    # ------Prepare to start Routine "Conditioning"-------
    t = 0
    ConditioningClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ConditionImages.setImage(ImageFile)
    randomTime = random.uniform(1.1, 5)
    # keep track of which components have finished
    ConditioningComponents = [p_port, ConditionImages, textZap]
    for thisComponent in ConditioningComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Conditioning"-------
    while continueRoutine:
        # get current time
        t = ConditioningClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *p_port* updates
        if t >= 0.0 and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port.tStart = t
            p_port.frameNStart = frameN  # exact frame index
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(1))
        frameRemains = 0.0 + 2.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if p_port.status == STARTED and t >= frameRemains:
            p_port.status = FINISHED
            win.callOnFlip(p_port.setData, int(0))
        
        # *ConditionImages* updates
        if t >= 0.75 and ConditionImages.status == NOT_STARTED:
            # keep track of start time/frame for later
            ConditionImages.tStart = t
            ConditionImages.frameNStart = frameN  # exact frame index
            ConditionImages.setAutoDraw(True)
        frameRemains = 0.75 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ConditionImages.status == STARTED and t >= frameRemains:
            ConditionImages.setAutoDraw(False)
        
        
        # *textZap* updates
        if t >= randomTime and textZap.status == NOT_STARTED:
            # keep track of start time/frame for later
            textZap.tStart = t
            textZap.frameNStart = frameN  # exact frame index
            textZap.setAutoDraw(True)
        frameRemains = randomTime + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textZap.status == STARTED and t >= frameRemains:
            textZap.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditioningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Conditioning"-------
    for thisComponent in ConditioningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port.status == STARTED:
        win.callOnFlip(p_port.setData, int(0))
    
    # the Routine "Conditioning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6 repeats of 'ConditioningLoop'


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
        EndText.tStart = t
        EndText.frameNStart = frameN  # exact frame index
        EndText.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndText.status == STARTED and t >= frameRemains:
        EndText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
