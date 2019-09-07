
import random,time, pygame, sys
from pygame.locals import *

FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (100, 100, 100)
LIGHTGRAY   = (185, 185, 185)
DARKGRAY    = ( 50,  50,  50)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR = BLUE
BORDERCOLOR2 = DARKGRAY
BGCOLOR =  GRAY
TEXTCOLOR = WHITE
TEXTCOLOR2 = BLACK
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
COLORS2      = (   BLACK,      GRAY)
LIGHTCOLORS2 = (DARKGRAY, LIGHTGRAY)
BG = pygame.image.load('background.jpeg')
BG2 = pygame.image.load('retrobg.jpg')
GAMEBOY = pygame.image.load('gameboy.png')
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color
assert len(COLORS2) == len(LIGHTCOLORS2) # each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

RING_TEMPLATE_SHAPE = [['..OO.',
                        '.O..O',
                        '.O..O',
                        '..OO.',
                        '.....',
                        ]]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}



def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT, CLASSICTHEMEBUTTON, MODERNTHEMEBUTTON, CONTROLMENUBUTTON, themefont, themefont2, themeinscription, themeinstruction1, themeinstruction2,controlinstruction
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('pixelate.ttf', 18)
    BIGFONT = pygame.font.Font('pixelate.ttf', 90)
    themefont = pygame.font.Font("MANICMINER.ttf", 18)
    themefont2 = pygame.font.Font("pixelate.ttf", 15)
    themeinscription = themefont.render('Choose your preferred theme.', 1, WHITE)
    themeinstruction1 = themefont.render('MOD THEME', 1, WHITE)
    themeinstruction2 = themefont.render('RETRO THEME', 1, BLACK)
    controlinstruction = themefont2.render('CONTROLS', 1, WHITE)
    pygame.display.set_caption('My Tetris')

    end_it = False
    while (end_it == False):
        tetrisLogo = pygame.image.load('tetris3.png')
        mainBG = pygame.image.load('mainBG.jpg')
        DISPLAYSURF.fill(BLUE)
        myfont = pygame.font.Font("MANICMINER.ttf", 25)
        myfont2 = pygame.font.Font("MANICMINER.ttf", 15)
        nlabel = myfont.render("MY TETRIS", 1, WHITE)
        instruction = myfont2.render("CLICK TO START GAME", 1, WHITE)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                end_it = True
            if event.type == QUIT:
                terminate()
        DISPLAYSURF.blit(mainBG, (0, 0))
        DISPLAYSURF.blit(tetrisLogo, (250, 100))
        DISPLAYSURF.blit(nlabel, (230, 150))
        DISPLAYSURF.blit(instruction, (200, 330))
        pygame.display.update()


    while True: # game loop
        mainBG = pygame.image.load('mainBG.jpg')
        DISPLAYSURF.blit(mainBG, (0, 0))
        DISPLAYSURF.blit(themeinscription, (150, 250))
        CLASSICTHEMEBUTTON = pygame.draw.rect(DISPLAYSURF, BLACK, (60, 105, 200, 100))
        MODERNTHEMEBUTTON = pygame.draw.rect(DISPLAYSURF, BLACK, (400, 105, 200, 100))
        MODERNTHEMEBUTTON = pygame.draw.rect(DISPLAYSURF, BLUE, (50, 100, 200, 100))
        CLASSICTHEMEBUTTON = pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (390, 100, 200, 100))
        CONTROLMENUBUTTON = pygame.draw.rect(DISPLAYSURF, BLACK, (510, 55, 100, 25))
        CONTROLMENUBUTTON = pygame.draw.rect(DISPLAYSURF, GRAY, (500, 50, 100, 25))
        DISPLAYSURF.blit(themeinstruction1, (70, 150))
        DISPLAYSURF.blit(themeinstruction2, (400, 150))
        DISPLAYSURF.blit(controlinstruction, (505, 55))
        for event in pygame.event.get():
            print(event)
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 50 and pygame.mouse.get_pos()[1] >= 100:
                    if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 200:
                        pygame.mixer.music.load('Off Limits.wav')
                        pygame.mixer.music.play(-1, 0.0)
                        runGame()
                        pygame.mixer.music.stop()
                        showTextScreen('Game Over')
                if pygame.mouse.get_pos()[0] >= 390 and pygame.mouse.get_pos()[1] >= 100:
                    if pygame.mouse.get_pos()[0] <= 590 and pygame.mouse.get_pos()[1] <= 200:
                        pygame.mixer.music.load('Off Limits.wav')
                        pygame.mixer.music.play(-1, 0.0)
                        runGame2()
                        pygame.mixer.music.stop()
                        showTextScreen2('Game Over')
                if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 25:
                    if pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] <= 125:
                        DISPLAYSURF.blit(mainBG, (0, 0))
                        pause = themefont2.render('P: PAUSE', 1, WHITE)
                        mutemusic = themefont2.render('M: MUTE MUSIC', 1, WHITE)
                        playmusic = themefont2.render('C: PLAY MUSIC', 1, WHITE)
                        rotate = themefont2.render('Q & W: ROTATE PIECE', 1, WHITE)
                        movedown = themefont2.render('S & DOWNBUTTON: MOVE DOWN', 1, WHITE)
                        moveleft = themefont2.render('A & LEFTBUTTON: MOVE LEFT', 1, WHITE)
                        moveright = themefont2.render('D & RIGHTBUTTON: MOVE RIGHT', 1, WHITE)
                        movepieceatwdown = themefont2.render('SPACE: MOVE PIECE STRAIGHT TO THE BOTTOM', 1, WHITE)
                        exitinst = themefont2.render('PRESS ANY KEY TO RETURN TO MENU', 1, WHITE)
                        DISPLAYSURF.blit(pause, (100, 50))
                        DISPLAYSURF.blit(mutemusic, (100, 70))
                        DISPLAYSURF.blit(playmusic, (100, 90))
                        DISPLAYSURF.blit(rotate, (100, 110))
                        DISPLAYSURF.blit(movedown, (100, 130))
                        DISPLAYSURF.blit(moveleft, (100, 150))
                        DISPLAYSURF.blit(moveright, (100, 170))
                        DISPLAYSURF.blit(movepieceatwdown, (100, 190))
                        DISPLAYSURF.blit(exitinst, (100, 250))

                        while checkForKeyPress() == None:
                            pygame.display.update()
                            FPSCLOCK.tick()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()


def runGame():
    # setup variables for the start of the game
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False # note: there is no movingUp variable
    movingLeft = False
    movingRight = False
    score = removeCompleteLines(board)
    level, fallFreq = calculateLevelAndFallFreq(score)
    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True: # game loop

        if fallingPiece == None:
            # No falling piece in play, so start a new piece at the top
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time() # reset lastFallTime

            if not isValidPosition(board, fallingPiece):
                return # can't fit a new piece on the board, so game over
        checkForQuit()

        for event in pygame.event.get():# event handling loop
            if event.type == KEYUP:
                if (event.key == K_m):
                    pygame.mixer.music.stop()
                elif (event.key == K_c):
                    pygame.mixer.music.play(-1, 0.0)
                elif (event.key == K_p):
                    # Pausing the game
                    #DISPLAYSURF.fill(BGCOLOR)
                    DISPLAYSURF.blit(BG, (0, 0))
                    pygame.mixer.music.stop()
                    showTextScreen('Paused') # pause until a key press
                    pygame.mixer.music.play(-1, 0.0)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                # moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                # rotating the piece (if there is room to rotate)
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == K_q): # rotate the other direction
                    fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])

                # making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()

                # move the current piece all the way down
                elif event.key == K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += i - 1

        # handle moving the piece because of user input
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        # let the piece fall if it is time to fall
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has landed
            if not isValidPosition(board, fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                # piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()


        # drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(BG, (0, 0))
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def runGame2():
    # setup variables for the start of the game
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False # note: there is no movingUp variable
    movingLeft = False
    movingRight = False
    score = removeCompleteLines(board)
    level, fallFreq = calculateLevelAndFallFreq(score)
    fallingPiece2 = getNewPiece2()
    nextPiece2 = getNewPiece2()

    while True: # game loop
        if fallingPiece2 == None:
            # No falling piece in play, so start a new piece at the top
            fallingPiece2 = nextPiece2
            nextPiece2 = getNewPiece2()
            lastFallTime = time.time() # reset lastFallTime

            if not isValidPosition(board, fallingPiece2):
                return # can't fit a new piece on the board, so game over

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == KEYUP:
                if (event.key == K_m):
                    pygame.mixer.music.stop()
                elif (event.key == K_c):
                    pygame.mixer.music.play(-1, 0.0)
                elif (event.key == K_p):
                    # Pausing the game
                    #DISPLAYSURF.fill(BGCOLOR)
                    DISPLAYSURF.blit(BG2, (0, 0))
                    pygame.mixer.music.stop()
                    showTextScreen('Paused') # pause until a key press
                    pygame.mixer.music.play(-1, 0.0)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                # moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece2, adjX=-1):
                    fallingPiece2['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece2, adjX=1):
                    fallingPiece2['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                # rotating the piece (if there is room to rotate)
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece2['rotation'] = (fallingPiece2['rotation'] + 1) % len(PIECES[fallingPiece2['shape']])
                    if not isValidPosition(board, fallingPiece2):
                        fallingPiece2['rotation'] = (fallingPiece2['rotation'] - 1) % len(PIECES[fallingPiece2['shape']])
                elif (event.key == K_q): # rotate the other direction
                    fallingPiece2['rotation'] = (fallingPiece2['rotation'] - 1) % len(PIECES[fallingPiece2['shape']])
                    if not isValidPosition(board, fallingPiece2):
                        fallingPiece2['rotation'] = (fallingPiece2['rotation'] + 1) % len(PIECES[fallingPiece2['shape']])

                # making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, fallingPiece2, adjY=1):
                        fallingPiece2['y'] += 1
                    lastMoveDownTime = time.time()

                # move the current piece all the way down
                elif event.key == K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece2, adjY=i):
                            break
                    fallingPiece2['y'] += i - 1

        # handle moving the piece because of user input
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board, fallingPiece2, adjX=-1):
                fallingPiece2['x'] -= 1
            elif movingRight and isValidPosition(board, fallingPiece2, adjX=1):
                fallingPiece2['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece2, adjY=1):
            fallingPiece2['y'] += 1
            lastMoveDownTime = time.time()

        # let the piece fall if it is time to fall
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has landed
            if not isValidPosition(board, fallingPiece2, adjY=1):
                # falling piece has landed, set it on the board
                addToBoard(board, fallingPiece2)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece2 = None
            else:
                # piece did not land, just move the piece down
                fallingPiece2['y'] += 1
                lastFallTime = time.time()

        # drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(BG2, (0, 0))
        DISPLAYSURF.blit(GAMEBOY, (50, 250))
        DISPLAYSURF.blit(GAMEBOY, (450, 250))
        drawBoard2(board)
        drawStatus2(score, level)
        drawNextPiece2(nextPiece2)
        if fallingPiece2 != None:
            drawPiece2(fallingPiece2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def terminate():
    pygame.quit()
    sys.exit()


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def showTextScreen(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

def showTextScreen2(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR2)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def calculateLevelAndFallFreq(score):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq


def getNewPiece():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece


def getNewPiece2():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(PIECES.keys()))
    newPiece2 = {'shape': shape,
                 'rotation': random.randint(0, len(PIECES[shape]) - 1),
                 'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                 'y': -2, # start it above the board (i.e. less than 0)
                 'color': random.randint(0, len(COLORS2)-1)}
    return newPiece2


def addToBoard(board, piece):
    # fill in the board based on piece's location, shape, and rotation
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']


def getBlankBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board


def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def isValidPosition(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True


def isCompleteLine(board, y):
    # Return True if the line filled with boxes with no gaps.
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True


def removeCompleteLines(board):
    # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1 # start y at the bottom of the board
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up
    return numLinesRemoved


def convertToPixelCoords(boxx, boxy):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    # draw a single box (each tetromino piece has four boxes)
    # at xy coordinates on the board. Or, if pixelx & pixely
    # are specified, draw to the pixel coordinates stored in
    # pixelx & pixely (this is used for the "Next" piece).
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
    pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))


def drawBox2(boxx, boxy, color, pixelx=None, pixely=None):
    # draw a single box (each tetromino piece has four boxes)
    # at xy coordinates on the board. Or, if pixelx & pixely
    # are specified, draw to the pixel coordinates stored in
    # pixelx & pixely (this is used for the "Next" piece).
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, COLORS2[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
    pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS2[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))


def drawBoard(board):
    # draw the border around the board
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
    # fill the background of the board
    # draw the individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])

def drawBoard2(board):
    # draw the border around the board
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR2, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
    # fill the background of the board
    # draw the individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox2(x, y, board[x][y])


def drawStatus(score, level):
    # draw the score text
    scoreSurf = BASICFONT.render('Score: ' + str(score), True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    # draw the level text
    levelSurf = BASICFONT.render('Level: ' + str(level), True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)


def drawStatus2(score, level):
    # draw the score text
    scoreSurf = BASICFONT.render('Score: ' + str(score), True, TEXTCOLOR2)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    # draw the level text
    levelSurf = BASICFONT.render('Level: ' + str(level), True, TEXTCOLOR2)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)


def drawPiece(piece, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))

def drawPiece2(piece2, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece2['shape']][piece2['rotation']]
    if pixelx == None and pixely == None:
        # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece2['x'], piece2['y'])

    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox2(None, None, piece2['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))

def drawNextPiece(piece):
    # draw the "next" text
    nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    # draw the "next" piece
    drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)

def drawNextPiece2(piece2):
    # draw the "next" text
    nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR2)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    # draw the "next" piece
    drawPiece2(piece2, pixelx=WINDOWWIDTH-120, pixely=100)

if __name__ == '__main__':
    main()
