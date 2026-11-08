#!/usr/bin/env python3
"""Exact, reproducible checks for an RK4 positivity theorem on q-ary Hamming graphs.
Uses only the Python standard library. This script checks identities and examples;
the all-parameter proof is the polynomial/Bernstein argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def spectral_coefficients(d, q):
    assert d >= 3 and q >= 2
    delta = d * (q - 1)
    p = q - 2
    a3 = q*q - 3*q + 3 + 3*(d - 1)*(q - 1)
    a4 = p*(q*q - 2*q + 2) + 10*(d - 1)*p*(q - 1)
    b4 = 6*p*p + 8*(q*q - 3*q + 3) + 12*(d - 2)*(q - 1)
    # P_1(h)=h F1(h); P_2(h)=h*h F2(h).
    f1 = (F(1), -F(delta)+F(p,2),
          F(delta*delta,2)-F(delta*p,2)+F(a3,6),
          -F(delta**3,6)+F(delta*delta*p,4)-F(delta*a3,6)+F(a4,24))
    f2 = (F(1), -F(delta-p), F(delta*delta,2)-F(delta*p)+F(b4,24))
    h3 = F(2, 2*delta-3*p)
    return f1, f2, h3


def horner(coeffs,x):
    acc = F(0)
    for c in reversed(coeffs):
        acc=acc*x+c
    return acc


def bernstein(coeffs,degree):
    from math import comb
    return tuple(sum(F(comb(j,i),comb(degree,i))*coeffs[i]
                     for i in range(j+1)) for j in range(degree+1))


def radial_laplacian(d,q):
    # Independent Hamming distance-regular adjacency-walk recurrence.
    # A row at distance k has k neighbors at k-1, k(q-2) at k,
    # and (d-k)(q-1) at k+1.
    v=[F(int(k==0)) for k in range(5)]
    rows=[v]
    for _ in range(4):
        v=[(k*v[k-1] if k else 0)+k*(q-2)*v[k]+
           ((d-k)*(q-1)*v[k+1] if k<4 else 0)
           for k in range(5)]
        rows.append(v)
    from math import comb
    delta=d*(q-1)
    powers=[[sum(comb(n,i)*delta**(n-i)*(-1)**i*rows[i][k]
                 for i in range(n+1)) for k in range(5)] for n in range(5)]
    return powers


def radial_update(d,q,h):
    powers=radial_laplacian(d,q)
    return [sum((-h)**n*F(powers[n][k],factorial(n))
                for n in range(5)) for k in range(5)]


def brute_update(d,q,h):
    # Direct sparse Laplacian powers of one coordinate delta mass.
    points=list(product(range(q),repeat=d))
    pindex={p:i for i,p in enumerate(points)}
    center=points[0]
    n=len(points)
    v=[F(0)]*n
    v[0]=F(1)
    acc=[F(0)]*n
    deg=d*(q-1)
    for j in range(5):
        t=F((-h)**j,factorial(j))
        acc=[a+t*b for a,b in zip(acc,v)]
        if j==4: break
        vv=[]
        for state in points:
            idx=pindex[state]
            val=deg*v[idx]
            for k in range(d):
                for x in range(q):
                    if x!=state[k]:
                        neighbor=state[:k]+(x,)+state[k+1:]
                        val-=v[pindex[neighbor]]
            vv.append(val)
        v=vv
    return [(sum(acc[pindex[s]] for s in points if
                 sum(x!=y for x,y in zip(s,center))==k),
             sum(sum(x!=y for x,y in zip(s,center))==k for s in points))
            for k in range(min(d,4)+1)]


def certify_formulas():
    checks=0
    for d in range(3,25):
        for q in (2,3,4,5,7,12,13,14,20,31,100):
            f1,f2,h3=spectral_coefficients(d,q)
            for h in (F(0), h3/F(2),h3,F(3,2)*h3):
                r=radial_update(d,q,h)
                assert r[1]==h*horner(f1,h)
                assert r[2]==h*h*horner(f2,h)
                assert r[3]==h**3*(1-h/h3)
                assert r[4]==h**4
                checks+=4
            b1=bernstein(tuple(c*h3**j for j,c in enumerate(f1)),3)
            b2=bernstein(tuple(c*h3**j for j,c in enumerate(f2)),2)
            assert b1[0]==b2[0]==1
            if d==3:
                assert b1[1]==F(4*(q+1),9*q)
                assert b1[2]==F(29*q*q+24*q+12,81*q*q)
                assert b1[3]==F(64-5*q,81*q)
                assert b2[1]==F(q+1,3*q)
                assert b2[2]==F(16,27)
            else:
                u=q-2;v=d-4
                H=(2*v+5)*u+2*v+8
                assert b1[1]==F(4*(u*v+2*u+v+4),3*H)
                assert b1[2]==F(18*u*u*v*v+78*u*u*v+89*u*u+36*u*v*v+228*u*v+332*u+18*v*v+150*v+308,9*H*H)
                C3=8*v**3+48*v*v+90*v+45
                C2=24*v**3+192*v*v+466*v+332
                C1=24*v**3+240*v*v+760*v+740
                C0=8*v**3+96*v*v+384*v+512
                assert b1[3]==F(u**3*C3+u*u*C2+u*C1+C0,3*H**3)
                assert b2[1]==F(u*v+2*u+v+4,H)
                assert b2[2]==F(2*(3*u*u*v*v+15*u*u*v+20*u*u+6*u*v*v+42*u*v+68*u+3*v*v+27*v+56),3*H*H)
            assert all(x>0 for x in b1[:3]+b2)
            assert (b1[3]<0)==(d==3 and q>=13)
            checks+=11
    for d,q,h in [(3,2,F(1,8)),(3,3,F(1,9)),(3,4,F(1,12)),(4,2,F(1,10)),(4,3,F(1,10))]:
        rv=radial_update(d,q,h)
        shell=brute_update(d,q,h)
        for k,(total,size) in enumerate(shell):
            assert total==size*rv[k]
            checks+=1
    # Threshold checks at d=3: sign switch exactly between q=12 and q=13.
    assert spectral_coefficients(3,12)[2]==F(1,18)
    assert spectral_coefficients(3,13)[2]==F(2,39)
    print('VERIFY_OK',checks,'exact coefficient/shell/Bernstein checks')

if __name__ == '__main__':
    certify_formulas()
