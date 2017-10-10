#!/usr/bin/python
import os

# PIPE
PIPE_STYLE_DEFAULT = 'line'
PIPE_STYLE_DASHED = 'dashed'
PIPE_STYLE_DOTTED = 'dotted'
PIPE_DEFAULT_COLOR = (127, 149, 151, 255)
PIPE_ACTIVE_COLOR = (172, 151, 94, 255)
PIPE_HIGHLIGHT_COLOR = (232, 184, 13, 255)
PIPE_LAYOUT_STRAIGHT = 0
PIPE_LAYOUT_CURVED = 1

# PORT
IN_PORT = 'in'
OUT_PORT = 'out'
PORT_ACTIVE_COLOR = (29, 80, 84, 255)
PORT_ACTIVE_BORDER_COLOR = (45, 215, 255, 255)

# NODE
NODE_ICON_SIZE = 24
NODE_SEL_COLOR = None  # (77, 64, 18, 255)
NODE_SEL_BORDER_COLOR = (173, 115, 5, 255)

# NODE GRAPH VIEWER
VIEWER_BG_COLOR = (35, 35, 35, 255)
VIEWER_GRID_OVERLAY = True

# SAVE FILE FORMAT
FILE_FORMAT = '.bpg'

# GRAPH PATHS
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
ICON_PATH = os.path.join(BASE_PATH, 'src', 'icons')
ICON_DOWN_ARROW_ICON = os.path.join(ICON_PATH, 'down_arrow.png')
ICON_NODE_BASE = os.path.join(ICON_PATH, 'node_base.png')

# DRAW STACK ORDER
Z_VAL_PIPE = -1
Z_VAL_NODE = 1
Z_VAL_PORT = 2
Z_VAL_KNOB = 3

