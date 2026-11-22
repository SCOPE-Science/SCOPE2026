"""Exact symbolic checks of local Gaussian null-current classification.
Only finite-degree diagnostics; the accompanying analytic proof covers all C^2 L2 fields.
"""
from sympy import symbols, Rational, Poly, Matrix, zeros, expand
from itertools import product

x1,x2,y1,y2=symbols('x1 x2 y1 y2')
vars_=(x1,x2,y1,y2)

def monomials(degree,vs):
    return [vs[0]**a*vs[1]**b for a in range(degree+1) for b in range(degree+1-a)]

def dimension(s1,s2,degree):
    mx=monomials(degree,(x1,x2)); my=monomials(degree,(y1,y2))
    templates=[mx,mx,my,my]; components=[]; symbols_unknown=[]
    for v in templates:
        a=symbols('t'+str(len(symbols_unknown))+':'+str(len(symbols_unknown)+len(v)))
        symbols_unknown+=list(a)
        components.append(sum(c*m for c,m in zip(a,v)))
    u1,u2,w1,w2=components
    a1=1/(1-s1*s1);a2=1/(1-s2*s2)
    b1=s1/(1-s1*s1);b2=s2/(1-s2*s2)
    expression=(u1.diff(x1)+u2.diff(x2)+w1.diff(y1)+w2.diff(y2)
        -a1*(x1*u1+y1*w1)-a2*(x2*u2+y2*w2)
        +b1*(y1*u1+x1*w1)+b2*(y2*u2+x2*w2))
    coefficients=Poly(expression,*vars_).coeffs()
    matrix,vec=__import__('sympy').linear_eq_to_matrix(coefficients,symbols_unknown)
    assert vec==zeros(len(vec),1)
    return len(symbols_unknown)-matrix.rank()

assert dimension(Rational(1,2),Rational(1,3),1)==0
assert dimension(Rational(1,2),Rational(1,3),2)==0
assert dimension(Rational(1,2),Rational(0),1)==0
assert dimension(Rational(1,2),Rational(0),2)==0
assert dimension(Rational(1,3),Rational(1,3),1)==1
assert dimension(Rational(1,3),Rational(1,3),2)==1
assert dimension(Rational(0),Rational(0),1)==2

assert dimension(Rational(0),Rational(0),2)==6
assert dimension(Rational(0),Rational(0),3)==12
assert dimension(Rational(1,2),Rational(0),3)==0
assert dimension(Rational(1,2),Rational(1,3),3)==0
assert dimension(Rational(1,3),Rational(1,3),3)==1
print("PASS: 12 exact polynomial nullity checks, degrees 1-3")
# A nonresonant block rotation fails the stationary weighted-divergence test,
# but coordinated rotations at equal singular values pass exactly.
for s1,s2 in [(Rational(1,3),Rational(1,3)),(Rational(1,2),Rational(1,3))]:
    alpha1=1/(1-s1**2);alpha2=1/(1-s2**2)
    beta1=s1/(1-s1**2);beta2=s2/(1-s2**2)
    u1,u2,w1,w2=-x2,x1,-y2,y1
    expression=expand(-alpha1*(x1*u1+y1*w1)-alpha2*(x2*u2+y2*w2)+beta1*(y1*u1+x1*w1)+beta2*(y2*u2+x2*w2))
    assert (expression==0)==(s1==s2)
print('PASS: exact resonance/anisotropy rotation comparison')
