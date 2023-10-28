a = 1
b = []
print("press ctrl+c to finish entering grades, or stop the program")
try:
    while True:
        c = int(input("Enter a grade: "))
        b.append(c)
        print(f"Current list: {b}")
except KeyboardInterrupt:
    print("\nDone.")
except ValueError:
    print("ValueError: you are stupid, i dont feel like making another thing just so that you can continue entering grades, so too bad, heres the current list: ")
d = []
for i in range(len(b)):
    c = b[i]
    match b[i]:
        case _ if c>=91:
            print("A")
            d.append("A")
        case _ if c>=81 and c<=90:
            print("B")
            d.append("B")
        case _ if c>=71 and c<=80:
            print("C")
            d.append("C")
        case _ if c>=61 and c<=70:
            print("D")
            d.append("D")
        case _ if c<=60:
            print("F")
            d.append("F")
print(f'copy pasta version: {d}')
print("this is probably the worst implementation of match and cases, but idk how to use them so it still works just not efficient")