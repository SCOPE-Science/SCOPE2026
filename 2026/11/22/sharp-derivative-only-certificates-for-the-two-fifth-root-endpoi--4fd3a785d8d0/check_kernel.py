"""Exact symbolic verification of the two fifth-root endpoint quadratures.
Requires SymPy; all equalities are symbolic in Q(sqrt(5)).
"""
import sympy as s
from itertools import product
x,t=s.symbols('x t',real=True)
r=s.sqrt(5)


def coefficients(sign):
    return sign*r/10, (sign*3*r-5)/20, (sign*r-2)/10


def q(p,sign):
    c2,c3,c4=coefficients(sign)
    d=lambda k: s.diff(p,x,k)
    v=lambda k,z: d(k).subs(x,z)
    out=(v(0,0)+v(0,1))/2-c2*(v(1,1)-v(1,0))/2
    out+=c3*(v(2,1)+v(2,0))/6-c4*(v(3,1)-v(3,0))/24
    return s.simplify(out)

A=3*r/2-3
B=3*r/2+3
z=t*(1-t)
kplus=s.expand(z*z*(A-z)/720)
kminus=s.expand(-z*z*(B+z)/720)
for sign,expected in [(1,kplus),(-1,kminus)]:
    c2,c3,c4=coefficients(sign)
    u=1-t
    # Peano kernel E[(x-t)_+^5]/5! from the boundary jet at x=1.
    kernel=(u**6/6-u**5/2+5*c2*u**4/2-10*c3*u**3/3+5*c4*u**2/2)/120
    assert s.simplify(kernel-expected)==0
    for k in range(6):
        assert s.simplify(q(x**k,sign)-s.Rational(1,k+1))==0
    assert s.simplify(q(x**6,sign)-s.Rational(1,7)+s.integrate(expected,(t,0,1))*s.factorial(6))==0

# Pointwise kernel ratio bounds, certified by 0<=z<=1/4 and A>1/4, B>0.
qmin=s.Rational(1,2)-s.Rational(13,12)/r
qmax=s.Rational(1,2)-1/r
kgap=s.expand(kplus-kminus)
assert s.simplify(kgap-r*z*z/240)==0
assert s.simplify((kplus-qmin*kgap)-z*z*(s.Rational(1,4)-z)/720)==0
assert s.simplify((qmax*kgap-kplus)-z**3/720)==0
assert s.simplify(qmax-qmin-1/(12*r))==0
qopt=s.Rational(1,2)-s.Rational(25,24)/r
assert s.simplify(qopt-(qmin+qmax)/2)==0
assert s.simplify(qmax-qopt-1/(24*r))==0
assert s.simplify(qopt-qmin-1/(24*r))==0

# Nonnegative polynomials for g^(6), with exact rational Bernstein weights.
checks=0
for deg in range(0,5):
  for mask in range(1,2**(deg+1)):
    w=sum(((mask>>j)&1)*t**j*(1-t)**(deg-j) for j in range(deg+1))
    # Construct g^(6)=w, vanishing derivatives through order 5 at 0.
    p=w.subs(t,x)
    for _ in range(6):
      v=s.symbols('v')
      p=s.integrate(p.subs(x,v),(v,0,x))
    I=s.integrate(p,(x,0,1))
    qp=q(p,1); qm=q(p,-1)
    assert s.simplify(I-qp)>0
    assert s.simplify(qm-I)>0
    assert s.simplify(I-qp-qmin*(qm-qp))>=0
    assert s.simplify(qmax*(qm-qp)-(I-qp))>=0
    checks+=1
print('VERIFY_OK',checks,'nonnegative-sixth-derivative polynomial tests; exact Peano identities; monomial exactness 0..5; sharp constants.')
print('qmin',s.N(qmin,15),'qmax',s.N(qmax,15),'interval_width',s.N(qmax-qmin,15))
