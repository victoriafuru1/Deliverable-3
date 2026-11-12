from character import Character

class Battle:
    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero 
        self.enemy = enemy

    def play_round(self):
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self): 
        while self.enemy.is_alive and self.hero.is_alive:
            self.play_round()

        if self.hero.is_alive:
            print("The Hero won!")
            return self.hero
        else:
            print("The enemy won!")
            return self.enemy