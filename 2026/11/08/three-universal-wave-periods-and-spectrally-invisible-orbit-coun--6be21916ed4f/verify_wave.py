#!/usr/bin/env python3
"""Exact binary-matrix checks for reversible waves on strongly regular graphs.
Only the Python standard library is needed. All arithmetic is over GF(2)."""
from itertools import combinations

def rank(rows):
    pivots={}
    for r in rows:
        while r:
            p=r.bit_length()-1
            if p in pivots:r^=pivots[p]
            else:pivots[p]=r;break
    return len(pivots)

def mul(A,B):
    out=[]
    for r in A:
        v=0
        while r:
            bit=r&-r;v^=B[bit.bit_length()-1];r-=bit
        out.append(v)
    return out

def power(A,t):
    n=len(A);result=[1<<i for i in range(n)]
    while t:
        if t&1:result=mul(result,A)
        A=mul(A,A);t//=2
    return result

def make_graph(n,edges):
    A=[0]*n
    for i,j in edges:
        if i==j:raise AssertionError('loop')
        A[i]^=1<<j;A[j]^=1<<i
    return A

def cyclic(n):return make_graph(n,[(i,(i+1)%n) for i in range(n)])
def bipartite(a,b):return make_graph(a+b,[(i,a+j) for i in range(a) for j in range(b)])
def rook(m):return make_graph(m*m,[(i,j) for i in range(m*m) for j in range(i+1,m*m) if i//m==j//m or i%m==j%m])
def triangular(m):
    pairs=list(combinations(range(m),2))
    return make_graph(len(pairs),[(i,j) for i in range(len(pairs)) for j in range(i+1,len(pairs)) if set(pairs[i])&set(pairs[j])])
def petersen():
    return make_graph(10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,((i+2)%5)+5) for i in range(5)])
def paley(p):
    residues={j*j%p for j in range(1,p)}
    return make_graph(p,[(i,j) for i in range(p) for j in range(i+1,p) if (j-i)%p in residues])
def sympl(x,y):
    return sum(((x>>i)&1)*((y>>(i+1))&1)+((x>>(i+1))&1)*((y>>i)&1) for i in (0,2,4))&1
def symplectic63():
    return make_graph(63,[(i,j) for i in range(63) for j in range(i+1,63) if sympl(i+1,j+1)])
def switched63(base):
    S=(1,4,16,21); idx=[x-1 for x in S];mask=sum(1<<i for i in idx)
    out=base.copy()
    assert all(not ((out[i]>>j)&1) for i,j in combinations(idx,2))
    for v in range(63):
        if v in idx:continue
        if (out[v]&mask).bit_count()==2:
            out[v]^=mask
            for j in idx:out[j]^=1<<v
    return out

def parameters(A):
    n=len(A);degree=A[0].bit_count();common_edge=set();common_nonedge=set()
    for i in range(n):
        assert not (A[i]>>i)&1
        assert A[i].bit_count()==degree
        for j in range(i+1,n):
            assert ((A[i]>>j)&1)==((A[j]>>i)&1)
            target=common_edge if ((A[i]>>j)&1) else common_nonedge
            target.add((A[i]&A[j]).bit_count())
    assert 0<degree<n-1 and len(common_edge)==len(common_nonedge)==1
    return n,degree,next(iter(common_edge)),next(iter(common_nonedge))

def wave(A):
    n=len(A)
    return [A[i]|(1<<(n+i)) for i in range(n)]+[1<<i for i in range(n)]

def check(name,A):
    n,k,l,m=parameters(A)
    d0=n-rank(A);d1=n-rank([r^(1<<i) for i,r in enumerate(A)])
    if k%2==l%2==m%2==0:period=4;exps={1:d0,2:2*d0,4:2*n}
    elif k%2==l%2==0 and m%2==1:period=10;exps={1:1,2:2,5:2*n-1,10:2*n}
    else:period=6;exps={1:d0,2:2*d0,3:d0+2*d1,6:2*n}
    F=wave(A);Id=[1<<i for i in range(2*n)]
    assert power(F,period)==Id
    for t in range(1,period):
        if period%t==0:assert power(F,t)!=Id
    for t,e in exps.items():
        Pt=power(F,t)
        nullity=2*n-rank([r^i for r,i in zip(Pt,Id)])
        assert nullity==e,(name,t,e,nullity)
    print('%-13s  srg(%d,%d,%d,%d)  order=%2d  d0=%2d d1=%2d  fixed-exponents=%s' %
          (name,n,k,l,m,period,d0,d1,repr(exps)))
    return period,d0,d1

if __name__=='__main__':
    examples=[('cycle5',cyclic(5)),('K2,2',bipartite(2,2)),('K3,3',bipartite(3,3)),
              ('Petersen',petersen()),('rook4',rook(4)),('rook5',rook(5)),
              ('triangle5',triangular(5)),('triangle6',triangular(6)),('Paley13',paley(13))]
    S=symplectic63()
    examples += [('symplectic63',S),('switched63',switched63(S))]
    results={name:check(name,A) for name,A in examples}
    assert results['symplectic63'][:2]==(4,57)
    assert results['switched63'][:2]==(4,55)
    print('PASS: exact orders, all listed fixed-point nullities, and isospectral rank separation.')
