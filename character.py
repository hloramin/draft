import random, os, time


def rollDice(side):
  result = random.randint(1, side)
  return result


def health():
  healthStat = ((rollDice(20) * rollDice(10)) // 2) + 10
  return healthStat


def dexterity():
  dexStat = ((rollDice(20) * rollDice(10)) // 2) + 10
  return dexStat


def strenght():
  strengthStat = ((rollDice(20) * rollDice(10)) // 2) + 10
  return strengthStat


def intellect():
  intellhStat = ((rollDice(20) * rollDice(10)) // 2) + 10
  return intellhStat


while rollDice:

  print("Создание персонажа:")
  print()
  
  name = str(input("Имя персонажа:\n"))
  race = str(input("Раса персонажа (Человек, Эльф, Дварф, Орк):\n"))

  print()
  print("Имя:", name)
  print("Раса:", race)
  print("Здоровье:", health())
  print("Сила:", strenght())
  print("Ловкость:", dexterity())
  print("Интелект:", intellect())
  print()
  
  again = str(input("Сгенерировать снова?(да/нет):\n"))

  if again == "нет":
    break
  elif again == "да":
    continue
  else:
    print("Введите правильную команду (да/нет.")
    time.sleep(2)
    os.system("clear")
