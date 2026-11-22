#!/usr/bin/env python3
"""Exact finite-state certificate for a quadratic character sum of Stern numbers.

No external packages are needed. The proof uses Cayley--Hamilton on a
24-dimensional integer transition, not finite experimentation alone.
"""
from functools import lru_cache

P = 5
STATES = [(a,b) for a in range(P) for b in range(P) if (a,b)!=(0,0)]
assert len(STATES)==24

def chi(a):
    a %= 5
    return 0 if a==0 else (1 if a in (1,4) else -1)

def step(w):
    nxt={state: 0 for state in STATES}
    for (a,b), n in w.items():
        nxt[(a,(a+b)%P)] += n
        nxt[((a+b)%P,b)] += n
    return nxt

w={state: 0 for state in STATES}
w[(1,1)]=1
B=[]
for level in range(32):
    assert sum(w.values())==2**level
    B.append(sum(chi(a)*n for (a,b),n in w.items()))
    w=step(w)

# For each j=0,...,23, the exact scalar matrix identity
# c^T (T^4 - T^2 + 4I) T^j e_(1,1) = 0.
# The 24-dimensional Cayley--Hamilton theorem extends this to all j>=0.
for j in range(24):
    assert B[j+4]-B[j+2]+4*B[j] == 0, (j,B[j:j+5])
assert B[:8]==[1,0,-2,0,-6,0,2,0]

# Independent verification by integer Stern recursion, not the state matrix.
@lru_cache(None)
def stern(n):
    if n==0: return 0
    if n==1: return 1
    if n%2==0: return stern(n//2)
    m=n//2
    return stern(m)+stern(m+1)

for level in range(14):
    direct=sum(chi(stern(n)) for n in range(2**level,2**(level+1)))
    assert B[level]==direct,(level,B[level],direct)

# Independently test the reduced even-index recurrence.
b=[B[2*j] for j in range(16)]
assert b[0:4]==[1,-2,-6,2]
for j in range(14):
    assert b[j+2] == b[j+1]-4*b[j]
for j in range(1,16):
    assert b[j]%4==2
for level in range(1,32,2):
    assert B[level]==0
print('PASS: 24 exact Cayley-Hamilton certificates; 14 direct integer blocks; 32 state blocks')
print('B[0..15] =',B[:16])
