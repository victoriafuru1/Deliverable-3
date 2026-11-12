class Dice:
    """ Represents a dice with n sides"""
    def __init__(self, sides: int = 6) -> None: 
        if sides < 2:
            raise ValueError("The dice needs to have atleast 2 sides")

        self.sides = sides


