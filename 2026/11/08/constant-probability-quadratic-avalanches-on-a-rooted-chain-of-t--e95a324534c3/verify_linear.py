"""Independent integer Laplacian and random-state certificates for a triangle cactus path.

Run: python verify_linear.py
Only the Python standard library is required.
"""
from itertools import product
from random import Random
from fractions import Fraction


def edges(k):
    return [(i-1, i) for i in range(1,k+1)] + [(i-1,k+i) for i in range(1,k+1)] + [(i,k+i) for i in range(1,k+1)]


def laplacian(k):
    n=2*k
    L=[[0]*n for _ in range(n)]
    for a,b in edges(k):
        if a: L[a-1][a-1]+=1
        if b: L[b-1][b-1]+=1
        if a and b:
            L[a-1][b-1]-=1;L[b-1][a-1]-=1
    return L


def matvec(a,x):
    return [sum(v*y for v,y in zip(row,x)) for row in a]


def solve(a,b):
    n=len(b);m=[[Fraction(x) for x in row]+[Fraction(rhs)] for row,rhs in zip(a,b)]
    for c in range(n):
        pivot=next(r for r in range(c,n) if m[r][c])
        m[c],m[pivot]=m[pivot],m[c]
        s=m[c][c];m[c]=[t/s for t in m[c]]
        for r in range(n):
            if r!=c:
                f=m[r][c]
                if f:m[r]=[v-f*w for v,w in zip(m[r],m[c])]
    return [r[-1] for r in m]


def heights(k, words):
    h=[0]*(2*k)
    for i,x in enumerate(words,1):
        a,b={'A':(1,1),'B':(1,0),'C':(0,1)}[x]
        h[i-1]=a+(2 if i<k else 0)
        h[k+i-1]=b
    return h


def stabilize(k, words):
    L=laplacian(k)
    h=heights(k,words)
    h[k-1]+=1
    u=[0]*(2*k)
    degree=[L[i][i] for i in range(2*k)]
    while True:
        x=next((i for i in range(2*k) if h[i]>=degree[i]),None)
        if x is None:break
        for j in range(2*k):h[j]-=L[j][x]
        u[x]+=1
    return u,h


def run():
    rng=Random(150827)
    for k in range(2, 51):
        L=laplacian(k)
        u=[2*i if i<k else 2*k-1 for i in range(1,k+1)] + [2*i-1 for i in range(1,k+1)]
        rhs=[0]*(2*k)
        rhs[k-2]=rhs[k-1]=rhs[2*k-1]=1
        assert matvec(L,u)==rhs
        mean=[Fraction(2*i,3) for i in range(1,k+1)]+[Fraction(2*i-1,3) for i in range(1,k+1)]
        source=[0]*(2*k);source[k-1]=1
        assert matvec(L,mean)==source
        assert sum(mean)==Fraction(2*k*k+k,3)
        assert sum(u)==2*k*k+k-1
        for _ in range(10):
            words=[rng.choice('ABC') for _ in range(k)]
            uu,_=stabilize(k,words)
            assert all(a<=b for a,b in zip(uu,u))
            assert (uu==u)==(words[-2:]==['A','A'])
        if k<=12:
            assert solve(L,source)==mean
    print('Exact Laplacian identities and independent stabilization samples for k=2..50 passed.')
    print('Rational Green-function inversion for k=2..12 passed.')

if __name__=='__main__':run()
