#!/usr/bin/env python3
"""Finite-identity checks and numerical asymptotic diagnostics for batch multicoverage.

This is supplementary reproducibility evidence, not a proof of an infinite limit.
Python 3 standard library only.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, exp, lgamma, log, pi, sqrt

checks = 0

def check(predicate, context):
    global checks
    if not predicate:
        raise AssertionError(context)
    checks += 1

def q_exact(t, m, p):
    return sum((Fraction(comb(t, j))*p**j*(1-p)**(t-j)
                for j in range(min(m, t+1))), Fraction(0))

def falling(x,k):
    z=1
    for h in range(k): z *= x-h
    return z

# A fixed inclusion/exclusion pattern in a uniform d-subset.
for N in range(4,11):
    for d in range(1,N):
        all_sets=list(combinations(range(N),d))
        for k in range(1,min(N,4)+1):
            for bit in product((0,1),repeat=k):
                a=sum(bit)
                predicted=Fraction(falling(d,a)*falling(N-d,k-a),falling(N,k))
                observed=Fraction(sum(all(((i in ss)==bool(bit[i])) for i in range(k))
                                      for ss in all_sets),len(all_sets))
                check(predicted==observed,(N,d,k,bit,predicted,observed))

# Exact one-coupon binomial survival recursion.
for dN in [Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(4,5)]:
    for t in range(0,20):
        for m in range(1,t+3):
            q0=q_exact(t,m,dN)
            top=Fraction(comb(t,m-1))*dN**(m-1)*(1-dN)**(t-m+1) if m-1<=t else 0
            check(q_exact(t+1,m,dN)==q0-dN*top,(dN,t,m))

# Two designated coupons' undercollection events are negatively correlated.
# Exact four-outcome transition law for each draw, then finite DP on counts.
for N in range(4,10):
    for d in range(1,N):
        probs={
          (0,0):Fraction(comb(N-2,d),comb(N,d)) if d<=N-2 else Fraction(0),
          (1,0):Fraction(comb(N-2,d-1),comb(N,d)),
          (0,1):Fraction(comb(N-2,d-1),comb(N,d)),
          (1,1):Fraction(comb(N-2,d-2),comb(N,d)) if d>=2 else Fraction(0),
        }
        check(sum(probs.values())==1,(N,d,'probability mass'))
        dp={(0,0):Fraction(1)}
        for t in range(1,7):
            nxt={}
            for (a,b),v in dp.items():
                for (i,j),pr in probs.items():
                    nxt[(a+i,b+j)]=nxt.get((a+i,b+j),Fraction(0))+v*pr
            dp=nxt
            check(sum(dp.values())==1,(N,d,t,'joint mass'))
            for m in range(1,t+2):
                q=q_exact(t,m,Fraction(d,N))
                joint=sum((v for (a,b),v in dp.items() if a<m and b<m),Fraction(0))
                check(joint<=q*q,(N,d,t,m,joint,q*q))

# Numerical checks of the exact saddlepoint formula. Used only as diagnostics.
def binary_kl(z,p):
    return z*log(z/p)+(1-z)*log((1-z)/(1-p))

def beta_value(alpha,p):
    low=alpha/p
    high=max(2*low,low+1)
    while high*binary_kl(alpha/high,p)<=1:
        high*=2
    for _ in range(100):
        mid=(low+high)/2
        if mid*binary_kl(alpha/mid,p)>1: high=mid
        else: low=mid
    return (low+high)/2

def log_binomial_cdf(t, m, p):
    # For integer t >= m: stable log-sum-exp of P(Bin(t,p)<m).
    vals=[lgamma(t+1)-lgamma(j+1)-lgamma(t-j+1)
          +j*log(p)+(t-j)*log(1-p) for j in range(m)]
    z=max(vals)
    return z+log(sum(exp(w-z) for w in vals))

for p, alpha in ((.35,.8),(.5,1.),(.7,2.)):
    beta=beta_value(alpha,p)
    eta=alpha*(1-p)/(p*(beta-alpha))
    r=(1-p)*beta/(beta-alpha)
    check(0<eta<1 and 0<r<1,(p,alpha,'rate bounds'))
    check(abs(beta*binary_kl(alpha/beta,p)-1)<1e-12,(p,alpha,'root'))
    for N in (10**5,10**7,10**9):
        L=log(N)
        m=__import__('math').ceil(alpha*L)
        delta=(m-1)-alpha*L
        t=round(beta*L-log(L)/(2*(-log(r))))
        C=eta**(-delta)/((1-eta)*sqrt(2*pi*alpha*(1-alpha/beta)))
        approx=C*L**(-.5)*r**(t-beta*L)
        truth=exp(log(N)+log_binomial_cdf(t,m,p))
        check(abs(truth/approx-1)<.035,(p,alpha,N,'saddlepoint',truth,approx))
        ratio=exp(log_binomial_cdf(t+1,m,p)-log_binomial_cdf(t,m,p))
        check(abs(ratio-r)<.045,(p,alpha,N,'local ratio',ratio,r))

print('PASS: %d finite exact and numerical assertions' % checks)
