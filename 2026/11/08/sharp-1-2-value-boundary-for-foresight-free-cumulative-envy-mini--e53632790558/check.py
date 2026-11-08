"""Independent finite checks for a temporal two-agent envy theorem.

Run: python3 check.py
Uses integer dynamic programming, not the proof's suffix invariants.
"""
from itertools import product
from random import Random


def greedy(values):
    delta = total = 0
    path = []
    for w in values:
        delta = abs(delta - w)
        total += delta
        path.append(delta)
    return total, path


def dynamic_program(values):
    # state: absolute value difference, minimal cumulative cost
    states = {0: 0}
    for w in values:
        next_states = {}
        for delta, cost in states.items():
            for successor in (abs(delta - w), delta + w):
                score = cost + successor
                if score < next_states.get(successor, float('inf')):
                    next_states[successor] = score
        states = next_states
    return min(states.values(), default=0)


def direct_enumeration(values):
    best = None
    for choices in product((-1, 1), repeat=len(values)):
        signed = cost = 0
        for w, sign in zip(values, choices):
            signed += sign * w
            cost += abs(signed)
        if best is None or cost < best:
            best = cost
    return 0 if best is None else best


def check():
    independent = 0
    for length in range(0, 9):
        for values in product((1, 2, 3), repeat=length):
            assert dynamic_program(values) == direct_enumeration(values)
            independent += 1
    count = 0
    for length in range(0, 16):
        for values in product((1, 2), repeat=length):
            actual = greedy(values)[0]
            expected = dynamic_program(values)
            assert actual == expected, (values, actual, expected)
            count += 1

    rng = Random(721913)
    samples = 0
    for length in (20, 40, 80, 150):
        for _ in range(240):
            values = [rng.choice((1, 2)) for _ in range(length)]
            assert greedy(values)[0] == dynamic_program(values)
            samples += 1

    # The property is falsified as soon as zero- or three-valued
    # goods are permitted; both examples have minimal length four.
    assert greedy((1, 1, 3, 1)) == (6, [1, 0, 3, 2])
    assert dynamic_program((1, 1, 3, 1)) == 4
    assert greedy((1, 1, 2, 0)) == (5, [1, 0, 2, 2])
    assert dynamic_program((1, 1, 2, 0)) == 3
    min_check = 0
    for length in range(0, 4):
        for values in product(range(0, 5), repeat=length):
            assert greedy(values)[0] == dynamic_program(values)
            min_check += 1
    assert min_check == 1 + 5 + 25 + 125
    print(f'PASS: {independent} exhaustive DP-versus-direct checks (length <= 8, values 1,2,3)')
    print(f'PASS: {count} exhaustive positive {{1,2}} words (length <= 15)')
    print(f'PASS: {samples} seeded positive {{1,2}} words (lengths 20,40,80,150)')
    print(f'PASS: {min_check} nonnegative words with length <= 3 and values in [0,4]')
    print('PASS: exact two length-four counterexamples, zero and three')


if __name__ == '__main__':
    check()
