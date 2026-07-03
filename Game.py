
# #Traditional conditional
class Player:
    def __init__(self, name, points, health, location):
        self.name = name
        self.points = points
        self.health = health
        self.location = location

    def calculatePoints(self):
        if self.health > 75:
            self.points = 100
        elif self.health > 50:
            self.points = 50
        elif self.health > 25:
            self.points = 25
        elif self.health == 0:
            self.points = 0

player_1 = Player(
    input("Enter your name: "),
    int(input("Enter points: ")),
    int(input("Enter health: ")),
    input("Enter location: ")
)
print(player_1.name) 
player_1.calculatePoints()
print(player_1.points) 
print(player_1.health)
print(player_1.location)


#Pattern matching
class Player:
    def __init__(self,name,points,health,location):
        self.name = name
        self.points = points
        self.health = health
        self.location = location

    def calculatePoints(self):
        match self.health:
            case _ if self.health > 75:
                self.points = 100
            case _ if self.health > 50:
                self.points = 50
            case _ if self.health > 25:
                self.points = 25
            case _ if self.health == 0:
                self.points = 0

player_1 = Player(
    input("Enter your name: "),
    int(input("Enter points: ")),
    int(input("Enter health: ")),
    input("Enter location: ")
)
player_1.calculatePoints()
print(player_1.name)     
print(player_1.points) 
print(player_1.health)    
print(player_1.location)  