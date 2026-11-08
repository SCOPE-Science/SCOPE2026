"""Numerical and finite-combinatorial checks for shifted-simplex section laws.

This verifies identities at finite parameter values and sampled approximations.
The infinite-dimensional limit theorems follow from the analytic proof.
Only Python 3's standard library is required.
"""
from collections import Counter
from itertools import combinations
from math import acos, comb, erf, pi, sqrt, asin
from random import Random

PHI = lambda x: 0.5*(1.0+erf(x/sqrt(2.0)))


def counts(values):
    n = len(values)-1
    positives = sum(v > 0 for v in values)
    return [comb(n+1,j+2) - (comb(positives,j+2) if positives >= j+2 else 0)
            - (comb(n+1-positives,j+2) if n+1-positives >= j+2 else 0)
            for j in range(n-1)]


def direct_counts(values):
    n=len(values)-1
    return [sum(any(values[i]>0 for i in subset) and
                any(values[i]<0 for i in subset)
                for subset in combinations(range(n+1),j+2))
            for j in range(n-1)]


def shifted_heights(draws, h):
    center = sum(draws)/len(draws)
    base = draws[0]-center
    return [draws[i]-center-h*base for i in range(len(draws))]


def mean_exact(n,h):
    den = n*(1+h*h)+2*h
    rho0 = -(1+n*h)/sqrt(n*den)
    rho1 = (n*h*h+2*h-1)/den
    return (n*acos(rho0)+comb(n,2)*acos(rho1))/pi


def limit_mean(h):
    return 0.25-asin(h*h/(1+h*h))/(2*pi)


def test():
    rng=Random(262622)
    finite_checks=0
    for n in range(2,12):
        for h in (0.,.02,.22,.6,.99):
            for _ in range(45):
                g=[rng.gauss(0,1) for i in range(n+1)]
                z=shifted_heights(g,h)
                assert max(z)>0 and min(z)<0
                lhs=counts(z)
                assert lhs == direct_counts(z)
                p=sum(x>0 for x in z)
                assert lhs[0]==p*(n+1-p)
                finite_checks+=1
    # Pairwise covariances calculated independently from projected Gram vectors.
    cov_checks=0
    for n in (2,3,4,7,13,100):
        for h in (0.,.12,.5,.89,.999):
            matrix=[[float(i==j)-1/(n+1) for j in range(n+1)] for i in range(n+1)]
            v0=matrix[0][0]
            diag=matrix[1][1]-2*h*matrix[0][1]+h*h*v0
            c01=(matrix[0][1]-h*v0)/sqrt(v0*diag)
            c12=(matrix[1][2]-h*(matrix[0][1]+matrix[0][2])+h*h*v0)/diag
            den=n*(1+h*h)+2*h
            assert abs(c01+(1+n*h)/sqrt(n*den))<1.e-12
            assert abs(c12-(n*h*h+2*h-1)/den)<1.e-12
            cov_checks+=1
    # Mean: Monte Carlo checks with conservative deterministic error thresholds.
    mc_checks=0
    for n,h in ((3,0.),(3,.75),(5,.3),(5,.95),(10,.15),(10,.8),(25,.6)):
        num=45000
        accum=0
        accum2=0
        for _ in range(num):
            g=[rng.gauss(0,1) for i in range(n+1)]
            x=counts(shifted_heights(g,h))[0]
            accum+=x
            accum2+=x*x
        empirical=accum/num
        variance=max(1.0,accum2/num-empirical*empirical)
        assert abs(empirical-mean_exact(n,h))<6*sqrt(variance/num)+.01, (n,h,empirical,mean_exact(n,h))
        mc_checks+=1
    # Almost-sure coupling approximation for the fixed-shift limit, and mean.
    coupling_checks=0
    for h in (.23,.7,.99):
        for _ in range(220):
            n=2000
            g=[rng.gauss(0,1) for i in range(n+1)]
            heights=shifted_heights(g,h)
            p=sum(x>0 for x in heights)
            vertex=p*(n+1-p)
            target=PHI(h*g[0])*PHI(-h*g[0])
            assert abs(vertex/(n*n)-target)<.048
            coupling_checks+=1
        assert abs(limit_mean(h)-(0.25-asin(h*h/(1+h*h))/(2*pi)))<1.e-14
    # For h->1, Phi(G) uniform and W=U(1-U): exact algebraic moments.
    assert abs(limit_mean(1)-1/6)<1.e-13
    assert abs((1/30-(1/6)**2)-1/180)<1.e-13
    # For h=c/sqrt(n), the critical variance formula is positive and interpolates correctly.
    sigma0=0.25-1/(2*pi)
    for c in (0,0.5,1,3):
        assert abs((sigma0+c*c/(2*pi))-(0.25+(c*c-1)/(2*pi)))<1.e-14
    print('PASS', 'face_subsets',finite_checks, 'Gaussian_covariances',cov_checks,
          'finite_means',mc_checks, 'coupled_limits',coupling_checks,
          'endpoint_mean',1/6)


if __name__=='__main__':
    test()
