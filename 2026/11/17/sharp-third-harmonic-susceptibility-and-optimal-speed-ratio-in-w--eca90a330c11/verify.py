"""Numerical and symbolic checks for the third-harmonic pursuit susceptibility.

Requires Python 3, numpy, scipy, sympy. Finite checks corroborate, not prove,
continuum results. The analytical proof is in RESULT.md.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root
import sympy as sp

x = sp.symbols('x', real=True)
F = x * (1 - x) / (4 * (9 - 5 * x))
assert sp.simplify(sp.diff(F, x) - (5*x*x - 18*x + 9)/(4*(9-5*x)**2)) == 0
assert sp.simplify(F.subs(x, sp.Rational(3,5))) == sp.Rational(1,100)
assert sp.solve(sp.together(sp.diff(F,x)).as_numer_denom()[0],x) == [sp.Rational(3,5),sp.Integer(3)]

def rhs(t, vals, n, eps):
    z = vals[0] + 1j * vals[1]
    w = 1 + eps * (np.exp(-2j*t) - 1)/2
    speed = np.sqrt(np.sin(t)**2 + (1 - eps)**2 * np.cos(t)**2)
    gap = w-z
    dz = -1j*z + n*speed*gap/abs(gap)
    return [dz.real,dz.imag]

def orbit(n, eps):
    r = np.sqrt(1-n*n)
    z0 = n*(n-1j*r)
    init = np.array([z0.real,z0.imag])
    def integrate(y, dense=False):
        return solve_ivp(rhs,[0,2*np.pi],y,args=(n,eps),
                         atol=3e-13,rtol=3e-12,max_step=.035,
                         dense_output=dense)
    solroot = root(lambda y: integrate(y).y[:,-1] - y,init, tol=1e-10)
    assert solroot.success or np.linalg.norm(solroot.fun) < 1e-10
    sol = integrate(solroot.x, dense=True)
    assert np.linalg.norm(sol.y[:,-1]-solroot.x) < 2e-9
    t = 2*np.pi*np.arange(4096)/4096
    zz = sol.sol(t)
    z = zz[0]+1j*zz[1]
    pp = z*np.exp(1j*t)
    assert np.min(np.abs(1 + eps*(np.exp(-2j*t)-1)/2-z)) > .02
    return np.mean(pp*np.exp(-3j*t))

checks=0
for n in [.2, .5, np.sqrt(3/5), .9]:
    r=np.sqrt(1-n*n)
    predicted=(1j*n*(r+1j*n))/(2*(3-2j*n/r))
    modulus=n*r/(2*np.sqrt(9-5*n*n))
    assert abs(abs(predicted)-modulus) < 5e-14
    if abs(n-np.sqrt(3/5))<1e-12:assert abs(modulus-.1)<1e-14
    last_err=None
    for eps in [.004,.002]:
        measured=orbit(n,eps)/eps
        err=abs(measured-predicted)
        assert err < .001 and (last_err is None or err<last_err*.66)
        print(f'CASE n={n:.9f} eps={eps:.3f} predicted={predicted} observed={measured} error={err:.3g}')
        last_err=err
        checks+=1
print('VERIFY_OK symbolic_maximum=1 numerical_fourier_cases='+str(checks)+' accurate_periodic_shooting=8')
