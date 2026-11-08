#!/usr/bin/env python3
"""Independent arithmetic checks for the quadratic NGN one-step envelope.

The analytic argument in RESULT.md proves the all-dimensional theorem; these
finite exact and numerical tests only test its formulas and boundary cases.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def exact_ratio(a, b, xa2, xb2, s):
    """Objective factor for diagonal Hessian diag(a,b); squared coordinates."""
    A = a*xa2+b*xb2
    B = a*a*xa2+b*b*xb2
    alpha = s*A/(A+s*B)
    Aplus = a*xa2*(1-alpha*a)**2 + b*xb2*(1-alpha*b)**2
    return Aplus/A


def envelope(a, b, s):
    a, b, s = float(a), float(b), float(s)
    if abs(a-b) < 1e-13:
        return (1+s*a)**-2, a
    m0 = (s*(a+b)+2*s*s*a*b-2)/(s*(2+s*(a+b)))
    m = max(a, min(b, m0))
    q = (1+s*s*(m-a)*(b-m))/(1+s*m)**2
    return q, m


def actual_ratio(spec, vec, s):
    A = sum(lam*z*z for lam,z in zip(spec,vec))
    B = sum(lam*lam*z*z for lam,z in zip(spec,vec))
    alpha = s*A/(A+s*B)
    Ap = sum(lam*z*z*(1-alpha*lam)**2 for lam,z in zip(spec,vec))
    mean = B/A
    second = sum(lam**3*z*z for lam,z in zip(spec,vec))/A
    identity = (1+s*s*(second-mean*mean))/(1+s*mean)**2
    return Ap/A, identity


def main():
    tests=0
    # 100% exact rational counterexample: NGN increases the objective.
    a,b,s=F(1),F(10),F(2)
    q=exact_ratio(a,b,F(950),F(13),s)
    assert q==F(41,31) and q>1
    tests+=1
    # Exact rational checks on endpoint mixtures, including single eigenmodes.
    for aa in [F(1),F(2,3),F(5,2)]:
        for bb in [aa,2*aa,5*aa,10*aa,20*aa]:
            for ss in [F(1,100),F(1,4),F(1),F(4),F(20)]:
                for t in range(21):
                    w=F(t,20)
                    if w==0: xa2=F(0);xb2=F(1)
                    elif w==1: xa2=F(1);xb2=F(0)
                    else: xa2=w/aa;xb2=(1-w)/bb
                    A=aa*xa2+bb*xb2
                    m=(aa*aa*xa2+bb*bb*xb2)/A
                    formula=(1+ss*ss*(m-aa)*(bb-m))/(1+ss*m)**2
                    assert exact_ratio(aa,bb,xa2,xb2,ss)==formula
                    tests+=1
    # Exact endpoint extremizers establish the optimal regularization law.
    for aa in [F(1,3),F(1),F(7,2)]:
        for bb in [2*aa,3*aa,7*aa,20*aa]:
            ss=2*(aa+bb)/(bb-aa)**2
            xa2=bb/(aa*(aa+bb))
            xb2=aa/(bb*(aa+bb))
            best=(bb-aa)**2/(bb+aa)**2
            assert exact_ratio(aa,bb,xa2,xb2,ss)==best
            tests+=1
    # Exact rational interior-envelope cases and endpoint boundary checks.
    for aa,bb in [(F(1),F(3)),(F(1),F(6)),(F(2),F(19))]:
        for ss in [F(1,10),F(1,2),F(1),F(3),F(50)]:
            m=(ss*(aa+bb)+2*ss*ss*aa*bb-2)/(ss*(2+ss*(aa+bb)))
            if m<aa:m=aa
            if m>bb:m=bb
            wa=(bb-m)/(bb-aa)
            wb=1-wa
            xa2=wa/aa
            xb2=wb/bb
            q=(1+ss*ss*(m-aa)*(bb-m))/(1+ss*m)**2
            assert exact_ratio(aa,bb,xa2,xb2,ss)==q
            if aa<m<bb:
                closed=(4+ss*ss*(bb-aa)**2)/(4*ss*(aa+bb+aa*bb*ss))
                assert q==closed
                tests+=1
            tests+=1
    # Random diagonal spectra: the exact objective is bounded by the envelope.
    r=Random(20261101)
    for t in range(12000):
        n=r.randrange(2,15)
        a=10**r.uniform(-1,1)
        k=10**r.uniform(0,2)
        b=a*k
        spec=[a,b]+[r.uniform(a,b) for _ in range(n-2)]
        vec=[r.gauss(0,1) for _ in range(n)]
        s=10**r.uniform(-3,3)
        actual, identity=actual_ratio(spec,vec,s)
        upper,m=envelope(a,b,s)
        assert abs(actual-identity)<5e-12*max(1,actual)
        assert actual<=upper+5e-11*max(1,upper)
        # Spectral endpoint weights recover sharp envelope.
        wa=(b-m)/(b-a) if b!=a else 1
        wb=1-wa
        z1=sqrt(wa/a)
        z2=sqrt(wb/b) if b!=a else 0
        got,_=actual_ratio([a,b],[z1,z2],s)
        assert abs(got-upper)<5e-10*max(1,upper)
        tests+=3
    # Verification of sharp regularization and entrance thresholds.
    for k in [1.01,1.25,2,3,5,3+2*sqrt(2),6,10,20,100]:
        a,b=1.0,k
        for s in [0.0001,0.01,0.1,0.5,1,10,100,10000]:
            q,m=envelope(a,b,s)
            if k <= 3+2*sqrt(2)+1e-9:
                assert q<=1+1e-10
            tests+=1
        if k>3+2*sqrt(2)+1e-8:
            critical=2/(a+b-2*sqrt(2*a*b))
            qc,_=envelope(a,b,critical)
            assert abs(qc-1)<2e-12
            assert envelope(a,b,critical*.99)[0]<1
            assert envelope(a,b,critical*1.01)[0]>1
            tests+=3
        if k>1:
            entrance=(-1+sqrt(1+8*a/(b-a)))/(2*a)
            qm,mm=envelope(a,b,entrance)
            assert abs(mm-a)<3e-9
            assert abs(qm-(1+a*entrance)**-2)<3e-11
            tests+=2
    print('PASS:',tests,'exact-rational / deterministic numerical assertions')
    print('Exact counterexample objective factor:',q if False else F(41,31))
    print('Sharp threshold at a=1, b=10:',2/(11-2*sqrt(20)))

if __name__=='__main__':
    main()
