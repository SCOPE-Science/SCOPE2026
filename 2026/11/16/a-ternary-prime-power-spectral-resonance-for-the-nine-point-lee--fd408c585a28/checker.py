"""Exact small-modulus checks for finite Lee-cross convolution."""
from itertools import product
from collections import Counter

def cyclotomic_zero(u, n):
    # For a ternary prime power, equality of the three lifted coefficient bins
    # is equivalent to annihilation by a primitive n-th root of unity.
    m = n // 3
    c = [0] * n
    c[0] += 1
    for x in u:
        c[x] += 1
        c[(-x) % n] += 1
    return all(c[r] == c[r+m] == c[r+2*m] for r in range(m))

def pattern(u, n):
    m = n // 3
    a = sum(x == 0 for x in u)
    b = sum(x in (m, 2*m) for x in u)
    if a == 1 and b == 3:
        return 'A'
    if a != 0 or b != 1:
        return None
    others = [x for x in u if x not in (m, 2*m)]
    if len(others) != 3 or m == 1:
        return None
    # The three arms must occupy one complete lifted fiber,
    # independently up to sign.
    reps = [(x % m, (-x) % m) for x in others]
    r = reps[0][0]
    if r == 0: return None
    if any(r not in pair for pair in reps): return None
    cells = []
    for x in others:
        oriented = x if x % m == r else (-x) % n
        cells.append((oriented - r) // m)
    return 'B' if sorted(cells) == [0, 1, 2] else None

def check():
    for k in (1, 2, 3):
        n = 3 ** k
        tally = Counter()
        for u in product(range(n), repeat=4):
            actual = cyclotomic_zero(u, n)
            label = pattern(u, n)
            assert actual == (label is not None), (n, u, actual, label)
            if actual: tally[label] += 1
        m = n // 3
        assert tally['A'] == 32, (n, tally)
        assert tally['B'] == 192*(m-1), (n, tally)
        print(f'n={n}: modes={n**4}, type_A={tally["A"]}, type_B={tally["B"]}, nullity={sum(tally.values())}')
    # Elementary zero-polynomial arguments for non-ternary primes are analytical;
    # the numerical loops above are not offered as an infinite proof.
    print('All exact finite-modulus tests passed.')

if __name__ == '__main__':
    check()
