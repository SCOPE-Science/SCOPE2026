"""Numerical consistency tests for integrated-Volterra one-site quadrature.

The theorem's all-order uniqueness is proved analytically; these finite tests
are reproducibility checks, not infinite-domain certification.
Run: python verify.py    Requires mpmath>=1.3.
"""
from math import isclose
import mpmath as mp

mp.mp.dps = 45
checks = 0

def check(cond, message):
    global checks
    assert cond, message
    checks += 1

def c(a,t):
    if t == 0:
        return mp.mpf(0)
    return (t**(a+1) * mp.hyp2f1(-a-1, 1, a+2, t) /
            ((a+1)*mp.gamma(a+1)*mp.gamma(a+2)))

def c_integral(a,t):
    return mp.quad(lambda s: (t-s)**a * (1-s)**(a+1), [0,t]) / (mp.gamma(a+1)*mp.gamma(a+2))

def variance(a,t):
    return t**(2*a+1)/((2*a+1)*mp.gamma(a+1)**2)

def target_variance(a):
    return 1/((2*a+3)*mp.gamma(a+2)**2)

def u(a,t):
    F = mp.hyp2f1(-a-1,1,a+2,t)
    Fp = -(a+1)/(a+2) * mp.hyp2f1(-a,2,a+3,t)
    return a+1 + t*Fp/F

def crit(a):
    if a==0: return mp.inf
    return 1/(4*a*(a+1)*(2*a+1)*mp.gamma(a+1)**2)

def gain(a,t,e):
    if t == 0: return mp.mpf(0)
    return c(a,t)**2/(variance(a,t)+e)

def stationarity(a,t,e):
    return 2*u(a,t)-(2*a+1)*variance(a,t)/(variance(a,t)+e)

def optimum(a,e):
    if a>0 and e>=crit(a): return mp.mpf(1)
    lo=mp.mpf('1e-20'); hi=mp.mpf(1)
    for _ in range(160):
        mid=(lo+hi)/2
        if stationarity(a,mid,e)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

for a in map(mp.mpf, ['0','0.25','0.5','1','1.5','2','3']):
    for t in map(mp.mpf, ['0.1','0.35','0.75','1']):
        check(mp.almosteq(c(a,t),c_integral(a,t),rel_eps=mp.mpf('1e-32')), ('covariance quadrature', a,t))
        check(mp.almosteq(variance(a,t),mp.quad(lambda s: (t-s)**(2*a),[0,t]) / mp.gamma(a+1)**2,rel_eps=mp.mpf('1e-32')), ('observation variance',a,t))
    for t in map(mp.mpf,['0.2','0.55','0.8']):
        numeric=t*mp.diff(lambda q:c(a,q),t)/c(a,t)
        check(abs(u(a,t)-numeric)<mp.mpf('1e-32'), ('log derivative',a,t))
    vals=[u(a,mp.mpf(k)/20) for k in range(1,21)]
    check(all(vals[i] > vals[i+1] for i in range(19)),('log-time concavity derivative',a))
    check(mp.almosteq(target_variance(a),mp.quad(lambda s: (1-s)**(2*a+2),[0,1])/mp.gamma(a+2)**2,rel_eps=mp.mpf('1e-32')), ('target variance',a))
    noises=([mp.mpf(0),mp.mpf('0.01'),mp.mpf('1'),mp.mpf('100')] if a==0 else
            [mp.mpf(0),crit(a)/4,crit(a)*mp.mpf('0.999'),crit(a),crit(a)*2])
    for e in noises:
        loc=optimum(a,e)
        check(0<loc<=1,('location',a,e))
        if a>0:
            check((loc==1)==(e>=crit(a)),('phase threshold',a,e))
        else:
            check(loc<1,('Brownian no finite endpoint',e))
        if loc<1:
            check(abs(stationarity(a,loc,e)) < mp.mpf('1e-28'),('stationarity',a,e))
        best=gain(a,loc,e)
        for k in range(101):
            t=mp.mpf(k)/100
            check(best + mp.mpf('1e-27') >= gain(a,t,e),('grid global opt',a,e,t))
        check(0<=target_variance(a)-best<=target_variance(a),('conditional variance',a,e))

check(abs(optimum(mp.mpf(0),mp.mpf(0))-mp.mpf(2)/3)<mp.mpf('1e-30'),'Brownian noiseless location')
check(abs(optimum(mp.mpf(1),mp.mpf(0))-(6-mp.sqrt(6))/5)<mp.mpf('1e-30'),'IWP2 noiseless location')
check(mp.almosteq(crit(mp.mpf(1)),mp.mpf(1)/24),'IWP2 boundary')
check(mp.almosteq(crit(mp.mpf(2)),mp.mpf(1)/480),'IWP3 boundary')
print(f'PASS: {checks} numeric consistency assertions, 7 process orders including fractional exponents.')
