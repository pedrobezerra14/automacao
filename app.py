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
    pyautogui.click(x=501, y=280)
    time.sleep(0.5)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.scroll(5000)
