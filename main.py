import time
import random
import pyautogui
import pyscreenshot as imagegrab
from PIL import Image
import pytesseract
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\reach\AppData\Local\Tesseract-OCR\tesseract.exe'
rpsBot = False
stupidChar = ''

while True:
    time.sleep(2)
    grab = imagegrab.grab(bbox=(580, 832, 637, 860))
    grab.save('bot.png')
    image = Image.open('bot.png')
    txt = pytesseract.image_to_string(image).replace('.', '').replace(
        '\n', '').replace(stupidChar, '').replace('‘', '').replace('[', '/').lower()
    print(txt)

    if txt == '/bot':
        pyautogui.typewrite('Hello, this is u.seless.bot! You can type /Bot rps, to play Rock, paper'
                            ' scissors with me!')
        pyautogui.press('enter')

    if txt == '/bot rps':
        rpsBot = True

    if rpsBot:
        # Getting all the starter vars
        moveList = ['rock', 'paper', 'scissors']
        stat = 'error'
        playerPoints = 0
        enemyPoints = 0
        end = False

        # Reading Chat
        def get_input():
            im = imagegrab.grab(bbox=(580, 830, 650, 864))
            im.save('rps.png')
            img = Image.open('rps.png')
            text = pytesseract.image_to_string(img)
            return text

        # Writing to chat
        def say(phrase):
            if keyboard.is_pressed('q'):
                quit()
            pyautogui.typewrite(phrase)
            time.sleep(0.2)
            pyautogui.keyDown('enter')
            time.sleep(0.05)
            pyautogui.keyUp('enter')
            time.sleep(0.2)
            pyautogui.scroll(-1000)

        # Checking which move they used
        def check():
            global stat
            if move.lower() == enemyMove:
                stat = 'tie'
            elif move.lower() == 'scissors':
                if enemyMove == 'rock':
                    stat = 'loss'
                elif enemyMove == 'paper':
                    stat = 'win'
            elif move.lower() == 'paper':
                if enemyMove == 'rock':
                    stat = 'win'
                elif enemyMove == 'scissors':
                    stat = 'loss'
            elif move.lower() == 'rock':
                if enemyMove == 'paper':
                    stat = 'loss'
                elif enemyMove == 'scissors':
                    stat = 'win'

        # Intro
        say('Welcome to the rock paper scissors bot!')
        time.sleep(1)
        # Loop of bot
        while not end:
            # Chooses enemy move and gets user input
            enemyMove = random.choice(moveList)
            say('Do you choose rock, paper, or scissors? ')
            time.sleep(7)
            move = get_input().replace('.', '').replace('\n', '').replace(stupidChar, '')

            print(move)
            # Checks if move is allowed
            if move.lower() not in moveList:
                say('Error viewing text, please try again.')
                time.sleep(1)
                continue

            time.sleep(0.5)
            # Checks possibilities
            check()
            # Seeing if user won or not
            if stat == 'win':
                playerPoints += 1
            elif stat == 'loss':
                enemyPoints += 1

            # Saying the move and if you beat the bot
            say(enemyMove)
            time.sleep(0.5)
            say(stat)
            # If tells you if you won or not
            if playerPoints == 2:
                say('You win!')
                end = True
            elif enemyPoints == 2:
                say('You lose!')
                end = True
        rpsBot = False

    pyautogui.scroll(-500)
