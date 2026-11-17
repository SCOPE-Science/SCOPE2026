"""Exact integer checks of product-body Godbersen coefficient envelopes.
Uses no external dependencies and does not substitute for the analytic proof.
"""
from math import comb


def polyconv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def narayana_B(n):
    return [comb(n,j)**2 for j in range(n+1)]


def compositions(n):
    if n==0:
        yield ()
    else:
        for first in range(1,n+1):
            for tail in compositions(n-first): yield (first,)+tail


def check():
    count=0
    for n in range(2,17):
        lo=[comb(n,k) for k in range(n+1)]
        hi=polyconv(narayana_B(1),narayana_B(n-1))
        assert all(hi[k]==comb(n-1,k)**2+comb(n-1,k-1)**2
                   for k in range(n+1) if 1<=k<=n-1)
        for dims in compositions(n):
            if len(dims)<2: continue
            p=[1]
            for d in dims: p=polyconv(p,narayana_B(d))
            assert len(p)==n+1
            for k in range(n+1):
                assert lo[k]<=p[k]<=hi[k], (n,dims,k,p[k],lo[k],hi[k])
                count+=1
            if dims==(1,n-1): assert p==hi
            if all(d==1 for d in dims): assert p==lo
    # Direct test of individual coefficients using actual polygon difference bodies.
    # The triangle, square and asymmetric quadrilateral are exactly calculable.
    # For a planar polygon K, P_K(t)=1+c*t+t^2 with c=area(K-K)/area(K)-2.
    examples={'triangle':[1,4,1], 'square':[1,2,1], 'trapezoid':[1,3,1]}
    # Trapezoid normalized c=3 corresponds to the exact lattice trapezoid
    # conv{(0,0),(3,0),(1,1),(0,1)}: area=2, difference body area=10.
    for a_name,a in examples.items():
        for b_name,b in examples.items():
            q=polyconv(a,b)
            n=4
            low=[comb(n,k) for k in range(n+1)]
            upper=polyconv(narayana_B(1),narayana_B(n-1))
            assert all(low[k]<=q[k]<=upper[k] for k in range(n+1)),(a_name,b_name,q)
            count+=n+1
    return count

if __name__=='__main__':
    print('PASS:',check(),'exact coefficient comparisons')
