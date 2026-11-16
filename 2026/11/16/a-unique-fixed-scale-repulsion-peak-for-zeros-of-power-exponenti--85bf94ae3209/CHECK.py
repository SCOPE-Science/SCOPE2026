#!/usr/bin/env python3
"""Separate finite consistency checks for the microscopic zero-pair theorem.

Usage: python CHECK.py
Requires mpmath. Finite tests illustrate, but cannot prove, infinite-parameter claims.
"""
import mpmath as mp
mp.mp.dps = 75
COUNT = 0

def check(cond, description):
    global COUNT
    if not cond:
        raise AssertionError(description)
    COUNT += 1

def coeff(beta, count=18):
    s = mp.mpf(2)/mp.mpf(beta)
    return [1/mp.gamma((n+1)*s) for n in range(count)]

def pair_intensity(beta, r):
    a=coeff(beta)
    r=mp.mpf(r)
    x=[mp.mpf(0),r]
    def cov(u,v):return sum(a[n]*(u*v)**n for n in range(len(a)))
    def cross(u,v):return sum(n*a[n]*u**(n-1)*v**n for n in range(1,len(a)))
    def deriv(u,v):return sum(n*n*a[n]*(u*v)**(n-1) for n in range(1,len(a)))
    A=mp.matrix([[cov(u,v) for v in x] for u in x])
    B=mp.matrix([[cross(u,v) for v in x] for u in x])
    C=mp.matrix([[deriv(u,v) for v in x] for u in x])
    W=C-B*(A**-1)*B.T
    return (W[0,0]*W[1,1]+W[0,1]**2)/(mp.pi**2*mp.det(A))

def gamma_J(s):return mp.gamma(2*s)**2/(mp.gamma(s)*mp.gamma(3*s))
def q(s):return 2*mp.gamma(2*s)**3/(mp.gamma(s)*mp.gamma(3*s)**2)
def R(s):return 2*gamma_J(s)**2

def test():
    # Analytic identity for the planar Gaussian entire function.
    check(abs(q(mp.mpf(1))-mp.mpf('0.5'))<mp.mpf('1e-50'), 'classical q')
    check(abs(R(mp.mpf(1))-mp.mpf('0.5'))<mp.mpf('1e-50'), 'classical R')
    check(abs(gamma_J(mp.mpf(1))-mp.mpf('0.5'))<mp.mpf('1e-50'), 'classical J')
    # Two independent ways to compute the two-point correlation: Gaussian blocks
    # versus the first-three-coefficients limiting expression.
    for beta in [mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4'),
                 mp.mpf('10'),mp.mpf('30'),mp.mpf('100')]:
        a=coeff(beta)
        limit=2*a[2]**2/(mp.pi**2*a[0]*a[1])
        for r in [mp.mpf('0.04'),mp.mpf('0.02'),mp.mpf('0.01')]:
            ratio=pair_intensity(beta,r)/(limit*r*r)
            check(abs(ratio-1)<mp.mpf('.004'), f'Kac-Rice beta={beta}, r={r}')
    # Verify the multiplication formulas independently at diverse parameters.
    for s in [mp.mpf('.005'),mp.mpf('.02'),mp.mpf('.06'),mp.mpf('.2'),
              mp.mpf('.5'),mp.mpf('1'),mp.mpf('3'),mp.mpf('12')]:
        j2=mp.sqrt(3)/2*(mp.mpf(16)/27)**s*mp.gamma(s+mp.mpf('.5'))**2/(mp.gamma(s+mp.mpf(1)/3)*mp.gamma(s+mp.mpf(2)/3))
        q2=3*mp.sqrt(mp.pi)*(mp.mpf(2)/3)**(6*s)*mp.gamma(s+mp.mpf('.5'))**3/(mp.gamma(s+mp.mpf(1)/3)**2*mp.gamma(s+mp.mpf(2)/3)**2)
        check(abs(j2/gamma_J(s)-1)<mp.mpf('1e-50'), 'Gauss identity J')
        check(abs(q2/q(s)-1)<mp.mpf('1e-50'), 'Gauss identity q')
    # Numerical samples only; the proof uses strict convexity of trigamma.
    s_values=[mp.mpf('0.0001')*(mp.mpf(2)**(k/2)) for k in range(39)]
    for s in s_values:
        tri=lambda t:mp.polygamma(1,t)
        mid=tri(s+mp.mpf(1)/2)
        ends=tri(s+mp.mpf(1)/3)+tri(s+mp.mpf(2)/3)
        check(ends-2*mid>0, 'strict midpoint convexity of trigamma at sample')
        check(3*mid-2*ends<0,'strict log-concavity q at sample')
        check(2*mid-ends<0,'strict log-concavity J at sample')
    d=lambda s: 6*mp.digamma(2*s)-mp.digamma(s)-6*mp.digamma(3*s)
    root=mp.findroot(d,(mp.mpf('.04'),mp.mpf('.09')))
    check(mp.mpf('.0597556889857')<root<mp.mpf('.0597556889859'),'unique root bracket')
    check(mp.mpf('33.4696165996')<2/root<mp.mpf('33.4696165997'),'beta star bracket')
    check(mp.mpf('2.2868409388')<q(root)<mp.mpf('2.2868409389'),'maximum bracket')
    check(d(mp.mpf('.01'))>0 and d(mp.mpf('.1'))<0,'derivative signs')
    # Physical-scale coefficient rises with s to a unique maximum, whereas
    # density-scaled coefficient falls strictly with s.
    pairs=[(mp.mpf('0.002')*(mp.mpf('1.32')**k)) for k in range(35)]
    for left,right in zip(pairs,pairs[1:]):
        check(R(left)>R(right),'R decreases with s at sampled points')
    # Gamma-ratio boundary values and classical beta=2 normalization.
    check(abs(R(mp.mpf('0.00001'))-mp.mpf(9)/8)<mp.mpf('1e-7'),'beta infinity limit')
    for s in [mp.mpf('5'),mp.mpf('15'),mp.mpf('25')]:
        asym=(mp.mpf(3)/2)*(mp.mpf(256)/729)**s
        check(abs(R(s)/asym-1)<mp.mpf('.2'),'small beta asymptotic')
    print('PASS:',COUNT,'finite assertions')

if __name__=='__main__':test()
