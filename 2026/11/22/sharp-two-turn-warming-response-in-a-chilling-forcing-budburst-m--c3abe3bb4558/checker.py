"""Supplementary numerical checks for the chilling–forcing phase theorem.

Run: python3 checker.py. Uses only Python's standard library. The theorem
is proved analytically; these finite checks test formulas and example values.
"""
import math
import random

COUNT = 0


def check(condition, message="diagnostic assertion failed"):
    global COUNT
    assert condition, message
    COUNT += 1


def threshold(h):
    y = (1.0 + math.sqrt(1.0 + 8.0*h)) / 2.0
    xc = math.sqrt(1.0 + 1.0/y)
    bc = y * math.exp((1.0 + 1.0/y)/2.0)
    gamma = y * math.sqrt(2.0 / (bc*(y+1.0)*(2.0*y-1.0)))
    return y, xc, bc, gamma


def response(x, b, h):
    v = b*math.exp(-x*x/2.0)
    return x*v/math.sqrt(2.0*(h+v))


def peak_equation(x,b,h):
    v = b*math.exp(-x*x/2.0)
    s = v/(h+v)
    return 1.0-x*x*(1.0-s/2.0)


def bisect(f, lo, hi):
    flo, fhi = f(lo), f(hi)
    check(flo*fhi <= 0.0)
    for _ in range(75):
        mid = (lo+hi)/2.0
        if f(mid)*flo > 0.0:
            lo,flo=mid,f(mid)
        else:
            hi=mid
    return (lo+hi)/2.0


def peak_x(b,h):
    return bisect(lambda x: peak_equation(x,b,h),1.0e-8,12.0)


def roots(b,h):
    p=peak_x(b,h)
    if response(p,b,h)<=1.0:
        return []
    return [bisect(lambda x: response(x,b,h)-1.0,0.0,p),
            bisect(lambda x: response(x,b,h)-1.0,p,12.0)]


def date(w,b,h,c=5.0,t0=10.0):
    x=max(c-w,0.0)
    return t0-w+math.sqrt(2.0*(h+b*math.exp(-x*x/2.0)))


def deriv(w,b,h,c=5.0):
    x=max(c-w,0.0)
    return -1.0+response(x,b,h)


for h in [0.001,0.02,0.2,1.0,2.0,10.0,100.0]:
    y,xc,bc,gamma=threshold(h)
    check(abs(y*y-y-2.0*h)<1.e-11*max(1,h))
    check(abs(response(xc,bc,h)-1)<1.e-12)
    check(abs(peak_equation(xc,bc,h))<1.e-12)
    check(len(roots(0.8*bc,h))==0)
    for fac in [1.05,1.2,2.0,5.0]:
        b=bc*fac
        r=roots(b,h)
        check(len(r)==2)
        check(0<r[0]<peak_x(b,h)<r[1])
        check(abs(response(r[0],b,h)-1)<2.e-12)
        check(abs(response(r[1],b,h)-1)<2.e-12)
        check(response((r[0]+r[1])/2,b,h)>1)
        check(response(r[0]/2,b,h)<1)
        check(response(2*r[1],b,h)<1)
        for d in [0.002,0.2,2.0]:
            w=5-d
            delta=1.e-6
            numerical=(date(w+delta,b,h)-date(w-delta,b,h))/(2*delta)
            check(abs(numerical-deriv(w,b,h))<1.e-6)
    for eps in [1.e-3,1.e-4]:
        r=roots(bc+eps,h)
        est=(r[1]-r[0])/(2*math.sqrt(eps))
        check(abs(est-gamma)<2.e-4)

r=roots(8.0,1.0)
check(abs(r[0]-0.5833401275872763)<2.e-10)
check(abs(r[1]-2.0578273421228315)<2.e-10)

rng=random.Random(172930)
for _ in range(1800):
    h=10**rng.uniform(-2,2)
    bc=threshold(h)[2]
    b=bc*rng.uniform(1.01,8.0)
    r=roots(b,h)
    check(len(r)==2)
    x=rng.uniform(0.0,8.0)
    correct=(r[0]<x<r[1])
    predicted=(response(x,b,h)>1.0)
    check(correct==predicted)
    w=rng.uniform(-2.0,4.9)
    delta=1.e-5
    numerical=(date(w+delta,b,h)-date(w-delta,b,h))/(2*delta)
    check(abs(numerical-deriv(w,b,h))<2.e-6)

print(f"PASS: {COUNT} supplementary numerical assertions")
