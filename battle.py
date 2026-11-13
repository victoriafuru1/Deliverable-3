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
        round_nr = 1

        while self.enemy.is_alive and self.hero.is_alive:
            print(f"Round number{round_nr}")
            self.play_round()
            print(self.hero)
            print(self.enemy)
            round_nr += 1

        if self.hero.is_alive:
            print(f"The hero won!")
            return self.hero
        else:
            print(f"The enemy won!")
            return self.enemy