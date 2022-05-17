import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [

"Que companhia produziu o filme Up! Altamente !\n(a) Walt Disney Studios\n(b) Lusomundo\n(c) Pixar\n(d) MGM\n\n",
"Qual Foi A Batalha Mais Mortal Da Segunda Guerra Mundial?\n(a) Moscovo\n(b) El Alamein\n(c) Estalinegrado\n(d) La Lys\n\n",
"O ferro é essencial ao corpo humano porque :\n(a) Dá Resistência aos ossos\n(b) Ajuda a digestão\n(c) Fixa o oxigénio\n(d) Faz parte do sistema imunológico\n\n",
"Qual Foi O Cognome do Décimo Segundo  Rei De Portugal?\n(a) O Lavrador\n(b) O Eloquente\n(c) O Desejado\n(d) O Africano\n\n",
"Qual era o 1º Nome de Picasso?\n(a) Pablo\n(b) Diego\n(c) Jorge\n(d) Nuno\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "a")
]

def jogo(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            os.system("clear")
        elif answer != ["a", "b", "c", "d"]:
            os.system("clear")
            print("Error")
            break
    print("\n\nTeve " + str(score) + "/" + str(len(questions)) + " questões corretas!\n\n")

jogo(questions)