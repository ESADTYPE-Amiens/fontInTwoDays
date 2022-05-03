pageSize = "A4"
border = 10

import os

import drawBot

root = "binaryFiles"


drawBot.newDrawing()

for fileName in os.listdir(root):
    if not fileName.endswith(".otf"):
        continue
    fontPath = os.path.join(root, fileName)
    
    drawBot.newPage(pageSize)
    
    txt = drawBot.FormattedString()
    txt.fontSize(100)
    fontName = txt.font(fontPath)
     
    
    txt.appendGlyph(*txt.listFontGlyphNames())
    
    drawBot.font("Helvetica")
    drawBot.text(fontName, (border, border))
    
    drawBot.textBox(txt, (border, border, drawBot.width() - border * 2, drawBot.height() - border * 2))
    
drawBot.saveImage("specimen.pdf")    
drawBot.endDrawing()