#!/usr/bin/env python3
"""Independently enumerate all constrained words, shadows and conflict edges."""
from collections import defaultdict

def words(n):
    if n==0:return ['']
    prev=['']
    for _ in range(n):prev=[x+b for x in prev for b in '01' if not (x.endswith('1') and b=='1')]
    return prev

def gf_coeffs(N):
    # coefficient of z/((1-z-z^2)^2) + z^2/((1-z)(1-z-z^2)^3)
    a=[0]*(N+1);a[0]=1
    for i in range(1,N+1):a[i]=a[i-1]+(a[i-2] if i>1 else 0)
    def conv(u,v):return [sum(u[j]*v[i-j] for j in range(i+1)) for i in range(N+1)]
    a2=conv(a,a);a3=conv(a2,a)
    return [(a2[n-1] if n>0 else 0)+(sum(a3[:n-1]) if n>=2 else 0) for n in range(N+1)]

def gf_coeffs_hamming(n):
    a=[0]*(n+1);a[0]=1
    for i in range(1,n+1):a[i]=a[i-1]+(a[i-2] if i>1 else 0)
    return sum(a[j]*a[n-1-j] for j in range(n))

N=15; expected=gf_coeffs(N)
for n in range(1,N+1):
    W=words(n); byoutput=defaultdict(list)
    for i,x in enumerate(W):
        for y in set(x[:p]+x[p+1:] for p in range(n)):
            byoutput[y].append(i)
    conflict=set()
    for group in byoutput.values():
        for p,i in enumerate(group):
            for j in group[p+1:]:conflict.add((i,j))
    e=len(conflict)
    # All Hamming-one pairs are deletion confusable and are counted
    # once by a constrained word's unique 1 at flipped coordinate.
    h=sum(x.count('1') for x in W)
    assert e==expected[n],(n,e,expected[n])
    assert h==gf_coeffs_hamming(n)
    if n<=7:
        print(f'n={n} vertices={len(W)} edges={e} hamming={h} extra={e-h}')
    else:
        print(f'n={n} vertices={len(W)} edges={e}')
print('BRUTE_FORCE_OK',N)

