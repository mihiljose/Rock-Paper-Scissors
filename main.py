rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

comp_choice = random.randint(0,2)

print("You choose:")
if human_choice == 0:
  print(rock)
elif(human_choice == 1):
  print(paper)
else:
  print(scissors)

print("Computer choose:\n")
if comp_choice == 0:
  print(rock)
elif(comp_choice == 1):
  print(paper)
else:
  print(scissors)

if (human_choice == 0):
  if(comp_choice==0):
    print("Its a Draw")
  elif(comp_choice==1):
    print("You Lost!")
  else:
    print("You Won!")

elif (human_choice == 1):
  if(comp_choice==0):
    print("You Won!")
  elif(comp_choice==1):
    print("Its a Draw")
  else:
    print("You Lost!")

else:
  if(comp_choice==0):
    print("You Lost!")
  elif(comp_choice==1):
    print("You Won!")
  else:
    print("Its a Draw")
    