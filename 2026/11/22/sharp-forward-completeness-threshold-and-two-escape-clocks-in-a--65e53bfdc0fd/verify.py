"""Exact local asymptotic identities and finite diagnostics for a polynomial jerk ODE.

Run with python verify.py. Numerical integration is diagnostic only; the
infinite-domain and global conclusions are established in the written proof.
"""
from fractions import Fraction as Q
from math import log, sqrt
from scipy.integrate import solve_ivp
import sympy as sp

alpha, gamma, v = sp.symbols('alpha gamma v', positive=True)
sigma = sp.symbols('sigma', real=True)
# The sign equation w' = gamma*w^3 - sigma*alpha*w^2 - w + O(1).
recip = v**3 / (gamma - sigma*alpha*v - v**2)
expr = sp.series(recip, v, 0, 5).removeO().expand()
assert sp.simplify(expr.coeff(v, 3)-1/gamma)==0
assert sp.simplify(expr.coeff(v, 4)-sigma*alpha/gamma**2)==0

# The critical quadratic equation w' = alpha*w^2 - w + O(log w).
recip0 = v**2 / (alpha - v)
expr0 = sp.series(recip0, v, 0, 4).removeO().expand()
assert sp.simplify(expr0.coeff(v, 2)-1/alpha)==0
assert sp.simplify(expr0.coeff(v, 3)-1/alpha**2)==0

# Asymptotic inversion: u=sqrt(tau); w=A/u+B.
u=sp.symbols('u',positive=True)
A=1/sp.sqrt(2*gamma)
B=sigma*alpha/(3*gamma)
w=A/u+B
series_t=1/(2*gamma*w**2)+sigma*alpha/(3*gamma**2*w**3)
assert sp.simplify(sp.limit((series_t-u**2)/u**3,u,0))==0
wc=1/(alpha*u)+1/(2*alpha)
series_tc=1/(alpha*wc)+1/(2*alpha**2*wc**2)
assert sp.simplify(sp.limit((series_tc-u)/u**2,u,0))==0

# Independent, finite numerical check using the growing curvature w as time variable.
# dx/dw=y/G, dy/dw=sign*w/G, dt/dw=1/G.
def quadrature(gamma0, sign, w0=80.0, w1=1200.0):
    aa=2.3
    bb=0.02
    def rhs(w, st):
        t,x,y=st
        z=sign*w
        zp=-x-y-z-aa*z*z+x*y-bb+gamma0*z**3
        G=sign*zp
        assert G>0.0
        return [1/G, y/G, z/G]
    sol=solve_ivp(rhs,(w0,w1),[0.0,0.0,0.0],rtol=2e-11,atol=2e-13,max_step=4.0)
    assert sol.success
    t,x,y=sol.y[:,-1]
    assert all(map(lambda a: abs(a)<100, (t,x,y)))
    return t,x,y

for gg,sg in ((0.05,1),(0.05,-1),(0,-1)):
    tt,xx,yy=quadrature(gg,sg)
    assert tt>0 and abs(xx)<0.05 and abs(yy)<8
    print('diagnostic',gg,sg,'t80-to-1200',f'{tt:.9g}','x',f'{xx:.9g}','y',f'{yy:.9g}')

print('VERIFY_OK')
