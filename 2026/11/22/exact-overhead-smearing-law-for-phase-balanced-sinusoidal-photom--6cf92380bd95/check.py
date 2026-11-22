#!/usr/bin/env python3
"""Numerical diagnostics for an idealized periodic-signal integration model."""
import math
import mpmath as mp
mp.mp.dps = 70

def root(a):
    a=mp.mpf(a)
    if a <= 0: raise ValueError('overhead must be positive')
    f=lambda x: 2*mp.cot(x)-1/x-1/(x+a)
    lo=mp.mpf('1e-45')
    hi=mp.pi/2
    for j in range(250):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else: hi=mid
    return (lo+hi)/2

def eta(x,a):
    return (mp.sin(x)**2)/(x*(x+a))

assert abs(mp.findroot(lambda x: mp.tan(x)-2*x,(mp.mpf('1'),mp.mpf('1.4')))-mp.mpf('1.1655611852072113'))<mp.mpf('1e-14')
xinf=mp.findroot(lambda x: mp.tan(x)-2*x, 1.2)
count=1
for a in ['0.0000000001','0.000001','0.001','0.01','0.1','1','10','100','1000000']:
    x=root(a)
    assert mp.mpf(0)<x<xinf<mp.pi/2
    assert abs(2*mp.cot(x)-1/x-1/(x+mp.mpf(a)))<mp.mpf('1e-60')
    count+=2
    # brute grid including alias lobes to 40 pi
    af=float(a); xf=float(x); jf=float(eta(x,mp.mpf(a)))
    for k in range(1,4001):
        xx=40*math.pi*k/4001
        assert (math.sin(xx)**2)/(xx*(xx+af)) <= jf+1e-12
        count+=1
    assert abs(float(eta(x,mp.mpf(a)))-float(eta(mp.mpf(xf),mp.mpf(a))))<1e-10
    count+=1
for a in [10.0**(i/9) for i in range(-90,91)]:
    x=root(str(a)); count+=1
    eps=1e-7
    def lf(y):return math.log((math.sin(y)**2)/(y*(y+a)))
    xx=float(x)
    assert lf(xx)>=lf(max(1e-12,xx-eps))-1e-12
    assert lf(xx)>=lf(xx+eps)-1e-12
    count+=2
for a in ['1e-12','1e-10','1e-8']:
    x=root(a)
    ratio=x/(mp.mpf('1.5')*mp.mpf(a))**(mp.mpf(1)/3)
    assert abs(ratio-1)<mp.mpf('0.001')
    eta_star=eta(x,mp.mpf(a))
    loss=(1-eta_star)/(mp.mpf('1.5')*mp.mpf(a))**(mp.mpf(2)/3)
    assert abs(loss-1)<mp.mpf('0.001')
    count+=2
for a in ['1e4','1e6','1e8']:
    x=root(a)
    assert abs(x-xinf)<mp.mpf('0.001')
    assert abs(mp.mpf(a)*eta(x,mp.mpf(a))-mp.sin(xinf)**2/xinf)<mp.mpf('0.001')
    count+=2
print('PASS',count,'assertions; limiting half-phase',mp.nstr(xinf,26),'limiting time fraction',mp.nstr(xinf/mp.pi,20))
for over in ['0.001','0.01','0.05','0.1']:
    a=mp.pi*mp.mpf(over)
    x=root(a)
    print('overhead/P',over,'optimal_exposure/P',mp.nstr(x/mp.pi,14),'efficiency',mp.nstr(eta(x,a),14))
