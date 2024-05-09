import random, os, time


def rollDice(side):
  result = random.randint(1, side)
  return result


def health():
  healthStat = ((rollDice(20) * rollDice(10)) // 2) + 10
  return healthStat


def strenght():
  strengthStat = ((rollDice(20) * rollDice(10)) // 2) + 10
  return strengthStat


c1name = str(input("First Character name:\n"))
c1race = str(input("Character race (Human, Elf, Dwarf, Orc):\n"))
print()
print("Name:", c1name)
print("Race:", c1race)
c1health = health()
c1strenght = strenght()
print("Health:", health())
print("Strenght:", strenght())
print()

c2name = str(input("Second Character name:\n"))
c2race = str(input("Character race (Human, Elf, Dwarf, Orc):\n"))
print()
print("Name:", c2name)
print("Race:", c2race)
c2health = health()
c2strenght = strenght()
print("Health:", health())
print("Strenght:", strenght())
print()

round = 1
winner = None

while round:
  time.sleep(5)
  os.system("clear")
  print("⚔️ Battle Start ⚔️")
  print()
  print("The figh begin!")

  c1dice = rollDice(20)
  c2dice = rollDice(20)

  difference = abs(c1strenght - c2strenght) + 1

  if c1dice > c2dice:
    c2health -= difference
    if round == 1:
      print(c1name, "wins the first fight")
    else:
      print(c1name, "wins round", round)
  elif c2dice > c1dice:
    c1health -= difference
    if round == 1:
      print(c2name, "wins the first fight")
    else:
      print(c2name, "wins round", round)
  else:
    print("Their swords clash and they fight again", round)

  print()
  print(c1name)
  print("Health:", c1health)
  print()
  print(c2name)
  print("Health:", c2health)
  print()

  if c1health <= 0:
    print(c1name, "has died!")
    winner = c2name
    break
  elif c2health <= 0:
    print(c2name, "has died!")
    winner = c1name
    break
  else:
    print("Next round:")
    round += 1

time.sleep(5)
os.system("clear")
print("⚔️ Battle End ⚔️")
print()
print(winner, "has won in", round, "round")