import random


class Dice:
    """Represents a dice with n sides."""
    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("The dice needs to have at least 2 sides")

        self.sides = sides

    def roll(self) -> int:
        """Roll dice and return a random number between 1 and sides."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Make the dice roll by calling the object directly."""
        return self.roll()
