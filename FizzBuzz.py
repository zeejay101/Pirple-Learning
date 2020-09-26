#for loop to get numbers from 1 to 100
for fizzbuzz in range(100):
    #have to add 1 in order to get exact from 1 too instead of 0 to 99
    fizzbuzz += 1
    #if number is divisible of both 3 and 5
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
        #if number is divisible of 3
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
        #if divisible of 5 then 
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)