"""Finite reproducibility check for constrained Rule 90 image stabilization."""
from itertools import product
from math import comb


def update(word):
    n = len(word)
    return tuple(word[(i - 1) % n] ^ word[(i + 1) % n] for i in range(n))


def admissible(word):
    return not any(a and b for a, b in zip(word, word[1:] + word[:1]))


def check(n):
    m = n & -n
    last = m // 2
    states = {x for x in product((0, 1), repeat=n) if admissible(x)}
    old = len(states)
    for t in range(1, last + 3):
        states = {update(x) for x in states}
        assert len(states) < old if t <= last else len(states) == old, (n, t)
        old = len(states)
        if t <= last:
            exponent = m - 2 * t
            block = tuple((comb(exponent, i) % 2) if i <= exponent else 0 for i in range(m))
            witness = block * (n // m)
            assert admissible(witness), (n, t, witness)
            for _ in range(t - 1):
                witness = update(witness)
            assert any(witness) and not any(update(witness)), (n, t)


if __name__ == '__main__':
    for n in range(2, 17):
        check(n)
    print('VERIFY_OK n=2..16: image counts and all strict-step witnesses')
