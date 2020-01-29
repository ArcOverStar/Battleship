import random, sys
UB=[]#User's board
CB=[]#Computer's Board
TB =  [["0","0","0","0","0","0","0","0","0","0"],#Target Board
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"]]
ship = {'C':["Carrier",5],'B':["Battleship",4],'S':["Submarine",3],'c':["Cruiser",3],'D':["Destroyer",2]}
symbol = list(ship.keys())
hit = False#Loop checks
end = False

def user_set_board():#Fuction to let user set the board
    confirm = False
    while (not confirm):
        B = [["0","0","0","0","0","0","0","0","0","0"],#Placeholder Board
             ["0","0","0","0","0","0","0","0","0","0"],
             ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"],
              ["0","0","0","0","0","0","0","0","0","0"]]
        k = 0 #Helps in the initialization of pieces
        placed = False#Placement check    
        ori =''#Orientation of ship
        conf = ''#Yes or No to Board setup
        for i in range(0,5): 
                chk=0
                print("Input ",ship[symbol[i]][0],"\'s coordinates",sep='')
                while(not placed):
                    x = int(input("Enter x coordinate(0-9): "))
                    y = int (input("Enter y coordinate(0-9): "))
                    if (B[y][x]=="0"):
                        ori = str(input("Enter orientation of ship(h/v): "))
                        n = ship[symbol[i]][1]
                        
                        if (ori == "h" and ((x+n-1)<10)):
                            for j in range(0,n):
                                if(B[y][x+j]=="0"):#Loop to ensure ships do not overlap
                                    chk=chk+1
                            if (chk==n):
                                for j in range (0,n):
                                    B[y][x+j]= symbol[k]
                                k+=1
                                placed = True  
                            else:
                                print("Ship already in those coordnates")
                        elif (ori == "v" and ((y+n-1)<10)):
                            for j in range(0,n):
                                if(B[y+j][x]=="0"):
                                    chk=chk+1
                            if (chk==n):
                                for j in range (0,n):
                                    B[y+j][x]= symbol[k]
                                k+=1
                                placed = True
                            else:
                                print("Ship already in those coordnates")
                        else:
                            print("There is not enough tiles for the input coordinates and orientation!")
                    else:
                        print("Ship already placed there!")
                placed = False
        print("   0     1    2    3    4    5    6    7    8    9")     #Prints board for user 
        rows =0     
        for b in B:
            print(rows,b)
            rows+=1
        conf=input("Are You Happy With the Board Configuration?(Y/N): ")
        if(conf=="Y"):
            confirm = True
            return B
        else:
            confirm = False
            i=0
def comp_set_board():
    B = [ ["0","0","0","0","0","0","0","0","0","0"],#Same as above
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"]]
    k = 0 #Same as above
    placed = False #Same as above
    ori =''#Same as above
    for i in range(0,5): 
            chk=0
            while(not placed):
                x = random.randrange(0,10)#Randomized x coordinate
                y = random.randrange(0,10)#Randomized y coordinate
                if (B[y][x]=="0"):
                    ori = random.randrange(0,2)
                    n = ship[symbol[i]][1]
                    
                    if (ori == 0 and ((x+n-1)<10)):
                        for j in range(0,n):
                                if(B[y][x+j]=="0"):
                                    chk=chk+1
                        if (chk==n):
                            for j in range (0,n):
                                B[y][x+j]= symbol[k]
                            k+=1
                            placed = True     
                    elif (ori == 1 and ((y+n-1)<10)):
                        for j in range(0,n):
                                if(B[y+j][x]=="0"):
                                    chk=chk+1
                        if (chk==n):
                            for j in range (0,n):
                                B[y+j][x]= symbol[k]
                            k+=1
                            placed = True
                    
            placed = False
    return B

def user_attack(x,y):
        hcount = 0
        global end
        global CB
        global hit
        global TB
        if (CB[y][x]=="0"):
            print ("It missed at (",x,",",y,") We'll get em next time.",sep='')
            TB[y][x]= 'x'
            hit = True
        elif(CB[y][x] in symbol):
            print("We hit!")           
            TB[y][x]= 'o' 
            hcount+=1
            if (hcount==17):
                print("***  ***   ********  ***   ***   **      ** ********  *****       ***")
                print(" **  **    **    **  ***   ***   **      **   ***     *** **      ***")
                print("   **      **    **  ***   ***   **      **   ***     ***  **     ***")
                print("   **      **    **  ***   ***   **  **  **   ***     ***    **   ***")
                print("   **      **    **  ***   ***   **  **  **   ***     ***     **  ***")
                print("   **      **    **  *********   **  **  **   ***     ***      ** ***")
                print("   **      ********  *********   ****  **** ********  ***       *****")
                end = True
            else:
                end = False
            hit = True
        else:
            print("You've already attacked there. Attack somewhere else.")
        Ret = [end,TB,hit, hcount]
        return Ret
def comp_attack():
    global end
    global UB
    hit = False
    comphcount=0
    while (not hit):
        x,y=random.randint(0,9),random.randint(0,9)
        if (UB[y][x]!="x" or UB[y][x]!="o"):
            if (UB[y][x]=="0"):
                UB[y][x]='x'
                print("The enemy missed at (",x,",",y,")",sep='')
                hit = True
                end = False
            elif(UB[y][x] in symbol):
                print("Gah the enemy hit us at (",x,",",y,")",sep='')
                UB[y][x]="o"
                comphcount+=1
                if(comphcount==17):
                    print("***  ***   ********  ***   ***   ***       ********  ********  ********")
                    print(" **  **    **    **  ***   ***   ***       **    **  ********  ********")
                    print("   **      **    **  ***   ***   ***       **    **  **        **")
                    print("   **      **    **  ***   ***   ***       **    **  ********  ********")
                    print("   **      **    **  ***   ***   ***       **    **        **  **")
                    print("   **      **    **  *********   ***       **    **  ********  ********")
                    print("   **      ********  *********   ********  ********  ********  ********")
                    end = True
                else:
                    end = False
                hit = True
        ret = [end,UB,hit,comphcount]
        return ret
def main():
    turn =1
    global end
    global hit
    global TB
    global UB  
    global CB
    uhcount = 0
    chcount = 0
    print("*********************************BATTLESHIP*********************************")
    print("1:Start Game")
    print("2:Quit Game")
    ch = input("Click 1 to begin anything else to quit: ")
    if (ch == '1'):
        UB = user_set_board()
        print("If computer is taking too long to set board it is recommended to restart program.")
        CB = comp_set_board()
        print("Game begins now!")
        while(not end):
            print("Turn:",turn)
            hit = False
            print("1:Attack")
            print("2:View Damage Board")
            print("3:View Target Board")
            print("4:View Symbol Key")
            print("5:View Hit Counts")
            print("6:Quit Game")
            c = int(input("Choose an action: "))
            if (c == 1):
                print ("Input Enter Target Coordinates")
                while(not hit):
                    a = int(input("Enter x coordinate(0-9): "))
                    b = int (input("Enter y coordinate(0-9): "))
                    strike = user_attack(a,b)
                    end,TB,hit,uhcount = strike[0],strike[1],strike[2],strike[3]
                    hit = False
                    defe = comp_attack()
                    end,UB,hit,chcount=defe[0],defe[1],defe[2],defe[3]
                    turn+=1
            elif(c == 2):
                print("   0     1    2    3    4    5    6    7    8    9")      
                rows =0     
                for b in UB:
                    print(rows,b)
                    rows+=1
            elif (c==3):
                print("   0     1    2    3    4    5    6    7    8    9")      
                rows = 0     
                for b in TB:
                    print(rows,b)
                    rows+=1
            elif (c==4):
                for i in symbol:
                    print(i,"-",ship[i][0])
                print("x - Miss")
                print("o - Miss")
                print("0 - Untargeted Space")
            elif(c==5):
                print("User Hit Count -",uhcount)
                print("Computer Hit Count -",chcount)
            elif(c==6):
                sys.exit()
    else:
        sys.exit()
        
if (__name__=="__main__"):
    main()