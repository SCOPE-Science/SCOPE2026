#!/usr/bin/env python3
"""Exact moment calculation for complex-projective first-harmonic cap restriction.
Pure Python 3, no external package. Runs a finite consistency check; the proof is analytic.
"""
from fractions import Fraction as Q


def gram(dim, threshold):
    """Gram matrices in the basis E_ij (i!=j), E_ii-E_(d-1,d-1)."""
    d=dim; n=d-1; s=1-threshold
    # distribution of y=1-|u_0|^2: density n*y^(n-1) on [0,1].
    def moment(k): return Q(n,n+k)*s**(n+k)
    EY0,EY1,EY2=moment(0),moment(1),moment(2)
    xx=EY0-2*EY1+EY2
    xy=(EY1-EY2)/n
    yy_diff=EY2/Q(n*(n+1))
    yy_same=2*yy_diff
    def M(i,j):
        if i==j==0:return xx
        if i==0 or j==0:return xy
        return yy_same if i==j else yy_diff
    basis=[(i,j) for i in range(d) for j in range(d) if i!=j]
    basis += [(i,i) for i in range(d-1)]
    m=len(basis)
    G=[[Q(0) for _ in range(m)] for _ in range(m)]
    for a,(i,j) in enumerate(basis):
        for b,(k,l) in enumerate(basis):
            if i!=j and k!=l:
                if i==k and j==l:G[a][b]=M(i,j)
            elif i==j and k==l:
                r=d-1
                G[a][b]=M(i,k)-M(i,r)-M(r,k)+M(r,r)
    return basis,G


def qform(G, x, y):
    return sum((a*b*G[i][j] for i,a in enumerate(x) if a for j,b in enumerate(y) if b),Q(0))

def verify(d,t):
    basis,G=gram(d,t)
    _,H=gram(d,Q(0))
    # Fourier-side traceless matrices split into three invariant subspaces:
    # axial, cross, and tangential traceless.
    m=len(basis); idx={b:i for i,b in enumerate(basis)}
    def unit_pair(items):
        v=[Q(0)]*m
        for pos,coef in items:v[idx[pos]]+=Q(coef)
        return v
    axial=unit_pair([((0,0),d-1)]+[((i,i),-1) for i in range(1,d-1)])
    # This encodes diag(d-1,-1,...,-1) in the trace-zero diagonal basis.
    cross=[unit_pair([((i,j),1)]) for i in range(d) for j in range(d) if (i==0) != (j==0)]
    tangent=[unit_pair([((i,j),1)]) for i in range(1,d) for j in range(1,d) if i!=j]
    tangent += [unit_pair([((k,k),1)]+([((k+1,k+1),-1)] if k+1<d-1 else [])) for k in range(1,d-1)]
    sectors=[('axial',[axial],(1-t)**(d-1)*(1-2*t+d*d*t*t)),
             ('cross',cross,(1-t)**d*(1+d*t)),
             ('tangent',tangent,(1-t)**(d+1))]
    vecs=[]
    for name,B,lam in sectors:
        for v in B:
            assert qform(H,v,v)>0,(d,t,name)
            for w in B:
                assert qform(G,v,w)==lam*qform(H,v,w),(d,t,name)
        vecs.extend((name,v) for v in B)
    assert len(vecs)==d*d-1
    for i,(name,v) in enumerate(vecs):
        for other,w in vecs[i+1:]:
            if name!=other:
                assert qform(H,v,w)==0 and qform(G,v,w)==0,(d,t,name,other)
    # Multiplicities 1,2(d-1),d(d-2); normalized trace equals cap measure.
    a,b,c=[p[2] for p in sectors]
    assert a+2*(d-1)*b+d*(d-2)*c==(d*d-1)*(1-t)**(d-1)
    assert a-c==(d*d-1)*t*t*(1-t)**(d-1)
    assert b-c==(d+1)*t*(1-t)**d
    assert a-b==(d+1)*t*(d*t-1)*(1-t)**(d-1)

if __name__=='__main__':
    count=0
    for d in range(3,9):
        for t in [Q(1,9),Q(1,4),Q(1,3),Q(1,2),Q(3,4),Q(8,9),Q(1,d)]:
            verify(d,t);count+=1
    print(f'PROJECTIVE_CAP_EXACT_MOMENT_PASS dimensions=3..8 threshold_cases={count}')
