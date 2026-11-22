#!/usr/bin/env python3
"""Standalone exact and independent integral checks for Poisson-maintained GHZ entanglement."""
from fractions import Fraction
from math import comb, sqrt
import mpmath as mp
import sympy as sp

z,r = sp.symbols('z r', positive=True)

def diagonal_exact(n,k,rho):
    p=sp.Poly(sp.expand(((1+z)/2)**(n-k)*((1-z)/2)**k/2 + ((1+z)/2)**k*((1-z)/2)**(n-k)/2), z)
    return sp.factor(sum(coef*rho/(rho+mon[0]) for mon,coef in p.terms()))

def F_exact(n):
    return sp.factor(r/(r+n) - 1 + sum(sp.Rational(comb(n,j),2**(n-1))*r/(r+j) for j in range(0,n+1,2)))

def F_num(n,rho):
    rho=mp.mpf(rho)
    return rho/(rho+n)-1+sum(mp.mpf(comb(n,j))/2**(n-1)*rho/(rho+j) for j in range(0,n+1,2))

checks=0
for n in range(3,9):
    for rho in (sp.Rational(1,2),sp.Integer(1),sp.Rational(7,3),sp.Integer(6)):
        vals=[diagonal_exact(n,k,rho) for k in range(n+1)]
        assert sp.simplify(sum(sp.binomial(n,k)*vals[k] for k in range(n+1))-1)==0
        checks+=1
        assert vals[0]==vals[-1]
        checks+=1
        for k in range(n+1):
            assert vals[k]==vals[n-k]
            left=rho*(vals[k]-(sp.Rational(1,2) if k in (0,n) else 0))
            right=sp.Rational(1,2)*((k*vals[k-1] if k else 0)+((n-k)*vals[k+1] if k<n else 0)-n*vals[k])
            assert sp.simplify(left-right)==0
            checks+=1
        coherence=rho/(2*(rho+n))
        assert sp.simplify(2*coherence-(1-2*vals[0])-F_exact(n).subs(r,rho))==0
        checks+=1
assert sp.simplify(F_exact(3)-(2*r**2+r-9)/(2*(r+2)*(r+3)))==0;checks+=1
assert sp.simplify(F_exact(4)-(r**2-7)/((r+2)*(r+4)))==0;checks+=1

mp.mp.dps=75
for n in (3,4,5,8,12):
    for rho in (mp.mpf('0.5'),mp.mpf('2.3'),mp.mpf('8.1')):
        # Independent integration in elapsed Poisson clock E, not the rational expansion.
        rr=mp.mpf(rho)
        def integrand(e):
            u=(1+mp.exp(-e/rr))/2
            v=(1-mp.exp(-e/rr))/2
            return mp.exp(-e)*(mp.exp(-n*e/rr)+u**n+v**n-1)
        val=mp.quad(integrand,[0,1,3,8,20,mp.inf]);val2=F_num(n,rr)
        assert abs(val-val2)<mp.mpf('1e-48'),(n,rho,val,val2)
        checks+=1

for n in (3,4,5,6,8,12,20,50,100,500):
    root=mp.findroot(lambda x:F_num(n,x),(mp.mpf(n)*mp.mpf('0.6'),mp.mpf(n)*mp.mpf('0.8')))
    assert abs(F_num(n,root))<mp.mpf('1e-45')
    assert F_num(n,root/2)<0<F_num(n,root*2)
    checks+=3

c0=1/mp.sqrt(2); d0=-mp.mpf(1)/2+mp.sqrt(2)/4
for n in (100,200,500,1000):
    root=mp.findroot(lambda x:F_num(n,x),(mp.mpf(n)*mp.mpf('0.6'),mp.mpf(n)*mp.mpf('0.8')))
    assert abs(root-n*c0-d0)<mp.mpf(1)/n, (n,root-n*c0-d0)
    checks+=1
print('PASS',checks,'exact matrix-component, integral, threshold and asymptotic assertion groups')
print('n=3:',mp.nstr(mp.sqrt(73)/4-mp.mpf(1)/4,18))
print('n=4:',mp.nstr(mp.sqrt(7),18))
print('asymptotic:',mp.nstr(c0,18),mp.nstr(d0,18))
