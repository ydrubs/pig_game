import random

class Turn:
    def __init__(self):
        self.die1 = 0
        self.die2 = 0
        self.roll_score = 0
        self.round_score = 0
        self.total_score = 0

    def roll(self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1, 6)
        return self.die1, self.die2

    def roll_result(self):
        result = self.roll()
        # print(result)
        self.roll_score = 0
        if result[0] == 6 and result[1] == 6:
            return self.roll_score, 'lose_points'

        elif result[0] == 6 or result[1] == 6:
            return self.roll_score, 'lose_turn'

        else:
            self.roll_score = self.roll_score + result[0] + result[1]
            # print(f"Roll Score: {result[0] + result[1]}")
            return self.roll_score, 'cont'


    def score_calc(self, roll_result, turn_result):
        # print(roll_result)
        if roll_result > 0:
            self.round_score += roll_result
            self.total_score += roll_result
            return self.round_score, self.total_score

        elif roll_result == 0 and turn_result == 'lose_turn':
            self.round_score = 0

        elif roll_result == 0 and turn_result == 'lose_points':
            pass

    def Turn(self, human_turn = True): #True = player control, false = Computer control
        turn_result =  self.roll_result()
        print(turn_result)
        if turn_result[0] > 0:
            self.round_score += turn_result[0]
            self.total_score += turn_result[0]
            print(f'Your current round score is: {self.round_score}\n'
                  f'Your current total score is: {self.total_score} ')

            if human_turn == True:
                again = self.player_input()
                if again == 'y':
                    print('you have decided to roll again')
                    print()
                    self.Turn()

                if again == 'n':
                    print('you have ended your turn')

        if turn_result[1] == 'lose_turn':
            print('you rolled a six and lost your turn as well as points for this round.')
            self.total_score -= self.round_score
            print(f'Your current total score is: {self.total_score}')
            return self.total_score

        if turn_result[1] == 'lose_points':
            print('you rolled TWO six and lost ALL your points.')
            self.total_score = 0
            return self.total_score

        # print(f'Your current round score is: {self.round_score}\n'
        #       f'Your current total score is: {self.total_score} ')
        self.round_score = 0

    def player_input(self):
        again =  input("Roll again(Y/N)?: ").casefold()
        print()
        return again

    def score_data(self):
        return self.total_score



player = Turn()
computer = Turn()
total_score = 0

for i in range (2):
    print('*' * 20, 'Players Turn', '*' *20)
    player.Turn(True)
    print('*' * 20, 'Computers Turn', '*' *20)
    computer.Turn(False)

print('\n', '*' * 20, 'RESULTS', '*' *20)

print(f'Players Final Score: {player.score_data()}')
print(f'Computers Final Score: {computer.score_data()}')

