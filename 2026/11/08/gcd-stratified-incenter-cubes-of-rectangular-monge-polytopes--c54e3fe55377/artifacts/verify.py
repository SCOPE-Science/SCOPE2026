"""Reproducible exact certificates for rectangular normalized Monge inballs.

Run: python artifacts/verify.py
Core checks require Python standard library. If SciPy/Numpy are installed,
an independent numerical LP optimization of the ambient Frobenius inradius runs.
"""
from fractions import Fraction as F
from math import ceil, gcd, sqrt
from itertools import product


def construction(p, q, endpoint=None):
    """Optimal dual potentials; endpoint controls common-boundary cube variables."""
    if endpoint is None:
        endpoint = [F(1,2)] * (gcd(p,q)-1)
    g=gcd(p,q)
    assert len(endpoint)==g-1
    b=[F(0)]
    for j in range(1,q):
        x=F(p*j,q)
        if x.denominator==1:
            k=j*g//q
            assert j*g % q==0 and 1<=k<g
            t=F(endpoint[k-1])
            assert 0<=t<=1
            theta=x+t
        else:
            theta=F(ceil(x))
        b.append(b[-1]+theta)
    a=[max(F(i*j)-b[j-1] for j in range(1,q+1)) for i in range(1,p+1)]
    d=[[a[i-1]+b[j-1]-i*j for j in range(1,q+1)] for i in range(1,p+1)]
    return d


def support(p,q):
    return {(i,j) for i in range(1,p+1) for j in range(1,q+1)
            if max(F(i-1,p),F(j-1,q)) < min(F(i,p),F(j,q))}


def check(p,q,end=None):
    d=construction(p,q,end)
    g=gcd(p,q)
    weights=sum(min(a*q,b*p)-a*b for a in range(1,p) for b in range(1,q))
    assert 12*weights == p*p*q*q-p*p-q*q+g*g,(p,q)
    assert all(x>=0 for row in d for x in row),(p,q,'negative')
    assert all(d[i][j+1]+d[i+1][j]-d[i][j]-d[i+1][j+1]==1
               for i in range(p-1) for j in range(q-1)),(p,q,'slack')
    assert sum(map(sum,d))==weights,(p,q,'mass')
    sup=support(p,q)
    assert len(sup)==p+q-g
    zero={(i,j) for i in range(1,p+1) for j in range(1,q+1) if d[i-1][j-1]==0}
    assert sup <= zero
    expect=len(sup) + (sum(t in (0,1) for t in end) if end is not None else 0)
    assert len(zero)==expect,(p,q,zero,sup,expect)
    # Distributional coupling identity for independently chosen random entries
    # vs a single uniform quantile, with arbitrary d (not only equality arrays).
    mass=sum(map(sum,d))
    joint=sum(d[i-1][j-1]*max(F(0),min(F(i,p),F(j,q))-
                                            max(F(i-1,p),F(j-1,q)))
              for i in range(1,p+1) for j in range(1,q+1))
    assert joint==0
    assert mass==p*q*joint+sum((min(a*q,b*p)-a*b)*
                              (d[a-1][b]+d[a][b-1]-d[a-1][b-1]-d[a][b])
                              for a in range(1,p) for b in range(1,q))
    return len(sup),weights


def run():
    cases=0
    for p in range(2,26):
        for q in range(2,26):
            check(p,q)
            cases+=1
    corner_checks=0
    for p in range(2,13):
        for q in range(2,13):
            g=gcd(p,q)
            for bits in product((F(0),F(1)),repeat=g-1):
                check(p,q,bits)
                corner_checks+=1
    lp_cases=0
    try:
        import numpy as np
        from scipy.optimize import linprog
    except ImportError:
        print('Optional SciPy LP check unavailable; exact checks completed.')
    else:
        for p in range(2,10):
            for q in range(2,10):
                n=p*q
                alpha=sqrt(1-1/n)
                A=[]
                for k in range(n):
                    row=np.zeros(n+1)
                    row[k]=-1
                    row[-1]=alpha
                    A.append(row)
                for i in range(p-1):
                    for j in range(q-1):
                        row=np.zeros(n+1)
                        row[i*q+j]=1
                        row[(i+1)*q+j+1]=1
                        row[i*q+j+1]=-1
                        row[(i+1)*q+j]=-1
                        row[-1]=2
                        A.append(row)
                obj=np.zeros(n+1); obj[-1]=-1
                equality=np.zeros((1,n+1));equality[0,:n]=1
                sol=linprog(obj,A_ub=A,b_ub=np.zeros(len(A)),A_eq=equality,b_eq=[1],
                            bounds=[(None,None)]*(n+1),method='highs')
                assert sol.success,(p,q,sol.message)
                g=gcd(p,q)
                denominator=n*alpha+(p*p*q*q-p*p-q*q+g*g)/6
                expected=1/denominator
                assert abs(sol.x[-1]-expected)<3e-8,(p,q,sol.x[-1],expected)
                lp_cases+=1
    print('RECT_MONGE_INBALL_CHECKS_PASSED exact_pairs=%d corner_profiles=%d independent_lp=%d'
          %(cases,corner_checks,lp_cases))

if __name__=='__main__':run()
