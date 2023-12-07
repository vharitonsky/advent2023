from collections import Counter

ALL_CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
ALL_CARDS_JOKER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


class Hand:
    def __init__(self, cards, bid):
        counter = Counter(cards)
        if len(counter) == 5:
            rank = 1
        elif len(counter) == 4:
            rank = 2
        elif len(counter) == 3:
            if counter.most_common(1)[0][1] == 2:
                rank = 3
            else:
                rank = 4
        elif len(counter) == 2:
            if counter.most_common(1)[0][1] == 3:
                rank = 5
            else:
                rank = 6
        else:
            rank = 7
        self.rank = rank
        self._cards = cards
        self.cards = [ALL_CARDS.index(c) for c in cards]
        self.bid = bid

    def __lt__(self, other):
        if self.rank > other.rank:
            return False
        if self.rank < other.rank:
            return True
        for self_card, other_card in  zip(self.cards, other.cards):
            if self_card > other_card:
                return True
            elif self_card < other_card:
                return False


class HandWithJoker(Hand):
    def __init__(self, cards, bid):
        counter = Counter(cards)
        if 'J' in counter:
            for c, score in counter.most_common():
                if c != 'J':
                    counter[c] += counter['J']
                    del counter['J']
                    break
        if len(counter) == 5:
            rank = 1
        elif len(counter) == 4:
            rank = 2
        elif len(counter) == 3:
            if counter.most_common(1)[0][1] == 2:
                rank = 3
            else:
                rank = 4
        elif len(counter) == 2:
            if counter.most_common(1)[0][1] == 3:
                rank = 5
            else:
                rank = 6
        else:
            rank = 7
        self.rank = rank
        self._cards = cards
        self.cards = [ALL_CARDS_JOKER.index(c) for c in cards]
        self.bid = bid


def parse_data():
    hands = []
    lines = open('input.txt').readlines()
    for line in lines:
        card, bid = line.strip().split()
        hands.append(Hand(card, int(bid)))
    return hands


def parse_data_joker():
    hands = []
    lines = open('input.txt').readlines()
    for line in lines:
        card, bid = line.strip().split()
        hands.append(HandWithJoker(card, int(bid)))
    return hands


def part1(hands):
    total = 0
    hands = sorted(hands)
    for rank, hand in enumerate(hands, 1):
        total += rank * hand.bid
    return total


def part2(hands):
    total = 0
    hands = sorted(hands)
    for rank, hand in enumerate(hands, 1):
        total += rank * hand.bid
    return total


if __name__ == '__main__':
    print(part1(parse_data()))
    print(part2(parse_data_joker()))
