from collections import defaultdict


class Game:
    id: int
    turns: list[dict[str, int]]

    def __str__(self):
        return str(self.id) + ' ' + str(self.turns)

    def __repr__(self):
        return str(self.id) + ' ' + str(self.turns)

    def __init__(self, raw):
        name, game = raw.strip().split(': ')
        self.id = int(name.split()[1])
        turns_raw = game.split('; ')
        self.turns = []
        for turn_raw in turns_raw:
            turn = defaultdict(int)
            steps = turn_raw.split(', ')
            for step in steps:
                number, colour = step.split()
                turn[colour] = int(number)
            self.turns.append(turn)

    def get_min_cubes(self):
        min_cubes = defaultdict(int)
        for turn in self.turns:
            for colour, number in turn.items():
                if min_cubes[colour] < number:
                    min_cubes[colour] = number
        return min_cubes


class Bag:
    cubes: dict[str, int]

    def __init__(self, cubes):
        self.cubes = defaultdict(int)
        for colour, count in cubes.items():
            self.cubes[colour] += count

    def enough_cubes(self, game):
        for turn in game.turns:
            for colour, number in turn.items():
                if self.cubes[colour] < number:
                    return False
        return True


def parse_data():
    return open('input.txt').readlines()


def part1(data):
    bag = Bag({'red': 12, 'green': 13, 'blue': 14})
    games = [Game(line) for line in data]
    ids = []
    for game in games:
        if bag.enough_cubes(game):
            ids.append(game.id)
    return sum(ids)


def part2(data):
    games = [Game(line) for line in data]
    powers = []
    for game in games:
        power = 1
        for number in game.get_min_cubes().values():
            power *= number
        powers.append(power)
    return sum(powers)


if __name__ == '__main__':
    data = parse_data()
    print(part1(data))
    print(part2(data))
