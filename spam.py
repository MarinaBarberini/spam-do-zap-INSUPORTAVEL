import pyautogui
import time

#---------atemçao! modificar as dimensoes da funcao click pro SEU monitor!!------------

pyautogui.PAUSE = 0.5 #senao trava tudo

frase = "marina e o maximo"  # frase que sera spammada
contato = "papagaio da minha vó"


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

for i in range(1000):  # numero de vezes que a frase sera spammada (pode muda!!)
    pyautogui.write(frase)
    pyautogui.press("enter") #envia

