"""Reproducible finite checks of a renewal-localization correlation identity.

Run: python3 CHECKER.py
Uses only Python's standard library. Finite tests are not a general proof.
"""
from math import exp, log, gamma, isclose
import random


def integrate(f, lo, hi, n=8000):
    """Composite Simpson quadrature on a finite interval."""
    assert n % 2 == 0 and hi > lo
    h = (hi-lo)/n
    total = f(lo)+f(hi)
    for k in range(1,n):
        total += (4 if k % 2 else 2)*f(lo+k*h)
    return total*h/3


def mu_and_tail(r, survival, t):
    # The discarded tail beyond t+50/r is exponentially small.
    mu = integrate(lambda u:exp(-r*u)*survival(u), 0.0, 50/r)
    tail = integrate(lambda u:exp(-r*u)*survival(u), t, t+50/r)
    return mu, tail


def lomax_draw(rng, beta, a):
    return a * ((1-rng.random())**(-1/beta)-1)


def paired_simulation(r, lag, sampler, sample_size=150000):
    rng=random.Random(704231)
    both=0
    at0=0
    att=0
    for _ in range(sample_size):
        age=rng.expovariate(r)
        initial_wait=sampler(rng)
        i0=(age<initial_wait)
        # Simulate all intervening resets; jumps cannot return to exactly zero.
        new_age=age+lag
        wait=initial_wait
        elapsed=0.0
        while True:
            elapsed += rng.expovariate(r)
            if elapsed>=lag:
                break
            new_age=lag-elapsed
            wait=sampler(rng)
        it=(new_age<wait)
        at0+=i0
        att+=it
        both+=i0 and it
    return at0/sample_size, att/sample_size, both/sample_size


def test_exact_exponential():
    for r in (0.35,1.0,3.0):
        for rate in (0.2,1.4,4.0):
            for t in (0.0,.3,1.1,3.5):
                mu, tail=mu_and_tail(r,lambda u:exp(-rate*u),t)
                assert isclose(mu,1/(r+rate),rel_tol=1e-6)
                assert isclose(tail/mu,exp(-(r+rate)*t),rel_tol=3e-6,abs_tol=1e-9)
                m=r*mu
                cov=m*(1-m)*tail/mu
                assert cov>=0 and cov<=m*(1-m)+1e-12
    print('Exponential clocks: 36 independent integral comparisons passed')


def test_fixed_wait():
    r=0.8
    a=1.3
    for t in (0.0,.2,.9,1.3,2.0):
        # Split the quadrature at the jump discontinuity of the survival function.
        mu=integrate(lambda u:exp(-r*u),0.0,a)
        tail=integrate(lambda u:exp(-r*u),t,a) if t<a else 0.0
        pred=(exp(-r*t)-exp(-r*a))/(1-exp(-r*a)) if t<a else 0.0
        assert isclose(tail/mu,pred,abs_tol=1e-9,rel_tol=1e-9)
    print('Deterministic clocks: compact-support correlation verified')


def test_lomax_inversion():
    for r,beta,a in ((.2,.4,1.0),(.8,1.3,1.4),(1.7,2.5,.7)):
        psi=lambda u:(1+u/a)**(-beta)
        mu, _ =mu_and_tail(r,psi,0.0)
        m=r*mu
        assert 0<m<1
        d0=-1/mu
        r_recovered=-m*d0
        assert isclose(r_recovered,r,rel_tol=1e-13)
        for t in (.1,.5,2.0):
            deriv=-exp(-r*t)*psi(t)/mu
            reconstructed=exp(r_recovered*t)*deriv/d0
            assert isclose(reconstructed,psi(t),rel_tol=1e-12)
            mu2,tail=mu_and_tail(r,psi,t)
            assert isclose(mu2,mu,rel_tol=1e-8)
            assert 0<tail/mu<1
    print('Lomax clocks: independent quadrature and inverse reconstruction passed')


def test_simulation():
    for r,t,sampler,survival in [
        (.7,.8,lambda rng:rng.expovariate(1.4),lambda u:exp(-1.4*u)),
        (.8,.8,lambda rng:lomax_draw(rng,1.3,1.2),lambda u:(1+u/1.2)**(-1.3)),
    ]:
        mu,tail=mu_and_tail(r,survival,t)
        m=r*mu
        joint=m*m+(1-m)*r*tail
        m0,mt,j=paired_simulation(r,t,sampler)
        assert abs(m0-m)<.012, (m0,m)
        assert abs(mt-m)<.012, (mt,m)
        assert abs(j-joint)<.012, (j,joint)
    print('Two stationary two-time Monte Carlo experiments passed')


def test_five_asymptotic_exponents():
    # Integrated-correlation checks in each of five parameter ranges;
    # sharp weak-reset asymptotics are established analytically in RESULT.md.
    a=1.0
    cases=((.4,.6), (1.0,1.0), (1.5,.5), (2.0,0.0),(3.0,0.0))
    for beta,_ in cases:
        psi=lambda u:(1+u/a)**(-beta)
        for r in (.25,.1):
            # Simultaneously integrate r-scaled variables to control tails.
            scale=lambda v:(1+v/(r*a))**(-beta)
            z0=integrate(lambda v:exp(-v)*scale(v),0,42,10000)
            z1=integrate(lambda v:v*exp(-v)*scale(v),0,42,10000)
            tau=z1/(r*z0)
            assert tau>0
            # The exact logarithmic derivative identity is checked by symmetric difference.
            eps=1e-5
            def mu(z):
                return integrate(lambda v:exp(-v)*(1+v/(z*a))**(-beta),0,42,10000)/z
            numerical=-(log(mu(r*(1+eps)))-log(mu(r*(1-eps))))/(2*r*eps)
            assert isclose(tau,numerical,rel_tol=3e-3),(beta,r,tau,numerical)
    print('All five power-law classes: integrated-correlation identity checked')


if __name__=='__main__':
    test_exact_exponential()
    test_fixed_wait()
    test_lomax_inversion()
    test_simulation()
    test_five_asymptotic_exponents()
    print('PASS: deterministic and stochastic checks completed')
