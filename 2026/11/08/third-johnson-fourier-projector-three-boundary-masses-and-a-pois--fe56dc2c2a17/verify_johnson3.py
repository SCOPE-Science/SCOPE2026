#!/usr/bin/env python3
"""Exact rational checks for third-degree Johnson Fourier projector kernels.

Run with Python 3.9 or later; only the standard library is required.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial


def falling(x, r):
    z = 1
    for t in range(r):
        z *= x - t
    return z


def linear_solve(a, b):
    m = [list(row) + [bb] for row, bb in zip(a, b)]
    n = len(b)
    for col in range(n):
        p = next(r for r in range(col, n) if m[r][col])
        m[col], m[p] = m[p], m[col]
        c = m[col][col]
        m[col] = [v / c for v in m[col]]
        for r in range(n):
            if r == col:
                continue
            c = m[r][col]
            m[r] = [x - c*y for x,y in zip(m[r],m[col])]
    return [m[i][-1] for i in range(n)]


def third_kernel(n,k):
    assert n >= 2*k and k >= 3
    w = [comb(k,j)*comb(n-k,k-j) for j in range(k+1)]
    total = comb(n,k)
    def mom(r):
        return Q(falling(k,r)**2, falling(n,r))
    def gm(a,b):
        return sum((Q(comb(a,l)*comb(b,l)*factorial(l))*mom(a+b-l)
                    for l in range(min(a,b)+1)),Q())
    a = [[gm(r,t) for t in range(3)] for r in range(3)]
    v = [-gm(r,3) for r in range(3)]
    c0,c1,c2 = linear_solve(a,v)
    coeffs = [c0,c1,c2,Q(1)]
    h = [sum(coeffs[r]*falling(j,r) for r in range(4)) for j in range(k+1)]
    dim = comb(n,3)-comb(n,2)
    ker = [Q(dim)*x/h[k] for x in h]
    assert ker[k] == dim
    # Exact orthogonality and the projector's squared reproducing kernel norm.
    for r in range(3):
        assert sum(Q(w[j])*h[j]*falling(j,r) for j in range(k+1)) == 0
    assert sum(Q(w[j],total)*ker[j]**2 for j in range(k+1)) == dim
    b2 = Q(1,n-2)
    b1 = (c2-3 + b2*(k*k-4*k+2*n-1))/Q(n-1)
    b0 = -c0/Q(k*k)
    def bound(j):
        if j < 0 or j == k:
            return Q(0)
        return Q(w[j])*(k-j)**2*(b0+b1*j+b2*j*j)
    for j in range(k+1):
        assert Q(w[j])*h[j] == bound(j-1)-bound(j)
    # Negative-value intervals are located by exact rational signs, without
    # using numerical root finding. A real cubic orthogonal polynomial has
    # three simple roots and at most two negative intervals on its support.
    neg_runs = []
    st = None
    for j in range(k+2):
        negative = j <= k and h[j] < 0
        if negative and st is None:
            st = j
        if not negative and st is not None:
            neg_runs.append((st,j-1))
            st = None
    assert len(neg_runs) <= 2
    direct = sum(Q(w[j],total)*abs(ker[j]) for j in range(k+1))
    boundary = Q(2*dim, total*h[k])*sum((bound(r)-bound(l-1) for l,r in neg_runs),Q(0))
    assert direct == boundary and direct >= 1
    return ker,direct,coeffs,boundary


def exact_projector_matrix(n,k):
    xs = list(combinations(range(n),k))
    ker,norm,_,_ = third_kernel(n,k)
    size = len(xs)
    entries = [[ker[len(set(x)&set(y))]/size for y in xs] for x in xs]
    assert all(sum(row) == 0 for row in entries)
    # Test actual idempotence on every matrix coordinate.
    for i in range(size):
        for j in range(size):
            assert sum(entries[i][h]*entries[h][j] for h in range(size)) == entries[i][j]
    return size,norm


def poisson_charlier(la, bound=200):
    # Approximation only, independent of the exact finite-dimensional tests.
    from math import exp
    p = exp(-la)
    val = 0.0
    for j in range(bound):
        c = (j*(j-1)*(j-2) - 3*la*j*(j-1) + 3*la*la*j - la**3)
        val += p*abs(c)
        p *= la/(j+1)
    return val/(6*la**1.5)


def main():
    count=0
    for n in range(6,61):
        for k in range(3,n//2+1):
            third_kernel(n,k)
            count += 1
    matrices=[]
    for n,k in [(6,3),(7,3),(8,3)]:
        matrices.append(exact_projector_matrix(n,k)[0])
    import math
    c = math.sqrt(3)
    f=lambda x: poisson_charlier(x*x)
    h=1e-5
    jump=(f(c+h)-2*f(c)+f(c-h))/h
    assert abs(jump-6*math.exp(-3)) < 0.001
    bulk=math.sqrt(2/math.pi)*(1+4*math.exp(-1.5))/6
    assert abs(poisson_charlier(100, bound=300)-bulk)<0.008
    print('JOHNSON_THIRD_ENDPOINT_CHECKS_PASS exact_cases=%d matrices=%s cusp=%.8f bulk=%.8f' % (count, matrices, jump, bulk))

if __name__ == '__main__':
    main()
