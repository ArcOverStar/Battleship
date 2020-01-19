import random, sys
UB=[]
CB=[]

ship = {'C':["Carrier",5],'B':["Battleship",4],'S':["Submarine",3],'c':["Cruiser",3],'D':["Destroyer",2]}
symbol = list(ship.keys())

def user_set_board():
    B = [["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"]]
    
    k = 0 #Helps in the initialization of user's pieces
    placed = False    
    confirm = False
    ori =''
    conf = ''
    while (not confirm):
        for i in range(0,5):   
                print("Input ",ship[symbol[i]][0],"\'s coordinates",sep='')
                while(not placed):
                    x = int(input("Enter x coordinate(0-9): "))
                    y = int (input("Enter y coordinate(0-9): "))
                    if (B[y][x]=="0"):
                        ori = str(input("Enter orientation of ship(h/v): "))
                        n = ship[symbol[i]][1]
                        
                        if (ori == "h" and ((x+n-1)<10)):
                            for j in range (0,n):
                                B[y][x+j]= symbol[k]
                            k+=1
                            placed = True     
                        elif (ori == "v" and ((y+n-1)<10)):
                            for j in range (0,n):
                                B[y+j][x]= symbol[k]
                            k+=1
                            placed = True
                        else:
                            print("There is not enough tiles for the input coordinates and orientation!")
                    else:
                        print("Ship already placed there!")
                placed = False
        print("   0     1    2    3    4    5    6    7    8    9")      
        rows =0     
        for b in B:
            print(rows,b)
            rows+=1
        conf=input("Are You Happy With the Board Configuration?(Y/N)")
        if(conf=="Y"):
            confirm = True
            return B
        else:
            confirm = False
            i=0
def comp_set_board():
    B = [ ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0","0","0","0"]]
    k = 0 #Helps in the initialization of user's pieces
    placed = False    
    ori =''
    for i in range(0,5):   
            while(not placed):
                x = random.randint(0,9)
                y = random.randint(0,9)
                if (B[y][x]=="0"):
                    ori = random.randint(0,1)
                    n = ship[symbol[i]][1]
                    
                    if (ori == 0 and ((x+n-1)<10)):
                        for j in range (0,n):
                            B[y][x+j]= symbol[k]
                        k+=1
                        placed = True     
                    elif (ori == 1 and ((y+n-1)<10)):
                        for j in range (0,n):
                            B[y+j][x]= symbol[k]
                        k+=1
                        placed = True
                    
            placed = False
    return B

def user_attack(x,y):
        hcount = 0
        
        if (CB[y][x]==0):
            print ("It missesd!We'll get em next time.")
            TB[y][x]=='x'
            hit = True
            return TB
        elif(CB[y][x] in symbol):
            print("We hit!")
            TB[y][x]="o"
            hit = True
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
            print("You've already attacked there. Attack somewhere else.")
        Ret = [end,TB,hit]
        return Ret
def comp_attack():
    hit = False
    compxcount=0
    while (not hit):
        x,y=random.randint(0,9),random.randint(0,9)
        if (UB[y][x]==0):
            UB[y][x]=='x'
            print("The enemy missed!")
            hit = True
        elif(UB[y][x] in symbol):
            print("Gah the enemy hit us!")
            UB[y][x]="o"
            if(compxcount==17):
                print("***  ***   ********  ***   ***   ***         ********  ********   ********")
                print(" **  **    **    **  ***   ***   ***         **    **  ********   ********")
                print("  ***      **    **  ***   ***   ***         **    **  **         **")
                print("  ***      **    **  ***   ***   ***         **    **  ********   ********")
                print("  ***      **    **  ***   ***   ***         **    **        **   **")
                print("  ***      **    **  ***   ***   ***         **    **  ********   ********")
                print("  ***      ********  *********   ********    ********  ********   ********")
                end = True
        ret = [end,UB]
        return ret
def main():
    end = False
    hit = False
    TB = [["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"],
      ["0","0","0","0","0","0","0","0","0","0"]]
    print("*************************BATTLESHIP*********************************")
    print("1:Start Game")
    print("2:Quit Game")
    ch = input("Click 1 to begin anything else to quit")
    if (ch == '1'):
        UB = user_set_board()
        CB = comp_set_board()
        while(not end):
            print("1:Attack")
            print("2:View Damage Board")
            print("3:View Target Board")
            print("4:View Symbol Key")
            print("5:Quit Game")
            c = int(input("Choose an action: "))
            if (c == 1):
                print ("Input Enter Target Coordinates")
                while(not hit):
                    a = int(input("Enter x coordinate(0-9): "))
                    b = int (input("Enter y coordinate(0-9): "))
                    strike = user_attack(a,b)
                    end = strike[0]
                    hit=strike[2]
                    TB = strike[1]
                    defe = comp_attack()
                    end=defe[0]
                    UB=defe[1]
            elif(c == 2):
                print("   0     1    2    3    4    5    6    7    8    9")      
                rows =0     
                for b in UB:
                    print(rows,b)
                    rows+=1
            elif (c==3):
                print("   0     1    2    3    4    5    6    7    8    9")      
                rows =0     
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
                sys.exit()
    else:
        sys.exit()
        
if (__name__=="__main__"):
    main()