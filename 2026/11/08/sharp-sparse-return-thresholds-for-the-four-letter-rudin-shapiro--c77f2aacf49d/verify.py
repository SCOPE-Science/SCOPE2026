"""Exact finite-language certificate for the four-letter Rudin-Shapiro word.

Run with Python 3 (standard library only): python verify.py
The proof of why the finite-language test is exhaustive is in RESULT.md.
"""
from itertools import combinations

SUB = {'a': 'ab', 'b': 'ac', 'c': 'db', 'd': 'dc'}
ALPHABET = 'abcd'
FOUR_OPTIMA = {(2, 14, 64, 66), (2, 52, 64, 66)}
FAST_OPTIMUM = (2, 4, 6, 8, 10)


def substitute(word):
    return ''.join(SUB[c] for c in word)


def factors(word, length):
    return {word[i:i + length] for i in range(len(word) - length + 1)}


def exact_factor_set():
    word = 'a'
    for _ in range(11):
        word = substitute(word)
    F = factors(word, 67)
    next_word = substitute(word)
    assert len(word) == 2048 and len(next_word) == 4096
    assert len(F) == 528
    assert factors(next_word, 67) == F
    lifted = set()
    for f in F:
        lifted.update(factors(substitute(f), 67))
    assert lifted == F
    return F, word, next_word


def columns(F, upper):
    ordered = sorted(F)
    # Bit j means the j-th distinct length-67 factor has an equal letter
    # at relative shift d.  The logical AND/OR tests are exact integers.
    return ordered, {
        d: sum(1 << i for i, f in enumerate(ordered) if f[0] == f[d])
        for d in range(1, upper + 1)
    }


def main():
    F, word, next_word = exact_factor_set()
    prefixes = {f[:11] for f in F}
    assert len(prefixes) == 80
    assert prefixes == factors(next_word, 11)

    # Odd and even positions always use disjoint two-letter alphabets.
    for i, c in enumerate(next_word):
        assert c in ('a', 'd') if i % 2 == 0 else c in ('b', 'c')

    ordered, c = columns(F, 66)
    full = (1 << len(ordered)) - 1
    assert all(c[d] == 0 for d in range(1, 67, 2))

    # At horizon 10, every one of the five even shifts is forced by
    # a factor having only that allowed match.
    for d in FAST_OPTIMUM:
        assert any(
            f[d] == f[0] and all(f[e] != f[0] for e in FAST_OPTIMUM if e != d)
            for f in prefixes
        )
    assert any(all(f[d] != f[0] for d in (2, 4, 6, 8)) for f in prefixes)
    u = 0
    for d in FAST_OPTIMUM:
        u |= c[d]
    assert u == full

    # Every subset of the ten admissible numerical delays is examined.
    horizon_solutions = []
    for mask in range(1 << 10):
        covered = 0
        shifts = []
        for d in range(1, 11):
            if mask & (1 << (d - 1)):
                covered |= c[d]
                shifts.append(d)
        if covered == full:
            horizon_solutions.append(tuple(shifts))
            assert set(FAST_OPTIMUM).issubset(shifts)
    assert len(horizon_solutions) == 32  # optional odd shifts
    assert tuple(FAST_OPTIMUM) in horizon_solutions

    # Exhaustively compare all 4-subsets of even delays <= 66.
    even = tuple(range(2, 67, 2))
    solutions = []
    checked = 0
    for S in combinations(even, 4):
        checked += 1
        if (c[S[0]] | c[S[1]] | c[S[2]] | c[S[3]]) == full:
            solutions.append(S)
    assert checked == 40920
    assert set(solutions) == FOUR_OPTIMA
    assert sum(1 for S in combinations(even[:-1], 4)) == 35960

    # Independent direct substitution-prefix tests, separate from factor masks.
    longer = substitute(next_word)
    for S in (*sorted(FOUR_OPTIMA), FAST_OPTIMUM):
        assert all(any(longer[i] == longer[i + d] for d in S)
                   for i in range(len(longer) - max(S)))

    # The two-symbol coding is the ordinary Rudin-Shapiro sequence.
    def count_11_mod2(n):
        v = n & (n >> 1)
        return v.bit_count() % 2

    assert all((longer[i] in 'cd') == bool(count_11_mod2(i))
               for i in range(len(longer)))

    print('VERIFY_OK factors67=528 factors11=80 four_shift_sets_checked=40920'
          ' max64_checked=35960 optimum_sets=2 horizon10_minimum=5')


if __name__ == '__main__':
    main()
