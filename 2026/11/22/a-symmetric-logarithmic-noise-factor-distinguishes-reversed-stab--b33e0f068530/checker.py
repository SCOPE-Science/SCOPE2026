"""Finite numerical checks for a stable/inverse-stable clock comparison.

This tests identities and signs on parameter grids. It is not the proof of
Lévy-measure positivity or of the all-parameter stochastic order.
"""
import math
import mpmath as mp

mp.mp.dps = 42
checks = 0

def close(u, v, tol=mp.mpf('4e-26')):
    global checks
    assert abs(u-v) <= tol * (1 + abs(u) + abs(v)), (u, v)
    checks += 1

def pos(x):
    global checks
    assert x > 0, x
    checks += 1

def mom_a(q, alpha, beta):
    a = 1/alpha
    return (mp.gamma(1-a*q)*mp.gamma(1+a*q)
            / (mp.gamma(1-q)*mp.gamma(1+beta*a*q)))

def mom_b(q, alpha, beta):
    a = 1/alpha
    return (mp.gamma(1-beta*a*q)*mp.gamma(1+q)
            / (mp.gamma(1-beta*q)*mp.gamma(1+beta*q)))

def excess(x, a, b):
    # Stable evaluation for finite x > 0.
    return (1/mp.expm1(x/a) + 1/mp.expm1(x/b)
            - 1/mp.expm1(x) - 1/mp.expm1(x/(a*b)))

for alpha_text in ['0.20','0.37','0.50','0.71','0.92']:
    for beta_text in ['0.10','0.24','0.50','0.79','0.93']:
        alpha, beta = mp.mpf(alpha_text), mp.mpf(beta_text)
        a, b = 1/alpha, beta
        for theta_text in ['0.01','0.05','0.17','0.47','0.83','1.35']:
            theta=mp.mpf(theta_text)
            ratio=mom_a(1j*theta,alpha,beta)/mom_b(1j*theta,alpha,beta)
            sinh_ratio=(mp.sinh(mp.pi*theta)*mp.sinh(mp.pi*a*b*theta)
                        /(mp.sinh(mp.pi*a*theta)*mp.sinh(mp.pi*b*theta)))
            close(ratio,sinh_ratio)
            pos(sinh_ratio)
            pos(1-sinh_ratio)
        for exponent in [mp.mpf('-3.0'),mp.mpf('-1.2'),mp.mpf('-0.6'),mp.mpf('-0.1'),
                         mp.mpf('0.0'),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2')]:
            x=mp.power(10,exponent)
            pos(excess(x,a,b))
        variance=(mp.pi**2/3)*(a*a-1)*(1-b*b)
        # Log-characteristic-function curvature, evaluated analytically
        g=lambda q: mp.log(mom_a(q,alpha,beta)/mom_b(q,alpha,beta))
        close(mp.diff(g,0,2),variance,mp.mpf('1e-22'))
        close(mp.diff(g,0,1),0,mp.mpf('1e-22'))
        # A numerical test of the Levy-Khintchine integral, not a certificate.
        theta=mp.mpf('0.17')
        log_ratio=mp.log(mom_a(1j*theta,alpha,beta)/mom_b(1j*theta,alpha,beta))
        def integrand(x):
            if x == 0:
                return mp.mpf(0)
            return 2*(mp.cos(theta*x)-1)*excess(x,a,b)/x
        integral=mp.quad(integrand,[mp.mpf('0.000001'),mp.mpf('0.01'),mp.mpf('1'),mp.mpf('20'),mp.inf])
        # The missing [0, 1e-6] interval is bounded using its small-x limit.
        # Its leading contribution is -theta^2*(a-1)*(1-b)*1e-6.
        missing=-theta*theta*(a-1)*(1-b)*mp.mpf('0.000001')
        close(log_ratio,integral+missing,mp.mpf('1e-10'))
print('PASS',checks,'finite diagnostic comparisons')
