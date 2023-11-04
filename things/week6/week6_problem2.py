while True:
    try:
        num = int(input("Enter a number: "))
        a=True
        factorial = 1
        if num >= 1:
            for i in range(1, num+1):
                factorial=factorial*i
            print(factorial)
        else:
            print("invalid number")
    except:
        print("something went wrong, try again")