#!/usr/bin/env python3
"""Reproducible supplementary checks for equal-mean passage with killing."""
import math

def prob_e(x, a):
    return -math.expm1(-(1+a)*x)/(1+a)

def prob_r(x, a):
    z=(2+a)*x
    return 4/((2+a)**2)*(-math.expm1(-z)-z*math.exp(-z))

def difference(x, a):
    return prob_r(x,a)-prob_e(x,a)

def h(x,a):
    return math.exp(-(2+a)*x)*(4*x-math.exp(x))

def bisect(f, lo, hi, n=85):
    fl=f(lo)
    fh=f(hi)
    assert fl*fh<0, (lo,hi,fl,fh)
    for _ in range(n):
        mid=(lo+hi)/2
        if mid==lo or mid==hi: break
        fm=f(mid)
        if fm==0: return mid
        if fm*fl>0:lo,fl=mid,fm
        else:hi,fh=mid,fm
    return (lo+hi)/2

def simpson(f,lo,hi,n=600):
    step=(hi-lo)/n
    return step/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*step) for i in range(1,n)))

def run():
    xlo=bisect(lambda x:4*x-math.exp(x),0.01,1.0)
    xhi=bisect(lambda x:4*x-math.exp(x),1.0,3.0)
    ac=bisect(lambda a:difference(xhi,a),0,1)
    assert abs(xlo-0.357402956181389)<3e-12
    assert abs(xhi-2.153292364110349)<3e-12
    assert abs(ac-0.316461352642136)<3e-11
    count=3
    for a in [0,0.01,0.1,0.2,0.3,ac+0.1,1,3]:
        for i in range(1,251):
            x=i*0.02
            # Independent numerical integral of the *difference*.
            integral=simpson(lambda t:4*t*math.exp(-(2+a)*t)-math.exp(-(1+a)*t),0,x,800)
            assert abs(integral-difference(x,a)) < 1e-8
            count+=1
            # Derivative of the difference from the two densities.
            assert abs((4*x*math.exp(-(2+a)*x)-math.exp(-(1+a)*x))-h(x,a)) < 2e-14
            count+=1
    for a in [0.002,0.01,0.05,0.1,0.2,0.3,ac-0.001]:
        left=bisect(lambda x:difference(x,a),xlo,xhi)
        right=bisect(lambda x:difference(x,a),xhi,40)
        assert xlo<left<xhi<right and difference((left+right)/2,a)>0
        count+=1
        assert difference(left/2,a)<0 and difference(right+2,a)<0
        count+=1
    for a in [ac+0.001,0.5,1,5]:
        for i in range(1,451):
            assert difference(0.01*i,a)<0
            count+=1
    for a in [0.001,0.01,0.1,0.2,0.3,1,3]:
        asymptotic=-a*a/((1+a)*(2+a)**2)
        assert abs(difference(80,a)-asymptotic)<1e-14
        count+=1
    print('PASS',count,'supplementary assertions')
    print('stationary locations:',round(xlo,12),round(xhi,12))
    print('critical mortality-to-passage ratio:',format(ac,'.14f'))

if __name__=='__main__':run()
