"""Exact checks for the finite-abelian path hard-core convolution theorem.

Runs with CPython 3.9+. Only integer arithmetic is used.
This is finite corroboration; the all-length argument is algebraic.
"""
from itertools import product
from math import comb


def continuum(n, q, mask):
    previous_previous = previous = 1
    for i in range(n):
        activity = -1 if mask >> i & 1 else q - 1
        previous_previous, previous = previous, previous + activity * previous_previous
    return previous


def expected(n, q, mask):
    if n % 3 != 1:
        return False
    return all(mask >> j & 1 for j in range(0, n, 3))


def boundary_mask(k):
    positions = {2, 3} | set(range(6, 3*k + 1, 3))
    return sum(1 << (j - 1) for j in positions)


def check_all():
    checks = 0
    for n in range(1, 17):
        k = (n - 1)//3
        for q in sorted(set([2, 3, 4, k + 2, k + 3])):
            if n % 3 == 1 and q < k + 2:
                continue
            num = 0
            for mask in range(1 << n):
                zero = continuum(n, q, mask) == 0
                assert zero == expected(n, q, mask), (n, q, mask, zero)
                if zero:
                    num += (q - 1)**mask.bit_count()
            if n % 3 == 1:
                assert num == (q - 1)**(k + 1) * q**(2*k)
            else:
                assert num == 0
            checks += 1
    for k in range(1, 8):
        mask = boundary_mask(k)
        n = 3*k + 1
        assert continuum(n, k + 1, mask) == 0
        assert not expected(n, k + 1, mask)
    print('Zero-pattern and character-multiplicity checks passed:', checks)


def check_direct_characters():
    # For cyclic G=Z/q, sum of each nontrivial character over G\{0}
    # is -1. Verify the actual exponentials independently using near-integer
    # complex arithmetic only for these small cases.
    import cmath
    for q,n in ((2,7), (3,6), (4,5)):
        for freq in product(range(q), repeat=n):
            expected_value = continuum(n, q, sum((1 << i) for i, v in enumerate(freq) if v))
            total = 0j
            for word in product(range(q), repeat=n):
                if any(word[i] != 0 and word[i+1] != 0 for i in range(n-1)):
                    continue
                total += cmath.exp(2j * cmath.pi * sum(u*v for u,v in zip(word,freq))/q)
            assert abs(total - expected_value) < 1e-8, (q,n,freq,total,expected_value)
    print('Direct character-sum checks passed')


if __name__ == '__main__':
    check_all()
    check_direct_characters()
