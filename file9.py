## 1

class People:
   population = 0

   def __init__(self, name):
      self.name = name
      People.population += 1

   @staticmethod

   def get_population():
      return People.population
   
   def __str__(self):
      return self.name
   
   def __del__(self):
      People.population -= 1
      print('{} is dead'.format(self.name))

man = People('james')
woman = People('emily')

print('{} is born'.format(man))
print('{} is born'.format(woman))

print('전체 인구수 {}명'.format(People.get_population()))

del man

print('전체 인구수 {}명'.format(People.get_population()))


##
del woman
print('\n')
##


## 2

class Shop:
   total = 0
   menu_list = [{'떡볶이' : 3000}, {'순대' : 3000}, {'튀김' : 500}, {'김밥' : 2000}]

   @classmethod
   def sales(cls, menu, sell):
      for item in cls.menu_list:
         if menu in item:
            price = item[menu]
            sales_price = price*sell
            cls.total += sales_price

Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

print('매출 : {}원'.format(Shop.total))


##
print('\n')
##


## 3
class Car:

   max_oil = 50

   def __init__(self, oil):
      self.oil = oil

   def add_oil(self, oil):
      if oil <= 0:
         return
      self.oil += oil
      if self.oil > Car.max_oil:
         self.oil = Car.max_oil

   def car_info(self):
      print('현재 주유상태 : {}'.format(self.oil))

class Hybrid(Car):

   max_battery = 30

   def __init__(self, oil, battery):
      super().__init__(oil)
      self.battery = battery

   def hybrid_info(self):
      super().car_info()
      print('현재 충전상태 : {}'.format(self.battery))

   def charge (self, battery):
      if battery <= 0:
         return
      self.battery += battery
      if self.battery > Hybrid.max_battery:
         self.battery = Hybrid.max_battery

car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()