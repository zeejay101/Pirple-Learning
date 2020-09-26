#function taking 3 parameters and checking value quality with if statements
def func(a,b,c):
#statements checking any 2 equalities of given values
    if a == 1 and b == 2:
        print(True)
    elif a == 1 and c == 3:
        print(True)
    elif b == 2 and c == 3:
        print(True)
    else:
        print(False)
#calling function with any 3 values 
func(1,3,3)