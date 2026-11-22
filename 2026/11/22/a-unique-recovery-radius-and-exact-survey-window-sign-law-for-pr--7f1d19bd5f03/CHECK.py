"""Finite diagnostic checks for the exponential seed/predator equilibrium theorem.

Standard-library only. These checks support, but do not replace, the analytical proof.
"""
from fractions import Fraction
from math import exp, log, sqrt, isclose
from random import Random


def equilibrium(F, N, mu, a, h):
    # Positive solution of mu*a*h*S^2 + (mu+a*N-a*h*F)*S-F=0.
    A = mu*a*h
    B = mu + a*N - a*h*F
    return 2*F/(B + sqrt(B*B+4*A*F)) if B >= 0 else (
        (-B+sqrt(B*B+4*A*F))/(2*A))


def survival(r, F0, N0, d, n, mu, a, h):
    F = F0*exp(-d*r)
    N = N0*exp(-n*r)
    return mu*equilibrium(F,N,mu,a,h)/F


def threshold_radius(R, n, d):
    assert d > n > 0 and R > 0
    return -expm1(-n*R)/(exp(-n*R)-exp(-d*R))


def expm1(x):
    from math import expm1 as f
    return f(x)


def check():
    count=0
    # Exact source and endpoint equalities in a three-dimensional parameter slice.
    S0 = Fraction(4)
    N0 = Fraction(5)
    F0 = S0+N0*S0/(1+S0)
    assert F0 == Fraction(8); count+=1
    z = Fraction(1,4)  # exp(-n*R); exp(-d*R)=z^2, d=2n.
    SR = z*z*S0
    FR = z*z*F0
    NR = z*N0
    assert FR == SR+NR*SR/(1+SR); count+=1
    assert SR/FR == S0/F0 == Fraction(1,2); count+=1

    sstar=1
    zstar=(5+sqrt(153))/32
    rstar=-2*log(zstar)
    rc=2*log(4)
    assert 0 < rstar < rc; count+=1
    assert isclose(8*zstar*zstar,1+2.5*zstar,rel_tol=1e-13);count+=1
    assert isclose(survival(0,8,5,1,.5,1,1,1),.5,abs_tol=2e-14);count+=1
    assert isclose(survival(rc,8,5,1,.5,1,1,1),.5,abs_tol=2e-14);count+=1
    assert isclose(survival(rstar,8,5,1,.5,1,1,1),1/(8*zstar*zstar),abs_tol=2e-14);count+=1
    assert survival(rstar,8,5,1,.5,1,1,1) < survival(2,8,5,1,.5,1,1,1) < .5;count+=1
    assert survival(5,8,5,1,.5,1,1,1) > .5;count+=1

    # For each randomized case, compare the theorem's analytically predicted
    # derivative sign with a symmetric numerical difference away from a zero.
    rng=Random(50420)
    for j in range(1200):
        F0=10**rng.uniform(-1,1.5)
        N0=10**rng.uniform(-1,1.5)
        mu=10**rng.uniform(-1,1)
        a=10**rng.uniform(-1,1)
        h=10**rng.uniform(-1,1)
        d=rng.uniform(.4,1.7)
        n=rng.uniform(.15,2.0)
        r=rng.uniform(.04,3.)
        F=F0*exp(-d*r); N=N0*exp(-n*r)
        S=equilibrium(F,N,mu,a,h)
        assert isclose(F,mu*S+a*N*S/(1+a*h*S),rel_tol=4e-13);count+=1
        desired=n-(d-n)*a*h*S
        if abs(desired)<1e-4: continue
        eps=2e-5
        difference=survival(r+eps,F0,N0,d,n,mu,a,h)-survival(r-eps,F0,N0,d,n,mu,a,h)
        # Skip near-zero finite-difference effects; the analytic sign is proved in RESULT.md.
        if abs(difference)>2e-11:
            assert difference*desired>0, (j,desired,difference);count+=1
        # Always test the exact endpoint comparison, independently of derivative.
        R=r
        p0=survival(0,F0,N0,d,n,mu,a,h)
        pR=survival(R,F0,N0,d,n,mu,a,h)
        s0=equilibrium(F0,N0,mu,a,h)
        x=exp(-d*R); z=exp(-n*R)
        sign=(1-z)+(x-z)*a*h*s0
        if abs(sign)>1e-7 and abs(pR-p0)>1e-11:
            assert sign*(pR-p0)>0, (j,sign,pR-p0);count+=1
    # Below the source threshold and beyond it, test each shape on a grid.
    for (F0,N0,d,n,mu,a,h) in [(8.,5.,1.,.5,1.,1.,1.),
                                   (1.,5.,1.,.5,1.,1.,1.),
                                   (10.,2.,.5,1.,1.,1.,1.),
                                   (15.,5.,1.,.7,1.,.8,.5)]:
        x=[survival(.025*i,F0,N0,d,n,mu,a,h) for i in range(301)]
        dy=[x[i+1]-x[i] for i in range(300)]
        signs=[1 if v>1e-11 else (-1 if v < -1e-11 else 0) for v in dy]
        signs=[s for s in signs if s]
        assert signs==sorted(signs) or all(s==1 for s in signs), signs[:10]
        count+=1
    return count


if __name__ == '__main__':
    print('PASS: %d finite diagnostic assertions (not an infinite proof)' % check())
