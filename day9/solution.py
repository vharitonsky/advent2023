class History:

    def __init__(self, values):
        self.values = values

    def extrapolate_right(self):
        diffs = [self.values[:]]
        while True:
            pairs = list(zip(diffs[-1][:-1], diffs[-1][1:]))
            new_diffs = [b - a for a, b in pairs]
            diffs.append(new_diffs)
            if all(d == 0 for d in new_diffs):
                break
        diffs[-1].append(0)
        reversed_diffs = list(reversed(diffs))
        for last_diff, second_to_last_diff in zip(reversed_diffs[:-1], reversed_diffs[1:]):
            second_to_last_diff.append(second_to_last_diff[-1] + last_diff[-1])
        return diffs[0][-1]

    def extrapolate_left(self):
        diffs = [self.values[:]]
        while True:
            pairs = list(zip(diffs[-1][:-1], diffs[-1][1:]))
            new_diffs = [b - a for a, b in pairs]
            diffs.append(new_diffs)
            if all(d == 0 for d in new_diffs):
                break
        diffs[-1].append(0)
        reversed_diffs = list(reversed(diffs))
        for last_diff, second_to_last_diff in zip(reversed_diffs[:-1], reversed_diffs[1:]):
            new_value = second_to_last_diff[0] - last_diff[0]
            second_to_last_diff.insert(0, new_value)
        return diffs[0][0]


def parse_data():
    return [History([int(c) for c in line.strip().split()]) for line in open('input.txt')]


def part1(data):
    r = sum(h.extrapolate_right() for h in data)
    return r


def part2(data):
    r = sum(h.extrapolate_left() for h in data)
    return r


if __name__ == '__main__':
    data = parse_data()
    print(part1(data))
    print(part2(data))
