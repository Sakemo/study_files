import openpyxl

# Cria uma nova planilha
wb = openpyxl.Workbook()

# Seleciona a planilha ativa
sheet = wb.active

# Adiciona alguns valores na planilha
sheet['A1'] = 'Nome'
sheet['B1'] = 'Idade'
sheet['A2'] = 'João'
sheet['B2'] = 30
sheet['A3'] = 'Maria'
sheet['B3'] = 25

# Salva a planilha em um arquivo
wb.save('exemplo.xlsx')
