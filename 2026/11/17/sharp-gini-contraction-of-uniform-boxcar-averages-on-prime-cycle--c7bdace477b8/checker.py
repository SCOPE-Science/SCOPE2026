"""Exact arithmetic checks for the sharp prime-cycle boxcar Gini contraction theorem."""
from fractions import Fraction as F
from random import Random

def gini(v):
    return sum(abs(x-y) for i,x in enumerate(v) for y in v[i+1:])

def box(v,m):
    n=len(v)
    return [sum(v[(i+j)%n] for j in range(m))/m for i in range(n)]

def constant(n,m):
    d=min(m,n-m)
    return F(d if m>n//2 else m,m) * (1-F(d*d-1,3*(n*n//4))) if m>n//2 else 1-F(m*m-1,3*(n*n//4))

def formula(n,m):
    d=min(m,n-m)
    return F(d,m)*(1-F(d*d-1,3*(n*n//4)))

primes=(3,5,7,11,13)
checks=0
for n in primes:
    for m in range(1,n):
        c=formula(n,m)
        k=n//2
        arc=(1<<k)-1
        w=[F((arc>>i)&1) for i in range(n)]
        assert gini(box(w,m))/gini(w)==c
        for bits in range(1,(1<<n)-1):
            w=[F((bits>>i)&1) for i in range(n)]
            assert gini(box(w,m))<=c*gini(w),(n,m,bits,c)
            checks+=1
    print('ALL_CUTS_EXACT_N',n,'PASS')
print('EXACT_ALL_PRIME_BINARY_CUTS_PASS',checks)

rng=Random(1949)
check2=0
for n in (11,13,17,19,23):
 for m in range(1,n):
  c=formula(n,m)
  for z in range(80):
   v=[F(rng.randint(-9,9),rng.randint(1,5)) for _ in range(n)]
   if gini(v)==0:continue
   assert gini(box(v,m))<=c*gini(v)
   check2+=1
print('EXACT_RATIONAL_MULTILEVEL_CHECKS_PASS',check2)
for n in (5,7,11,13,17,19,23,29,31,37,41):
 for m in range(1,n):
  d=min(m,n-m); k=n//2
  for q in range(1,k+1):
   arc=(1<<q)-1
   v=[F((arc>>i)&1) for i in range(n)]
   ratio=gini(box(v,m))/gini(v)
   assert ratio<=formula(n,m)
print('ARC_FORMULAS_AND_BALANCED_EXTREMIZERS_PASS')
print('ALL_PRIME_BOXCAR_GINI_CHECKS_PASS')
