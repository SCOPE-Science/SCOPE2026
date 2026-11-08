"""Exact self-contained checks of polar-volume and stationarity identities.

Run with python3 verify.py.  No nonstandard dependencies.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import combinations


def det(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    sign = 1
    value = F(1)
    for i in range(n):
        p = next((j for j in range(i, n) if a[j][i]), None)
        if p is None:
            return F(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            sign *= -1
        v = a[i][i]
        value *= v
        for j in range(i + 1, n):
            q = a[j][i] / v
            for t in range(i + 1, n):
                a[j][t] -= q * a[i][t]
            a[j][i] = F(0)
    return value * sign


def predicted_volume(n, k, s):
    a, b = 1/(1-s), 1/s
    d = k-n*s
    return ((a+b)**n + sum(F(comb(n,j)*(j-k))*a**j*b**(n-j)
                              for j in range(k+1, n+1))/d)/factorial(n)


def volume_by_visible_facets(n,k,s):
    a,b = 1/(1-s),1/s
    d = k-n*s
    apex = [1/d]*n
    total_base = F(0)
    total_apex = F(0)
    for j in range(n+1):
        for subset in combinations(range(n),j):
            P=set(subset)
            vertices = [tuple(a if q==i else F(0) for q in range(n))
                        if i in P else tuple(-b if q==i else F(0) for q in range(n))
                        for i in range(n)]
            total_base += a**j*b**(n-j)/factorial(n)
            functional = F(j) - n*s
            visible = functional/d > 1
            assert visible == (j > k)
            if visible:
                matrix = [[vertices[i][q]-apex[q] for q in range(n)] for i in range(n)]
                total_apex += abs(det(matrix))/factorial(n)
    return total_base+total_apex


def derivative_rational(n,s):
    # For the one-vertex-cut k=n-1: differentiate two rational summands.
    d=n-1-n*s
    B = (s*(1-s))**(-n)
    C = (1-s)**(-n)/d
    return B*(-n*(1-2*s)/(s*(1-s))) + C*(n/(1-s)+n/d)


def stationarity_polynomial(n,s):
    return (1-2*s)*(n-1-n*s)**2 - s**(n+1)*(n-(n+1)*s)


def check():
    checks=0
    for n in range(2,8):
        for k in range(1,n):
            for ratio in [F(1,4),F(2,5),F(3,4)]:
                s=F(k,n)*ratio
                assert predicted_volume(n,k,s) == volume_by_visible_facets(n,k,s)
                checks+=1
    for n in range(3,16):
        for s in [F(1,10),F(1,4),F(2,5),F(49,100)]:
            # Exact equivalence of the derivative-sign and root polynomial.
            d=n-1-n*s
            scale = (s*(1-s))**(-n)*n/(s*(1-s)*d*d)
            assert derivative_rational(n,s)==-scale*stationarity_polynomial(n,s)
            checks+=1
        assert stationarity_polynomial(n,F(0))>0
        assert stationarity_polynomial(n,F(1,2))<0
        checks+=2
    print('EXACT_CHECKS_OK', checks)

if __name__=='__main__':
    check()
