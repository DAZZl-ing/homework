## 1
score = int(input('점수를 입력하세요 : '))

if score >= 90:
   print('점수는 {}이고 A학점입니다.'.format(score))
elif score >= 80:
   print('점수는 {}이고 B학점입니다.'.format(score))
elif score >= 70:
   print('점수는 {}이고 C학점입니다.'.format(score))
elif score >= 60:
   print('점수는 {}이고 D학점입니다.'.format(score))
else:
   print('점수는 {}이고 F학점입니다.'.format(score))

## 2
a = int(input('정수를 입력하세요 : '))
if a % 3 == 0:
   print('{}는 3의 배수입니다.'.format(a))
else:
   print('{}는 3의 배수가 아닙니다.'.format(a))

## 3
A = int(input('정수 1입력 : '))
B = int(input('정수 2입력 : '))
C = int(input('정수 3입력 : '))

if A > B and A > C:
   print('가장 큰 수는 {}입니다.'.format(A))
if B > A and B > C:
   print('가장 큰 수는 {}입니다.'.format(B))
if C > A and C > B:
   print('가장 큰 수는 {}입니다.'.format(C))

## 4
car = str(input('차량번호를 입력하세요 : '))
Z = int(car[-2]) / 2
if Z == 0:
   print('차량번호 {}는 오늘 운행가능입니다.'.format(car))
else:
   print('차량번호 {}는 오늘 운행불가능입니다.'.format(car))