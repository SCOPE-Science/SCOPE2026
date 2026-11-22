"""Independent symbolic checks for Poisson-restarted dichotomous acceleration.

Requires Python 3 and SymPy. Prints key exact identities; no random sampling
is used to establish analytic claims.
"""
from functools import lru_cache
from math import factorial
import sympy as S

r, gamma, amplitude = S.symbols('r gamma amplitude', positive=True)

@lru_cache(maxsize=None)
def stationary_moment(i, j, parity):
    """E[X**i V**j sigma**parity] via the stationary Markov generator."""
    if i == j == 0:
        return S.Integer(1) if parity == 0 else S.Integer(0)
    numerator = S.Integer(0)
    if i:
        numerator += i * stationary_moment(i-1, j+1, parity)
    if j:
        numerator += amplitude*j*stationary_moment(i, j-1, 1-parity)
    return S.cancel(numerator/(r+2*gamma*parity))

m2 = S.factor(stationary_moment(2, 0, 0))
m4 = S.factor(stationary_moment(4, 0, 0))
expected_m2 = 2*amplitude**2*(4*gamma+3*r)/(r**3*(2*gamma+r)**2)
expected_m4 = (24*amplitude**4*(320*gamma**3+624*gamma**2*r
                 +426*gamma*r**2+105*r**3)/(r**6*(2*gamma+r)**5))
assert S.simplify(m2-expected_m2)==0
assert S.simplify(m4-expected_m4)==0

# Independently integrate the ordered four-time telegraph correlation.
# The four positive gaps have exponential rates [r+2gamma,r,r+2gamma,r].
g1,g2,g3,g4=S.symbols('g1 g2 g3 g4')
p=S.Poly((g1+g2+g3+g4)*(g2+g3+g4)*(g3+g4)*g4,g1,g2,g3,g4)
independent=S.Integer(0)
for powers, coefficient in p.terms():
    term=coefficient
    for degree,rate in zip(powers,[r+2*gamma,r,r+2*gamma,r]):
        term *= S.factorial(degree)/rate**(degree+1)
    independent+=term
assert S.simplify(24*amplitude**4*independent-expected_m4)==0

# Independently integrate the two-time correlation of the telegraph force.
independent_m2=2*amplitude**2*(2/(r**3*(r+2*gamma))
                                +1/(r**2*(r+2*gamma)**2))
assert S.simplify(independent_m2-expected_m2)==0

z=S.symbols('z', positive=True)
K=3*(608+1184*z+810*z**2+201*z**3)/((z+2)*(3*z+4)**2)
excess=S.factor(m4/m2**2-3)
assert S.simplify(excess-K.subs(z,r/gamma))==0
DK=S.factor(S.diff(K,z))
assert S.simplify(DK-192*(6*z**3+15*z**2+6*z-4)/((z+2)**2*(3*z+4)**3))==0
assert S.simplify(K-57-6*z*(15*z**2+6*z-16)/((z+2)*(3*z+4)**2))==0
assert S.simplify(K-67+32*(3*z+2)*(4*z+5)/((z+2)*(3*z+4)**2))==0
zc=(S.sqrt(249)-3)/15
assert S.simplify((15*z**2+6*z-16).subs(z,zc))==0
C=6*z**3+15*z**2+6*z-4
assert C.subs(z,0)<0
assert S.simplify(S.diff(C,z))==18*z**2+30*z+6
z_star=S.nsolve(C,0.3,prec=60)
assert 0<z_star<zc
assert 56 < K.subs(z,z_star) < 57
assert S.limit(K,z,0,dir='+')==57
assert S.limit(K,z,S.oo)==67
assert S.simplify(K.subs(z,zc)-57)==0
# Under Gaussian white acceleration with velocity diffusivity D>0,
# E[X^2]=4D/r^3 and E[X^4]=960D^2/r^6, hence excess 57.
D=S.symbols('D',positive=True)
assert S.simplify((960*D**2/r**6)/(4*D/r**3)**2-3)==57
print('Symbolic moment recursion, independent pair/four-point integrals,')
print('and global kurtosis phase diagram: all checks passed.')
print('unique minimizer r/gamma =', S.N(z_star,18))
print('minimum excess kurtosis =', S.N(K.subs(z,z_star),18))
print('Gaussian-acceleration crossing r/gamma =',S.N(zc,18))
