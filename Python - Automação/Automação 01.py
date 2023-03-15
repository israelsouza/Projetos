import pyautogui as pya
import time
import pandas as pd
import pyperclip

# ETAPA 1 - LOGIN E IMPORTAR BASE DE DADOS -----------------------------------

pya.PAUSE = 1.2

# Acessar site para pegar base dados
pya.press('win')
pya.write('edge')
pya.press('enter')
pya.hotkey('ctrl', 't')
pya.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pya.press("enter")

time.sleep(5)

# Fazer o login
pya.click(x=890, y=552)
pya.write('meu usuario')
pya.press('tab')
pya.write('minha senha')
pya.press('tab')
pya.press('enter')

time.sleep(7)

# baixar base de dados
pya.click(x=533, y=446)
pya.click(x=1032, y=294)
pya.click(x=1197, y=894)

time.sleep(10) # tempo para download, opc

# ETAPA 2 - INDICADORES -----------------------------------

# Criacao

tabela = pd.read_csv(r"C:\Users\israe\Downloads\Compras.csv", sep=';')
display(tabela)

total_gasto = tabela["ValorFinal"].sum()
produto = tabela["Quantidade"].sum()
valor_medio = total_gasto / produto

print(total_gasto)
print(produto)
print(valor_medio)

# ETAPA 3 - E-MAIL -----------------------------------

# escrever e enviar

texto = f"""Bom dia chefe!
Conforme pedido em daily, segue o relatório de compras:

Total Gasto: R$ {total_gasto:,.2f}
Quantidade de Produtos: {produto:,}
Preço Médio: R$ {valor_medio:,.2f}
"""

pya.PAUSE = 1

pya.click(x=696, y=1036)

time.sleep(7)

pya.click(x=34, y=160)
pya.write('apps.sites.sistematico@gmail.com')
pya.press('tab')
pya.press('tab')
pya.press('tab')
pya.write('testando automação')
pya.press('tab')
pyperclip.copy(texto)
pya.hotkey('ctrl', 'v')
pya.click(x=1765, y=86)