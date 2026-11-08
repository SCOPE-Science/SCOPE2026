"""Reproduce numerical checks for generalized-Gaussian spectral zero intensities.

Dependencies: Python 3, scipy, mpmath. The proof is analytic; numerical tests
are spot checks rather than certificates for every parameter.
"""
from math import exp, pi, sqrt
from scipy.integrate import quad
from scipy.optimize import brentq
import mpmath as mp


def posterior(beta, kappa, R):
    # For the tested R>=5 the positive saddle is dominant.
    potential = lambda x: 2 * pi * (x-R)**2 + kappa * abs(x)**beta
    if beta == 1:
        a = R - kappa/(4*pi)
    elif beta < 1:
        a = brentq(lambda x: 4*pi*(x-R)+kappa*beta*x**(beta-1), R/2, R)
    else:
        a = brentq(lambda x: 4*pi*(x-R)+kappa*beta*x**(beta-1), 1e-12, R)
    # Integrate the entire positive saddle interval and both remote tails, to
    # avoid falsely improving agreement by omitting distant contributions.
    z = potential(a)
    fun = lambda x: exp(-potential(x)+z)
    i0 = quad(fun, -float('inf'), 0, epsabs=1e-12)[0] + quad(fun, 0, a, epsabs=1e-12)[0] + quad(fun, a, float('inf'), epsabs=1e-12)[0]
    i1 = quad(lambda x: (x-a)*fun(x), -float('inf'), 0, epsabs=1e-12)[0] + quad(lambda x: (x-a)*fun(x), 0, a, epsabs=1e-12)[0] + quad(lambda x: (x-a)*fun(x), a, float('inf'), epsabs=1e-12)[0]
    mean = a+i1/i0
    i2 = quad(lambda x: (x-mean)**2*fun(x), -float('inf'), 0, epsabs=1e-12)[0] + quad(lambda x: (x-mean)**2*fun(x), 0, a, epsabs=1e-12)[0] + quad(lambda x: (x-mean)**2*fun(x), a, float('inf'), epsabs=1e-12)[0]
    return 4*pi*i2/i0, mean


def leading(beta,kappa,R):
    if beta < 1:
        return 1 + kappa*beta*(1-beta)/(4*pi)*R**(beta-2)
    if 1 < beta < 2:
        return 1 - kappa*beta*(beta-1)/(4*pi)*R**(beta-2)
    if beta == 2:
        return 2*pi/(2*pi+kappa)
    return (4*pi/(kappa*beta))**(1/(beta-1))/(beta-1)*R**(-(beta-2)/(beta-1))


def beta1_high_precision(kappa,R):
    mp.mp.dps=95
    k=mp.mpf(kappa); x=mp.mpf(R); a=2*mp.pi; shift=k/(2*a)
    norm=mp.sqrt(mp.pi)/(2*mp.sqrt(a))
    def convolved(t):
        return norm*mp.exp(k*k/(4*a))*(mp.exp(-k*t)*mp.erfc(mp.sqrt(a)*(shift-t)) + mp.exp(k*t)*mp.erfc(mp.sqrt(a)*(shift+t)))
    intensity=1+mp.diff(lambda z: mp.log(convolved(z)),x,2)/(4*mp.pi)
    estimate=k*mp.sqrt(2)/(2*mp.pi)*mp.exp(-2*mp.pi*x*x+k*x-k*k/(8*mp.pi))
    return float((1-intensity)/estimate)


if __name__ == '__main__':
    for beta, R, tol in [(0.5,100,0.003),(0.75,100,0.005),(1.3,100,0.006),(1.5,100,0.002),(2,100,1e-9),(3,500,0.003),(4,500,0.02)]:
        intensity,mean=posterior(beta,1,R)
        approx=leading(beta,1,R)
        ratio=(intensity-1)/(approx-1) if beta<2 else intensity/approx
        assert abs(ratio-1)<tol, (beta,R,ratio)
        if beta<1: assert intensity>1, (beta,R,intensity)
        if 1<beta: assert 0<intensity<1,(beta,R,intensity)
        print('tail_check', beta, R, f'{intensity:.12g}', f'{ratio:.8f}')
    for R in (2,3,4):
        ratio=beta1_high_precision(1,R)
        assert 0.8<ratio<1 and ratio>1-0.17/R,(R,ratio)
        print('laplace_edge',R,f'{ratio:.8f}')
    # Even spectral density: rho(0)<1 for nontrivial exponent.
    for beta in (0.5,0.75,1,1.5,3):
        v = lambda x: exp(-2*pi*x*x-abs(x)**beta)
        mass=quad(v,0,float('inf'))[0]
        e2=quad(lambda x:x*x*v(x),0,float('inf'))[0]/mass
        assert 0<4*pi*e2<1,(beta,e2)
    # Independently test d(mean)/dR=4*pi*posterior variance.
    for beta in (0.6,1.6,2,3):
        R=6; step=1e-3
        rp,m=posterior(beta,1,R)
        derivative=(posterior(beta,1,R+step)[1]-posterior(beta,1,R-step)[1])/(2*step)
        assert abs(derivative-rp)<2e-5,(beta,derivative,rp)
    print('ALL_STRETCHED_SPECTRAL_INTENSITY_CHECKS_PASSED')
