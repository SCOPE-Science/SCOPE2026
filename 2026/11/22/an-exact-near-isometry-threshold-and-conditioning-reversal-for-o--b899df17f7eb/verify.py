"""Exact rational certificate for the one-collision Gram spectra.
Requires only the Python standard library. Run: python verify.py
"""
from fractions import Fraction as F
from math import comb


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def charpoly(A):
    """Monic polynomial in descending powers by Faddeev-LeVerrier."""
    n=len(A)
    B=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    co=[F(1)]
    for k in range(1,n+1):
        C=mm(A,B)
        ck=-sum(C[i][i] for i in range(n))/k
        co.append(ck)
        B=[[C[i][j]+(ck if i==j else 0) for j in range(n)] for i in range(n)]
    return co

def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return r

def predicted(n,ell,kind):
    z=[F(1),F(0)]
    for _ in range(n-3):z=mul(z,[F(1),F(-1)])
    if kind=='cycle-good': q=[F(1),-F(2)-F(2,ell),F(4,ell)]
    elif kind=='cycle-bad': q=[F(1),-F(2)+F(2,ell),F(0)]
    elif kind=='cross': q=[F(1),F(-2),F(1,ell)]
    elif kind=='tree-tree': q=[F(1),F(-2),F(0)]
    else:raise ValueError(kind)
    return mul(z,q)

def projected_gram(n,ell,i,j,tau,orientation):
    c=[F(orientation[k]) if k<ell else F(0) for k in range(n)]
    P=[[F(int(a==b))-c[a]*c[b]/ell for b in range(n)] for a in range(n)]
    H=[[F(int(a==b)) for b in range(n)] for a in range(n)]
    H[i][j]=H[j][i]=F(tau)
    return mm(mm(P,H),P)

checks=0
for n in range(3,10):
  for ell in range(3,n+1):
    orientation=[1 if k%2==0 else -1 for k in range(ell)]+[0]*(n-ell)
    for i in range(n):
      for j in range(i+1,n):
        for tau in (-1,1):
          if i<ell and j<ell:
            kind='cycle-good' if tau*orientation[i]*orientation[j]==-1 else 'cycle-bad'
          elif i<ell or j<ell:kind='cross'
          else:kind='tree-tree'
          actual=charpoly(projected_gram(n,ell,i,j,tau,orientation))
          expected=predicted(n,ell,kind)
          assert actual==expected,(n,ell,i,j,tau,kind,actual,expected)
          checks+=1
# Independent exact exhaustive rank frequency for the triangle with 3 buckets.
# There are 3^3 hash maps, and 2^3 independent sign assignments.
import itertools
rank_success=0
for hashes in itertools.product(range(3),repeat=3):
  for sig in itertools.product((-1,1),repeat=3):
    counts={h:hashes.count(h) for h in range(3)}
    if sorted(counts.values())==[1,1,1]:rank_success+=1
    elif sorted(counts.values())==[0,1,2]:
      i,j=[k for k in range(3) if counts[hashes[k]]==2]
      if sig[i]!=sig[j]:rank_success+=1
# m=n=ell=3: F3(3)=6; F2(3)=6; cycle pairs=3, half safe => probability (6+9)/27=5/9.
assert F(rank_success,3**3*2**3)==F(5,9)
# Independent four-edge/three-bucket count, all hash and sign configurations.
pass_eps=0
rank_ok=0
for hashes in itertools.product(range(3),repeat=4):
  occ={h:hashes.count(h) for h in range(3)}
  for sig in itertools.product((-1,1),repeat=4):
    if sorted(occ.values())==[1,1,1]:
      # Impossible with four edges and three buckets.
      raise AssertionError('bad occupancy')
    if sorted(occ.values()) != [1,1,2]:continue
    i,j=[k for k in range(4) if occ[hashes[k]]==2]
    if i<3 and j<3:
      if sig[i]!=sig[j]:rank_ok+=1
    elif i<3 or j<3:
      rank_ok+=1
      pass_eps+=1
assert F(pass_eps,3**4*2**4)==F(2,9)
assert F(rank_ok,3**4*2**4)==F(1,3)
print(f'PASS: {checks} exact rational characteristic-polynomial checks; 216-case triangle and 1296-case pendant-triangle enumerations')
