"""Independent verification of transfer counts and deletion-insertion implication.

Run: python3 verify_structural.py
Uses the actual channel definitions; no external packages.
"""
from itertools import product
from collections import Counter

PAIRS = ('00', '01', '10', '11')


def prof(word):
    c = Counter(word[i:i+2] for i in range(len(word)-1))
    return tuple(c[p] for p in PAIRS)


def ins_size(word):
    return len({prof(word[:i]+a+word[i:])
                for i in range(len(word)+1) for a in '01'})


def del_size(word):
    return len({prof(word[:i]+word[i+1:]) for i in range(len(word))})


def matrix_multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def test():
    transition = [[0, 1], [1, 1]]
    power = [[1, 0], [0, 1]]
    # Trace(M^(n-1)) counts no-00 words with matching endpoints.
    for n in range(1, 17):
        words = [''.join(x) for x in product('01', repeat=n)]
        equal_no00 = sum('00' not in w and w[0] == w[-1] for w in words)
        trace = power[0][0] + power[1][1]
        assert trace == equal_no00, (n, trace, equal_no00)
        power = matrix_multiply(power, transition)
        if n >= 2:
            # Every word with both 00,11 and equal endpoints has six profiles.
            six = sum('00' in w and '11' in w and w[0] == w[-1] for w in words)
            formula_six = 2**(n-1) - 2*trace + 1 - (-1)**n
            assert six == formula_six, (n, six, formula_six)
        if n <= 12 and n >= 2:
            for w in words:
                if del_size(w) == 6:
                    assert ins_size(w) == 6, (n, w)
    print('PASS: no-00 transfer recurrence, saturation counts through n=16')
    print('PASS: direct deletion-six implies insertion-six through n=12')


if __name__ == '__main__':
    test()
