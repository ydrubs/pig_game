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


    def Turn(self, human_turn = True): #True = player control, false = Computer control
        turn_result =  self.roll_result()
        print(turn_result)
        if turn_result[0] > 0:
            self.round_score += turn_result[0]
            self.total_score += turn_result[0]
            print(f'Your current round score is: {self.round_score}\n'
                  f'Your current total score is: {self.total_score} ')

            if human_turn:
                again = self.player_input()
                if again == 'y':
                    print('you have decided to roll again')
                    print()
                    self.Turn()

                elif again == 'n':
                    print('you have ended your turn')

            else:
                return turn_result

        if turn_result[1] == 'lose_turn':
            print('you rolled a six and lost your turn as well as points for this round.')
            self.total_score -= self.round_score
            print(f'Your current total score is: {self.total_score}')
            return self.total_score, turn_result

        if turn_result[1] == 'lose_points':
            print('you rolled TWO six and lost ALL your points.')
            self.total_score = 0
            return self.total_score, turn_result

        # print(f'Your current round score is: {self.round_score}\n'
        #       f'Your current total score is: {self.total_score} ')
        self.round_score = 0

    def player_input(self):
        while True:
            again =  input("Roll again(Y/N)?: ").casefold()
            if again == 'y' or again == 'n':
                print()
                return again
            print("invalid input")
            print()

    def computer_strategy1(self):
        self.round_score = 0
        re_roll = random.randint(1,3)
        for i in range(re_roll):
            result = self.Turn(False)
            # print(result[1][1])
            if result[1][1] == 'lose_turn':
                break
            if result[1][1] == 'lose_points':
                break

    def score_data(self):
        return self.total_score

# def score_card(score1, score2, round):
    # top_bottom = ' ' * 9 + '*' * 24
    # score_row = '\n' + 'round #' + str(round) + ' ' + '*' + ' ' * 4 + str(score1) + ' ' * 4 + '*' + ' ' * 4 + str(score2) + ' ' * 4 + '*'
    # print ((top_bottom + score_row + '\n')* round + top_bottom)

scores = []
def score_card(score1, score2, num_rounds):
    top_bottom = ' ' * 9 + '*' * 24
    score_rows = ''
    scores.append((score1, score2))

    for round_num in range(1, num_rounds + 1):
        score_row = '\n' + 'round #' + str(round_num) + ' ' + '*' + ' ' * 4 + str(
            scores[round_num -1][0]) + ' ' * 4 + '*' + ' ' * 4 + str(scores[round_num -1][1]) + ' ' * 4 + '*' + '\n'
        score_rows += top_bottom + score_row

    print('\n' + score_rows + top_bottom)
    print(scores)


player = Turn()
computer = Turn()
total_score = 0

for i in range (5):
    print('*' * 20, 'Players Turn', '*' * 20)
    player.Turn(True)
    print('*' * 20, 'Computers Turn', '*' * 20)
    computer.computer_strategy1()
    score_card(player.score_data(), computer.score_data(), i+1)

# computer.computer_strategy1()