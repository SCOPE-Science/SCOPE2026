#!/usr/bin/env python3
"""Reproducibility checks for equal-width two-interval Fourier-intensity geometry.
All assertions are finite checks; the general theorems rely on the written proof.
Requires numpy; no network access.
"""
import math
import numpy as np

checks = 0

def require(x, detail):
    global checks
    checks += 1
    if not x:
        raise AssertionError(detail)

def tri(w, t):
    return max(w-abs(t), 0.)

def covar(w, gap, t):
    return 2*tri(w,t)+tri(w,t-(w+gap))+tri(w,t+(w+gap))

def intensity(w,gap,freq):
    if abs(freq) < 1e-15:
        return (2*w)**2
    one=(np.exp(-2j*np.pi*freq*w)-1)/(-2j*np.pi*freq)
    return abs(one*(1+np.exp(-2j*np.pi*freq*(w+gap))))**2

def exact_gap_sq(w,delg):
    h=abs(delg)
    if h<=w:
        return 4*w*h*h-2*h*h*h
    if h<=2*w:
        return 8*w*w*w/3-2*(2*w-h)**3/3
    return 8*w*w*w/3

def metric(w,g):
    m=min(w,g)
    return np.array([[16*w,4*m],[4*m,4*w]])

def covar_jac(w,g,t):
    # Lebesgue a.e. on positive half-axis; negative reflection.
    t=abs(t)
    dw=2*float(0<t<w)+2*float(w+g<t<2*w+g)
    dg=-float(g<t<g+w)+float(g+w<t<g+2*w)
    return np.array([dw,dg],float)

def integrate_piecewise(func, points):
    ps=sorted(set(float(x) for x in points))
    total=0.
    for a,b in zip(ps[:-1],ps[1:]):
        if b<=a: continue
        # four Gauss-Legendre points exact for squared piecewise-affine functions
        xx, ww=np.polynomial.legendre.leggauss(4)
        z=0.5*(b-a)*xx+0.5*(a+b)
        total+=0.5*(b-a)*sum(float(func(v))*u for v,u in zip(z,ww))
    return total

# Global gap-distance formula with exact integration of the *original* covariograms.
for w in [0.19,0.43,1.,1.7,3.1]:
    for g in [0.11*w,0.54*w,1.21*w,2.63*w,8*w]:
        for h in [0.025*w,0.47*w,0.98*w,1.4*w,3.2*w,12.3*w]:
            breaks=[-30*w,30*w,0.,-w,w]
            for x in [g+w,h+w]:
                breaks +=[-x-w,-x,-x+w,x-w,x,x+w]
            actual=integrate_piecewise(lambda x:(covar(w,g,x)-covar(w,h,x))**2,breaks)
            expected=exact_gap_sq(w,g-h)
            require(abs(actual-expected)<8e-10*max(1.,expected),('gap',w,g,h,actual,expected))
            # symmetry, positivity and sharp saturation
            require(abs(exact_gap_sq(w,g-h)-exact_gap_sq(w,h-g))<1e-10,'symmetry')

# Pullback metric via independently integrated derivatives and exact spectrum.
for w in [0.23,0.67,1.,1.83,2.4]:
    for ratio in [0.06,0.3,0.9,1.,1.15,1.9,4.2,10.]:
        g=w*ratio
        breaks=[0.,w,g,g+w,g+2*w,20*w]
        for a in range(2):
            for b in range(2):
                actual=2*integrate_piecewise(lambda t:covar_jac(w,g,t)[a]*covar_jac(w,g,t)[b],breaks)
                expected=metric(w,g)[a,b]
                require(abs(actual-expected)<1e-9*max(1.,abs(expected)),('jac',w,g,a,b,actual,expected))
        expect_eig=sorted([2*(5*w-s) for s in [-math.sqrt(9*w*w+4*min(w,g)**2),math.sqrt(9*w*w+4*min(w,g)**2)]])
        eig=list(np.linalg.eigvalsh(metric(w,g)))
        for a,b in zip(eig,expect_eig):
            require(abs(a-b)<1e-9,'spectrum')
        require(eig[0]>0,'positive')

# Finite differences against *direct* covariogram, after integration.
for w,g in [(0.37,0.15),(0.62,1.18),(1.2,2.75)]:
    breaks=[-20*w,20*w]
    for delta in [2e-3*w,6e-4*w]:
        for direction in [np.array([1.,0.]),np.array([0.,1.]),np.array([0.4,-0.7])]:
            ww,gg=w+delta*direction[0],g+delta*direction[1]
            for W,G in [(w,g),(ww,gg)]:
                breaks += [0., W,G,G+W,G+2*W,-W,-G,-G-W,-G-2*W]
            diff=integrate_piecewise(lambda t:(covar(ww,gg,t)-covar(w,g,t))**2,breaks)
            expect=delta**2*(direction @ metric(w,g) @ direction)
            require(abs(diff-expect)<0.05*max(diff,expect),('finite-difference L2',w,g,delta,direction.tolist(),diff,expect))

# Fourier intensity agrees with analytic formula for its inverse-transform covariogram.
for w,g in [(0.37,0.45),(0.9,1.8),(1.4,0.3)]:
    xi=np.linspace(-200,200,40001)
    F=np.array([intensity(w,g,z) for z in xi])
    for t in [0.,0.37*w,0.8*w,g,0.53*(g+2*w),g+2*w+0.6]:
        inv=float(np.trapezoid(F*np.cos(2*np.pi*xi*t),xi))
        expected=covar(w,g,t)
        require(abs(inv-expected)<2e-3,('Fourier quadrature',w,g,t,inv,expected))

print('PASS',checks,'assertions; tested independent piecewise integration, spectrum, finite differences and Fourier quadrature')
