# bot de spam pro zap

fiz esse bot pra dar aquela floodada básica ou automatizar mensagens no whatsapp usando python e pyautogui. é simples, funcional e quebra um galhão.

## aviso importante: o bagulho das dimensões

by the way: como o pyautogui trabalha com cliques em pixels, as coordenadas que funcionam no meu monitor provavelmente não vão funcionar no seu. se você só baixar e der play, o mouse vai clicar em qualquer lugar, menos no campo de texto.

### como ajustar pro seu pc:
não entra em pânico, eu deixei um arquivo auxiliar pronto pra resolver isso.

1. abre o arquivo auxiliar (aquele que tem o time.sleep e o print(pyautogui.position())).
2. roda ele e corre com o mouse pra cima do campo de digitação do whatsapp ou do botão de enviar.
3. espera o tempo do sleep acabar e olha no terminal: ele vai te dar as coordenadas exatas (x e y) do seu monitor.
4. pega esses números e troca lá no código principal. gg!

## o que usei:
* python
* pyautogui (pra controlar o mouse e teclado)
* time (pra dar aquele respiro entre um clique e outro)

## próximos passos (vou incrementar!)
o projeto ainda tá em obras. logo menos pretendo colocar:
* tentar fazer ele identificar o botão sozinho (pra acabar com esse drama das dimensões).

## como rodar
1. instala o pyautogui: pip install pyautogui
2. ajusta as coordenadas usando o script auxiliar.
3. dá o play e seja feliz (mas não seja banido kkk).

dica: se o bot ficar maluco e começar a clicar onde não devia, só joga o mouse com tudo pro canto da tela que o pyautogui para na hora (fail-safe).