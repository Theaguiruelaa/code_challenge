import os
GoOn= True
No = 0 

while GoOn == True:
    question = input("You want to create more triangles (yes or no)?: ")

    if question.lower() == "no" :
        os.system("cls")
        print("Program is Terminated")
        break
    elif question.lower() == "yes":
        os.system("cls")
        No += 1
        for x in range(1,6):
            for r in range (1, No + 1):
                for y in range(1, x + 1):
                    print("^", end = " ")
                for z in range(6, x, -1):
                    print(" ", end = " ")
            print()
        continue 
    else:
        os.system("cls")
        print("Invalid Answer \nAnswer only Yes or No ")
        continue
        