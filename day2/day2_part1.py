class Rock:
    points = 1


class Paper:
    points = 2


class Scissors:
    points = 3


class Lose:
    points = 0


class Draw:
    points = 3


class Win:
    points = 6


def determine_outcome(oppo, you):
    oppo_mapping = {"rock": "A", "paper": "B", "scissors": "C"}
    you_mapping = {"rock": "X", "paper": "Y", "scissors": "Z"}

    # if oppo plays Rock
    if oppo == oppo_mapping["rock"]:
        # win if you play paper
        if you == you_mapping["paper"]:
            return Win
        elif you == you_mapping["scissors"]:
            return Lose
        else:
            return Draw

    elif oppo == oppo_mapping["paper"]:
        if you == you_mapping["scissors"]:
            return Win
        elif you == you_mapping["rock"]:
            return Lose
        else:
            return Draw

    elif oppo == oppo_mapping["scissors"]:
        if you == you_mapping["rock"]:
            return Win
        elif you == you_mapping["paper"]:
            return Lose
        else:
            return Draw

    else:
        return "I don't recognize this code"


def calc_score(fin):
    you_mapping_to_shape = {"X": Rock, "Y": Paper, "Z": Scissors}

    with open(fin, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]

    total_score = 0

    for rnd in lines:
        oppo = rnd[0]
        you = rnd[2]

        outcome = determine_outcome(oppo, you)
        rnd_score = you_mapping_to_shape[you].points + outcome.points
        total_score += rnd_score

    return total_score


def main():
    print(calc_score("example.txt"))
    print(calc_score("test.txt"))


main()
