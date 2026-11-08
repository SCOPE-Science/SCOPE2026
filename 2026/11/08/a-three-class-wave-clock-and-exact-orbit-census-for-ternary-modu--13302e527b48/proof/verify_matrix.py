#!/usr/bin/env python3
"""Independent exact F_3 matrix-rank check of Hamming-graph wave claims.
Run: python3 verify_matrix.py. Uses only the Python standard library.
"""
from itertools import product

def rank(a):
    a=[row[:] for row in a]; rows=len(a); cols=len(a[0]); r=0
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][c]%3),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        if a[r][c]==2: a[r]=[(2*x)%3 for x in a[r]]
        for i in range(r+1,rows):
            z=a[i][c]
            if z: a[i]=[(x-z*y)%3 for x,y in zip(a[i],a[r])]
        r+=1
        if r==rows: break
    return r

def multiply(a,b):
    n=len(a); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,z in enumerate(a[i]):
            if z:
                for j in range(n):out[i][j]=(out[i][j]+z*b[k][j])%3
    return out

def counts(m,d):
    n=m**d; a=((m-1)**d+(m-3)**d)//2
    b=((m-1)**d-(m-3)**d)//2; c=(n-a-2*b)//3
    return a+b+c,a+2*b+2*c,(a,b,c)

def check(m,d):
    words=list(product(range(m),repeat=d)); n=len(words)
    a=[[int(sum(x!=y for x,y in zip(u,v))==1) for v in words] for u in words]
    k1,k2,blocks=counts(m,d)
    h=[[ (a[i][j]+d*int(i==j))%3 for j in range(n)] for i in range(n)]
    h2=multiply(h,h); h3=multiply(h2,h)
    assert rank(h)==n-k1 and rank(h2)==n-k2 and not any(any(row) for row in h3)
    sz=2*n; ident=[[int(i==j) for j in range(sz)] for i in range(sz)]
    t=[[0]*sz for _ in range(sz)]
    for i in range(n):
        for j in range(n):t[i][j]=a[i][j]
        t[i][n+i]=2; t[n+i][i]=1
    v=ident
    if d%3==0:
        expected={1:0,2:0,3:0,4:2*k1,6:0,12:2*n}
        period=12
    elif d%3==1:
        expected={1:k1,2:k1,3:k1+k2,9:2*n}
        period=9
    else:
        expected={1:0,2:k1,3:0,6:k1+k2,9:0,18:2*n}
        period=18
    for step in range(1,period+1):
        v=multiply(v,t)
        if step in expected:
            r=rank([[(v[i][j]-ident[i][j])%3 for j in range(sz)] for i in range(sz)])
            assert sz-r==expected[step],(m,d,step,sz-r,expected[step])
        if step<period:assert v!=ident,(m,d,step)
    assert v==ident
    print('PASS',m,d,'vertices',n,'kernel N',k1,'kernel N^2',k2,
          'blocks',blocks,'wave order',period)

for test in [(3,1),(3,2),(3,3),(3,4),(6,1),(6,2),(9,1)]:check(*test)
print('ALL EXACT MATRIX TESTS PASSED')
