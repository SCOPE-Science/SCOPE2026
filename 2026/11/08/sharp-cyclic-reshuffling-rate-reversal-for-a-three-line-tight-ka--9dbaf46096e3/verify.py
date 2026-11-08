"""Exact symbolic checks for three-line relaxed Kaczmarz rates.

Requires Python 3 and SymPy. This is an independent reproducible algebraic
check of identities proved in the accompanying mathematical note; finite
checks and symbolic computations do not replace the stated analytic proofs.
"""
import itertools
from fractions import Fraction
import sympy as sp

w = sp.symbols('w', real=True)
s3 = sp.sqrt(3)
normals = [sp.Matrix([1, 0]), sp.Matrix([sp.Rational(1, 2), s3/2]),
           sp.Matrix([-sp.Rational(1, 2), s3/2])]
I = sp.eye(2)
P = [I - w * n * n.T for n in normals]
perms = list(itertools.permutations(range(3)))

def sweep(perm):
    S = I
    for j in perm:
        S = P[j] * S
    return sp.simplify(S)

def zero_matrix(X):
    return all(sp.simplify(x) == 0 for x in X)

def assert_positive(expr):
    assert sp.ask(sp.Q.positive(expr)) is True, expr

S = sweep((0, 1, 2))
T = sp.factor(sp.trace(S))
d = sp.factor(S.det())
Delta = sp.factor(T**2 - 4*d)
r = (1-w)**3 + w**6/32
assert sp.factor(T - (w-2)*(w*w+8*w-8)/8) == 0
assert sp.factor(d - (1-w)**3) == 0
assert sp.factor(Delta - w**4*(w*w+12*w-12)/64) == 0
assert sp.factor(sp.trace(S.T*S)/2 - r) == 0

# Six exact finite products, and the full isotropic reshuffling covariance.
M = sp.zeros(2)
for pi in perms:
    X = sweep(pi)
    M += X.T * X / 6
    assert sp.factor(sp.trace(X.T*X)/2 - r) == 0
    assert sp.factor(sp.trace(X)-T) == 0
    assert sp.factor(X.det()-d) == 0
assert zero_matrix(M-r*I)

# IID individual rows over one three-update epoch and the strict improvement.
u = (1-w*(2-w)/2)**3
assert sp.factor(u-r - 3*w**2*(2-w)**4/32) == 0

# Uniquely optimal reshuffling parameter, rational-root isolating bracket.
F = w**5 - 16*(1-w)**2
lo = sp.Rational(83886, 100000)
hi = sp.Rational(83888, 100000)
assert F.subs(w,lo) < 0 < F.subs(w,hi)
assert (1-hi)**3+lo**6/32 > sp.Rational(3,200)
# On (1,2), w**5/(w-1)**2 has its unique minimum at 5/3.
assert sp.Rational(3125,108) > 16

# The spectral optimum is the unique crossing from complex to real spectrum.
wstar = 4*s3-6
dstar = sp.simplify((1-wstar)**3)
qstar = sp.sqrt(dstar)
assert sp.simplify(wstar**2+12*wstar-12) == 0
assert sp.simplify(dstar-(1351-780*s3)) == 0
assert sp.simplify(dstar<sp.Rational(1,2500)) is sp.true
assert sp.simplify(wstar>sp.Rational(92820,100000)) is sp.true
assert sp.simplify(wstar<sp.Rational(92821,100000)) is sp.true
# Derivative of trace T is negative on [wstar,6/5].
assert sp.factor(sp.diff(T,w)-(3*w*w+12*w-24)/8) == 0
assert sp.diff(T,w).subs(w,sp.Rational(6,5)) < 0
assert sp.simplify(T.subs(w,wstar) < 0) is sp.true
# On [6/5,2), the opposite-sign eigenvalues satisfy rho^2>=|det|>=1/125> dstar.
assert sp.Rational(1,125) > dstar

Sc=S.subs(w,wstar).applyfunc(sp.simplify)
lam=sp.simplify(sp.trace(Sc)/2)
N=(Sc-lam*I).applyfunc(sp.simplify)
assert zero_matrix(N*N)
assert sp.simplify(lam**2-dstar) == 0
assert sp.simplify(sp.trace(N.T*N)-wstar**6/16) == 0
assert zero_matrix(Sc**2-(lam**2*I+2*lam*N))
# A norm bound: ||S_*^2|| <= dstar+2*sqrt(dstar)*||N|| <1/2500+1/100=0.0104.
assert sp.Rational(1,2500)+sp.Rational(1,100) < sp.Rational(3,200)
# The exact Jordan power obeys ||S_*^k||^2=dstar^k * [sqrt(1+(k*c)^2)+k*c]^2,
# c=||N||/(2|lambda|); the ratio of successive factors is <=dstar*((k+1)/k)^2.
assert sp.Rational(9,4)*sp.Rational(1,2500) < sp.Rational(3,200)

# One-epoch strict reversal: max singular squared exceeds half Frobenius squared,
# and the latter exceeds the optimally reshuffled factor.
assert not zero_matrix(Sc.T*Sc-sp.trace(Sc.T*Sc)*I/2)
assert sp.simplify(r.subs(w,wstar) > sp.Rational(3,200)) is sp.true

# Additional exact consistency for unrelaxed sweeps.
assert sp.factor(r.subs(w,1)-sp.Rational(1,32)) == 0
assert sp.factor(u.subs(w,1)-sp.Rational(1,8)) == 0
assert sp.factor(d.subs(w,1)) == 0
assert sp.factor(T.subs(w,1)+sp.Rational(1,8)) == 0

# Exact small integer-angle tests of multi-epoch covariance, as separate sanity checks.
for wt in (sp.Rational(1,2), sp.Rational(4,5), sp.Rational(1), sp.Rational(6,5)):
    matrices = [sweep(pi).subs(w,wt) for pi in perms]
    one = sp.zeros(2)
    for A in matrices:
        one += A.T*A/6
    assert zero_matrix(one-r.subs(w,wt)*I)
    two = sp.zeros(2)
    for A in matrices:
        for B in matrices:
            two += (A*B).T*(A*B)/36
    assert zero_matrix(two-r.subs(w,wt)**2*I)

print('PASS: exact polynomial, symmetry, covariance, iid improvement, root brackets, optimum, Jordan and finite-horizon bounds')
print('cyclic optimum w =', sp.simplify(wstar), 'asymptotic squared factor =', dstar)
print('reshuffling optimum in interval =', lo, hi)
print('unrelaxed RR factor =', r.subs(w,1), 'unrelaxed cyclic asymptotic squared factor =', sp.Rational(1,64))
