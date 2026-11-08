"""Reproduce exact windmill resistance identities and budget-optimality examples.
Uses only Python 3 standard library. No external data or networks required.
"""
from fractions import Fraction as Q
from random import Random

def inv(mat):
    n=len(mat); a=[[Q(z) for z in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(mat)]
    for k in range(n):
        piv=next((i for i in range(k,n) if a[i][k]),None)
        assert piv is not None, 'disconnected test graph'
        a[k],a[piv]=a[piv],a[k]
        z=a[k][k];a[k]=[v/z for v in a[k]]
        for i in range(n):
            if i!=k:
                z=a[i][k]
                if z: a[i]=[v-z*w for v,w in zip(a[i],a[k])]
    return [row[n:] for row in a]

def resistance(m,r,spoke,blade):
    # Exact trace of the grounded inverse, independently evaluated per blade.
    # Internal edge (i,j), i<j in blade k, is represented by blade[k][(i,j)].
    n=1+m*r; tr=Q(0); total=Q(0)
    for k in range(m):
        mat=[[Q(0) for _ in range(r)] for _ in range(r)]
        for i in range(r):
            mat[i][i]+=spoke[k][i]
        for (i,j),w in blade[k].items():
            mat[i][i]+=w;mat[j][j]+=w
            mat[i][j]-=w;mat[j][i]-=w
        im=inv(mat)
        tr+=sum(im[i][i] for i in range(r))
        total+=sum(sum(row) for row in im)
    return n*tr-total

def uniform(m,r,x,y):
    s=[[x]*r for _ in range(m)]
    t=[{(i,j):y for i in range(r) for j in range(i+1,r)} for _ in range(m)]
    return resistance(m,r,s,t)

def analytic(m,r,x,y):
    n=m*r+1;return m*(Q(r*(m-1)+1)/x+Q(n*(r-1))/(x+r*y))

checks=0
for m in range(2,5):
 for r in range(2,5):
  for x in [Q(1,2),Q(3,5),Q(2)]:
   for y in [Q(0),Q(2,7),Q(4,3)]:
    assert uniform(m,r,x,y)==analytic(m,r,x,y)
    checks+=1
  n=m*r+1; a=Q(1); aa=Q(r*(m-1)+1); dd=Q(n*(r-1)); q=Q(2)
  bb=Q(2)*dd*r*a/(Q(r-1)*(dd+q*q*aa))
  assert bb>0 and bb<Q(2)*n*a/Q(n-1)
  yy=Q(1,r); xx=Q(1); zz=xx+r*yy
  assert zz/xx==q
  budget=m*(r*a*xx+Q(r*(r-1),2)*bb*yy)
  assert analytic(m,r,xx,yy)<analytic(m,r,budget/(m*r*a),Q(0))
  alpha=r*a-Q(r-1,2)*bb;beta=Q(r-1,2)*bb
  assert dd*alpha==q*q*aa*beta
  # Exact stationary condition for the one-dimensional strictly convex profile.
  assert alpha*xx+beta*zz==budget/m
  assert aa*beta==dd*alpha/q**2
  checks+=5
  # At and above the sharp price threshold, every cycle edge is excluded.
  for bb in [Q(2)*n*a/Q(n-1),Q(3)*n*a/Q(n-1)]:
   budget=Q(2*m*r);x=budget/(m*r*a)
   assert analytic(m,r,x,Q(0))==Q((n-1)**2)/x
   alpha=r*a-Q(r-1,2)*bb;beta=Q(r-1,2)*bb
   assert beta*aa>=alpha*dd
   checks+=2

# Arbitrary (not symmetry-restricted) feasible designs, exact comparison.
rng=Random(1729)
for m,r in [(2,2),(2,3),(3,2),(2,4)]:
 n=m*r+1;aa=Q(r*(m-1)+1);dd=Q(n*(r-1));a=Q(1)
 q=Q(2); b=Q(2)*dd*r/(Q(r-1)*(dd+q*q*aa))
 budget=m*(r*a+Q(r-1,2)*b*(q-1))
 optimum=analytic(m,r,Q(1),Q(q-1,r))
 for v in range(90):
  spokes=[[Q(rng.randrange(1,8),rng.randrange(1,7)) for _ in range(r)] for _ in range(m)]
  blades=[{(i,j):Q(rng.randrange(0,8),rng.randrange(1,8)) for i in range(r) for j in range(i+1,r)} for _ in range(m)]
  cost=a*sum(map(sum,spokes))+b*sum(sum(row.values()) for row in blades)
  factor=budget/cost
  spokes=[[z*factor for z in row] for row in spokes]
  blades=[{ij:z*factor for ij,z in row.items()} for row in blades]
  assert resistance(m,r,spokes,blades)>=optimum
  checks+=1
print('VERIFY_OK',checks)
