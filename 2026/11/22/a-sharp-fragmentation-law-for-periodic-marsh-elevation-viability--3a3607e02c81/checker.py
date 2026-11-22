#!/usr/bin/env python3
"""Independent checks for a piecewise-constant, quadratically regulated marsh-margin model.

Run with: python checker.py
Requires Python 3, mpmath, scipy; no remote access required.
"""
import math
from fractions import Fraction
import mpmath as mp
from scipy.integrate import solve_ivp

mp.mp.dps=65
checks=0

def verify(cond,tag):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(tag)

def threshold(p,q,L,n):
    return n/mp.mpf(q)*mp.atan(mp.mpf(p)/q*mp.tanh(mp.mpf(p)*L/n))

def maps(p,q,L,T,n,z):
    l=L/n; b=T/n
    U=mp.tanh(p*l); V=mp.tan(q*b)
    g=p*(z+p*U)/(p+z*U)
    f=(g-q*V)/(1+(g/q)*V)
    return g,f

def fixed_point(p,q,L,T,n):
    l=L/n; b=T/n
    U=mp.tanh(p*l); V=mp.tan(q*b)
    C=U+(p/q)*V
    alpha=U*V*(p*p+q*q)/q
    beta=p*(p*U-q*V)
    return 2*beta/(alpha+mp.sqrt(alpha*alpha+4*C*beta))

# Functional identities and order boundaries, testing both high and low contrasts.
for p,q,L in [(mp.mpf('0.5'),mp.mpf('2'),mp.mpf('0.3')),
              (mp.mpf('1'),mp.mpf('1'),mp.mpf('1')),
              (mp.mpf('3'),mp.mpf('0.7'),mp.mpf('2')),
              (mp.mpf('4'),mp.mpf('5'),mp.mpf('0.8'))]:
    prev=mp.mpf('0')
    for n in [1,2,3,4,5,8,16,32,64,128]:
        Tc=threshold(p,q,L,n)
        verify(Tc>prev,'strictly increasing threshold')
        verify(Tc<p*p*L/(q*q),'strictly below mean-field threshold')
        verify(Tc<mp.pi*n/(2*q),'adverse phase under first pole')
        prev=Tc
        for fraction in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.999')]:
            T=fraction*Tc
            root=fixed_point(p,q,L,T,n)
            verify(root>0,'positive fixed point')
            g,f=maps(p,q,L,T,n,root)
            verify(abs(f-root)<mp.mpf('1e-57')*(1+abs(root)),'fixed-point exact map')
            verify(g>root,'minimum at end of adverse phase')
            U=mp.tanh(p*L/n); V=mp.tan(q*T/n)
            C=U+p*V/q
            alpha=U*V*(p*p+q*q)/q
            beta=p*(p*U-q*V)
            verify(abs(C*root**2+alpha*root-beta)<mp.mpf('1e-57')*(1+abs(root)),'quadratic identity')
        # Exact mean-positive yet finite-death regime for any n.
        Tbad=(Tc+p*p*L/(q*q))/2
        verify(Tbad>Tc and Tbad<p*p*L/(q*q),'mean-positive extinction window')
        if q*Tbad/n<mp.pi/2:
            U=mp.tanh(p*L/n); V=mp.tan(q*Tbad/n)
            C=U+p*V/q
            alpha=U*V*(p*p+q*q)/q
            beta=p*(p*U-q*V)
            verify(beta<0 and alpha>0 and C>0,'no positive fixed point quadratic')

# Strict concavity and high-frequency asymptotic coefficient.
for p,q,L in [(mp.mpf('1'),mp.mpf('1'),mp.mpf('1')),
              (mp.mpf('2'),mp.mpf('3'),mp.mpf('0.7')),
              (mp.mpf('5'),mp.mpf('1'),mp.mpf('2'))]:
    limit=p*p*L/(q*q)
    coefficient=p**4*(p*p+q*q)*L**3/(3*q**4)
    for n in [40,80,160,320,640]:
        deficit=limit-threshold(p,q,L,n)
        scaled=n*n*deficit
        verify(abs(scaled-coefficient)<10*coefficient/n**2*(1+(p*L)**2+(p/q)**2)**2,
               'inverse-square penalty controlled')

# Independent ODE integration of each flow, not using their closed-form solution.
for p,q,L,n in [(0.7,1.9,1.2,1),(1.0,1.0,1.0,2),(2.1,0.8,0.8,4),(1.6,1.3,2.5,8)]:
    tc=float(threshold(mp.mpf(str(p)),mp.mpf(str(q)),mp.mpf(str(L)),n))
    for frac in [0.2,0.65,0.94]:
        T=frac*tc
        for z0 in [0.01,0.3,1.5]:
            ga,fa=maps(mp.mpf(str(p)),mp.mpf(str(q)),mp.mpf(str(L)),mp.mpf(str(T)),n,mp.mpf(str(z0)))
            res1=solve_ivp(lambda t,y:[p*p-y[0]**2],[0,L/n],[z0],rtol=1e-12,atol=1e-13)
            res2=solve_ivp(lambda t,y:[-q*q-y[0]**2],[0,T/n],[res1.y[0,-1]],rtol=1e-12,atol=1e-13)
            verify(res1.success and res2.success,'ODE solved')
            verify(abs(float(ga)-res1.y[0,-1])<3e-10,'positive flow agrees with ODE')
            verify(abs(float(fa)-res2.y[0,-1])<3e-10,'negative flow agrees with ODE')

# One explicit counterexample to judging persistence by mean forcing alone.
p=q=L=mp.mpf('1'); n=1
Tc=threshold(p,q,L,n)
T=mp.mpf('0.8')
verify(Tc<T<1,'counterexample lies inside gap')
z=mp.mpf('1'); count=0
while z>0 and count<500:
    z=maps(p,q,L,T,n,z)[1]; count+=1
verify(z<=0 and count<500,'extinction despite positive time-average forcing')
for n in [2,3,5,10]:
    verify(T<threshold(p,q,L,n),'fragmentation restores positive periodic state')

print('PASS checks:',checks)
print('example n1 threshold:',mp.nstr(Tc,18))
print('example n2 threshold:',mp.nstr(threshold(p,q,L,2),18))
print('example adverse duration:',T,'mean forcing numerator:',p*p*L-q*q*T)
print('finite extinction iterations in coarse case:',count)
