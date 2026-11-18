class Character:
    def __init__(self, name:str, health:int, attack_power:int):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def describe(self):
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK"

    def attack(self, target:"Character") -> None:
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")


    def heal(self,amount:int):
        if amount <= 0:
            print("Healing amount cannot be 0 or negative")
            return
        
        self.health += amount
        self.health = min(self.health,100)
        return f"{self.name} now has {self.health} HP"




    # Level 2 pseudo
    def __init__(self, ):
        self._health = health   # use protected (encapsulation)
        self.__max_health = self.health

    @property
    def health (self) -> int:
        return self.health

    @property
    def is_alive(self) -> bool:
        return self._health >0