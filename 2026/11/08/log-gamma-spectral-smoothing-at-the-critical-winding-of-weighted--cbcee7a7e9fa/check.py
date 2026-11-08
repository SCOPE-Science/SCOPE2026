#!/usr/bin/env python3
"""Finite checks of beta-integral matrix coefficients for a Bergman angular spiral.
Requires mpmath. These tests supplement, not replace, the asymptotic proof.
"""
from mpmath import mp
mp.dps = 38

def beta(a,b): return mp.beta(a,b)

def entry(n,k,alpha,beta_twist,gamma):
    assert n >= max(0,-k)
    A=mp.mpf(alpha); B=mp.mpf(beta_twist); G=mp.mpf(gamma)
    norm=mp.sqrt(beta(n+1,A+1)*beta(n+k+1,A+1))
    def fun(u):
        if not (0<u<n): return mp.mpc(0)
        phase= -k*B*(1+mp.log(n/u))**G
        return (u/n)**A*(1-u/n)**(n+k/2)*mp.exp(1j*phase)/n
    return mp.quad(fun,[0,mp.mpf(n)/8,mp.mpf(n)/2,mp.mpf(n)])/norm

def critical(n,k,alpha,beta_twist):
    return mp.exp(-1j*k*beta_twist)*beta(n+k/2+1,alpha+1+1j*k*beta_twist)/mp.sqrt(beta(n+1,alpha+1)*beta(n+k+1,alpha+1))

checks=0
for alpha in ('0','1.4'):
    for n,k in [(5,1),(19,2),(40,-2)]:
        B=mp.mpf('1.3'); val=entry(n,k,alpha,B,1); expected=critical(n,k,mp.mpf(alpha),B)
        assert abs(val-expected)<mp.mpf('1e-11'), (n,k,alpha,val,expected)
        checks+=1
for n in (100,500):
    for gamma in ('0.6','1','1.55'):
        alpha=mp.mpf('0'); B=mp.mpf('1.3'); k=1
        J=entry(n,k,alpha,B,gamma)
        gauge=mp.exp(1j*k*B*(1+mp.log(n))**mp.mpf(gamma))
        normalized=gauge*J
        assert abs(normalized)<=1.0000001
        if gamma=='1': assert abs(normalized-mp.gamma(1+1j*B))<mp.mpf('0.02')
        if gamma=='0.6': assert abs(normalized-1)<mp.mpf('0.4')
        if gamma=='1.55': assert abs(normalized)<mp.mpf('0.1')
        checks+=1
for B in ('0.4','1.3','2.1'):
    beta_twist=mp.mpf(B)
    lhs=abs(mp.gamma(1+1j*beta_twist))**2
    rhs=mp.pi*beta_twist/mp.sinh(mp.pi*beta_twist)
    assert abs(lhs-rhs)<mp.mpf('1e-35')
    checks+=1
print('BERGMAN_SPIRAL_BETA_GAMMA_CHECKS_PASS', checks)
