## 111p ~ 113p

## 1
n1 = int(input('정수를 입력하세요 : '))
count = 1
if n1 >= 0:      
   while count <= n1:
      print('{}번째 Hello'.format(count))
      count += 1
else:
   print('잘못된 입력입니다.')

## 2
count = 1
while count*7 <= 100:
   print(count*7)
   count += 1

## 3
money = int(input('자판기에 얼마를 넣을까요? : '))
coffee = 0
while money >= 300:
   coffee += 1
   money -= 300
   print('커피 {}잔, 잔돈 {}원'.format(coffee, money))

## 4
num = set({})
while len(num) < 5:
   A = int(input('0 ~ 9 사이 정수를 입력하세요. : '))
   num.add(A)
print('모두 입력되었습니다.')
print('입력된 값은{}입니다.'.format(num))

## 5
n = 1
while n <= 100:
   print('{} {} {} {} {} {} {} {} {} {}'.format(n, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10))
   n += 10

'''
강사님 코드 5번
count = 1

while count <= 100:
   line = ''
   count2 = 1

   while count2 <= 10:
      line += f'{str(count)}	'
      count += 1
      count2 += 1
   
   print(line)
'''

## 6
N = 1
while N <= 9:
   dan = 2
   while dan <= 9:
      print('{}x{}={}  '.format(dan, N, dan*N), end='')
      dan += 1
   print('\n')
   N += 1
