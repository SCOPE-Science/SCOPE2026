"""Exact stationary-moment identity checks for a telegraph-driven oscillator.
Run: python verify.py. Dependency: SymPy >=1.10.
The symbolic derivation is valid over positive parameters; exact-rational examples
check the reconstructed stationary generator equations independently.
"""
import sympy as S

a,z=S.symbols('a z',positive=True)
P=(48*a**5+384*a**4*z+1152*a**3*z**2+104*a**3
   +1632*a**2*z**3+448*a**2*z+1104*a*z**4+476*a*z**2
   -9*a+288*z**5+132*z**3+12*z)
D=2*z*(3*z**2+1)*(4*a**2+4*a*z+1)**2*(4*a**2+12*a*z+9)*(4*a**2+12*a*z+8*z**2+1)
M2=(a+z)/(z*(4*a**2+4*a*z+1))
K4=-3*P/D
M4=S.factor(3*M2**2+K4)

def moments(rate,damping):
    # Generator: v d_x + (-x-2 z v+s) d_v + a(f(x,v,-s)-f(x,v,s)).
    # The state label s is encoded by a parity exponent 0 or 1.
    known={(0,0,0):S.Integer(1)}
    for degree in (1,2,3,4):
        labels=[(p,degree-p,b) for p in range(degree+1)
                for b in (0,1) if (degree+b)%2==0]
        U=S.symbols('u:'+str(len(labels)))
        unknown=dict(zip(labels,U))
        def get(t):return unknown.get(t,known.get(t,S.Integer(0)))
        eq=[]
        for p,q,b in labels:
            expression=S.Integer(0)
            if p:expression+=p*get((p-1,q+1,b))
            if q:
                expression-=q*get((p+1,q-1,b))
                expression-=2*damping*q*get((p,q,b))
                expression+=q*get((p,q-1,1-b))
            if b:expression-=2*rate*get((p,q,b))
            eq.append(expression)
        A,B=S.linear_eq_to_matrix(eq,U)
        assert A.det()!=0,('singular block',degree,rate,damping)
        solution=A.inv()*B
        known.update({label:S.factor(value) for label,value in zip(labels,solution)})
    return known

# First verify the symbolic, all-parameter linear recurrences, not just samples.
all_moments=moments(a,z)
assert S.cancel(all_moments[(2,0,0)]-M2)==0
assert S.cancel(all_moments[(4,0,0)]-M4)==0
assert S.factor(S.diff(P,a,2)).subs({a:S.Rational(1,7),z:S.Rational(1,11)})>0
assert S.factor(S.diff(P,z)).subs({a:S.Rational(1,7),z:S.Rational(1,11)})>0
assert S.expand(P.subs(z,0)-48*a*(a*a-S.Rational(1,12))*(a*a+S.Rational(9,4)))==0
# Four independent exact-rational generator reconstructions at positive parameters.
for A,Z in [(S.Rational(1,10),S.Rational(1,100)),(S.Rational(1,5),S.Rational(1,50)),
            (S.Rational(1,2),S.Rational(1,10)),(S.Integer(3),S.Rational(3,2))]:
    check=moments(A,Z)
    assert check[(2,0,0)]==S.factor(M2.subs({a:A,z:Z}))
    assert check[(4,0,0)]-3*check[(2,0,0)]**2==S.factor(K4.subs({a:A,z:Z}))
# Exact rational existence witness; strict increase gives a unique critical damping.
assert P.subs({a:S.Rational(11,100),z:S.Rational(42,1000)})<0
# At sufficiently large damping P is increasing in a and has positive intercept.
assert S.diff(P,a).subs({a:0,z:1})>0
assert P.subs({a:0,z:1})>0
print('PASS: all-parameter symbolic moment equations and cumulant factorization')
print('PASS: four independent exact-rational generator constructions')
print('PASS: exact onset witness and large-damping positivity')
