import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("home")
pyautogui.press("search")
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")
time.sleep(10)
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
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write("codigo")
    pyautogui.press("tab")
    pyautogui.write("marca")
    pyautogui.press("tab")
    pyautogui.write("tipo")
    pyautogui.press("tab")
    pyautogui.write("categoria")
    pyautogui.press("tab")
    pyautogui.write("preco")
    pyautogui.press("tab")
    pyautogui.write("custo")
    pyautogui.press("tab")
    pyautogui.write("obs")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
