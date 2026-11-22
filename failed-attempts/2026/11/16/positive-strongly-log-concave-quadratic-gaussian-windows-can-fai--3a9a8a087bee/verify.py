#!/usr/bin/env python3
"""Supplementary high-precision checks for an explicit quadratic-Gaussian Gabor obstruction.

Requires Python 3 and mpmath. The general theorem uses the analytic proof;
finite-precision sums do not establish the all-parameter claim.
"""
import mpmath as mp

mp.mp.dps = 85
TEST_GAMMAS = [mp.mpf('0.25'), mp.mpf('0.4'), mp.mpf('0.75'),
               mp.mpf('1'), mp.mpf('1.5'), mp.pi**2 / 6]
N = 65
checks = 0

def chk(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def theta_original(g):
    return sum((-1)**k * mp.exp(-g*k*k) for k in range(-N, N+1))

def theta_derivative(g):
    return -sum((-1)**k * k*k * mp.exp(-g*k*k) for k in range(-N, N+1))

def theta_dual(g):
    return mp.sqrt(mp.pi/g) * sum(mp.exp(-mp.pi**2*(m+mp.mpf('0.5'))**2/g)
                                      for m in range(-N, N+1))

def coefficient(g, c, t):
    return (t*t+c)*mp.exp(-g*t*t)

def H(g, c, t):
    return sum((-1)**k * coefficient(g,c,t-k) for k in range(-N, N+1))

def Fourier(g,c,xi):
    return mp.sqrt(mp.pi/g)*mp.exp(-mp.pi**2*xi*xi/g) * \
           (c+1/(2*g)-mp.pi**2*xi*xi/(g*g))

for g in TEST_GAMMAS:
    theta = theta_original(g)
    derivative = theta_derivative(g)
    c = derivative/theta
    dual = theta_dual(g)
    z = [mp.exp(-mp.pi**2*(m+mp.mpf('0.5'))**2/g) for m in range(-N,N+1)]
    moment = sum((m+mp.mpf('0.5'))**2*zz for m,zz in zip(range(-N,N+1),z))/sum(z)
    c_dual = -1/(2*g) + mp.pi**2*moment/(g*g)
    chk(theta > 0 and abs(theta-dual)<mp.mpf('1e-70'), 'Poisson theta sum')
    chk(abs(c-c_dual)<mp.mpf('1e-65'), 'dual derivative')
    chk(g*c>1 and c>0, 'positive strong log concavity constant')
    chk(moment>mp.mpf('0.25'), 'strict dual half-integer second moment')
    for t in [mp.mpf('-7.5'), mp.mpf('-4'), mp.mpf('-1.5'), mp.mpf('-1'),
              mp.mpf('-0.5'), mp.mpf('0'), mp.mpf('0.5'), mp.mpf('1'),
              mp.mpf('2.5'), mp.mpf('4.5'), mp.mpf('7')]:
        chk(abs(H(g,c,t))<mp.mpf('1e-65'), 'alternating translate annihilation')
    print('H23',mp.nstr(H(g,c,mp.mpf('0.23')),10)); chk(abs(H(g,c,mp.mpf('0.23')))>mp.mpf('1e-65'), 'nontrivial alternating translate')
    for t in [mp.mpf('0'), mp.mpf('0.25'), mp.mpf('0.75'),
              mp.mpf('1.1'), mp.mpf('3.2')]:
        second = 2*(c-t*t)/(c+t*t)**2-2*g
        chk(second < 0 and second <= 2/c-2*g+mp.mpf('1e-65'),
            'log curvature strict inequality')
    chk(any(abs(Fourier(g,c,mp.mpf(k)+mp.mpf('0.5')))>mp.mpf('1e-50')
            for k in [0,1,2]), 'nonzero Fourier series coefficient')
    print('gamma=',mp.nstr(g,16), 'c=',mp.nstr(c,30),
          'gamma*c=',mp.nstr(g*c,18), 'H(0)=',mp.nstr(H(g,c,0),6))

print('PASS', checks, 'independent finite precision checks; proof is analytic')
