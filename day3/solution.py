from collections import defaultdict


class Number:
    def __init__(self, value, row, starts, ends):
        self.value = value
        self.row = row
        self.starts = starts
        self.ends = ends
        self.gears = []

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Engine:

    def __init__(self, lines):
        self.numbers = []
        self.all_numbers = []
        self.rows = defaultdict(lambda: defaultdict(str))
        single_line = ''
        for l in lines:
            single_line += l
        counter = 0
        number = ''
        for c in single_line:
            if c.isdigit():
                number += c
                if not number:
                    counter += 1
                continue
            if c.isdigit() and number:
                number += c
                continue
            if not c.isdigit():
                if number:
                    self.all_numbers.append(int(number))
                    number = ''

        for i, l in enumerate(lines):
            for j, c in enumerate(l):
                self.rows[i][j] = c

    def get_numbers(self):
        for i, row in self.rows.items():
            number = ''
            number_start = None
            for j, value in row.items():
                if value.isdigit():
                    number += value
                    if number_start is None:
                        number_start = j
                else:
                    if number:
                        self.numbers.append(
                            Number(int(number), i, number_start, j)
                        )
                        number_start = None
                        number = ''
            if number:
                self.numbers.append(
                    Number(int(number), i, number_start, len(row))
                )
        return self.numbers

    def get_valid_numbers(self):
        valid = []
        not_valid = []
        for number in self.numbers:
            for i in range(number.starts - 1, number.ends + 1):
                value = self.rows[number.row - 1][i]
                if value == '*':
                    number.gears.append((number.row - 1, i))
                value = self.rows[number.row + 1][i]
                if value == '*':
                    number.gears.append((number.row + 1, i))
                value = self.rows[number.row][i]
                if value == '*':
                    number.gears.append((number.row, i))
            else:
                not_valid.append(number)
        for number in self.numbers:
            for i in range(number.starts - 1, number.ends + 1):
                value = self.rows[number.row - 1][i]
                if value and not value.isdigit() and value != '.':
                    valid.append(number)
                    break
                value = self.rows[number.row + 1][i]
                if value and not value.isdigit() and value != '.':
                    valid.append(number)
                    break
                value = self.rows[number.row][i]
                if value and not value.isdigit() and value != '.':
                    valid.append(number)
                    break
            else:
                not_valid.append(number)
        return valid


def parse_data():
    return Engine([l.strip() for l in open('input.txt').readlines()])


def part1(engine):
    engine.get_numbers()
    return sum([n.value for n in engine.get_valid_numbers()])


def part2(engine):
    engine.get_numbers()
    engine.get_valid_numbers()
    double_gears = []
    seen_gears = set()
    for number in engine.numbers:
        if not number.gears:
            continue
        for other_number in engine.numbers:
            if number is other_number:
                continue
            if not other_number.gears:
                    continue
            for gear in number.gears:
                if gear in other_number.gears and gear not in seen_gears:
                    seen_gears.add(gear)
                    double_gears.append((number, other_number))
    return sum([g1.value * g2.value for g1, g2 in double_gears])


if __name__ == '__main__':
    print(part1(parse_data()))
    print(part2(parse_data()))
