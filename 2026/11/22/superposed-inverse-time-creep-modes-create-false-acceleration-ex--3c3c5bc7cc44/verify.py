"""Independent numerical checks for the two-clock inverse-velocity mixture identities.

Run with Python 3.9 or newer: python verify.py
Finite checks supplement, and do not replace, the analytic proofs.
"""
import math
import random


def v_and_derivatives(t, a, b, delta):
    x = -t
    y = x + delta
    return (a/x+b/y, a/x**2+b/y**2, 2*a/x**3+2*b/y**3)


def bias_formula(a, b, delta, x1, x2):
    return b*delta*x1*x2/(a*delta**2+a*delta*(x1+x2)+(a+b)*x1*x2)


def alpha_formula(a, b, z):
    return 2+2*a*b*z*(1-z)**2/(a+b*z*z)**2


def hump_root(a, b):
    lo, hi = 0.0, 1.0/3.0
    for _ in range(95):
        z=(lo+hi)/2
        h=a*(1-3*z)-b*z*z*(3-z)
        if h>0:
            lo=z
        else:
            hi=z
    return (lo+hi)/2


def close(x, y, rtol=2e-9, atol=2e-12):
    if not math.isclose(x, y, rel_tol=rtol, abs_tol=atol):
        raise AssertionError(f'mismatch: {x} vs {y}')


def main():
    rng=random.Random(19850915)
    checks=0
    for _ in range(1800):
        a=math.exp(rng.uniform(-2,2))
        b=math.exp(rng.uniform(-2,2))
        d=math.exp(rng.uniform(-2,2))
        x2=d*math.exp(rng.uniform(-1,1))
        x1=x2*(1+rng.uniform(.08,3))
        v1=v_and_derivatives(-x1,a,b,d)[0]
        v2=v_and_derivatives(-x2,a,b,d)[0]
        R1,R2=1/v1,1/v2
        slope=(R2-R1)/(x1-x2) # derivative dR/dt <0
        that=-x2-R2/slope
        bias=bias_formula(a,b,d,x1,x2)
        close(that,bias,rtol=1e-9)
        checks+=1
        if not (0<bias<b*d/(a+b)):
            raise AssertionError('failed sharp bias bound')
        checks+=1
        x3=x2/2
        if not bias_formula(a,b,d,x1,x3)<bias:
            raise AssertionError('late-sample monotonicity')
        checks+=1
        v,vp,vpp=v_and_derivatives(-x2,a,b,d)
        z=x2/(x2+d)
        close(v*vpp/vp**2,alpha_formula(a,b,z))
        checks+=1
        if not v*vpp/vp**2>2:
            raise AssertionError('nontrivial two-clock exponent excess')
        checks+=1
        zm=hump_root(a,b)
        if not (0<zm<1/3):
            raise AssertionError('peak interval')
        checks+=1
        h=lambda u:a*(1-3*u)-b*u*u*(3-u)
        if h(zm/2)<=0 or h((zm+1)/2)>=0:
            raise AssertionError('unique derivative sign profile')
        checks+=1
        pk=alpha_formula(a,b,zm)
        if not (pk>alpha_formula(a,b,max(1e-15,zm*.5)) and pk>alpha_formula(a,b,(zm+1)/2)):
            raise AssertionError('strict maximum')
        checks+=1
    close(hump_root(1,1),2-math.sqrt(3),rtol=1e-12)
    checks+=1
    close(alpha_formula(1,1,hump_root(1,1)),2.25,rtol=1e-12)
    checks+=1
    close(bias_formula(1,1,2,2,1),2/7)
    checks+=1
    for n in [3,4,6,9]:
        for _ in range(100):
            weights=[math.exp(rng.uniform(-2,2)) for _ in range(n)]
            clocks=[math.exp(rng.uniform(-2,2)) for _ in range(n)]
            t=-1
            s=[sum(w/(T-t)**k for T,w in zip(clocks,weights)) for k in (1,2,3)]
            gap=s[0]*s[2]-s[1]**2
            if not gap>0:
                raise AssertionError('strict Cauchy-Schwarz gap')
            checks+=1
    for r in [1e5,1e6,1e7]:
        z=hump_root(1,r)
        close(z*math.sqrt(r),1/math.sqrt(3),rtol=.01)
        checks+=1
        close((alpha_formula(1,r,z)-2)/math.sqrt(r),9/(8*math.sqrt(3)),rtol=.02)
        checks+=1
    print(f'PASS: {checks} deterministic numerical checks; universal results require the written proofs')


if __name__=='__main__':
    main()
