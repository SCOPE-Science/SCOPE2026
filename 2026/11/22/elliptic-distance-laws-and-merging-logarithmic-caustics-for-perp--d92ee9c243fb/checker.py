"""Self-contained numerical diagnostics for perpendicular-circle cross distances.
Requires Python 3 standard library only. Quadrature confirms, but does not replace proof.
"""
import math
import random
PI=math.pi

def elliptic_k(m):
    assert 0.0 <= m < 1.0
    a,b=1.0,math.sqrt(1.0-m)
    for _ in range(100):
        na=(a+b)/2
        nb=math.sqrt(a*b)
        a,b=na,nb
        if abs(a-b)<1e-15*a:break
    return PI/(2*a)

def density(d,z):
    A=1+d*d-z*z
    if A<=0:return 0.
    if abs(z)<d:return 2/(PI*PI*math.sqrt(A))*elliptic_k(1/A)
    if abs(z)>d:return 2/(PI*PI)*elliptic_k(A)
    return float('inf')

def conditional_quadrature(d,z,N=20000):
    # Numerically integrate the conditional arcsine density without using elliptic K.
    if abs(z)<d:
        endpoint=PI/2
    else:
        endpoint=math.acos(math.sqrt(z*z-d*d))
    # tame endpoint sqrt singularity for |z|>d via s=endpoint*(1-v*v)
    n=N
    h=1.0/n
    t=0.
    for j in range(n):
        v=(j+.5)*h
        s=endpoint*(1-v*v)
        R2=d*d+math.cos(s)**2
        if R2<=z*z:continue
        t+=2*endpoint*v/math.sqrt(R2-z*z)
    return 2/(PI*PI)*h*t

def run():
    checks=0
    for d,zs in [(0.0,[.1,.25,.6,.85]),(.2,[0,.1,.12,.25,.6]),(.9,[0,.2,.4,1.02])]:
        for z in zs:
            x=density(d,z)
            y=conditional_quadrature(d,z)
            assert abs(x-y) < 2.0e-4, (d,z,x,y)
            checks+=1
        M=math.sqrt(1+d*d)
        assert abs(density(d,M-1e-10)-1/PI)<1e-4
        checks+=1
    for d in [.2,.6,1.,2.]:
        # Two symmetric logarithmic caustics have the sharp slope 1/pi^2.
        for z0 in [-d,d]:
            for delta in [1e-4,1e-5,1e-6]:
                x=density(d,z0+delta)
                expected=math.log(8/(d*delta))/PI**2
                assert abs(x-expected)<.004, (d,z0,delta,x,expected)
                checks+=1
    for d in [.03,.01,.003]:
        for lam in [0.,.5,1.6,-.8]:
            observed=density(d,d*lam)
            expected=(2*math.log(1/d)+math.log(16)-math.log(abs(1-lam*lam)))/PI**2
            assert abs(observed-expected)<.001, (d,lam,observed,expected)
            checks+=1
    for z in [.04,.1,.3]:
        observed=density(0,z)
        expected=(2/PI**2)*math.log(4/z)
        assert abs(observed-expected)<.03
        checks+=1
    rng=random.Random(207164)
    for d in [0.,.3,1.1]:
        n=30000
        ss=0.
        ss2=0.
        for i in range(n):
            t=rng.random()*2*PI
            s=rng.random()*2*PI
            dist2=(math.cos(t)-d)**2+(math.sin(t)-math.cos(s))**2+math.sin(s)**2
            ss+=dist2
            ss2+=dist2**2
        assert abs(ss/n-(2+d*d))<.025
        assert abs(ss2/n-((2+d*d)**2+2*d*d+1))<.13
        checks+=2
    print('PASS:',checks,'deterministic density, asymptotic, and sampled-moment diagnostics')
if __name__=='__main__': run()
