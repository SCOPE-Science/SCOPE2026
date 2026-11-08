#!/usr/bin/env python3
"""Deterministic numerical checks of the two-phase stationary flux construction.

Requires Python 3.10+ and scipy.  All infinite-parameter conclusions are
analytical statements in the accompanying proof; these tests are finite.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq

TEST_COUNT = 0

def check_near(x, y, tol=2e-9):
    global TEST_COUNT
    assert math.isfinite(x) and math.isfinite(y)
    assert abs(x-y) <= tol*(1+abs(y)), (x,y)
    TEST_COUNT += 1

def check_truth(x):
    global TEST_COUNT
    assert x
    TEST_COUNT += 1

def b_exact(p, t, c, ell, gc):
    if p == 1:
        return c / gc * math.log(t)/t
    return c*p*ell**(p-1)/(gc*(p-1))*(t**(-1/p)-t**(-1))

def t_star(p):
    return math.e if p == 1 else p**(p/(p-1))

def run():
    c, ell, g, alpha, M = 1.1, 2.0, 0.4, 1.3, 9.0
    for p in (0.5, 0.75, 1.0):
        f = lambda u: c*u**p
        fp = lambda u: c*p*u**(p-1)
        fs = f(ell)
        gc = 2*fs/M
        for t in (1.05, 1.5, 2.4, 4.2):
            gamma = gc*t
            r = (math.sqrt(alpha*alpha+4*gamma*gamma)-alpha)/2
            q = math.sqrt(r/(r+alpha))
            center = ell*t**(1/p)
            b = b_exact(p,t,c,ell,gc)
            check_near(gamma, math.sqrt(r*(r+alpha)))
            check_near(f(center),gamma*M/2)
            check_near(b, quad(lambda u: fp(u)/u,ell,center,epsabs=1e-12)[0]/gamma)
            check_near(2*(f(center)-fs)/gamma,M-2*fs/gamma)
            check_truth(b>0)
            for s in (0.1,0.45,0.9):
                x = s*b
                residual = quad(lambda u: fp(u)/u,ell,center,epsabs=1e-11)[0] - gamma*x
                rho = brentq(lambda u: quad(lambda z: fp(z)/z,ell,u)[0]-residual,ell,center)
                check_near(fp(rho)*(-gamma*rho/fp(rho)), -gamma*rho)
                check_near(q*(-gamma*rho), -r*rho)
                check_near(-(r+alpha)*q*rho, -gamma*rho)
                check_truth(ell<rho<center)
            for gas in ("linear","rational"):
                if gas=="linear":
                    fg=lambda u: fs*u/g
                    fgp=lambda u: fs/g
                else:
                    fg=lambda u: fs*(1+g)*u/(g*(1+u))
                    fgp=lambda u: fs*(1+g)/(g*(1+u)**2)
                check_near(fg(g), fs)
                check_near(quad(fgp,0,g)[0]/gamma,fs/gamma)
                for dx in (0.03, 0.13, 0.7):
                    density=brentq(lambda u: quad(lambda z: fgp(z)/z,u,g)[0]/gamma-dx,1e-12,g)
                    check_truth(0<density<g)
                    check_near(fgp(density)*(-gamma*density/fgp(density)),-gamma*density)
                    check_near(q*(-gamma*density),-r*density)
                    check_near(-(r+alpha)*q*density,-gamma*density)
        st=t_star(p)
        check_truth(st>1)
        check_near((b_exact(p,st*0.999,c,ell,gc)-b_exact(p,st*1.001,c,ell,gc)),0,tol=2e-5)
        for t in (1.0001,1.1,1.25,st*0.95,st*1.05,st*2,st*10):
            if t != st: check_truth(b_exact(p,st,c,ell,gc)>b_exact(p,t,c,ell,gc))
    check_near(t_star(0.5),2.0)
    check_near(t_star(1.0),math.e)
    check_truth(t_star(0.4)<t_star(0.6)<t_star(0.9)<t_star(1.0))
    print("PASS:",TEST_COUNT,"flux, mass, matching, branch and sharp-optimizer checks")

if __name__=="__main__":
    run()
