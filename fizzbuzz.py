# Fizzbuzz counts up to entered number and prints "fizz" if a number can be divided by 3, "buzz" if a number can be divided by 5 and "fizzbuzz" if a number can be divided by both 3 and 5.

enter = int(raw_input("Select a number between 1 and 100: "))+1

for var in range(1,enter):

    if var % 15 ==0:
        print "fizzbuzz"
    elif var % 5 == 0:
        print "buzz"
    elif var % 3 == 0:
            print "fizz"
    else:
        print(var)
