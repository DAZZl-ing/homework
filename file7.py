## 1

def vending_machine(money):
   drink = 0
   while money > 0:
      print('음료수 = {}개, 잔돈 = {}원'.format(drink, money))
      drink += 1
      money -= 700

vending_machine(3000)


## 2
def get_average(marks):
   sum = dict.values()
   n = len(marks)
   return sum / n

marks = {'국어': 90,'영어': 80,'수학': 85}
average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))