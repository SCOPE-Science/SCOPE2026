"""Exact checks of path-independent-set Fourier minors and explicit inverses.
Runs with the Python standard library (Fractions, itertools); no external files.
"""
from fractions import Fraction as F
from itertools import product
from math import prod, isclose

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b,q):
    x,y=a; u,v=b
    if q==3: return (x*u-y*v,x*v+y*u-y*v)
    return (x*u-y*v,x*v+y*u)
def conj(a,q): return (a[0]-a[1],-a[1]) if q==3 else (a[0],-a[1])
ZERO=(F(0),F(0)); ONE=(F(1),F(0))
def phase(k,q):
    k%=q
    if q==2: return (F(1 if k==0 else -1),F(0))
    if q==3: return (ONE,(F(0),F(1)),(F(-1),F(-1)))[k]
    if q==4: return (ONE,(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1)))[k]
    raise ValueError(q)
def states(n,q):
    return [t for t in product(range(q),repeat=n) if all(not(t[i] and t[i+1]) for i in range(n-1))]
def ipath(m,q):
    z=F(-(q-1),q)
    if m==0:return F(1)
    a,b=F(1),F(1)+z
    for k in range(2,m+1):a,b=b,b+z*a
    return b

def inv(a,b,q):
    n=len(a); U={i for i in range(n) if a[i] or b[i]}
    if any(i+1 in U for i in U):return ZERO
    forbidden=set(U)
    for i in U:
        if i>0:forbidden.add(i-1)
        if i<n-1:forbidden.add(i+1)
    multiplier=F(1);run=0
    for i in range(n+1):
        if i<n and i not in forbidden:run+=1
        else:
            if run:multiplier*=ipath(run,q);run=0
    return tuple(v*multiplier/F(q**len(U)) for v in conj(phase(sum(x*y for x,y in zip(a,b)),q),q))

def integer_determinant(matrix):
    a=[list(row) for row in matrix]; n=len(a)
    prev=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            assert r is not None
            a[k],a[r]=a[r],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                assert val%prev==0
                a[i][j]=val//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]

def check(q,n):
    T=states(n,q);m=len(T)
    H=[[phase(sum(x*y for x,y in zip(a,b)),q) for b in T] for a in T]
    V=[[inv(a,b,q) for b in T] for a in T]
    for i in range(m):
        for j in range(m):
            s=ZERO
            for k in range(m):s=add(s,mul(H[i][k],V[k][j],q))
            assert s==(ONE if i==j else ZERO),(q,n,m,i,j,s)
    if q==2 and n<=6:
        num=sum(sum(bool(v) for v in x) for x in T)
        det=integer_determinant([[int(z[0]) for z in row] for row in H])
        assert abs(det)==2**num, (q,n,det,num)
    # Symmetry makes checking right inverse automatic.
    assert H==[list(x) for x in zip(*H)]
    assert V==[list(x) for x in zip(*V)]
    extras=sum(bool(not any(i+1 in (set(k for k,x in enumerate(a) if x) | set(k for k,x in enumerate(b) if x)) for i in range(n-1)) and V[i][j]==ZERO) for i,a in enumerate(T) for j,b in enumerate(T))
    if q!=2:assert extras==0
    if q==2:
        assert (V[0][0]==ZERO)==(n%4==2)
    print('EXACT_TWO_SIDED q=%d n=%d size=%d independent_union_zeros=%d'%(q,n,m,extras))

if __name__=='__main__':
    for q,ns in [(2,range(2,9)),(3,range(2,6)),(4,range(2,5))]:
        for n in ns:check(q,n)
    print('PATH_INDEPENDENCE_FOURIER_CHECKS_PASS')
