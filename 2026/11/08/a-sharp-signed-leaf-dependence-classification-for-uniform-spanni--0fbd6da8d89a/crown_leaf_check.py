#!/usr/bin/env python3
"""Exact independent Kirchhoff tests for pairwise UST leaf events in crown graphs."""
from fractions import Fraction
from itertools import combinations
from math import isqrt

def determinant(a):
    a = [[Fraction(x) for x in row] for row in a]
    n = len(a); d=Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return Fraction(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];d=-d
        b=a[k][k];d*=b
        for i in range(k+1,n):
            c=a[i][k]/b
            for j in range(k+1,n):a[i][j]-=c*a[k][j]
            a[i][k]=0
    return d

def tau(n,removed=()):
    v=[i for i in range(2*n) if i not in removed]; idx={x:i for i,x in enumerate(v)}
    if len(v)<2:return 1
    M=[[0]*len(v) for _ in v]
    for i in range(n):
      for j in range(n):
        if i==j:continue
        a=i;b=n+j
        if a in idx and b in idx:
            x,y=idx[a],idx[b]
            M[x][x]+=1;M[y][y]+=1;M[x][y]-=1;M[y][x]-=1
    return determinant([row[:-1] for row in M[:-1]])

def predicted(n):
    c=n*n-3*n+1; x=(n-1)*(n-3);y=n*n-4*n+2
    T=(n-1)*n**(n-2)*(n-2)**(n-1)
    single=Fraction(c**(n-2),(n*(n-2))**(n-2))
    cross=Fraction((n-2)**2*c*x**(n-3),T) if n>3 else Fraction(1,6)
    matched=Fraction((n-1)**2*(n-2)*(n-3)*x**(n-3),T) if n>3 else Fraction(0)
    same=Fraction((n-1)**2*(n-2)*(n-3)*y**(n-3),T) if n>3 else Fraction(0)
    return T,single,cross,matched,same

checks=0
for n in range(3,8):
    T,p,a,m,s=predicted(n)
    assert tau(n)==T;checks+=1
    for vertices,expect in [((0,),p),((0,n+1),a),((0,n),m),((0,1),s)]:
      d=1
      for u in vertices:
        d*=sum((u<n and v>=n and u!=v-n) or (u>=n and v<n and u-n!=v) for v in range(2*n) if v not in vertices)
      got=Fraction(d*tau(n,vertices),T)
      assert got==expect,(n,vertices,got,expect)
      checks+=1
    assert a>p*p>m>=s
    if n>3:assert m>s
    checks+=1

L=[2,3]
for i in range(2,25):L.append(3*L[-1]-L[-2])
for j in range(1,22):
 N=(1-j)*2**j +3*j+4 +3**(j+1) +2*j*L[j+1]-(5*j+5)*L[j]
 assert (N==0 if j<4 else N>0),(j,N)
 checks+=1
print('VERIFY_OK',checks,'exact assertions')
