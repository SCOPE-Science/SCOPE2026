#!/usr/bin/env python3
"""Finite brute-force checks for the two-run periodic Abelian-power theorem."""
from random import Random


def predicted_phase_count(a, b, q, k):
    p = a + b
    r = k % p
    if r == 0:
        return p
    s = min(r, p-r)
    if 2*s == p:
        return 2 if a % 2 == b % 2 == 0 else 0
    return max(a-q*s+1, 0) + max(b-q*s+1, 0)


def predicted_distinct_count(a, b, q, k):
    if q*k < a+b:
        return int(a >= q*k) + int(b >= q*k)
    return predicted_phase_count(a, b, q, k)


def direct_counts(a, b, q, k):
    block = '0'*a + '1'*b
    p = len(block)
    expanded = block*((q*k+p-1)//p+2)
    admissible = []
    for i in range(p):
        word = expanded[i:i+q*k]
        pieces = [word[j*k:(j+1)*k] for j in range(q)]
        if len({piece.count('1') for piece in pieces}) == 1:
            admissible.append(word)
    return len(admissible), len(set(admissible))


def main():
    cases = 0
    phases = 0
    for a in range(1, 13):
        for b in range(1, 13):
            p = a + b
            for q in range(3, 9):
                for k in range(1, 2*p+1):
                    observed = direct_counts(a,b,q,k)
                    expected = (predicted_phase_count(a,b,q,k), predicted_distinct_count(a,b,q,k))
                    assert observed == expected, (a,b,q,k,observed,expected)
                    cases += 1
                    phases += p
    rng = Random(170102836)
    for _ in range(2000):
        a = rng.randrange(1, 35)
        b = rng.randrange(1, 35)
        q = rng.randrange(3, 14)
        k = rng.randrange(1, 4*(a+b)+1)
        observed = direct_counts(a,b,q,k)
        expected = (predicted_phase_count(a,b,q,k), predicted_distinct_count(a,b,q,k))
        assert observed == expected, (a,b,q,k,observed,expected)
        cases += 1
        phases += a+b
    print(f'PASS cases={cases}; phase-start comparisons={phases}; exhaustive a,b=1..12, q=3..8, k=1..2(a+b); randomized=2000')

if __name__ == '__main__':
    main()
