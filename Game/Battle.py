#import module random
import random

#declare variables
text=''
text_pn=''

#get user input
DON = input("Enter player name : ")
DON= DON.capitalize()
print("\nWELCOME",DON,":)"+" "+"Letter-Kind IS WAITING FOR YOU TO SAVE THEM FROM EVIL NUMBERS.\n")    
print("\nPlayer name : ",DON)
text+="\nPlayer name : "
text+=DON

#use a function for the program
def Battle_fun_don():
    ''' this block will run the game'''
    global text#for the text file 
    #declare local variables
    ch_ev=''
    text_killed=''
    att=''
    text_ls=''
    text_def=''
    text_enemy=''
    text_total=''
    ls=''
    ev=''
    text=''
    text_total=''
    text_fs=''
    text_gs=''
    text_pn=''
    attem=0
    attempt=1
    score=0
    evil_numbers=[]
    enemy=0
    life_score=random.randrange(1,51)#get a life score between 1-50
    for y in range(1,22):
        evil_numbers=[]
        for i in range(1,6):#get 5 evil numbers
            if attempt<=5:
                enemy=random.randrange(15,101)#get a rendom number between 15-100
            elif 5<attempt<=10:
                enemy=random.randrange(250,2001)#get a rendom number between 250-2000
            elif 10<attempt<=15:
                enemy=random.randrange(3000,10001)#get a rendom number between 3000-10000
            else:
                15<attempt<=20
                enemy=random.randrange(20000,100001)#get a rendom number between 20000-100000
            evil_numbers.append(enemy)
            
        print('Attempt is : ',attempt)#print attempt
        txt_att='\n\nAttempt is : '
        att=str(attempt)
        text+=txt_att
        text+=att
        attempt+=1
        print(DON+"'s"+' life score is: ',life_score)
        ls=str(life_score)
        text+='\n'+DON
        text+="'s life score is: "
        text+=ls

        #take out the rendom evil numbers from the list
        text+="\nPresented enemies:"

        #take out the rendom evil numbers from the list
        for x in evil_numbers:
            print(x,end=' ')
            ev=str(x)
            text+='\n'+ev
        #use error handling
        try:
            choose=int(input(" \nChoose your Evil number to fight with : "))
            ch_ev=str(choose)
            text+='\nThe evil number that was selected is : '
            text+=ch_ev
            if choose not in evil_numbers:
                print(choose,'is not there to fight')
                ch_ev=str(choose)
                text+='\n'+ch_ev
                text+=' '+'is not there to fight'
                print("\n\n*** Game status ***")
                text_gs="\n\n\n*** Game status ***"
                text+=text_gs
                print("\nPlayer name : ",DON)
                text_pn="\n\nPlayer name : "
                text+=text_pn
                text+=DON
                print("Total attempts : ",attempt-1)
                att=str(attempt-1)
                text+="\nTotal attempts : "
                text+=att
                print("Final score is : ",life_score)
                text_fls=str(life_score)
                text+="\nFinal score is : "
                text+=ls
                print(DON,"was defeated\n")
                text+='\n'+DON
                text+=' '+"was defeated\n"
                break

            elif choose<=life_score:
                print(DON,"killed",choose,'\n')
                ch_ev=str(choose)
                text+='\n'+DON
                text+=' '+"killed"
                text+=' '+ch_ev
                life_score=life_score+choose
                if attempt==21:
                    print("\n\n*** Game status ***")
                    text+="\n\n\n*** Game status ***"
                    print("\nPlayer name : ",DON)
                    text+="\n\nPlayer name : "
                    text+=DON
                    print("Total attempts : ",attempt-1)
                    text+="\nTotal attempts : "
                    attem=attempt-1
                    att_1=str(attem)
                    text+=att_1
                    print("Final score is : ",life_score)
                    text+="\nFinal score is : "
                    text+=ls
                    
                    print("Letter-kind was saved by",DON,'~-'+'\n Congratulations',DON,'you won the game.')
                    text+="\nLetter-kind was saved by"
                    text+=' '+DON
                    break
            else:
                print(choose,"killed",DON)
                ch_ev=str(choose)
                text+='\n'+ch_ev
                text+=' '+"killed"
                text+=' '+DON
                print("\n\n*** Game status ***")
                text+="\n\n\n*** Game status ***"
                print("\nPlayer name : ",DON)
                text+="\n\nPlayer name : "
                text+=DON
                print("Total attempts : ",attempt-1)
                attemp=str(attempt-1)
                text+="\nTotal attempts : "
                text+=attemp
                print("Final score is : ",life_score)
                text+="\nFinal score is : "
                text+=ls
                print(DON,"was defeated\n")
                text+='\n'+DON
                text+=' '+"was defeated\n"
                break
        except ValueError:
            print('No such enemy')
            text+='\nNo such enemy'
            print("\n\n*** Game status ***")
            text+="\n\n\n*** Game status ***"
            print("\nPlayer name : ",DON)
            text+="\n\nPlayer name : "
            text+=' '+DON
            print("Total attempts : ",attempt-1)
            r_attempt=str(attempt-1)
            text+="\nTotal attempts : "
            text+=r_attempt
            print("Final score is : ",life_score)
            text+="\nFinal score is : "
            text+=ls
            
            print(DON,"was defeated\n")
            text+='\n'+DON
            text+=' '+"was defeated\n"
            break
    return text#return the value of text to do the file writing
        
        
        
    


