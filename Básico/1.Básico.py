import random

print("Numeros randomicos!\n")

for i in range(5):
    print(random.random())

''' Em Python as variáveis são como objetos,
 então podemos alterar o tipo de dado dela
 conforme o programa avança '''

# A. uma variável do tipo int
variavel = 10

#  exibe a variável
print("\n A.")
print(variavel)

# B. agora ela será float
variavel = 1.23

#  exibe a variável
print("\n B.")
print(variavel)

# C. agora ela será boolean
variavel = True

#  exibe a variável
print("\n C.")
print(variavel)


''' Em Python as operações matemáticas são
bem semelhantes com as demais linguagens '''

# D. Operações matemáticas básicas
variavel = 10 + ((1200/10) - (2*10))

#  exibe a variável
print("\n D.")
print(variavel)

# E. Uma exponenciação nom**exp
variavel = 4**2

#  exibe a variável
print("\n E.")
print(variavel)

# F. Operação de módulo
variavel = 4 % 2

#  exibe a variável
print("\n F.")
print(variavel)
