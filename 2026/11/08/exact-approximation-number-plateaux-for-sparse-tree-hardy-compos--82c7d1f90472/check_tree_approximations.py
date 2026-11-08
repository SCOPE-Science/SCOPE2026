#!/usr/bin/env python3
"""Finite, reproducible checks of sparse level-copy composition formulas.

This checker is not a proof of the infinite-dimensional assertion.
It uses only Python's standard library and exact Fraction arithmetic.
"""
from fractions import Fraction
from random import Random

rng = Random(314159)
checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def c(q, n):
    return 1 if n == 0 else (q + 1) * q ** (n - 1)

def normpower(f, q, p):
    levels = {v[0] for v in f}
    return max([Fraction(0), *[sum(abs(f.get((n, i), 0)) ** p for i in range(c(q, n))) / c(q, n)
                        for n in levels]])

def test_case(q, a, b, p, J):
    pairs = [(a * j, (a + b) * j) for j in range(1, J + 1)]
    inputs = {0, *(m for m, n in pairs)}
    f = {(0, 0): rng.randint(-3, 3)}
    for m, n in pairs:
        for i in range(c(q, m)):
            f[(m, i)] = rng.randint(-3, 3)
    def images_at_level(n):
        for m, nn in pairs:
            if n == nn:
                return [f[(m, i)] if i < c(q, m) else f[(0, 0)]
                        for i in range(c(q, n))]
        return [f[(0, 0)] for _ in range(c(q, n))]
    input_norm = normpower(f, q, p)
    out_norm = abs(f[(0, 0)])**p
    for m, n in pairs:
        out_vals = images_at_level(n)
        actual = Fraction(sum(abs(x)**p for x in out_vals), c(q, n))
        t = Fraction(c(q, m), c(q, n))
        mp = Fraction(sum(abs(f[(m, i)])**p for i in range(c(q, m))), c(q, m))
        predicted = t * mp + (1-t) * abs(f[(0, 0)])**p
        check(actual == predicted, 'level identity')
        check(actual <= input_norm, 'contractive')
        out_norm = max(out_norm, actual)
        # Exact norm of the copied block and exact rank.
        check(c(q, m) < c(q, n), 'proper sparse injection')
        check(t == Fraction(1, q**(n-m)), 'weight identity')
    check(out_norm <= input_norm, 'global contraction')
    return pairs

for q, a, b, p, jmax in [(2,1,1,1,4),(2,1,1,2,4),(2,2,1,2,3),(3,1,1,3,3),(3,1,2,2,2)]:
    for sample in range(30):
        pairs = test_case(q, a, b, p, jmax)
    Js = [0]
    for j, (m,n) in enumerate(pairs, 1):
        Js.append(Js[-1] + c(q, m))
        check(Js[-1] == sum(c(q, a*i) for i in range(1,j+1)), 'multiplicity')
        check(Js[-1] == Fraction((q+1)*q**(a-1)*(q**(a*j)-1), q**a-1), 'geometric count')
    # Exact plateau multiplicities, including the rank-one initial term.
    weights = [Fraction(1)]
    for j, (m,n) in enumerate(pairs, 1):
        weight_p = Fraction(1, q**(b*j))
        weights += [weight_p]*c(q, m)
        check(all(x == weight_p for x in weights[Js[j-1]+1:Js[j]+1]), 'plateau')
    check(len(weights) == 1 + Js[-1], 'total multiplicity')
    check(all(weights[i]>=weights[i+1] for i in range(len(weights)-1)), 'monotonic')
    for r in range(1, 8):
        # Integral p/r choices are not needed for the exact exponent condition.
        check((a - Fraction(b*r,p) < 0) == (r > Fraction(a*p,b)), 'threshold')

# Generic nonmonotone depth-gap case: sorting with full block multiplicities.
q=2
pairs=[(1,5),(2,4),(3,10)]
mult=[]
for m,n in pairs:
    mult.extend([Fraction(1,q**(n-m))]*c(q,m))
rearranged=sorted(mult,reverse=True)
check(len(rearranged)==sum(c(q,m) for m,n in pairs), 'generic multiplicity')
check(rearranged[0]==Fraction(1,4), 'nonmonotone sorting')
check(rearranged[-1]==Fraction(1,128), 'smallest block weight')
print(f'TREE_SPARSE_COPY_EXACT_FINITE_OK {checks}')
