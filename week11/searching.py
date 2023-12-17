integers = []
#finding the biggest num in list
for i in range(1,11):
    integers.append(int(input("Input a number:\n")))
if integers[0]>integers[1]:
    biggest = integers[0]
elif integers[1]>integers[0]:
    biggest = integers[1]
else:
    biggest = integers[0]
for i in range(2,10):
    if integers[i]>biggest:
        biggest = integers[i]
    else:
        pass

#finding the smallest
if integers[0]<integers[1]:
    smallest = integers[0]
elif integers[1]<integers[0]:
    smallest = integers[1]
else:
    smallest = integers[0]
for i in range(2,10):
    if integers[i]<smallest:
        smallest = integers[i]
    else:
        pass

#finding sum and average
sum = 0
for i in range(0,10):
    sum = sum+integers[i]
average = sum/10
print(f"{smallest} is the smallest number in the list")
print(f"{biggest} is the biggest number in the list")
print(f"The sum is {sum}, and the average is {average}")

