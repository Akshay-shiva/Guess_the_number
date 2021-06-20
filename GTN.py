import random

games=int(input("how many games do you want to play \n"))

while games>=1:
    cunt=1;
    

    
    x=random.randint(1,20)
    #print(x)
    while  cunt>0:  
        p=int(input("Enter ur Number \n"))
        if p==x:
            
            print("You did it")
            break
        elif(p>x):
            print("na try lesser")
        elif p<x:
            print("try greater")
        else:
            print("loss")
        
        
        cunt+=1
    print("your cunts are %f" %cunt)
    
    games-=1
   
    


    
