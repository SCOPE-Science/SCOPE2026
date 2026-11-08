#!/usr/bin/env python3
"""Independent finite checks of the free-swimmer angular-inertia formulas.

Proof of the continuum theorem is analytic, in RESULT.md; this program does
not claim an exhaustive or independently certified proof.
"""
import math

COUNT = 0

def check(test, label):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(label)


def variance_ou(t, tau, dr):
    # From double integration of R(u)=dr/tau*exp(-abs(u)/tau).
    # Integrate 2 * integral_0^t (t-s)R(s) ds.
    return 2.0 * dr * (t + tau * math.expm1(-t / tau))


def covariance_kernel(t, tau, dr):
    return math.exp(-variance_ou(t, tau, dr) / 2.0)


def integral(tau, omega, dr=1.0):
    # Composite Simpson, with tail chosen by the exact exponent g(T)>=42.
    if tau == 0:
        return dr / (dr * dr + omega * omega)
    top = max(1 / dr, math.sqrt(tau / dr))
    while -math.log(covariance_kernel(top, tau, dr)) < 42:
        top *= 2
    step = min(0.035 / dr, 0.035 / (abs(omega) + 0.3))
    n = max(200, math.ceil(top / step))
    if n % 2:
        n += 1
    h = top / n
    accumulator = covariance_kernel(0, tau, dr)
    for j in range(1, n):
        t = j * h
        accumulator += (4 if j % 2 else 2) * covariance_kernel(t, tau, dr) * math.cos(omega*t)
    accumulator += covariance_kernel(top, tau, dr) * math.cos(omega*top)
    return accumulator * h / 3


def optimize(omega, dr=1):
    # Bracket a numerical maximum on a logarithmic mesh, golden section refine.
    lo, hi = -9.0, math.log(max(1000.0, 100 * dr / omega**2))
    mesh = [lo + (hi - lo)*j/72 for j in range(73)]
    values = [integral(math.exp(z), omega, dr) for z in mesh]
    idx = max(range(len(values)), key=lambda j: values[j])
    check(0 < idx < len(values)-1, 'interior maximum in search range')
    a, b = mesh[idx - 1], mesh[idx + 1]
    q = (math.sqrt(5) - 1) / 2
    c, d = b - q*(b-a), a + q*(b-a)
    fc, fd = integral(math.exp(c), omega, dr), integral(math.exp(d), omega, dr)
    for _ in range(48):
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - q*(b-a)
            fc = integral(math.exp(c), omega, dr)
        else:
            a, c, fc = c, d, fd
            d = a + q*(b-a)
            fd = integral(math.exp(d), omega, dr)
    z=(a+b)/2
    return math.exp(z), integral(math.exp(z), omega, dr)


def run():
    # Check stationary angular OU variance against an independently
    # discretized covariance double-integral (trapezoid in separation).
    for dr in (0.7, 1.0, 2.2):
        for tau in (0.08, 0.5, 2.0):
            for t in (0.2, 1.0, 3.0):
                steps=4000
                h=t/steps
                numerical=0.0
                for j in range(steps+1):
                    s=j*h
                    term=2 * (t-s) * (dr/tau) * math.exp(-s/tau)
                    numerical+=(0.5 if j in (0,steps) else 1)*term*h
                exact=variance_ou(t,tau,dr)
                check(abs(numerical-exact)<2e-5*max(1,exact),'OU integrated variance')
    # Closed white-noise limit and first inertia derivative.
    for om in (0.0, 0.25, 1.0, 3.0):
        base=1/(1+om*om)
        check(abs(integral(0,om)-base)<1e-14,'white-noise limit')
        for tau in (0.01,0.025):
            numerical_slope=(integral(tau,om)-base)/tau
            analytical_slope=base
            check(abs(numerical_slope-analytical_slope)<0.045,'small inertia derivative')
    for tau in (0.06, 0.6, 3, 50):
        for om in (0.2, 1.0):
            check(abs(integral(tau,om)-integral(tau,-om))<2e-8,'chirality parity')
            check(integral(tau,om)>-1e-7,'positive spectral diffusivity')
    zero_values=[integral(t,0) for t in (0.02,0.1,1,10,100,1000)]
    check(all(a < b for a,b in zip(zero_values,zero_values[1:])), 'zero chirality strict monotonicity')
    check(abs(zero_values[-1]/math.sqrt(math.pi*1000/2)-1)<0.03,'zero chirality Gaussian tail')
    # Verify the sharp crossover and no-infinity-maximum numerically.
    fstar=math.sqrt(math.pi/(2*math.e))
    for om,tol_x,tol_f in ((0.3,0.18,0.04),(0.1,0.07,0.012),(0.03,0.022,0.004)):
        tau,k=optimize(om)
        check(abs(om*om*tau-1)<tol_x,'rescaled optimal angular inertia')
        check(abs(om*k-fstar)<tol_f,'rescaled maximal diffusivity')
        check(k>integral(0,om),'finite optimum beats white-noise rotation')
        check(k>integral(300/om**2,om),'finite optimum beats extreme inertia')
        print('omega=%.3f tau*=%.7f omega^2*tau*=%.7f omega*Kmax=%.7f' %(om,tau,om*om*tau,om*k))
    print('PASS: %d numerical consistency assertions; analytic proof is in RESULT.md' %COUNT)

if __name__ == '__main__':
    run()
