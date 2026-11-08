"""Exact-rational checker for symmetric cap cubature on the two-sphere.

Python 3 standard library only. Uses Q[t]/(t*t-3/7).
"""
from fractions import Fraction as Q
from math import comb
from itertools import product

t2=Q(3,7)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]+t2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scalar(c):return (Q(c),Q(0))
def div(a,b):
    d=b[0]*b[0]-t2*b[1]*b[1]
    assert d
    return mul(a,(b[0]/d,-b[1]/d))
ONE=scalar(1);ZERO=scalar(0);T=(Q(0),Q(1))
def power(x,n):
    v=ONE
    for _ in range(n):v=mul(v,x)
    return v

def odd_double_fact(k):
    if k<=0:return 1
    out=1
    for j in range(k,0,-2):out*=j
    return out

def angular(b,c):
    assert b%2==0 and c%2==0
    return Q(odd_double_fact(b-1)*odd_double_fact(c-1),odd_double_fact(b+c))

def polar_integral(a,k):
    # integral_t^1 s^a (1-s^2)^k ds
    out=ZERO
    for j in range(k+1):
        p=a+2*j+1
        out=add(out,mul(scalar(Q((-1)**j*comb(k,j),p)),sub(ONE,power(T,p))))
    return out

def cap_weight_moment(exponents):
    # sum of six ± coordinate-axis caps, full-sphere normalized
    if any(v%2 for v in exponents):return ZERO
    out=ZERO
    for i in range(3):
        a=exponents[i];b,c=[exponents[j] for j in range(3) if j!=i]
        out=add(out,mul(scalar(angular(b,c)),polar_integral(a,(b+c)//2)))
    return out

def uniform_moment(exponents):
    if any(v%2 for v in exponents):return Q(0)
    return Q(odd_double_fact(exponents[0]-1)*odd_double_fact(exponents[1]-1)*odd_double_fact(exponents[2]-1),odd_double_fact(sum(exponents)+1))
MASS=mul(scalar(3),sub(ONE,T))
assert cap_weight_moment((0,0,0))==MASS
print('SIX_CAP_NORMALIZATION_EXACT')

for degree in range(6):
    for a in range(degree+1):
        for b in range(degree-a+1):
            c=degree-a-b
            calc=div(cap_weight_moment((a,b,c)),MASS)
            assert calc==scalar(uniform_moment((a,b,c))),(a,b,c,calc)
print('ALL_56_MONOMIAL_MOMENTS_THROUGH_DEGREE_FIVE_EXACT')

mom6=div(cap_weight_moment((0,0,6)),MASS)
assert mom6 != scalar(Q(1,7))
# P6=(231 z^6-315 z^4+105 z^2-5)/16.
p6=scalar(0)
for coef,exp in [(231,6),(-315,4),(105,2),(-5,0)]:
    p6=add(p6,mul(scalar(Q(coef,16)),div(cap_weight_moment((0,0,exp)),MASS)))
assert p6==mul(scalar(Q(-11,784)),mul(T,add(ONE,T)))
print('DEGREE_SIX_EXACT_OBSTRUCTION_NONZERO')

# Compare the two five-dimensional eigensectors with closed formulas at t^2=3/7.
E=mul(scalar(Q(3,16)),mul(sub(ONE,T),
    add(add(add(add(mul(scalar(21),power(T,4)),mul(scalar(21),power(T,3))),mul(scalar(-9),power(T,2))),mul(scalar(-9),T)),scalar(16))))
F=mul(scalar(Q(3,8)),mul(power(sub(ONE,T),2),
    add(add(add(mul(scalar(7),power(T,3)),mul(scalar(14),power(T,2))),mul(scalar(11),T)),scalar(8))))
assert E==F==MASS
print('QUADRUPOLE_RESTRICTION_IS_EXACT_TIGHT_FRAME')

# For a test away from the tight radius, the two sector functions differ.
def sector_diff_polynomial(u):
    return Q(-15,16)*u*(u-1)*(u+1)*(7*u*u-3)
assert sector_diff_polynomial(Q(3,4)) != 0
assert sector_diff_polynomial(Q(1,2)) != 0
print('UNIQUE_INTERIOR_NONTRIVIAL_TIGHT_RADIUS_CERTIFIED_BY_FACTOR')
print('ALL_OCTAHEDRAL_CAP_CUBATURE_CHECKS_OK')

# Independent all-radius rational-polynomial check of the two sector eigenvalues.
# A polynomial is a dict degree -> exact rational coefficient.
def poly(a):return {k:Q(v) for k,v in a.items() if v}
def padd(a,b):
    d=dict(a)
    for k,v in b.items():d[k]=d.get(k,Q(0))+v
    return poly(d)
def pscale(a,s):return poly({k:v*s for k,v in a.items()})
def pmul(a,b):
    d={}
    for i,x in a.items():
        for j,y in b.items():d[i+j]=d.get(i+j,Q(0))+x*y
    return poly(d)
def ppow(a,n):
    p={0:Q(1)}
    for _ in range(n):p=pmul(p,a)
    return p
U={1:Q(1)}; O={0:Q(1)}
def ppolar(a,k):
    # integral_u^1 s^a(1-s^2)^k ds in Q[u]
    out={}
    for j in range(k+1):
        d=a+2*j+1
        c=Q((-1)**j*comb(k,j),d)
        out=padd(out,{0:c,d:-c})
    return out
def pweighted(exps):
    if any(v%2 for v in exps):return {}
    out={}
    for i in range(3):
        a=exps[i]
        b,c=[exps[j] for j in range(3) if j!=i]
        out=padd(out,pscale(ppolar(a,(b+c)//2),angular(b,c)))
    return out
M400=pweighted((4,0,0)); M220=pweighted((2,2,0))
e_poly=pscale(padd(pscale(M400,2),pscale(M220,-2)),Q(15,4))
t_poly=pscale(M220,15)
e_expected=pscale(pmul(padd(O,pscale(U,-1)),{4:21,3:21,2:-9,1:-9,0:16}),Q(3,16))
t_expected=pscale(pmul(ppow(padd(O,pscale(U,-1)),2),{3:7,2:14,1:11,0:8}),Q(3,8))
assert e_poly==e_expected and t_poly==t_expected
assert padd(pscale(e_poly,2),pscale(t_poly,3))==pscale(padd(O,pscale(U,-1)),15)
d_expected=pscale(pmul(pmul(U,padd(O,pscale(ppow(U,2),-1))),padd(pscale(ppow(U,2),7),{0:Q(-3)})),Q(15,16))
assert padd(e_poly,pscale(t_poly,-1))==d_expected
for denom,coefficients,expected in [
    (8,[(35,4),(-30,2),(3,0)],pscale(pmul(pmul(U,padd(O,U)),padd(pscale(ppow(U,2),7),{0:Q(-3)})),Q(7,96))),
    (16,[(231,6),(-315,4),(105,2),(-5,0)],pscale(pmul(pmul(U,padd(O,U)),padd(padd(pscale(ppow(U,4),33),pscale(ppow(U,2),-30)),{0:Q(5)})),Q(1,128)))
]:
    raw={}
    for c,k in coefficients:raw=padd(raw,pscale(pweighted((0,0,k)),Q(c,denom)))
    assert raw==pmul(pscale(padd(O,pscale(U,-1)),3),expected)
print('ALL_RADIUS_EXACT_GRAM_EIGENVALUE_AND_LEGENDRE_POLYNOMIAL_IDENTITIES_OK')
