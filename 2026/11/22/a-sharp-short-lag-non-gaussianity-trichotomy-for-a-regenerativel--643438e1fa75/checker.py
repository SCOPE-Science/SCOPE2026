#!/usr/bin/env python3
"""Independent finite numerical checks of a regenerative exponential-clock model.

Only finite quadrature and algebra are tested; asymptotic proofs are in RESULT.md.
No optional dependencies, network, or external data required.
"""
import math

COUNT = 0

def check(condition, note):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(f"check {COUNT}: {note}")


def simpson(f, left, right, panels=16000):
    assert panels % 2 == 0
    h = (right - left) / panels
    s = f(left) + f(right)
    for j in range(1, panels):
        s += (4 if j % 2 else 2) * f(left + j*h)
    return s*h/3


def h_second_moment(gamma, eta):
    """Quadrature of exact first-cycle tail formula; b=d=1."""
    a=gamma
    u0=-math.log1p(-eta)
    # Numerically stable evaluation of 2 int_0^u0 u exp(-a u) du.
    z=a*u0
    small= 2*u0*u0 * sum(((-z)**k)/(math.factorial(k)*(k+2)) for k in range(21))
    # u=u0 exp(z), integrate positive tail on logarithmic scale.
    uhi=max(100.0, 60.0/a)
    high=math.log(uhi/u0)
    power=1+gamma
    def f(x):
        u=u0*math.exp(x)
        return 2*u*u*math.exp(-a*u)*(eta/(-math.expm1(-u)))**power
    return small+simpson(f, 0, high)


def predicted_h2(gamma, eta):
    if gamma < 1:
        return 2*math.pi/(gamma*math.sin(math.pi*gamma))*eta**(1+gamma)
    if gamma == 1:
        return 2*eta*eta*math.log(1/eta)
    raise ValueError("Only the two divergent normalized regimes")


def run():
    # Stationary density normalization and moments of the instantaneous speed.
    for a in (0.3, 0.5, 1, 1.7, 3, 5):
        for b in (0.2, 0.8, 1.4):
            d=0.3+b
            z=(a+b)*simpson(lambda y: math.exp(-(a+b)*y),0,40/(a+b),2400)
            check(abs(z-1)<1e-5, 'stationary age density')
            mean=(a+b)/d * simpson(lambda y: math.exp(-a*y),0,40/a,2400)
            check(abs(mean-(a+b)/(a*d))<1e-5, 'stationary mean speed')
            if a>b:
                second=(a+b)/(d*d) * simpson(lambda y: math.exp(-(a-b)*y),0,80/(a-b),2400)
                expected=(a+b)/(d*d*(a-b))
                check(abs(second/expected-1)<2e-5, 'stationary second speed moment')

    # Exact survival formula for the first operational excursion and its second moment:
    # H2 is positive, monotone in eta; asymptotic constants are approached.
    for gamma in (0.25,0.5,0.75,1.0):
        vals=[h_second_moment(gamma,e) for e in (0.01,0.001,0.0001,0.00001)]
        check(all(0<vals[j+1]<vals[j] for j in range(3)),'H2 monotone in eta')
        ratios=[v/predicted_h2(gamma,e) for v,e in zip(vals,(.01,.001,.0001,.00001))]
        check(all(0<x<1.6 for x in ratios),'H2 normalized positive finite')
        if gamma<1:
            check(abs(ratios[-1]-1)<0.08,'subcritical sharp coefficient')
            check(abs(ratios[-1]-1)<abs(ratios[0]-1),'subcritical convergence')
        else:
            check(abs(ratios[-1]-1)<0.15,'critical logarithmic leading coefficient')
            check(abs(ratios[-1]-1)<abs(ratios[0]-1),'critical convergence')
    # Exact normalized leading critical coefficients and finite-phase geometry.
    for g in (0.05,0.1,0.25,0.5,0.75,0.9):
        coeff=6*math.pi*g / ((1+g)**2*math.sin(math.pi*g))
        check(coeff>0, 'positive cusp amplitude')
        # Reflection identity: gamma*B(gamma,1-gamma) equals gamma*pi/sin(pi*gamma).
        check(math.isclose(math.gamma(g)*math.gamma(1-g),math.pi/math.sin(math.pi*g),rel_tol=1e-13),'Euler reflection')
    for g in (1.1,1.25,1.5,2,3,5,10):
        v=(g+1)/g
        v2=(g+1)/(g-1)
        ratio=3*(v2/(v*v)-1)
        check(math.isclose(ratio,3/(g*g-1),rel_tol=1e-13),'finite-regime ratio')
    print(f"PASS {COUNT} finite algebraic and quadrature assertions")

if __name__=='__main__':
    run()
