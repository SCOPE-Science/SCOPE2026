#!/usr/bin/env python3
"""Exact arithmetic checks for lattice-polygon prism Ehrhart numerators.

The theorem's infinite proof uses Pick's formula, Wagner's product theorem,
and symbolic discriminant identities; finite parameter tests are supplementary.
"""
from math import comb


def padd(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out


def pneg(a): return [-x for x in a]

def pscale(a, n): return [n*x for x in a]

def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def cubdisc(c0, c1, c2, c3):
    # Discriminant of c3*t^3+c2*t^2+c1*t+c0; inputs are polynomials in q.
    return padd(padd(pscale(pmul(pmul(c2,c2),pmul(c1,c1)),1),
                      pscale(pmul(c3,pmul(c1,pmul(c1,c1))),-4)),
                padd(padd(pscale(pmul(pmul(c2,pmul(c2,c2)),c0),-4),
                          pscale(pmul(pmul(c3,c3),pmul(c0,c0)),-27)),
                     pscale(pmul(pmul(c3,c2),pmul(c1,c0)),18)))


def coeff(I, B, m):
    a = I + B - 3
    return (1, (m+1)*a+3*m-1, (2*m-1)*a+(2*m+1)*I, (m-1)*I)


def disc(I, B, m):
    c0, c1, c2, c3 = coeff(I,B,m)
    if c3: return c1*c1*c2*c2 - 4*c2**3 - 4*c1**3*c3 - 27*c3*c3 + 18*c1*c2*c3
    if c2: return c1*c1 - 4*c2
    return 1


def ehrhart_poly_count(I, B, m, n):
    twice_area = 2*I+B-2
    return ((twice_area*n*n+B*n+2)//2)*(m*n+1)


def ehrhart_from_hstar(c, n):
    return sum(c[j]*comb(n+3-j,3) for j in range(4) if n+3-j>=3)


def verify():
    # Exact symbolic expansion of all discriminants in q=m-1 for
    # the three non-real-rooted planar inputs.
    expected = {
        1: [0,288,549,288,0],
        2: [256,2304,4180,2832,600],
        3: [2304,10560,16317,10800,2592],
    }
    for k, ex in expected.items():
        # m=q+1; a=k, c1=(k+3)q+(2k+2),
        # c2=4k(q+1), c3=k*q.
        c1 = [2*k+2, k+3]
        c2 = [4*k, 4*k]
        c3 = [0, k]
        got = cubdisc([1],c1,c2,c3)
        got += [0]*(5-len(got))
        assert got == ex, (k,got,ex)
        for m in range(1,60):
            val = sum(v*(m-1)**j for j,v in enumerate(ex))
            if m==1:  # cubic leading coefficient vanishes at height one
                val = val//coeff(k,3,m)[2]**2
            assert disc(k,3,m)==val, (k,m,val,disc(k,3,m))
    exact_tests = 0
    for I in range(0,42):
        for B in range(3,31):
            base_discriminant = (I+B-3)**2-4*I
            assert (base_discriminant < 0) == (B==3 and 1<=I<=3)
            for m in range(1,21):
                c = coeff(I,B,m)
                assert c[0] == 1 and all(x>=0 for x in c)
                assert disc(I,B,m)>=0,(I,B,m,disc(I,B,m))
                for n in range(0,5):
                    assert ehrhart_from_hstar(c,n)==ehrhart_poly_count(I,B,m,n),(I,B,m,n)
                    exact_tests += 1
    # Nontrivial polygon with base numerator having nonreal zeros:
    # P=conv((0,0),(1,0),(2,3)), I=1, B=3, base h*=1+t+t^2.
    assert coeff(1,3,1)==(1,4,4,0)  # squared numerator
    assert coeff(1,3,2)==(1,8,8,1)
    print('PASS: all three symbolic discriminant identities; ' +
          str(exact_tests) + ' exact Ehrhart and root-discriminant grid checks')

if __name__ == '__main__': verify()
