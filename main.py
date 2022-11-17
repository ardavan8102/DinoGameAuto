from PIL import ImageGrab, ImageOps
from webbrowser import open_new_tab as new
from pyautogui import keyDown, keyUp
from time import sleep
from numpy import array

site_url = "https://trex-runner.com/" # Game Link


def pressSpaceButton(): # Press & Release Space Button
 
    keyDown('space')
 
    sleep(0.007)
 
    keyUp('space')
    
      
def openGamePage(): # Open Game URL In New Tab
    new(site_url)


def restartGame(): # Press Space Button To Start/Restart Game
    keyDown('space')
    print("Game Has Been Started / Restarted")


def FindCactuses(): # Find Cactuses In Screen
    box = ( #(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        2378,
        470,
        2429, 
        511   
    )      
    image = ImageGrab.grab(box, all_screens=True) # Get Coords As A Box
    grayImage = ImageOps.grayscale(image) # Convert Box To Black & White
    a = array(grayImage.getcolors()) # Make An Array With Color Number
    print(a.sum())  
    return a.sum() # Returns The Sum Of Color Numbers In Array

    
sleep(3) # Wait 3 Seconds
openGamePage()

sleep(5)# Wait 5 Seconds
restartGame()

  
while True: # infinite loop
    if FindCactuses() != 2338: # So If Sum Of Numbers Does Not Match With "white" Screen Sum, It is Black Probably So Need To Press Button
        pressSpaceButton()

        