"""Exact rational checks for a beta-competitor ecological sorting theorem.

Run: python3 verify.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import comb


def beta_cdf(x):
    return 3*x*x-2*x*x*x


def moment(law, k):
    return sum((p*x**k for x,p in law), F(0))


def D(law):
    return 2*sum((p*beta_cdf(x) for x,p in law), F(0))-1


def endpoints(mu, nu):
    assert 0<mu<1 and mu*mu<=nu<=mu
    hi = [(F(0),1-mu*mu/nu),(nu/mu,mu*mu/nu)]
    a = (mu-nu)/(1-mu)
    lo = [(a, (1-mu)**2/(1-2*mu+nu)),(F(1),(nu-mu*mu)/(1-2*mu+nu))]
    return lo,hi


def fix(J,k,d):
    r=(1-d)/(1+d)
    return sum((r**i for i in range(k)),F(0))/sum((r**i for i in range(J)),F(0))


def rates(J,m,pi,c,d):
    pp=[F(0)]*(J+1); pm=[F(0)]*(J+1)
    for n in range(J+1):
        h=F(2*n*(J-n),J*(J-1))
        pp[n]=(1-m)*c*h*(1+d)/2 + m*pi*F(J-n,J)
        pm[n]=(1-m)*c*h*(1-d)/2 + m*(1-pi)*F(n,J)
        assert 0<=pp[n] and 0<=pm[n] and pp[n]+pm[n]<=1
    return pp,pm


def stationary(J,m,pi,c,d):
    pp,pm=rates(J,m,pi,c,d)
    v=[F(1)]
    for n in range(J):
        v.append(v[-1]*pp[n]/pm[n+1])
    z=sum(v)
    return [x/z for x in v]


def closed_stationary(J,m,pi,c,d):
    W=(1+d)/2; L=(1-d)/2
    a=F(2)*(1-m)*c*W/(J-1)
    b=F(2)*(1-m)*c*L/(J-1)
    alpha=m*pi/a; beta=m*(1-pi)/b
    def rising(x,k):
        z=F(1)
        for i in range(k): z*=x+i
        return z
    v=[F(comb(J,n))*rising(alpha,n)*rising(beta,J-n)*(a/b)**n for n in range(J+1)]
    return [x/sum(v) for x in v]


def main():
    # The polynomial bound is a rational algebra identity at many points;
    # the global nonnegative factorization is established in RESULT.md.
    for j in range(1001):
        x=F(j,1000)
        assert F(9,8)*x-beta_cdf(x)==x*(4*x-3)**2/8

    # Verify both moment extremizers, sharp D formulas, and equality cases.
    for denominator in range(3,12):
        for numerator in range(1,denominator):
            mu=F(numerator,denominator)
            for t in range(11):
                nu=mu*mu + F(t,10)*(mu-mu*mu)
                lo,hi=endpoints(mu,nu)
                for law in (lo,hi):
                    assert sum((p for x,p in law),F(0))==1
                    assert all(0<=x<=1 and p>=0 for x,p in law)
                    assert moment(law,1)==mu and moment(law,2)==nu
                Dlo=2*nu-1+4*(mu-nu)**2/(1-mu)
                Dhi=6*nu-1-4*nu**2/mu
                assert D(lo)==Dlo and D(hi)==Dhi
                assert Dhi-Dlo==4*(mu-nu)*(nu-mu*mu)/(mu*(1-mu))
                assert Dlo<=Dhi

    # At fixed mean 12/25 below the rival mean 1/2, identical means
    # and variances can yield opposite drift signs.
    mu=F(12,25);nu=F(9,25)
    lo,hi=endpoints(mu,nu)
    assert hi==[(F(0),F(9,25)),(F(3,4),F(16,25))]
    assert lo==[(F(3,13),F(169,250)),(F(1),F(81,250))]
    assert D(lo)==F(-11,65) and D(hi)==F(2,25)
    assert F(9,8)*mu==F(27,50) and 2*F(27,50)-1==F(2,25)
    assert F(9,4)*F(4,9)-1==0

    # Universal analytic logistic robustness uses the beta density bound
    # sup f_Y = 3/2 and the elementary integral ∫ exp(-lambda |z|) dz = 2/lambda.
    # Rational sign margins suffice for all real lambda > 75.
    lam=F(75)
    assert F(2,25)-6/lam==0
    assert F(-11,65)+6/lam<0

    # Sharp finite-J fixation, exact harmonic recurrence and ordering.
    for J in range(2,13):
        for d in (F(-11,65),F(-1,8),F(0),F(1,8),F(2,25)):
            pp,pm=rates(J,F(0),F(1,3),F(2,3),d)
            for k in range(1,J):
                v=fix(J,k,d)
                assert v==pp[k]*fix(J,k+1,d)+pm[k]*fix(J,k-1,d)+(1-pp[k]-pm[k])*v
        for k in range(1,J):
            assert fix(J,k,F(-11,65))<fix(J,k,F(2,25))
    assert fix(10,5,F(1,8))==F(59049,75856)
    assert fix(10,5,F(-1,8))==F(16807,75856)

    # Irreducible finite-chain detailed balance, explicit beta-binomial
    # tilt, and strict upper-tail ranking for every finite threshold.
    for J in range(2,13):
        for m in (F(1,10),F(2,5),F(4,5)):
            for pi in (F(1,3),F(3,5)):
                for c in (F(1,3),F(1)):
                    plo=stationary(J,m,pi,c,F(-11,65))
                    phi=stationary(J,m,pi,c,F(2,25))
                    assert plo==closed_stationary(J,m,pi,c,F(-11,65))
                    assert phi==closed_stationary(J,m,pi,c,F(2,25))
                    assert sum(plo)==sum(phi)==1
                    for d,p in ((F(-11,65),plo),(F(2,25),phi)):
                        pp,pm=rates(J,m,pi,c,d)
                        for n in range(J):
                            assert p[n]*pp[n]==p[n+1]*pm[n+1]
                    for n in range(1,J+1):
                        assert sum(phi[n:])>sum(plo[n:])
                    assert all(phi[n+1]*plo[n]>phi[n]*plo[n+1] for n in range(J))
    print('PASS: sharp moment certificates, lower-mean reversal, fixation identities, and exact stationary monotone-likelihood-ratio comparisons')


if __name__=='__main__':main()
