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
    if answer == answer_1:
        print("Correct!!, Good job\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_1,"\n")

print("---------------------------------------")

question_2 = print("2) Who was able to pick up Thor’s hammer in Endgame?\n","(a) Black Panther \n (b) Captain America \n (c) Iron Man \n (d) Spiderman")
answer_2 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    if answer == answer_2:
        print("Correct!!, very nice\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_2,"\n")

print("---------------------------------------")

question_3 = print("3) Black Panther is set in which fictional country?\n","(a) Ethiopia \n (b) London \n (c) Wakanda \n (d) Zimbabwe")
answer_3 = "c"

for i in range(chances):
    answer = input("Enter your answer :")
    if answer == answer_3:
        print("Correct!!, MY Nigga\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_3,"\n")

print("---------------------------------------")
print("Second topic is 'FOOTBALL'")

question_4 = print("4) Which is not an English Football Club?\n","(a) Manchester United \n (b) PSG \n (c) Chelsea \n (d) Liverpool")
answer_4 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    if answer == answer_4:
        print("Correct!!, MY Man\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_4,"\n")


print("---------------------------------------")

question_5 = print("5) In 4-3-3 system, there are 3 Centre Backs?\n","(a) True \n (b) False ")
answer_5 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    if answer == answer_5:
        print("Correct!!, MY Man\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice_2:
        print("Invalid input please answer using the alphabet letters a or b !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_5,"\n")


print("---------------------------------------")

question_6 = print("6) Which team is not in the Uefa Champions League Semi Finals this year?\n","(a) Real Madrid \n (b) Chelsea\n (c) Manchester City \n (d) Fc Barcelona")
answer_6 = "d"

for i in range(chances):
    answer = input("Enter your answer :")
    if answer == answer_6:
        print("Correct!!, On Fire\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_6,"\n")
