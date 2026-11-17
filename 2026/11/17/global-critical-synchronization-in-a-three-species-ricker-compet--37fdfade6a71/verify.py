"""Independent arithmetic and symbolic diagnostics for the stated Ricker recurrence.

Requires Python 3, sympy, mpmath. Finite tests are not proofs of global convergence.
"""
import math
import sympy as sp
import mpmath as mp

z=sp.Symbol('z')
f=z+2-2*sp.exp(z)
g_series=sp.series(f.subs(z,sp.series(f,z,0,6).removeO()),z,0,5).removeO().expand()
assert sp.expand(g_series).coeff(z,3)==sp.Rational(-4,3)
assert sp.expand(g_series).coeff(z,2)==0

for c in [sp.Rational(3,10),sp.Rational(1,2),sp.Rational(9,10)]:
    eq=2/(1+2*c)
    mat=sp.Matrix([[1-eq,-c*eq,-c*eq],[-c*eq,1-eq,-c*eq],[-c*eq,-c*eq,1-eq]])
    lam=(4*c-1)/(1+2*c)
    assert sorted([float(sp.re(v)) for v in mat.eigenvals().keys()]) == sorted([-1.,float(lam)]) or list(mat.eigenvals().values())==[1,2]
    assert sp.simplify((mat+sp.eye(3))*(mat-lam*sp.eye(3)))==sp.zeros(3)

mp.mp.dps=140
for cfloat in [0.3,0.5,0.8]:
    c=mp.mpf(str(cfloat)); a=1+2*c
    X=[mp.mpf('0.2'),mp.mpf('1.3'),mp.mpf('0.8')]
    for n in range(220):
        total=sum(X)
        X=[x*mp.exp(2-c*total-(1-c)*x) for x in X]
        assert all(x>0 for x in X)
    target=2/a
    assert max(abs(x-target) for x in X)<mp.mpf('0.2')
    lam=(4*c-1)/a
    # When pairwise differences are numerically resolvable, the exact multiplier
    # of the logarithmic ratios tends toward the transverse eigenvalue.
    ratio=mp.log(X[0]/X[1]); total=sum(X)
    newX=[x*mp.exp(2-c*total-(1-c)*x) for x in X]
    newratio=mp.log(newX[0]/newX[1])
    if abs(ratio)>mp.mpf('1e-125'):
        assert abs(newratio/ratio-lam)<mp.mpf('0.1')

# On the diagonal, the original-generation inverse-square amplitude tends to 3/4.
mp.mp.dps=60
zz=mp.mpf('0.05')
for n in range(1,25001):
    zz=zz+2-2*mp.exp(zz)
val=n*zz**2
assert abs(val-mp.mpf('0.75'))<mp.mpf('0.02'),val
print('PASS: cubic composition, Jacobian factorization, 3D positive samples, diagonal critical rate')
