"""Standalone exact tests of first-Johnson-harmonic shell frame formulas.

Standard library only. Finite checks support, but do not prove, the universal theorem.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, isqrt


def claimed(k, t):
    d = 2*t-k
    return (Fraction(2*(2*k-1)*t*(k-t), k*k*(k-1)),
            Fraction((2*k-1)*d*d, k*k))


def column_vectors(k):
    n = 2*k
    vectors = []
    for start in (0, k):
        for i in range(1, k):
            v = [0]*n
            v[start] = -1
            v[start+i] = 1
            vectors.append(v)
    vectors.append([1]*k+[-1]*k)
    return vectors


def matrix_moments(k, level, vectors):
    n = 2*k
    X = list(combinations(range(n), k))
    if level is not None:
        X = [s for s in X if sum(i < k for i in s)==level]
    total = len(X)
    assert total
    m = len(vectors)
    table = [[0]*m for _ in range(m)]
    for x in X:
        values = [sum(v[i] for i in x) for v in vectors]
        for i in range(m):
            for j in range(i+1):
                table[i][j] += values[i]*values[j]
    return [[Fraction(table[max(i,j)][min(i,j)], total) for j in range(m)] for i in range(m)]


counter=0
for k in range(3,8):
    B = column_vectors(k)
    G = matrix_moments(k, None, B)
    n = len(B)
    assert n==2*k-1
    for t in range(k+1):
        M=matrix_moments(k,t,B)
        a,b=claimed(k,t)
        for i in range(n):
            for j in range(n):
                ratio = b if i==n-1 and j==n-1 else a
                if (i==n-1) != (j==n-1):
                    assert G[i][j]==M[i][j]==0
                else:
                    assert M[i][j] == ratio*G[i][j], (k,t,i,j,M[i][j],ratio*G[i][j])
        counter += 1


def kappa(k,d):
    r=Fraction(2*(k-1)*d*d,k*k-d*d)
    return max(r,1/r)


def ds(k):
    return range(1 if k%2 else 2, k, 2)

low_equal=[]
high_equal=[]
for k in range(3,1501):
    res=min(kappa(k,d) for d in ds(k))
    assert res>=1+Fraction(1,2*k+1),(k,res)
    if res==1+Fraction(1,2*k+1):
        low_equal.append(k)
    if res==1+Fraction(1,2*k-2):
        high_equal.append(k)
    if k<200:
        da=min(ds(k),key=lambda d:kappa(k,d))
        assert kappa(k,da)==res
assert low_equal==[2*u*u-1 for u in range(3,isqrt((1501+1)//2)+2,2) if 2*u*u-1<=1500]
assert all(k==2*(isqrt(k//2))**2 for k in high_equal) # Secondary equality may coincide with near-tight choices.
print('JOHNSON_SHELL_EXACT_PASS matrices=%d arithmetic_k=%d lower_equality=%s' % (counter,1498,low_equal))
