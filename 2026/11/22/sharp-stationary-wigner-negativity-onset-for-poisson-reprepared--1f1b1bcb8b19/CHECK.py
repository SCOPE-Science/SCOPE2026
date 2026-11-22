#!/usr/bin/env python3
"""Reproduce numerical checks for a Poisson-reprepared odd optical cat.
No external dependencies; the infinite-parameter theorem rests on the proof,
not on these finite integrations. Run with Python 3.10+.
"""
import math

N_CHECKS = 0

def check(condition, what):
    global N_CHECKS
    assert condition, what
    N_CHECKS += 1

def simpson(f, n=800):
    assert n > 0 and n % 2 == 0
    h = 1.0 / n
    s = f(0.0) + f(1.0)
    for j in range(1, n):
        s += (4 if j % 2 else 2) * f(j*h)
    return s*h/3

def I(A,k,n=1200):
    # eta = t**(1/k) turns the stationary Beta(k,1) law into uniform dt.
    return simpson(lambda t: math.exp(-2*A*t**(1/k))-math.exp(-2*A*(1-t**(1/k))),n)

def F(A,k,x,y,n=400):
    def f(t):
        eta=t**(1/k)
        tA=math.sqrt(A*eta)
        return (math.exp(-2*A*eta)*math.cosh(4*x*tA) -
                math.exp(-2*A*(1-eta))*math.cos(4*y*tA))
    return simpson(f,n)

def W(A,k,x,y,n=400):
    return (2/(math.pi*(-math.expm1(-2*A))) *
            math.exp(-2*(x*x+y*y))*F(A,k,x,y,n))

def J(A,n=2000):
    def f(t):
        if t == 0 or t == 1: return 0.0
        eta=t*t
        return 4*t*math.log(t)*(math.exp(-2*A*eta)-math.exp(-2*A*(1-eta)))
    return simpson(f,n)

def coeff(A):
    a=2*A
    B1=(1-(1+a)*math.exp(-a))/(a*a)
    B2=(a-1+math.exp(-a))/(a*a)
    j=J(A)
    return j*j/(8*A*(-math.expm1(-a))*math.sqrt(B1*B2)),B1,B2,j

def negative_volume(A,k,n_side=100,n_age=128):
    C,b1,b2,j=coeff(A)
    eps=k-1
    xradius=math.sqrt(-j*eps/(8*A*b1))
    yradius=math.sqrt(-j*eps/(8*A*b2))
    # A factor 1.7 encloses the small negative island, checked at the boundary.
    xmax=1.7*xradius
    ymax=1.7*yradius
    s=0.0
    for i in range(n_side):
        x=-xmax+(i+0.5)*2*xmax/n_side
        for j in range(n_side):
            y=-ymax+(j+0.5)*2*ymax/n_side
            s+=max(0.0,-W(A,k,x,y,n_age))
    return s*4*xmax*ymax/(n_side*n_side)

if __name__=='__main__':
    for A in (0.08,0.25,1.0,4.0):
        for k in (0.3,0.7,0.99,1.0,1.01,1.4,3.0):
            val=I(A,k)
            check(val > 1e-5 if k<1 else (val < -1e-5 if k>1 else abs(val)<5e-9),
                  f'origin classification A={A}, k={k}: {val}')
            check(abs(W(A,k,0,0,n=1200)-2*val/(math.pi*(-math.expm1(-2*A))))<1e-8,
                  'Wigner normalization')
    # Independent Fock-parity representation of the odd cat.  A pure-loss
    # channel maps the parity generating function to sinh(A*(1-2eta))/sinh(A).
    for A in (0.1,0.8,3.0):
        for k in (0.35,0.75,1.0,1.6,3.5):
            parity=simpson(lambda t: math.sinh(A*(1-2*t**(1/k)))/math.sinh(A),1200)
            check(abs(parity-I(A,k)/(1-math.exp(-2*A)))<3e-8,
                  "Fock parity and phase-space Wigner agree")
    for A in (0.2,1.0,4.0):
        for k in (0.5,1.0):
            for x,y in ((0,0),(0.13,0), (0,0.27),(.5,.3),(-.4,.8),(1.,-1.)):
                v=W(A,k,x,y)
                check(v>-1e-7,'nonnegative for k <=1')
                if k==1 and (x!=0 or y!=0):
                    check(v>1e-6,'unique zero for k=1')
    for A in (.1,1.0,4.0):
        C,b1,b2,j=coeff(A)
        check(C>0 and b1>0 and b2>0 and j<0,'coefficient signs')
        check(abs(b1-simpson(lambda t:t*math.exp(-2*A*t)))<1e-7,'B1 independent quadrature')
        check(abs(b2-simpson(lambda t:t*math.exp(-2*A*(1-t))))<1e-7,'B2 independent quadrature')
        check(abs((I(A,1+1e-4)-I(A,1-1e-4))/(2e-4)-j)<3e-5,'critical derivative')
    # Compare directly integrated Wigner-negative phase-space volume with
    # the predicted coefficient; this is numerical evidence only.
    for eps in (.04,.02):
        C,*_=coeff(1.0)
        vol=negative_volume(1.0,1+eps)
        check(abs(vol/(C*eps*eps)-1)<0.13, f'negative-volume onset eps={eps}: {vol/(C*eps*eps)}')
    print(f'PASS {N_CHECKS} numerical assertions')
    for A in (.1,1.,4.):
        C,*_=coeff(A)
        print('A=',A,'onset coefficient=',round(C,12))
