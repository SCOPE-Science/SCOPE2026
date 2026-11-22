"""Numerical checks for two-rate MFPT reconstruction on a reflected interval."""
import numpy as np
from scipy.integrate import solve_ivp

L = 1.0
x_reset = 0.43
rates = (0.4, 2.0)

def D(x):
    return 1.0 + 0.25*x

def b(x):
    return -0.3 + 0.5*x

def make_phi(r):
    def ode(x, y):
        u, du = y
        return [du, (r*u-b(x)*du)/D(x)]
    sol = solve_ivp(ode, (L, 0), (1., 0.), rtol=5e-12, atol=5e-13, dense_output=True)
    assert sol.success
    norm = sol.sol(0.)[0]
    assert norm>1
    return lambda x: sol.sol(x)/norm

phis = [make_phi(r) for r in rates]
c = [1/(r*p(x_reset)[0]) for r,p in zip(rates, phis)]
W_min=float('inf')
maxDerr=0.
maxberr=0.
for x in np.linspace(.02,.94,185):
    vals=[]
    for r,p,cc in zip(rates,phis,c):
        phi, phip = p(x)
        m=cc*(1-phi)
        mp=-cc*phip
        mpp=-cc*(r*phi-b(x)*phip)/D(x)
        q=r*(m-cc*(1-p(x_reset)[0]))-1
        vals.append((m,mp,mpp,q))
    _,p1,pp1,q1=vals[0]
    _,p2,pp2,q2=vals[1]
    W=pp1*p2-pp2*p1
    assert W>0, (x,W)
    D_recon=(q1*p2-q2*p1)/W
    b_recon=(pp1*q2-pp2*q1)/W
    W_min=min(W_min,W)
    maxDerr=max(maxDerr, abs(D_recon-D(x)))
    maxberr=max(maxberr, abs(b_recon-b(x)))
assert maxDerr<3e-9, maxDerr
assert maxberr<3e-9, maxberr

# Exact constant-coefficient benchmark.
for r1,r2 in [(0.2,0.8),(.4,2), (2,7)]:
    x=.6
    def exact(r):
        k=np.sqrt(r)
        phi=np.cosh(k*(1-x))/np.cosh(k)
        phip=-k*np.sinh(k*(1-x))/np.cosh(k)
        phipp=k*k*phi
        c=1/(r*np.cosh(k*(1-x_reset))/np.cosh(k))
        m=c*(1-phi)
        mstar=c*(1-np.cosh(k*(1-x_reset))/np.cosh(k))
        return -c*phip,-c*phipp,r*(m-mstar)-1
    p1,pp1,q1=exact(r1)
    p2,pp2,q2=exact(r2)
    w=pp1*p2-pp2*p1
    assert w>0
    assert abs((q1*p2-q2*p1)/w-1)<1e-11
    assert abs((pp1*q2-pp2*q1)/w)<1e-11
print('PASS: 185 variable-coefficient points + 3 constant-coefficient cases')
print('minimum determinant on numerical grid:', W_min)
print('max reconstructed D error:', maxDerr)
print('max reconstructed b error:', maxberr)
