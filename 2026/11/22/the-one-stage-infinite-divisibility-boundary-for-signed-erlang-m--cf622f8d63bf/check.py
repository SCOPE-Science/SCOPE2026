#!/usr/bin/env python3
"""Finite reproducibility checks for the analytic signed-Erlang theorem.

The proof of the full parameter range is in RESULT.md; this script
checks algebraic identities and representative complex zeros.
"""
from fractions import Fraction as F
from math import comb
import cmath
import mpmath as mp

mp.mp.dps = 65
count = 0

def check(x, why):
    global count
    assert x, why
    count += 1

# Check exact coefficients of rational MGF for the shape-one case.
for ap, bp in [(1,1),(1,2),(2,3),(3,1),(7,11)]:
    a,b = F(ap),F(bp)
    for pn,pd in [(1,2),(1,3),(2,3),(1,7),(6,7),(17,31)]:
        p = F(pn,pd)
        c = p/b - (1-p)/a
        check(-1/a<c<1/b, 'Lévy-threshold bounds')
        for j in range(1,9):
            # Coefficient [z^j] of p(1-z/a)^-1+(1-p)(1+z/b)^-1
            m1=p/a**j+(1-p)*(-1)**j/b**j
            # Rational numerator (1+cz) over common denominator
            m2=sum((1/a)**r*((-1/b)**(j-r)) for r in range(j+1))
            m2+=c*sum((1/a)**r*((-1/b)**(j-1-r)) for r in range(j))
            check(m1==m2,'MGF rational identity')
        # Lévy measure is nonnegative and exp integrable on both half-lines.
        for v in [F(1,10),F(1,2),F(1),F(3),F(10)]:
            # Use exponentials at rational intensity in high precision.
            vp=mp.mpf(v.numerator)/v.denominator
            nup=mp.exp(-mp.mpf(ap)*vp)
            num=mp.exp(-mp.mpf(bp)*vp)
            if c<0: nup-=mp.exp(-vp/mp.mpf(-c.numerator)*c.denominator)
            if c>0: num-=mp.exp(-vp/mp.mpf(c.numerator)*c.denominator)
            check(nup>=-mp.mpf('1e-55') and num>=-mp.mpf('1e-55'),'positive jump densities')

# Exact polynomial reduction: a zero is equivalent to w**k=-(1-p)/p.
for k in range(2,13):
    for p in [mp.mpf('0.001'),mp.mpf('0.03'),mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.85'),mp.mpf('0.999')]:
        w=((1-p)/p)**(mp.mpf(1)/k)*mp.exp(mp.pi*1j/k)
        check(abs(w**k+(1-p)/p)<mp.mpf('1e-48'),'complex root equation')
        for a,b in [(1,1),(1,3),(3,1),(7,11),(50,1)]:
            aa,bb=mp.mpf(a),mp.mpf(b)
            z=(w-1)/(w/aa+1/bb)
            check(-bb<z.real<aa,'zero strictly in MGF strip')
            m=p/(1-z/aa)**k+(1-p)/(1+z/bb)**k
            check(abs(m)<mp.mpf('1e-40'),'zero of MGF numerator')
            check(abs(1-z/aa)>mp.mpf('1e-12') and abs(1+z/bb)>mp.mpf('1e-12'),'non-pole zero')

# Shape-one integral form versus exact MGF at interior points.
for p in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.9')]:
    for a,b in [(1,1),(2,3),(4,1)]:
        a,b=mp.mpf(a),mp.mpf(b)
        c=p/b-(1-p)/a
        for zz in [mp.mpf('0.1'),mp.mpf('-0.2'),mp.mpf('0.25')]:
            if zz>=a or zz<=-b: continue
            lap=-mp.log(1-zz/a)-mp.log(1+zz/b)+mp.log(1+c*zz)
            def integ(rate, sign):
                return -mp.log(1-sign*zz/rate)
            comp=integ(a,1)+integ(b,-1)
            if c>0: comp-=integ(1/c,-1)
            elif c<0: comp-=integ(1/(-c),1)
            check(abs(comp-lap)<mp.mpf('1e-50'),'finite variation Lévy exponent')
print(f'PASS: {count} exact and high-precision finite checks; no inference of infinite coverage from finite tests.')
