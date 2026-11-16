"""Exact small-rank checks for unitary Steinberg projector formulas.
Standard library only. This checks a rational coefficient product and independently
enumerates the unitary three-space over F4 via its isotropic-line building.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb

def mu(k):
    c = 0
    p = 2
    while p*p <= k:
        if k % p == 0:
            k //= p
            c += 1
            if k % p == 0: return 0
            while k % p == 0: k //= p
        p += 1
    if k > 1: c += 1
    return (-1)**c

def orbit_count(q,d):
    x=sum(mu(d//e)*(q**e-(-1)**e) for e in range(1,d+1) if d%e==0)
    assert x%d==0
    return x//d

def mul(A,B,M):
    C=[Q(0)]*(M+1)
    for i,a in enumerate(A):
        if not a: continue
        for j,b in enumerate(B[:M+1-i]):
            C[i+j]+=a*b
    return C

def power(A,n,M):
    B=[Q(1)]+[Q(0)]*M
    while n:
        if n&1: B=mul(B,A,M)
        n//=2
        if n: A=mul(A,A,M)
    return B

def coeffs(q,M):
    H=[Q(1)]+[Q(0)]*M
    for d in range(1,M+1):
        B=[Q(0)]*(M+1); B[0]=1
        a=Q(1)
        for m in range(1,M//d+1):
            a/=q**(d*m)-(-1)**(d*m)
            B[d*m]=a
        H=mul(H,power(B,orbit_count(q,d),M),M)
    return H

for q in (2,3,4,5):
    a=coeffs(q,7)
    assert a[0] == 1 and a[1] == 1
    assert a[2] == Q(q,q+1)
    assert a[3] == Q(q*(q-1)*(q*q+q+1),(q+1)**2*(q*q-q+1))
    assert all(v>0 for v in a)
    print('q',q,'A_0..A_5', [str(x) for x in a[:6]])

# Independent enumeration of U_3(2) and rank-one building character.
# Construct F_4 as F_2[t]/(t^2+t+1).
mult=[[0]*4 for _ in range(4)]
for x in range(4):
 for y in range(4):
  u=0
  for i in range(2):
   for j in range(2):
    if ((x>>i)&(y>>j)&1): u^=(1<<(i+j))
  if u&4: u^=7
  mult[x][y]=u
conj=[mult[x][x] for x in range(4)]
def herm(a,b):
 s=0
 for x,y in zip(a,b): s^=mult[x][conj[y]]
 return s
v=list(product(range(4),repeat=3))
norm1=[a for a in v if herm(a,a)==1]
iso=[a for a in v if a!=(0,0,0) and herm(a,a)==0]
def canon(a):return min(tuple(mult[t][x] for x in a) for t in (1,2,3))
lines=set(canon(x) for x in iso)
assert len(lines)==9
G=[(a,b,c) for a in norm1 for b in norm1 if herm(a,b)==0 for c in norm1 if herm(a,c)==0 and herm(b,c)==0]
assert len(G)==648
def action(g,x):
 return tuple(mult[g[0][i]][x[0]]^mult[g[1][i]][x[1]]^mult[g[2][i]][x[2]] for i in range(3))
h=Counter()
for g in G:
    fix=sum(canon(action(g,line))==line for line in lines)
    h[fix-1]+=1
assert h==Counter({0:405,-1:168,2:72,8:3}),h
# Rank-one building Steinberg character = fixed points -1.
L=Q(8*sum(abs(t)*k for t,k in h.items()),len(G))
assert L==Q(112,27)
assert L/8==coeffs(2,3)[3]
print('U3(2) conjugacy-agnostic Steinberg value frequencies',dict(sorted(h.items())))
print('U3(2) projector endpoint norm',L)
print('UNITARY_STEINBERG_EXACT_CHECKS_PASS')
