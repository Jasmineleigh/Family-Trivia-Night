from family_game_night.questions import question
from family_game_night.round3 import p1, p2, p3, p4, p5, p1_points, p2_points, p3_points, p4_points, p5_points

# title_of_round
input()
print("\n\n---Finish the Lyric---")
input()
print("-->Each player will try to finish the next lyric in the song presented.")
input()

# question 1
question1 = question("\nPlop, Plop. Fizz, Fizz.--", "Oh what a relief it is.")
print(question1.prompt)

guess = input(f"{p1}, What do you think the answer is? ") # player trys to guess answer

print("\n")
correct = question1.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 2
question1 = question("\nLike a good neighbor,--", "Statefarm is there.")
print(question1.prompt)

guess = input(f"{p2}, What do you think the answer is? ")

print("\n")
correct = question1.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 3
question1 = question("\nLike a good neighbor,--", "Statefarm is there.")
print(question1.prompt)

guess = input(f"{p3}, What do you think the answer is? ")

print("\n")
correct = question1.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 4
question1 = question("\nNothing like it,--", "Krystals.")
print(question1.prompt)

guess = input(f"{p4}, What do you think the answer is? ")

print("\n")
correct = question1.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 5
question1 = question("\nThe best part of waking up --", "is Folder's in your cup.")
print(question1.prompt)

guess = input(f"{p5}, What do you think the answer is? ")

print("\n")
correct = question1.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

input("Press [Enter] to continue.")
