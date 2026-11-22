#!/usr/bin/env python3
"""Recompute the finite carry certificate and low-depth direct Franel checks."""
from fractions import Fraction
from math import comb
from itertools import product
A = (0, 1, 3, 4)
S = list(product((0, 1), repeat=3))
EXPECTED = {
 (0,0,0):(12,4,4,4,4), (0,0,1):(8,5,6,5,8),
 (0,1,0):(8,5,6,5,8), (0,1,1):(7,5,5,7,8),
 (1,0,0):(8,7,5,5,7), (1,0,1):(8,5,6,5,8),
 (1,1,0):(8,5,6,5,8), (1,1,1):(4,4,4,4,12)
}
W = lambda s: 3 if s in ((0,0,0),(1,1,1)) else 2

def nxt(s, a):
 c1,c2,t = s
 b,t1 = (2*a+t)%5,(2*a+t)//5
 ans=[]
 for d in A:
  x,y=d+a+c1,d+b+c2
  if x%5 in A and y%5 in A:
   ans.append((x//5,y//5,t1))
 return ans
for s in S:
 vals=tuple(sum(W(u) for u in nxt(s,a)) for a in range(5))
 assert vals==EXPECTED[s],(s,vals)
 assert all(v <= 4*W(s) for v in vals)
for a in (1,2):
 assert sorted(nxt((0,0,0),a))==[(0,1,0),(1,1,0)]
for a in (3,4):
 assert sorted(nxt((0,0,0),a))==[(0,0,1),(1,0,1)]
assert all(sorted(nxt(s,4)).count((1,1,1))==2 for s in [(0,0,1),(0,1,0),(1,0,1),(1,1,0)])

# Exact probability for an all-zero tail, verified against the transition equations.
Q={(0,0,0):Fraction(1), (0,0,1):Fraction(2,3),
   (0,1,0):Fraction(2,3), (0,1,1):Fraction(7,12),
   (1,0,0):Fraction(2,3), (1,0,1):Fraction(2,3),
   (1,1,0):Fraction(2,3), (1,1,1):Fraction(1,3)}
for s in S:
 assert Q[s]==sum((Q[u] for u in nxt(s,0)),Fraction(0))/4
assert all(Q[s]==Fraction(2,3) for s in [(0,0,1),(0,1,0),(1,0,1),(1,1,0)])

# Compute exact limiting overlap from the finite digits of h, followed by the zero tail.
def limit(h):
 digits=[]
 while h:
  digits.append(h%5); h//=5
 curr={(0,0,0):Fraction(1)}
 for a in digits:
  nd={}
  for s,p in curr.items():
   for u in nxt(s,a):nd[u]=nd.get(u,Fraction(0))+p/4
  curr=nd
 return sum((v*Q[u] for u,v in curr.items()),Fraction(0))
for h in range(1,2001):
 v=limit(h)
 h0=h
 while h0%5==0:h0//=5
 eq =h0 in (1,2,3,4)
 assert (v==Fraction(1,3))==eq,(h,v)
 assert 0<=v<=Fraction(1,3)

# Direct Franel values and the independently checked base-five digit criterion.
for n in range(500):
 f=sum(comb(n,j)**3 for j in range(n+1))
 m=n
 digit_ok=True
 while m:
  if m%5==2:digit_ok=False
  m//=5
 assert (f%5!=0)==digit_ok

# Direct unwrapped block counts for several shifts, compared to limit at increasing depth.
finite_checks=0
for h in list(range(1,45))+[50,75,100,125]:
 for r in range(3,6):
  if h>=5**r:continue
  def allowed(n):
   while n:
    if n%5==2:return False
    n//=5
   return True
  count=sum(allowed(n) and allowed(n+h) and allowed(n+2*h) for n in range(5**r))
  # Independent carry count with *deterministic* zero digits beyond the block.
  hd=[];t=h
  for i in range(r): hd.append(t%5);t//=5
  assert t==0
  dic={(0,0,0):1}
  for a in hd:
   nd={}
   for state,v in dic.items():
    for u in nxt(state,a):nd[u]=nd.get(u,0)+v
   dic=nd
  def terminal_accept(state):
   c1,c2,carry=state
   for i in range(4):
    b=carry
    x,y=c1,b+c2
    if x%5 not in A or y%5 not in A:return False
    c1,c2,carry=x//5,y//5,0
    if (c1,c2,carry)==(0,0,0):return True
   raise AssertionError('carry not cleared')
  predicted=sum(v for state,v in dic.items() if terminal_accept(state))
  assert predicted==count,(h,r,predicted,count)
  finite_checks+=1
print(f'VERIFY_OK states=8 transitions=40 direct_franel=500 tested_shifts=2000 finite_counts={finite_checks}')
