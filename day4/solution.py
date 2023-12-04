from collections import defaultdict


class Card:

    def __init__(self, raw):
        name, values = raw.split(':')
        self.id = int(name.split()[1])
        winning_numbers, card_numbers = values.split(' | ')
        self.winning = [int(n.strip()) for n in winning_numbers.split()]
        self.numbers = [int(n.strip()) for n in card_numbers.split()]
        self.matching = len([n for n in self.numbers if n in self.winning])
        self.score = 2 ** (self.matching - 1) if self.matching else 0

    def __mul__(self, other):
        return [self] * other


def parse_data():
    return [Card(line.strip()) for line in open('input.txt').readlines()]


def part1(data):
    return sum(card.score for card in data)


def part2(data):
    card_map = {card.id: card for card in data}
    all_cards = defaultdict(list)
    for card in data:
        all_cards[card.id].append(card)
    for id, cards in all_cards.items():
        if cards[0].matching:
            for i in range(id + 1, id + cards[0].matching + 1):
                all_cards[i].extend(card_map[i] * len(cards))
    return sum(len(v) for v in all_cards.values())


if __name__ == '__main__':
    data = parse_data()
    print(part1(data))
    print(part2(data))
