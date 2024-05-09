class Building: #inheritance
  __year = None
  __city = None #encapsulation

  def __init__(self, year, city):
    self.year = year
    self.city = city

  def get_info(self):
    print('Year:', self.year, 'City:', self.city)


class School(Building): #polymorphism
  students = 0

  def __init__(self, students, year, city):
    super(School, self). __init__(year, city)
    self.students = students

  def get_info(self):
    print('School:')
    super().get_info()
    print('Studdents', self.students)


class House(Building):
  residents = 0

  def __init__(self, residents, year, city):
    super(House, self). __init__(year, city)
    self.residents = residents

  def get_info(self):
    print('House:')
    super().get_info()
    print('Residents', self.residents)


class Shop(Building):
  buyers = 0

  def __init__(self, buyers, year, city):
    super(Shop, self). __init__(year, city)
    self.buyers = buyers
    
  def get_info(self):
    print('Shop:')
    super().get_info()
    print('Buyers', self.buyers)
    


school = School(350, 2012, 'Moscow')
school.get_info()
house = House(250, 2002, 'St. Petersburg')
house.get_info()
shop = Shop(500, 2011, 'Tula')
shop.get_info()