"""Exact certificate for the minimum-width transition of biclique graph associahedra.

Run with Python 3: python verify.py
Every finite comparison uses integer arithmetic, without floating-point tolerances.
The separate analytic argument covers all n >= 128.
"""
from itertools import combinations


def cut_weight(p: int, q: int, s: int, t: int) -> int:
    total = (2**p - 1) * (2**q - 1)
    return (total - (2**s - 1) * (2**t - 1)
            - (2**(p-s) - 1) * (2**(q-t) - 1))


def predicted(p: int, q: int):
    n = p + q
    if n <= 14:
        answers = {(0, 1), (p, q-1)}
        if p == q:
            answers |= {(1, 0), (p-1, q)}
        return answers
    low = n // 2
    return {(s, t)
            for s in {p//2, (p+1)//2}
            for t in {q//2, (q+1)//2}
            if s+t in {low, n-low}}


def check_exact_finite():
    profiles = cuts = comparisons = 0
    for n in range(4, 128):
        for p in range(2, n//2+1):
            q = n-p
            smallest_num = None
            smallest_den = None
            minimizers = set()
            for s in range(p+1):
                for t in range(q+1):
                    k = s+t
                    if k == 0 or k == n:
                        continue
                    w = cut_weight(p, q, s, t)
                    assert w > 0
                    a, b = w*w, k*(n-k)
                    cuts += 1
                    if smallest_num is None:
                        smallest_num, smallest_den = a, b
                        minimizers = {(s, t)}
                    else:
                        comparison = a*smallest_den - smallest_num*b
                        comparisons += 1
                        if comparison < 0:
                            smallest_num, smallest_den = a, b
                            minimizers = {(s, t)}
                        elif comparison == 0:
                            minimizers.add((s, t))
            expected = predicted(p, q)
            assert minimizers == expected, (p, q, minimizers, expected)
            profiles += 1
    return profiles, cuts, comparisons


def check_independent_tube_enumeration():
    cases = 0
    for p in range(2, 5):
        for q in range(p, 6):
            n = p+q
            left_mask = (1<<p)-1
            right_mask = ((1<<q)-1)<<p
            tubes = [u for u in range(1, 1<<n)
                     if u & left_mask and u & right_mask]
            for S in range(1, (1<<n)-1):
                s = (S & left_mask).bit_count()
                t = (S & right_mask).bit_count()
                observed = sum(1 for tube in tubes
                               if tube & S and tube & (((1<<n)-1)^S))
                assert observed == cut_weight(p,q,s,t), (p,q,s,t,observed)
                cases += 1
    return cases


def check_analytic_bounds():
    # Rational-side inequalities at the smallest dimension of the analytic range.
    # The proof shows that the scaled exponential bound decreases for n >= 128.
    from fractions import Fraction
    n=128
    assert Fraction(32,9*2**(n//8)) < Fraction(2,n*n)
    assert Fraction(16,9)*(
        Fraction(1,8)+Fraction(1,2**(n-3))) < Fraction(1,4)
    assert Fraction(16,9)*(
        Fraction(1,4)+Fraction(1,2**(n-2))) < Fraction(1,2)
    return 3


if __name__ == '__main__':
    p, cuts, comps = check_exact_finite()
    direct = check_independent_tube_enumeration()
    bounds = check_analytic_bounds()
    print('BICLIQUE_ASSOCIAHEDRON_WIDTH_CHECKS_PASSED',
          f'finite_profiles={p}', f'exact_cut_profiles={cuts}',
          f'exact_cross_comparisons={comps}',
          f'independent_tube_cut_tests={direct}', f'bound_checks={bounds}')
