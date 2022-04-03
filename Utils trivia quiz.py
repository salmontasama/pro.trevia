print("welcome to the quiz game !!\n")
chances = 1
print ("you will have",chances,"chance to each question to answer correctly","\n","Please answer using the alphabet letters a - d !\n" )
score = 0
choice = ["a","b","c","d"]
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

question_3 = print("3) Black Panther is set in which fictional country?\n","(a) Ethiopia \n (b)  \n (c) Iron Man \n (d) Spiderman")
answer_3 = "b"

for i in range(chances):
    answer = input("Enter your answer :")
    if answer == answer_3:
        print("Correct!!, very nice\n")
        score+=10
        print("your score is: ",score)
        break
    while answer not in choice:
        print("Invalid input please answer using the alphabet letters a - d !")
        answer = input("try again :")
    else:
        print("Incorrect!\n")
        print("The correct answer is:",answer_3,"\n")


