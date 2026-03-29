'''Josh Hernandez
Assignment 5
OOP Classes for a Football team Organizer describing a team and its players
including Offensive, Defensive, and Special Teams players.
Module: PythonClasses.py'''

#Class with generic player information
#Methods include player name, stats, and changing jersey number
class Player:
    def __init__(self, name, position, team, number):
        self.name = name
        self.position = position
        self.team = team
        self.number = number

    def player_name(self):
        return f"{self.name} is currently playing on the field!"
    
    def get_stats(self):
        return f"{self.name} plays {self.position} for the {self.team} and is wearing jersey #{self.number}."
    
    #Method to change an attribute with input validation
    def change_jersey_number(self, new_number):
        new_number = int(input(f"Enter the new jersey number for {self.name}: "))
        if new_number >= 0 and new_number < 100:
            self.number = new_number
            print(f"{self.name} has changed the jersey number to {self.number}.")
        else:
            print("Invalid number! Jersey number must be between 0 and 99.")

#Class for any offensive player
#Inherits from Player class
#Includes methods for running plays, passing, scoring touchdowns, and changing positions
#Includes attributes for passes, rushes, touchdowns, and yards
class OffensivePlayer(Player):
    def __init__(self, name, position, team, number, passes=0, catches=0, rush=0, touchdowns=0, yards=0):
        super().__init__(name, position, team, number)
        self.passes = passes
        self.catches = catches
        self.rush = rush
        self.touchdowns = touchdowns
        self.yards = yards

    def run_play(self):
        return f"{self.name} runs the ball for {self.yards} yards! It was his {self.rush} rush of the game."

    def pass_ball(self):
        return f"{self.name} throws his pass for {self.yards} yards! It was his {self.passes} pass of the game."
    
    def catch_pass(self):
        return f"{self.name} catches the pass! It was his {self.catches} catch of the game."
    
    def score_touchdown(self):
        return f"{self.name} scores a touchdown! It was his {self.touchdowns} touchdown of the game."
    
    #Override the get_stats method to include more offensive stats
    def get_stats(self):
        full_stats = super().get_stats()
        full_stats += f" The Quarterback has thrown {self.passes} passes, rushed for {self.rush} yards, scored {self.touchdowns} touchdowns, and gained {self.yards} total yards."
        return full_stats

    #Method to change the player's position
    def change_position(self, new_position):
        new_position = input(f"Enter the new position for {self.name}: ")
        if new_position == "":
            print("Invalid position! Please choose a valid position.")
            return
        self.position = new_position
        print(f"{self.name} has changed positions to {self.position}.")

#Class for any defensive player
#Inherits from Player class
#Includes methods for tackling, intercepting passes, and qb sacks
class DefensivePlayer(Player):
    def __init__(self, name, position, team, number, tackles=0, interceptions=0, sack=0):
        super().__init__(name, position, team, number)
        self.tackles = tackles
        self.sack = sack
        self.interceptions = interceptions

    def tackle(self):
        return f"{self.name} playing {self.position} makes a tackle!"

    def interception(self):
        return f"{self.name} intercepts the ball! It was his {self.interceptions} interception of the game."
    
    def sack_quarterback(self):
        return f"{self.name}, jersey #{self.number}, has sacked the quarterback! It was his {self.sack} sack of the game."

#Class for any special teams player
#Inherits from Player class
#Includes methods for kicking the ball, returning kicks, and punting
#Includes attributes for kicks, returns, and punts
class SpecialTeamsPlayer(Player):
    def __init__(self, name, position, team, number, kicks=0, returns=0, punts=0):
        super().__init__(name, position, team, number)
        self.kicks = kicks
        self.returns = returns
        self.punts = punts
    
    def kick_ball(self):
        return f"{self.name} kicks the ball {self.kicks} yards for a field goal!"

    def return_kick(self):
        return f"{self.name} wearing jersey #{self.number} returns the kick for {self.returns} yards!"

    def punt_ball(self):
        return f"The {self.position} {self.name} punts the ball! It was his {self.punts} punt of the game."
    


