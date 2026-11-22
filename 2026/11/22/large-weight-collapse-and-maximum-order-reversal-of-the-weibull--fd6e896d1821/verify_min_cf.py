"""Reproducible numerical checks for the high-weight Weibull minCF theorem.

Run: python verify_min_cf.py
Requires mpmath >= 1.2. Numerical checks supplement the analytic proof.
"""
import math
import mpmath as mp

mp.mp.dps = 65
assertions = 0

def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)


def psi0(t):
    return -t * mp.expm1(-1/t)


def empirical(t, ys):
    return sum(min(mp.mpf(1), t*y) for y in ys)/len(ys)


def reference_integral(gamma):
    return 2*(mp.mpf(2)/gamma)**mp.mpf('1.5') * mp.besselk(3, 2*mp.sqrt(2*gamma))


def reference_integral_independent(gamma):
    return mp.quad(lambda t: t*t*mp.exp(-2/t-gamma*t), [0, 1/mp.sqrt(gamma), mp.inf])


def statistic(ys, gamma):
    n=len(ys)
    nodes=[mp.mpf(0)]+sorted(set(1/y for y in ys))+[mp.inf]
    return n*sum(mp.quad(lambda t: (empirical(t,ys)-psi0(t))**2*mp.exp(-gamma*t), [lo,hi])
                 for lo,hi in zip(nodes[:-1],nodes[1:]))


def correction(ys, gamma):
    n=len(ys)
    nodes=sorted(set(1/y for y in ys))+[mp.inf]
    def integrand(t):
        a=sum(max(mp.mpf(0),t*y-1) for y in ys)/n
        d=t*mp.exp(-1/t)
        return (2*d*a-a*a)*mp.exp(-gamma*t)
    return n*sum(mp.quad(integrand, [lo,hi]) for lo,hi in zip(nodes[:-1],nodes[1:]))


def error_bound(n,gamma):
    a=mp.mpf(1)/n
    return n*mp.exp(-gamma*a)*((1+a*a)/gamma+2*a/gamma**2+2/gamma**3)


def fit_weibull_standardized(xs):
    """Shape MLE by monotone root bracket; scale profiled out."""
    lx=list(map(math.log,xs))
    av=sum(lx)/len(lx)
    def score(phi):
        values=[phi*v for v in lx]
        vmax=max(values)
        w=[math.exp(v-vmax) for v in values]
        return 1/phi+av-sum(ww*xx for ww,xx in zip(w,lx))/sum(w)
    lo=1e-6
    hi=1.0
    while score(hi)>0:
        hi*=2
        if hi>1e6:
            raise ValueError('could not bracket MLE')
    for _ in range(140):
        mid=(lo+hi)/2
        if score(mid)>0:
            lo=mid
        else:
            hi=mid
    phi=(lo+hi)/2
    u=[phi*v for v in lx]
    umax=max(u)
    weights=[math.exp(t-umax) for t in u]
    y=[mp.mpf(len(xs)*w/sum(weights)) for w in weights]
    return phi,y

for gamma in map(mp.mpf, (3,12,40,100)):
    x=reference_integral(gamma)
    z=reference_integral_independent(gamma)
    check(abs(x/z-1)<mp.mpf('1e-35'), 'Bessel integral identity')

samples=[['0.2','1.8'], ['0.3','0.9','1.8'], ['0.2','0.2','2.6'], ['0.05','0.25','0.5','1.2','3.0']]
for sample in samples:
    ys=[mp.mpf(x) for x in sample]
    n=len(ys)
    check(abs(sum(ys)-n)<mp.mpf('1e-40'), 'mean one')
    check(max(ys)<=n, 'sample maximum bound')
    for t in (mp.mpf(1)/(2*n),mp.mpf(1)/n):
        check(abs(empirical(t,ys)-t)<mp.mpf('1e-40'), 'linear minCF segment')
    for gamma in map(mp.mpf, (20,60,100)):
        actual=statistic(ys,gamma)
        ideal=n*reference_integral(gamma)
        d=correction(ys,gamma)
        check(abs((ideal-actual)-d) < max(mp.mpf('1e-58'),abs(d)*mp.mpf('1e-28')), 'correction identity')
        check(abs(actual-ideal)<=error_bound(n,gamma)*(1+mp.mpf('1e-30')), 'uniform bound')
    M=max(ys)
    k=ys.count(M)
    for gamma in map(mp.mpf, (100,200,400)):
        actual=correction(ys,gamma)
        estimate=2*k*mp.exp(-M-gamma/M)/gamma**2
        check(abs(actual/estimate-1)<mp.mpf('0.26'), 'endpoint correction scaling')

for sample in ([0.4,1.0,3.1,6.8],[1.0,1.7,2.8,4.2,8.1]):
    phi,ys=fit_weibull_standardized(sample)
    check(phi>0,'finite positive Weibull shape')
    check(abs(sum(ys)-len(ys))<mp.mpf('1e-12'),'profile MLE mean-one equation')
    check(max(ys)<=len(ys),'fitted maximum bound')

# The large-weight statistic eventually orders fixed samples by reverse maximum.
a=[mp.mpf(s) for s in ['0.2','0.6','2.2']]
b=[mp.mpf(s) for s in ['0.8','1.0','1.2']]
check(max(a)>max(b),'distinct maxima')
for gamma in map(mp.mpf,(120,200,300)):
    check(correction(a,gamma)>correction(b,gamma), 'extreme-order ranking')

print('PASS', assertions, 'analytic-identity and numerical checks')
print('Leading constant:',mp.nstr(2**mp.mpf('1.25')*mp.sqrt(mp.pi),20))
print('Check status: numerical only; proof is in RESULT.md')
