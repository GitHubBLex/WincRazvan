# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
#scorers = f'{player1} {goal_0}, {player2} {goal_1}'
scorers = player1 + ' '+ str(goal_0)+ ','+' '+ player2 + ' '+ str(goal_1)
print(scorers)
report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'
print(report)
# 1. Choose a player that played in the soccer match and store his name as a string in the variable player.
player = 'Erwin Koeman'

#2 .first_name: use slicing and the find-method (help) to isolate and store the player's first name.
first_name = player[0:5]
player.find('Erwin')
print(first_name)
#3 .last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player[6:12])
player.find('Koeman')
print(last_name_len)

#4 name_short: isolate and store the player's name in this format:
#G. von Examplestein
name_short = player[0:1] +'.' +' '+ player[6:12]
print(name_short)
#5.chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. Make sure the last character of this string is not a space! For our example player:
#Gut! Gut! Gut!
chant = ((first_name+"! ")*len(first_name))[0:34]
print(chant)
#5.good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).
good_chant = chant.find(chant) != ' '
print(good_chant)