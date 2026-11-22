#!/usr/bin/env python3
"""Independent numerical checks of the stated rectangle identities; not an infinite proof."""
import math

def profile(t):
    s=math.hypot(1,t)
    A=math.asinh(1/t); B=math.asinh(t)
    I=2*(1+t**3)+(2/3)*s*(-t*t+4*t-1)+(2/3)*((2+3*t)*B+t*t*(2*t+3)*A)
    return I/(8*(1+t)**3)

def F(t):
    s=math.hypot(1,t)
    return t*(t+2)*math.asinh(1/t)-(2*t+1)*math.asinh(t)-3*(1-t)*(1+t-s)

def H(z):
    return (z*z+2*z+3)/math.hypot(z,1)-3-math.asinh(z)

def side_integral(t,n=160):
    # Independent four-side midpoint quadrature, including both ordered endpoints.
    side=[(((i+0.5)/n,0),1/n) for i in range(n)]
    side += [((1,t*(i+0.5)/n),t/n) for i in range(n)]
    side += [((1-(i+0.5)/n,t),1/n) for i in range(n)]
    side += [((0,t*(1-(i+0.5)/n)),t/n) for i in range(n)]
    total=0.
    for (x,y),w in side:
        for (u,v),h in side:
            total+=w*h*math.hypot(x-u,y-v)
    return total/(8*(1+t)**3)

def run():
    ts=(0.03,0.1,0.25,0.5,0.8,1.0)
    for t in ts:
        assert abs(profile(t)-side_integral(t))<1.5e-5,(t,profile(t),side_integral(t))
    for t in (0.01,0.05,0.16,0.3,0.6,0.88):
        h=1e-5
        D=(profile(t+h)-profile(t-h))/(2*h)
        assert abs(D-F(t)/(4*(1+t)**4))<3e-8,(t,D,F(t)/(4*(1+t)**4))
        assert F(t)>0 and H(1/t)>0
    for z in (1.,1.3,2.,3.,10.):
        h=1e-5
        D=(H(z+h)-H(z-h))/(2*h)
        theory=(z-1)**2*(z+1)/(z*z+1)**1.5
        assert abs(D-theory)<1e-8,(z,D,theory)
    rsquare=1/16+math.sqrt(2)/48+5*math.log1p(math.sqrt(2))/48
    assert abs(profile(1)-rsquare)<1e-14
    for t in (1e-3,1e-4):
        scaled=(profile(t)-1/6)/(t*t)
        asym=math.log(2/t)/4-3/8
        assert abs(scaled-asym)<0.03,(t,scaled,asym)
    c=(3*math.sqrt(2)-3-math.asinh(1))/64
    for t in (0.99,0.999):
        scaled=(rsquare-profile(t))/(1-t)**2
        assert abs(scaled-c)<0.0002,(t,scaled,c)
    print('PASS: 6 independent boundary integrals, derivatives, H-factorization, both sharp endpoint checks')
if __name__=='__main__':run()
