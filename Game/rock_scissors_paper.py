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

game = [rock, paper, scissors]

# rock, paper, scissors 중에 하나 입력받기
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game[user_choice])
# rock, paper, scissors 중 하나 랜덤하게 출력
com_choice = int(random.random()*len(game))
print(game[com_choice])
# 같으면(index - index) 무승부
if user_choice == com_choice:
  print("draw")
# 다르다면 
else:
  # 승리 경우의 수: user - com = -2, 1, 1
  if user_choice - com_choice == -2 or user_choice - com_choice == 1:
    print("You win")
  # 패배의 경우의 수: -1, -1, 2
  else:
    print("You lose")

# 1. 입력이 rock(0)이면
#   1.1 paper(1)이면 패배
#   1.2 scissors(2) 승리
# 2. paper(1)
#   2.1 rock(0) 승리
#   2.2 scissors(2) 패배
# 3. scissors(2)
#   3.1 rock(0) 패배
#   3.2 paper(1) 승리

