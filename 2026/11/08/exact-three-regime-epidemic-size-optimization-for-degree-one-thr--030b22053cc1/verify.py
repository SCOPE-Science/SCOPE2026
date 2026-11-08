#!/usr/bin/env python3
"""Reproduce exact identities and numerical checks for the restricted-degree epidemic theorem.
No external packages are needed. Numerical tests support, but do not replace, the proof.
"""
from fractions import Fraction as Q
from math import isclose

checks = 0

def chk(test, msg):
    global checks
    checks += 1
    if not test:
        raise AssertionError(msg)

def G0(u, t):
    return u**3 + t*u*(1-u*u)**2

def G1(u, t):
    return u*u + t*(1-u*u)*(1-5*u*u)/3

def D(u, t):
    return (1+u)*(1+t*(5*u*u-1)/3)

def Fu(u, t):
    return 1+t*(15*u*u+10*u-1)/3

def Ft(u, t):
    return (1+u)*(5*u*u-1)/3

def Gu(u, t):
    return 3*u*u+t*(1-6*u*u+5*u**4)

def P(u, t):
    return (10*t*u**6 + 5*t*u**5 + (12-9*t)*u**4
            +(3-6*t)*u**3 + (t-3)*u-t)

def Qpoly(u):
    return 10*u**4+5*u**3+u*u-u+1

for a in range(0, 15):
    t = Q(a, 30)
    for b in range(1, 26):
        u = Q(b, 26)
        T = Q((b%17)+1, 19)
        chk(u-(1-T+T*G1(u,t)) == (1-u)*(T*D(u,t)-1), 'fixed point factorization')
        H = -u*(1-u*u)**2*Fu(u,t)+Gu(u,t)*Ft(u,t)
        chk(H == (1+u)*P(u,t)/3, 'derivative polynomial identity')
        chk((P(u,t+Q(1,7))-P(u,t))*7 == (u*u-1)*Qpoly(u), 'slope identity')
        chk(Fu(u,t)>0, 'positive implicit derivative')
        chk(Qpoly(u)>0, 'positive Q(u)')


def bisect(fn,lo,hi,inc=True,steps=120):
    f0=fn(lo); f1=fn(hi)
    if inc: chk(f0<=0 and f1>=0, 'increasing root bracket')
    else: chk(f0>=0 and f1<=0, 'decreasing root bracket')
    for _ in range(steps):
        md=(lo+hi)/2
        val=fn(md)
        if (val<0)==inc:lo=md
        else:hi=md
    return (lo+hi)/2

def z(t):
    return bisect(lambda u:P(u,t),.5,1.)

def Tstar(t):
    return 1/D(z(t),t)

def U(t,T):
    Tc=3/(6+8*t)
    if T<=Tc:return 1.
    return bisect(lambda u:D(u,t)-1/T,0.,1.)

def outbreak(t,T):
    u=U(t,T)
    return 1-G0(u,t)

z0,z1=z(0.),z(.5)
TL,TU=Tstar(.5),Tstar(0.)
chk(.556693094<z0<.556693096,'z(0)')
chk(.660044216<z1<.660044219,'z(1/2)')
chk(.503512761<TL<.503512764,'lower threshold')
chk(.642387379<TU<.642387382,'upper threshold')
chk(.3<TL<TU<1,'threshold order')

for k in range(100):
    t=k/198
    chk(z(t) > .5, 'root above one half')
    if k>0:
        chk(z(t)>z((k-1)/198),'root increasing')
        chk(Tstar(t)<Tstar((k-1)/198),'threshold decreasing')
    chk(abs(P(z(t),t))<2e-12,'stationary root residual')

# Numerically independent fixed-point iteration from zero for interior cases.
for T in [.35,.4,.5,.52,.55,.6,.63,.68,.8,1.]:
    for k in range(21):
        t=k/40
        u=U(t,T)
        if u<1-1e-7:
            x=0.
            for j in range(15000):
                nx=1-T+T*G1(x,t)
                if abs(nx-x)<2e-15:break
                x=nx
            chk(abs(x-u)<2e-10, 'branching fixed point vs iteration')
        chk(-1e-10<=outbreak(t,T)<=1+1e-10, 'outbreak range')

for T in [.32,.4,.49,TL,.52,.55,.6,.64,TU,.7,.9,1.]:
    # Find maximizer among 2001 samples, compare to structural claim.
    yy=[outbreak(j/4000,T) for j in range(2001)]
    best=max(yy); arg=yy.index(best)/4000
    if T<=TL: chk(abs(arg-.5)<.001, 'lower phase endpoint optimum')
    elif T>=TU: chk(arg<.001, 'upper phase endpoint optimum')
    else:
        tstar=bisect(lambda t:Tstar(t)-T,0.,.5,inc=False)
        chk(abs(arg-tstar)<.001, 'interior optimum location')
    chk(best>0,'nontrivial outbreak in test window')

# Check sign of exact derivative and finite-difference derivative far from transition.
for T in [.4,.53,.58,.63,.72]:
    for j in range(1,50):
        t=j/100
        u=U(t,T)
        if u>.9999:continue
        deriv=(1+u)*P(u,t)/(3*Fu(u,t))
        h=1e-5
        fd=(outbreak(t+h,T)-outbreak(t-h,T))/(2*h)
        chk(abs(fd-deriv)<4e-5, 'derivative vs central difference')

print('PASS', checks, 'assertions')
print('z0=',format(z0,'.15f'),'z_half=',format(z1,'.15f'))
print('T_low=',format(TL,'.15f'),'T_high=',format(TU,'.15f'))
