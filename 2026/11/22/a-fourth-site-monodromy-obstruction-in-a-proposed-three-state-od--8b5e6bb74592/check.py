"""Reproduce exact finite-prefix orbit and monodromy certificates.

Requires only Python 3.9 or later. The infinite-system conclusion
follows separately from the invariant finite-coordinate factor.
"""
from itertools import product
from collections import Counter

# Input table: predecessor symbol 0 cycles 0->1->2->0;
# predecessor 1 interchanges 0,1; predecessor 2 interchanges 0,2.
PERM = ((1, 2, 0), (1, 0, 2), (2, 1, 0))


def update_direct(x):
    result = [(x[0] + 1) % 3]
    for previous, here in zip(x, x[1:]):
        if previous == 0:
            result.append((here + 1) % 3)
        elif previous == 1:
            result.append(1 - here if here <= 1 else 2)
        else:
            result.append(2 - here if here in (0, 2) else 1)
    return tuple(result)


def update_table(x):
    return tuple(PERM[x[i - 1] if i else 0][x[i]] for i in range(len(x)))


def compose_left(word):
    p = (0, 1, 2)
    for symbol in word:
        p = tuple(PERM[int(symbol)][k] for k in p)
    return p


def orbit(seed):
    seen = []
    x = tuple(seed)
    while x not in seen:
        seen.append(x)
        x = update_direct(x)
    assert x == tuple(seed), (seed, x)
    return seen


def cycle_profile(n):
    unvisited = set(product(range(3), repeat=n))
    profile = Counter()
    while unvisited:
        seed = min(unvisited)
        states = orbit(seed)
        assert all(t in unvisited for t in states)
        unvisited.difference_update(states)
        profile[len(states)] += 1
    return dict(sorted(profile.items()))


def main():
    for n in range(1, 5):
        states = product(range(3), repeat=n)
        assert all(update_direct(x) == update_table(x) for x in states)
    profiles = [cycle_profile(n) for n in range(1, 5)]
    assert profiles == [{3: 1}, {9: 1}, {27: 1}, {27: 3}], profiles

    words = []
    expected_words = ('012', '010201122', '010112220201201011122020102')
    for n, length in ((1, 3), (2, 9), (3, 27)):
        states = orbit((0,) * n)
        assert len(states) == length
        word = ''.join(str(state[-1]) for state in states)
        assert word == expected_words[n - 1], (n, word)
        words.append(word)
    assert list(map(compose_left, words)) == [(2, 0, 1), (2, 0, 1), (0, 1, 2)]

    for x in product(range(3), repeat=4):
        y = x
        for _ in range(27):
            y = update_direct(y)
        assert y == x, (x, y)

    seeds = [(0, 0, 0, k) for k in range(3)]
    sets = [set(orbit(s)) for s in seeds]
    assert all(len(s) == 27 for s in sets)
    assert len(set.union(*sets)) == 81
    assert all(not (sets[i] & sets[j]) for i in range(3) for j in range(i+1, 3))
    print('PASS: 3-, 9-, 27-cycles, followed by three disjoint 27-cycles')
    print('PASS: exact trace words and three monodromies (last one identity)')
    print('PASS: all 81 four-symbol states satisfy 27-step return')
    print('PASS: independent direct-rule and lookup-table implementations agree')


if __name__ == '__main__':
    main()
