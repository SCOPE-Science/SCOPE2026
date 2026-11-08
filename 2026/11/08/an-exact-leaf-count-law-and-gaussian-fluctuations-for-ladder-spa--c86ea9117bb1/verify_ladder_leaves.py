#!/usr/bin/env python3
"""Independent integer checks of a leaf-enumerator for random ladder spanning trees.
All computations use Python's standard library and exact integer arithmetic.
Run: python verify_ladder_leaves.py
"""
from itertools import combinations
from math import comb

def add(a,b,sgn=1):
    return tuple((a[i] if i<len(a) else 0)+sgn*(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return tuple(out)
def coeff_series(nmax):
    # D=1-(z+3)u+(3-2z)u^2-(2z^2-3z+1)u^3.
    # N=u-(z-1)u^2+(z^2-1)u^3-(z-1)^3u^4.
    N={1:(1,),2:(1,-1),3:(-1,0,1),4:(1,-3,3,-1)}
    # corrected N2: -(z-1)=1-z; N4= -(z-1)^3 =1-3z+3z^2-z^3.
    C=[(0,)]
    for n in range(1,nmax+1):
        v=N.get(n,(0,))
        if n>=1:v=add(v,mul((3,1),C[n-1]))
        if n>=2:v=add(v,mul((-3,2),C[n-2]))
        if n>=3:v=add(v,mul((1,-3,2),C[n-3]))
        C.append(v)
    return C

def brute(n):
    vertices=2*n
    edges=[(i,n+i) for i in range(n)]+[(i,i+1) for i in range(n-1)]+[(n+i,n+i+1) for i in range(n-1)]
    counts=[0]*(2*n)
    for ids in combinations(range(len(edges)),vertices-1):
        parent=list(range(vertices))
        deg=[0]*vertices
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]];x=parent[x]
            return x
        ok=True
        for ei in ids:
            u,v=edges[ei];ru,rv=find(u),find(v)
            if ru==rv:ok=False;break
            parent[ru]=rv;deg[u]+=1;deg[v]+=1
        if ok:
            assert all(find(v)==find(0) for v in range(vertices))
            leaves=sum(d==1 for d in deg)
            assert leaves>=2
            counts[leaves-2]+=1
    while counts and counts[-1]==0:counts.pop()
    return tuple(counts)

def ntrees(n):
    a,b=0,1
    for _ in range(n):a,b=b,4*b-a
    return a

def mean_var_poly(p):
    tot=sum(p)
    m1=sum(i*a for i,a in enumerate(p));m2=sum(i*i*a for i,a in enumerate(p))
    from fractions import Fraction
    return Fraction(m1,tot), Fraction(m2,tot)-Fraction(m1,tot)**2

if __name__=='__main__':
    P=coeff_series(30)
    checks=0
    for n in range(1,8):
        a=P[n];b=brute(n)
        assert a[:len(b)]==b and all(x==0 for x in a[len(b):]), (n,a,b)
        checks+=1
    for n in range(1,31):
        assert sum(P[n])==ntrees(n),n
        assert all(v>=0 for v in P[n]),n
        assert mean_var_poly(P[n])[1]>=0,n
        checks+=3
    assert P[3][:3]==(8,6,1) and P[4][:3]==(14,28,14)
    checks+=2
    print(f'VERIFY_OK {checks} exact checks; exhaustive n=1..7; coefficient recurrence n<=30')
