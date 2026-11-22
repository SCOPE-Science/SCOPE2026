#!/usr/bin/env python3
"""Reproducibility checks for the Poissonized Hardy BV approximation theorem.
Requires Python 3 and mpmath; numerical checks do not replace the proof.
"""
import mpmath as mp

mp.mp.dps=45


def W(t, a):
    return mp.exp(-t)*mp.besseli(0, 2*mp.sqrt(t*a))


def root(t):
    lo, hi=mp.mpf('0'),max(mp.mpf('4'),t*2+4)
    while W(t, hi)<1: hi*=2
    for _ in range(200):
        mid=(lo+hi)/2
        if W(t,mid)<1: lo=mid
        else: hi=mid
    return (lo+hi)/2


def step_err_bessel(t,a):
    s=mp.exp(-a)
    return mp.quad(lambda v: mp.exp(-v)*(1-W(t,v)),[0,a])


def step_err_poisson(t,a):
    s=mp.exp(-a)
    total=mp.mpf('0')
    for m in range(1,180):
        weight=mp.exp(-t)*t**m/mp.factorial(m)
        power=mp.fsum(a**k/mp.factorial(k) for k in range(1,m+1))
        total+=weight*s*power
        if m>t+45 and weight<mp.mpf('1e-35'):break
    return total


def gap_ratio(t,a):
    s=mp.exp(-a)
    # 1 - C(t) at a maximizer, by integration by parts for the compound-Poisson CDF
    return 1+mp.quad(lambda z:mp.exp(z)*W(t,a-z),[0,a])


def close(x,y,tol=mp.mpf('1e-28')):
    assert abs(x-y)<tol*max(mp.mpf('1'),abs(x),abs(y)),(x,y)


checks=0
for t in map(mp.mpf, ['0.02','0.2','0.75','1.5','3','5']):
    a0=root(t)
    close(W(t,a0),1);checks+=1
    assert W(t,a0*mp.mpf('.9'))<1<W(t,a0*mp.mpf('1.1'));checks+=1
    for a in [a0/3,a0,a0*mp.mpf('1.6'),mp.mpf('0.15'),mp.mpf('2.5')]:
        c1=step_err_bessel(t,a)
        c2=step_err_poisson(t,a)
        close(c1,c2,mp.mpf('2e-29'));checks+=1
        assert c1>=0 and c1<=1;checks+=1
    # Strict unique maximum verified at two points each side, corroborative only.
    peak=step_err_bessel(t,a0)
    for scale in ['0.6','0.85','1.15','1.5']:
        assert peak>step_err_bessel(t,a0*mp.mpf(scale));checks+=1

for tval in ['50','100','250']:
    t=mp.mpf(tval);a=root(t)
    s=mp.exp(-a)
    ratio=gap_ratio(t,a)
    # large-t asymptotics converge slowly, so check only robust coarse ranges
    assert 2 < ratio < mp.mpf('2.09'),(t,ratio);checks+=1
    assert abs(a-(t/4+mp.log(2*mp.pi*t)/4))<mp.mpf('0.10');checks+=1
    print('large-time',tval,'a=',mp.nstr(a,18),'jump=',mp.nstr(s,12),
          'deficit/jump=',mp.nstr(ratio,12))

for tval in ['0.005','0.01','0.02']:
    t=mp.mpf(tval);a=root(t)
    c=step_err_bessel(t,a)
    assert abs(a-(1+t/4))<t*t
    assert abs(c-(t/mp.e-t*t/(4*mp.e)))<t*t*t
    checks+=2

print('PASS',checks,'numerical comparisons; exact mathematical proof is in RESULT.md')
