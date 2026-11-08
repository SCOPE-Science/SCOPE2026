"""Exact finite diagnostics for the real ternary Haar sign-multiplier theorem.

Usage: python checker.py
Only standard-library rational arithmetic is used. Finite checks are not a proof
for arbitrary depth; the all-depth argument is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache

A = ((F(3,2), F(-3,2), F(0)),
     (F(-3,2), F(3,2), F(0)),
     (F(0), F(0), F(0)))
B = ((F(1,2), F(1,2), F(-1)),
     (F(1,2), F(1,2), F(-1)),
     (F(-1), F(-1), F(2)))


def closed(depth, z):
    z = abs(F(z))
    assert 0 <= z <= 1
    if depth == 0:
        return z
    if z <= F(1,2):
        return depth + F(1,2) + (z-F(1,2))/3**depth
    return depth + F(1,6) + F(2,3)*z + (1-2*z)/F(2*3**depth)


@lru_cache(None)
def bellman(depth, z):
    if depth == 0:
        return abs(z)
    candidates = []
    for i in range(3):
        for s in (-1,1):
            for t in (-1,1):
                v = [s*A[i][j] + t*B[i][j] for j in range(3)]
                siblings = sum((abs(z+v[j]) for j in range(3) if j != i),F(0))/3
                candidates.append(siblings + bellman(depth-1, (z+v[i])/3))
    return max(candidates)


def direct_rows(depth):
    leaves = list(product(range(3), repeat=depth))
    best = []
    for x in leaves:
        top = F(-1)
        for signs in product((-1,1), repeat=2*depth):
            total = F(0)
            for y in leaves:
                val = F(1)
                for ell in range(depth):
                    if x[:ell] != y[:ell]:
                        break
                    val += 3**ell*(signs[2*ell]*A[x[ell]][y[ell]] + signs[2*ell+1]*B[x[ell]][y[ell]])
                total += abs(val)
            top = max(top,total/3**depth)
        best.append(top)
    return dict(zip(leaves,best))


def main():
    comparisons=0
    for m in range(1,7):
        for j in range(-18,19):
            z=F(j,18)
            value=bellman(m,z)
            assert value == closed(m,z),(m,z,value,closed(m,z))
            comparisons+=1
    print('EXACT_INDEPENDENT_BELLMAN_BRANCH_CHECKS_PASSED', comparisons)
    checked=0
    for d in range(1,5):
        rows=direct_rows(d)
        predicted=closed(d,1)
        assert max(rows.values())==predicted
        norming={leaf for leaf,value in rows.items() if value==predicted}
        expected={leaf for leaf in rows if all(letter in (0,1) for letter in leaf[1:-1])}
        assert norming==expected,(d,norming,expected)
        checked+=len(rows)
        print('DEPTH',d,'NORM',str(predicted),'MAXIMIZING_LEAVES',len(norming))
    print('EXACT_FULL_KERNEL_ROW_SEARCHES_PASSED',checked)
    print('ALL_TERNARY_HAAR_ENDPOINT_CHECKS_PASSED')

if __name__=='__main__':
    main()
