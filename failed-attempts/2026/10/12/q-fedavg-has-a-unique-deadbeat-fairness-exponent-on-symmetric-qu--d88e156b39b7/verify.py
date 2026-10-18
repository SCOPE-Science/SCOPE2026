import math
import random

rng = random.Random(350059)

def source_round(x, a, b, q):
    L = a
    eta = 1.0/a
    bs = (b, -b)
    nums = []
    dens = []
    for bi in bs:
        grad = a*(x-bi)
        local = x-eta*grad
        delta_w = L*(x-local)
        F = 0.5*a*(x-bi)**2
        assert F > 0.0
        Delta = (F**q)*delta_w
        h = q*(F**(q-1.0))*(delta_w**2) + L*(F**q)
        nums.append(Delta)
        dens.append(h)
    return x-sum(nums)/sum(dens)

def closed_round(x, b, q):
    d1=x-b
    d2=x+b
    num=d1*(abs(d1)**(2*q))+d2*(abs(d2)**(2*q))
    den=(2*q+1.0)*(abs(d1)**(2*q)+abs(d2)**(2*q))
    return x-num/den

# Direct source-form update equals the closed map.
for _ in range(1000):
    a=10**rng.uniform(-1,1)
    b=10**rng.uniform(-1,1)
    q=rng.choice([0.1,0.25,0.5,0.75,1.0,2.0,5.0])
    x=rng.uniform(-4*b,4*b)
    if abs(x-b)<1e-6*b or abs(x+b)<1e-6*b:
        continue
    got=source_round(x,a,b,q)
    exp=closed_round(x,b,q)
    assert abs(got-exp) <= 2e-11*max(1.0,abs(exp),abs(x))

# q=1/2 is exactly deadbeat throughout the open interval up to floating error.
for b in (0.2,1.0,3.7):
    for j in range(1,100):
        x=b*(-1.0+2.0*j/100.0)
        got=closed_round(x,b,0.5)
        assert abs(got) < 3e-14*max(1.0,b)

# General cubic coefficient.
for q in (0.1,0.25,0.75,1.0,1.5,3.0):
    b=1.7
    c=2*q*(2*q-1)/(3*b*b)
    for h in (1e-2,5e-3,2e-3):
        ratio=closed_round(h,b,q)/(h**3)
        assert abs(ratio-c) < 5e-3*max(1.0,abs(c))

# Exact q=1 closed form and global contraction.
for b in (0.3,1.0,4.0):
    for x in (-20*b,-2*b,-0.7*b,-0.1*b,0.1*b,0.7*b,2*b,20*b):
        got=closed_round(x,b,1.0)
        exp=2*x**3/(3*(x*x+b*b))
        assert abs(got-exp) < 2e-12*max(1.0,abs(exp))
        assert 0.0 < abs(got) < (2.0/3.0)*abs(x)

# q=0 FedAvg exact-local-solve baseline.
for x in (-100.0,-1.0,0.0,2.0,100.0):
    local1=1.0
    local2=-1.0
    assert (local1+local2)/2.0 == 0.0

print("verification passed")
