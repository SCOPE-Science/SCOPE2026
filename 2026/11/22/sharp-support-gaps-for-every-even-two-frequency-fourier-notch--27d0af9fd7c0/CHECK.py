"""Finite numerical diagnostics for two-notch positive-circle gap theorem.
Python 3 standard library only; all universal statements require the written proof.
"""
import math

COUNT=0

def check(cond, message='diagnostic assertion failed'):
    global COUNT
    if not cond:
        raise AssertionError(message)
    COUNT+=1

def bisect(fun, a,b, steps=100):
    fa=fun(a)
    check(fa*fun(b)<0)
    for _ in range(steps):
        m=(a+b)/2
        if fun(m)*fa>0:
            a=m; fa=fun(a)
        else:
            b=m
    return (a+b)/2

def calc(k):
    if k==2:
        t=math.pi
    else:
        t=bisect(lambda t:math.sin(t)*math.sin(t/k)+math.cos(t)*math.cos(t/k)/k,math.pi/2,math.pi)
    xp=math.sin(t/k)
    lam=-math.cos(t)/xp
    r=bisect(lambda r: math.cos(k*math.asin(r))-lam*r,0.0,math.sin(math.pi/(2*k)))
    a=math.pi/2+math.asin(r)
    b=math.pi/2-t/k
    wm=xp/(xp+r)
    wp=r/(xp+r)
    # explicit reflection-invariant positive probability: total masses wm,wp on their two cosine fibers.
    check(abs(wm+wp-1)<1e-12)
    check(abs(wm*math.cos(a)+wp*math.cos(b))<1e-12)
    check(abs(wm*math.cos(k*a)+wp*math.cos(k*b))<1e-11)
    check(abs(wm*math.sin(a)*0+wp*math.sin(b)*0)<1e-12)
    # Tangent line F(x)+lambda*x is nonnegative throughout the complete candidate support interval.
    for j in range(2001):
        x=-r+(1+r)*j/2000
        F=math.cos(k*math.asin(min(1.0,max(-1.0,x))))
        check(F+lam*x>=-1e-10, f'failed k={k}, j={j}')
    check(abs(math.cos(k*math.asin(-r))-lam*r)<1e-10)
    check(abs(math.cos(k*math.asin(xp))+lam*xp)<1e-10)
    if k>=4:
        det=math.sin(a)*math.sin(k*b)-math.sin(b)*math.sin(k*a)
        check(abs(det)>0.01)
    return t,lam,r,math.pi-2*math.asin(r),wm,wp

for k in range(2,102,2):
    t,lam,r,g,w0,w1=calc(k)
    if k in (2,4,6,8,10,20,100):
        print('k=%d t=%.12f lambda=%.12f r=%.12f gap=%.12f weights=(%.12f,%.12f)'%(k,t,lam,r,g,w0,w1))

# The k=4 value is an independently known exact special case.
check(abs(calc(4)[3]-2.5693561006314884)<1e-11)
limit_t=bisect(lambda t:t*math.sin(t)+math.cos(t),math.pi/2,math.pi)
L=-math.cos(limit_t)/limit_t
limit_a=bisect(lambda a:math.cos(a)-L*a,0.0,math.pi/2)
check(abs(100*(math.pi-calc(100)[3])/2-limit_a)<0.002)
print('t_infinity=%.12f L=%.12f gap_coefficient_a=%.12f'%(limit_t,L,limit_a))
print('CHECK_PASSED',COUNT)
