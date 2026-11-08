#!/usr/bin/env python3
"""Exact rational checks for the K_{2,q} polar Ehrhart magic-basis theorem."""
from fractions import Fraction as F
from math import comb


def ehrhart_value(q, t):
    assert q >= 1 and t >= 0
    return (2*t + 1)**q + 2*sum(s**q for s in range(1,2*t+1))


def multiply_linear(p, c):
    out=[F(0)]*(len(p)+1)
    for k,v in enumerate(p):
        out[k] += c*v
        out[k+1] += v
    return out


def magic_coefficients(q):
    d=q+1
    vals=[ehrhart_value(q,t) for t in range(d+1)]
    differences=[]
    while vals:
        differences.append(vals[0])
        vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
    power=[F(0)]*(d+1)
    basis=[F(1)]
    for j in range(d+1):
        for i,c in enumerate(basis):
            power[i] += differences[j]*c
        if j<d:
            basis=[v/F(j+1) for v in multiply_linear(basis, -j)]
    a=[]
    for k in range(d+1):
        a.append(power[k] - sum(a[i]*comb(d-i,k-i) for i in range(k)))
    # Verify the complete basis identity at two additional points.
    for t in [d+1,d+2]:
        assert sum(a[i]*t**i*(t+1)**(d-i) for i in range(d+1)) == ehrhart_value(q,t)
    assert all(a[i]==a[d-i] for i in range(d+1))
    return a


def bernoulli(n):
    vals=[F(1)]
    for m in range(1,n+1):
        vals.append(-sum(F(comb(m+1,k))*vals[k] for k in range(m))/F(m+1))
    return vals[n]


def main():
    checks=0
    # Complete low-parameter positivity and the six middle-range obstruction certificates.
    for q in range(1,15):
        a=magic_coefficients(q)
        if q<=8:
            assert all(c>0 for c in a)
        else:
            i={9:5,10:5,11:6,12:6,13:4,14:5}[q]
            expected={9:F(-144,5),10:F(-598,11),11:F(-892,3),
                      12:F(-262324,455),13:F(-27967,105),14:F(-21971,15)}[q]
            assert a[i]==expected and a[i]<0, (q,i,a[i])
        checks+=len(a)
    assert bernoulli(14)==F(7,6)
    assert bernoulli(16)==F(-3617,510)
    assert bernoulli(18)==F(43867,798)
    checks+=3
    # Exact starting inequalities for the four residue classes; from the
    # Euler formula and zeta bounds, |B_{j+2}|>3|B_j| for every even j>=14.
    assert bernoulli(14)>F(15-5,24)
    assert -bernoulli(16)>F(16-1,4)
    assert -bernoulli(16)>F(17-3,8)
    assert bernoulli(18)>F(18-3,8)
    checks+=4
    # Check the first several obstruction formulas against exact full expansion.
    for q in range(15,33):
        a=magic_coefficients(q)
        if q%4==0:
            i=1; predicted=F(q-1)+4*bernoulli(q)
        elif q%4==1:
            i=2; predicted=F(q)*(F(q-3,2)+4*bernoulli(q-1))
        elif q%4==2:
            i=2; predicted=F(q)*(F(q-3,2)-4*bernoulli(q))
        else:
            i=3; predicted=F(q*(q-1),6)*(q-5-24*bernoulli(q-1))
        assert a[i]==predicted and predicted < 0, (q,i,a[i],predicted)
        checks+=2
    print('VERIFY_OK', checks, 'exact rational checks')
    print('positive low range q=1..8; negative finite range q=9..14; analytic four-residue threshold q>=15')

if __name__=='__main__':
    main()
