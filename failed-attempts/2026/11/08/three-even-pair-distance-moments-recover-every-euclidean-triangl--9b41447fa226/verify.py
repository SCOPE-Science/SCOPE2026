"""Recompute interior-triangle pair-distance moments by exact Dirichlet algebra.

Requires Python 3, numpy, sympy. The exact polynomial check does not depend on
Monte Carlo; simulation is only a separate diagnostic.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, factorial, sqrt
import numpy as np
import sympy as sp

x,y,z = sp.symbols('x y z')
d0,d1,d2 = sp.symbols('d0 d1 d2')

@lru_cache(None)
def difference_moment(k0,k1,k2):
    k=(k0,k1,k2); total=Fraction(0)
    for u in product(*(range(t+1) for t in k)):
        v=tuple(k[i]-u[i] for i in range(3))
        coeff=(-1)**sum(v)
        for i in range(3): coeff*=comb(k[i],u[i])
        def dr(m):
            num=2
            for t in m: num*=factorial(t)
            return Fraction(num, factorial(2+sum(m)))
        total += coeff*dr(u)*dr(v)
    return total

q=-x*d1*d2-y*d0*d2-z*d0*d1
e1=x+y+z; e2=x*y+x*z+y*z; e3=x*y*z
expected={
 1:e1/sp.Integer(18),
 2:(x*x+y*y+z*z)/sp.Integer(60),
 3:(23*e1**3-62*e1*e2+20*e3)/sp.Integer(4200)
}
for k in (1,2,3):
    p=sp.Poly(sp.expand(q**k),(d0,d1,d2))
    actual=sum(sp.Rational(c.numerator,c.denominator)*coef
       for mon,coef in p.terms()
       for c in [difference_moment(*mon)])
    assert sp.simplify(actual-expected[k])==0,(k,actual-expected[k])

# Validate exact inverse formulas with algebraic, nonsymmetric inputs.
m1,m2,m3=(sp.expand(expected[k]) for k in (1,2,3))
e1r=18*m1
e2r=(e1r**2-60*m2)/2
e3r=(4200*m3-23*e1r**3+62*e1r*e2r)/20
assert sp.expand(e1r-e1)==0
assert sp.expand(e2r-e2)==0
assert sp.expand(e3r-e3)==0
area_r=(81* m1**2/4-15*m2/2)
assert sp.expand(area_r-(4*e2-e1**2)/16)==0

# Two noncongruent, nondegenerate isosceles triangles with equal moments 1,2.
t=sp.sqrt(3)/3
xp=(2+t,2+t,2-2*t)
xm=(2-t,2-t,2+2*t)
for v in (xp,xm):
  assert min(float(w) for w in v)>0
  assert (float(sum(map(sp.sqrt,v)))-2*max(float(sp.sqrt(w)) for w in v))>0
  assert sp.simplify(sum(v)-6)==0
  assert sp.simplify(sum(v[i]*v[j] for i in range(3) for j in range(i+1,3))-11)==0
P=lambda v,k:sp.simplify(expected[k].subs(dict(zip((x,y,z),v))))
assert P(xp,1)==P(xm,1)==sp.Rational(1,3)
assert P(xp,2)==P(xm,2)==sp.Rational(7,30)
assert sp.simplify(P(xm,3)-P(xp,3)-sp.Rational(2,315)/sp.sqrt(3))==0

# Conditional sixth-moment envelope: at fixed first two moments, all
# squared-side triples are on a circle, and the product extrema are isosceles.
u,v=sp.symbols('u v',positive=True)
sym=(u+v,u+v,u-2*v)
sym2=(u-v,u-v,u+2*v)
for values in (sym,sym2):
    s1=sum(values)
    s2=sum(values[i]*values[j] for i in range(3) for j in range(i+1,3))
    productv=sp.prod(values)
    rad=s1**2-3*s2
    assert sp.simplify(rad-9*v**2)==0
    lo=(s1*(9*s2-2*s1**2)-2*rad**sp.Rational(3,2))/27
    hi=(s1*(9*s2-2*s1**2)+2*rad**sp.Rational(3,2))/27
    # Because v>0 and |v|=v in the symbolic assumptions.
    assert sp.simplify(productv-lo)==0 or sp.simplify(productv-hi)==0

# Independent coordinate sampling (not barycentric polynomial integration).
rng=np.random.default_rng(20261104)
configs=[(1.,1.,1.),(1.,1.,1.95),(2.,3.,4.),(2.,2.4,3.),(1.,2.,2.5),
         (1.,1.8,2.7),(2.,2.,2.8),(1.5,1.7,2.0)]
n=180_000
for a,b,c in configs:
    # vertices (0,0), (c,0), (u,v); opposite sides a,b,c.
    u=(b*b+c*c-a*a)/(2*c)
    v=sqrt(max(0,b*b-u*u))
    assert v>0
    # Independent barycentric points generated from independent exponential variables.
    gam1=rng.exponential(size=(n,3)); gam1/=gam1.sum(axis=1)[:,None]
    gam2=rng.exponential(size=(n,3)); gam2/=gam2.sum(axis=1)[:,None]
    delta=gam1-gam2
    d_sq=(c*delta[:,1]+u*delta[:,2])**2+(v*delta[:,2])**2
    e1v=a*a+b*b+c*c
    e2v=a*a*b*b+a*a*c*c+b*b*c*c
    e3v=a*a*b*b*c*c
    w=sqrt(max(0,e1v*e1v-3*e2v))
    emin=(e1v*(9*e2v-2*e1v**2)-2*w**3)/27
    emax=(e1v*(9*e2v-2*e1v**2)+2*w**3)/27
    assert emin-1e-9<=e3v<=emax+1e-9
    targets=[e1v/18,(e1v*e1v-2*e2v)/60,
        (23*e1v**3-62*e1v*e2v+20*e3v)/4200]
    for k,target in enumerate(targets,1):
        data=d_sq**k
        err=abs(float(data.mean())-target)
        se=float(data.std(ddof=1)/sqrt(n))
        assert err<7*se+0.00001,(a,b,c,k,err,se)

print('PAIR_TRIANGLE_INVERSE_OK exact_polynomials=3 inverse=3 conditional_envelope=2 isosceles_pair=2 monte_carlo_shapes=8 samples_each=180000')
