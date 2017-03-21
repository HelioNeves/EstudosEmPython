
''' Arquivo Python trabalham em
 utf-8 e por isso por padrão não
 exibem acentos em strings '''

# A. Usando uma String
nome = "Helio"

print("\n A.")
print(nome)

# B. Usando uma String
nome = "Helio"[0]

print("\n B.")
print(nome)

# C. Métodos de strings
nome = "Neves"

print("\n C.")
print(len(nome))
print(nome.lower())
print(nome.upper())

# D. Conversão de strings
pi = 3.14

print("\n D.")
print(str(pi))

# E. Concatenação de strings
print("\n E.")
print("Helio" + " " + "Neves")

# F. Formatando o print
nome = "Helio"
idade = 22

print("\n F.")
print(nome, " " + "tem" + " " , str(idade), " " + "anos")
