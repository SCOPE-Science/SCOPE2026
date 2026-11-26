#!/usr/bin/env python3
"""Reproducibility checks for a ternary periodic-word MAS enumerator.
Requires Python 3 standard library only.
"""
from collections import defaultdict
from itertools import product, permutations

Q=3
STATES=list(product(range(Q),repeat=2))
D=[1,-3,2,-4,2,-3,1]
# P_(a,b) in increasing order of polynomial degree, states lexicographic.
P=[
 [1,1,2,1,2,-1],            # (0,0)
 [0,1,0,2,-1],              # (0,1) = x+2x^3-x^4
 [0,2,-1,1],                # (0,2)
 [1,0,2,-1,3,-1],           # (1,0)
 [1,0,2,-1],                # (1,1)
 [0,1,0,-1],                # (1,2) = x-x^3
 [1,-2,3,-2,3,-1],          # (2,0)
 [1,-1,2],                  # (2,1)
 [1,0,-1],                 # (2,2)
]
N=[0,6,-2,10,-3,8,-3]

def add(A,B):
 C=[0]*max(len(A),len(B))
 for i,v in enumerate(A):C[i]+=v
 for i,v in enumerate(B):C[i]+=v
 while len(C)>1 and C[-1]==0:C.pop()
 return C

def scale(A,k): return [a*k for a in A]

def mul(A,B):
 C=[0]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):C[i+j]+=a*b
 return C

def same(A,B):
 n=max(len(A),len(B));return A+[0]*(n-len(A))==B+[0]*(n-len(B))

def delta(a,b,c):return int(a>=b)+int(b>=c)-int(a>=c)

# Independently check finite polynomial identity (I-M) P=D e, and vP=N.
for i,(a,b) in enumerate(STATES):
 lhs=P[i]
 for c in range(Q):
  if delta(a,b,c)>=1:
   j=STATES.index((b,c))
   lhs=add(lhs,scale(mul(P[j],[0,1] if b>=c else [1]),-1))
 rhs=D if a>=b else [0]
 assert same(lhs,rhs),(a,b,lhs,rhs)
value=[0]
for i,(a,b) in enumerate(STATES):
 if a>=b:value=add(value,mul(P[i],[0,1]))
assert same(value,N),(value,N)
print('CERT_IDENTITY_OK: 9 polynomial equations plus numerator')

# Rational coefficient recurrence computed separately from finite-state counts.
rat=[0]*19
for m in range(1,len(rat)):
 rat[m]=((N[m] if m<len(N) else 0)-sum(D[j]*rat[m-j] for j in range(1,min(m,len(D)-1)+1)))
count=defaultdict(int)
for a,b in STATES:
 if a>=b:count[(a,b,1)]+=1
transfers=[0]*19
for l in range(2,40):
 for (a,b,desc),n in count.items():
  if desc<len(transfers) and a>=b:transfers[desc]+=n
 nxt=defaultdict(int)
 for (a,b,desc),n in count.items():
  for c in range(Q):
   d=desc+int(b>=c)
   if d<len(transfers) and delta(a,b,c)>=1:
    nxt[(b,c,d)]+=n
 count=nxt
assert transfers==rat,(transfers,rat)
print('RATIONAL_COUNTS_OK:',rat[1:13])

# Definition-level brute force, not using the local triple characterization.
def emb(u,w):
 pos=0
 for ch in u:
  while pos<len(w) and w[pos]!=ch:pos+=1
  if pos==len(w):return False
  pos+=1
 return True

for m in (1,2,3):
 w=tuple(range(3))*m
 direct=defaultdict(int)
 for L in range(2,3*m+2):
  for u in product(range(3),repeat=L):
   if emb(u,w):continue
   if all(emb(u[:i]+u[i+1:],w) for i in range(L)):
    direct[L]+=1
 assert sum(direct.values())==rat[m],(m,direct,rat[m])
 assert {1:{2:6},2:{3:10,4:6},3:{4:15,5:30,6:1}}[m]==dict(direct)
 print('EXHAUSTIVE_MAS_OK:',m,sorted(direct.items()))

for perm in permutations(range(3)):
 for m in (1,2):
  w=tuple(perm)*m
  direct=0
  for L in range(2,3*m+2):
   for u in product(range(3),repeat=L):
    if not emb(u,w) and all(emb(u[:i]+u[i+1:],w) for i in range(L)):direct+=1
  assert direct==rat[m]
print('PERMUTATION_INVARIANCE_OK: 12 cases')
print('VERIFY_OK')
