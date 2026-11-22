#!/usr/bin/env python3
"""Diagnostic checks of an exact heterogeneous-SIR pressure-coordinate theorem."""
import mpmath as mp
mp.mp.dps = 45

def calc(s, rates, probs, R):
    s = mp.mpf(str(s)); R=mp.mpf(str(R)); i=1-s
    rates = [mp.mpf(str(x)) for x in rates]
    probs = [mp.mpf(str(x)) for x in probs]
    assert all(x>=0 for x in rates) and all(p>0 for p in probs)
    assert abs(sum(probs)-1)<mp.mpf('1e-30') and i>0
    G=lambda x: sum(p*mp.exp(-v*x) for p,v in zip(probs,rates))
    L=lambda x: sum(p*v*mp.exp(-v*x) for p,v in zip(probs,rates))
    assert R*s*L(0)>1
    lo=mp.mpf(0);hi=mp.mpf(1)
    while s*L(hi)>1/R: hi*=2
    for _ in range(260):
        md=(lo+hi)/2
        if s*L(md)>1/R: lo=md
        else: hi=md
    A=(lo+hi)/2
    H=lambda x: i+s*(1-G(x))-x/R
    t=mp.quad(lambda x: 1/H(x),[0,A])/R
    positive=[(p,v) for p,v in zip(probs,rates) if v>0]
    star=min(v for p,v in positive)
    pstar=sum(p for p,v in positive if v==star)
    p0=sum(p for p,v in zip(probs,rates) if v==0)
    Hinf=1-s*p0
    C=mp.quad(lambda x: (s*(G(x)-p0))/((i+s*(1-G(x)))*Hinf),[0, 1, 5, 20, mp.inf])
    approx=mp.log(R*s*pstar*star)/(star*Hinf)+C
    return t,A,R*t-approx

if __name__ == '__main__':
    s=mp.mpf('0.99')
    triple={}
    for a in [mp.mpf('0'),mp.mpf('0.5'),mp.mpf('1')]:
        val=calc(s,[a,2-a],[mp.mpf('0.5')]*2,20)
        triple[a]=val
        assert abs(val[2])<mp.mpf('2')
    assert triple[mp.mpf('.5')][0]>triple[mp.mpf('1')][0]>triple[mp.mpf('0')][0]
    for a in [mp.mpf('0'),mp.mpf('.2'),mp.mpf('1')]:
        t,A,error=calc(mp.mpf('.6'),[a,2-a],[mp.mpf('.5')]*2,mp.mpf('1e8'))
        assert abs(error)<mp.mpf('0.002'), (a,error)
        assert A>0 and t>0
    print('PASS: exact-pressure peak ordering and asymptotic constant diagnostics')
