#!/usr/bin/env python3
"""Exact rational certification of first Fefferman--Szego egg zero threshold.
Run with python3 CHECK.py; requires only the Python standard library.
The analytic kernel reduction and Cohn/Rouche rule are proved in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, gcd


def rising(u, k):
    v = F(1)
    for j in range(k):
        v *= u + j
    return v


def poly(n, m=2):
    """Ascending coefficients of (1-X)^n sum_{b>=0}(mu+b/m)_(n-1)X^b."""
    k = n - 1
    mu = F(n + m, m * (n + 1))
    f = [rising(mu + F(b, m), k) for b in range(k + 1)]
    ans = [F(0)] * (k + 1)
    for j in range(k + 1):
        delta = sum(((-1)**(j-i)) * comb(j, i) * f[i] for i in range(j + 1))
        for h in range(k-j+1):
            ans[j+h] += delta * comb(k-j, h) * (-1)**h
    assert ans[0] > 0 and ans[-1] != 0
    return ans


def divmod_poly(a, b):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    while len(b) > 1 and not b[-1]:
        b.pop()
    if b == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and a != [0]:
        t = a[-1]/b[-1]
        k = len(a)-len(b)
        q[k] = t
        for j, v in enumerate(b):
            a[k+j] -= t*v
        while len(a) > 1 and not a[-1]:
            a.pop()
    return q, a


def coprime(a, b):
    while b != [0]:
        _, r = divmod_poly(a,b)
        a,b=b,r
    return len(a)==1 and a[0]!=0


def cohn(c):
    """Exact Cohn/Schur sequence; positive root count only if no unit roots."""
    c=[F(t,c[0]) for t in c]
    ds=[]
    while len(c)>1:
        d=len(c)-1
        q=c[-1]
        assert abs(q)!=1
        den=1-q*q
        nxt=[(c[i]-q*c[d-i])/den for i in range(d)]
        assert nxt[0]==1 and (d==1 or nxt[-1]!=0)
        ds.append((d,q,abs(q)<1))
        c=nxt
    assert c == [1]
    count=0
    for d,q,lt in reversed(ds):
        count = count if lt else d-count
    return count, ds


def coeff_identity(n, P):
    """Checks 22 exact coefficients of the generating function identity."""
    m=2;k=n-1;mu=F(n+2,2*(n+1))
    # Coeffs of P(X)/(1-X)^n: binomial(n+b-i-1,n-1)
    for b in range(22):
        rhs=sum(P[i]*comb(n+b-i-1,n-1) for i in range(min(b,len(P)-1)+1))
        lhs=rising(mu+F(b,2),k)
        assert rhs==lhs, (n,b)


def verify():
    total=0
    for n in range(2,12):
        p=poly(n)
        coeff_identity(n,p)
        assert coprime(p,list(reversed(p))) # exact boundary-root exclusion
        assert coprime(p, [i*p[i] for i in range(1,len(p))]) # simple roots
        count, ds=cohn(p)
        assert len(ds)==n-1
        assert count==(2 if n==11 else 0)
        if n<=10:
            assert all(u[2] for u in ds)
        else:
            assert [d for d,q,lt in ds if not lt]==[4,2]
        total+=22+len(ds)+4
        print('n=%d: degree=%d, zeros_inside=%d, max_abs_reflection=%.12f, Cohn_flags=%s' % (
            n,n-1,count,max(abs(float(q)) for _,q,_ in ds),
            ''.join('<' if lt else '>' for _,q,lt in ds)))
    print('EXACT_CERTIFICATE_OK; checked assertions=%d (excluding polynomial divisions)'%total)

if __name__=='__main__':
    verify()
