"""Exact checks for the cyclic order-27 quartic-threefold quotient.

This program uses only the Python standard library and SymPy. It verifies
finite eigenweight combinatorics, local representations, and an exact
smoothness witness, without replacing the general geometric arguments.
"""
from math import gcd
from collections import Counter
import sympy as sp

W = (1,24,18,9,0)
# Monomial exponent vectors for the invariant quartic family.
MONOMIALS = (
    (3,1,0,0,0),(0,3,0,1,0),(0,0,3,0,1),
    (0,0,0,3,1),(0,0,0,0,4),(0,0,2,2,0),(0,0,1,1,2)
)
assert all(sum(a*b for a,b in zip(e,W)) % 27 == 0 for e in MONOMIALS)

# Compute projective eigenspace blocks for each nontrivial element.
def blocks(k):
    B={}
    for i,w in enumerate(W,1): B.setdefault((k*w)%27,[]).append(i)
    return tuple(sorted(tuple(v) for v in B.values()))

counts=Counter()
for k in range(1,27):
    b=blocks(k)
    if gcd(k,27)==1:
        assert all(len(t)==1 for t in b)
        counts['four-coordinate-fixed']+=1
    elif gcd(k,27)==3:
        assert b==((1,), (2,), (3,4,5)),(k,b)
        counts['plane-curve-plus-two']+=1
    elif gcd(k,27)==9:
        assert b==((1,), (2,3,4,5)),(k,b)
        counts['quartic-surface-plus-one']+=1
assert counts=={'four-coordinate-fixed':18,'plane-curve-plus-two':6,'quartic-surface-plus-one':2}

# All projectively fixed coordinate points are e1,e2,e3,e4, not e5.
# The smooth hypersurface tangent coordinates omit the variable indicated.
tangent_free={1:(3,4,5),2:(1,3,5),3:(1,2,4),4:(1,2,3)}
expect={1:(17,8,26),2:(4,21,3),3:(10,6,18),4:(19,15,9)}
for i,t in tangent_free.items():
    assert tuple((W[j-1]-W[i-1])%27 for j in t)==expect[i]

# Quotient first by the order-three reflection at e2,e3,e4.
# The first transverse coordinate is cubed, then residual order-nine weights.
reduced={i:((v[0]%9),v[1]//3,v[2]//3) for i,v in expect.items() if i!=1}
assert reduced[2]==(4,7,1)
assert reduced[3]==(1,2,6)
assert reduced[4]==(1,5,3)
assert sorted((5*x)%9 for x in reduced[3])==sorted(reduced[4])

def min_age(weights,n):
    sums=[sum((k*w)%n for w in weights) for k in range(1,n)]
    return sp.Rational(min(sums),n)
assert min_age(expect[1],27)==sp.Rational(1,3)
assert min_age(reduced[2],9)==1
assert min_age(reduced[3],9)==1
assert min_age(reduced[4],9)==1

assert 27//gcd(27,sum(expect[1]))==9
assert 9//gcd(9,sum(reduced[2]))==3
assert 9//gcd(9,sum(reduced[3]))==1
assert 9//gcd(9,sum(reduced[4]))==1

# Euler: e(smooth quartic threefold)=-56, e(K3)=24, e(genus-3 curve)=-4.
assert (-56+18*4+6*(-4+2)+2*(24+1))//27==2
assert -56+18*4+6*(-4+2)+2*(24+1)==27*2
# Only order-three fixed divisor contributes to Riemann-Hurwitz.
assert (3**3*4)//27==4

# Explicit smoothness witness a=1,b=0: the affine plane quartic is
# f=x^3+y^3+1+x^2*y^2, and its gradient has no common zero on f=0.
x,y=sp.symbols('x y')
f=x**3+y**3+1+x**2*y**2
G=sp.groebner([f,sp.diff(f,x),sp.diff(f,y)],x,y,order='lex',domain=sp.QQ)
assert len(G.polys)==1 and G.polys[0].as_expr()==1
# At infinity z=0 the quartic is x^2*y^2; its two points [1:0:0],
# [0:1:0] have dF/dz=x^3+y^3 nonzero.
assert sp.expand((x**2*y**2).subs({x:1,y:0}))==0
assert sp.expand((x**2*y**2).subs({x:0,y:1}))==0

print('INVARIANT_MONOMIALS',len(MONOMIALS))
print('NONTRIVIAL_FIXED_PROFILES',dict(counts))
print('TANGENT_WEIGHTS',expect)
print('RESIDUAL_QUOTIENT_TYPES',reduced)
print('MINIMAL_AGE_NONCANONICAL',min_age(expect[1],27))
print('SMOOTH_QUARTIC_WITNESS',True)
print('QUOTIENT_EULER',2,'ANTICANONICAL_VOLUME',4,'CANONICAL_INDEX',9)
print('CERTIFICATE_OK')
