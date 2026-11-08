"""Standalone verification of the complement-convex Ferrers partition theorem.
Only finite independent checks; the infinite proof is supplied separately.
"""
from itertools import permutations

def nested(rows):
    return all(((x & ~y)==0 or (y & ~x)==0) for k,x in enumerate(rows) for y in rows[k+1:])

def antichain(rows):
    return all(x != y and x&~y and y&~x for k,x in enumerate(rows) for y in rows[k+1:])

def convex_zeros(rows,m,n):
    for p in permutations(range(m)):
        good=True
        for j in range(n):
            absent=[a for a,i in enumerate(p) if not (rows[i]>>j)&1]
            if absent and absent[-1]-absent[0]+1!=len(absent):good=False;break
        if good:return True,p
    return False,None

def ferrers_two(rows,m,n):
    edges=[(i,j) for i in range(m) for j in range(n) if (rows[i]>>j)&1]
    k=len(edges)
    for mask in range(1<<k):
        a=[0]*m;b=[0]*m
        for h,(i,j) in enumerate(edges):
            if mask>>h&1:a[i]|=1<<j
            else:b[i]|=1<<j
        if nested(a) and nested(b):return True
    return False

def theorem_complete(m,n):
    checked=0
    for word in range(1<<(m*n)):
        rows=[(word>>(i*n))&((1<<n)-1) for i in range(m)]
        if not antichain(rows):continue
        c,_=convex_zeros(rows,m,n)
        f=ferrers_two(rows,m,n)
        if c!=f:raise AssertionError((m,n,rows,c,f))
        checked+=1
    return checked

def ferrers_three_construct(n):
    C=[[[0]*n for _ in range(n)] for _ in range(3)]
    M=[]
    for i in range(n):
        for j in range(n):
            if j in (i,(i+1)%n):continue
            color=0 if j>i+1 else 1 if j>0 else 2
            C[color][i][j]=1
    for color in C:
        rows=[sum(v<<j for j,v in enumerate(r)) for r in color]
        assert nested(rows)
    return True

if __name__=='__main__':
    for m,n in [(3,3),(3,4),(4,4)]:
        c=theorem_complete(m,n)
        print(f'EXHAUSTIVE_ANTICHAIN_BIPARTITE_MATRICES_OK {m}x{n} {c} cases',flush=True)
    for n in range(3,101):ferrers_three_construct(n)
    print('THREE_FERRERS_CYCLIC_COMPLEMENT_OK n=3..100')
    print('VERIFY_OK')
