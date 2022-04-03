print("welcome to the quiz game !!\n")
chances = 1
print ("you will have",chances,"chance to each question to answer correctly","\n","Please answer using the alphabet letters a - d !\n" )
score = 0
choice = ["a","b","c","d"]
choice_2 = ['a','b']
print("First topic is 'MARVEL'")
print("---------------------------------------\n")
question_1 = print("1) How many Infinity Stones are there?\n","(a) 4 \n (b) 2 \n (c) 8 \n (d) 6")
answer_1 = "d"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_1:
        print("Correct!!, Good job\n")
        score+=10
        print("your score is: ",score)
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_1,"\n")

print("---------------------------------------")

question_2 = print("2) Who was able to pick up Thor’s hammer in Endgame?\n","(a) Black Panther \n (b) Captain America \n (c) Iron Man \n (d) Spiderman")
answer_2 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_2:
        print("Correct!!, very nice\n")
        score+=10
        print("your score is: ",score)
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_2,"\n")

print("---------------------------------------")

question_3 = print("3) Black Panther is set in which fictional country?\n","(a) Ethiopia \n (b) London \n (c) Wakanda \n (d) Zimbabwe")
answer_3 = "c"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_3:
        print("Correct!!, MY Nigga\n")
        score+=10
        print("your score is: ",score)
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_3,"\n")

print("---------------------------------------")
print("Second topic is 'FOOTBALL'")

print("---------------------------------------")

question_4 = print("4) Which is not an English Football Club?\n","(a) Manchester United \n (b) PSG \n (c) Chelsea \n (d) Liverpool")
answer_4 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_4:
        print("Correct!!, MY Man\n")
        score+=10
        print("your score is: ",score)
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_4,"\n")


print("---------------------------------------")

question_5 = print("5) In 4-3-3 system, there are 3 Centre Backs?\n","(a) True \n (b) False ")
answer_5 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice_2:
        print("Invalid input please answer using the alphabet letters a or b !")
        answer = input("try again :")
    if answer == answer_5:
        print("Correct!!, Awesome \n")
        score+=10
        print("your score is: ",score)
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_5,"\n")


print("---------------------------------------")

question_6 = print("6) Which team is not in the Uefa Champions League Semi Finals this year?\n","(a) Real Madrid \n (b) Chelsea\n (c) Manchester City \n (d) Fc Barcelona")
answer_6 = "d"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_6:
        print("Correct!!, On Fire\n")
        score+=10
        print("your score is: ",score)
        break

    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_6,"\n")

print("---------------------------------------")
print("third topic is 'General Knowledge'")

print("---------------------------------------")

question_7 = print("7) Which animal is known as the 'Ship of the Desert?""\n","(a) Lion \n (b) Whale\n (c) Camel \n (d) Elephant")
answer_7 = "c"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_7:
        print("Correct!!, On Fire\n")
        score+=10
        print("your score is: ",score)
        break

    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_7,"\n")


print("---------------------------------------")

question_8 = print("8) Who painted the Mona Lisa?""\n","(a) Leonardo da Vinci \n (b) Rembrandt\n (c) Van Gogh \n (d) Claude Monet")
answer_8 = "a"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_8:
        print("Correct!!, King\n")
        score+=10
        print("your score is: ",score)
        break

    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_8,"\n")


print("---------------------------------------")

question_9 = print("9) Who is the highest spiritual leader of Tibet?""\n","(a) Dalai Lama \n (b) Damba Mali\n (c) prime minister \n (d) Mister Bean")
answer_9 = "a"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_9:
        print("Correct!!, King\n")
        score+=10
        print("your score is: ",score)
        break

    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_9,"\n")

print("---------------------------------------")
print("** BONUS POINTS **\n")
print("Last question for double points")
print("-------------------------------------")

question_10 = print("10) Where did Takela Mekonen(Tech CEO) served in the IDF?""\n","(a) 8200 \n (b) GOLANI \n (c) Drone Unit \n (d) All of the above ")
answer_10 = "c"

for i in range(chances):
    answer = input("Enter your answer :")
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    if answer == answer_10:
        print("Correct!!, ALUFIM\n")
        score+=20
        print("your score is: ",score)
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_10,"\n")
if score < 70:
    print("keep studying")
elif 70 < score < 90 :
    print("close to perfection")
elif 90 < score < 100 :
    print("You are a genius")
elif score > 100:
    print("You're too smart for this test")
print("Game Over")