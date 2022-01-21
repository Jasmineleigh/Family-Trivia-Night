class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def got_answer(self, guess, contestant):
        if guess.lower() in self.answer.lower():
            print(f"{contestant}, You got it!")
            return True
        else:
            print(f"{contestant}, You got it wrong\nThe Answer is {self.answer}.")
