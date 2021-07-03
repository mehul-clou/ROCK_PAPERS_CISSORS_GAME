import random

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
# print(rock)
# print(paper)
# print(scissors)

l=[rock,paper,scissors]
user=int(input("type 0 for rock ,1 for paper and 2 for scissors\n"))
computer = random.randint(0,2)
print("computer choice", computer)

if user>=3 or user <0:
    print("invalid number ")
elif user==0 and computer==2:
    print("user win")
elif user==2 and computer==0:
    print("computer win")
elif computer>user:
    print("computer wins")
elif user>computer:
    print("user win")
else :
    print("draw")







