#!/usr/bin/env python3
"""Standalone supporting checks for section dynamics and discrete-scale tail."""
from fractions import Fraction
import mpmath as mp
mp.mp.dps=45
count=0
for m,n in [(4,2),(6,3),(3,2),(5,2),(2,3),(3,4),(4,4)]:
    p=Fraction(m,n)
    for a in [Fraction(1,2),Fraction(2,3),Fraction(1,1),Fraction(3,2)]:
        # Fraction powers of general rational exponents are tested in logarithmic form.
        x=mp.mpf(a.numerator)/a.denominator
        y=x**(mp.mpf(m)/n)
        z=y**(mp.mpf(m)/n)
        assert mp.almosteq(z,x**(mp.mpf(m*m)/(n*n)))
        count+=1
for p in [mp.mpf('1.5'),mp.mpf(2),mp.mpf('2.5'),mp.mpf(5)]:
    L=mp.log(p); g=mp.euler; omega=2*mp.pi/L
    def S(q):
        t=q; ans=mp.mpf(0)
        for j in range(3000):
            v=mp.exp(-t); ans+=v
            if v<mp.mpf('1e-43'):break
            t*=p
        return ans
    def P(w):
        return mp.re(sum(mp.gamma(1j*omega*k)/L*mp.exp(2j*mp.pi*k*w) for k in range(-60,61) if k))
    for w in [mp.mpf('8.125'),mp.mpf('10.125'),mp.mpf('12.578')]:
        q=p**(-w)
        T=2*S(q)-mp.exp(-q)
        e=T-(2*w-2*g/L+2*P(w))
        assert -mp.mpf('1e-27')<=e<=(1+2/(p-1))*q+mp.mpf('1e-27'),(p,w,e)
        count+=1
print('supporting_checks_passed',count)
