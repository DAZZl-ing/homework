## 1
for n in range(5, 0, -1):
   print(n)

## 2
plus = int(input('임의의 양수를 입력하세요 : '))
n = 0
sum = 1
for n in range(plus+1):
   sum += plus
   plus += 1
   print(sum)