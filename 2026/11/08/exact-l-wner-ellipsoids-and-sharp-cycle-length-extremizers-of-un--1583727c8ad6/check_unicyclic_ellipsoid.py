"""Exact rational checks for Löwner ellipsoids of unicyclic graphical zonotopes.

Requires Python 3 and SymPy.  This script is finite corroboration, not a proof.
"""
from itertools import product, combinations
from math import comb
from fractions import Fraction
import sympy as S


def graphs(n,k):
    base=[(j,(j+1)%k) for j in range(k)]
    b=n-k
    if not b: return [base]
    return [base+[(j,0) for j in range(k,n)],
            base+[(j,j-1) for j in range(k,n)],
            base+[(j, (j-k)%k) for j in range(k,n)]]


def check(n,k,edges):
    assert len(edges)==n and len(set(tuple(sorted(x)) for x in edges))==n
    d=n-1; b=n-k; q=(k*k)//4
    B=S.zeros(n,n)
    for j,(u,v) in enumerate(edges):
        B[u,j]=1;B[v,j]=-1
    assert B.rank()==d
    sb=S.Rational(d,4)
    sc=S.Rational(d*q,k*(k-1))
    D=S.diag(*([sc]*k+[sb]*b))
    M=B*D*B.T
    assert M.rank()==d
    N=S.ones(n,n)/n
    Minv=(M+N).inv()-N
    assert M*Minv*M==M
    assert (M[:n-1,:n-1].det() == k*sb**b*sc**(k-1))
    contact=set(); vert=set(); allsigns=0
    cert_mean=S.zeros(n,1); cert_cov=S.zeros(n,n)
    balanced=[]
    for z in product((-1,1),repeat=k):
        if abs(sum(z))==k%2: balanced.append(z)
    assert len(balanced)== (comb(k,k//2) if k%2==0 else 2*comb(k,k//2))
    for bridge in product((-1,1),repeat=b):
        for cyc in product((-1,1), repeat=k):
            s=S.Matrix(cyc+bridge)
            x=B*s/2
            v=(x.T*Minv*x)[0]
            assert v<=1,(n,k,edges,cyc,bridge,v)
            eq = v==1
            assert eq==(cyc in balanced),(n,k,eq,cyc)
            if 0<sum(zz==1 for zz in cyc)<k:
                vert.add(tuple(x))
                if eq: contact.add(tuple(x))
            allsigns+=1
        for cyc in balanced:
            x=B*S.Matrix(cyc+bridge)/2
            cert_mean+=x
            cert_cov+=x*x.T
    count=len(balanced)*(2**b)
    assert len(vert)==(2**k-2)*(2**b)
    assert len(contact)==count
    assert cert_mean==S.zeros(n,1)
    assert cert_cov/count==M/d
    return len(vert),len(contact),allsigns


def main():
    case=0; contact=0; signs=0
    for n in range(3,9):
        for k in range(3,n+1):
            for E in graphs(n,k):
                a,z,s=check(n,k,E)
                case+=1;contact+=z;signs+=s
    # Direct exact monotonic comparisons of full formula squared, 3 <= k <= 40.
    from math import floor
    for k in range(3,40):
        # monotonic squared F(k) via exact fractions
        F=lambda j: S.Rational(j,1)*(S.Rational(4*(j*j//4),j*(j-1)))**(j-1)
        assert F(k+1)>F(k), k
    print('UNICYCLIC_GRAPHICAL_ZONOTOPE_LOEWNER_CHECKS_PASSED',case,contact,signs)


if __name__=='__main__': main()
