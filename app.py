import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("home")
pyautogui.press("search")
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")
time.sleep(8)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click()
