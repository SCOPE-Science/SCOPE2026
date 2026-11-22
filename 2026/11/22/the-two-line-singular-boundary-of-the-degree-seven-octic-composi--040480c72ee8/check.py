"""Exact checks for the degree-eight quadratic/quartic composition compactification.
Reproducibility only: the geometric proof is in RESULT.md.
Requires Python 3 and sympy.
"""
import sympy as S
from math import comb

t=S.symbols('t')
c,u,v,a,b=S.symbols('c u v a b')
H=c*t**4+u*t**2+v*t
f=S.expand(a*H**2+b*H)
expected={8:a*c**2,6:2*a*c*u,5:2*a*c*v,4:a*u**2+b*c,
          3:2*a*u*v,2:a*v**2+b*u,1:b*v}
assert {i:S.expand(f).coeff(t,i) for i in (8,6,5,4,3,2,1)}==expected
C,D,E,F=S.symbols('C D E F')
# Boundary c=0: a(u*t^2+v*t)^2+b(u*t^2+v*t).
g=D**3-4*C*D*E+8*C**2*F
assert S.expand(g.subs({C:a*u**2,D:2*a*u*v,E:a*v**2+b*u,F:b*v}))==0
assert S.factor(g.subs({D:0}))==8*C**2*F
assert S.factor(S.diff(g,F))==8*C**2
assert S.factor(S.diff(g,E))==-4*C*D
assert S.factor(S.diff(g,D))==3*D**2-4*C*E
assert S.expand(S.diff(g,C))==-4*D*E+16*C*F
# The cubic is primitive of degree one in F, so irreducible.
assert S.gcd(C**2, D**3-4*C*D*E)==1
# Explicit generic birational inverse on C != 0:
z=D/(2*C)
assert S.simplify((z*(E-C*z**2)-F)*8*C**2+g)==0
# The nonsingular source charts have independent local parameter coordinates.
# a != 0, c=0, u=1: X3=1+bc, X1=2ac, X4=2av, X5=av^2+b.
cc,z,k=S.symbols('cc z k')
chart=[2*cc/(1+k*cc),2*z/(1+k*cc),(z*z+k)/(1+k*cc)]
J=S.Matrix(chart).jacobian([cc,z,k]);
assert S.factor(J.det().subs(cc,0))==4
# a=0,c=1,b=1: X0=l, X5=l*v^2+u, X6=v, X3=1+l*u^2.
l=S.symbols('l')
chart=[l/(1+l*u**2),(u+l*v*v)/(1+l*u**2),v/(1+l*u**2)]
assert S.simplify(S.Matrix(chart).jacobian([l,u,v]).det().subs(l,0))==1
# degree calculations and exact Stirling recursion for the global projective boundary.
def stir(n,k):
    if n==k or k==1: return 1
    if k<1 or k>n: return 0
    return stir(n-1,k-1)+k*stir(n-1,k)
for r in range(2,8):
    for s in range(3,9):
        degree=stir(r+s-2,r)
        plane_or_lower=stir(r+s-3,r-1)
        inner_deg_drop=stir(r+s-3,r)
        assert degree==plane_or_lower+r*inner_deg_drop
assert stir(4,2)==7 and stir(3,1)==1 and stir(3,2)==3
# Singular-line witnesses: two distinct source data giving the same target polynomial.
# q=3*t^4+5*t^2 on m: a=0, H=q and a=3,H=t^2,b=5.
assert S.expand((3*t**4+5*t**2)-(3*(t**2)**2+5*t**2))==0
# q=3*t^2+5*t on ell: a=0,H=q and a=3,H=t,b=5.
assert S.expand((3*t**2+5*t)-(3*t**2+5*t))==0
# The source differential loses rank at the one-preimage point q=t.
cc,uu,ll=S.symbols('cc uu ll')
# At H=cc*t^4+uu*t^2+t, b=1 and a=ll, normalize the t coefficient to 1.
cur=[ll*cc**2,2*ll*cc*uu,2*ll*cc,ll*uu**2+cc,2*ll*uu,ll+uu]
assert S.Matrix(cur).jacobian([cc,uu,ll]).subs({cc:0,uu:0,ll:0}).rank()==2
# Rational witness for cubic, on the second boundary component.
assert S.expand(g.subs({C:12,D:60,E:89,F:35}))==0
print('PASS: exact coefficient map, irreducible cubic boundary, inverse, chart ranks, Stirling recurrence, rational witness')
# Finite-field stress test of the projective-map fiber stratification (not an infinite proof).
from collections import defaultdict
p=5

def normalized(x):
    i=next(i for i,z in enumerate(x) if z%p)
    inv=pow(int(x[i])%p,-1,p)
    return tuple((int(z)*inv)%p for z in x)

def projective_points(n):
    from itertools import product
    out=set()
    for vals in product(range(p),repeat=n):
        if any(vals):out.add(normalized(vals))
    return sorted(out)
by_image=defaultdict(set)
for c0,u0,v0 in projective_points(3):
    for aa,bb in projective_points(2):
        coords=[aa*c0*c0,2*aa*c0*u0,2*aa*c0*v0,aa*u0*u0+bb*c0,
                2*aa*u0*v0,aa*v0*v0+bb*u0,bb*v0]
        by_image[normalized(coords)].add(((c0,u0,v0),(aa,bb)))
assert len(by_image)>100
count_double=0
for x,preimages in by_image.items():
    onell=x[0]==x[1]==x[2]==x[3]==x[4]==0
    onm=x[0]==x[1]==x[2]==x[4]==x[6]==0
    if onell or onm:
        if not (x[3]==x[4]==x[5]==0 and x[6]!=0):
            assert len(preimages)==2,(x,preimages)
            count_double+=1
        else:
            assert len(preimages)==1
    else:
        assert len(preimages)==1,(x,preimages)
print('PASS: F5 pointwise fiber classification, number of doubled rational image fibers:',count_double)
