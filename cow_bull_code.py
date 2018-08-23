import random
number=[]
attempts=0
def MakeNumber():
    for i in range(4):
        x=random.randrange(0,9)
        number.append(x)
    if len(number)>len(set(number)):
        number.clear()
        MakeNumber()
def PlayGame():
    global attempts
    attempts+=1 
    cows=0
    bulls=0
    #print(number)
    choice=input("Please enter a 4 digit number\n")
    guess=[]
    for i in range(4):
        guess.append(int(choice[i]))
    if len(guess)>len(set(guess)):
        attempts-=1 
        print("please enter distinct digits\n")
        PlayGame()
    for i in range(4):
        for j in range(4):
            if i!=j:
                if(guess[i]==number[j]):
                    cows+=1 
            if i==j:
                if(guess[i]==number[i]):
                    bulls+=1 
    print("bulls ",bulls)
    print("cows ",cows)
    if bulls==4:
        print("congratulations you won in ",attempts," attempts")
        exit()
    if bulls!=4:
        PlayGame()
MakeNumber()
PlayGame()