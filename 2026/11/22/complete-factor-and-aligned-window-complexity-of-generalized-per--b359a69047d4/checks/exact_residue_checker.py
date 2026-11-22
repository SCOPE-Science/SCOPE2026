"""Exact finite residue-class enumeration for factors of u_i=v2(i+1) mod q.

For K such that 2^K>length, each length-n window has at most one
entry divisible by 2^K. Its label runs through all residues modulo q.
The function exact_factors is thus an exhaustive, not sampled, factor-set
construction for the infinite word.
"""
from collections import defaultdict


def valuation2(a):
    return (a & -a).bit_length() - 1


def exact_factors(q, length):
    K = length.bit_length() + 1
    period = 1 << K
    seen = set()
    for start in range(period):
        vals = []
        hole = None
        for j in range(1, length + 1):
            x = (start + j) % period
            if x == 0:
                if hole is not None:
                    raise AssertionError('two holes in window')
                hole = j - 1
                vals.append(0)
            else:
                vals.append(valuation2(x) % q)
        if hole is None:
            seen.add(bytes(vals))
        else:
            for v in range(q):
                vals[hole] = v
                seen.add(bytes(vals))
    return seen


def deficiency(length):
    if length == 1:
        return 0
    k = length.bit_length() - 1
    return max(1 << (k - 1), length - (1 << k))


def expected(q, length):
    return q * length - deficiency(length)


def oddpart(n):
    return n >> ((n & -n).bit_length() - 1)


def main():
    count = 0
    for q in range(2, 8):
        for n in range(1, 97):
            v = exact_factors(q, n)
            assert len(v) == expected(q, n), (q, n, len(v), expected(q, n))
            count += 1
    for q in range(2, 8):
        for n in range(1, 3001):
            if n <= 3:
                continue
            x = expected(q, n)
            y = (2 * expected(q, n//2)) if n % 2 == 0 else expected(q, n//2) + expected(q, n//2 + 1)
            assert x == y, (q, n)
    print(f'PASS: {count} exact infinite-factor sets (q=2..7, n=1..96).')
    print('PASS: 17,982 recurrence equalities (q=2..7, n=4..3000).')
    for q in (2, 3, 4, 5):
        print('q=', q, 'factor counts n=1..16:', [expected(q, n) for n in range(1, 17)])


if __name__ == '__main__':
    main()
