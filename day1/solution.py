def parse_data():
    return open('input.txt').readlines()


str_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def part1(data):
    numbers = []
    for line in data:
        number = ''
        for c in line:
            if c.isdigit():
                number += c
                break
        for c in reversed(line):
            if c.isdigit():
                number += c
                break
        numbers.append(int(number))
    return sum(numbers)


def part2(data):
    total_numbers = []
    for line in data:
        numbers = {}

        for i, n in enumerate(str_numbers, 1):
            try:
                number_index = line.index(n)
            except ValueError:
                continue
            else:
                numbers[number_index] = str(i)
            try:
                number_index = line.rindex(n)
            except ValueError:
                continue
            else:
                numbers[number_index] = str(i)

        for i, c in enumerate(line):
            if c.isdigit():
                numbers[i] = c
        print(numbers)
        full_number = numbers[min(numbers)] + numbers[max(numbers)]
        print(line, full_number)
        total_numbers.append(int(full_number))
    return sum(total_numbers)




if __name__ == '__main__':
    data = parse_data()
    # print(part1(data))
    print(part2(data))
