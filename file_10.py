## 랜덤 자판기
import random

choice_1000 = ['젤리(50%)', '젤리(50%)', '젤리(50%)', '젤리(50%)', '젤리(50%)', '올리브영 3000원 상품권(30%)', '올리브영 3000원 상품권(30%)', '올리브영 3000원 상품권(30%)', 
               '스타벅스 아메리카노 교환권(20%)', '스타벅스 아메리카노 교환권(20%)']
choice_2000 = ['젤리(30%)', '젤리(30%)', '젤리(30%)', '올리브영 3000원 상품권(40%)', '올리브영 3000원 상품권(40%)', '올리브영 3000원 상품권(40%)', '올리브영 3000원 상품권(40%)', 
               '스타벅스 아메리카노 교환권(30%)', '스타벅스 아메리카노 교환권(30%)', '스타벅스 아메리카노 교환권(30%)']
choice_3000 = ['젤리(20%)', '젤리(20%)', '올리브영 3000원 상품권(30%)', '올리브영 3000원 상품권(30%)', '올리브영 3000원 상품권(30%)', '스타벅스 아메리카노 교환권(50%)', 
               '스타벅스 아메리카노 교환권(50%)', '스타벅스 아메리카노 교환권(50%)', '스타벅스 아메리카노 교환권(50%)', '스타벅스 아메리카노 교환권(50%)']

class Making:
   def __init__(self, money):
      self.mode = 'guest'
      self.money = money
      self.profit = 0
      self.my_list = [] ##현재 구매한 상품 목록
   
   def vending_machine(self): ## 관리자모드
      money = self.money
      profit = self.profit

      while money > 0:
         if self.mode == 'guest':
            key = input('손님 : 명령을 입력하세요(a:관리자모드, 1:1000원 상품 구매, 2:2000원 상품 구매, 3:3000원 상품 구매, b:현재 잔액 조회, l:현재 구매한 상품 목록 조회) : ')
         elif self.mode == 'admin':
            key = input('관리자 : 명령을 입력하세요 (g:손님모드, p:매출조회) : ')
         
         if key == 'a':
            pw = input('비밀번호를 입력하세요. : ')
            
            if pw == 'admin':
               self.mode = 'admin'
               continue
            else:
               print('비밀번호가 올바르지 않습니다.')
               continue
         elif key == 'p':
            print('오늘의총 매출은 {}입니다.'.format(profit))
         elif key == 'g':
            self.mode = 'guest'
            continue
         elif key == '1':
            if money < 1000:
               print('잔액이 부족합니다. 잔액{}, 상품금액 1000원'.format(money))
               continue
            small = random.choice(choice_1000)
            money -= 1000
            profit += 1000
            self.my_list.append(small)
            print('{}에 당첨되셨습니다.'.format(small))
         elif key == '2':
            if money < 2000:
               print('잔액이 부족합니다. 잔액{}, 상품금액 2000원'.format(money))
               continue
            middle = random.choice(choice_2000)
            money -= 2000
            profit += 2000
            self.my_list.append(middle)
            print('{}에 당첨되셨습니다.'.format(middle))
         elif key == '3':
            if money < 3000:
               print('잔액이 부족합니다. 잔액{}, 상품금액 3000원'.format(money))
               continue
            large = random.choice(choice_3000)
            money -= 3000
            profit += 3000
            self.my_list.append(large)
            print('{}에 당첨되셨습니다.'.format(large))
         elif key == 'b':
            print('현재 잔액은 {}입니다.'.format(money))
         elif key == 'l':
            print('현재 구매하신 품목은 {} 입니다.'.format(self.my_list))

      print('소지금을 모두 소진하여 구매가 불가능하니 프로그램을 종료합니다.')

making = Making(10000)
making.vending_machine()
