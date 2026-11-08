"""Exact finite sublemmas and independent finite tests for the sharp split-product inequality."""
from fractions import Fraction
from itertools import combinations
from math import prod

# The proof reduces its three-extra-factor case to these 24 rational comparisons.
checks3=[]
for u in range(2,32):
    for v in range(u+1,32):
        if u*v>31:
            break
        m=v+1
        lhs=Fraction(2*m*u*v,m+u+v)
        rhs=Fraction(m+2,m+1)**(m+u+v-1)
        assert lhs>rhs,(u,v,lhs,rhs)
        checks3.append((u,v))
assert len(checks3)==24

# Two-extra-factor case, with the isolated (2,3) vector treated separately.
checks2=[]
for u in range(3,8):
    v=u+1
    lhs=Fraction(2*u*v,u+v)
    rhs=Fraction(v+2,v+1)**(u+v-1)
    assert lhs>rhs,(u,v)
    checks2.append((u,v))
u,v=2,4
assert Fraction(2*u*v,u+v)>Fraction(v+2,v+1)**(u+v-1)

# For (2,3), exhaust all compositions of D into b positive summands,
# where 1<=b<=D<=4, and bound the product of distortion factors.
def comps(n,b):
    if b==1:
        yield (n,)
    else:
        for z in range(1,n-b+2):
            for tail in comps(n-z,b-1):
                yield (z,)+tail
all_special=[]
for D in range(1,5):
    for b in range(1,D+1):
        for ds in comps(D,b):
            val=prod((Fraction(j+4+delta,j+4) for j,delta in enumerate(ds)))
            # u_(a+j) >= 3+j, for j=1,2,...
            assert val<=Fraction(21,10), (D,b,ds,val)
            all_special.append(val)
assert max(all_special)==Fraction(21,10)

# Fully independent finite trial: all separated U,V in [2,13],
# letting x=max U, G=min V-x (the largest possible value of G).
sets=0
best=(Fraction(100),None)
for x in range(3,12):
    small=range(2,x+1)
    large=range(x+1,14)
    for r in range(2,min(7,x)+1):
        for U in combinations(small,r):
            if max(U)!=x:continue
            for b in range(1,min(r,4)):
                for V in combinations(large,b):
                    d=sum(U)-sum(V)
                    if d<=0:continue
                    G=min(V)-x
                    ratio=Fraction(2*prod(U),(d+G)*prod(V))
                    assert ratio>=1,(U,V,x,G,d,ratio)
                    if ratio<best[0]:best=(ratio,(U,V))
                    sets+=1
assert sets>500
print('VERIFY_OK', 'three_extra_rational_cases=',len(checks3),
      'two_extra_rational_cases=',len(checks2)+1,
      'exception_distortion_cases=',len(all_special),
      'independent_set_pairs=',sets,
      'small_range_min_ratio_twice_constant=',best[0],
      'sharp_family_limit=1/2')
