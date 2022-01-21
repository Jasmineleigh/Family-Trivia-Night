from family_game_night.questions import question
from family_game_night.round1 import p1, p2, p3, p4, p5, p1_points, p2_points, p3_points, p4_points, p5_points

input()
# title
print("\n\n---Guess the Song---")
input()
# question 1
question1 = question("\"Hey pretty baby with the high heels on\n"
                     "You give me fever"
                     "\nLike I've never, ever known"
                     "\nYou're just a product of loveliness\"", "The Way You Make Me Feel")

print(question1.prompt + "\n")

guess = input(f"\n-->{p1}, What do you think the song is? ")

print("\n")
correct = question1.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 2
question2 = question("\"I had high hopes for us baby\n"
                     "Like I was on dope for us baby\n"
                     "Chasin' after a high that I'll never get back again\"", "Forever Don't Last")

print(question2.prompt + "\n")

guess = input(f"\n-->{p2}, What do you think the song is? ")

print("\n")
correct = question2.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 3
question3 = question("\"If we don't got it\n"
                     "I'll go get it (it ain't a thang)\n"
                     "And if it's broken\nI'll fix it (I don't complain)\"", "Man of the House")
print(question3.prompt + "\n")

guess = input(f"\n-->{p3}, What do you think the song is? ")

print("\n")
correct = question3.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 4
question4 = question("\"Listen to the song here in my heart\n"
                     "A melody I start but can't complete\n"
                     "Listen to the sound from deep within\n"
                     "It's only beginning to find release\"", "Listen")

print(question4.prompt + "\n")

guess = input(f"\n-->{p4}, What do you think the song is? ")

print("\n")
correct = question4.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 5
question5 = question("\"Hey sista, go sista, soul sista, flow sista\n"
                     "Hey sista, go sista, soul sista, go sista\n"
                     "Voulez-vous coucher avec moi, ce soir?\n"
                     "Voulez-vous coucher avec moi?\"", "Lady Marmalade")

print(question5.prompt + "\n")

guess = input(f"\n-->{p5}, What do you think the song is? ")

print("\n")
correct = question5.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 6
question6 = question("\"I met this little girlie, her hair was kinda curly\n"
                     "Went to her house and bust her out, I had to leave real early\n"
                     "These girls are really sleazy, all they just say is please me\"", "It's Tricky")

print(question6.prompt + "\n")

guess = input(f"\n-->{p1}, What do you think the song is? ")

print("\n")
correct = question6.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 7
question7 = question("\"Easy come, easy go, that's just how you live, oh\n"
                     "Take, take, take it all, but you never give\n"
                     "Should have known you was trouble from the first kiss\n"
                     "Had your eyes wide open\"", "Grenade")

print(question7.prompt + "\n")

guess = input(f"\n-->{p2}, What do you think the song is? ")

print("\n")
correct = question7.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 8
question8 = question("\"Pop pop, it's show time (show time)\n"
                     "Show time (show time)\nGuess who's back again?",
                     "24K Magic")

print(question8.prompt + "\n")

guess = input(f"\n-->{p3}, What do you think the song is? ")

print("\n")
correct = question8.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 9
question9 = question("\"You used to call me on my cell phone\n"
                     "Late night when you need my love\n"
                     "Call me on my cell phone\nLate night when you need my love\"",
                     "Hotline Bling")

print(question9.prompt + "\n")

guess = input(f"\n-->{p4}, What do you think the song is? ")

print("\n")
correct = question9.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 10
question10 = question("\"God will do what he said he will do\n"
                      "He will stand by his word, he will come through\"",
                      "No Weapon")

print(question10.prompt + "\n")

guess = input(f"\n-->{p5}, What do you think the song is? ")

print("\n")
correct = question10.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 11
question11 = question("\"Used to spend my nights out in a barroom\n"
                      "Liquor was the only love I've known\n"
                      "But you rescued me from reachin' for the bottom\n"
                      "And brought me back from being too far gone",
                      "Tennesse Whiskey")

print(question11.prompt + "\n")

guess = input(f"\n-->{p1}, What do you think the song is? ")

print("\n")
correct = question11.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 12
question12 = question("\"Well, you can tell by the way I use my walk\n"
                      "I'm a woman's man, no time to talk\n"
                      "Music loud and women warm, I've been kicked around\n"
                      "Since I was born\"", "Stayin' Alive")

print(question12.prompt + "\n")

guess = input(f"\n-->{p2}, What do you think the song is? ")

print("\n")
correct = question12.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 13
question13 = question("\"I never meant to cause you any sorrow\n"
                      "I never meant to cause you any pain\n"
                      "I only wanted to one time to see you laughing\n"
                      "I only wanted to see you\"", "Purple Rain")

print(question13.prompt + "\n")

guess = input(f"\n-->{p3}, What do you think the song is? ")

print("\n")
correct = question13.got_answer(guess, p3)
print("\n")

if correct == True:    p3_points += 1

# question 14
question14 = question("\"What? You wanna ball with the kid?\n"
                      "Watch your step, you might fall\nTrying "
                      "to do what I did\nMama, uh, mama, uh mama, "
                      "come closer\nIn the middle of the club with "
                      "the rub-a-dub, uh\"", "Gettin' Jiggy Wit It")

print(question14.prompt + "\n")

guess = input(f"\n-->{p4}, What do you think the song is? ")

print("\n")
correct = question14.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 15
question15 = question("\"Oh, when you walk by every night\n"
                      "Talking sweet and looking fine\nI get "
                      "kinda hectic inside\nMmm, baby I'm so into you\n"
                      "Darling, if you only knew\nAll the things that "
                      "flow through my mind\"", "Fantasy")

print(question15.prompt + "\n")

guess = input(f"\n-->{p5}, What do you think the song is? ")

print("\n")
correct = question15.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

print("This marks the end of the second round.\nHere is the current leaderboard.\n\n")

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

print(f"Congratulations, {scores[0][0]}! You are in the lead.\n"
      f"Keep up the good work! Let's get ready for the next round.\n")

input("Press [Enter] to continue.")
