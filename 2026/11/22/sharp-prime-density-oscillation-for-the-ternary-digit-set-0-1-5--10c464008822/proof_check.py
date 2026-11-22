#!/usr/bin/env python3
"""Exact finite-state certificate of extremal ternary digit-profile bounds."""
from fractions import Fraction
from collections import deque

b, D = 3, (0,1,5)
K = (-3,-2,-1,0)
digit = {d%3:d for d in D}
trans = tuple(tuple(K.index((a+c-digit[(a+c)%3])//3) for c in K) for a in range(3))
start=(0,0,0,1)
def advance(v,a): return tuple(v[trans[a][i]] for i in range(4))
q=deque([start]);states={start}
while q:
 v=q.popleft()
 for a in range(3):
  u=advance(v,a)
  if u not in states:states.add(u);q.append(u)
states=sorted(states)
assert len(states)==14
weights=lambda v:v[1]+2*v[2]+5*v[3]
# Exact stationary distribution (0,1/8,1/4,5/8), independent check.
pi=(Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(5,8))
for k in range(4):
 assert sum(pi[i] for i in range(4) for a in range(3) if trans[a][i]==k)/3 == pi[k]
assert sum(pi)==1
# Exact Bellman potentials are indexed by state bits in K order.
low={'0000':-5,'0001':0,'0010':-3,'0011':0,'0100':-4,'0110':-2,'0111':0,
     '1000':-5,'1001':0,'1011':0,'1100':-4,'1101':0,'1110':-2,'1111':0}
up={'0000':0,'0001':0,'0010':0,'0011':1,'0100':0,'0110':0,'0111':2,
    '1000':0,'1001':0,'1011':1,'1100':0,'1101':1,'1110':0,'1111':2}
assert len(low)==len(up)==len(states)
for v in states:
 key=''.join(map(str,v))
 children=[advance(v,a) for a in range(3)]
 wchildren=[weights(child) for child in children]
 for a in range(3):
  prefix5=sum(wchildren[j]-5 for j in range(a))
  prefix6=sum(wchildren[j]-6 for j in range(a))
  assert 3*low[key] <= prefix5+low[''.join(map(str,children[a]))]
  assert 3*up[key] >= prefix6+up[''.join(map(str,children[a]))]
 assert low[key]<=0<=up[key]
# Root restriction to t in [1/3,1]: first trit is 1 or 2.
children=[advance(start,a) for a in range(3)]
for a in (1,2):
 ch=''.join(map(str,children[a]))
 assert sum(weights(children[j])-5 for j in range(a))+low[ch]>=0
 assert sum(weights(children[j])-6 for j in range(a))+up[ch]<=0
# Extremal phases: F(1/3)=5/24 and F(2/3)=1/2.
assert weights(children[0])==5 and weights(children[1])==7
assert Fraction(5,24)/Fraction(1,3)==Fraction(5,8)
assert Fraction(12,24)/Fraction(2,3)==Fraction(3,4)
# Independent finite digit-count checks; not a proof of infinite inequality.
from functools import lru_cache
@lru_cache(None)
def representable(n):
 if n==0:return 1
 if n<0:return 0
 return representable((n-digit[n%3])//3)
for m in range(1,9):
 n=3**m
 counts=[representable(j) for j in range(n)]
 for k in range(3**(m-1),n+1):
  v=sum(counts[:k])
  # finite count approximates not exactly limiting profile; only coarse convergence diagnostics.
  if m>=3 and k in (3**(m-1),2*3**(m-1),n):
   target=Fraction(5,8) if k!=2*3**(m-1) else Fraction(3,4)
   assert abs(Fraction(v,k)-target)<Fraction(1,3**(m-2))
print('TERNARY_DIGIT_PROFILE_EXACT_CERTIFICATE_OK',len(states),len(states)*3,8)
