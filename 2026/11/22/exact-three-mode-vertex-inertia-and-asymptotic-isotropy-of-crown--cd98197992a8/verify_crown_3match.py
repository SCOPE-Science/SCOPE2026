"""Independent enumeration and rational tests for crown 3-matching inertia."""
from itertools import combinations
from fractions import Fraction
from collections import Counter

def check(n):
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    m=len(edges)
    triples=[]
    for comb in combinations(range(m),3):
        es=[edges[t] for t in comb]
        if len({e[0] for e in es})==3 and len({e[1] for e in es})==3:
            triples.append(comb)
    T=len(triples)
    by=Counter(i for tri in triples for i in tri)
    pairs=Counter(tuple(sorted((i,j))) for tri in triples for i,j in combinations(tri,2))
    d=n*n-3*n+3
    D=n*n-5*n+8
    K=d*D-2*(n-1)
    assert T==m*K//6 and m*K%6==0,(n,T,m*K//6)
    p=Fraction(3,m)
    eig_0=p+Fraction(D,T)
    eig_plus=p+Fraction(D*(3-n)-(n-2),T)
    eig_minus=p+Fraction(D*(1-n)+n,T)
    assert len(by)==m and all(c==3*T//m for c in by.values())
    for a,e in enumerate(edges):
        for b,f in enumerate(edges):
            observed=Fraction(pairs[tuple(sorted((a,b)))],T) if a!=b else Fraction(by[a],T)
            theoretical=(p if a==b else (Fraction(D-int(e[0]==f[1])-int(e[1]==f[0]),T) if e[0]!=f[0] and e[1]!=f[1] else 0))
            assert observed==theoretical,(n,e,f,observed,theoretical)
    # Test covariance eigenvectors using independent full moment counts.
    from math import isclose
    def mul(v):
        avg= sum(v)*p
        return [sum(Fraction(pairs[tuple(sorted((a,b)))],T)*v[b] if a!=b else Fraction(by[a],T)*v[b] for b in range(m))-p*avg for a in range(m)]
    u=[0]*n;u[0]=1;u[1]=-1
    vs=[([u[i]+u[j] for i,j in edges],eig_plus),([u[i]-u[j] for i,j in edges],eig_minus)]
    for v,ev in vs:
        assert mul(v)==[ev*z for z in v],(n,ev)
    # cycle-supported row and col-balanced vector (2x2 non-diagonal subgrid) for n>=4
    if n>=4:
        a,b,c,d=0,1,2,3
        v=[(1 if (i,j) in [(a,c),(b,d)] else -1 if (i,j) in [(a,d),(b,c)] else 0) for i,j in edges]
        assert mul(v)==[eig_0*z for z in v],(n,eig_0)
    if n>=4:
        assert 0<eig_minus<eig_plus<eig_0
    else:
        assert eig_minus==eig_plus==0
    assert eig_0*(n*n-3*n+1)+(eig_minus+eig_plus)*(n-1)==m*p*(1-p)
    print('n',n,'T',T,'lambda',eig_minus,eig_plus,eig_0, 'kappa',eig_0/eig_minus if n>=4 else 'singular')
for n in range(3,9):check(n)
print('CROWN_THREE_MATCH_PASS')
