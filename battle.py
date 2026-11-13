from character import Character


class Battle:
    """A turn based battle between a hero and an enemy."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """One round of combat."""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        """Simulate the full battle until one is dead."""
        round_nr = 1

        while self.enemy.is_alive and self.hero.is_alive:
            print(f"Round number {round_nr}")
            self.play_round()
            print(self.hero)
            print(self.enemy)
            round_nr += 1

        if self.hero.is_alive:
            print(f"{self.hero.name} won!")
            return self.hero
        else:
            print(f"{self.enemy.name} won!")
            return self.enemy
        