import random
class Dice:
    """ Represents a dice with n sides"""
    def __init__(self, sides: int = 6) -> None: 
        if sides < 2:
            raise ValueError("The dice needs to have atleast 2 sides")

        self.sides = sides

    def roll(self) -> int: 
        return random.randint(1, self.sides)

    def __repr__(self):
        return f"Dice(sides={self.sides})"

    def __call__(self):
        


