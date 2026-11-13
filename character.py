
from items import Weapon


class Character:
    """Represents a character in the RPG"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character
        
        Args:
        name (str): The name of the character.
        hp_max (int): Max hit points (default = 100)
        damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon 

    def take_damage(self, amount: int) -> None:
        """Reduce the characters own HP without going under 0.""" 
        self._hp -= amount
        self._hp = max(self._hp, 0)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None: 
            dmg = self.weapon.roll_damage()
        else: 
            dmg = self.damage
        
        target.take_damage(dmg)

    def heal(self, amount: int) -> None:
        """Let character heal."""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object."""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"
    
    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"
    
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe
        edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Check if character is alive."""
        return self._hp > 0
           

class Warrior(Character):
    def __init__(self, name, hp_max=100, damage=10, weapon=None, armour: int = 5):
        super().__init__(name, hp_max, damage, weapon)
        self.armour = armour

    def take_damage(self, amount: int) -> None:
        """ Armour makes character take less damage"""
        armour_damage = amount - self.armour
        armour_damage = max(armour_damage, 0)
        super().take_damage(armour_damage)

    def __str__(self) -> str:
        return f"{super().__str__()} | Armour: {self.armour}"


class Mage(Character):
    def __init__(self, name, hp_max=100, damage=10, weapon=None, mana: int = 30, mana_max: int = 30):
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana 
        self.mana_max = mana_max

    def attack(self, target):
        if self.mana >= 10: 
            self.mana -= 10
            magic_damage = self.damage * 2
            print(f"{self.name} attacks with magic!")

            target.take_damage(magic_damage)
        else:
            self.mana += 5
            print(f"{self.name} attacks with weapon and restores 5 mana")
            super().attack(target)

    def __str__(self) -> str:
        return f"{super().__str__()} | Mana: {self.mana}/{self.mana_max}"
