"""Recovery test: graded-automorphism parameter counts for Markov weighted planes.

For a well-formed weighted projective plane P(w0,w1,w2) with Cox ring
S = k[x0,x1,x2], deg xi = wi, graded automorphisms send xi to a
weighted-homogeneous polynomial of degree wi in variables of weight <= wi.
Counting those monomials (n0+n1+n2 parameters) minus 1 for the grading
torus gives the standard presentation dim Aut(P) = n0+n1+n2-1, and in
particular the explicit unipotent families below already force dim > 2
for every larger Markov triple, refuting the "distinct weights => dim 2"
claim used in WORKLOG Route A.
"""
from itertools import product


def count_mons(usable, d):
    n = 0
    def rec(i, rem):
        nonlocal n
        if i == len(usable) - 1:
            if rem % usable[i] == 0:
                n += 1
            return
        for e in range(rem // usable[i] + 1):
            rec(i + 1, rem - usable[i] * e)
    rec(0, d)
    return n


def dim_aut(weights):
    w = sorted(weights)
    tot = 0
    detail = []
    for wi in w:
        usable = [u for u in w if u <= wi]
        c = count_mons(usable, wi)
        detail.append((wi, usable, c))
        tot += c
    return tot - 1, detail


triples = [(1, 1, 1), (1, 1, 2), (1, 2, 5), (1, 5, 13), (2, 5, 29)]
for t in triples:
    w = [x * x for x in t]
    d, detail = dim_aut(w)
    print(f"Markov {t} -> weights {w} -> dim Aut = {d}")
    for wi, usable, c in detail:
        print(f"    var wt {wi}: {c} coeffs (vars {usable})")
