def sum(a,b,c):
    return (a+b+c)

def printBoard(XState,ZState):
    zero='x' if XState[0] else('0' if ZState[0] else 0)
    one='x' if XState[1] else('0' if ZState[1] else 1)
    two='x' if XState[2] else('0' if ZState[2] else 2)
    three='x' if XState[3] else('0' if ZState[3] else 3)
    four='x' if XState[4] else('0' if ZState[4] else 4)
    five='x' if XState[5] else('0' if ZState[5] else 5)
    six='x' if XState[6] else('0' if ZState[6] else 6)
    seven='x' if XState[7] else('0' if ZState[7] else 7)
    eight='x' if XState[8] else('0' if ZState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    
    

def checkwin(XState,ZState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(XState[win[0]], XState[win[1]],XState[win[2]])== 3):
            print("X won the match")
            return 1
        if(sum(ZState[win[0]], ZState[win[1]],ZState[win[2]]) == 3):
            print("0 won the match")
            return 0
    return -1
if __name__== "__main__":
    XState=[0,0,0,0,0,0,0,0,0]
    ZState=[0,0,0,0,0,0,0,0,0]
    turn =1
    print("Welcome to Tic Tak Toe")
    while(True):
        printBoard(XState,ZState)
        if(turn == 1):
           print("X's chance")
           value = int(input("please enter a  value"))
           XState[value] = 1
        else:
            print("X's chance")
            value = int(input("please enter a  value"))
            ZState[value] =1
        cwin =checkwin(XState, ZState)  
        if(cwin!=-1):
            print("Match over")
            break
        turn = 1-turn    
               
        
    
