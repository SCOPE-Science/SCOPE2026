"""Deterministic reproducibility checks for a nonlinear planar first-zero bound.

Numerical integration illustrates the theorem; it does not certify the all-state
or all-time assertion. The proof in RESULT.md supplies that argument.
"""
from math import exp, pi, sin, cos, sqrt, isclose


def logistic(z):
    if z >= 0:
        return 1.0 / (1.0 + exp(-z))
    e = exp(z)
    return e / (1.0 + e)


def field(x, y):
    return 1.0 - logistic(y - 5.0) - 0.1*x, logistic(x - 5.0) - 0.1*y


def rk4(state, step):
    x,y=state
    a,b=field(x,y)
    c,d=field(x+step*a/2,y+step*b/2)
    e,f=field(x+step*c/2,y+step*d/2)
    g,h=field(x+step*e,y+step*f)
    return (x+step*(a+2*c+2*e+g)/6,y+step*(b+2*d+2*f+h)/6)


def advance(state,T,steps=12000):
    h=T/steps
    for _ in range(steps):
        state=rk4(state,h)
    return state


def sigmoid_case(eps,T):
    plus=advance((5.0,5.0+eps),T)[0]
    minus=advance((5.0,5.0-eps),T)[0]
    return plus-minus


def saturator(z,d=.1,e=.1):
    v=abs(z)
    if v <= d: return z
    return (1 if z>0 else -1)*(d+e*(1-exp(-(v-d)/e)))


def plateau_field(x,y):
    return 0.5-saturator(y-5.0)-.1*x, 0.5+saturator(x-5.0)-.1*y


def main():
    # The logistic slopes are bounded by 1/4; the first return lower bound is 4 pi.
    critical=4*pi
    for eps in [0.2,0.05,0.01,0.002]:
        for frac in [.1,.4,.8,.98]:
            z=sigmoid_case(eps,frac*critical)
            assert z < 0, (eps,frac,z)
        a=sigmoid_case(eps,critical-0.25)
        b=sigmoid_case(eps,critical+0.25)
        assert a < 0 and b > 0,(eps,a,b)
        lo,hi=critical-.25,critical+.25
        for _ in range(18):
            mid=(lo+hi)/2
            if sigmoid_case(eps,mid)<0:lo=mid
            else:hi=mid
        print(f'logistic eps={eps:.3f} first sampled equality near {(lo+hi)/2:.8f}; lower bound {critical:.8f}')
    # Positive C1 saturator has exactly unit central slopes, with an affine
    # invariant ball of radius <0.1 about (5,5).
    for z in [-20,-3,-.3,-.05,0,.05,.3,3,20]:
        assert 0<.5-saturator(z)<1 and 0<.5+saturator(z)<1
    for v0 in [-.05,-.02,.02,.05]:
        for n in range(1,11):
            t=n*pi
            u=-v0*exp(-.1*t)*sin(t)
            v=v0*exp(-.1*t)*cos(t)
            assert abs(u)<.1 and abs(v)<.1
            assert abs(u)<3e-15
        # The linear field on the central strip coincides with the constructed
        # nonlinear field throughout the exact orbit.
        for t in [i*pi/32 for i in range(129)]:
            u=-v0*exp(-.1*t)*sin(t)
            v=v0*exp(-.1*t)*cos(t)
            dx,dy=plateau_field(5+u,5+v)
            expected_u=-.1*u-v
            expected_v=u-.1*v
            assert abs(dx-expected_u)<1e-12 and abs(dy-expected_v)<1e-12
    print('Exact plateau identities verified for 4 amplitudes; all grid observations at k*pi have x1=5.')
    print('PASS: numerical sigmoid stress tests and exact plateau identity checks.')


if __name__=='__main__':main()
