#!/usr/bin/env python3
"""Exact finite F_7 orbit and independent trace verification for eight-branch Howe curves."""
from itertools import combinations, product
from collections import Counter

p=7
F=frozenset(range(7))
P=list(range(7))+['inf']
SQ={i*i%7 for i in range(1,7)}
TS=list(combinations(range(7),3))
TIDX={t:i for i,t in enumerate(TS)}
STATES=[(t,a,b) for t in TS for a,b in product((0,1),repeat=2)]
IDX={v:i for i,v in enumerate(STATES)}
assert len(STATES)==140

def determinant(M):
 a,b,c,d=M
 return (a*d-b*c)%p

def inv(M):
 a,b,c,d=M
 z=pow(determinant(M),-1,p)
 return (d*z%p,-b*z%p,-c*z%p,a*z%p)

def point(M,t):
 a,b,c,d=M
 x,z=(1,0) if t=='inf' else (t,1)
 u,v=(a*x+b*z)%p,(c*x+d*z)%p
 return 'inf' if v==0 else u*pow(v,-1,p)%p

def multiply(f,g):
 r=[0]*(len(f)+len(g)-1)
 for i,x in enumerate(f):
  for j,y in enumerate(g):r[i+j]=(r[i+j]+x*y)%p
 return tuple(r)

def form(S):
 f=(1,)
 for t in P:
  if t in S:
   f=multiply(f,(1,0) if t=='inf' else (-t%p,1))
 assert len(f)==5
 return f

def evaluate(f,x,z):
 return sum(a*pow(x,i,p)*pow(z,4-i,p) for i,a in enumerate(f))%p

G=set()
for M in product(range(7),repeat=4):
 if not determinant(M):continue
 z=pow(next(a for a in M if a),-1,p)
 G.add(tuple(a*z%p for a in M))
G=sorted(G)
assert len(G)==336

def partition(t):
 A=frozenset(t)|{'inf'}
 return (A,frozenset(P)-A)

def action(M, index):
 t,a,b=STATES[index]
 A,B=partition(t)
 Am=frozenset(point(M,x) for x in A)
 Bm=frozenset(P)-Am
 C=Am if 'inf' in Am else Bm
 j=TIDX[tuple(sorted(C-{'inf'}))]
 N=inv(M)
 newbits=[]
 for S,bit in ((A,a),(B,b)):
  mapped=frozenset(point(M,x) for x in S)
  f,g=form(S),form(mapped)
  # The forms f(M^{-1}(X,Z)) and g(X,Z) have same roots,
  # so the following ratio is a constant, independent of the test point.
  for h in P:
   x,z=(1,0) if h=='inf' else (h,1)
   w=evaluate(g,x,z)
   if w:
    u=(N[0]*x+N[1]*z)%p
    v=(N[2]*x+N[3]*z)%p
    k=evaluate(f,u,v)*pow(w,-1,p)%p
    assert k
    newbits.append(bit^(k not in SQ))
    break
  else:raise AssertionError('No evaluation point')
 if 'inf' in Am:return IDX[(TS[j],*newbits)]
 return IDX[(TS[j],*newbits[::-1])]

PERMS={M:tuple(action(M,s) for s in range(140)) for M in G}
assert all(len(set(perm))==140 for perm in PERMS.values())
# Full projective representation check, against multiplication of 336 normalized matrices.
for M in G:
 for N in G:
  a,b,c,d=M;e,f,g,h=N
  Q=((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
  z=pow(next(k for k in Q if k),-1,p)
  Q=tuple(k*z%p for k in Q)
  pm,pn,pq=PERMS[M],PERMS[N],PERMS[Q]
  assert all(pm[pn[j]]==pq[j] for j in range(140))

unseen=set(range(140));orbits=[]
while unseen:
 q=min(unseen)
 orbit={perm[q] for perm in PERMS.values()}
 assert len(orbit)*sum(perm[q]==q for perm in PERMS.values())==336
 orbits.append(orbit)
 unseen-=orbit

def elliptic_trace(S,bit):
 f=form(S)
 v=0
 for h in P:
  x,z=(1,0) if h=='inf' else (h,1)
  y=evaluate(f,x,z)*(3 if bit else 1)%p
  v+=0 if y==0 else (1 if y in SQ else -1)
 return -v

def tracepair(index):
 t,a,b=STATES[index]
 A,B=partition(t)
 return tuple(sorted((elliptic_trace(A,a),elliptic_trace(B,b))))

actual={}
for orbit in orbits:
 spec={tracepair(i) for i in orbit}
 assert len(spec)==1
 actual[(len(orbit),next(iter(spec)))]=336//len(orbit)
assert actual=={
 (84,(0,0)):4,
 (14,(-4,-4)):24,
 (14,(4,4)):24,
 (28,(-4,4)):12,
},actual
# Check all 140 exact elliptic trace distributions without trusting orbit implementation
assert Counter(tracepair(i) for i in range(140))=={
 (0,0):84,(-4,-4):14,(4,4):14,(-4,4):28
}
part_orbits={}
for orbit in orbits:
 spec=next(iter({tracepair(i) for i in orbit}))
 part_orbits[spec]=len({STATES[i][0] for i in orbit})
assert part_orbits=={(0,0):21,(-4,-4):14,(4,4):14,(-4,4):14}
# Base-changing x -> ax+b and reciprocal x ->1/x generate projectivities.
# Independently count all image projectivities and partitions.
assert len({tuple(point(M,h) for h in P) for M in G})==336
print('HOWE_F7_MODULI_VERIFIED group=336 states=140 partitions=35 orbits=14,14,28,84 stabilizers=24,24,12,4')
for spec in ((-4,-4),(4,4),(-4,4),(0,0)):
 orbit=next(o for o in orbits if tracepair(min(o))==spec)
 t,a,b=STATES[min(orbit)]
 print('TRACE',spec,'size',len(orbit),'T',t,'twists',a,b,'base_partitions',len({STATES[i][0] for i in orbit}))
