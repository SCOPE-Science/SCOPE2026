#!/usr/bin/env python3
"""Exact checks for the two-endpoint anchored-path sampling formulas.
All computations use Q(sqrt(2)) represented as pairs of Fractions.
Finite checks supplement, rather than replace, the all-order proof.
"""
from fractions import Fraction as F

Z = (F(0), F(0))
ONE = (F(1), F(0))
ROOT2 = (F(0), F(1))

def add(x, y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,t): return (x[0]*t,x[1]*t)
def summ(xs):
    s=Z
    for x in xs: s=add(s,x)
    return s

def check(n, theta):
    assert n >= 2 and 0 <= theta <= 1
    v=[(F(1),F(min(i,n-1-i))) for i in range(n)]
    S=summ(mul(x,x) for x in v)
    p=[Z for _ in range(n+1)]
    if n % 2 == 0:
        m=n//2
        p[0]=summ(v[:m]);p[n]=p[0]
        for j in range(1,m):
            p[j]=mul(ROOT2,summ(v[j:m]))
            p[n-j]=p[j]
        assert p[m] == Z
    else:
        m=n//2
        p[0]=add(summ(v[:m]),scale(v[m],theta))
        p[n]=add(summ(v[:m]),scale(v[m],1-theta))
        for j in range(1,m+1):
            t=summ(v[j:m])
            p[j]=mul(ROOT2,add(t,scale(v[m],theta)))
            p[n-j]=mul(ROOT2,add(t,scale(v[m],1-theta)))
        assert add(p[m],p[m+1]) == mul(ROOT2,v[m])
    assert summ(p) == S, ('normalization',n,theta)
    assert all(float(x[0])+2**.5*float(x[1]) >= 0 for x in p)
    assert p[0] != Z and p[n] != Z
    ans=[Z for _ in range(n)]
    ans[0]=add(ans[0],mul(p[0],v[0]))
    ans[-1]=add(ans[-1],mul(p[n],v[-1]))
    for j in range(1,n):
        flux=scale(mul(p[j],sub(v[j-1],v[j])),F(1,2))
        ans[j-1]=add(ans[j-1],flux)
        ans[j]=sub(ans[j],flux)
    assert ans == v, ('eigenvector identity',n,theta)
    # Verifies all row Rayleigh squares are 1 except the unsampled center
    assert mul(v[0],v[0]) == ONE and mul(v[-1],v[-1]) == ONE
    for j in range(1,n):
        d=sub(v[j-1],v[j]);
        assert scale(mul(d,d),F(1,2)) == (Z if n%2==0 and j==n//2 else ONE)
    return 1

def main():
    k=0
    for n in range(2,101):
        for theta in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            k+=check(n,theta)
    print('VERIFY_OK',k)

if __name__=='__main__': main()
