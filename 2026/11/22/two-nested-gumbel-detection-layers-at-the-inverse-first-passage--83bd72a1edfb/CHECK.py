#!/usr/bin/env python3
"""Standalone finite checks of a variable-diffusivity inverse hitting-time law.

The continuum assertions in the accompanying theorem use analysis, not these tests.
"""
import math

checks=0

def close(actual, expected, tol=2.e-10):
    global checks
    assert math.isfinite(actual) and math.isfinite(expected)
    assert abs(actual-expected) <= tol*max(1.0,abs(actual),abs(expected)), (actual,expected)
    checks+=1

def rates(x, delta, a, b, A, d0):
    z=1.0+x
    ell=1.0+math.log(z)
    ac=2.0+delta
    k=1.0/(d0*A*a)
    D=d0*z**(-delta)
    DT=D*(-delta/z)
    tp=A*a*z**(a-1.0)*ell**b
    logder=(a-1.0)/z+b/(z*ell)
    tpp=tp*logder
    Wp=1.0/(D*tp)
    Up=(-delta/z)+logder+Wp
    gap=ac-a
    if b==0.0 and gap!=0.0:
        W=k*math.expm1(gap*math.log(z))/gap
        W_inf=math.inf if gap>0 else -k/gap
        tail=math.inf if gap>0 else -k/gap*z**gap
    elif gap==0.0:
        if b==1.0:
            W=k*math.log(ell)
            tail=math.inf
        else:
            W=k*(ell**(1.0-b)-1.0)/(1.0-b)
            tail=math.inf if b<1 else k*ell**(1.0-b)/(b-1)
    else:
        raise ValueError('only b=0 away from the critical exponent')
    h=1.0 if math.isinf(tail) else -math.expm1(-tail)
    hp=0.0 if math.isinf(tail) else -math.exp(-tail)*Wp
    Tprime=tp*h
    Tpp=tpp*h+tp*hp
    L_T=D*Tpp+(DT-D*Up)*Tprime
    return dict(D=D,tp=tp,tpp=tpp,W=W,Wp=Wp,Up=Up,
                h=h,hp=hp,Tprime=Tprime,Tpp=Tpp,L_T=L_T,tail=tail)

for delta in (0.3,1.0,1.7):
    ac=2+delta
    for a,b in ((1.5,0.),(ac-.35,0.),(ac,0.),(ac,1.),(ac,2.),(ac,3.),(ac+.5,0.),(ac+1.4,0.)):
        for x in (0.,0.01,.2,1.,4.,30.,500.):
            d=rates(x,delta,a,b,1.3,0.7)
            close(d['Wp'],1.0/(d['D']*d['tp']))
            close(d['L_T'],-1.,tol=2.e-9)
            close(d['hp'],0.0 if math.isinf(d['tail']) else -math.exp(-d['tail'])*d['Wp'])
            close(d['Tprime'],d['tp']*d['h'])
            if a<ac or a==ac and b<=1:
                close(d['h'],1.)

# Exact closed-form clipping and its universal amplitude at large distance.
for delta in (0.5,1.,2.):
    ac=2.+delta
    for a in (ac+.2,ac+1.,ac+2.5):
        for A in (.3,1.,3.):
            for x in (1.e10,1.e15):
                d=rates(x,delta,a,0.,A,.8)
                expected=(1.+x)**(ac-1.)/(.8*(a-ac))
                # Distinguish the finite-distance correction from limiting equivalence.
                close(d['Tprime']/expected,1.,tol=.060)

# Exact marginal logarithmic clipping formula, with no numerical tail integration.
for delta in (.5,1.3):
    ac=2.+delta
    for b in (1.2,2.,3.5):
        for A in (20.,50.):
            for x in (1.e6,1.e10):
                d=rates(x,delta,ac,b,A,1.1)
                expected=(1.+x)**(ac-1.)*(1+math.log1p(x))/(1.1*(b-1.))
                close(d['Tprime']/expected,1.,tol=.035)

# At the superquadratic critical pure-power profile, the potential is globally
# logarithmic and the target mean hitting time is realized exactly.
for delta in (.1,1.,3.):
    ac=2.+delta
    for x in (.01,1.,20.,300.):
        d=rates(x,delta,ac,0.,2.,1.)
        close(d['Up'],(1.+1./(2.*ac))/(1.+x))
        close(d['Tprime'],2.*ac*(1+x)**(ac-1.))

# Boundary against the constant-diffusion cubic counterexample.
for x in (.5,4.,20.):
    d=rates(x,0.,3.,0.,1.,1.)
    close(d['Tprime'],3.*(1+x)**2*(-math.expm1(-1./(3.*(1.+x)))))

# Dual critical transition layers: compute in logarithmic position coordinates,
# avoiding astronomical distances that needlessly overflow floating point.
for delta in (.3,1.,2.):
    ac=2.+delta
    for A in (.2,1.,6.):
        kc=1./(.9*A*ac)
        for s in (-4.,-2.,0.,1.,3.):
            for eps in (.02,.1,.4):
                ke=1./(.9*A*(ac+eps))
                logz=(math.log(1./eps)+s)/eps
                Q=ke/eps*math.exp(-eps*logz)
                close(math.exp(-Q),math.exp(-ke*math.exp(-s)))
            for eta in (.02,.1,.4):
                logell=(math.log(1./eta)+s)/eta
                Q=kc/eta*math.exp(-eta*logell)
                close(math.exp(-Q),math.exp(-kc*math.exp(-s)))

print(f'PASS: {checks} finite checks of generator, boundary correction, phase classes and clipping derivatives.')
