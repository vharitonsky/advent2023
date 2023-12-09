import math

def get_move_gen(moves):
    def gen():
        while True:
            for m in moves:
                yield m
    return gen()


class Map:
    def __init__(self, map_lines):
        self.map = {}
        for line in map_lines:
            key, values = line.strip().split(' = ')
            left, right = values[1:][:-1].split(', ')
            self.map[key] = (left, right)

    def traverse(self, start, finish, moves):
        pos = start
        steps = 0
        move_gen = get_move_gen(moves)
        while True:
            if finish(pos):
                return steps
            steps += 1
            move = next(move_gen)
            if move == 'L':
                pos = self.map[pos][0]
            else:
                pos = self.map[pos][1]


def parse_data():
    data = open('input.txt')
    moves = next(data).strip()
    next(data)
    map = Map(list(data))
    return moves, map


def part1(moves, map):
    return map.traverse('AAA', lambda pos: pos == 'ZZZ', moves)


def part2(moves, map):
    all_steps = []
    for key in map.map:
        if key.endswith('A'):
            all_steps.append(map.traverse(key, lambda pos: pos.endswith('Z'), moves))
    return math.lcm(*all_steps)


if __name__ == '__main__':
    data = parse_data()
    print(part1(*data))
    print(part2(*data))
