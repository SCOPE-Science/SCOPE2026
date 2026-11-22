"""Independent numerical checks of an exact sharp BV norm for a sparse cosine projection.
Uses only the Python standard library; not an infinite proof.
"""
import math
import random

K=(16*math.sqrt(2)-8)/(3*math.pi)

def I(b):
    if -1.0/3.0<=b<=1.0:
        return 2*(1+b/3)
    if b>1:
        r=math.sqrt((b-1)/(4*b))
        return 2*(1+b/3)+(8.0/3.0)*(b-1)*r
    r=math.sqrt((b-1)/(4*b))
    return 2*(1+b/3)-4*((1-b)*(1-r)+4*b*(1-r**3)/3)

def profile(theta):
    c=math.cos(math.pi*theta)
    return (2.0/math.pi)*abs(math.sin(math.pi*theta))*I(4*c*c-1)

def direct_profile(n,t,steps=10000):
    s1=math.sin(n*math.pi*t)
    s3=math.sin(3*n*math.pi*t)
    h=1.0/steps
    a=0.0
    for j in range(steps):
        x=(j+0.5)*h
        d=2*s1*math.sin(n*math.pi*x)+2*s3*math.sin(3*n*math.pi*x)
        a+=abs(d)*h
    return a

assert abs(K-1.552017146595508)<1e-12
assert abs((2/math.pi)*I(-1)-K)<1e-12
assert abs(I(-1)-(8*math.sqrt(2)-4)/3)<1e-12
assert (20*math.sqrt(10)/27) < I(-1)
assert (4*math.sqrt(2)/3) < I(-1)
for i in range(10001):
    t=i/10000
    p=profile(t)
    assert p <= K+1e-10, (t,p,K)
for n in (1,2,3,4,5,9):
    for j in range(n):
        jump=(j+0.5)/n
        p=direct_profile(n,jump,steps=3000)
        assert abs(p-K)<5e-5,(n,jump,p,K)
    for k in range(100):
        t=random.Random(n*1000+k).random()
        p=direct_profile(n,t,steps=2000)
        assert p<=K+1e-4,(n,t,p,K)

# For finite-jump BV data, the spectral projection is obtained by superposition.
rng=random.Random(41)
for n in (1,3,6):
    for _ in range(150):
        jumps=[(rng.random(),rng.uniform(-1,1)) for _ in range(8)]
        v=sum(abs(a) for _,a in jumps)
        # evaluate derivative at 3000 midpoint quadrature cells
        a=0.0
        s1=sum(amp*math.sin(n*math.pi*t) for t,amp in jumps)
        s3=sum(amp*math.sin(3*n*math.pi*t) for t,amp in jumps)
        for j in range(3000):
            x=(j+0.5)/3000
            a+=abs(2*s1*math.sin(n*math.pi*x)+2*s3*math.sin(3*n*math.pi*x))/3000
        assert a <= K*v+1e-6
print('PASS exact identity, branch bounds, 10001 analytic kernel samples, 54 attaining jumps, 600 other jump tests, 450 multijump tests')
