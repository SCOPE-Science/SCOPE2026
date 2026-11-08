"""Reproduce algebraic identities and a numerical diagnostic for a predator–prey extinction-fold theorem.

Requires Python 3 and SymPy. Numerical tests are corroboration, not proofs of asymptotic limits.
"""
import math
import sympy as sp

alpha, d, q, z = sp.symbols('alpha d q z', positive=True)
zs = (1-q)/alpha
a = alpha*(d+1)*sp.exp(1-q)
b = q*(d+1)*sp.exp(1-q)
h = (b+a*z)*sp.exp(-alpha*z)-(d+1)
lam = 1-a*z*sp.exp(-alpha*z)
mu = d-(d+1)*q
kappa = alpha*(d+1)*(1-q)/2
nu = 2*q/(1-q)
checks = {
    'fold_value': h.subs(z,zs),
    'fold_first_derivative': sp.diff(h,z).subs(z,zs),
    'fold_second_derivative': sp.diff(h,z,2).subs(z,zs)+alpha**2*(d+1),
    'radial_eigenvalue': lam.subs(z,zs)+mu,
    'power_exponent': sp.diff(lam,z).subs(z,zs)/kappa+nu,
    'linear_stable_eigenvector': (-mu)*(-zs/mu)-zs,
}
for name, expression in checks.items():
    assert sp.simplify(expression)==0, (name, expression)

A = 2*math.exp(.9)
B = .2*math.exp(.9)
Z = .9
MU = .8
K = .9
NU = 2/9
assert B < 1
assert abs((B+A*Z)*math.exp(-Z)-2) < 1e-13

# Integrate logarithmic prey and ratio, avoiding artificial numerical underflow.
def rhs(logu, ratio):
    prey = math.exp(logu) if logu > -700 else 0.
    return (1-A*ratio*math.exp(-ratio)-prey,
            ratio*((B+A*ratio)*math.exp(-ratio)-2+prey))

def integrate(target, step=.1):
    steps=round(target/step)
    logu=math.log(.0001)
    ratio=Z+.05
    for _ in range(steps):
        x1,y1=rhs(logu,ratio)
        x2,y2=rhs(logu+step*x1/2, ratio+step*y1/2)
        x3,y3=rhs(logu+step*x2/2, ratio+step*y2/2)
        x4,y4=rhs(logu+step*x3, ratio+step*y3)
        logu +=step*(x1+2*x2+2*x3+x4)/6
        ratio+=step*(y1+2*y2+2*y3+y4)/6
    return (target*(ratio-Z), math.exp(logu+MU*target+NU*math.log(target)))

r500,c500=integrate(500.)
r1000,c1000=integrate(1000.)
assert abs(r1000-1/K) < .04, (r1000,1/K)
assert abs(c1000/c500-1)<.02, (c500,c1000)
assert 0<c500<c1000<.01
print('FOLD_RATIO_500',repr(r500))
print('FOLD_RATIO_1000',repr(r1000))
print('NORMALIZED_PREY_500',repr(c500))
print('NORMALIZED_PREY_1000',repr(c1000))
print('VERIFY_OK')
