"""Reproduce finite checks of a theorem on paperfolding-prefix factor obstructions."""
from collections import defaultdict


def bit(i):
    """The 1-based paperfolding bit at positive integer i."""
    assert i > 0
    odd = i // (i & -i)
    return '0' if odd % 4 == 1 else '1'


def word(n):
    return ''.join(bit(i) for i in range(1, n + 1))


def factor_occurrences(w, length):
    groups = defaultdict(list)
    for j in range(len(w) - length + 1):
        groups[w[j:j+length]].append(j)
    return groups


def minimal_absent_of_length(w, length):
    # Exact deck criterion: both (length-1)-factors must occur.
    interior = set(factor_occurrences(w, length - 2))
    shorter = set(factor_occurrences(w, length - 1))
    longer = set(factor_occurrences(w, length))
    return {a + v + b for v in interior for a in '01' for b in '01'
            if a + v in shorter and v + b in shorter
            and a + v + b not in longer}


def verify():
    # For offsets mod 16, the length-eight patterns differ only at the
    # unique index divisible by eight. Enumerate both values through
    # the first 128 positions and assert all 32 patterns are distinct.
    s = word(128)
    groups = [set(s[j:j+8] for j in range(i, 121, 16)) for i in range(16)]
    assert all(len(x) == 2 for x in groups)
    assert len(set().union(*groups)) == 32

    for k in range(5, 12):
        n = 1 << k
        m = n // 4
        s = word(n)
        A, B, C, D = (s[j*m:(j+1)*m] for j in range(4))
        assert B == D
        assert [i for i in range(m) if A[i] != B[i]] == [m//2-1]
        assert [i for i in range(m) if A[i] != C[i]] == [m-1]
        classes = factor_occurrences(s, m)
        repeats = {x: pos for x, pos in classes.items() if len(pos)>1}
        assert repeats == {B: [m, 3*m]}, (k, repeats)
        assert len(factor_occurrences(s, m+1)) == n-m
        # The candidate is absent; its prefix and suffix occur; all
        # other longest minimal absences are excluded by the factor deck.
        predicted = C[-1] + B + C[0]
        assert predicted not in s
        assert predicted[:-1] in s and predicted[1:] in s
        assert minimal_absent_of_length(s, m+2) == {predicted}, k
        if k <= 7:
            # Independent exhaustive range check for strictly longer
            # minimal absent factors, not used in the all-length proof.
            for length in range(m+3, n+2):
                assert not minimal_absent_of_length(s, length)
    print('VERIFY_OK base_patterns=32 dyadic_k=5..11 longest_absence_checks=7')


if __name__ == '__main__':
    verify()
