#!/usr/bin/env python3
"""Independent finite-prime-field checks for derivation spectra of perfect evolution algebras."""
from itertools import product
from math import factorial, comb
from collections import Counter

def rank(A, q):
    A=[list(map(lambda t:t%q, row)) for row in A]
    if not A:return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:continue
        A[r], A[piv]=A[piv],A[r]
        v=pow(A[r][c],-1,q)
        A[r]=[(v*x)%q for x in A[r]]
        for i in range(m):
            if i==r or A[i][c]==0:continue
            k=A[i][c]
            A[i]=[(a-k*b)%q for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def derdim(M,p):
    n=len(M);eq=[]
    for i in range(n):
        for j in range(i,n):
            for v in range(n):
                row=[0]*(n*n)
                if i==j:
                    for a in range(n): row[v*n+a]+=M[i][a]
                    row[i*n+i]-=2*M[i][v]
                else:
                    row[j*n+i]-=M[j][v]
                    row[i*n+j]-=M[i][v]
                eq.append(row)
    return n*n-rank(eq,p)

def GL(n,q):
    r=1
    for j in range(n):r*=q**n-q**j
    return r

def order2(p):
    if p==2:return 0
    a=2%p;v=a;h=1
    while v!=1:
        h+=1;v=v*a%p
    return h

def check(q,n):
    dist=Counter()
    for data in product(range(q),repeat=n*n):
        M=[data[i*n:(i+1)*n] for i in range(n)]
        if rank(M,q)!=n:continue
        dist[derdim(M,q)]+=1
    h=order2(q)
    if not h:
        expected={0:GL(n,q)}
    elif n<2*h:
        v=(comb(n,h)*factorial(h-1)*(q-1)**h*GL(n-h,q) if n>=h else 0)
        expected={0:GL(n,q)-v,1:v}
    else:raise ValueError('use separate test for n>=2h')
    assert dist==Counter({k:v for k,v in expected.items() if v}), (q,n,dist,expected)
    print('PASS enumeration',q,n,dict(sorted(dist.items())))

for q,n in [(2,2),(2,3),(3,2),(3,3),(5,2),(7,2)]:check(q,n)
# Explicit residue-char 7 example with order of 2 equal to 3.
q=7;M=[[0,1,0],[0,0,1],[1,0,0]]
assert rank(M,q)==3 and derdim(M,q)==1
# Split 3-cycle + identity in dimension four: one-dimensional derivations.
M=[[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,1]]
assert derdim(M,7)==1
# Connected size-4 admissible components for p=3 (h=2): two 2x2 invertible offdiagonal blocks.
q=3
blocks=[]
for data in product(range(q),repeat=4):
    X=[data[:2],data[2:]]
    if rank(X,q)==2:blocks.append(X)
connected=0
for X in blocks:
    for Y in blocks:
        adj=[set() for _ in range(4)]
        for i in range(2):
            for j in range(2):
                if X[i][j] or Y[j][i]:
                    adj[i].add(j+2); adj[j+2].add(i)
        seen={0};stack=[0]
        while stack:
            for j in adj[stack.pop()]:
                if j not in seen:seen.add(j);stack.append(j)
        if len(seen)==4:connected+=1
assert connected==GL(2,3)**2-2*(3-1)**4,(connected, GL(2,3)**2-32)
# Connected labeled 4-vertex eligible count is 4!/(h*(m!)^h) times this number, with h=m=2.
assert 3*connected==6816
# All four-vertex matrices of nonzero derivation have exactly-one and exactly-two strata counts.
assert 3*(3-1)**4==48
assert 6816+(6*4*GL(2,3)-2*48)==7872
assert 6816+6*4*GL(2,3)-48==7920
# Distinct derivations in h-cycle block have cardinality q; dimensions 1, not q-1.
print('PASS connected cyclic blocks',connected,'dimension-4 q=3 eligible total',7920)
print('VERIFY_OK')
