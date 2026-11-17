"""Exact two-node network-SIRS coefficient check (SymPy required).

Scientific equations: y' = (1-y-z)*(W*y) - Gamma*y,
                      z' = Gamma*y - Delta*z.
Elementwise multiplication is used in the infection term.
"""
from sympy import (Matrix, symbols, Rational, diag, factor, simplify,
                   diff, cancel, expand, limit, oo)

d = symbols('d', positive=True)
W = Matrix([[Rational(3,4), Rational(1,4)],
            [Rational(1,2), Rational(3,2)]])
G = diag(1, 2)
A = W - G
v = Matrix([1, 1])
w = Matrix([[Rational(2,3), Rational(1,3)]])
h = Matrix([1/d, 2/d])
b = (v+h).multiply_elementwise(W*v)
K = factor((w*b)[0])
p = Matrix([4*(d+3)/(9*d), -8*(d+3)/(9*d)])
q = diag(1/d, 1/d) * (G*p + K*h)
c = (v+h).multiply_elementwise(W*p) + (p+q).multiply_elementwise(W*v)
L = factor((w*c)[0]); B=factor(L/K)

def eq0(z):
    if isinstance(z, Matrix):
        assert all(simplify(a)==0 for a in z)
    else:
        assert simplify(z)==0

eq0(A*v); eq0(w*A); eq0(w*v-Matrix([[1]]))
eq0(A*p - (b-K*v)); eq0(w*p)
eq0(diag(d,d)*q-G*p-K*h)
eq0(K-2*(2*d+3)/(3*d))
eq0(L+2*(8*d**3+45*d**2+27*d-54)/(27*d**3))
eq0(B+(8*d**3+45*d**2+27*d-54)/(9*d**2*(2*d+3)))
eq0(B.subs(d,Rational(1,2))-Rational(113,36))
eq0(B.subs(d,1)+Rational(26,45))
assert diff(8*d**3+45*d**2+27*d-54,d).is_positive
print('PASS: Perron normalization; reduced coefficients; cubic sign change; rational comparison points')

# Independent expansion check via the original polynomial vector field:
u=symbols('u',positive=True)
y=v*u+p*u**2
z=h*u+q*u**2
N=(y+z).multiply_elementwise(W*y)
# Coefficients of w^T N at orders two and three:
eq0(expand((w*N)[0]).coeff(u,2)-K)
eq0(expand((w*N)[0]).coeff(u,3)-L)
# Matched invariance equations to cubic order:
# y' = v u'+(2p u)u', with u'=-Ku^2-Lu^3
lhs_y=(v+2*u*p)*(-K*u**2-L*u**3)
rhs_y=A*y-N
eq0(Matrix([expand(a).coeff(u,2) for a in lhs_y-rhs_y]))
lhs_z=(h+2*u*q)*(-K*u**2-L*u**3)
rhs_z=G*y-diag(d,d)*z
eq0(Matrix([expand(a).coeff(u,2) for a in lhs_z-rhs_z]))
print('PASS: cubic infection expansion and second-order center-manifold invariance')

# Supplemental trajectory check (not a proof of the infinite-time limits).
try:
    import numpy as np
    from scipy.integrate import solve_ivp
    wn=np.array([[.75,.25],[.5,1.5]])
    gamma=np.array([1.,2.]);w_num=np.array([2/3,1/3])
    times=np.array([1.e3,1.e4,1.e5])
    for delta, ks, expected in [(.5,16/3,113/36),(1.,10/3,-26/45)]:
        def flow(t, yz):
            yi=yz[:2];zi=yz[2:]
            return np.r_[(1-yi-zi)*(wn@yi)-gamma*yi,gamma*yi-delta*zi]
        sol=solve_ivp(flow,(0.,times[-1]),[.12,.03,.02,.01],
                      method='LSODA',t_eval=times,rtol=1.e-11,atol=1.e-15)
        assert sol.success
        vals=np.array([w_num@state[:2] for state in sol.y.T])
        residual=1./vals-ks*times
        estimates=np.diff(residual)/np.log(times[1:]/times[:-1])
        assert np.all(np.abs(estimates-expected)<.02),(delta,estimates,expected)
        print('PASS: numerical tail, waning rate',delta,'coefficient',expected,
              'two scales',estimates)
except ImportError:
    print('Optional SciPy numerical trajectory check skipped; exact checks passed')
