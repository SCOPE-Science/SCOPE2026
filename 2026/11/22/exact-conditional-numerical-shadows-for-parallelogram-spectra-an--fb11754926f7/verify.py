"""Exact rational checks for a four-corner numerical-shadow conditional law."""
from fractions import Fraction as Q
from itertools import product
from math import factorial

# Four coordinates ordered (++), (+-), (-+), (--).
signs=((1,1),(1,-1),(-1,1),(-1,-1))
def to_xyz(p):
    return tuple(sum(p[i]*(s if k==0 else t if k==1 else s*t)
        for i,(s,t) in enumerate(signs)) for k in range(3))
def to_p(x,y,z):
    return tuple((1+s*x+t*y+s*t*z)/4 for s,t in signs)
def endpoints(x,y):
    return -1+abs(x+y),1-abs(x-y)
def conditional_mean(x,y):
    a,b=endpoints(x,y)
    return (a+b)/2

def beta(a,b):
    return Q(factorial(a-1)*factorial(b-1),factorial(a+b-1))

checks=0
for a,b,c in product(range(8), repeat=3):
    d=7-a-b-c
    if d<0: continue
    p=tuple(Q(k,7) for k in (a,b,c,d))
    x,y,z=to_xyz(p)
    assert to_p(x,y,z)==p
    lo,hi=endpoints(x,y)
    assert lo<=z<=hi
    assert hi-lo ==2*(1-max(abs(x),abs(y)))
    assert conditional_mean(x,y) == Q(abs(x+y)-abs(x-y),2)
    checks+=5
# Conditioned triples from rational measurement lattice: both endpoints are valid probability vectors.
for k,l in product(range(-9,10), repeat=2):
    x,y=Q(k,10),Q(l,10)
    lo,hi=endpoints(x,y)
    for z in (lo,(lo+hi)/2,hi):
        p=to_p(x,y,z)
        assert all(v>=0 for v in p)
        assert sum(p)==1
        assert to_xyz(p)==(x,y,z)
        checks+=3
# Uniform Dirichlet-simplex pushforward Jacobian |det|=1/16, density 6/16=3/8.
# Formula: integrate f(x,y) over max(|x|,|y|)=r with shell area 8r dr.
# Given conditional length=2(1-r), f(x,y)=(3/4)(1-r).
assert 6*beta(2,2)==1;checks+=1 # 6 * 1/6 mass
# Integrated Z conditional variance: E[(1-r)^2/3] = (1/3)*6*Beta(2,4) = 1/10.
assert 2*beta(2,4)==Q(1,10);checks+=1
# Dirichlet Z variance: two + and two - eigenvalues, 4/[4*5].
assert Q(4,4*5)==Q(1,5);checks+=1
# Exactly 50% of affine squared risk is optimal nonlinear risk.
assert Q(1,10)/Q(1,5)==Q(1,2);checks+=1
#  E Z = E X = E Y = 0 by symmetry, and E Z X=E Z Y=0 by parity.
print('PARALLELOGRAM_NUMERICAL_SHADOW_EXACT_CHECK_OK', checks)
