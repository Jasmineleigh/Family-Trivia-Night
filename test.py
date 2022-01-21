from questions import question

p1 = "Jazz"
p1_points = 1
# checks players' answers


print("We will now begin with the black history trivia.")

# question 1
question1 = question("\nWhen was Tyler Perry’s first play?", "1992")
print(question1.prompt)

guess = input(f"{p1}, What do you think the answer is? ")

print("\n")
x = question1.got_answer(guess, p1_points, p1)
print("\n")

if x == True:
    p1_points += 1
