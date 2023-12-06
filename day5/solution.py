class SeedMap:

    def __init__(self, raw):
        self.ranges = []
        lines = [l for l in raw.split('\n') if l]
        for line in lines:
            destination, source, steps = line.split()
            destination = int(destination)
            source_start = int(source)
            steps = int(steps)
            source_end = source_start + steps
            self.ranges.append((source_start, source_end, destination, steps))
            self.ranges = sorted(self.ranges, key=lambda r: r[0])

    def get(self, number):
        for source_start, source_end, destination, steps in self.ranges:
            if source_end > number >= source_start:
                result = destination + (number - source_start)
                return result

        return number


def parse_data():
    lines = open('input.txt').readlines()
    seeds = [int(i) for i in lines[0].strip().split(': ')[1].split()]
    maps = []
    map_line = ''
    for line in lines:
        if line[0].isdigit():
            map_line += line
        elif map_line:
            maps.append(SeedMap(map_line))
            map_line = ''
    return seeds, maps


def part1(seeds, maps):
    locations = []
    for seed in seeds:
        value = seed
        for map in maps:
            value = map.get(value)
        locations.append(value)
    return min(locations)


def part2(seeds, maps):
    locations = []
    all_seeds = []
    for i in range(0, len(seeds), 2):
        start, length = seeds[i], seeds[i + 1]
        all_seeds.append((start, length))
    return all_seeds
    for range_start, range_length in
    #     seed_range = range(start, start + length)
    #
    #     value = next(seed_range)
    #     for map in maps:
    #         map_ranges = iter(map.ranges)
    #         current_map_range = next(map_ranges)
    #         while current_map_range[1] > value > current_map_range[0]:
    #
    #         value = map.get(value)
    #     locations.append(value)
    # return min(locations)


if __name__ == '__main__':
    data = parse_data()
    print(part1(*data))
    print(part2(*data))
