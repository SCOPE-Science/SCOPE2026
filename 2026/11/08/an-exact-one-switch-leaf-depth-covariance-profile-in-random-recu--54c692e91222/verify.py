"""Exact reproducibility checks for the depth-profile/leaf-count covariance theorem.

Run: python3 verify.py
Uses only the Python standard library. No external files or network are needed.
"""
from fractions import Fraction
from itertools import product
from math import factorial

TESTS = 0


def eq(actual, expected, label):
    global TESTS
    TESTS += 1
    assert actual == expected, (label, actual, expected)


def pad_sum(a, b):
    return [((a[k] if k < len(a) else 0) +
             (b[k] if k < len(b) else 0))
            for k in range(max(len(a), len(b)))]


def scale(a, c):
    return [v * c for v in a]


def shift(a):
    return [0] + list(a)


def analytic_cov(n):
    assert n >= 2
    if n == 2:
        return [Fraction(0)] * 2
    p = [1]
    for k in range(2, n-1):
        q = [0] * (len(p)+1)
        for j, c in enumerate(p):
            q[j] += k*c
            q[j+1] += c
        p = q
    return [Fraction((n-2)*v, 2*factorial(n-1))
            for v in pad_sum(shift(p), scale(shift(shift(p)), -1))]


def enumerate_tree_cov(n):
    sums = [0]*n
    crosses = [0]*n
    lsum = 0
    total = 0
    for parents in product(*(range(1, k) for k in range(2, n+1))):
        depths = [0]
        child = [0]*n
        for p in parents:
            depths.append(depths[p-1]+1)
            child[p-1] += 1
        l = sum(c == 0 for c in child)
        hist = [0]*n
        for d in depths:
            hist[d] += 1
        for d in range(n):
            sums[d] += hist[d]
            crosses[d] += hist[d]*l
        lsum += l
        total += 1
    eq(total, factorial(n-1), ('tree count',n))
    return [Fraction(c,total)-Fraction(s*lsum,total*total)
            for s,c in zip(sums,crosses)]


def recurrence_covariances(stop):
    # A=E[sum(z**depth)]; B=E[sum_leaves(z**depth)];
    # M=E[(sum(z**depth))*total_leaves]; ell=E[total_leaves].
    A = [Fraction(1)]
    B = [Fraction(1)]
    M = [Fraction(1)]
    ell = Fraction(1)
    for n in range(1, stop):
        nF = Fraction(n)
        newA = pad_sum(A, scale(shift(A), Fraction(1,n)))
        newB = pad_sum(scale(B, 1-Fraction(1,n)), scale(shift(A), Fraction(1,n)))
        newM = pad_sum(
            pad_sum(scale(M, 1-Fraction(1,n)), scale(shift(M), Fraction(1,n))),
            pad_sum(newA, scale(shift(B), -Fraction(1,n))))
        newell = (1-Fraction(1,n))*ell+1
        A,B,M,ell = newA,newB,newM,newell
        cov = pad_sum(M, scale(A,-ell))
        target = analytic_cov(n+1)
        for j in range(n+1):
            eq(cov[j], target[j], ('recurrence',n+1,j))


def main():
    # Independent enumeration of all labelled increasing trees through order ten.
    for n in range(2,11):
        got = enumerate_tree_cov(n)
        want = analytic_cov(n)
        for j in range(n):
            eq(got[j], want[j], ('enumeration',n,j))
    recurrence_covariances(65)
    for n in range(3,251):
        coeff = analytic_cov(n)
        eq(len(coeff), n, ('polynomial length',n))
        eq(coeff[0], 0, ('root constant',n))
        eq(sum(coeff), 0, ('total vertex count deterministic',n))
        eq(sum(Fraction(j)*v for j,v in enumerate(coeff)),
           Fraction(-(n-2),4), ('path length covariance',n))
        eq(coeff[1], Fraction(n-2,2*(n-1)), ('root degree covariance',n))
        eq(sum(((-1)**j)*v for j,v in enumerate(coeff)),
           Fraction(-1,n-1), ('depth parity covariance',n))
        signs = [0 if x==0 else (1 if x>0 else -1) for x in coeff[1:]]
        eq(signs[0],1,('positive shallow level',n))
        eq(signs[-1],-1,('negative deepest level',n))
        eq(sum(signs[j] > signs[j-1] for j in range(1,len(signs))),
           0, ('nonincreasing signs',n))
        eq(signs.count(0) <= 1, True, ('at most one zero',n))
    print('PASS: %s exact comparisons; exhaustive trees n=2..10; recurrences n=2..65; sign laws n=3..250.' % TESTS)

if __name__ == '__main__':
    main()
