def drawField(field):
	for row in range(5):#01234
		if row%2 == 0:
			practicalrow = int(row/2)
			for column in range(5):
				if column%2 == 0:
					practicalcolumn=int(column/2)
					if column != 4:
						print(field[practicalcolumn][practicalrow],end="")
					else:
						print(field[practicalcolumn][practicalrow])
				else:
					print("|",end="")
		else:
			print("-----")
Player = 1
currentField = [[" "," "," "],[" ","  "," "],[" "," "," "]]			
drawField(currentField)
while(True):
	print("Player Turn: ",Player)
	MoveRow = int(input("Please enter row\n"))
	MoveColumn = int(input("please enter the column\n"))
	if Player==1:
		if currentField[MoveColumn][MoveRow] = " ":
				currentField[MoveColumn][MoveRow] = "X"
				Player=2
	else:
		if currentField[MoveColumn][MoveRow] = " ":
				currentField[MoveColumn][MoveRow] = "O"
				Player=1
	drawField(currentField)