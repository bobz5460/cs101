while True:
    try:
        number1 = int(input("enter number: "))
        number2 = int(input("enter another number: "))
        triangle = eval(f"{number1} * {number2}/ 2")
        square = eval(f'{number1}*{number1}')
        r2 = eval(f'{number2}*{number2}')
        circle = eval(f'3.14*{r2}')
        print(f'area of triangle when base is number1 and height is number2 is {triangle}\n'
              f'area of square when number1 is the side length is {square}\n'
              f'area of circle when radius equals number2 is {circle}')
    except ValueError:
        print("you typed something wrong, prob typed a string into the integer thing")
    except SyntaxError:
        print('i didnt even think this was possible but you somehow made a syntax error in my code ¯\_(ツ)_/¯ easter egg i guess unless youre looking at the code hmmm in that case hi')
