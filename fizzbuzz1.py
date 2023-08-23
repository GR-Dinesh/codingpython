for n in range(1, 50):
    #print(n)
    if (n % 3 == 0 and n % 5 == 0):
        print("The number is FizzBuzz")
    elif (n % 3 == 0):
        print("The number is Fizz")
    elif (n % 5 == 0):
        print("The number is Buzz")
    else:
        print(f"The number is: {n}")