number = int(input("Enter a number between 1 and 30: "))
if number >= 1 and number <= 30:
    for i in range(1, 13):
        print(f'{number}x{i} = {i*number}')
else:
    print("the number has to be from 1 to 30")