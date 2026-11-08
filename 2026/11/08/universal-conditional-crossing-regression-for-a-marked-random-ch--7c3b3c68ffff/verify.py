"""Exact finite verification of a conditional crossing-regression identity.

A random chord diagram is a uniformly sampled perfect matching of 2n
cyclically ordered endpoints. This script enumerates the unmarked matching
after fixing a chord, independently evaluating every crossing indicator.
Requires only Python's standard library.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial


def perfect_matchings(points):
    points = tuple(points)
    if not points:
        yield ()
        return
    x = points[0]
    for i in range(1, len(points)):
        y = points[i]
        remainder = points[1:i] + points[i+1:]
        for rest in perfect_matchings(remainder):
            yield ((x, y),) + rest


def crosses(edge1, edge2):
    a, b = sorted(edge1)
    c, d = sorted(edge2)
    return (a < c < b < d) or (c < a < d < b)


def doublefactorial_odd(k):
    val = 1
    while k > 1:
        val *= k
        k -= 2
    return val


def observed(n, a):
    e = (0, a+1)
    other = tuple(v for v in range(2*n) if v not in e)
    joint = defaultdict(lambda: [0, 0, 0])
    total = 0
    for M in perfect_matchings(other):
        t = sum(crosses(e, chord) for chord in M)
        y = sum(crosses(M[i], M[j]) for i in range(len(M)) for j in range(i+1, len(M)))
        row = joint[t]
        row[0] += 1
        row[1] += y
        row[2] += (y+t)
        total += 1
    return total, dict(joint)


def run():
    checks = 0
    cases = 0
    diagrams = 0
    for n in range(3, 8):
        total_expected = doublefactorial_odd(2*n-3)
        for a in range(n):
            b = 2*n-2-a
            total, joint = observed(n, a)
            diagrams += total
            assert total == total_expected
            checks += 1
            feasible = set(range(a%2, min(a,b)+1, 2))
            assert set(joint) == feasible
            checks += 1
            mean_t = Fraction(0)
            mean_t2 = Fraction(0)
            mean_y = Fraction(0)
            mean_ty = Fraction(0)
            mean_total = Fraction(0)
            for t in sorted(joint):
                k, sum_y, sum_K = joint[t]
                # Direct brute-force means, without using the four-type proof.
                observed_y = Fraction(sum_y, k)
                proposed_y = Fraction(a*(a-2)+b*(b-2),24) + Fraction(2*n-3,12)*t
                assert observed_y == proposed_y, (n, a, t, observed_y, proposed_y)
                checks += 1
                assert Fraction(sum_K,k) == proposed_y+t
                checks += 1
                # The independently countable distribution of bridge edges.
                mass_num = factorial(a)*factorial(b)
                mass_den = (factorial(t)*2**(n-1-t)*factorial((a-t)//2)
                            *factorial((b-t)//2)*doublefactorial_odd(2*n-3))
                assert Fraction(k,total) == Fraction(mass_num,mass_den)
                checks += 1
                w = Fraction(k,total)
                mean_t += w*t
                mean_t2 += w*t*t
                mean_y += w*observed_y
                mean_ty += w*t*observed_y
                mean_total += w*Fraction(sum_K,k)
            assert mean_t == Fraction(a*b,2*n-3)
            checks += 1
            var_t = mean_t2 - mean_t**2
            var_formula = Fraction(2*a*(a-1)*b*(b-1), (2*n-5)*(2*n-3)**2)
            assert var_t == var_formula
            checks += 1
            assert mean_ty - mean_t*mean_y == Fraction(2*n-3,12)*var_t
            checks += 1
            assert mean_total == Fraction((n-1)*(n-2),6) + mean_t
            checks += 1
            cases += 1
    print('PASS', 'n=3..7', 'arc cases', cases,
          'complete residual matchings', diagrams, 'exact assertions', checks)


if __name__ == '__main__':
    run()
