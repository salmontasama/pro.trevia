def newGame():
    pass


def chekAnser(answer, guess):
    if answer == guess:
        print("Correct!!, MY Nigga")
        return 10
    else:
        print("WORNG!! LOSER")
        return 0

def displayScore(corrcet_guesses,guuses):
    print("---------------------------------------")
    print("RESULTS")
    print("---------------------------------------")

    print("Answers :",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("you'r guesses:",end=" ")
    for i in guuses:
        print(i)
    print()

    score = int((corrcet_guesses/len(questions))*100)
    print("your score is : "+str(score))


def playAgain():
    pass


questions = {
    'How many Infinity Stones are there?:': 'd',
    'Who was able to pick up Thor’s hammer in Endgame?': 'b',
    'Black Panther is set in which fictional country?': 'c',
    'Which is not an English Football Club?': 'b',
    'In 4-3-3 system, there are 3 Centre Backs?': 'b',
    'Which team is not in the Uefa Champions League Semi Finals this year?': 'd',
    'Which animal is known as the Ship of the Desert?': 'c',
    'Who painted the Mona Lisa?': 'a',
    'Who is the highest spiritual leader of Tibet?': 'a',
    'Where did Takela Mekonen(Tech CEO) served in the IDF?': 'c'

}
options = [['(a) 4 \n (b) 2 \n (c) 8 \n (d) 6'],
           ['(a) Black Panther \n (b) Captain America \n (c) Iron Man \n (d) Spiderman'],
           ['(a) Ethiopia \n (b) London \n (c) Wakanda \n (d) Zimbabwe'],
           ['(a) Manchester United \n (b) PSG \n (c) Chelsea \n (d) Liverpool'],
           ['(a) True \n (b) False '],
           ['(a) Real Madrid \n (b) Chelsea\n (c) Manchester City \n (d) Fc Barcelona'],
           ['(a) Lion \n (b) Whale\n (c) Camel \n (d) Elephant'],
           ['(a) Leonardo da Vinci \n (b) Rembrandt\n (c) Van Gogh \n (d) Claude Monet'],
           ['(a) Dalai Lama \n (b) Damba Mali\n (c) prime minister \n (d) Mister Bean'],
           ['(a) 8200 \n (b) GOLANI \n (c) Drone Unit \n (d) All of the above']]


