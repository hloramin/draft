import os, time

while True:
  print("High Score Table")
  print()
  name = input("Name > ").upper()
  score = input("Score > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("Added")
  time.sleep(1)
  os.system("clear")
  
f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)