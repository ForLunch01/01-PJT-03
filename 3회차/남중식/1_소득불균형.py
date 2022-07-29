import sys

sys.stdin = open("_소득불균형.txt")

T = int(input().strip())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    
    num_avr = sum(num_list)/N
    
    count = 0
    
    for n in num_list:
        if n <= num_avr:
            count += 1
    
    print(f'#{i+1} {count}')