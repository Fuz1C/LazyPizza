print("Hi, I'm the Lazy Pizza app, I exist because you are too lazy to do simple dividing. Here we go.")
print("How many slices of pizza do you have?")
slices = int(input())
print("How many people are sharing this pizza?")
people = int(input())
sliceperson = slices // people
remains = slices % people
print (f"Each person gets {sliceperson}!")

if remains <= 1:
  print (f"There is {remains} slice remaining... FIGHT FOR THE DEATH FOR IT GOOOOO, THIS IS MY ONLY ENTERTAINMENT!!!!")
if remains == 0:
  print(f"oh... there are no spare slices...")
if people == 1:
  print(f"Wow... eating pizza by yourself?")
else:
  print(f"There are {remains} slices remaining... FIGHT FOR THE DEATH, I'LL GRANT YOU WEAPONS. GOOOOOOOOOOOOO, THIS IS MY ONLY ENTERTAINMENT!!!!!")
