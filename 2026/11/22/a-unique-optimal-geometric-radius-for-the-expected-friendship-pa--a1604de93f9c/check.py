"""Reproduce finite numerical and algebraic checks for the radius-optimization theorem.
No external dependencies. Finite checks supplement, and do not replace, the proof.
"""
from fractions import Fraction
from math import comb, exp, log


def rho(r):
    return .75 if r <= 1/3 else 3 - 1.5/r + .25/(r*r)


def rho_prime(r):
    return 0. if r <= 1/3 else (3*r-1)/(2*r**3)


def tail(n, p):
    # Probability of >=2 successes in Bin(n-1,p).
    N = n-1
    return 1-(1-p)**N-N*p*(1-p)**(N-1)


def mean(n, m, r):
    return (1-rho(r)**m)*tail(n,(2*r)**m)


def elasticity(n,p):
    N=n-1
    if p == 0: return 2.
    if p == 1: return 0. if N>2 else 2.
    odds=p/(1-p)
    den=sum(comb(N,k)*odds**(k-2) for k in range(2,N+1))
    return N*(N-1)/den


def penalty(m,r):
    if r <= 1/3:return 0.
    z=rho(r)
    return r*z**(m-1)*rho_prime(r)/(1-z**m)


def optimal(n,m):
    lo=1/3
    hi=.5
    for _ in range(95):
        x=(lo+hi)/2
        if elasticity(n,(2*x)**m)>penalty(m,x):lo=x
        else:hi=x
    return (lo+hi)/2


def dense_coefficient(m):
    kappa=1-(3/4)**m
    return 2*kappa/(27*(3/4)**(m-1))


def high_d_t(n):
    lo=0.
    hi=1.
    N=n-1
    for _ in range(95):
        t=(lo+hi)/2
        if (1-t)/t*elasticity(n,t)>1:lo=t
        else:hi=t
    return (lo+hi)/2


def run():
    checks=0
    # The n=3,m=1 exact polynomial and its exact critical point.
    r=Fraction(3,8)
    result=-8*r*r+6*r-1
    assert result == Fraction(1,8)
    checks+=1
    assert Fraction(1,3)<r<Fraction(1,2)
    checks+=1
    assert abs(mean(3,1,float(r))-1/8)<1e-13
    checks+=1
    # Test exact binomial-tail rational representation (not a general proof).
    for n in range(3,15):
        N=n-1
        for p in (Fraction(1,10),Fraction(1,4),Fraction(2,5),Fraction(3,4)):
            b=sum(Fraction(comb(N,k))*p**k*(1-p)**(N-k) for k in range(2,N+1))
            b2=1-(1-p)**N-N*p*(1-p)**(N-1)
            assert b==b2
            checks+=1
    # Locate the unique predicted numerical root, check slopes and strictness.
    for n in (3,4,5,7,12,20,45):
        for m in (1,2,3,5,10,30,100):
            x=optimal(n,m)
            assert 1/3<x<.5
            checks+=1
            for dr in (-1e-5,1e-5):
                rr=x+dr
                if 1/3<rr<.5:
                    assert mean(n,m,rr)<mean(n,m,x)+1e-9
                    checks+=1
            for a,b in ((.335,.35),(.36,.40),(.41,.46),(.47,.49)):
                if a<b:
                    assert penalty(m,a)<penalty(m,b)
                    checks+=1
            for p1,p2 in ((.01,.1),(.2,.5),(.7,.9)):
                assert elasticity(n,p1)>=elasticity(n,p2)-1e-12
                checks+=1
    # Verify fixed-m exponentially close radius, and high-m rescaling.
    for m in (1,2,3):
        for n in (10,14,18):
            x=optimal(n,m)
            p0=(2/3)**m
            N=n-1
            scale=dense_coefficient(m)*N*(N-1)*p0**2*(1-p0)**(N-2)
            if scale>1e-11:
                assert abs((x-1/3)/scale-1)<.3
                checks+=1
    for n in (3,4,7,12):
        t=high_d_t(n)
        assert 0<t<1
        checks+=1
        for m in (100,300,800):
            c=m*(.5-optimal(n,m))
            assert abs(c+.5*log(t))<.02
            checks+=1
    assert abs(high_d_t(3)-2/3)<1e-10
    checks+=1
    print('PASS',checks,'finite algebraic and numerical assertions')
    print('exact optimizer n=3,m=1:',optimal(3,1))
    print('sample n=4,m=1:',optimal(4,1))
    print('fixed n=3 high-dimensional parameter c3:',-.5*log(high_d_t(3)))

if __name__=='__main__':
    run()
