# Josh Hernandez
# Week 5 Assignment 5
# Football Organizer describing a team and its players

import PythonClasses as fb

# Player Instances
# Creating instances of Player with various attributes
# Parameters are (name, position, team, number):
player1 = fb.Player("Kyler Murray", "Quarterback", "Cardinals", 1)
player2 = fb.Player("Walter Nolen", "Defensive Tackle", "Cardinals", 97)
player3 = fb.Player("Marvin Harrison Jr.", "Wide Receiver", "Cardinals", 18)

#Offensive Player Instances
#Creating instances of OffensivePlayer with various attributes
#Parameters are (name, position, team, number, passes=0, catches=0, rush=0, touchdowns=0, yards=0):
qb = fb.OffensivePlayer("Kyler Murray", "Quarterback", "Cardinals", 1, "first", touchdowns="third", yards=45)
rb = fb.OffensivePlayer("James Conner", "Running Back", "Cardinals", 22, rush="ninth", touchdowns=2, yards=12)
wr = fb.OffensivePlayer("Larry Fitzgerald", "Wide Receiver", "Cardinals", 11, catches="fifth", yards=80)

#Defensive Player Instances
#Creating instances of DefensivePlayer with various attributes
#Parameters are (name, position, team, number, tackles=0, interceptions=0, sack=0)
cb = fb.DefensivePlayer("Garret Williams", "Cornerback", "Cardinals", 5, tackles="sixth", interceptions="first", sack="first")
lb = fb.DefensivePlayer("Isaiah Simmons", "Linebacker", "Cardinals", 9, tackles="eighth", interceptions=0, sack="second")
db = fb.DefensivePlayer("Budda Baker", "Safety", "Cardinals", 3, tackles="tenth", interceptions="first", sack="third")

#Special Teams Player Instances
#Creating instances of SpecialTeamsPlayer with various attributes
#Parameters are (name, position, team, number, kicks=0, returns=0, punts=0)
kicker = fb.SpecialTeamsPlayer("Chad Ryland", "Kicker", "Cardinals", 9, kicks=52)
returner = fb.SpecialTeamsPlayer("Cordarrelle Patterson", "Returner", "Falcons", 84, returns=22)
punter = fb.SpecialTeamsPlayer("Blake Gillikin", "Punter", "Cardinals", 6, punts="fifth")

print("\nWelcome to the Football Team Organizer!\n")
print("********Player Information:********")
print(player1.get_stats())
print(player2.get_stats())
print(player3.get_stats())

print("\n********The Offense is Playing:********")
print(qb.pass_ball())
print(rb.run_play())
print(wr.catch_pass())
print(qb.score_touchdown())

print("\n********The Defense is Playing:********")
print(cb.interception())
print(lb.tackle())
print(db.sack_quarterback())
print(cb.get_stats())

print("\n********The Special Teams unit is now on the field:********")
print(kicker.kick_ball())
print(returner.return_kick())
print(punter.punt_ball())





