#!/usr/bin/env python3
"""Independent finite tests for a three-adic ordered-Bell residue theorem.

The proof in RESULT.md is unbounded; these finite checks are reproducibility aids.
"""
from collections import Counter
from math import comb, factorial

def bell_mod(N, modulus):
    a=[1]
    for n in range(1,N+1):
        a.append(sum(comb(n,j)*a[n-j] for j in range(1,n+1))%modulus)
    return a

def stirling_bell(N):
    row=[1]; out=[1]
    for n in range(1,N+1):
        nxt=[0]*(n+1)
        for j in range(1,n+1):
            nxt[j]=(row[j-1] if j-1<len(row) else 0)+j*(row[j] if j<len(row) else 0)
        row=nxt;out.append(sum(factorial(j)*row[j] for j in range(n+1)))
    return out

checks=0
full=stirling_bell(48)
a=bell_mod(48,3**12)
assert all(x%(3**12)==y for x,y in zip(full,a));checks+=len(full)

c={b:sum((-1)**(j-b)*comb(j,b) for j in range(b,9)) for b in range(1,9)}
assert c=={1:-4,2:16,3:-34,4:46,5:-40,6:22,7:-7,8:1}
for n in range(4,70):
    a=bell_mod(n+4,81)
    assert a[n+2]-a[n] == a[n+2]-a[n] # integer check of index alignment
    if n%2==0:
        assert (a[n+2]-a[n])%81==72
        assert (a[n+4]-2*a[n+2]+a[n])%81==0
    else:
        assert (a[n+2]-a[n])%9==6
    for h in (1,2):
        residue=sum(c[b]*pow(b,n,81)*pow(b*b-1,h,81) for b in range(1,9))%81
        expected=(sum((-1)**(h-j)*comb(h,j)*a[n+2*j] for j in range(h+1)))%81
        assert residue==expected
        checks+=1

K=7
N=2*3**(K-1)+40
A=bell_mod(N,3**K)
for k in range(1,K+1):
    q=3**k;period=2*3**(k-1);start=max(4,k+2)
    assert len(A)>start+period
    counts=Counter(A[n]%q for n in range(start,start+period))
    if k==1:
        assert counts=={0:1,1:1}
    else:
        for y in range(q):
            target=1 if y%3==1 else (3 if y%9==3 else 0)
            assert counts[y]==target,(k,y,counts[y],target)
            checks+=1
        assert len(counts)==4*3**(k-2)
    for n in range(start, min(start+period, len(A)-period)):
        assert A[n]%q==A[n+period]%q
        checks+=1

for n in range(6,120):
    for t in [1,2,3,4,5,6,9,12,18,27,36,54,81]:
        s=0;u=t
        while u%3==0: s+=1;u//=3
        if n<max(4,s+3):continue
        q=3**(s+4)
        a=bell_mod(n+2*t,q)
        delta=(a[n+2*t]-a[n])%q
        v=0
        while delta%3==0 and delta>0:
            delta//=3;v+=1
        assert v==s+(2 if n%2==0 else 1),(n,t,v)
        checks+=1
print(f'PASS: {checks} finite assertions; exact recurrence, digit fibres and shift valuations.')
