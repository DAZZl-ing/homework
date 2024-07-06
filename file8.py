## 1

class Book():
   def set_info(self, title, author):
      self.title = title
      self.author = author

   def print_info(self):
      print(f'책 제목: {self.title}')
      print(f'책 저자: {self.author}')

book1 = Book()
book1.set_info('파이썬', '민경태')
book1.print_info()

book2 = Book()
book2.set_info('어린왕자', '생텍쥐페리')
book2.print_info()

book_list = [book1, book2]

## 2

class Watch():
   def set_time(self, time):
      self.hour = int(time[0:2])
      self.minute = int(time[3:5])
      self.second = int(time[6:8])

   def add_hour(self, hour):
      self.hour += hour

   def add_minute(self, minute):
      self.minute += minute


      hour = self.minute // 60
      self.hour += hour

      self.minute = self.minute % 60

   def add_second(self, second):
      self.second += second


      minute = self.second // 60
      self.minute += minute

      self.second = self.second % 60

   def print_calc_time(self):
      print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초')

watch = Watch()

time = input('시간을 입력하세요 : ')
watch.set_time(time)

hour = int(input('계산할 시간을 입력하세요 : '))
minute = int(input('계산할 분을 입력하세요 : '))
second = int(input('계산할 초를 입력하세요 : '))

watch.add_second(second)
watch.add_minute(minute)
watch.add_hour(hour)

watch.print_calc_time()

## 3

class Song():
   def set_song(self, name: str, genre: str):
      self.name: str = name
      self.genre:str = genre

   def print_song(self):
      print(f'노래 제목: {self.name}({self.genre})')


class Singer():
   def set_singer(self, singer: str):
      self.singer = singer
   
   def hit_song(self, song: Song):
      self.hit_song : Song = song

   def print_singer(self):
      print(f'가수 이름: {self.singer}')
      print(f'노래 제목: {self.hit_song.name}({self.hit_song.genre})')


song = Song()
song.set_song('취중진담', '발라드')

singer = Singer()
singer.set_singer('김동률')

singer.hit_song(song)

singer.print_singer()