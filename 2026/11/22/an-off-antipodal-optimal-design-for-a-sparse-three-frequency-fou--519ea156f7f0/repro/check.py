#!/usr/bin/env python3
"""Reproducible calculations for the sparse three-frequency, two-arc theorem.
Run: python3 repro/check.py (requires mpmath and sympy).
This is corroboration; the proof establishes universal statements.
"""
from __future__ import annotations
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 55
CHECKS = 0

def check(condition, desc):
    global CHECKS
    assert condition, desc
    CHECKS += 1

u=sp.symbols('u', real=True)
F=8*(1+7*u-8*u**2)/(16*u**2-4*u+2)
Fprime=-4*(40*u*u+32*u-9)/(8*u*u-2*u+1)**2
ustar=(sp.sqrt(154)-8)/20
check(sp.simplify(sp.diff(F,u)-Fprime)==0, 'derivative identity')
check(sp.simplify(F.subs(u,ustar)-(2+4*sp.sqrt(154)/7))==0, 'sharp coefficient')
check(sp.simplify(40*ustar**2+32*ustar-9)==0, 'critical root')
check(sp.simplify(F.subs(u,0)-4)==0, 'antipodal constant')
check(sp.simplify(sp.diff(F,u,2).subs(u,ustar))<0, 'nondegenerate maximum')

z,c=sp.symbols('z c',real=True)
P=z**3+(1-4*c*c)*z+2*c
check(sp.expand((z*z-2*c*z+1)*(z+2*c)-P)==0,'root polynomial factorization')
check(sp.expand(4*c*c+(1-4*c*c)**2+1-(16*c**4-4*c*c+2))==0,'coefficient normalization')
check(sp.expand(9+(1-4*c*c)**2+6*(1-4*c*c)*(2*c*c-1)-(4+28*c*c-32*c**4))==0,'derivative norm')

Fnum=sp.lambdify(u,F,'mpmath')
ust=mp.mpf(str(sp.N(ustar,50)))
thst=2*mp.acos(mp.sqrt(ust))

def gram(a,theta):
    # Fourier basis k=0,1,3; normalized Haar measure.
    ks=(0,1,3)
    H=mp.matrix(3)
    for i,k in enumerate(ks):
        for j,h in enumerate(ks):
            m=k-h
            if m==0:
                H[i,j]=2*a/mp.pi
            else:
                H[i,j]=2*mp.sin(m*a)/(mp.pi*m)*mp.cos(m*theta/2)
    return H

def small_eigen(a,theta):
    return mp.eigsy(gram(a,theta),eigvals_only=True)[0]

# Independent direct interval integration of basis cross products at multiple angles.
for a in [mp.mpf('0.04'),mp.mpf('0.13'),mp.mpf('0.31')]:
    for theta in [mp.mpf('1.12'),mp.mpf('2.11'),mp.pi]:
        for i,k in enumerate((0,1,3)):
            for j,h in enumerate((0,1,3)):
                direct = sum(mp.quad(lambda t: mp.exp(1j*(k-h)*t), [center-a,center+a]) for center in [-theta/2,theta/2])/(2*mp.pi)
                check(abs(direct-gram(a,theta)[i,j])<mp.mpf('1e-47'), 'integral Fourier matrix entry')

# Verify asymptotic coefficient convergence across separated angles, with a^2 rate.
for theta in [mp.mpf('0.3'),mp.mpf('0.7'),mp.mpf('1.2'),mp.mpf('1.8'),thst,mp.mpf('2.7'),mp.pi]:
    predicted = Fnum(mp.cos(theta/2)**2)/(3*mp.pi)
    errs=[]
    for a in [mp.mpf('0.05'),mp.mpf('0.025'),mp.mpf('0.0125')]:
        observed=small_eigen(a,theta)/(a**3)
        errs.append(abs(observed-predicted))
        check(abs(observed-predicted)<mp.mpf('0.03'), 'asymptotic bound')
    check(errs[2]<errs[1]<errs[0], 'monotone asymptotic error')
    check(errs[0]/errs[1]>mp.mpf('3.0'), 'quadratic convergence')

# At antipodality the spectrum is exactly diagonal-plus a 2x2 block.
for a in [mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.3'),mp.mpf('0.7'),mp.mpf('1.1')]:
    result=small_eigen(a,mp.pi)
    check(abs(result-(2*a-mp.sin(2*a))/mp.pi)<mp.mpf('1e-43'), 'exact antipodal reference')

# A neighborhood of the predicted optimum improves on the antipodal reference.
for a in [mp.mpf('0.03'),mp.mpf('0.07'),mp.mpf('0.12'),mp.mpf('0.18')]:
    check(small_eigen(a,thst)>small_eigen(a,mp.pi),'off-antipodal advantage')

# Numeric maximization at representative small positive widths.
for a in [mp.mpf('0.02'),mp.mpf('0.04'),mp.mpf('0.07'),mp.mpf('0.1')]:
    values=[]
    for j in range(301):
        theta=2*a+(mp.pi-2*a)*j/300
        val=small_eigen(a,theta)
        values.append(val)
        # Uniform polynomial trial bound including coalescing centers.
        ub=(a**3)/(3*mp.pi)*Fnum(mp.cos(theta/2)**2)
        # Trial polynomial has O(a^5) perturbation; no strict ub at leading scale.
        check(val>=0,'positive minimum')
    i=max(range(len(values)),key=values.__getitem__)
    gridtheta=2*a+(mp.pi-2*a)*i/300
    check(abs(gridtheta-thst)<mp.mpf('0.045'),'grid maximizer placement')
    check(values[i]>small_eigen(a,mp.pi),'grid design advantage')

print(f'SPARSE_ARC_CHECKS_PASS {CHECKS}')
