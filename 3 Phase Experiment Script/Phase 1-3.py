#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.4),
    on June 28, 2019, at 17:24
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
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
                                 originPath='C:\\Users\\sumsh86\\Desktop\\Main AGG codes\\New Psychopy aggression\\3 Phase Experiment Script\\Phase 3 Original_lastrun.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
                              text="Please have a seat\n\n\nPress 'Spacebar' to continue",
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

# Initialize components for Routine "InstructionRetaliation"
InstructionRetaliationClock = core.Clock()
IRText = visual.TextStim(win=win, name='IRText',
                         text="It is now your turn to return shocks to the other players\n\nUse the NumPad\nPress '0' for NO shocks\nPress '1' for ONE shock\nPress '2' for TWO shocks\n\nPress 'Spacebar' when you are ready to continue",
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
                              text='Waiting for players...',
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
                       text='P3 (you)',
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
    win=win, name='RetaliationImages', units='pix',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(360, 450),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
RetaliationReminder = visual.TextStim(win=win, name='RetaliationReminder',
                                      text="Press '0' for NO shocks\nPress '1' for ONE shock\nPress '2' for TWO shocks",
                                      font='Arial',
                                      pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0,
                                      color='white', colorSpace='rgb', opacity=1,
                                      languageStyle='LTR',
                                      depth=-1.0);
Shock0 = visual.ImageStim(
    win=win, name='Shock0',
    image='images/shock0.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.08, 0.1),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Shock1 = visual.ImageStim(
    win=win, name='Shock1',
    image='images/Shock1.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.08, 0.1),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Shock2 = visual.ImageStim(
    win=win, name='Shock2',
    image='images/Shock2.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.08, 0.1),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
                          text='Thank you for participating\n\nPlease contact the researcher',
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
WelcomeContinue = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeScreenComponents = [WelcomeText, WelcomeContinue]
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
    WelcomeContinue.keys = None
thisExp.addData('WelcomeContinue.keys', WelcomeContinue.keys)
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
    frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
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

# ------Prepare to start Routine "InstructionRetaliation"-------
t = 0
InstructionRetaliationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
IRContinue = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionRetaliationComponents = [IRText, IRContinue]
for thisComponent in InstructionRetaliationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstructionRetaliation"-------
while continueRoutine:
    # get current time
    t = InstructionRetaliationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *IRText* updates
    if t >= 0.0 and IRText.status == NOT_STARTED:
        # keep track of start time/frame for later
        IRText.tStart = t
        IRText.frameNStart = frameN  # exact frame index
        IRText.setAutoDraw(True)

    # *IRContinue* updates
    if t >= 0.0 and IRContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        IRContinue.tStart = t
        IRContinue.frameNStart = frameN  # exact frame index
        IRContinue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(IRContinue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if IRContinue.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            IRContinue.keys = theseKeys[-1]  # just the last key pressed
            IRContinue.rt = IRContinue.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionRetaliationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionRetaliation"-------
for thisComponent in InstructionRetaliationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IRContinue.keys in ['', [], None]:  # No response was made
    IRContinue.keys = None
thisExp.addData('IRContinue.keys', IRContinue.keys)
if IRContinue.keys != None:  # we had a response
    thisExp.addData('IRContinue.rt', IRContinue.rt)
thisExp.nextEntry()
# the Routine "InstructionRetaliation" was not non-slip safe, so reset the non-slip timer
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
    frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
        WaitingText.tStart = t
        WaitingText.frameNStart = frameN  # exact frame index
        WaitingText.setAutoDraw(True)
    frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if WaitingText.status == STARTED and t >= frameRemains:
        WaitingText.setAutoDraw(False)

    # *P1* updates
    if t >= 0.0 and P1.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1.tStart = t
        P1.frameNStart = frameN  # exact frame index
        P1.setAutoDraw(True)
    frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1.status == STARTED and t >= frameRemains:
        P1.setAutoDraw(False)

    # *P2* updates
    if t >= 0.0 and P2.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2.tStart = t
        P2.frameNStart = frameN  # exact frame index
        P2.setAutoDraw(True)
    frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2.status == STARTED and t >= frameRemains:
        P2.setAutoDraw(False)

    # *User* updates
    if t >= 0.0 and User.status == NOT_STARTED:
        # keep track of start time/frame for later
        User.tStart = t
        User.frameNStart = frameN  # exact frame index
        User.setAutoDraw(True)
    frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if User.status == STARTED and t >= frameRemains:
        User.setAutoDraw(False)

    # *P4* updates
    if t >= 0.0 and P4.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4.tStart = t
        P4.frameNStart = frameN  # exact frame index
        P4.setAutoDraw(True)
    frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4.status == STARTED and t >= frameRemains:
        P4.setAutoDraw(False)

    # *P1G* updates
    if t >= 5.5 and P1G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1G.tStart = t
        P1G.frameNStart = frameN  # exact frame index
        P1G.setAutoDraw(True)
    frameRemains = 5.5 + 2.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1G.status == STARTED and t >= frameRemains:
        P1G.setAutoDraw(False)

    # *P1R* updates
    if t >= 0.0 and P1R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P1R.tStart = t
        P1R.frameNStart = frameN  # exact frame index
        P1R.setAutoDraw(True)
    frameRemains = 0.0 + 5.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P1R.status == STARTED and t >= frameRemains:
        P1R.setAutoDraw(False)

    # *P2G* updates
    if t >= 6 and P2G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2G.tStart = t
        P2G.frameNStart = frameN  # exact frame index
        P2G.setAutoDraw(True)
    frameRemains = 6 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2G.status == STARTED and t >= frameRemains:
        P2G.setAutoDraw(False)

    # *P2R* updates
    if t >= 0.0 and P2R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P2R.tStart = t
        P2R.frameNStart = frameN  # exact frame index
        P2R.setAutoDraw(True)
    frameRemains = 0.0 + 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P2R.status == STARTED and t >= frameRemains:
        P2R.setAutoDraw(False)

    # *UserG* updates
    if t >= 0.0 and UserG.status == NOT_STARTED:
        # keep track of start time/frame for later
        UserG.tStart = t
        UserG.frameNStart = frameN  # exact frame index
        UserG.setAutoDraw(True)
    frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if UserG.status == STARTED and t >= frameRemains:
        UserG.setAutoDraw(False)

    # *P4G* updates
    if t >= 2 and P4G.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4G.tStart = t
        P4G.frameNStart = frameN  # exact frame index
        P4G.setAutoDraw(True)
    frameRemains = 2 + 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4G.status == STARTED and t >= frameRemains:
        P4G.setAutoDraw(False)

    # *P4R* updates
    if t >= 0.0 and P4R.status == NOT_STARTED:
        # keep track of start time/frame for later
        P4R.tStart = t
        P4R.frameNStart = frameN  # exact frame index
        P4R.setAutoDraw(True)
    frameRemains = 0.0 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if P4R.status == STARTED and t >= frameRemains:
        P4R.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
        frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
        frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
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

    # ------Prepare to start Routine "Retaliation"-------
    t = 0
    RetaliationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    RetaliationImages.setImage(ImageFile)
    RetaliationKey = event.BuilderKeyResponse()
    Shock0.opacity = 0  # start shock0 invisible
    Shock1.opacity = 0  # start shock1 invisible
    Shock2.opacity = 0  # start shock2 invisible

    # keep track of which components have finished
    RetaliationComponents = [RetaliationImages, RetaliationReminder, RetaliationKey, Shock0, Shock1, Shock2]
    for thisComponent in RetaliationComponents:
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
            RetaliationImages.tStart = t
            RetaliationImages.frameNStart = frameN  # exact frame index
            RetaliationImages.setAutoDraw(True)
        frameRemains = 0.75 + 9.25 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if RetaliationImages.status == STARTED and t >= frameRemains:
            RetaliationImages.setAutoDraw(False)

        # *RetaliationReminder* updates
        if t >= 0.6 and RetaliationReminder.status == NOT_STARTED:
            # keep track of start time/frame for later
            RetaliationReminder.tStart = t
            RetaliationReminder.frameNStart = frameN  # exact frame index
            RetaliationReminder.setAutoDraw(True)
        frameRemains = 0.6 + 9.4 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if RetaliationReminder.status == STARTED and t >= frameRemains:
            RetaliationReminder.setAutoDraw(False)

        # *RetaliationKey* updates
        if t >= 0.75 and RetaliationKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            RetaliationKey.tStart = t
            RetaliationKey.frameNStart = frameN  # exact frame index
            RetaliationKey.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(RetaliationKey.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.75 + 9.25 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if RetaliationKey.status == STARTED and t >= frameRemains:
            RetaliationKey.status = FINISHED
        if RetaliationKey.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_0', 'num_1', 'num_2'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                RetaliationKey.keys = theseKeys[-1]  # just the last key pressed
                RetaliationKey.rt = RetaliationKey.clock.getTime()

        # *Shock0* updates
        if t >= 0.0 and Shock0.status == NOT_STARTED:
            # keep track of start time/frame for later
            Shock0.tStart = t
            Shock0.frameNStart = frameN  # exact frame index
            Shock0.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Shock0.status == STARTED and t >= frameRemains:
            Shock0.setAutoDraw(False)

        # *Shock1* updates
        if t >= 0.0 and Shock1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Shock1.tStart = t
            Shock1.frameNStart = frameN  # exact frame index
            Shock1.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Shock1.status == STARTED and t >= frameRemains:
            Shock1.setAutoDraw(False)

        # *Shock2* updates
        if t >= 0.0 and Shock2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Shock2.tStart = t
            Shock2.frameNStart = frameN  # exact frame index
            Shock2.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Shock2.status == STARTED and t >= frameRemains:
            Shock2.setAutoDraw(False)
        if 'num_0' == RetaliationKey.keys:  # if down key pushed,
            Shock0.opacity = 1.0  # make shock0 appear
            Shock1.opacity = 0  # make shock1 invisible
            Shock2.opacity = 0  # make shock2 invisible
        elif 'num_1' == RetaliationKey.keys:  # if left key is pushed
            Shock1.opacity = 1.0  # make shock1 appear
            Shock0.opacity = 0  # make shock0 invisible
            Shock2.opacity = 0  # make shock2 invisible
        elif 'num_2' == RetaliationKey.keys:  # if right key is pushed
            Shock2.opacity = 1.0  # make shock2 appear
            Shock0.opacity = 0  # make shock0 invisible
            Shock1.opacity = 0  # make shock1 invisible

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # check responses
    if RetaliationKey.keys in ['', [], None]:  # No response was made
        RetaliationKey.keys = None
    RetaliationLoop.addData('RetaliationKey.keys', RetaliationKey.keys)
    if RetaliationKey.keys != None:  # we had a response
        RetaliationLoop.addData('RetaliationKey.rt', RetaliationKey.rt)

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
    frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
