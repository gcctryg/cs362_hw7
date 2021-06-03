def fizzbuzz(a):
    thislist = []
    for i in range (1, 101):
        if ( i % 3 == 0 and i % 5 == 0):
            thislist.append("FizzBuzz")
        elif ( i % 3 == 0 ):
            thislist.append("Fizz")
        elif ( i % 5 == 0 ):
            thislist.append("Buzz")
        else:
            thislist.append(i)
        print(thislist[i-1])

    return thislist[a-1]
