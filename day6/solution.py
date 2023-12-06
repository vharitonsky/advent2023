class Race:

    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def __repr__(self):
        return f"{self.time} X {self.distance}"

    def ways_to_beat(self):
        count = 0
        for t in range(self.time):
            if t * (self.time - t) > self.distance:
                count += 1
        return count


def part1():
    lines = open('input.txt').readlines()
    times = lines[0].split(':')[1].strip().split()
    distances = lines[1].split(':')[1].strip().split()
    races = [
        Race(int(time), int(distance))
        for time, distance in zip(times, distances)
    ]
    result = 1
    for r in races:
        result *= r.ways_to_beat()
    return result


def part2():
    lines = open('input.txt').readlines()
    time = int(lines[0].split(':')[1].strip().replace(' ', ''))
    distance = int(lines[1].split(':')[1].strip().replace(' ', ''))
    race = Race(time, distance)
    return race.ways_to_beat()


if __name__ == '__main__':
    print(part1())
    print(part2())
