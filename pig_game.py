# Roll dice - generate two random numbers between 1 and 6
# Check if one or both numbers are 6
# If not add result
# if one 6, end turn, if two 6's score is 0
# If not 6, add score
# ask if player wanted to reroll?
#
import random

def roll():
    roll = [1,2,3,4,5,6]
    roll_tuple = (random.choice(roll), random.choice(roll))
    return roll_tuple

def check_roll(roll, score):
    if roll[0] == 6 and roll[1] == 6:
        return "You lost all your points!", 0, '0'
    elif roll[0] == 6 or roll [1] == 6:
        return "You lost your turn" , score, '1'

    return roll[0] + roll[1], score , '2'


def player_input():
    again = input("Would you like to roll again (Y/N)? ")
    return again

in_turn = 0
player1_score = 0
computer_score = 0
rounds_played = 3

for i in range (rounds_played):
    print("\n" + "#"*12 +"Players turn" + "#"*12)
    while (in_turn == 0):
        print(f"Computer score is {computer_score} \n")
        roll_result = roll()
        print(roll_result)
        result = check_roll(roll_result, player1_score)
        if result[2] == '0':
            player1_score = 0
            print(result[0])
            print(f"Your score is currently {player1_score}")
            break
        if result[2] == '1':
            print(result[0])
            print(f"Your score is currently {player1_score}")
            break
        if result[2] == '2':
            print(f"roll score =  {result[0]}")
            player1_score +=result[0]
            print(f"Total score: {player1_score} \n")
            roll_again = player_input()
            if roll_again == 'Y':
                continue
            if roll_again == 'N':
                break

    print("\n" + "#"*12 +"computers turn" + "#"*12)

    for i in range (3):
        roll_result = roll()
        print(roll_result)
        result = check_roll(roll_result, computer_score)
        if result[2] == '0':
            computer_score = 0
            print(result[0])
            print(f"Your score is currently {computer_score}")
            break
        if result[2] == '1':
            print(result[0])
            print(f"Your score is currently {computer_score}")
            break
        if result[2] == '2':
            print(f"roll score =  {result[0]}")
            computer_score +=result[0]
            print(f"Total score: {computer_score}")



print(f"\nRounds played {rounds_played}")
print(player1_score,computer_score)
