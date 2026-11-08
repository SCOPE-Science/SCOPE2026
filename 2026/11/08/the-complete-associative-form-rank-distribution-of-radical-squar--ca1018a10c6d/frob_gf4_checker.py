"""Independent GF(4) checks for multiplication-pairing rank enumerators."""
from itertools import product
from collections import Counter

def mul(a,b):
    out=0
    for i in (0,1):
        for j in (0,1):
            if (a>>i)&1 and (b>>j)&1:
                p=i+j
                out^=3 if p==2 else (1<<p)
    return out

def inv(a):
    for x in (1,2,3):
        if mul(a,x)==1:return x
    raise ZeroDivisionError

def rk(M):
    a=[r[:] for r in M];n=len(a);h=0
    for j in range(n):
        piv=next((i for i in range(h,n) if a[i][j]),None)
        if piv is None:continue
        a[h],a[piv]=a[piv],a[h]
        u=inv(a[h][j]);a[h]=[mul(u,x) for x in a[h]]
        for i in range(n):
            if i!=h and a[i][j]:
                c=a[i][j];a[i]=[v^mul(c,w) for v,w in zip(a[i],a[h])]
        h+=1
    return h

def direct(n,E):
    d=Counter()
    for vals in product(range(4),repeat=n+len(E)):
        M=[[0]*(n+len(E)) for _ in range(n+len(E))]
        for i in range(n): M[i][i]=vals[i]
        for a,(s,t) in enumerate(E):
            M[s][n+a]=vals[n+a]
            M[n+a][t]=vals[n+a]
        d[rk(M)]+=1
    return d

def pred(n,E):
    d=Counter()
    for c in product(range(4),repeat=len(E)):
        S={s for (s,t),v in zip(E,c) if v}
        T={t for (s,t),v in zip(E,c) if v}
        for v in product(range(4),repeat=n):
            r=len(S)+len(T)+sum(v[i]!=0 for i in range(n) if i not in S|T)
            d[r]+=1
    return d

cases=[(1,[(0,0)]),(2,[(0,1)]),(2,[(0,1),(1,0)]),(3,[(0,1),(1,2)]),(3,[(0,1),(0,2)])]
for n,E in cases:
    a=direct(n,E);b=pred(n,E)
    assert a==b,(n,E,a,b)
    print('GF4_PASS',n,E,dict(sorted(a.items())))
print('GF4_ALL_FROBENIUS_RANK_CHECKS_PASS')
