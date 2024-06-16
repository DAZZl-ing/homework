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