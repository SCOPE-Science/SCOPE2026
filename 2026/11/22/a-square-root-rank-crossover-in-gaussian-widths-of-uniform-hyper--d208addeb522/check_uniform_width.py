#!/usr/bin/env python3
"""Finite checks for normalized random widths of uniform hypergraph degree zonotopes."""
import itertools
import math
import random
from fractions import Fraction


def subsets(n, k):
    return tuple(itertools.combinations(range(n), k))


def width(n, k, g):
    ss = subsets(n, k)
    return sum(abs(sum(g[i] for i in s) / math.sqrt(k)) for s in ss) / len(ss)


def mean_square_chaos(n, k, g):
    ss = subsets(n, k)
    return sum((sum(g[i] for i in s) ** 2) / k - 1 for s in ss) / len(ss)


def chaos_identity(n, k, g):
    a = sum(v * v - 1 for v in g) / n
    b = sum(g) ** 2 / n - 1
    return (n-k) * a / (n-1) + (k-1) * b / (n-1)


def cov_abs(rho):
    rho = min(1.0, max(-1.0, rho))
    return 2 / math.pi * (math.sqrt(max(0.0, 1-rho*rho)) + rho*math.asin(rho) - 1)


def exact_variance(n,k):
    return sum(math.comb(k,j)*math.comb(n-k,k-j)/math.comb(n,k)*cov_abs(j/k)
               for j in range(k+1) if 0 <= k-j <= n-k)


def fourth_overlap(n,k):
    ex = sum(Fraction(math.comb(k,j)*math.comb(n-k,k-j),math.comb(n,k)) * Fraction(j,k)**4
             for j in range(k+1) if 0 <= k-j <= n-k)
    fac = sum(Fraction(t*(t-1)* (t-2)*(t-3),1) * Fraction(math.comb(k,t)*math.comb(n-k,k-t),math.comb(n,k)) for t in range(k+1) if t <= n-k)
    falling = lambda x,r: math.prod(x-j for j in range(r))
    alt = sum(Fraction(s * falling(k,r)**2, falling(n,r)) for r,s in ((1,1),(2,7),(3,6),(4,1)) if r<=k and r<=n)
    assert ex == alt/Fraction(k**4), (n,k,ex,alt)
    return ex


def run():
    rng = random.Random(20261118)
    count=0
    for n in range(2,12):
        for k in range(1,n):
            ss=subsets(n,k)
            assert len(ss)==math.comb(n,k)
            for j in range(7):
                # Exact rational arithmetic for nontrivial normalization identity.
                g=[Fraction((i*i+3*i+2*j)%17-8, 7) for i in range(n)]
                lhs=sum((sum(g[i] for i in s)**2) / k-1 for s in ss) / len(ss)
                rhs=Fraction(n-k,n-1)*sum(v*v-1 for v in g)/n + Fraction(k-1,n-1)*(sum(g)**2/n-1)
                assert lhs==rhs,(n,k,j,lhs,rhs)
                count+=1
            e4=fourth_overlap(n,k)
            assert 0<=e4<=1
            var=exact_variance(n,k)
            assert 0 < var <=1-2/math.pi +1e-10
            # Higher Gaussian chaoses are nonnegative and the Hermite tail is bounded by overlap fourth moment.
            a2=1/math.sqrt(2*math.pi)
            v2=(2*(n-k)**2/n +2*(k-1)**2 +4*(n-k)*(k-1)/n)/(n-1)**2
            tail=var-a2*a2*v2
            assert tail >=-2e-12,(n,k,tail)
            assert tail <= (1-2/math.pi)*float(e4)+1e-12,(n,k,tail,e4)
    # Independently estimate moments of exact widths from sampled Gaussian input.
    # This is a finite diagnostic, not evidence for the asymptotic theorem.
    for n,k in [(4,1),(5,2),(6,3),(7,2),(8,4),(9,5),(10,3)]:
        ns=3500
        ww=[]
        for _ in range(ns):
            g=[rng.gauss(0,1) for i in range(n)]
            ww.append(width(n,k,g))
        mu=sum(ww)/ns
        v=sum((v-mu)**2 for v in ww)/(ns-1)
        analytic=exact_variance(n,k)
        assert abs(mu-math.sqrt(2/math.pi))<0.07,(n,k,mu)
        assert abs(v-analytic)<max(0.025,0.16*analytic),(n,k,v,analytic)
    print('UNIFORM_HYPERGRAPH_WIDTH_PASS exact_rational_checks=',count,
          ' parameter_pairs=',sum(n-1 for n in range(2,12)),
          ' independent_gaussian_trials=',7*3500)

if __name__=='__main__':
    run()
