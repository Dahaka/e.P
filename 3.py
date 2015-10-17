import random
import sys




def to_number(obj):
    if( obj == 'rock'):
     return 0;
    elif(obj == 'spock'):
        return 1;
    elif(obj == 'paper'):
        return 2;
    elif(obj == 'lizard'):
        return 3;
    elif(obj == 'scissors'):
        return 4;
    else:
        print("wrong obj")

def to_obj(number):
     
    if(number == 0):
        return 'rock';
    elif(number == 1):
        return 'spock';
    elif(number == 2):
        return 'paper';
    elif(number == 3):
        return 'lizard';
    elif(number == 4):
        return 'scissors';
    else:
        print ("wrong number")

def R_P_S_L_S(choice):

    print("\nPlayer chooses " + choice)

    p_num = to_number(choice);

    c_num = random.randrange(0,5);

    c_choice = to_obj( c_num);

    print("Computer chooses " + c_choice);

    diff = (c_num - p_num) % 5;

    if( diff ==1 or diff==2):
        print("Sorry you loose. .. Computer wins..");

    elif(diff==4 or diff ==3 ):
        print("Congratulations!! U WON! ");
    else:
        print(" TIE ! ") 

print("Hello , this is a 'Rock, Paper, Scissors, Lizard, Spock' game");
programIsActive=True;
while programIsActive:

        playersChoise = input("plese select :rock/paper/scissors/lizard/spock  or exit \n");
        if(playersChoise=='exit'):
            sys.exit();
            
        
        if(playersChoise!='rock' and playersChoise!='paper' and playersChoise!='scissors' and playersChoise!='lizard' and playersChoise!='spock'):
            print("wrong input");
        else:    
            R_P_S_L_S(playersChoise);

            chooseToPlayAgain = input("Wanna play again ?? y/n : ");
            if chooseToPlayAgain=='n':
                programIsActive=False;
                print("OK , bye bye :) ");
            





