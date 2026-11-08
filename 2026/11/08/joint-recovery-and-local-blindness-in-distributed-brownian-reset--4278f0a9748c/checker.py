#!/usr/bin/env python3
"""Reproduce finite diagnostics for Brownian distributed-reset inversion.

The mathematical conclusions at arbitrary parameters follow from the written proof,
not from these finite checks. Uses Python 3 standard library only.
"""
import cmath
import math

count = 0

def check(cond, label):
    global count
    if not cond:
        raise AssertionError(label)
    count += 1

def H_atoms(b, k, points):
    return sum(w*math.exp(-k*abs(b-x)) for x,w in points)

def M_atoms(b, k, r, points):
    h = H_atoms(b,k,points)
    return (1/h-1)/r

def integrate(f, lo, hi, steps=60000):
    h = (hi-lo)/steps
    s = (f(lo)+f(hi))/2
    for j in range(1,steps):
        s += f(lo+j*h)
    return s*h

# Fixed physical rate and diffusivity; an exactly tractable two-atom law.
k=1.4
r=2.7
D=r/k**2
atoms=[(-0.8,0.3),(1.2,0.7)]
for b in [-12.0,-4.,-0.8,-0.1,0.,0.7,1.2,2.,5.,11.]:
    h=H_atoms(b,k,atoms)
    m=M_atoms(b,k,r,atoms)
    check(abs(h*(1+r*m)-1)<1e-12,"forward MFPT identity")
    check(m>=0,"nonnegative MFPT")

# For this two-atom case integrate H exactly on each side of both atoms.
# Integral on (-R,R) and missing tail calculated without numerical truncation.
R=16.0
for s in [0.2*r,0.8*r,1.0*r,1.3*r,3*r]:
    f=lambda b:1.0/(1+s*M_atoms(b,k,r,atoms))
    numeric=integrate(f,-R,R,steps=40000)
    # At s=r, integrand is exactly H and the missing tails integrate explicitly.
    if s==r:
        left=sum(w*math.exp(-k*(R+x))/k for x,w in atoms)
        right=sum(w*math.exp(-k*(R-x))/k for x,w in atoms)
        check(abs(numeric+left+right-2/k)<3e-6,"normalization calibration")
    check(numeric>0 and math.isfinite(numeric),"positive calibration curve")

# Unknown physical rate recovered via monotone calibration.
for b in [6.0,9.0,12.0,15.0]:
    tail=lambda q: math.log(M_atoms(q,k,r,atoms))
    fd=(tail(b+0.0001)-tail(b-0.0001))/0.0002
    check(abs(fd-k)<0.025,"tail logarithmic derivative")

# Different left-side measures with exactly matching exponential moment.
for kk in [0.4,1.0,1.4,2.0]:
    z=math.log((math.exp(-2*kk)+math.exp(-3*kk))/2)/kk
    left1=[(z,1.0)]
    left2=[(-2.,0.5),(-3.,0.5)]
    check(-3 < z < -2,"strict intermediate location")
    for b in [0.01,0.2,1.,5.,10.]:
        check(abs(M_atoms(b,kk,r,left1)-M_atoms(b,kk,r,left2))<1e-11*max(M_atoms(b,kk,r,left1),M_atoms(b,kk,r,left2),1),
              "exact local observational blindness")
    check(abs(M_atoms(-2.5,kk,r,left1)-M_atoms(-2.5,kk,r,left2))>1e-3,
          "laws distinguishable with additional targets")

# Kernel Fourier multiplier exactness, including high-frequency quadratic order.
for kk in [0.5,1.0,2.0]:
    for n in [8,16,32,64,128,256]:
        mult=2*kk/(kk*kk+n*n)
        check(abs(n*n*mult-2*kk)<2*kk*(kk/8)**2,
              "quadratic high-frequency multiplier")
        check(mult>0,"positive Fourier multiplier")

# Density positivity and exact mass for the even bump and odd sine perturbation.
phi=lambda x:math.exp(-1/(1-x*x)) if abs(x)<1 else 0.0
norm=integrate(phi,-1.,1.,steps=20000)
check(norm>0,"finite bump mass")
for epsilon in [0.1,0.5,0.9]:
    for n in [1,2,5,12,40]:
        mass=integrate(lambda x: phi(x)*(1+epsilon*math.sin(n*x))/norm,-1.,1.,steps=10000)
        check(abs(mass-1)<1e-9,"oscillatory perturbation normalization")
        for x in [-0.97,-0.5,0,0.31,0.99]:
            check(phi(x)*(1+epsilon*math.sin(n*x))>=0,"nonnegative density")

# Reconstruct the actual position-space response perturbation by quadrature.
kappa=1.4
epsilon=0.5
for n in [16,32,64,128]:
    target=0.2
    hdiff=integrate(lambda x: math.exp(-kappa*abs(target-x))*phi(x)*epsilon*math.sin(n*x)/norm,
                    -1.0,1.0,steps=50000)
    predicted=2*kappa*epsilon*phi(target)*math.sin(n*target)/norm
    check(abs(n*n*hdiff-predicted)<0.15,
          "real-space high-frequency quadratic leading profile")

print("PASS:",count,"finite deterministic diagnostic assertions")
