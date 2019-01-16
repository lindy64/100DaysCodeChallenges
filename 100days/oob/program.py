from rolls import Roll, Player
import csv

csv_file = '/Users/davidythomas/PycharmProjects/100days/100days/oob/battles.csv'


def print_header():
    print('----------------------------------------------------------')
    print('                 15-way Rock Paper Scissors               ')
    print('----------------------------------------------------------')


def read_results_matrix(csv_file):
    with open(csv_file) as fin:
        return list(csv.DictReader(fin))


def get_player_one_name():
    player_one = input("Please enter the name of Player 1: ")
    return player_one


def results_checker(p1_roll, p2_roll, attacking_results):
    if p1_roll == p2_roll:
        return 'draw'
    else:
        for i in attacking_results:
            if i.name == p1_roll:
                return i.outcomes[p2_roll] 


def game_loop(player1, player2, attacking_options, attacking_results):
    count = 1
    p1_wins = 0
    p2_wins = 0
    while count <= 5:
        p2_roll = player2.roll(attacking_options)
        p1_roll = player1.roll(attacking_options)

        outcome = results_checker(p1_roll, p2_roll, attacking_results)
        if outcome == 'win':
            result = "Player One Wins!"
            p1_wins += 1
        elif outcome == 'lose':
            result = "Player Two Wins!"
            p2_wins += 1
        else:
            result = "Draw!!"

        print(f"Round {str(count)}: Player One: {p1_roll} .... Player Two: {p2_roll}  >>>>> Result: {result} ")

        count += 1

    if p1_wins > p2_wins:
        print(f"Player One is victorious with {str(p1_wins)} victory to {str(p2_wins)}")
    else:
        print(f"Player Two is victorious with {str(p2_wins)} victory to {str(p1_wins)}")


def main():

    print_header()
    results_matrix = read_results_matrix(csv_file)

    attacking_results = []
    for i in results_matrix:
        attacking_results.append(Roll(i['Attacker'], i))

    attacking_options = []
    for i in results_matrix:
        attacking_options.append(i['Attacker'])

    name = get_player_one_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, attacking_options, attacking_results)


if __name__ == '__main__':
    main()