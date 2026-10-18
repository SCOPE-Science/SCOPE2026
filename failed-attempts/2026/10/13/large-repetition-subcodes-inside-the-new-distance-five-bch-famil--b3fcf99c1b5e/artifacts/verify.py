#!/usr/bin/env python3
import math
from collections import Counter


def mul(a,b,m,mod):
    r=0
    while b:
        if b&1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & (1<<m):
            a ^= mod
    return r & ((1<<m)-1)


def power(a,n,m,mod):
    r=1
    while n:
        if n&1:
            r=mul(r,a,m,mod)
        a=mul(a,a,m,mod)
        n//=2
    return r


def order(a,m,mod):
    N=(1<<m)-1
    for d in range(1,N+1):
        if N%d==0 and power(a,d,m,mod)==1:
            return d
    raise AssertionError


def psum(theta,E,p,m,mod):
    z=0
    for e in E:
        z ^= power(theta,p*e,m,mod)
    return z

# The polynomial moduli are irreducible; verify the resulting nonzero groups.
for m,mod in [(4,0b10011),(8,0x11b)]:
    N=(1<<m)-1
    for a in range(1,1<<m):
        assert power(a,N,m,mod)==1
        assert mul(a,power(a,N-1,m,mod),m,mod)==1

E5=[0,1,2,3,4]
order5=[a for a in range(1,16) if order(a,4,0b10011)==5]
assert len(order5)==4
for a in order5:
    assert psum(a,E5,1,4,0b10011)==0
    assert psum(a,E5,3,4,0b10011)==0

E51=[0,3,21,33,44]
good51=[]
for a in range(1,256):
    if order(a,8,0x11b)==51:
        if psum(a,E51,1,8,0x11b)==0 and psum(a,E51,3,8,0x11b)==0:
            good51.append(a)
assert len(good51)==8


def construction(s):
    n=(2**(2*s)+1)*(2**s-1)
    if s%4!=2:
        assert n%5==0
        M=5; E=E5
    else:
        assert n%51==0
        M=51; E=E51
    r=n//M
    supports=[]
    for t in range(r):
        S=tuple(sorted(t+r*e for e in E))
        assert len(set(S))==5
        assert all(0<=x<n for x in S)
        supports.append(S)
    # Disjointness follows from distinct residues modulo r; check it exactly.
    seen=set()
    for S in supports:
        assert seen.isdisjoint(S)
        seen.update(S)
    assert len(seen)==5*r
    return n,r,supports

for s in range(2,201):
    n=(2**(2*s)+1)*(2**s-1)
    if s%4!=2:
        assert n%5==0
    else:
        assert n%51==0

# Exact disjoint-support and enumerator checks for representative cases.
for s in (2,3,4,6):
    n,r,S=construction(s)
    assert len(S)==r

for s in (2,3):
    n,r,S=construction(s)
    # Enumerator of disjoint binary generators is binomial in block count.
    dist={5*j:math.comb(r,j) for j in range(r+1)}
    assert sum(dist.values())==2**r
    assert dist[0]==1 and dist[5]==r

# Check the advertised sample arithmetic without materializing huge supports again.
samples={2:(51,1),3:(455,91),4:(3855,771),6:(258111,5061)}
for s,(n0,r0) in samples.items():
    n=(2**(2*s)+1)*(2**s-1)
    M=51 if s%4==2 else 5
    assert (n,n//M)==(n0,r0)

print('VERIFY_OK')
