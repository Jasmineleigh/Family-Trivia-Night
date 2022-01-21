# Essentially this is the "Start Button" for now

from family_game_night.round4 import p1, p2, p3, p4, p5, p1_points, p2_points, p3_points, p4_points, p5_points
input()
print("This marks the end of the family trivia night.\nHere is the final leaderboard.\n\n")

input("Press [Enter] to continue.")

scores = [[p1, p1_points], [p2, p2_points], [p3, p3_points], [p4, p4_points], [p5, p5_points]]

scores.sort(key=lambda x:x[-1])
scores.reverse()

print(" ___________________________")
print("|***************************|")
print("|******* Leader Board ******|")
print("|***************************|")
print(" VVVVVVVVVVVVVVVVVVVVVVVVVVV")
print(f" 1.) {scores[0][0]} - {scores[0][1]}")
print(f" 2.) {scores[1][0]} - {scores[1][1]}")
print(f" 3.) {scores[2][0]} - {scores[2][1]}")
print(f" 4.) {scores[3][0]} - {scores[3][1]}")
print(f" 5.) {scores[4][0]} - {scores[4][1]}")

print(f"Congratulations, {scores[0][0]}! You are the winner!")
