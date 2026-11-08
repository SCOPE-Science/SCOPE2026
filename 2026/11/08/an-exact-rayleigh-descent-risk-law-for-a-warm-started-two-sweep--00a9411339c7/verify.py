"""Standalone exact-algebra and numerical checks for the stated first-two-sweep law."""
from fractions import Fraction as F
import math
import random


def exact_identity_checks():
    rng = random.Random(17191)
    for _ in range(8000):
        a = F(rng.randrange(2, 30), rng.randrange(1, 12))
        b = F(rng.randrange(1, 12), rng.randrange(1, 12))
        if a <= b:
            a, b = b, a
        if a == b:
            continue
        t = F(rng.randrange(-50, 51), rng.randrange(1, 15))
        lhs = a*a*(b*b+t)**2-b*b*(a*a+t)**2
        rhs = (a*a-b*b)*(t*t-a*a*b*b)
        assert lhs == rhs


def numerical_step(a, b, beta, theta):
    c, s = math.cos(theta), math.sin(theta)
    u = math.hypot(a*c, b*s)
    x1 = (a*c/u, b*s/u)
    y2 = (a*x1[0]+beta*c, b*x1[1]+beta*s)
    v = math.hypot(*y2)
    assert v > 0
    mu1 = a*x1[0]**2+b*x1[1]**2
    mu2 = (a*y2[0]**2+b*y2[1]**2)/v**2
    return mu1, mu2, beta*beta*u*u-a*a*b*b


def step_checks():
    rng = random.Random(7187)
    tested = 0
    for _ in range(40000):
        b = 0.1+6*rng.random()
        a = b*(1.01+8*rng.random())
        beta = a*(4*rng.random()-2)
        theta = 2*math.pi*rng.random()
        m1, m2, d = numerical_step(a,b,beta,theta)
        if abs(d) < 1e-8*a*a*b*b or abs(m2-m1)<1e-11*a:
            continue
        assert (m2<m1)==(d>0), (a,b,beta,theta,m1,m2,d)
        tested+=1
    assert tested>39000


def law(a,b,beta):
    q=abs(beta)
    if q<=b:return 0.
    if q>=a:return 1.
    v=b*b*(a*a/(q*q)-1)/(a*a-b*b)
    return 2/math.pi*math.acos(math.sqrt(v))


def probability_checks():
    for a,b in ((2,1),(7,2),(1.05,1),(13,0.05)):
        for beta in (0,b*0.999999,b,1.000001*b,(a+b)/2,0.999999*a,a,1.1*a,-(a+b)/2):
            prob=law(a,b,beta)
            n=20000
            true_count=0
            for k in range(n):
                theta=2*math.pi*(k+0.5)/n
                u2=a*a*math.cos(theta)**2+b*b*math.sin(theta)**2
                true_count += int(beta*beta*u2 > a*a*b*b)
            assert abs(true_count/n-prob)<0.00011,(a,b,beta,prob,true_count/n)
    assert abs(law(2,1,1.5)-(2/math.pi)*math.acos(math.sqrt(7/27)))<1e-14


def cusp_checks():
    a,b=2.,1.
    CL=2*math.sqrt(2)*a/(math.pi*math.sqrt(a*a-b*b))
    CR=2*math.sqrt(2)*b/(math.pi*math.sqrt(a*a-b*b))
    for eps in (1e-3,1e-4,1e-5):
        left=law(a,b,b*(1+eps))/math.sqrt(eps)
        right=(1-law(a,b,a*(1-eps)))/math.sqrt(eps)
        assert abs(left/CL-1)<0.005
        assert abs(right/CR-1)<0.005


if __name__=='__main__':
    exact_identity_checks()
    step_checks()
    probability_checks()
    cusp_checks()
    print('VERIFY_OK: 8000 exact identity trials, 40000 float steps, 36 angular laws, 3 cusp scales')
