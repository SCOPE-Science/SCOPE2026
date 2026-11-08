#!/usr/bin/env python3
"""Supplementary standard-library checks for a star-network gain allocation theorem.

Requires Python 3.9+. These finite checks supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction
from math import sqrt, isfinite
from random import Random


def target(m, p0, p, lam):
    """Minimum price for a prescribed positive spectral rate; dual Schur formula."""
    ell = max(0.0, 1.0-lam)
    def g(a):
        return lam-m+sum(1.0/max(ell,sqrt(a/pi)) for pi in p)
    if g(p0)>=0.0:
        alpha=p0
    else:
        lo,hi=0.0,p0
        for _ in range(110):
            mid=(lo+hi)/2
            if g(mid)>0: lo=mid
            else: hi=mid
        alpha=(lo+hi)/2
    t=[max(ell,sqrt(alpha/pi)) for pi in p]
    u=[max(0.0,lam-m+sum(1/v for v in t))]+[max(0.0,v+lam-1.0) for v in t]
    return p0*u[0]+sum(pi*ui for pi,ui in zip(p,u[1:])), u, alpha


def optimal(m,p0,p,B):
    lo,hi=0.0,max(2.0,m+1+B/min([p0]+list(p)))
    for _ in range(110):
        mid=(lo+hi)/2
        if target(m,p0,p,mid)[0]<B:lo=mid
        else:hi=mid
    lam=(lo+hi)/2
    return (lam,)+target(m,p0,p,lam)


def secular(m,u):
    """Smallest eigenvalue of star Laplacian plus an arbitrary nonnegative diagonal."""
    a=[1.0+v for v in u[1:]]
    high=min(a)
    def equation(lam):
        return m+u[0]-lam-sum(1.0/(d-lam) for d in a)
    low=0.0
    for _ in range(110):
        mid=(low+high)/2
        if equation(mid)>0:low=mid
        else:high=mid
    return (low+high)/2


def equal_leaf_exact():
    n=0
    for m in range(2,11):
      for P,Q in ((1,4),(4,1),(1,9),(9,1),(4,4),(9,4),(4,9)):
        R=sqrt(Fraction(P,Q))
        # These pairs have rational square roots.
        R=Fraction(int(round(R*12)),12)
        assert R*R==Fraction(P,Q)
        split=(1-R) if R<1 else m*(1-1/R) if R>1 else 0
        for lam in [Fraction(1,12),Fraction(1,3),Fraction(3,4),
                    Fraction(5,4),Fraction(m,2), Fraction(m+3,1),
                    max(Fraction(0),split-Fraction(1,8)),split,
                    split+Fraction(1,8)]:
          if lam<=0: continue
          if R<1 and lam<=split:
            u0=lam*(m+1-lam)/(1-lam);ul=Fraction(0)
          elif R>1 and lam<=split:
            u0=Fraction(0);ul=lam*(m+1-lam)/(m-lam)
          else:
            u0=lam-m+m/R;ul=lam-1+R
          assert u0>=0 and ul>=0
          # The exact 2x2 reduced determinant at the asserted lowest eigenvalue vanishes.
          assert (m+u0-lam)*(1+ul-lam)==m
          assert 1+ul>lam
          B=P*u0+m*Q*ul
          assert B>0
          asym=(P+m*Q)*lam -P*m-m*Q+2*m*Fraction(P,1)/R
          if lam>=split: assert B==asym
          n+=1
    return n


def randomized_checks():
    rng=Random(360041)
    cases=0;competitors=0;activation=0;inversions=0
    for j in range(400):
      m=rng.randint(2,10)
      p0=10**rng.uniform(-1.7,1.5)
      p=[10**rng.uniform(-1.7,1.5) for _ in range(m)]
      B=10**rng.uniform(-2.4,2.4)
      lam,c,u,alpha=optimal(m,p0,p,B)
      assert abs(c-B)<2e-9*max(1,B)
      assert abs(secular(m,u)-lam)<5e-9*max(1,lam)
      assert min(u)>-1e-12 and 0<alpha<=p0
      for _ in range(15):
        v=[rng.expovariate(1.0) for _ in range(m+1)]
        scale=B/sum(pi*vi for pi,vi in zip([p0]+p,v))
        v=[scale*w for w in v]
        assert secular(m,v)<lam+2e-8*max(1,lam)
        competitors+=1
      # For increasing target rate, active leaf sets are nested.
      rates=[(k+1)*lam/20 for k in range(20)]
      states=[];hubs=[]
      for rate in rates:
        _,z,_=target(m,p0,p,rate)
        states.append({i for i,v in enumerate(z[1:]) if v>2e-9})
        hubs.append(z[0]>2e-9)
      for ii in range(19):
        assert states[ii]<=states[ii+1]
        assert not hubs[ii] or hubs[ii+1]
        activation+=1
      cases+=1
    return cases,competitors,activation


def main():
    exact=equal_leaf_exact()
    cases,competitors,activation=randomized_checks()
    print('PASS exact two-price determinant/budget cases:',exact)
    print('PASS heterogeneous-price target + secular calculations:',cases)
    print('PASS budget-feasible competitor comparisons:',competitors)
    print('PASS nested activation comparisons:',activation)
    print('Total supplementary checks:',exact+cases+competitors+activation)

if __name__=='__main__':main()
