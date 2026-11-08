#!/usr/bin/env python3
"""Standalone exact-arithmetic checks for a finite-step-size sampling theorem.
Only finite identities are tested; the global proof is analytic.
"""
from fractions import Fraction as Q
from itertools import product
from math import isclose, sqrt


def stationary(a, r, p, eta):
    m = len(a)
    bar_a = sum(a) / m
    C = 2 * m * m * bar_a / eta
    S = sum(ai*ai/pi for ai, pi in zip(a, p))
    assert C > S, (C,S)
    return sum(ri*ri/pi for ri, pi in zip(r,p))/(C-S)


def recur(a,r,p,eta):
    m=len(a)
    q=[1-eta*ai/(m*pi) for ai,pi in zip(a,p)]
    v=[-eta*ri/(m*pi) for ri,pi in zip(r,p)]
    mean=sum(pi*qi for pi,qi in zip(p,q))
    noise=sum(pi*vi for pi,vi in zip(p,v))
    rho=sum(pi*qi*qi for pi,qi in zip(p,q))
    sig=sum(pi*vi*vi for pi,vi in zip(p,v))
    return mean,noise,rho,sig


def exact_example():
    a=[Q(1),Q(1),Q(10)]; r=[Q(1),Q(-1),Q(0)]; eta=Q(2,9)
    pstar=[Q(2,9),Q(2,9),Q(5,9)]
    punif=[Q(1,3)]*3
    Vstar=stationary(a,r,pstar,eta)
    Vunif=stationary(a,r,punif,eta)
    assert Vstar==Q(1,15)
    assert Vunif==Q(1,3)
    assert Vunif/Vstar==5
    assert recur(a,r,pstar,eta)==(Q(1,9),Q(0),Q(7,27),Q(4,81))
    assert recur(a,r,punif,eta)==(Q(1,9),Q(0),Q(73,81),Q(8,243))
    assert sum(ai*ai/pi for ai,pi in zip(a,pstar)) == 189
    assert sum(ai*ai/pi for ai,pi in zip(a,punif)) == 306
    # The optimizer equality is checked algebraically in Q at eta=2/9:
    assert [ri*ri+Vstar*ai*ai for ai,ri in zip(a,r)] == [Q(16,15),Q(16,15),Q(20,3)]
    assert [pstar[i]*pstar[i]/(r[i]*r[i]+Vstar*a[i]*a[i]) for i in range(3)] == [Q(5,108)]*3
    assert Q(72)/eta*Vstar == sum((ri*ri+Vstar*ai*ai)/pi for ri,ai,pi in zip(r,a,pstar))
    return 11


def perturbation_exhaustive():
    # rational grid of feasible full-support distributions for the exact example,
    # checking global-optimum inequality at 2/9 without numerical tolerances.
    a=[Q(1),Q(1),Q(10)]; r=[Q(1),Q(-1),Q(0)]; eta=Q(2,9)
    examined=0; stable=0
    for den in [9, 18, 27, 36, 45, 54, 72, 81]:
        for j in range(1,den):
            for k in range(1,den-j):
                p=[Q(j,den),Q(k,den),Q(den-j-k,den)]
                examined+=1
                C=Q(324)
                S=sum(ai*ai/pi for ai,pi in zip(a,p))
                if S>=C:continue
                stable+=1
                assert stationary(a,r,p,eta)>=Q(1,15)
    return examined,stable


def general_identity_cases():
    # finite selection from noninterpolating m-component models; each exact V
    # equals the covariance recursion fixed point where stable.
    cases=0
    for a in ([1,1], [1,2,4], [2,3,4,5], [1,4,9]):
        m=len(a); abar=Q(sum(a),m)
        r=[Q(i) for i in range(1,m)] + [-Q(m*(m-1),2)]
        assert sum(r)==0
        for w in product([1,2,3], repeat=m):
            p=[Q(x,sum(w)) for x in w]
            for eta in [Q(1,50),Q(1,20)]:
                C=2*m*m*abar/eta; S=sum(Q(ai*ai)/pi for ai,pi in zip(a,p))
                if C<=S:continue
                v=stationary([Q(x) for x in a],r,p,eta)
                mean,bias,rho,sig=recur([Q(x) for x in a],r,p,eta)
                assert bias == 0 and mean == 1-eta*abar
                assert sig == (1-rho)*v
                cases+=1
    return cases


def asymptotic_formula():
    # sample exact symbolic/numeric threshold for the symmetric triple
    count=0
    for j in range(1,100):
        eta=Q(j,200)
        p3=5*sqrt(float(eta))/(3*sqrt(2))
        p1=(1-p3)/2
        a=[1.,1.,10.];r=[1.,-1.,0.];p=[p1,p1,p3]
        V=stationary(a,r,p,float(eta))
        C=72/float(eta)
        lhs=(sum(sqrt(ri*ri+V*ai*ai) for ai,ri in zip(a,r)))**2
        assert isclose(lhs, C*V,rel_tol=1e-10,abs_tol=1e-10)
        assert p3>0 and p1>0
        count+=1
    return count

if __name__=='__main__':
    n=exact_example()
    inspected,stable=perturbation_exhaustive()
    cases=general_identity_cases()
    examples=asymptotic_formula()
    print(f"PASS: {n} exact example identities; {inspected} rational grid candidates ({stable} stable); {cases} independent exact rational covariance identities; {examples} floating-point root consistency checks")
