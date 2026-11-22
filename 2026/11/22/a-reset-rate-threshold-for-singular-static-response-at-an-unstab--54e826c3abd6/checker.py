"""Numerical consistency checks for a renewal-response asymptotic theorem.
The analytic proof, not this finite computation, establishes the limits.
Run: python checker.py
"""
from math import exp, log, sqrt, gamma
from scipy.integrate import solve_ivp


def stationary_mean(h, rho, horizon=150.0):
    assert 0 < h < 1 and rho > 0
    def ode(s, yy):
        y, acc = yy
        return [h+y-y**3, rho*exp(-rho*s)*y]
    z = solve_ivp(ode, (0, horizon), [0.0, 0.0], method='DOP853',
                  rtol=3e-11, atol=1e-13, max_step=0.20)
    assert z.success
    return z.y[1,-1]


def low_rate_constant(rho):
    assert 0<rho<1
    return 0.5*gamma((1-rho)/2)*gamma(1+rho/2)/gamma(1.5)


def test():
    total=0
    # Positivity, ordering, and cubic response to vanishing constant field.
    for rho in [0.35,0.7,1.0,1.4,2.0]:
        vals=[stationary_mean(h,rho) for h in [1e-3,1e-4,1e-5,1e-6]]
        assert all(0<vals[j+1]<vals[j]<1.1 for j in range(3))
        total+=4
    # Weak-field coefficients approach their respective exact asymptotes.
    for rho,h,tol in [(0.35,1e-6,0.02), (0.70,1e-7,0.07),
                      (1.,1e-7,0.05), (1.4,1e-7,0.14), (2.,1e-7,0.001)]:
        m=stationary_mean(h,rho)
        leading=(low_rate_constant(rho)*h**rho if rho<1 else
                 h*log(1/h) if rho==1 else h/(rho-1))
        error=abs(m/leading-1.)
        assert error<tol,(rho,h,error)
        total+=1
    # Near-critical crossover, finite fields give controlled preasymptotics.
    h=1e-9
    L=log(1/h)
    for lam in [-1.,0.,1.]:
        rho=1.+lam/L
        m=stationary_mean(h,rho)
        theory=1. if lam==0 else -__import__('math').expm1(-lam)/lam
        assert abs(m/(h*L)-theory)<0.09,(lam,m/(h*L),theory)
        total+=1
    # Linear-response side, direct calculus solution of variational equation.
    for rho in [1.5,2.5,4.0]:
        h=1e-9
        m=stationary_mean(h,rho)
        assert abs(m/h-1/(rho-1))<.03,(rho,m/h)
        total+=1
    print('PASS: '+str(total)+' numerical/asymptotic consistency checks')

if __name__=='__main__':
    test()
