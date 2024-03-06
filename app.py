import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("home")
pyautogui.press("search")
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=445, y=389)
time.sleep(0.5)
pyautogui.write("examplemail@gmail.com")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write("password123")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(1)
