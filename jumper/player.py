class Player:
    def __init__(self):
        self.lives = 4
        self.guesses=[]

    def lose_lifes(self):
        self.lives -= 1
    
    def get_lives(self):
        return self.lives
    
    def set_guesses(self, guess):
        self.guesses.append(guess)

    def get_guesses(self):
        return self.guesses