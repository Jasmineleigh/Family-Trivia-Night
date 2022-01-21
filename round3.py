from family_game_night.questions import question
from family_game_night.round2 import p1, p2, p3, p4, p5, p1_points, p2_points, p3_points, p4_points, p5_points

input()
# title
print("\n\n---Random Trivia---")
input()
print("-->Each player will take turns answering a question.\n"
      "   There are 40 question that are unrelated.")
input()

# question 1
question1 = question("\nWhich country produces the most coffee in the world?", "Brazil")
print(question1.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question1.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 2
question2 = question("\nWhich song by Luis Fonsi and Daddy Yankee has the most views (of all time) on YouTube? ",
                     "\"Despacito\"")
print(question2.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question2.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1


# question 3
question3 = question("\nWhat is the capital city of Spain?", "Madrid")
print(question3.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question3.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1


# question 4
question4 = question("\nWhat is the third sign of the zodiac?", "Gemini")
print(question4.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question4.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 5
question5 = question("\nName the three primary colors (alphabetically).", "Blue, Red, Yellow")
print(question5.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question5.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 6
question6 = question("\nWhat language has the most words? ", "English")
print(question6.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question6.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 7
question7 = question("\nName the world’s largest ocean.", "The Pacific Ocean")
print(question7.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question7.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 8
question8 = question("\nWhat’s the hardest rock?", "A Diamond")
print(question8.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question8.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 9
question9 = question("\nHow many bones do sharks have in their bodies? ", "0 or none")
print(question9.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question9.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 10
question10 = question("\nThe fear referred to as arachnophobia indicates a fear of what?",
                      "Spiders")
print(question10.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question10.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 11
question11 = question("\nWhich boxer was known as “The Greatest” and “The People’s Champion”?", "Muhammad Ali")
print(question11.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question11.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 12
question12 = question("\nWhat is your body’s largest organ?", "The Skin")
print(question12.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question12.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 13
question13 = question("\nThe colored part of the human eye that controls how much "
                      "light passes through the pupil is called?", "The Iris")
print(question13.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question13.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 14
question14 = question("\nWhich company owns Bugatti, Lamborghini, Audi, Porsche, and Ducati?", "Volkswagen")
print(question14.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question14.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 15
question15 = question("\nThe Statue of Liberty was given to the US by which country?", "France")
print(question15.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question15.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 16
question16 = question("\nGoogle Chrome, Safari, Firefox, and Explorer are different types of what?",
                      "Web Browsers or Search Engines")
print(question16.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question16.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 17
question17 = question("Which US city is known as the City of Brotherly Love?", "Philadelphia or Philly")

print(question17.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question17.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 18
question18 = question("Who played Neo in The Matrix? ", "Keanu Reeves")

print(question18.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question18.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 19
question19 = question("What is the largest bone in the human body?", "The Femur")

print(question19.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question19.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 20
question20 = question("What is the symbol for potassium? ", "K")

print(question20.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question20.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 21
question21 = question("Which desert is the largest in the world?", "The Sahara Desert")

print(question21.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question21.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 22
question22 = question("What is the first letter on a typewriter?", "Q")

print(question22.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question22.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 23
question23 = question("How much weight can an ant lift?", "50 times its body weight")

print(question23.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question23.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# questions 24
question24 = question("When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win?",
                      "six or 6")

print(question24.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question24.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 25
question25 = question("What’s the shortcut for the “copy” function on most computers?", "ctrl + c")

print(question25.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question25.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 26
question26 = question("What does \"www\" stand for in a website browser?", "World Wide Web")

print(question26.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question26.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 27
question27 = question("What does Wi-Fi stand for?", "Wireless Fidelity")

print(question27.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question27.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 28
question28 = question("What geometric shape is generally used for stop signs?", "An octagon")

print(question28.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question28.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 29
question29 = question("Which animal can be seen on the Porsche logo?", "Horse")

print(question29.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question29.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 30
question30 = question("Who was the first woman pilot to fly solo across the Atlantic?",
                      "Amelia Earhart")

print(question30.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question30.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 31
question31 = question("What is the rarest M&M color?", "Brown")

print(question31.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question31.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 32
question32 = question("What was the first soft drink in space?", "Coke or Coca Cola")

print(question32.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question32.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 33
question33 = question("What is the most popular book ever written?", "The Bible")

print(question33.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question33.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 34
question34 = question("Who was the first man?", "Adam")

print(question34.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question34.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 35
question35 = question("How many days and nights did it rain when Noah was on the ark?", "40")

print(question35.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question35.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 36
question36 = question("Who were Adam and Eve's 3 sons (alphabetically)?", "Abel, Cain, Seth")

print(question36.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question36.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 37
question37 = question("By US law, exit signs in buildings must be one of what two colors?", "Red or Green")

print(question37.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question37.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 38
question38 = question('What is the primary ingredient in a "hoecake"?', "Cornmeal")

print(question38.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question38.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 39
question39 = question("The Chevy model known as the Camaro was originally intended to be called what?", "Panther")

print(question39.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question39.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 40
question40 = question("In what country is Valentine's Day practiced by women\n"
                      "rather being obligated to purchase chocolate for men?", "In Japan, women traditionally buy"
                                                                               "dark chocolate for the men.")

print(question40.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question40.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

print("This marks the end of the third round.\nHere is the current leaderboard.\n\n")

input("Press [Enter] to continue.")

scores = [[p1, p1_points], [p2, p2_points], [p3, p3_points], [p4, p4_points], [p5, p5_points]]

scores.sort(key=lambda x:x[1])
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