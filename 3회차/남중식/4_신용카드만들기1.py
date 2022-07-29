import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for j in range(T):
    num_list = list(map(int, input().split()))
    sum = 0
    for i, n in enumerate(num_list):
        # 홀수면
        if i % 2 == 0:
            sum = sum + (n*2)
        
        # 짝수면
        if i % 2 == 1:
            sum = sum + n
        
    N = (10 - (sum%10)) % 10
    print(f'#{j+1} {N}')