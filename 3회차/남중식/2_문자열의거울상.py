import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for i in range(T):
    data = input()
    mirror_data = []
    for d in data:
        if d == 'd':
            mirror_data.append('b')
        if d == 'b':
            mirror_data.append('d')
        if d == 'p':
            mirror_data.append('q')
        if d == 'q':
            mirror_data.append('p')
    
    print(f'#{i+1}', end=" ")
    print("".join(mirror_data[::-1]))