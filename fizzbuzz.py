kattis = input()
x,y,n = kattis.split(" ")

for z in range(1, int(n)+1):
    if z % int(x) == 0 and z % int(y) == 0:
        print("FizzBuzz")
    elif z % int(x) == 0:
        print("Fizz")
    elif z % int(y) == 0:
        print("Buzz")
    else:
        print(z)