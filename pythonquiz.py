print("Welcome to Python Quiz!!!")
playing=input("DO YOU WANT TO PLAY")
if playing.lower()!="yes":
    quit()
print("okay !! Lets Play!!!")
score=0
answer=input("1) who developed python")
if answer.lower()=="guido van rossum":
    print("         CORRECT ANSWER!!")
    score=+1
else:
    print("         WRONG ANSWER!!")

answer=input("2) what is the extension of python file")
if answer.lower()==".py":
    print("         CORRECT ANSWER!!")
    score=+2
else:
    print("         WRONG ANSWER!!")

answer=input("3) what are like container that are used to store data")
if answer.lower()=="variables":
    print("         CORRECT ANSWER!!")
    score=+3
else:
    print("         WRONG ANSWER!!")

answer=input("4) when was the python started")
if answer.lower()=="1991":
    print("         CORRECT ANSWER!!")
    score=+4
else:
    print("         WRONG ANSWER!!")

answer=input("5)how many conditional statements in python")
if answer.lower()=="6":
    print("         CORRECT ANSWER!!")
    score=+5
else:
    print("         WRONG ANSWER!!")

answer=input("6) which statement we can stop the loop before it has looped through all items")
if answer.lower()=="break statement":
    print("         CORRECT ANSWER!!")
    score=+6
else:
    print("         WRONG ANSWER!!")

answer=input("7)list some of numerical types in python")
if answer.lower()=="int,float and complex":
    print("         CORRECT ANSWER!!")
    score=+7
else:
    print("         WRONG ANSWER!!")

answer=input("8) In python, strings are surrounded by how many quotation marks")
if answer.lower()=="single or double":
    print("         CORRECT ANSWER!!")
    score=+8
else:
    print("         WRONG ANSWER!!")

answer=input("9) In python a function is defined by which key word ")
if answer.lower()=="def keyword":
    print("         CORRECT ANSWER!!")
    score=+9
else:
    print("         WRONG ANSWER!!")

answer=input("10) which key function works with files in python")
if answer.lower()=="open function":
    print("         CORRECT ANSWER!!")
    score=+10
else:
    print("         WRONG ANSWER!!")
print("YOU GOT "+str(score)+" QUESTIONS CORRECT")
print("YOU HAVE GOT "+str((score/10)*100)+"%")
