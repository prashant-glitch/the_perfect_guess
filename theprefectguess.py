import random

#i=0
def guessnumber(comp,you):
    while True:
        if you>comp:
            print("you entered a greater number")
            b=int(input("enter the number you guessed\n"))
            #i+=1
            guessnumber(comp,b)
        elif you<comp:
            print("you entered a lesser number")
            a=int(input("enter the number you guessed\n"))
            #i+=1
            guessnumber(comp,a)
        else:
            print("you guess the perfect number\n")
            print(f"CONGRATS!!! ")
            #print(f"your guess attempt is {i}")
            break
        break
print("guess a number between 1  <---and---> 100   !!!!!!!")
you=int(input("enter the number you guessed\n"))
comp=random.randint(1,100)
guessnumber(comp,you)
