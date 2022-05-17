vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
new_word = ""

word = input("Introduza uma palavra:")

for letter in word:
    if letter in vogais:
        if letter.islower():
            new_word = new_word + "g"
        elif letter.isupper():
            new_word = new_word + "G"
    else:
        new_word = new_word + letter 

print(new_word)