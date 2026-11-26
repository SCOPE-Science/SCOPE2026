import math
import random

rng = random.Random(350071)

def closed_ratio(kappa, t):
    return 1.0 + (kappa*kappa - 1.0)/(kappa**(2*t-1) + 1.0)

def direct_residual_ratio(kappa, z1, z2, t):
    q1 = (kappa**(2*t-2))*z1
    q2 = z2
    p1 = kappa*q1
    p2 = q2
    n = math.hypot(p1,p2)
    p1 /= n
    p2 /= n
    return (kappa*kappa + 1.0) - (kappa*kappa*p1*p1 + p2*p2)

def pointwise_formula(kappa, z1, z2, t):
    num = kappa*kappa * (kappa**(4*t-4)*z1*z1 + z2*z2)
    den = kappa**(4*t-2)*z1*z1 + z2*z2
    return num/den

def adaptive_simpson(f, a, b, eps=1e-11, maxdepth=30):
    fa, fb = f(a), f(b)
    c = (a+b)/2.0
    fc = f(c)
    S = (b-a)*(fa+4.0*fc+fb)/6.0

    def rec(a,b,fa,fb,fc,S,eps,depth):
        c=(a+b)/2.0
        l=(a+c)/2.0
        r=(c+b)/2.0
        fl,fr=f(l),f(r)
        Sl=(c-a)*(fa+4.0*fl+fc)/6.0
        Sr=(b-c)*(fc+4.0*fr+fb)/6.0
        total=Sl+Sr
        if depth <= 0 or abs(total-S) <= 15.0*eps:
            return total+(total-S)/15.0
        return (
            rec(a,c,fa,fc,fl,Sl,eps/2.0,depth-1)
            + rec(c,b,fc,fb,fr,Sr,eps/2.0,depth-1)
        )
    return rec(a,b,fa,fb,fc,S,eps,maxdepth)

for kappa in (1.0,1.2,2.0,5.0,10.0):
    for t in (1,2,3,4):
        for _ in range(200):
            z1=rng.gauss(0.0,1.0)
            z2=rng.gauss(0.0,1.0)
            if z1*z1+z2*z2 < 1e-20:
                continue
            d=direct_residual_ratio(kappa,z1,z2,t)
            p=pointwise_formula(kappa,z1,z2,t)
            assert abs(d-p) < 2e-10*max(1.0,abs(d),abs(p))

# Adaptive angular integration checks the isotropic Gaussian-direction expectation.
for kappa in (1.0,1.2,2.0,5.0,10.0):
    for t in (1,2,3):
        f=lambda th: pointwise_formula(kappa,math.cos(th),math.sin(th),t)
        avg=(2.0/math.pi)*adaptive_simpson(f,0.0,math.pi/2.0)
        target=closed_ratio(kappa,t)
        assert abs(avg-target) < 2e-8*max(1.0,target)

for kappa in (1.0,1.2,2.0,5.0,10.0,100.0):
    assert abs(closed_ratio(kappa,1)-kappa) < 1e-12*max(1.0,kappa)
    r2=closed_ratio(kappa,2)
    target=kappa*kappa/(kappa*kappa-kappa+1.0)
    assert abs(r2-target) < 2e-12*max(1.0,target)

print("verification passed")
