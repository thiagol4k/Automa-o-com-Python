# passo 1 - entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# biblioteca necessária: pip install pyautogui
import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey (atalho)

pyautogui.PAUSE = 1
# "PAUSE = 1" a cada comando que vai rodar ele aguarda 1 segundo a cada comando

# apertar a tecla do windons
pyautogui.press("win")
# digita o nome do programa
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=794, y=508)

# inserir o link (Utilizado o de teste disponibilizado pela hashtagtreinamentos)
link ="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# espera 1 segundos
time.sleep(1)


# passo 2 - fazer login

pyautogui.click(x=665, y=375)
# digitar o email
pyautogui.write("pythonimpressionador@gmail.com")
# passar para o campo da senha
pyautogui.press("tab")
# digitar minha senha 
pyautogui.write("minha senha")
# clicar no botão do login
pyautogui.click(x=785, y=530)
time.sleep(1)

# passo 3 - importar a abase de dados
# biblioteca necessária: pip install pandas numpy openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# passo 4 - cadastrar um produto 
for linha in tabela.index:
    pyautogui.click(x=696, y=260)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

# passo 5 - repetir isso até acabar a base de dados

