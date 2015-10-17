programIsActive= True;

while programIsActive:

 inputText = input("insert text\n");

 key = int(input("insert Key .. :"));

 crypto=[];
 s="";
 #kanei ta grammata mikra
 inputText= inputText.lower();
 # vgazei ta kena
 inputText = inputText.replace(" ","");

 print("\nArxiko keimeno  : ");
 print(inputText);

 for x in range(0, len(inputText)):
    crypto.append(ord(inputText[x]) + key)     
    
 for x1 in range(0, len(crypto)):
    s+=chr(crypto[x1]);
    
 print("\nKriptografimeno keimeno :  ");  
 print(s);


 UserChoise = input("Wanna do this again ?? y/n : ");
 if UserChoise=='n' :
    programIsActive=False;
    print("Okey ..bye bye :) " );
 elif UserChoise=='y' :
        programIsActive=True;
 else:
            print("i guess not , bye bye :) " );
