#!/usr/bin/env python
# encoding: utf-8
"""
MonOhmod_Map.py

Created by amounra on 2010-10-05.
Copyright (c) 2010 __artisia__. All rights reserved.

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
There will eventually be a way to reassign the functions accessed by the different shift modes from this file as well....
Hold tight ;)
"""
CHANNEL = 0		#main channel (0 - 15)

OHM_BUTTONS = [65, 73, 66, 74, 67, 75, 68, 76]    #there are 8 of these

OHM_FADERS = [23, 22, 15, 14, 5, 7, 6, 4]		#there are 8 of these

OHM_ROTARIES_TOP = [17, 16, 9, 8, 19, 18, 11, 10]	#these aren't currently used

OHM_ROTARIES_BOTTOM = [21, 20, 13, 12, 3, 1, 0, 2]		#these aren't currently used

OHM_DIALS = [17, 16, 9, 8, 19, 18, 11, 10, 21, 20, 13, 12, 3, 1, 0, 2]		#there are 16 of these

OHM_MENU = [69, 70, 71, 77, 78, 79]			#there are 6 of these

CROSSFADER = 24		#single

SHIFT_L = 64		#single

SHIFT_R = 72		#single

LIVID = 87			#single

RIGHT_USER1_CHANNEL = 9			#this is the channel for the first (partial right) grid in Right Function Mode 2

RIGHT_USER1_MAP = 	[[0, 1, 2, 3, 16],			#these are the note numbers for the first (partial) grid in Right Function Mode 2
 					[4, 5, 6, 7, 17],
					[8, 9, 10, 11, 18],
					[12, 13, 14, 15, 19]]
					
RIGHT_USER2_CHANNEL = 2			#this is the channel for the second (full right) grid in Right Function Modes 3 & 4

RIGHT_USER2_MAP = 	[[0, 1, 2, 3, 4, 5, 6, 7],		#these are the note numbers for the first (partial) grid in Right Function Mode 3 & 4
					[8, 9, 10, 11, 12, 13, 14, 15],
					[16, 17, 18, 19, 20, 21, 22, 23],
					[24, 25, 26, 27, 28, 29, 30, 31]]
					
RIGHT_USER3_CHANNEL = 3			#this is the channel for the second (full right) grid in Right Function Modes 3 & 4

RIGHT_USER3_MAP = 	[[0, 1, 2, 3, 4, 5, 6, 7],		#these are the note numbers for the first (partial) grid in Right Function Mode 3 & 4
					[8, 9, 10, 11, 12, 13, 14, 15],
					[16, 17, 18, 19, 20, 21, 22, 23],
					[24, 25, 26, 27, 28, 29, 30, 31]]

L_USER_DIAL_CHAN = 1			#this is the channel for the knobs in Left Function Mode 4

L_USER_DIAL_MAP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]		#these are the identifiers for the knobs in Left Function Mode 4

R_USER1_DIAL_CHAN = 2			#this is the channel for the knobs in Right Function Mode 3

R_USER1_DIAL_MAP = [0, 1, 2, 3]	#these are the identifiers for the knobs in Right Function Mode 3

R_USER2_DIAL_CHAN = 3				#this is the channel for the knobs in Right Function Mode 4

R_USER2_DIAL_MAP = [0, 1, 2, 3]		#these are the identifiers for the knobs in Right Function Mode 4

R_USER2_FADER_CHAN = 4				#this is the channel for the faders in Right Function Mode 4

R_USER2_FADER_MAP = [0, 1, 2, 3]	#these are the identifiers for the faders in Right Function Mode 4

BACKLIGHT_TYPE = ['static', 'pulse', 'up', 'down']  #this assigns the backlight mode for left_shift_modes 1-4.  If 'static', the value below will be used

BACKLIGHT_VALUE = [127, 96, 64, 32]		#this assigns the led intensity for the backlight if it is in 'static' mode for left_shift_modes 1-4

OHM_TYPE = ['static', 'pulse', 'up', 'down']	#this assigns the ohm logo mode for right_shift_modes 1-4.  If 'static', the value below will be used

OHM_VALUE = [127, 96, 64, 32]	#this assigns the led intensity for the ohm logo if it is in 'static' mode for right_shift_modes 1-4

PAD_TRANSLATION = 	((0, 0, 0, 9), (0, 1, 1, 9), (0, 2, 2, 9), (0, 3, 3, 9),		#this is used by DrumRacks to translate input to one of the visible grid squares for triggering
					(1, 0, 4, 9), (1, 1, 5, 9), (1, 2, 6, 9), (1, 3, 7, 9),			#the format is (x position, y position, note-number, channel)
					(2, 0, 8, 9), (2, 1, 9, 9), (2, 2, 10, 9), (2, 3, 11, 9),
					(3, 0, 12, 9), (3, 1, 13, 9), (3, 2, 14, 9), (3, 3, 15, 9))
					
OHM_MAP_ID = [[0, 1, 2, 3, 4, 5, 6, 7],		#these are the notenumbers for the grid when in Livid_Mode
			[8, 9, 10, 11, 12, 13, 14, 15],
			[16, 17, 18 , 19, 20, 21, 22, 23],
			[24, 25, 26, 27, 28, 29, 30, 31],
			[32, 33, 34, 35, 36, 37, 38, 39],
			[40, 41, 42, 43, 44, 45, 46, 47],
			[48, 49, 50, 51, 52, 53, 54, 55],
			[56, 57, 58, 59, 60, 61, 62, 63]]
			
OHM_MAP_CHANNEL = [[15, 15, 15, 15, 15, 15, 15, 15],		#these are the channels for each grid square in Livid_Mode
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15]]
				
OHM_MAP_VALUE = [[4, 8, 5, 2, 0, 3, 0, 6], 			#these are the values that are lit up in Livid_Mode
				[8, 4, 2, 0, 2, 0, 3, 0],
				[5, 2, 0, 3, 0, 2, 0, 3], 
				[2, 0, 3, 0, 1, 0, 2, 0],
				[0, 2, 0, 1, 0, 3, 0, 2], 
				[3, 0, 2, 0, 3, 0, 2, 5],
				[0, 3, 0, 2, 0, 2, 4, 8], 
				[6, 0, 3, 0, 2, 5, 8, 4]]

FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track

MUTE = [1, 127]
SOLO = [10, 127]
ARM = [6, 8]
SEND_RESET = [8, 8]
SCENE_LAUNCH = [4, 17]
USER1_COLOR = [5, 127]
USER2_COLOR = [6, 127]
USER3_COLOR = [127, 127]
CROSSFADE_TOGGLE = [2, 127]
TRACK_STOP = [127, 127]
DEVICE_SELECT = [127, 7]
BANK_BUTTONS = [3, 1]
STOP_ALL = [127, 15]
SESSION_NAV = [4, 32]
OVERDUB = [1, 127]
LOOP = [3, 127]
STOP = [127, 127]
RECORD = [6, 15]
PLAY = [5, 127]
PLAY_ON = [12, 127]
DEVICE_BANK = [127, 127]
DEVICE_NAV = [3, 127]
DEVICE_ON = [127, 127]
DEVICE_LOCK = [2, 127]
CLIP_RECORDING = [6, 7]	
CLIP_STARTED = [5, 32]
CLIP_STOP = [127, 127]
CLIP_TRG_REC = [4, 7]
CLIP_TRG_PLAY = [3, 14]
ZOOM_STOPPED = [6, 127]
ZOOM_PLAYING = [5, 14]
ZOOM_SELECTED = [127, 7]
STOP_CLIP = [6, 2]

DEVICE_NAV_NAMES = ['bank ^', 'enable', 'lock', 'bank v', '< device', 'device >']
TRANSPORT_NAMES = [' ', ' ', ' ', ' ', ' ', ' ']
SESSION_NAV_NAMES = [' ^', 'PLAY', 'STOP', ' v', ' <', ' >']
MONOMOD_SHIFT_NAMES = ['bank ^', 'PLAY', 'STOP', 'bank v', '< device', 'device >']
MONOMOD_NAMES = [' ^', 'S-LOCK', 'ALT', ' v', ' <', ' >']
SESSION_BANK_NAMES = ['left ^', 'PLAY', 'STOP', 'mix  v', ' < ', ' >']
SESSION_BANK2_NAMES = ['right ^', 'PLAY', 'STOP', 'mix   v', ' < ', ' >']
SESSION_MAIN_BANK_NAMES = ['main ^', 'PLAY', 'STOP', 'mix  v', ' < ', ' >']
GRID_NAMES = [[[' x', ' x', ' x', ' x', ' x', ' x', ' x', ' x'],
				[' +', ' +', ' +', ' +', ' +', ' +', ' +', ' +'],
				[' *', ' *', ' *', ' *', ' *', ' *', ' *', ' *']],
				[['rec', 'ovr', 'loop', 'stop', 's1', 's2', 's3', 's4'],
				['assign', 'assign', 'assign', 'assign', 'assign', 'assign', 'assign', 'assign'],
				['stop', 'stop', 'stop', 'stop', 'stop', 'stop', 'stop', 'stop']],
				[['s1', 's2', 's3', 's4', 'rec', 'ovr', 'loop', 'stop'],
				['assign', 'assign', 'assign', 'assign', 'assign', 'assign', 'assign', 'assign'],
				['stop', 'stop', 'stop', 'stop', 'stop', 'stop', 'stop', 'stop']],
				[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]]

DISPLAY_BUTTON_NAMES = True
## a



