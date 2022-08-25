digits = input()

one, two = digits.split(" ")
one = int(one[::-1])
two = int(two[::-1])

if two > one:
    print(two)
else:
    print(one)