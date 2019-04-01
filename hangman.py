

def printing():
    
    num=0
    for a in word:
        if a in z:
            print(a,end=" ")
            num=num+1
        else:
            print("-",end=" ")

    if num<len(word):
        inputing()
    else:
        gameover('w')        
def inputing():
    
    global lives
    #print(len(word_list))
    let=input("\nEnter a letter: ")
    clear()
    if let in word:
        if len(let)==1:
            if let in z:
                print("The letter is already in the word")
            else:
                print("Correct letter")
                z.append(let)
        else:
            print("Too many letters entered or nothing entered...")
            
    else:
        if let in wl:
            
            print("You have tried this letter before...")
        else:
            if not let.isalpha():
                
                print("You have not entered a letter...")

            else:
                if len(let)>1:
                    
                    print("You have entered more than 1 letters")
                else:    
                    wl.append(let)
                    lives = lives-1
                   
                    print("Wrong letter, you lose a life. Now you have",lives)
            
    if lives>0:
        printing()
    else:
        gameover('l')

def menu():
    clear()
    print("1. Play")
    print("2. Exit")
    mcho=input();
    clear()
    if mcho=='1':
        printing()
    else:
        bye=input("OK Bye\nPress Enter to Exit")
        sys.exit(0)

    


    
def gameover(x):
    if x=='l':
        print ("\nYou lose")
        print ("The word was",word)
        
    else:
        print("\nYou win")
    ask=input("Press Enter for Menu")
import sys
import os
clear = lambda: os.system('cls')


import random
word_list=['attention','something','significant','earth','teacher','school','television','global',
           'table','defender','street','device','balcony','house',
           'ministry','liberty','bottle','conversation','drink','paper',
           'plate','border','pillow','curtain','independent','sandwich',
           'whiskey','action','greeting','world','space','stranger','iron','glass',
           'yellow','brown','stupid','woman','spirit','queen','spaceship',
           'screen','elevator','elbow','castle','century','beautiful','dragon',
           'option','against','recorder','human','president','government',
           'lawyer','investigation','statement','comment','surprise','immediately']
while True:
    
    i=random.randrange(len(word_list)-1)
    word=word_list[i]
    #word="television"
    z=[word[0],word[(len(word)-1)]]
    wl=[]

    lives=3
    menu()
    
