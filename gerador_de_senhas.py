# Exercicio Gerador de Senhas
# Mais de 10 Caracteres
# Sem palavras de dicionario
# Inclua Caractere Especial

#Criptografia:
 # A = !
 # B = @
 # C = #
 # D = $
 # E = %
 # F = ¨
 # G = &
 # H = *
 # I = 1
 # J = 4
 # K = _
 # L = /
 # M = 7
 # N = q
 # O = 9
 # P = E
 # Q = A
 # R = 5
 # S = 8
 # T = H
 # U = Ç
 # V = 3
 # W = J
 # X = +
 # Y = }
 # Z = {

key = input('Insira uma chave para criptografar: ')
senha = ""

for letra in key:
 if letra in "Aa":
     senha = senha + "!"
 elif letra in "Bb":
     senha = senha+ "@"
 elif letra in "Cc":
     senha = senha+ "#"
 elif letra in "Dd":
     senha = senha + "$"
 elif letra in "Ee":
     senha = senha + "%"
 elif letra in "Ff":
     senha = senha + "¨"
 elif letra in "Gg":
     senha = senha + "&"
 elif letra in "Hh":
     senha = senha + "*"
 elif letra in "Ii":
     senha = senha + "1"
 elif letra in "Jj":
     senha = senha + "4"
 elif letra in "Kk":
     senha = senha + "_"
 elif letra in "Ll":
     senha = senha + "/"
 elif letra in "Mm":
     senha = senha + "7"
 elif letra in "Nn":
     senha = senha + "q"
 elif letra in "Oo":
     senha = senha + "9"
 elif letra in "Pp":
     senha = senha + "E"
 elif letra in "Qq":
     senha = senha + "A"
 elif letra in "Rr":
     senha = senha + "5"
 elif letra in "Ss":
     senha = senha + "8"
 elif letra in "Tt":
     senha = senha + "H"
 elif letra in "Uu":
     senha = senha + "Ç"
 elif letra in "Vv":
     senha = senha + "3"
 elif letra in "Ww":
     senha = senha + "J"
 elif letra in "Xx":
     senha = senha + "+"
 elif letra in "Yy":
     senha = senha + "}"
 elif letra in "Zz":
     senha = senha + "{"
print(senha)