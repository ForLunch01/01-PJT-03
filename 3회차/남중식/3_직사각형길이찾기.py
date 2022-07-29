import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for i in range(T):
    s_list = list(map(int, input().split()))
    
    s_dict = dict()
    
    for s in s_list:
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1
            
    for k, v in s_dict.items():
        if v == 1 or v == 3:
            print(f'#{i+1} {k}')