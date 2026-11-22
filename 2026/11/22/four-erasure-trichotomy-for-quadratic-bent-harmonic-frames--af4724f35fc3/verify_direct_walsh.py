"""Exact direct Fourier/Gram verification for a quadratic bent harmonic frame.
This standalone checker uses character sums and integer characteristic polynomials.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb


def quadratic(x,m):
    return sum(((x >> (2*j))&1) & ((x >> (2*j+1))&1) for j in range(m))%2


def determinant(a):
    n=len(a); z=0
    for p in permutations(range(n)):
        s=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        prod=1
        for i,j in enumerate(p):prod*=a[i][j]
        z+=(-1 if s&1 else 1)*prod
    return z


def traces(a):
    n=len(a)
    b=[[int(i==j) for j in range(n)] for i in range(n)]
    t=[]
    for _ in range(n):
        b=[[sum(b[i][k]*a[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        t.append(sum(b[i][i] for i in range(n)))
    return t


def charpoly_coeffs(a):
    n=len(a); t=traces(a);c=[1]
    for j in range(1,n+1):
        s=sum(c[j-i]*t[i-1] for i in range(1,j+1))
        assert s%j==0
        c.append(-s//j)
    assert c[-1]==determinant(a)
    return tuple(c)


def verify(m):
    v=1<<(2*m); k=(v-(1<<m))//2
    D=[x for x in range(v) if quadratic(x,m)==1]
    assert len(D)==k
    f=[sum(-1 if ((h&d).bit_count()&1) else 1 for d in D) for h in range(v)]
    scale=1<<(m-1)
    assert f[0]==k
    assert all(abs(f[h])==scale for h in range(1,v))
    S=[[0 if x==y else f[x^y]//scale for y in range(v)] for x in range(v)]
    assert all(S[x][y] in (-1,1) for x in range(v) for y in range(v) if x!=y)
    cnt=Counter()
    for T in combinations(range(v),4):
        X=[[S[x][y] for y in T] for x in T]
        pol=charpoly_coeffs(X)
        cnt[pol]+=1
    target={
        (1,0,-6,-8,-3):v**3*(v-1)//192,
        (1,0,-6,0,5):v**2*(v-4)*(v-1)//32,
        (1,0,-6,8,-3):v*(v-12)*(v-4)*(v-1)//192,
    }
    assert cnt==target, (cnt,target)
    assert sum(cnt.values())==comb(v,4)
    print('direct_walsh m=',m,'v=',v,'k=',k,'charpoly_counts=',sorted(cnt.items()),'total=',sum(cnt.values()))

if __name__=='__main__':
    verify(2)
