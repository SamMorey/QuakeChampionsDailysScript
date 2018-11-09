import webbrowser
import pyautogui
import time
import os
import ctypes

quakeAppID = 611500

def playGame(game):
	webbrowser.open('steam://rungameid/{}'.format(game))
	
def skipMenus():
	pyautogui.moveTo(500,500)
	pyautogui.click()
	for x in range(0, 10):
		pyautogui.press('esc')
		time.sleep(1)
	
def claimRewards():
	pyautogui.moveTo(1145,981)
	time.sleep(1)
	pyautogui.doubleClick()
	time.sleep(5)
	pyautogui.moveTo(1289, 927)
	time.sleep(1)
	pyautogui.doubleClick()

	
playGame(quakeAppID)
time.sleep(10)
skipMenus()
time.sleep(40)
claimRewards()
time.sleep(10)
os.system("taskkill /f /im QuakeChampions.exe")


