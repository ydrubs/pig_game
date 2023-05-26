import random

class Turn:
    def __init__(self):
        self.die1 = 0
        self.die2 = 0
        self.score = 0

    def roll(self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1, 6)
        return self.die1, self.die2

    def roll_result(self):
        result = self.roll()
        print(result)
        self.score = 0
        if result[0] == 6 and result[1] == 6:
            self.score = 0
            return self.score, 'end'

        elif result[0] == 6 or result[1] == 6:
            return self.score, 'end'

        else:
            self.score = self.score + result[0] + result[1]
            print(f"Roll Score: {result[0] + result[1]}")
            return self.score, 'cont'


player = Turn()
computer = Turn()
total_score = 0

for i in range (3):
    print("\n" + "#" * 12 + "turn number:" + str(i+1) + "#" * 12, end="\n")
    round_score = 0
    while True:
        print("\n" + "#"*12 +"Players turn" + "#"*12, end = "\n")
        score = player.roll_result()
        if score[1] == 'end':
            print(f"You lost your turn")
            print(f"Total Score (player): {total_score}")
            break
        if score[1] == 'cont':
            round_score += score[0]
            print(f"Round Score (player): {round_score}")
            print(f"Total Score (player): {total_score+round_score}")
            again = input("Roll again (Y/N)?: ").casefold()
            if again == 'n':
                total_score = round_score
                break


    for i in range(3):
        print("\n" + "#"*12 +"Computer turn" + "#"*12, end = "\n")
        score = computer.roll_result()
        print(f"Total Score (computer) - {score[0]}")
        if score[1] == 'n' or score[1] == 'end':
            break
