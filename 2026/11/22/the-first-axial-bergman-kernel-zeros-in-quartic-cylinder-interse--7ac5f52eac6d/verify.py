#!/usr/bin/env python3
"""Exact rational certificate for the first axial Bergman zero in quartic-cylinder intersections.

Requires only Python 3 standard library. Every root-count decision uses integer
and rational arithmetic; numerical approximations are not used as certificates.
"""
from fractions import Fraction
from math import comb, factorial, prod


def monomial_reciprocal(m, n):
    return prod(n + 2*j + 1 for j in range(m + 1))


def numerator(m):
    """Ascending coefficients of the integer polynomial Q_m."""
    a = [monomial_reciprocal(m, k) for k in range(m + 2)]
    b = [sum((-1)**(j-k) * comb(m+2, j-k) * a[k]
             for k in range(j+1)) for j in range(m+2)]
    assert b[-1] == 0, (m, b[-1])
    return b[:-1]


def cayley_transform(q):
    """R(u)=(1+u)^m Q((1-u)/(1+u)), ascending coefficients."""
    m = len(q)-1
    r = [0]*(m+1)
    for j, value in enumerate(q):
        for a in range(j+1):
            for b in range(m-j+1):
                r[a+b] += value*(-1)**a*comb(j,a)*comb(m-j,b)
    return r


def clean(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_remainder(a, b):
    a = clean(Fraction(x) for x in a)
    b = clean(Fraction(x) for x in b)
    if not b:
        raise ZeroDivisionError()
    while len(a) >= len(b):
        quotient = a[-1]/b[-1]
        offset = len(a)-len(b)
        for j in range(len(b)):
            a[offset+j] -= quotient*b[j]
        a = clean(a)
    return a


def polynomials_coprime(a,b):
    a = clean(a)
    b = clean(b)
    while b:
        a,b = b,poly_remainder(a,b)
    return len(a)==1 and a[0]!=0


def routh_right_half_plane_count(ascending):
    """Exact Routh array. Call only if there are no imaginary-axis roots."""
    d = len(ascending)-1
    if d == 0:
        return 0,'+'
    descending = list(reversed(ascending))
    width = (d+2)//2
    rows = [[Fraction(0) for _ in range(width)] for _ in range(d+1)]
    for j in range(width):
        if 2*j <= d:
            rows[0][j] = Fraction(descending[2*j])
        if 2*j+1 <= d:
            rows[1][j] = Fraction(descending[2*j+1])
    assert rows[0][0] and rows[1][0]
    for i in range(2,d+1):
        assert rows[i-1][0] != 0 and any(rows[i-1]), ('degenerate Routh row',d,i)
        for j in range(width-1):
            rows[i][j] = (rows[i-1][0]*rows[i-2][j+1]
                          - rows[i-2][0]*rows[i-1][j+1]) / rows[i-1][0]
    first=[row[0] for row in rows]
    assert all(x != 0 for x in first)
    signs=''.join('+' if x>0 else '-' for x in first)
    return sum(a!=b for a,b in zip(signs, signs[1:])),signs


def check():
    expected = ['+','++','+++','++++','+++++','++++++',
                '+++++++','++++++++','+++++++++','+++++++ -++'.replace(' ','')]
    counts=[]
    for m in range(10):
        q = numerator(m)
        assert len(q)==m+1 and q[0]>0
        assert all((-1)**j*q[j]>0 for j in range(m+1)), ('alternation',m)
        # Exact generating-function identity in the first 16 coefficients.
        for n in range(16):
            rhs=sum(q[j]*comb(n-j+m+1,m+1) for j in range(min(n,m)+1))
            assert rhs==monomial_reciprocal(m,n),('generating series',m,n)
        r=cayley_transform(q)
        assert len(r)==m+1 and r[-1]>0
        # For u=it, real and imaginary parts are E(t^2), t O(t^2).
        even=[(-1)**j*r[2*j] for j in range((m+2)//2)]
        odd=[(-1)**j*r[2*j+1] for j in range((m+1)//2)]
        if odd:
            assert polynomials_coprime(even,odd),('imaginary root',m)
        assert r[0]!=0
        count,signs=routh_right_half_plane_count(r)
        assert count==(2 if m==9 else 0),('count',m,count)
        assert signs==expected[m],('signs',m,signs,expected[m])
        counts.append(count)
        print('m=%d degree=%d Routh=%s interior_zero_count=%d' % (m,m,signs,count))
    assert numerator(9)==[654729075,-3486128625,8884606500,-14023894500,
                          14939174250,-11039178150,5618913300,
                          -1889187300,379053675,-34459425]
    assert counts==[0]*9+[2]
    print('PASS: 10 exact rational root counts, all boundary and generating-function checks')

if __name__=='__main__':
    check()
