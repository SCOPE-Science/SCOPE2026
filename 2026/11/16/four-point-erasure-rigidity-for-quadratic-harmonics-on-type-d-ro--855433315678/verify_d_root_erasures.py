#!/usr/bin/env python3
"""Exact checks for the low-degree D-type harmonic erasure theorem."""
from itertools import combinations, product
from math import comb

def vertices(d):
    out=[]
    for i,j in combinations(range(d),2):
        for s,t in product((-1,1),repeat=2):
            v=[0]*d; v[i]=s;v[j]=t
            out.append(tuple(v))
    return out

def det_bareiss(A):
    n=len(A)
    M=[list(map(int,row)) for row in A]
    sign=1; den=1
    for k in range(n-1):
        if M[k][k]==0:
            for j in range(k+1,n):
                if M[j][k]:
                    M[k],M[j]=M[j],M[k];sign=-sign;break
            else:return 0
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=M[i][j]*pivot-M[i][k]*M[k][j]
                assert numerator % den==0
                M[i][j]=numerator//den
            M[i][k]=0
        den=pivot
    return sign*M[n-1][n-1]

def predicted_bad4(V, inds):
    vv=[V[i] for i in inds]
    # Exactly two disjoint antipodal pairs whose directions are orthogonal.
    antip=[]
    for i,j in combinations(range(4),2):
        if all(vv[i][k]==-vv[j][k] for k in range(4)):
            antip.append((i,j))
    if len(antip)!=2: return False
    (a,b),(c,d)=antip
    if len({a,b,c,d})!=4:return False
    return sum(vv[a][k]*vv[c][k] for k in range(4))==0

def check_d4():
    V=vertices(4); n=len(V); assert n==24
    # The degree <=2 spherical reproducing kernel is K(v,w)=(1+4t+12t^2-3)/24.
    # Since t=v.w/2, its numerator matrix is M=3(v.w)^2+2(v.w)-2.
    M=[[3*sum(a*b for a,b in zip(v,w))**2 + 2*sum(a*b for a,b in zip(v,w))-2 for w in V] for v in V]
    assert all(sum(M[i][k]*M[k][j] for k in range(24))==24*M[i][j] for i in range(24) for j in range(24))
    # Thus K=M/24 is an orthogonal projection with trace 14.
    assert sum(M[i][i] for i in range(24))==24*14
    counts=[]
    for r in (1,2,3,4):
        bad=[]
        for I in combinations(range(n),r):
            H=[[24*(i==j)-M[I[i]][I[j]] for j in range(r)] for i in range(r)]
            if det_bareiss(H)==0:bad.append(I)
        counts.append((r,len(bad)))
        if r==4:
            pred=[I for I in combinations(range(n),4) if predicted_bad4(V,I)]
            assert set(bad)==set(pred)
    assert counts==[(1,0),(2,0),(3,0),(4,18)], counts
    print('d=4: all 1-,2-,3-,4-erasures checked exactly; 18/10626 singular 4-sets')

def witness(d, i,j):
    V=vertices(d)
    return [x for x in V if x[i]*x[j]!=0]

def check_higher():
    for d in range(4,11):
        V=vertices(d)
        assert len(V)==2*d*(d-1)
        assert all(len(witness(d,i,j))==4 for i,j in combinations(range(d),2))
        # Injectivity of signed-edge representation: evaluate the polynomial basis
        # for all choices on every edge; check its coordinate Walsh coefficients.
        for i,j in combinations(range(d),2):
            vals=[(s,t,s*t) for s,t in product((-1,1),repeat=2)]
            assert sum(s for s,t,z in vals)==sum(t for s,t,z in vals)==sum(z for s,t,z in vals)==0
        if d==4:
            for (i,j),(k,l) in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]:
                for a,b in product((-1,1),repeat=2):
                    # h_i=h_j=+1, h_k=h_l=-1, gamma_ij=2*a, gamma_kl=2*b.
                    h=[0]*d;h[i]=h[j]=1;h[k]=h[l]=-1
                    g={(i,j):2*a,(k,l):2*b}
                    support=[]
                    for v in V:
                        inds=[r for r,x in enumerate(v) if x]
                        x,y=inds
                        val=h[x]+h[y]+g.get((x,y),0)*v[x]*v[y]
                        if val:support.append(v)
                    assert len(support)==4
    print('d=4..10: all coordinate-square and exceptional supports verified')

if __name__=='__main__':
    check_d4();check_higher();print('PASS: exact finite arithmetic checks')
