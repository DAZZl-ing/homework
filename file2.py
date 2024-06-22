n1 = float(input('첫 번째 실수를 입력하세요 : '))
n2 = float(input('두 번째 실수를 입력하세요 : '))
print('{}와 {}의 합은 {}입니다.'.format(n1, n2, n1 + n2))

li = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
cal = int(input('1~12 사이의 월을 입력하세요 : '))
print(li[cal-1])

english_dict = {
   'flower' : '꽃',
   'fly' : '날다',
   'floor' : '바닥'
}
word = str(input('영어 단어를 입력하세요 :'))
print(english_dict[word])


A = str(input('희망하는 수학여행지를 입력하세요 :'))
B = str(input('희망하는 수학여행지를 입력하세요 :'))
C = str(input('희망하는 수학여행지를 입력하세요 :'))
adr = set({A, B, C})
print('조사된 수학여행지는 {}입니다.'.format(adr))


##페이지 85~86

## 1
N1 = int(input('10 ~ 99사이의 정수를 입력하세요 : '))
print('십의 자리는 : {}'.format(N1 // 10))
print('일의 자리는 : {}'.format(N1 % 10))

## 2
sec = int(input('초를 입력하세요 : '))
a = sec//3600
b = (sec-a*3600)//60
c = sec - (a*3600) - (b*60)
print('변환 결과는 {}시간 {}분 {}초입니다.'.format(a, b, c))

## 3
number = int(input('4자리 사원번호를 입력하세요 : '))
A = number % 10
time = ('오전') if (A >= 5) else ('오후')
print('근무시간은 {}입니다.'.format(time))

## 4
print('한박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
ramen = int(input('라면의 개수를 입력하세요 : '))
result = ramen // 20
box = (result + 1) if (ramen % 20 >= 1) else (ramen // 20)
print('{}개의 라면을 담으려변 {}박스가 필요합니다.'.format(ramen, box))

## 5
korean = int(input('국어 점수를 입력하세요 :'))
english = int(input('영어 점수를 입력하세요 : '))
math = int(input('수학 점수를 입력하세요 : '))
avg = (korean + english + math) / 3
result = ('합격') if (avg >= 80) else ('불합격')
print('평균은 {}점이고, 결과는 {}입니다.'.format(avg, result))
