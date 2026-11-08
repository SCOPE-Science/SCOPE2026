"""Independent exact finite-field tests for cycle polynomial discriminants.
No floating-point trigonometry is used."""
from itertools import combinations, product
from random import Random
from math import comb
P=1000000007
I2=pow(2,-1,P)
rng=Random(724901)
def root(z,eps):
    w=1
    for a,e in zip(z,eps):
        w=w*(a if e==1 else pow(a,-1,P))%P
    return (w+pow(w,-1,P))*I2%P
def differences(xs):
    ans=1
    for a,b in combinations(xs,2): ans=ans*(a-b)**2%P
    return ans
def check(m,z):
    reps=[(1,)+t for t in product((-1,1),repeat=m-1)]
    roots=[root(z,e) for e in reps]
    d=len(roots)
    disc=differences(roots)
    rhs=pow(2,d*(d-1),P)
    for mask in range(1,(1<<m)-1):
        S=[i for i in range(m) if mask>>i&1]
        zs=[z[i] for i in S]
        ps=1
        for tup in product((-1,1),repeat=len(S)-1):
            rs=root(zs,(1,)+tup)
            ps=ps*(1-rs*rs)%P
        rhs=rhs*pow(ps,1<<(m-len(S)-1),P)%P
    assert disc==rhs,(m,disc,rhs)
    return disc
for m in range(2,9):
 for i in range(5):
    z=[rng.randrange(2,1000000) for j in range(m)]
    check(m,z)
 print('FINITE_FIELD_DISCRIMINANT_OK',m,'degree',1<<(m-1))
print('ALL_DISCRIMINANT_IDENTITY_TESTS_OK')
# Independent numeric check of lower-cycle-polynomial factor identity for |S|>=3
for s in range(3,9):
 for trial in range(5):
  z=[rng.randrange(2,1000000) for _ in range(s)]
  x=[(a+pow(a,-1,P))*I2%P for a in z]
  p=1
  for eps in product((-1,1),repeat=s-1):
   r=root(z,(1,)+eps)
   p=p*(1-r*r)%P
  gam=1; gamneg=1
  for eps in product((-1,1),repeat=s-2):
   r=root(z[1:],(1,)+eps)
   gam=gam*(x[0]-r)%P
   gamneg=gamneg*(-x[0]-r)%P
  assert p == (gam*gamneg)**2%P,(s,p,gam, gamneg)
 print('CYCLE_FACTOR_COMPONENT_OK',s)
print('ALL_COMPONENT_TESTS_OK')
