"""Finite exact checks for the star edge-diamond ellipsoid theorem.
Usage: python star_edge_diamond_verify.py
Uses integer/Fraction arithmetic only. Tests support-function identities,
all explicit vertices, the inner and outer ellipsoid barriers, and contacts.
The general proof is mathematical, not inferred from these tests.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def vertices(q):
    out=set()
    for k in range(q+1):
        for subset in combinations(range(q), k):
            for signs in product((-1,1),repeat=k):
                v=[0]*(q+1)
                for j,s in zip(subset,signs):v[j+1]=s
                if k==q:
                    out.add(tuple(v))
                else:
                    for s in (-1,1):
                        v[0]=s*(q-k)
                        out.add(tuple(v))
    return out

def verify(q):
    V=vertices(q)
    assert len(V)==2*3**q-2**q, (q,len(V))
    assert all(sum(map(abs,v))<=q and all(abs(v[j])<=1 for j in range(1,q+1)) for v in V)
    # The minimum enclosing ellipsoid has squared semiaxes q^2,q,...,q.
    for v in V:
        score=F(v[0]**2,q*q)+sum(F(v[j]**2,q) for j in range(1,q+1))
        assert score<=1,(q,v,score)
        touches=(abs(v[0])==q or (v[0]==0 and all(abs(v[j])==1 for j in range(1,q+1))))
        assert (score==1)==touches,(q,v,score)
    assert sum(F(v[0]**2,q*q)+sum(F(v[j]**2,q) for j in range(1,q+1))==1 for v in V)==2+2**q
    if q==1:
        a2=b2=F(1,2)
    else:
        a2=F(q*(q-1));b2=F(1)
    # Inball ellipsoid lies within every signed facet, and leaf slabs.
    assert b2<=1
    assert a2+q*b2<=q*q
    for s in product((-1,1),repeat=q+1):
        assert sum((a2 if j==0 else b2)*s[j]**2 for j in range(q+1))<=q*q
    if q>=2:
        # The q leaf slab contacts and 2^(q+1) signed sum-facet contacts are distinct.
        inner=set()
        for j in range(1,q+1):
            for sign in (-1,1):
                v=[F(0)]*(q+1);v[j]=F(sign);inner.add(tuple(v))
        for signs in product((-1,1),repeat=q+1):
            v=(F((q-1)*signs[0]),)+tuple(F(sign,q) for sign in signs[1:])
            inner.add(v)
            assert sum(map(abs,v))==q
            assert F(v[0]**2,a2)+sum(v[j]**2/b2 for j in range(1,q+1))==1
        assert len(inner)==2*q+2**(q+1)
    # Show no intermediate orbit can touch the outer ellipsoid.
    for k in range(1,q):
        assert F((q-k)**2,q*q)+F(k,q)<1
    return (len(V), 2+2**q, 2*q+2**(q+1) if q>=2 else 4)

if __name__=='__main__':
    for q in range(1,9):
        print(q,verify(q))
    print('PASS: all exact finite consistency checks')
