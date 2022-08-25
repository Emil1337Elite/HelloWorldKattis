chess_pieces = [1, 1, 2, 2, 2, 8]

input = input().split(" ")
out = []

for x in range(6):
    out.append(str(chess_pieces[x]-int(input[x])))


print(' '.join(out))