#!/usr/bin/env python3
"""Numerical cross-checks of a visible-target stochastic-return search theorem.

Dependencies: Python 3, NumPy, SciPy. All tests use independent numerical
quadrature of finite-rate killed-Brownian resolvents, plus return ODE solvers.
No finite set of numerical tests proves the asymptotic theorem.
"""
import math
from scipy.integrate import quad, solve_ivp
from scipy.special import pbdv


def boundary_data(D, L, kappa, s):
    """Return splitting transforms u_s,v_s and one-sided derivatives at 0."""
    if kappa == 0:
        if s == 0:
            return (lambda x: (max(x, 0.0) / L if x < L else 1.0),
                    lambda x: (1.0 - x / L if x > 0 else 1.0),
                    1.0 / L, 0.0, -1.0 / L)
        w = math.sqrt(s / D)
        return (lambda x: math.sinh(w * x) / math.sinh(w * L) if x > 0 else 0.0,
                lambda x: math.sinh(w * (L - x)) / math.sinh(w * L) if x > 0 else math.exp(w * x),
                w / math.sinh(w * L), w, -w / math.tanh(w * L))

    def ode(x, y):
        return (y[1], (kappa*x*y[1] + s*y[0])/D,
                y[3], (kappa*x*y[3] + s*y[2])/D)
    sol = solve_ivp(ode, (0., L), (1., 0., 0., 1.),
                    dense_output=True, rtol=1e-11, atol=1e-12)
    assert sol.success
    A_L, _, B_L, _ = sol.y[:, -1]
    C = A_L / B_L
    if s == 0:
        def vneg(x): return 1.0
        vprime_minus = 0.0
    else:
        nu = -s / kappa
        p0, pprime0 = pbdv(nu, 0.)
        vprime_minus = -math.sqrt(kappa / D) * pprime0 / p0
        def vneg(x):
            z = -math.sqrt(kappa / D) * x
            return math.exp(z*z/4) * pbdv(nu, z)[0] / p0
    def u(x):
        return sol.sol(x)[2]/B_L if x > 0 else 0.0
    def v(x):
        if x <= 0: return vneg(x)
        a, _, b, _ = sol.sol(x)
        return a - C*b
    return u, v, 1/B_L, vprime_minus, -C


def resolvent_density(x, D, L, theta):
    w = math.sqrt(theta/D)
    return (math.exp(-w * abs(x)) - math.exp(-w*(2*L-x))) / (2*D*w)


def finite_transform(D, L, kappa, r, s, q, marking):
    # Marking is either number of alarms / sqrt(r), or sqrt(r) times active-search time.
    theta = r+s+(q*math.sqrt(r) if marking == 'active' else 0.)
    mark = math.exp(-q/math.sqrt(r)) if marking == 'alarm' else 1.0
    u, v, *_ = boundary_data(D, L, kappa, s)
    def integral(fn, left, right):
        return quad(lambda x:r*resolvent_density(x,D,L,theta)*fn(x), left,right,
                    epsabs=4e-11, epsrel=4e-11, limit=160)[0]
    A = integral(u, 0., L)
    B = integral(v, -8., 0.) + integral(v, 0., L)
    direct = math.exp(-L*math.sqrt(theta/D))
    return (direct+mark*A)/(1.-mark*B)


def limiting_transform(D, L, kappa, s, q):
    _, _, up, vm, vp = boundary_data(D, L, kappa, s)
    return up / (vm-vp + 2*q/math.sqrt(D))


def main():
    # Independently verify exact single-attempt formula for a drift-free return.
    for D,L,r in [(1.,1.,0.3),(1.,1.,2.),(0.5,1.4,4.),(2.,0.7,100.),(1.,1.,5000.)]:
        theta = r
        w = math.sqrt(theta/D)
        u, _, *_ = boundary_data(D,L,0.,0.)
        actual = math.exp(-w*L) + quad(
            lambda x:r*resolvent_density(x,D,L,theta)*u(x), 0.,L,
            epsabs=1e-13)[0]
        expected = -math.expm1(-2*w*L)/(2*w*L)
        assert abs(actual-expected)<2e-11, (D,L,r,actual,expected)
    print('PASS: 5 exact drift-free success-probability checks')

    for D,L,kappa in [(1.,1.,0.),(1.,1.,0.7),(0.6,1.3,1.4)]:
        # Scale-function and success-probability leading constant from an independent quadrature.
        H = quad(lambda y: math.exp(kappa*y*y/(2*D)),0,L,epsabs=1e-13)[0]
        u, _, up, vm, vp = boundary_data(D,L,kappa,0.)
        assert abs(up-1/H)<3e-10 and abs(vm-vp-1/H)<3e-10
        for r in [400.,1600.,6400.]:
            p=math.exp(-L*math.sqrt(r/D))+quad(
                lambda x:r*resolvent_density(x,D,L,r)*u(x),0,L,epsabs=1e-12)[0]
            approx=math.sqrt(D)/(2*H)
            assert abs(math.sqrt(r)*p-approx)<0.07*approx, (D,L,kappa,r,p)
        print('PASS: three large-rate per-cycle success asymptotics, kappa=',kappa)

    for D,L,kappa,s,q in [(1.,1.,0.,0.,0.4),(1.,1.,0.,0.2,0.5),
                            (1.,1.,0.,2.,0.25),(1.,1.,0.7,0.5,0.3),
                            (0.6,1.3,1.4,0.8,0.3)]:
        target=limiting_transform(D,L,kappa,s,q)
        for rate in [400.,2500.,10000.]:
            marked=finite_transform(D,L,kappa,rate,s,q,'alarm')
            active=finite_transform(D,L,kappa,rate,s,q,'active')
            assert abs(marked-target)<0.05, (D,L,kappa,s,q,rate,marked,target)
            assert abs(active-target)<0.05, (D,L,kappa,s,q,rate,active,target)
            assert abs(marked-active)<0.015, (rate,marked,active)
        print('PASS: 6 marked-resolvent comparisons, kappa,s,q=',kappa,s,q)

    # The drift-free limiting transform has an independent elementary formula.
    for s,q in [(0.,0.7),(.03,.2),(.5,1.),(5.,.5)]:
        expected = 1/(1+2*q) if s==0 else math.exp(-math.sqrt(s))/(1+q*(-math.expm1(-2*math.sqrt(s)))/math.sqrt(s))
        assert abs(limiting_transform(1.,1.,0.,s,q)-expected)<1e-12
    print('PASS: 4 independent closed-form limiting Laplace checks')

    # Cross-check the closed positive covariance of the *limiting* count and
    # completion time against finite-difference derivatives of the exact
    # limiting Laplace transform. These are not finite-rate moment claims.
    for D,L,kappa in [(1.,1.2,1.1),(.6,.8,2.0)]:
        phi=lambda x: kappa*x*x/(2*D)
        H=lambda x: quad(lambda y: math.exp(phi(y)),0,x,epsabs=1e-13)[0]
        h=H(L)
        a1=quad(lambda x: math.exp(phi(x))*quad(lambda y: math.exp(-phi(y)),0,x)[0]/D,0,L)[0]
        b1=quad(lambda x: math.exp(phi(x))*quad(lambda y: math.exp(-phi(y))*H(y),0,x)[0]/D,0,L)[0]
        mean_slope=math.sqrt(math.pi/(2*kappa*D))
        covariance=2/math.sqrt(D)*(h*a1-b1+mean_slope*h*h)
        assert covariance>0
        for eps in [2e-4,5e-5]:
            _,_,up,vm,vp=boundary_data(D,L,kappa,eps)
            B=1/up
            F=(vm-vp)/up
            C=2*B/math.sqrt(D)
            estimate=C*(F-1)/eps-(C-2*h/math.sqrt(D))/eps
            assert abs(estimate-covariance)<2e-3*max(1,covariance), (estimate,covariance)
    print('PASS: 4 finite-difference cross-checks of positive limiting covariance')
    print('PASS ALL; numerical tests do not substitute for the analytical proof')

if __name__=='__main__': main()
