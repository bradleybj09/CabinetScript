base = True #change to false for wall cabinets
width = 34 #width from outside to outside of walls
wallHeight = 36 #height of wall cabinets
baseHeight = 34.5 #do not change
plyWidth = .75
toeHeight = 4
toeDepth = 2
plateHeight = 4
widthInput = input('Enter width: ')
width = int(widthInput)
baseInput = input('[b]ase or [w]all: ')
base = True if baseInput == 'b' else False
if not base:
    heightInput = input('Enter height: ')
    wallHeight = int(heightInput)
innerWidth = width - (plyWidth * 2)
depth = 24 if base else 12
topDepth = plateHeight if base else depth
height = baseHeight if base else wallHeight
sideString = ''
if base:
    sideString = 'Sides: 2x: {} x {}; cut out 4h x 2w; {}x{}x{}x{}x{}x{}'.format(height, depth, height, depth, height - toeHeight, toeDepth, toeHeight, depth - toeDepth)
else:
    sideString = 'Sides: 2x: {} x {}'.format(height, depth)
baseString = 'Base: {} x {}'.format(innerWidth, depth)
toeKickString = 'Toe kick: {} x {}'.format(width, toeHeight)
basePlateString = 'Base plate: {} x {}'.format(innerWidth, toeHeight)
backPlateString = 'Back plates: 2x: {} x {}'.format(innerWidth, plateHeight)
topString = 'Top: {} x {}'.format(innerWidth, topDepth)
summaryString = 'For a {}" width {} cabinet:'.format(width, 'base' if base else 'wall')
lines = summaryString, sideString, baseString, topString, backPlateString
print(*lines, sep='\n')
xInput = input('enter x coordinate (int), leave blank for 0: ')
yInput = input('enter y coordinate (int), leave blank for 0: ')
x1 = 0 if xInput == '' else int(xInput)
y1 = 0 if yInput == '' else int(yInput)
y2 = y1 + height + 2
y3 = y2 + height + 2
y4 = y3 + width + 2
y5 = y4 + width + 2
x2 = x1 + toeHeight + 2
x3 = x2 + toeHeight + 2
x4 = x3 + plateHeight + 2
x5 = x1 + plateHeight + 2

commands = [
    ## write the first side
    'li',
    '{}, {}'.format(x1, y1),
    '@0, {}'.format(height),
    '@{}, 0'.format(depth),
    '@0, -{}'.format(height - toeHeight),
    '@-{}, 0'.format(toeDepth),
    '@0, -{}'.format(toeHeight),
    'c',
    'k',
    ## copy the second side
    'li',
    '{}, {}'.format(x1, y2),
    '@0, {}'.format(height),
    '@{}, 0'.format(depth),
    '@0, -{}'.format(height - toeHeight),
    '@-{}, 0'.format(toeDepth),
    '@0, -{}'.format(toeHeight),
    'c',
    'k',
    ## write the base
    'li',
    '{}, {}'.format(x1, y3),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(depth),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write the top
    'li',
    '{}, {}'.format(x1, y4),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(topDepth),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write toe kick
    'li',
    '{}, {}'.format(x1, y5),
    '@0, {}'.format(width),
    '@{}, 0'.format(toeHeight),
    '@0, -{}'.format(width),
    'c',
    'k',
    ## write back plate below base
    'li',
    '{}, {}'.format(x2, y5),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(toeHeight),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write back plate above base
    'li',
    '{}, {}'.format(x3, y5),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(plateHeight),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write back plate at top
    'li',
    '{}, {}'.format(x4, y5),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(plateHeight),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## last semicolon in import
    '\n'
] if base else [
    ## write the first side
    'li',
    '{}, {}'.format(x1, y1),
    '@0, {}'.format(height),
    '@{}, 0'.format(depth),
    '@0, -{}'.format(height),
    'c',
    'k',
    ## copy the second side
    'li',
    '{}, {}'.format(x1, y2),
    '@0, {}'.format(height),
    '@{}, 0'.format(depth),
    '@0, -{}'.format(height),
    'c',
    'k',
    ## write the base
    'li',
    '{}, {}'.format(x1, y3),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(depth),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write the top
    'li',
    '{}, {}'.format(x1, y4),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(topDepth),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write back plate above base
    'li',
    '{}, {}'.format(x1, y5),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(plateHeight),
    '@0, -{}'.format(innerWidth),
    'c',
    'k',
    ## write back plate at top
    'li',
    '{}, {}'.format(x5, y5),
    '@0, {}'.format(innerWidth),
    '@{}, 0'.format(plateHeight),
    '@0, -{}'.format(innerWidth),
    'c',
    'k;',
    ## last semicolon in import
]
print(*commands, sep=';')
input('Press any key to close')