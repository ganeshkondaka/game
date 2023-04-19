while True:
    import random as rnd
    import time as t
    ds=("rock","paper","scissor")
    cc=rnd.choice(ds)
    t.sleep(0.5)
    print("------------------------------")
    print("******ROCK PAPER SCISSOR******")
    print("------------------------------")
    t.sleep(0.5)
    print("")
    print("winnig rules :------")
    print("rock vs paper -> paper wins")
    print("rock vs scissor -> rock wins")
    print("paper vs scissor -> scissor wins")
    print("")
    t.sleep(0.5)
    print("enter your choice")
    t.sleep(0.5)
    print("  rock")
    t.sleep(0.5)
    print("  paper")
    t.sleep(0.5)
    print("  scissor")
    t.sleep(0.5)
    print("")
    ut=input("user turn : ")
    t.sleep(0.5)

    if ut=="rock":
        print("user choice is : rock")
    elif ut=="paper":
        print("user choice is : paper")
    elif ut=="scissor" :
        print("user choice is : scissor")
    else:
        print("please enter valid input")
    print("")
    t.sleep(1)

    f=["rock","paper","scissor"]
    if (ut in f ):
        print("now it is computer turn")
        t.sleep(2)
        print("computer choice is : ",cc)
        print("")
        
        t.sleep(0.9)
        print(ut,"vs",cc)
        print("")
        fin=(ut+cc)
        t.sleep(2.5)
        if ut == cc:
            print("< Draw >")
        elif ut=="rock" and cc=="scissor":
            print(ut," wins < user wins >")
        elif ut=="paper" and cc=="rock":
            print(ut," wins < user wins >")
        elif ut=="scissor" and cc=="paper":
            print(ut," wins < user wins >")
        else:
            print(cc," wins < computer wins >")
        print("------------------------------")
        t.sleep(0.5)
        
    else:
        print("please enter valid input")

    print("do you want to play again (y/n)")
    ans=(input(">>> "))
    
    if ans=="y":
        continue
    else:
        print("thanks for playing")
        t.sleep(0.5)
        break
        




