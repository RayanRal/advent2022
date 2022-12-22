from utils import read_input

input_path = "./input/day2"

# Rock defeats Scissors,
# Scissors defeats Paper,
# Paper defeats Rock


# opponent is going to play: A for Rock, B for Paper, and C for Scissors
# you should play in response: X for Rock, Y for Paper, and Z for Scissors

# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
LOSE = 0
DRAW = 3
WIN = 6

player_shape_scores = {"X": 1, "Y": 2, "Z": 3}
outcome_scores = {"X": LOSE, "Y": DRAW, "Z": WIN}
round_scoring_rules = {
    "A": {"X": DRAW, "Y": WIN, "Z": LOSE},
    "B": {"X": LOSE, "Y": DRAW, "Z": WIN},
    "C": {"X": WIN, "Y": LOSE, "Z": DRAW},
}
round_shape_rules = {}
for op, rule in round_scoring_rules.items():
    shape = {v: k for k, v in rule.items()}
    round_shape_rules[op] = shape


def get_round_outcome_score(opponent: str, player: str) -> int:
    return round_scoring_rules.get(opponent).get(player)


def get_shape_score(player: str) -> int:
    return player_shape_scores.get(player)


def get_score_from_outcome(outcome: str) -> int:
    return outcome_scores.get(outcome)


def get_player_shape(opponent: str, outcome: int) -> str:
    return round_shape_rules.get(opponent).get(outcome)


def get_sum_round_scores(input: str):
    lines = read_input(input)
    round_scores = []
    for line in lines:
        (opponent, player) = line.strip().split(" ")
        shape_score = get_shape_score(player)
        outcome_score = get_round_outcome_score(opponent, player)
        round_score = shape_score + outcome_score
        round_scores.append(round_score)

    return sum(round_scores)


def get_sum_round_scores_pt2(input: str):
    lines = read_input(input)
    round_scores = []
    for line in lines:
        (opponent, outcome) = line.strip().split(" ")
        outcome_score = get_score_from_outcome(outcome)
        player_shape = get_player_shape(opponent, outcome_score)
        shape_score = get_shape_score(player_shape)
        round_score = outcome_score + shape_score
        round_scores.append(round_score)

    return sum(round_scores)


if __name__ == '__main__':
    total_score = get_sum_round_scores(input_path)
    print(total_score)
    score_pt2 = get_sum_round_scores_pt2(input_path)
    print(score_pt2)
