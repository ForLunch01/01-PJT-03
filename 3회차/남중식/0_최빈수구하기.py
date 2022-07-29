import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(T):
      case_num = int(input())
      num_list = list(map(int, input().split()))
      
      num_dict = dict()
      
      for n in num_list:
            if n in num_dict:
                  num_dict[n] += 1
            else:
                  num_dict[n] = 1
      
      max_value = max(num_dict.values())
      max_list = []
      
      for k, v in num_dict.items():
            if v == max_value:
                  max_list.append(k)
      
      max_list.sort()
      print(f"#{i+1} {max_list[-1]}")