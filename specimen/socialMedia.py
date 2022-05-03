letters = "abcdefghijklmnopqrstuvwxyz".upper()
s = 100
amount = len(letters)

path = '/Users/frederik/Dropbox/lectures/Amiens/Amiens20220502/fontInTwoDays/localFiles/NewestFont-TheRegular.otf'

for i, letter in enumerate(letters):
    factor1 = i / amount
    
    newPage(s*2.5, s*2.5)
    font(path)

    with savedState():
        fill(1)
        rect(0, 0, width(), height())
          
    with savedState():
        fontSize(s)
        text(letter, (width() / 2, height() / 2 - fontXHeight()/2), align="center")

    for c in range(amount):
        factor2 = c / amount 
        letter = letters[c]
    
        with savedState():
            translate(width() / 2, height() / 2)                
            rotate(360 * factor2 + 360 * factor1) 
            translate(s, 0)
            rotate(-90)
            text(letter, (0, 0))
 
saveImage("socialMedia.gif")