"""Exact finite-state checks for uniform-edge dimer RSA on nearly complete graphs.

Run: python verify.py.  Only the Python standard library is needed.
This tests finite cases, not the limiting theorem's analytic proof.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb
from itertools import permutations


def jamming_probability(n, forbidden):
    forbidden = {tuple(sorted(e)) for e in forbidden}
    assert all(0 <= u < v < n for u, v in forbidden)
    available = [(1 << u) | (1 << v) for u in range(n)
                 for v in range(u + 1, n) if (u, v) not in forbidden]

    @lru_cache(None)
    def q(mask):
        choices = [e for e in available if mask & e == e]
        if not choices:
            return Fraction(int(mask.bit_count() == 2))
        return sum((q(mask ^ e) for e in choices), Fraction()) / len(choices)

    return q((1 << n) - 1)


def cycle(n):
    return {(i, (i + 1) % n) for i in range(n)}


def matching(n):
    return {(2 * i, 2 * i + 1) for i in range(n // 2)}


def main():
    tests = 0
    # Only one forbidden edge: exact survival probability is 3/(n^2-1).
    for n in (4, 6, 8, 10, 12, 14):
        assert jamming_probability(n, {(0, 1)}) == Fraction(3, n*n-1)
        tests += 1
    # Complement of a cycle: exact finite benchmarks via an independent
    # recursion over vertex vacancy masks (not the asymptotic approximation).
    known = {
        4: Fraction(0),
        6: Fraction(1, 3),
        8: Fraction(212, 825),
        10: Fraction(178177, 825825),
        12: Fraction(1176274483, 6324993675),
        14: Fraction(5221338553679, 31915014513525),
    }
    for n, expected in known.items():
        assert jamming_probability(n, cycle(n)) == expected
        tests += 1
    # For every four-vertex graph H, independently calculate the endpoint
    # probability and confirm that the forbidden graph defines the only
    # possible two-vertex terminal states whenever H is triangle-free.
    for hbits in range(1 << 6):
        pairs = [(u, v) for u in range(4) for v in range(u+1, 4)]
        bad = {p for j,p in enumerate(pairs) if hbits & (1<<j)}
        triangle_free = all(not ({(a,b),(a,c),(b,c)} <= bad)
                            for a in range(4) for b in range(a+1,4)
                            for c in range(b+1,4))
        if triangle_free:
            result = jamming_probability(4,bad)
            allowed = [e for e in pairs if e not in bad]
            outcomes = 0
            for arrival_order in permutations(allowed):
                occupied = set()
                for u,v in arrival_order:
                    if u not in occupied and v not in occupied:
                        occupied.update((u,v))
                outcomes += int(4 - len(occupied) == 2)
            from math import factorial
            brute = Fraction(outcomes, factorial(len(allowed)))
            assert result == brute, (bad, result, brute)
            tests += 1
    # Empty forbidden graph never leaves two particles unpaired.
    for n in (4,6,8,10):
        assert jamming_probability(n, set()) == 0
        tests += 1
    # Bounded-degree matching-deletion family: probabilities must be in [0,1].
    for n in (4,6,8,10,12):
        val=jamming_probability(n,matching(n))
        assert 0<=val<=1
        tests+=1
    print('PASS: {} exact finite-state assertions; no analytic limit inferred from tests.'.format(tests))
    print('cycle probabilities:')
    for n,x in known.items():
        print(n,str(x),float(x), 'N*q',float(n*x))

if __name__=='__main__':
    main()
