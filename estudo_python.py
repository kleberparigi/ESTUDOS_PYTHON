## Importanto biblioteca pyautogui
import pyautogui
import time
### abrir o navegador (chrome) ou edge
pyautogui.press("win")
time.sleep(2)
#pyautogui.write("chrome")
pyautogui.write("edge")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
## precisará no meu caso clicar em nome do kleber 
# pyautogui.click(x=830, y=949)
#pyautogui.click 
# entrar no link 
pyautogui.write("https://app2.pontomais.com.br/login")
pyautogui.press("enter")
time.sleep(5)
#print (pyautogui.position())
#pyautogui.click(x=1331, y=131)
# verificar localização do mouse para clicar em login e senha;
#pyautogui.click (x=426, y=751)
#time.sleep(6)
#print (pyautogui.position())
#pyautogui.click(x=750, y=1046)
#time.sleep(1)
#pyautogui.write("kleber.parigi@aurum.com.br")
#time.sleep(2)
#pyautogui.press("enter")
#time.sleep(2)
#pyautogui.write("KPP5k@t32024!")
#time.sleep(2)
#print (pyautogui.position())
#pyautogui.click(x=292, y=453)