import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for i in range(T):
    card_num = input()
    
    card_num_no_hypen = card_num.replace("-", "")
    
    if len(card_num_no_hypen) != 16:
        print(f'#{i+1} 0')
        continue
    
    if card_num_no_hypen[0] not in ['3', '4' , '5', '6', '9']:
        print(f'#{i+1} 0')
        continue
    
    print(f'#{i+1} 1')