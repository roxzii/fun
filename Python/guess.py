user_word = ""
secret = "Pilão"
guess = 1
out_of_guess = False
guess_limit = 5

#Algoritmo do jogo (assenta num ciclo "while"):
while user_word != secret and user_word != "q" and not out_of_guess:
    if guess == guess_limit:
        out_of_guess = True
    user_word = input("Introduza uma palavra para jogar: ")
    guess += 1
    if guess == 2:
        print("\nPista: É usado em coisas húmidas!\n")
    elif guess == 3:
        print("\nTem um formato fálico!\n")
    elif guess == 4:
        print("\nMete-se e tira-se com força!\n")
    elif guess == 5:
        print('\nPrima "q" para desistir!\n')

#Verifica se o user venceu:
if user_word == secret:
    print("\n\nParabéns, acertou!\n\n")
else:
    print('\n\nA palavra correta era "Pilão", como é óbvio!\n\n')
