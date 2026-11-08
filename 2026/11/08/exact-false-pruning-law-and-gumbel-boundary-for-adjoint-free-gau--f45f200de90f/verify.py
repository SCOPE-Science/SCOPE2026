#!/usr/bin/env python3
"""Numerical checks for the adjoint-free Gaussian rank-pruning obstruction.

Requires Python 3 with NumPy and SciPy. Run: python verify.py
This is a finite numerical reproduction, not an infinite proof.
"""
from math import exp, expm1, isclose, log, log1p, pi, sqrt
import numpy as np
from scipy.stats import chi2


def exact_two_step_probability(b, tau):
    """Probability of valid second-step termination with incorrect pruning."""
    assert isinstance(b, int) and b >= 2 and 0 < tau < 1
    # The first sketch contains b*b independent standard normal squares.
    first_pass = chi2.sf(b*tau*tau, b*b)
    # Each of the b rows of the independent second sketch contains b squares.
    row_tail = chi2.cdf(b*tau*tau, b)
    return float(first_pass * (-expm1(b*log1p(-row_tail))))


def gumbel_tau(b, x):
    l = log(b)-0.5*log(log(b))-0.5*log(4*pi)+x
    assert 0 < 2*sqrt(l/b) < 1
    return sqrt(1-2*sqrt(l/b))


def check_analytic_distribution():
    checks = 0
    rng = np.random.default_rng(47015)
    for b in (2, 4, 6, 8, 12, 16):
        for tau in (0.4, 0.7, 0.9, 0.99):
            target=exact_two_step_probability(b,tau)
            # Synthetic Monte Carlo from *independent* chi-square blocks,
            # representing exactly the first and second Gaussian probes.
            reps = 20000
            start = rng.chisquare(b*b, size=reps)/b > tau*tau
            row_sums = rng.chisquare(b, size=(reps,b))/b
            bad = start & (np.min(row_sums, axis=1)<tau*tau)
            freq=float(np.mean(bad))
            # Five standard deviations plus a small absolute guard.
            allowance=5*sqrt(target*(1-target)/reps)+0.009
            assert abs(freq-target)<allowance,(b,tau,target,freq,allowance)
            checks+=1
    print('Chi-square independent-sample Monte Carlo comparisons:', checks)
    return checks


def check_actual_algorithm_path():
    rng=np.random.default_rng(91147)
    checks=0
    # Explicitly reconstruct the first QR, the exact-zero lookahead,
    # the second sketched coefficient matrix, and original-error norm.
    for b in (2,3,4,7,10):
        n=2*b
        a=np.diag([1.0]*b+[0.0]*b)
        for _ in range(240):
            omega1=rng.standard_normal((n,b))/sqrt(b)
            z1=a@omega1
            tau=0.82
            if np.linalg.norm(z1,'fro')<=tau:
                continue   # exceptional first-stop branch, not part of claim
            q1,r=np.linalg.qr(z1,mode='reduced')
            assert np.linalg.norm(q1.T@q1-np.eye(b),'fro')<1e-12
            assert np.linalg.norm(a-q1@q1.T@a,'fro')<1e-12
            omega2=rng.standard_normal((n,b))/sqrt(b)
            z2=a@omega2
            y2=z2-q1@(q1.T@z2)
            assert np.linalg.norm(y2,'fro')<1e-12
            estimates=np.linalg.norm(q1.T@z2,axis=1)
            # Exact Algorithm 3: iterate up sorted row estimates and
            # exclude only those that keep the accumulated estimate < tau.
            order=np.argsort(estimates)
            discarded=[]
            accumulated=0.0
            for j in order:
                candidate=sqrt(accumulated**2+estimates[j]**2)
                if candidate>=tau:
                    break
                discarded.append(int(j))
                accumulated=candidate
            kept=[j for j in range(b) if j not in discarded]
            qout=q1[:,kept]
            actual=np.linalg.norm(a-qout@qout.T@a,'fro')
            assert isclose(actual,sqrt(len(discarded)),abs_tol=2e-12)
            assert (actual>tau)==(len(discarded)>0)
            assert (len(discarded)>0)==(float(np.min(estimates))<tau)
            checks+=1
    print('Original two-step QR and pruning path checks:',checks)
    return checks


def check_window():
    checks=0
    # Distributions approach the stated Gumbel boundary only slowly.
    for x in (-1.0,0.0,1.0):
        target=1-exp(-exp(-x))
        b=10_000_000
        tau=gumbel_tau(b,x)
        actual=exact_two_step_probability(b,tau)
        assert abs(actual-target)<0.04,(x,actual,target)
        checks+=1
    # On each side of the sharp c=2 boundary, check direction at large b.
    b=1_000_000
    low=exact_two_step_probability(b,sqrt(1-1.4*sqrt(log(b)/b)))
    high=exact_two_step_probability(b,sqrt(1-2.6*sqrt(log(b)/b)))
    assert low>0.97 and high<0.01,(low,high)
    checks+=2
    print('Asymptotic boundary spot checks:',checks)
    return checks


if __name__=='__main__':
    total=check_analytic_distribution()+check_actual_algorithm_path()+check_window()
    print('PASS: ',total,'numeric assertions/groups; infinite claims require the supplied proof')
