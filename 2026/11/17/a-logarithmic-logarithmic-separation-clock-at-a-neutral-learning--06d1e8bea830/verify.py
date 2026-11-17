"""Reproduce exact critical-map identities and finite escape-clock checks."""
import math


def step_logit(m, d):
    t, s = math.tanh(m/2), math.tanh(d/2)
    den = 1-t*t*s*s
    return m-4*t*(1-s*s)/den, d+4*s*(1-t*t)/den


def logistic(u):
    return 1/(1+math.exp(-u))


def step_direct(m, d):
    x, y = logistic(m+d), logistic(m-d)
    fx = x/(x+(1-x)*math.exp(8*(y-.5)))
    fy = y/(y+(1-y)*math.exp(8*(x-.5)))
    u, v = math.log(fx/(1-fx)), math.log(fy/(1-fy))
    return (u+v)/2, (u-v)/2


def first_exit(m, eps, threshold=.035):
    d, n = eps, 0
    while d < threshold and n < 5000:
        m, d = step_logit(m, d)
        n += 1
    assert n < 5000
    return n


def check():
    for m in (-1.1, -.6, -.2, 0, .1, .4, 1.0):
        for d in (.0001, .003, .02, .04):
            a, b = step_logit(m, d), step_direct(m, d)
            assert max(abs(a[0]-b[0]),abs(a[1]-b[1])) < 3e-13
    for m0 in (.3, .5, 1.2):
        residuals=[]
        for L in (12, 20, 30, 45, 60, 80, 120, 160):
            n=first_exit(m0, math.exp(-L))
            pred=(L+math.log(L)/2)/math.log(3)
            residuals.append(n-pred)
        assert max(residuals)-min(residuals)<3.0, (m0,residuals)
        assert all(abs(r)<8 for r in residuals), residuals
    residuals=[]
    for L in (12, 20, 30, 45, 60, 80, 120, 160):
        n=first_exit(0, math.exp(-L))
        residuals.append(n-L/math.log(3))
    assert max(residuals)-min(residuals)<1.4, residuals
    try:
        import sympy as s
        m,d=s.symbols('m d')
        t=s.tanh(m/2);u=s.tanh(d/2)
        center=m-4*t*(1-u**2)/(1-t**2*u**2)
        transverse=d+4*u*(1-t**2)/(1-t**2*u**2)
        cm=s.series(s.series(center,m,0,5).removeO(),d,0,4).removeO().expand()
        tr=s.series(s.series(transverse,m,0,4).removeO(),d,0,5).removeO().expand()
        assert s.expand(cm.coeff(m,3).subs(d,0)-s.Rational(1,6))==0
        assert s.expand(cm.coeff(m,1).coeff(d,2)-s.Rational(1,2))==0
        assert s.expand(tr.coeff(d,1).coeff(m,2)+s.Rational(1,2))==0
        assert s.expand(tr.coeff(d,3).subs(m,0)+s.Rational(1,6))==0
    except ImportError:
        pass
    print('PASS: exact-coordinate identities, Taylor coefficients, and bounded numerical escape-clock offsets')


if __name__=='__main__':
    check()
