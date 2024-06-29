## 1
money = 10000

while money > 0:
   pay = int(input('사용할 금액을 입력하세요. : '))

   if pay < 0:
      print('0 이하의 금액은 사용할 수 없습니다.')
      continue

   A = (money - pay)
   B = (pay - money)

   if A < 0:
      print(f'{B}원이 부족합니다.')
   else:
      money -= pay
      print(f'현재 {money}원이 있습니다.')

## 2

while True:
   movie = int(input('이번 영화의 평점을 입력하세요. : '))

   if movie < 1 or movie > 5:
      print('평점은 1~5 사이만 입력할 수 있습니다.')
      continue
   
   else:
      print('평점: ','★ '*movie )
      break

## 3
password = ['qwerty']
count = 5

while count > 0:
   program = input('비밀번호를 입력하세요 : ')
   if program in password:
      print('비밀번호를 맞췄습니다.')
      break

   else:
      count -= 1

if count == 0:
   print('비밀번호 입력 횟수를 초과했습니다.')

## 4
dan = 1
n = 1

for dan in range(2,10):
   if dan % 2 == 0:
      print('')
      continue
   for n in range(1, 10):
      if n <= dan:
         print('{}x{}={}'.format(dan, n, dan*n))