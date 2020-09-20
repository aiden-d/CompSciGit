line1 = [0,0,0]
line2 = [0,0,0]
line3 = [0,0,0]
lines = [line1, line2, line3]
won = false
victor = ''
def playGame (user) :
    rowNum = int(input("which row do u choose?"))
    columnNum = int(input("which column do u choose?"))
    
    if lines[rowNum][columnNum] ==0:
        lines[rowNum][columnNum] = user
    
    elif line1 == ['x','x','x']:
        won=True
        victor = 'x'
    elif line1 == ['o','o','o']:
        won  = true
        victor = 'o'
    elif line2 == ['x','x','x']:
        won  = true
        victor = 'x'
    elif line2 == ['o','o','o']:
        won  = true
        victor = 'o'
    elif line3 == ['x','x','x']:
        won  = true
        victor = 'x'
    elif line3 == ['o','o','o']:
        won  = true
        victor = 'o'
    elif line1[0] == 'x' and line2[0] == 'x' and line3[0] == 'x':
        won  = true
        victor = 'x'
    
    elif line1[0] == 'x' and line2[1] == 'x' and line3[2] == 'x':
        won  = true
        victor = 'x'
    elif line1[0] == 'o' and line2[1] == 'o' and line3[2] == 'o':
        won  = true
        victor = 'o'
    elif line3[0] == 'x' and line2[1] == 'x' and line1[2] == 'x':
        won  = true
        victor = 'x'
    elif line3[0] == 'o' and line2[1] == 'o' and line1[2] == 'o':
        won  = true
        victor = 'o'
    
    


while won == false:
    print 
