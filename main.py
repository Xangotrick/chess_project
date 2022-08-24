import math
import time

import pygame
import os
from gamestate import *




class PGPiece:
    def __init__(self,apiece):
        self.piece = apiece
        pos = getpgposfromboard(self.piece.x,self.piece.y)
        self.img = pygame.transform.smoothscale(PIECEDICT[self.piece.type+str(self.piece.color)],(SQUARE_SIZE,SQUARE_SIZE))
        self.rect = rectfromcenter(pos[0],pos[1],SQUARE_SIZE,SQUARE_SIZE)
        self.requiredpos = (self.rect.x,self.rect.y)
        self.rect = rectfromcenter(WWW/2, HHH/2, SQUARE_SIZE, SQUARE_SIZE)

    def updatepos(self):
        deltapos = SQUARE_SIZE * 5  / REFRESH_RATE #to move at SQUARE_SIZE (px/s) per second multiply by the refresh rate that is a (1/s) unit to get the delta to move (px)
        clippingmargin = deltapos * 1.5

        deltax =  self.requiredpos[0] - self.rect.x
        deltay =  self.requiredpos[1] - self.rect.y
        if deltax != 0 or deltay != 0:
            if math.fabs(deltax) < clippingmargin:
                self.rect.x = self.requiredpos[0]
            else:
                self.rect.x += math.copysign(1,deltax) * deltapos
            if math.fabs(deltay) < clippingmargin:
                self.rect.y = self.requiredpos[1]
            else:
                self.rect.y += math.copysign(1,deltay) * deltapos


class PGManager:
    def __init__(self,gamestate):
        self.mousehoversquare = (-1,-1)
        self.piecelist = []
        for piece in gamestate.board.pieces:
            self.piecelist.append(PGPiece(piece))





def rectfromcenter(posx,posy,width,height):
    return pygame.Rect(posx- (width / 2), posy - (height/2),width,height)

def draw_background():
    SCREEN.fill((50,50,50))

def draw_board():
    mousepos = pygame.mouse.get_pos()
    for row in range(8):
        for col in range(8):
            pos = getpgposfromboard(col,row)
            rect = rectfromcenter(pos[0], pos[1], SQUARE_SIZE, SQUARE_SIZE)
            isdark = ((row + col) % 2 == 0)

            if pos[0] - SQUARE_SIZE / 2 < mousepos[0] < pos[0] + SQUARE_SIZE / 2 and pos[1] - SQUARE_SIZE / 2 < mousepos[1] < pos[1] + SQUARE_SIZE/2:
                PGMANAGER.mousehoversquare = (col,row)
                if isdark:
                    pygame.draw.rect(SCREEN, rect=rect, color=(151, 128, 215))
                else:
                    pygame.draw.rect(SCREEN, rect=rect, color=(191, 215, 128))
            else:
                if isdark:
                    pygame.draw.rect(SCREEN, rect=rect, color=(191, 168, 255))
                else:
                    pygame.draw.rect(SCREEN, rect=rect, color=(231, 255, 168))

def draw_pieces():
    for pgpiece in PGMANAGER.piecelist:
        pgpiece.updatepos()
        SCREEN.blit(pgpiece.img,(pgpiece.rect.x,pgpiece.rect.y))

def getpgposfromboard(x,y):
    initpos = (int(WWW/2 - (SQUARE_SIZE * 3.5)) ,int(HHH / 2 - (SQUARE_SIZE * 3.5)))

    retx = initpos[0] + SQUARE_SIZE * x
    rety = initpos[1] + (SQUARE_SIZE * (7 - y))

    returner = (retx,rety)
    return returner


def timer(lastupdate):
    aimdelta = 1 / REFRESH_RATE
    time.sleep(1 / REFRESH_RATE)
    delta = time.time() - lastupdate
    reldelta = math.fabs(aimdelta - delta)/aimdelta
    if reldelta > 0.2:
        pass
        #print("LAG!")

def game_input():
    mousepress = pygame.mouse.get_pressed()
    if mousepress[0]:
        m_square=PGMANAGER.mousehoversquare
        if GAMESTATE.board.ispieceatpos(m_square[0],m_square[1]):
            print(m_square)

def main():
    running = True

    updatetimestamp = time.time()
    while running:
        timer(updatetimestamp)
        updatetimestamp = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_background()
        draw_board()
        draw_pieces()

        game_input()

        pygame.display.update()





REFRESH_RATE = 60
DIR_ASSETS = os.getcwd()+'\\assets\\'
WWW = 800
HHH = int(WWW * 9 / 16)
SCREEN_SIZE = (WWW,HHH)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
MARGIN = 50
SQUARE_SIZE = int((HHH - MARGIN) / 8)

PIECEDICT = {
    'P0':pygame.image.load(DIR_ASSETS+'P0.svg'),
    'K0':pygame.image.load(DIR_ASSETS+'K0.svg'),
    'Q0':pygame.image.load(DIR_ASSETS+'Q0.svg'),
    'B0':pygame.image.load(DIR_ASSETS+'B0.svg'),
    'N0':pygame.image.load(DIR_ASSETS+'N0.svg'),
    'R0':pygame.image.load(DIR_ASSETS+'R0.svg'),

    'P1':pygame.image.load(DIR_ASSETS+'P1.svg'),
    'K1':pygame.image.load(DIR_ASSETS+'K1.svg'),
    'Q1':pygame.image.load(DIR_ASSETS+'Q1.svg'),
    'B1':pygame.image.load(DIR_ASSETS+'B1.svg'),
    'N1':pygame.image.load(DIR_ASSETS+'N1.svg'),
    'R1':pygame.image.load(DIR_ASSETS+'R1.svg')
}


GAMESTATE = Gamestate()
PGMANAGER = PGManager(GAMESTATE)

if __name__ == '__main__':
    main()
