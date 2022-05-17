import os

#Declaração das varáveis:
example1 = "StOnKs HiGh"
count_up = 0
count_low = 0

#Deteção de input do utilizador:
print('Para um exemplo pressione "i", para continuar pressione "Enter".')
if input() == str("i"):
    phrase = example1
else:
    phrase = str(input("Introduza uma frase: "))

#Ciclo para identificar quantas maiúsculas e minúsculas existem:
for i in phrase:
    if i.isupper():
        count_up = count_up + 1
for n in phrase:
    if n.islower():
        count_low = count_low + 1

os.system("clear")

#Print das mensagens com o resultado consoante a frase inserida:
if count_up == 0 and count_low == 0:
    print("Erro: Não foi inserido qualquer carácter!")
else:
    print('Na frase "' + phrase + '":\n')
    if count_up <= 1:
        if count_up == 0:
            print("-não existem maiúsculas.")
        if count_up == 1:
            print("-existe", count_up, "maiúscula.")
    else:
        print("-existem", count_up, "maiúsculas.")
    if count_low <= 1:
        if count_low == 0:
            print("-não existem minúsculas.\n")
        if count_low == 1:
            print("-existe", count_low, "minúscula.\n")
    else:
        print("-existem", count_low, "minúsculas.\n")

