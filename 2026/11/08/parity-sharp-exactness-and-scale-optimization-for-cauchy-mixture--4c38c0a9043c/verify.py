"""Reproducibility checks for scale-tuned cotangent trapezoids on Cauchy mixtures.

Run with Python 3 and mpmath: python verify.py
This code tests, but does not replace, the analytic proofs of global and asymptotic claims.
"""
import mpmath as mp

mp.mp.dps = 110
checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def r(a, L):
    return (a - L) / (a + L)

def q_closed(a, w, L, n):
    return sum(wi * (1 + r(ai, L)**n) / (1 - r(ai, L)**n)
               for ai, wi in zip(a, w))

def q_sample(a, w, L, n):
    total = mp.mpf(0)
    for k in range(n):
        c = mp.cos(2 * mp.pi * k / n)
        g = sum(wi * ai * L / (mp.pi * (ai**2 + L**2 + (L**2 - ai**2) * c))
                for ai, wi in zip(a, w))
        total += 2 * mp.pi * g / n
    return total

def dq_dL(a, w, L, n):
    total = mp.mpf(0)
    for ai, wi in zip(a, w):
        u = r(ai, L)
        dudL = -2 * ai / (ai + L)**2
        total += 2 * wi * n * u**(n-1) * dudL / (1-u**n)**2
    return total

def bisect(fun, lo, hi, steps=360):
    fl, fh = fun(lo), fun(hi)
    check(fl*fh < 0, 'root bracket')
    for _ in range(steps):
        mid=(lo+hi)/2
        fm=fun(mid)
        if fm==0: return mid
        if fl*fm > 0:
            lo,fl=mid,fm
        else:
            hi,fh=mid,fm
    return (lo+hi)/2

p = mp.mpf
families = [
    ([p(1),p(3)], [p('0.5'),p('0.5')]),
    ([p(1),p(8),p(30)], [p('0.3'),p('0.2'),p('0.5')]),
    ([p('0.1'),p('0.5'),p(2),p(20)], [p('0.1'),p('0.2'),p('0.4'),p('0.3')]),
]
for aa, ww in families:
    low,high=aa[0],aa[-1]
    for n in range(1, 24):
        for L in (low/2, low, mp.sqrt(low*high), high, high*2):
            err=abs(q_sample(aa,ww,L,n)-q_closed(aa,ww,L,n))
            check(err < p('1e-70'),f'quadrature aliasing {aa}, {n}, {L}, {err}')
        if n%2:
            root = bisect(lambda L:q_closed(aa,ww,L,n)-1, low, high)
            check(abs(q_closed(aa,ww,root,n)-1)<p('1e-75'),'odd exactness')
            check(q_closed(aa,ww,low,n)>1 and q_closed(aa,ww,high,n)<1,'odd bracketing')
        else:
            root = bisect(lambda L:dq_dL(aa,ww,L,n), low, high)
            check(abs(dq_dL(aa,ww,root,n)) < p('1e-70'),'even stationary')
            check(q_closed(aa,ww,root,n)>1,'even positive bias')
            for mult in (p('0.6'),p('0.9'),p('1.1'),p('1.6')):
                check(q_closed(aa,ww,root*mult,n)>q_closed(aa,ww,root,n),
                      'even global min samples')
    am=sum(ai*wi for ai,wi in zip(aa,ww))
    hm=sum(wi/ai for ai,wi in zip(aa,ww))
    check(abs(bisect(lambda L:q_closed(aa,ww,L,1)-1, low, high)-am)<p('1e-75'), 'arithmetic n1')
    l2=mp.sqrt(am/hm)
    check(abs(dq_dL(aa,ww,l2,2))<p('1e-80'), 'n2 optimal mean')
    check(abs(q_closed(aa,ww,l2,2)-mp.sqrt(am*hm))<p('1e-80'), 'n2 min bias')

# Strict convexity certificate: bracket is bounded below by one on 0 <= y < 1.
for m in range(1, 12):
    n=2*m
    for yi in range(0,100):
        y=p(yi)/100
        bracket=(n-1)*(1+y**m)-2*sum(y**k for k in range(1,m))
        check(bracket >= 1-p('1e-96'), 'convexity polynomial')

# Two equally weighted endpoint scales: exact geometric even optimizer.
aa=[p(1),p(9)]; ww=[p('0.5'),p('0.5')]
gm=mp.sqrt(aa[0]*aa[1]); rho=(mp.sqrt(aa[1])-mp.sqrt(aa[0]))/(mp.sqrt(aa[1])+mp.sqrt(aa[0]))
for n in range(2,42,2):
    check(abs(dq_dL(aa,ww,gm,n))<p('1e-100'), 'balanced even derivative')
    check(abs(q_closed(aa,ww,gm,n)-1-2*rho**n/(1-rho**n))<p('1e-100'), 'even exact residual')
prev=p('1e9')
for n in range(1,42,2):
    opt=bisect(lambda L:q_closed(aa,ww,L,n)-1, aa[0],aa[1])
    check(gm < opt < prev, 'odd monotone approach')
    prev=opt
    if n >= 29:
        leading=2*rho**(n+1)/(n*(1-rho**2))
        ratio=mp.log(opt/gm)/leading
        check(abs(ratio-1)<p('0.00001'), 'odd exponential refinement')

# The large-node optimal-scale shift and minimized excess are dictated by extremes.
aa=[p(1),p(2),p(7),p(15)]
ww=[p('0.3'),p('0.2'),p('0.1'),p('0.4')]
gm=mp.sqrt(aa[0]*aa[-1]); rho=(mp.sqrt(aa[-1])-mp.sqrt(aa[0]))/(mp.sqrt(aa[-1])+mp.sqrt(aa[0]))
coefficient=(aa[-1]-aa[0])/(4*gm)*mp.log(ww[-1]/ww[0])
for n in (40,81,100,141,200):
    if n%2:
        opt=bisect(lambda L:q_closed(aa,ww,L,n)-1,aa[0],aa[-1],steps=360)
    else:
        opt=bisect(lambda L:dq_dL(aa,ww,L,n),aa[0],aa[-1],steps=360)
    discrepancy=abs(n*mp.log(opt/gm)-coefficient)
    check(discrepancy < p('2.0')/n+mp.mpf('1e-15'), 'asymptotic scale shift')
    if n%2==0:
        actual=q_closed(aa,ww,opt,n)-1
        expected=4*mp.sqrt(ww[0]*ww[-1])*rho**n
        check(abs(actual/expected-1)<p('1.5')/n, 'even endpoint amplitude asymptotic')

print('PASS',checks,'checks; independent trigonometric evaluations, rational identities, finite-scale optimizations, asymptotic regimes')
