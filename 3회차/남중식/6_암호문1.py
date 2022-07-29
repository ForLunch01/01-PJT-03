import sys

sys.stdin = open("_암호문1.txt")

for i in range(10):
    N = int(input())
    
    origin_pw = list(map(int, input().split()))

    M = int(input())
    
    inst_list = input().split()
    
    for idx, inst in enumerate(inst_list):
        if inst == 'I':
            start = int(inst_list[idx+1])
            inst_len = int(inst_list[idx+2])
            inst_nums = list(map(int, inst_list[idx+3:idx+3+inst_len]))

            for j in range(inst_len):
                origin_pw.insert(start, inst_nums[-j-1])
    
    print(f'#{i+1}',*origin_pw[0:10])