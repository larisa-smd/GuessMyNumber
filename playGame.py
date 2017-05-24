import random,os,io,time,sys

play=True

while True:
    fileName="rank.txt"
    wins=0
    loses=0
    found=False


    print ("Lets play a game: Guess my number!")
    userName=input("Your name please:  ")
    userName=userName.capitalize()

    try:
        f=open(fileName,"r+")
        line=f.readline()
        while line!="":
            if line.find(userName.capitalize())>0:
                words=line.split(";")
                wins=int(words[1][2:])
                loses=int(words[2][2:-1])
                found=True
            line=f.readline()
        f.close()
    except IOError as e:
        print ("WELCOME!! "+userName);


    while play:

        print ("OK %s,  I am thinking of a number between 1 and 10, you have 3 attempts to guess." %userName)

        userGuesses=0
        winner=False

        myNumber= random.randint(1,10)

        while userGuesses<3 and winner==False:
            number=False
            guess=0
            while  not number:
                print ( "Can you guess my number?? ")
                guess=input()
                if guess.isdigit()==True :
                    guess=int(guess)
                    number=True
                else:
                    print ("You didn't  enter a number. We'll try again.")
                    number=False

            if guess<myNumber:
                print ("The guess is too low.")
                userGuesses +=1
            if guess>myNumber:
                print ("The guess is too high. ")
                userGuesses +=1
            if  guess==myNumber:
                winner=True


        if winner:
            print ("You win!!! Congratulation %s !!" %userName)
            wins+=1
        elif userGuesses==3:
            print ("You lose! The number was %d" %myNumber)
            loses+=1

        games=wins+loses
        print ("The total number of games played is %d; Wins: %s; Loses: %s  " %(games,wins,loses))
        print ("If you want to play more press Enter, if not  pres q and enter!")
        q=input()
        if q.lower()=="q":
            play=False

    mess="U:%s;W:%s;L:%s\n"  %(userName,wins,loses)

    if found:
            print ("Updating the file...")
            try:
                f=open(fileName,"r+")
                newf=open("new.tmp","w+")
                line=f.readline()
                while line!="":
                    if line.find(userName.capitalize())>0:
                        newf.write(mess)
                    else:
                        newf.write(line)
                    line=f.readline()
                f.close()
                newf.close()
                os.remove(fileName)
                os.rename(newf.name,"rank.txt")
            except IOError as e:
                print ("There was some problem updating the file....")
            print ("Updating finished.")
    else:
        print ("Saving the scores....")
        f=open(fileName,"at")
        f.write(mess)
        f.close()
        print ("Saving finished ")

    if play==False:
        print ("I am sorry but you have to leave. I am still waiting for my next player!")
        time.sleep(3)
        print ("Have a nice day!! ByBy..")
        play=True
        myNumber= random.randint(1,10)
        time.sleep(3)

