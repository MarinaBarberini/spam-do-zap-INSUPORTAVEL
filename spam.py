import pyautogui
import time
import random

#---------atemçao! modificar as dimensoes da funcao click pro SEU monitor!!------------

frase = "ooooooooi miguel"  # frase que sera spammada
contato = "lindo pepeka pepeka"
repeticoes = 50

#----------- modificar a frase contato e repeticoes

pyautogui.PAUSE = 0.5 #senao trava tudo

pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter") 

time.sleep(5) #cu down né

pyautogui.click(x=246, y=118) # coordenadas campo escrever zap
pyautogui.write(contato)

time.sleep(5) #cu down dois

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

#selecionar campo d escrita
pyautogui.click(x=699, y=671)
pyautogui.press("space") 
pyautogui.press("backspace") 

for i in range(repeticoes):  # numero de vezes que a frase sera spammada (pode muda!!)
    pyautogui.write(frase) 
    pyautogui.press("enter")
    #evita ban
    time.sleep(random.uniform(0.5, 2.0))

print("missao cumprida kkk")
