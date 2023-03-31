# Exercicio 2
# Área de Retangulo

def retangulo():
    b=input('Insira a base do retangulo em M ')
    h=input('Insira a altura do retangulo em M ')
    a=(int(b)*int(h))
    print(f"A área do retangulo é {a}M Quadrados")

# Exercicio 3
# Área do Quadrado
def quadrado():
    l=input('Insira o tamanho do lado do quadrado em M')
    aq=(int(l)**2)
    print(aq)

# Exercicio 4
# Um produto custa (x) reais, quanto fica com (y%) de desconto

def desconto():
    x=(input('Insira o valor em reais: R$'))
    y=(input(f'Insira a porcetagem de desconto:'))
    desconto_real = (int(y)/100)
    preco=(int(x)*desconto_real)
    preco_real = (int(x)-preco)
    print(preco_real)

# Exercicio 5
# Área de um circulo
import math

def circulo():
    print('Use uma regua para medir o ponto mais longe do outro no circulo')
    d = input('Insira oque obteve em Cm: ')
    radius = (int(d)/2)
    area = math.pi * (radius**2)
    print(f"A área do circulo é {round(area)}Cm")

# Exercicio 6
# Convertendo Real para Dólar
from forex_python.converter import CurrencyRates
def real_to_dolar():
    c = CurrencyRates()
    rate = c.get_rate('USD', 'BRL')
    real =(input('Insira a quantidade de Reais para converter: BRL R$'))
    real_to_dolar = (int(real)/int(rate))
    print(f'R${round(int(real))} = ${round(int(real_to_dolar))}')

# Exercicio 7
# Convertendo Dólar para Real
from forex_python.converter import CurrencyRates
def dolar_to_real():
    c = CurrencyRates()
    rate = c.get_rate('BRL', 'USD')
    dolar =(input('Insira a quantidade de Dólares para converter: USD $'))
    dolar_to_real = (int(dolar)/rate)
    print(f'USD ${round(int(dolar))} = BRL R${round(int(dolar_to_real))} ')
