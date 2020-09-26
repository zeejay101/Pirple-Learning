#two empty lists
myuniquelist = []
myleftovers = []
#for loop to ask user 10 values
for j in range(0,10):
    a = input("Enter the number: ")
    #if condition to decide if int move to unique list other wise in leftovers
    if a.isdigit():
        myuniquelist.append(a)
    else:
        myleftovers.append(a)
#at last print both lists
print(myuniquelist)
print(myleftovers)
#end of code