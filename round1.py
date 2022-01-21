from family_game_night.questions import question
from family_game_night.Intro import p1, p2, p3, p4, p5, p1_points, p2_points, p3_points, p4_points, p5_points

input()
# title
print("\n\n---Black History Trivia---")
print("-->Each player will take turns answering a question.")
input()
# checks players' answers

print("We will now begin with the black history trivia.")

# question 1
question1 = question("\nWhen was Tyler Perry’s first play?", "1992")
print(question1.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question1.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 2
question2 = question("\nWhen was MLK Jr.’s March to Washington?", "August 28, 1963")
print(question2.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question2.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 3
question3 = question("\nWhen was Oprah Winfrey's first show aired?", "September 8, 1986")
print(question3.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question3.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 4
question4 = question("\nWho was the first black Miss America?", "Vanessa Williams")
print(question4.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question4.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 5
question5 = question("\nHow many members are in New Edition?", "6")
print(question5.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question5.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 6
question6 = question("\nWhen is Black History Month?", "February")
print(question6.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question6.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 7
question7 = question("\nHi, I am a teenager who was born July 25, 1941\n"
                     "I was murdered in August of 1955 at the age of 14.\n"
                     "My death inspired black Americans to begin the civil rights movement.\n"
                     "I had an open casket funeral. Who am I?", "Emmett Till")
print(question7.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question7.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 8
question8 = question("\nThis was a network of people, African American as well as white, "
                     "offering shelter and aid to escaped enslaved people from the South. ", "The Underground Railroad")
print(question8.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question8.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 9
question9 = question("\nWhat does NAACP stand for?", "National Association for the Advancement of Colored People")
print(question9.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question9.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 10
question10 = question("\nWe broke the “White – only” rules. We protested on segregated buses\n"
                      "by staying in our seat, or by drinking from the “Whites – only” water\n"
                      "fountain. Rosa Parks was one of us. They call us…",
                      "Freedom Riders")
print(question10.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question10.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

# question 11
question11 = question("\nWho was the first black president?", "Barack Obama")
print(question11.prompt)

guess = input(f"\n-->{p1}, What do you think the answer is? ")

print("\n")
correct = question11.got_answer(guess, p1)
print("\n")

if correct == True:
    p1_points += 1

# question 12
question12 = question("\nI grew up in Turkey. I do the tough interviews\nfor my news company. "
                      "Oprah is my best friend. Who am I? ", "Gayle King")
print(question12.prompt)

guess = input(f"\n-->{p2}, What do you think the answer is? ")

print("\n")
correct = question12.got_answer(guess, p2)
print("\n")

if correct == True:
    p2_points += 1

# question 13
question13 = question("\nWho were the top 3 popular members of Destiny’s Child (alphabetically)? ", "Beyonce, Kelly, Michelle")
print(question13.prompt)

guess = input(f"\n-->{p3}, What do you think the answer is? ")

print("\n")
correct = question13.got_answer(guess, p3)
print("\n")

if correct == True:
    p3_points += 1

# question 14
question14 = question("\nWho was the first black female vice president?", "Kamila Harris")
print(question14.prompt)

guess = input(f"\n-->{p4}, What do you think the answer is? ")

print("\n")
correct = question14.got_answer(guess, p4)
print("\n")

if correct == True:
    p4_points += 1

# question 15
question15 = question("\nWho was the first Black Disney Princess?", "Tiana")
print(question15.prompt)

guess = input(f"\n-->{p5}, What do you think the answer is? ")

print("\n")
correct = question15.got_answer(guess, p5)
print("\n")

if correct == True:
    p5_points += 1

print("This marks the end of the first round.\nHere is the current leaderboard.\n\n")

input("Press [Enter] to continue.")

scores = [[p1, p1_points], [p2, p2_points], [p3, p3_points], [p4, p4_points], [p5, p5_points]]
print(scores)

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