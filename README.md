# bot de spam pro zap por marina barberini

fiz esse bot pra dar aquela floodada básica ou automatizar mensagens no whatsapp usando python e pyautogui. o projeto ainda tá em desenvolvimento e vou incrementar mais coisas em breve.

## dimensões (leia isso)

by the way: como o pyautogui trabalha com cliques em pixels, as coordenadas que funcionam no meu monitor provavelmente não vão funcionar no seu. se você só baixar e der play, o mouse vai clicar em qualquer lugar, menos no campo de texto.

### como ajustar pro seu pc:
não entra em pânico, eu deixei um arquivo auxiliar pronto pra resolver isso.

1. abre o arquivo auxiliar (aquele que tem o time.sleep e o print(pyautogui.position())).
2. roda ele e corre com o mouse pra cima do campo de digitação do whatsapp ou do botão de enviar.
3. espera o tempo do sleep acabar e olha no terminal: ele vai te dar as coordenadas exatas (x e y) do seu monitor.
4. pega esses números e troca lá no código principal (main.py) dentro do comando pyautogui.click(x, y).

## o que usei
* python
* pyautogui (pra controlar o mouse e teclado)
* time (pra gerenciar os intervalos)

## próximos passos (vou incrementar)
o projeto ainda tá em obras. logo menos pretendo colocar:
* uma interface gráfica pra facilitar o uso.
* opção de puxar mensagens de um arquivo txt ou csv.
* tentar fazer o bot identificar o botão sozinho pra não depender de coordenadas.

## como rodar

1. clone o repositório:
git clone https://github.com/MarinaBarberini/spam-do-zap-INSUPORTAVEL.git

2. entre na pasta:
cd loopinsuportavel

3. instale as dependências:
pip install -r requirements.txt

4. ajuste as coordenadas usando o script auxiliar conforme explicado acima.

5. execute o bot:
python main.py

## dica de ouro
se o bot ficar maluco e começar a clicar onde não devia, só joga o mouse com tudo pro canto superior esquerdo da tela que o pyautogui para na hora (fail-safe).