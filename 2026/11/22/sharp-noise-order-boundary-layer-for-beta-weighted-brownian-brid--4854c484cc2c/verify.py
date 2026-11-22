"""Supplementary numerical/exact checks for beta-weighted Brownian-bridge quadrature.
Requires Python >= 3.9 and mpmath >= 1.3.0.
The proof of uniqueness and asymptotics is in RESULT.md, not in this script.
"""
from fractions import Fraction as Q
import math
from mpmath import mp

mp.dps = 70


def covariance(n, t):
    return t * (1-t**n) / (n+1)


def variance(n):
    return Q(n*n,(n+1)**2*(2*n+1))


def F(n, eta, t):
    return 2*eta + t - 2*(n+1)*eta*t**n - (2*n+1)*t**(n+1) + 2*n*t**(n+2)


def score(n, eta, t):
    v=t*(1-t)+eta
    if v == 0: return mp.mpf(0)
    return t**2*(1-t**n)**2 / ((n+1)**2*v)


def root(n, eta):
    lo=mp.mpf(0)
    hi=mp.mpf(1)
    for _ in range(240):
        mid=(lo+hi)/2
        if F(n,eta,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


count=0
# Exact moment covariance identity by separate rational integrations of K(s,t).
for n in range(1,18):
    for a in range(1,17):
        t=Q(a,17)
        lower=n*(1-t)*t**(n+1)/(n+1)
        upper=n*t*((1-t**n)/n-(1-t**(n+1))/(n+1))
        value=lower+upper
        assert value == covariance(n,t), (n,t,value,covariance(n,t))
        count+=1
print('Exact rational point-covariance identities:',count)

# Independent variance integral: n * int s^(n-1) cov(A_n,B_s) ds.
for n in range(1,51):
    independent=Q(n,n+1)*(Q(1,n+1)-Q(1,2*n+1))
    assert independent==variance(n),(n,independent,variance(n))
    count+=1
print('Exact total algebraic identities:',count)

# Root is interior and score is maximal on dense non-root grids.
for n in (1,2,3,4,5,10,25,100):
    previous=None
    for eta in map(mp.mpf, ('0','0.0001','0.02','0.1','1','30')):
        t=root(n,eta)
        r=mp.power(n+1,mp.mpf(-1)/n)
        assert mp.mpf(0)<t<mp.mpf(1)
        assert abs(F(n,eta,t))<mp.mpf('1e-50')
        assert t>=r-mp.mpf('1e-55')
        if previous is not None:
            assert t<=previous+mp.mpf('1e-55')
        previous=t
        val=score(n,eta,t)
        for j in range(1,1000):
            x=mp.mpf(j)/1000
            assert val+mp.mpf('1e-50')>=score(n,eta,x),(n,eta,t,x)
            count+=1
print('Exact-root and dense-grid design comparisons:', count)

# Limit constants and double scaling; moderate n only to avoid cancellation in float.
c=mp.findroot(lambda u: mp.exp(u)-1-2*u,(mp.mpf('1'),mp.mpf('2')))
lim0=2*(1-mp.exp(-c))**2/c
assert abs(c-mp.mpf('1.2564312086261696770'))<mp.mpf('1e-17')
for alpha in (mp.mpf('0'),mp.mpf('.5'),mp.mpf('1'),mp.mpf('5')):
    u=mp.findroot(lambda z: mp.exp(z)-1-2*z-2*alpha,(mp.mpf('1'),mp.mpf('5')))
    fraction_lim=2*(1-mp.exp(-u))**2/(u+alpha)
    estimates=[]
    for n in (200,1000,6000):
        eta=alpha/n
        t=root(n,eta)
        fn=score(n,eta,t)/mp.mpf(variance(n).numerator)*variance(n).denominator
        estimates.append((abs(n*(1-t)-u),abs(fn-fraction_lim)))
        count+=1
    assert estimates[-1][0]<estimates[0][0] and estimates[-1][1]<estimates[0][1],(alpha,estimates)
print('Crossover checks:',count,'limiting noiseless information fraction:',mp.nstr(lim0,18))

for eta in map(mp.mpf,('0.03','0.2','2')):
    errors=[]
    for n in (200,1000,6000):
        t=root(n,eta)
        u=n*(1-t)
        predicted=mp.log(n)+mp.log(2*eta/(1+2*eta))
        rel=score(n,eta,t)/mp.mpf(variance(n).numerator)*variance(n).denominator
        errors.append((abs(u-predicted),abs(rel*n*eta/2-1)))
        count+=1
    assert errors[-1][0] < errors[0][0] and errors[-1][1] < errors[0][1],(eta,errors)
print('Fixed-noise asymptotic checks:',count)
print('PASS')
