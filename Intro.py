# Black History
# Guess the song
# Finish the lyric
# Random Trivia
import random

print("\n\n\tWelcome to the Merritt Family Trivia Night! Tonight we will play four different rounds!\n"
      "Each player will get a chance to participate, and the winner will get a prize worth playing for.\n"
      "\n-->Each player will guess a number between 0-100. This number will determine who will go first\n"
      "   and who goes after that person. The closest to what the computer chooses is the person\n"
      "   who will go first.\n\nFirst, each player needs to pick their nickname.")
player_name1 = input("\nPlease enter your nickname: ")
player_name2 = input("\nPlease enter your nickname: ")
player_name3 = input("\nPlease enter your nickname: ")
player_name4 = input("\nPlease enter your nickname: ")
player_name5 = input("\nPlease enter your nickname: ")

int(input(f"\n{player_name1}, What number do you think it is?"))
int(input(f"\n{player_name2}, What number do you think it is?"))
int(input(f"\n{player_name3}, What number do you think it is?"))
int(input(f"\n{player_name4}, What number do you think it is?"))
int(input(f"\n{player_name5}, What number do you think it is?"))

number = random.randint(0, 100)

print("\nThe computer picked... {number}\nHost please enter in the order of the contestants.\n".format(**locals()))

p1 = input("Who was closest? ")

p2 = input("Who was next? ")

p3 = input("Who was next? ")

p4 = input("Who was next? ")

p5 = input("Who is last? ")

players = (p1, p2, p3, p4, p5)

p1_points = 1
p2_points = 0
p3_points = 0
p4_points = 0
p5_points = 0

print(f"\nCongratulations, {p1} you had the closest guess! \n--> 1 point will be added to {p1}'s score.\n"
      f"\nHere is the order of the players: ")

for i in range(len(players)):
    print(str(i + 1) + ".)\t" + players[i])
