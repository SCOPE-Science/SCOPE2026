"""Reproducible numerical checks for a critical logistic feedforward threshold flow.
Dependencies: Python 3, scipy, numpy. These tests supplement an analytic proof.
"""
from math import sqrt, tanh, isclose
from scipy.integrate import solve_ivp, quad
A0=0.8
B0=0.5
U0=0.2
C=sqrt(1.5)

def g(z): return z-tanh(z)
def RHS(t,z,p):
    u,a,b=z
    return [-u+tanh(p*a-(1-p)*b),-g(a),-g(b)]

def check(p, T):
    sol=solve_ivp(lambda t,z: RHS(t,z,p),(0,T),[U0,A0,B0],method='DOP853',rtol=1e-11,atol=1e-13)
    if not sol.success: raise AssertionError(sol.message)
    u,a,b=sol.y[:,-1]
    assert a>0 and b>0 and abs(a)<A0 and abs(b)<B0
    return u,a,b

tau=quad(lambda z:1/g(z),B0,A0,epsabs=1e-11,epsrel=1e-11)[0]
expected=C*tau/4
print('signed_time_shift',format(tau,'.13f'),'balanced_coefficient',format(expected,'.13f'))
for T in [300.,1000.,3000.]:
    u,a,b=check(0.5,T)
    ratio=T**1.5*u/expected
    print('balanced',T,'amplitude',format(T**1.5*u,'.10f'),'ratio',format(ratio,'.10f'))
    assert abs(ratio-1)<0.025
    for p in [0.3,0.7]:
        up,aa,bb=check(p,T)
        target=(2*p-1)*C
        print('unbalanced',p,T,'rescaled',format(sqrt(T)*up,'.10f'),'target',format(target,'.10f'))
        assert abs(sqrt(T)*up/target-1)<0.03
for p in [0.3,0.5,0.7]:
    u,a,b=check(p,100)
    assert a>b>0
# Exact symmetry of terminal states causes no relay forcing.
for T in [0,3,100]:
    out=solve_ivp(lambda t,z: RHS(t,z,0.5),(0,max(T,1e-5)),[U0,0.65,0.65],rtol=1e-11,atol=1e-13,dense_output=True)
    assert abs(out.sol(T)[0]-U0*__import__('math').exp(-T)) < 1e-9
# Critical scalar time-shift: a(t) and b(t-tau) coincide for t>=tau.
for T in [200.,1000.]:
    va=solve_ivp(lambda t,z:[-g(z[0])],(0,T),[A0],rtol=1e-12,atol=1e-14)
    vb=solve_ivp(lambda t,z:[-g(z[0])],(0,T-tau),[B0],rtol=1e-12,atol=1e-14)
    assert abs(va.y[0,-1]-vb.y[0,-1]) < 2e-9
for T in [500.,2000.]:
    for lam in [-2.,0.,1.5]:
        u,a,b=check(0.5+lam/T,T)
        prediction=C*(2*lam+tau/4)
        assert abs((T**1.5)*u-prediction)<0.012
print('VERIFY_OK critical_relay=1 symmetric_exact=1 signed_quadrature=1 balanced_samples=3 unbalanced_samples=6 time_shift_samples=2 crossover_samples=6')
