import numpy as np
from PIL import Image, ImageColor
from numpy import random


HEIGHT = 640
WIDTH = 640
#235, 64, 52 red Start tile
tileStart = []
tileStart.append(235)
tileStart.append(64)
tileStart.append(52)

rS = tileStart[0]
gS = tileStart[1]
bS = tileStart[2]

#56, 47, 224 blue end

tileEnd = []
tileEnd.append(56)
tileEnd.append(47)
tileEnd.append(224)

rE = tileEnd[0]
gE = tileEnd[1]
bE = tileEnd[2]

#38, 181, 62 grass tile (walkable)

tileGrass = []
tileGrass.append(38)
tileGrass.append(181)
tileGrass.append(62)

rG = tileGrass[0]
gG = tileGrass[1]
bG = tileGrass[2]

# Rock tilego 109 65 31
tileRock = []
tileRock.append(109)
tileRock.append(65)
tileRock.append(31)

rR = tileRock[0]
gR = tileRock[1]
bR = tileRock[2]

r = 255
g = 255
b = 255
row = 0
column = 0

imgName = "TestTileMap.png"
img = Image.new('RGB', (HEIGHT,WIDTH)) # create the Image of size Height*Width pixel 
for i in range(WIDTH):
    column = i
    index = random.randint(100)
    print(index)
    if index <= 40:
        r = 255
        g = 255
        b = 255
    elif index > 40 and index <=80:
       r = tileRock[0]
       g = tileRock[1]
       b = tileRock[2]
    elif index >80 and index <=100:
        r = tileGrass[0]
        g = tileGrass[1]
        b = tileGrass[2]

    for j in range (HEIGHT):
        row = j
        index = random.randint(100)
        print (index)
        if index <= 40:
            r = 125
            g = 125
            b = 125
            noise = random.randint(100)
            if noise <= 20:
                r = tileGrass[0]
                g = tileGrass[1]
                b = tileGrass[2]
            elif noise > 20 and noise <=40:
                r = tileRock[0]
                g = tileRock[1]
                b = tileRock[2]
            elif noise >40 and noise <=100:
                r = rE
                g = gE
                b = bE
        elif index > 40 and index <=80:
            r = tileGrass[0]
            g = tileGrass[1]
            b = tileGrass[2]
            noise = random.randint(100)
            if noise <= 20:
                r = tileGrass[0]
                g = tileGrass[1]
                b = tileGrass[2]
            elif noise > 20 and noise <=40:
                r = tileRock[0]
                g = tileRock[1]
                b = tileRock[2]
            elif noise >40 and noise <=100:
                r = rE
                g = gE
                b = bE
        elif index > 80 and index <= 100:
            r = tileRock[0]
            g = tileRock[1]
            b = tileRock[2]
        img.putpixel((row,column),(r,g,b))
    row - 1
    img.putpixel((column,row),(r,g,b))
img.save(imgName) 
