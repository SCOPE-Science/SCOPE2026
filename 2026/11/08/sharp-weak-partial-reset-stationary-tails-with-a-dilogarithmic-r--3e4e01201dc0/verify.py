"""Numerical diagnostics for weak-partial-reset stationary rare-event tails.

Requires Python 3.10+ standard library only. Mathematical infinity claims
are established in RESULT.md, not by finite computations.
"""
from math import exp, log, log1p, pi, sqrt, sin, isfinite


def li2(z):
    """Real dilogarithm on [0,1], via convergent series and reflection."""
    assert 0 <= z <= 1
    if z == 1:
        return pi*pi/6
    if z > 0.5:
        return pi*pi/6 - log(z)*log1p(-z) - li2(1-z)
    tot = 0.0
    p = z
    for k in range(1, 150):
        new = p/(k*k)
        tot += new
        if abs(new) < 1.e-16:
            break
        p *= z
    return tot


def exponent(theta, ell=1.0):
    assert abs(theta*ell) < 1
    return 0.5*li2((theta*ell)**2)


def d_exponent(theta, ell=1.0):
    if theta == 0:
        return 0.0
    return -log1p(-(theta*ell)**2)/theta


def dd_exponent(theta, ell=1.0):
    if theta == 0:
        return ell*ell
    z = (theta*ell)**2
    return 2*ell*ell/(1-z) + log1p(-z)/(theta*theta)


def optimum(y, ell=1.0):
    if y == 0:
        return 0.0
    lo, hi = 0., (1-1.e-14)/ell
    for _ in range(120):
        mid = (lo+hi)/2
        if d_exponent(mid, ell) < abs(y):
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2 * (1 if y > 0 else -1)


def rate(y, ell=1.0):
    theta = optimum(y, ell)
    return theta*y - exponent(theta, ell)


def cgf(eps, theta, ell=1.0, derivative=0):
    assert eps > 0 and abs(theta*ell)<1
    tot = 0.0
    for j in range(int(24/eps)+1):
        z = ell*ell*exp(-2*eps*j)
        den = 1-z*theta*theta
        if derivative == 0:
            tot -= log(den)
        elif derivative == 1:
            tot += 2*z*theta/den
        elif derivative == 2:
            tot += 2*z*(1+z*theta*theta)/(den*den)
        else:
            raise ValueError('derivative must be 0,1,2')
    return tot


def asymptotic_tail(y, eps, ell=1.0):
    assert y > 0
    theta = optimum(y, ell)
    return (sqrt(eps) * exp(-rate(y,ell)/eps) /
            (theta * sqrt(2*pi*dd_exponent(theta,ell)) *
             sqrt(1-(ell*theta)**2)))


def fourier_tail(y, eps, ell=1.0, delta=.006, tmax=12):
    """Finite Fourier inversion of the exact stationary product. Avoids simulation."""
    assert y > 0
    vals = [ell*ell*exp(-2*eps*j) for j in range(int(16/eps)+1)]
    s = y/eps
    n = int(tmax/delta)
    n += n%2
    h=tmax/n
    total=0.
    for i in range(n+1):
        t=i*h
        if t == 0:
            f=s
        else:
            t2=t*t
            product=1.
            for z in vals:
                product /= (1+t2*z)
                if product < 1e-80:
                    break
            f=sin(s*t)/t*product
        total += (1 if i in (0,n) else (4 if i%2 else 2))*f
    return 0.5 - h*total/(3*pi)


def run():
    checks=0
    def check(cond,label):
        nonlocal checks
        if not cond:
            raise AssertionError(label)
        checks+=1

    for ell in (0.6,1,2.3):
        for theta_frac in (0.0,0.15,0.3,0.6,0.85):
            theta=theta_frac/ell
            check(dd_exponent(theta,ell)>0, 'strict convexity')
            for eps in (.2,.1,.05,.025):
                # For monotone f, Euler-Maclaurin first boundary correction.
                k=cgf(eps,theta,ell)
                approx=(exponent(theta,ell)/eps -
                        0.5*log1p(-(theta*ell)**2))
                check(abs(k-approx) < 1.5*eps*ell*ell*theta*theta/(1-theta*theta*ell*ell)+1e-9,
                      'Euler-Maclaurin envelope')
                check(abs(eps*cgf(eps,theta,ell,1)-d_exponent(theta,ell)) < eps*ell*4/(1-(theta*ell)**2),
                      'first derivative limit')
                check(abs(eps*cgf(eps,theta,ell,2)-dd_exponent(theta,ell)) < eps*ell*ell*15/(1-(theta*ell)**2)**2,
                      'second derivative limit')

    for ell in (.6,1.,2.3):
        prev=0.
        for y in (.01*ell,.1*ell,.4*ell,.8*ell,1.5*ell,3*ell,8*ell):
            theta=optimum(y,ell)
            check(abs(d_exponent(theta,ell)-y)<1e-9,'optimizer')
            check(rate(y,ell)>prev,'rate increasing')
            prev=rate(y,ell)
            check(abs(rate(-y,ell)-rate(y,ell))<1e-12,'even rate')
            check(isfinite(asymptotic_tail(y,.05,ell)),'positive finite prefactor')
    check(abs(rate(.03) - (.03**2/2-.03**4/8)) < 5e-10,'Gaussian jet')
    check(abs(rate(15)-(15-pi*pi/12))<1e-6,'Laplace far rate')

    # Exact Fourier inversions are an independent implementation of the
    # stationary characteristic function; errors shrink with epsilon.
    for y in (.7,1.0):
        ratios=[]
        for eps in (.2,.1,.05):
            exact=fourier_tail(y,eps)
            appr=asymptotic_tail(y,eps)
            check(exact>0 and appr>0,'tail positivity')
            ratios.append(exact/appr)
        check(ratios[0]<ratios[1]<ratios[2]<1.,'relative prefactor convergence')
        print('x=',y,'ratios',*[round(z,6) for z in ratios])
    print('PASS:',checks,'deterministic diagnostic assertions')

if __name__=='__main__':
    run()
