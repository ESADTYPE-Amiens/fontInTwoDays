 letters = "abcdefghijklmnopqrstuvwxyz".upper()
s = 100
amount = len(letters)

import os

import drawBot

root = "binaryFiles"


drawBot.newDrawing()

for fileName in os.listdir(root):
    if not fileName.endswith(".otf")
        continue

    drawBot.fontPath = os.path.join(root, fileName)


for i, letter in enumerate(letters):
    factor1 = i / amount
    
    drawBot.newPage(s*2.5, s*2.5)
    drawBot.font(path)

    with drawBot.savedState():
        drawBot.fill(1)
        drawBot.rect(0, 0, drawBot.width(), drawBot.height())
          
    with drawBot.savedState():
        drawBot.fontSize(s)
        drawBot.text(letter, (drawBot.width() / 2, drawBot.height() / 2 - drawBot.fontXHeight()/2), align="center")

    for c in drawBot.range(amount):
        factor2 = c / amount 
        letter = letters[c]
    
        with drawBot.savedState():
            drawBot.translate(drawBot.width() / 2, drawBot.height() / 2)                
            drawBot.rotate(360 * factor2 + 360 * factor1) 
            drawBot.translate(s, 0)
            drawBot.rotate(-90)
            drawBot.text(letter, (0, 0))
 
drawBot.saveImage("socialMedia.gif")
drawBot.endDrawing()