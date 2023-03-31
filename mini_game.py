# Jogo para adivinhar um número gerado aleatoriamente
import random

palpite = 0
numero = random.randint(1,9)
pontos = 0
resposta = ''
palpite= ''

while resposta != 'S':    
        print("Qual o número correto? (de 1 á 9)")
        palpite = int(input(''))
        print(f'Este é o seu palpite? {palpite}')
        resposta = (input('Responda com S ou N.'))
        if resposta == 'S':
            if palpite == numero:
                pontos += 1 
                print(f'Parabens! Você acertou!. \n Potuanção: {pontos}')
            elif palpite != numero:
                print (f'Game Over! Sua pontuação foi de {pontos}. \n O Número era {numero}')