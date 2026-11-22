"""Numerical diagnostics for the hyperbolic ideal-quadrilateral clearance law.

Run with Python 3.10+ and SciPy; checks are independent finite diagnostics,
not a substitute for the local-limit proof in RESULT.md.
"""
from math import asinh, pi, sqrt, sinh
from scipy.integrate import quad


def model(c2, h):
    c, s = sqrt(c2), sqrt(1-c2)
    k0 = 1 / sqrt(4*c2-1)
    rho = asinh(k0)
    k = sinh(rho-h)
    def integrand(x):
        E = 1-x*x
        a = 1 + c*c*k*k
        rad = a*E-s*s
        if rad<0: return 0.
        yhi = (s - c*k*sqrt(rad))/a
        if yhi <= 0: return 0.
        yhi = min(yhi, s)
        f = E-(c-x)**2/(s*s*k*k)
        ylo = sqrt(f) if f>0 else 0.
        if ylo >= yhi: return 0.
        def antideriv(y): return y/(E*sqrt(max(1e-300, E-y*y)))
        return max(0.,antideriv(yhi)-antideriv(ylo))
    xstar = (2*c2-1)/c
    if c2 == 0.5:
        low, high = 0., min(c,5*h)
    elif c2-0.5 > 20*sqrt(h):
        L = 4*c2-1
        U = (1-c2)*L/c2
        V = 2*(1-c2)*L/(2*c2-1)
        low, high = max(0.,xstar-2*V*h), min(c,xstar+2*U*h)
    else:
        low, high = 0., min(c,xstar+4*sqrt(h))
    boundaries=[low,high]
    if low < xstar <high: boundaries=[low,xstar,high]
    v=0.
    for a0,b0 in zip(boundaries,boundaries[1:]):
        z,err=quad(integrand,a0,b0,epsabs=1e-13,epsrel=1e-9,limit=300)
        v+=z
    return 4*v/(2*pi)


def area(lam):
    x0sq = max(0., 8*lam*lam-2*sqrt(2))
    return 8*sqrt(2)*lam-(64/3)*lam**3+(2*sqrt(2)/3)*x0sq**1.5


def main():
    checks = 0
    for c2 in (0.64,0.81):
        exact = (4*c2-1)**1.5/(pi*(2*c2-1))
        vals=[]
        for h in (2e-4,4e-5):
            p = model(c2,h)
            ratio = p/(h*h*exact)
            print(f'fixed c^2={c2}: h={h:.1e}, measured/predicted={ratio:.7f}')
            assert abs(ratio-1)<0.035, (c2,h,ratio)
            vals.append(abs(ratio-1))
            checks+=1
        assert vals[1]<vals[0]
    for lam in (0.3,0.55,0.75,1.2):
        h=1e-5
        c2=0.5+lam*sqrt(h)
        p=model(c2,h)
        predicted = area(lam)*h**1.5/(2*pi)
        ratio = p/predicted
        print(f'critical lambda={lam}: measured/predicted={ratio:.7f}')
        assert abs(ratio-1)<0.05,(lam,ratio)
        checks+=1
    # At the square the geometric blow-up is an axis-aligned square.
    h=3e-4
    p=model(0.5,h)
    ratio=p/(2*h*h/pi)
    print(f'square: measured/predicted={ratio:.7f}')
    assert abs(ratio-1)<0.04
    checks+=1
    print(f'PASS: {checks} analytical-asymptotic quadrature comparisons')


if __name__=='__main__': main()
