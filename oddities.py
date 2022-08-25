odds = []

odd = int(input())

for x in range(odd):
    odds.append(int(input()))

for x in odds:
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")