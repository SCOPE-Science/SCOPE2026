"""Exact image-language check for alternating conserving four-input rules."""

from collections import Counter, deque
from itertools import product

from verify import boolean_solutions, conservation_matrix, rule_bit


def shortest_missing(f, g):
    """Return a shortest unattainable word of output pairs, or None."""
    successors = [[0] * 4 for _ in range(8)]
    for a, b, c, d, e in product((0, 1), repeat=5):
        state = 4*a + 2*b + c
        target = 4*c + 2*d + e
        label = 2*rule_bit(f, (a, b, c, d)) + rule_bit(g, (b, c, d, e))
        successors[state][label] |= 1 << target

    full = (1 << 8) - 1
    queue = deque([(full, ())])
    seen = {full}
    while queue:
        subset, word = queue.popleft()
        for label in range(4):
            nxt = 0
            for state in range(8):
                if subset & (1 << state):
                    nxt |= successors[state][label]
            if not nxt:
                return word + (label,)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, word + (label,)))
    return None


def main():
    solutions, rank, free = boolean_solutions(conservation_matrix(8))
    assert (len(solutions), rank, free) == (174, 17, 15)
    onto = []
    histogram = Counter()
    for f, g in sorted(solutions):
        word = shortest_missing(f, g)
        if word is None:
            onto.append((f, g))
        else:
            histogram[len(word)] += 1
    assert len(onto) == 16 and histogram == {1: 4, 2: 84, 3: 70}
    print("Surjective ordered pairs:", onto)
    print("Shortest missing even-aligned pair-word lengths:", dict(sorted(histogram.items())))


if __name__ == "__main__":
    main()
