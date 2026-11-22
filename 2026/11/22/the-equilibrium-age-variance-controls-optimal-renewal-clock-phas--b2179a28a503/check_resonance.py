"""Reproduce exact stationary-age harmonic and slow-drive optimum for renewal resetting.
Only standard mathematical computations; not an independent certification.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar

def variance_age_gamma(k):
    return (k+1)*(k+5)/(12*k*k)

def exact_gamma(k, r, omega, tau):
    z=k*r+1j*omega
    # Stationary age density r exp(-kr a) sum_{j=0}^{k-1}(kr a)^j/j!.
    w=0j
    for j in range(k):
        w += (k*r/z)**j * sum((z*tau)**ell/math.factorial(ell) for ell in range(j+1))
    return abs(r*np.exp(-z*tau)/z*w)

def exact_deterministic(r,omega,tau):
    if r*tau >= 1: return 0.
    y=omega*(1/r-tau)/2
    return (1-r*tau) * abs(np.sinc(y/np.pi))

def opt_exact(fun,omega,tau):
    # Full log-rate minimization, range physically broad enough for these test cases
    points=np.geomspace(1e-7,10/tau,500)
    values=np.array([fun(float(z),omega,tau) for z in points])
    i=int(np.argmax(values))
    left=max(i-2,0); right=min(i+2,len(points)-1)
    res=minimize_scalar(lambda log_r:-fun(math.exp(log_r),omega,tau),
                        bounds=(math.log(points[left]),math.log(points[right])),method='bounded',
                        options={'xatol':1e-13})
    return math.exp(res.x),-res.fun

def checks():
    tau=1.7
    assert variance_age_gamma(1)==1
    assert abs(variance_age_gamma(2)-7/16)<1e-14
    assert abs(variance_age_gamma(3)-8/27)<1e-14
    for omega in (0.03,0.008,0.002,0.0005):
        for k in (1,2,3,5,12):
            r,g=opt_exact(lambda x,y,z:exact_gamma(k,x,y,z),omega,tau)
            pred=(variance_age_gamma(k)*omega**2/tau)**(1/3)
            loss=(1.5)*(variance_age_gamma(k)*tau**2)**(1/3)*omega**(2/3)
            print(f'k={k:2d} w={omega:.4g} r={r:.8g} /pred={r/pred:.6f}  loss/leading={(1-g)/loss:.6f}')
            if omega<=0.0005:assert abs(r/pred-1)<0.055
        rd,gd=opt_exact(exact_deterministic,omega,tau)
        pd=((1/12)*omega**2/tau)**(1/3)
        print(f'deterministic w={omega:.4g} r={rd:.8g} /pred={rd/pd:.6f}')
        if omega<=0.0005:assert abs(rd/pd-1)<0.055
    # Exact Poisson formula consistency.
    for r in (0.1,0.4,2.3):
        for w in (0.03,0.7,2.0):
            assert abs(exact_gamma(1,r,w,tau)-math.exp(-r*tau)*r/math.hypot(r,w))<1e-14
    # Gamma age variance bound and monotone Erlang approach to periodic age variance.
    vs=[variance_age_gamma(k) for k in range(1,51)]
    assert all(x>1/12 for x in vs)
    assert all(vs[i+1]<vs[i] for i in range(49))
    print('ALL CHECKS PASSED')

if __name__=='__main__':checks()
