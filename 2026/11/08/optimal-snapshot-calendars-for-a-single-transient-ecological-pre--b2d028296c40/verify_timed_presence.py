#!/usr/bin/env python3
"""Independent reproducibility checks for optimal transient-presence snapshots.

The scientific theorem is established analytically in RESULT.md. These finite
checks compare its formulas with direct event integration and independent
optimization calculations; they are not substitutes for infinite proofs.
"""
from fractions import Fraction
import math
import random

CHECKS = 0


def ensure(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def first_detection_gap(q, h):
    if abs(q - 1.0) < 1e-12:
        return h * math.exp(-h)
    return q * (math.exp(-h) - math.exp(-q * h)) / (q - 1.0)


def exact_optimal_value(q, n):
    a = 0.0
    vals = [a]
    for _ in range(n):
        if abs(q - 1) < 1e-12:
            a = math.exp(a - 1)
        else:
            a = math.exp(-math.log(q-(q-1)*a)/(q-1))
        vals.append(a)
    gaps = [-math.log(vals[k]) for k in range(n, 0, -1)]
    return a, gaps


def detect_probability(q, gaps):
    t = 0.0
    output = 0.0
    for h in gaps:
        output += math.exp(-q*t)*first_detection_gap(q, h)
        t += h
    return output


def detect_probability_by_direct_integrals(q, gaps):
    # Independently integrated conditional survival, by Simpson quadrature.
    t = 0.0
    total = 0.0
    partitions = 200
    for h in gaps:
        a,b=t,t+h
        step=(b-a)/partitions
        segment=0.0
        for k in range(partitions+1):
            arrival=a+step*k
            weight=1 if k==0 or k==partitions else (4 if k%2 else 2)
            segment += weight*q*math.exp(-q*arrival)*math.exp(-(b-arrival))
        total += segment*step/3
        t=b
    return total


def golden_max(f, low, high, iterations=95):
    # independent bounded scalar optimizer
    frac=(math.sqrt(5)-1)/2
    x=high-frac*(high-low)
    y=low+frac*(high-low)
    fx,fy=f(x),f(y)
    for _ in range(iterations):
        if fx<fy:
            low=x; x=y; fx=fy
            y=low+frac*(high-low); fy=f(y)
        else:
            high=y; y=x; fy=fx
            x=high-frac*(high-low); fx=f(x)
    z=(low+high)/2
    return z,f(z)


def independently_optimize_times(q, n, seed):
    rng=random.Random(seed)
    times=[]
    t=0.0
    for i in range(n):
        t += 0.1 + rng.random()*2.0
        times.append(t)
    for _ in range(180):
        old=times.copy()
        for i in range(n):
            lower=0.0 if i==0 else times[i-1]
            upper=times[i+1] if i<n-1 else times[i]+4
            def score(newtime):
                cand=times.copy()
                cand[i]=newtime
                gaps=[cand[0]]+[cand[j]-cand[j-1] for j in range(1,n)]
                return detect_probability(q,gaps)
            times[i],_=golden_max(score, lower,upper,iterations=60)
        if max(abs(times[i]-old[i]) for i in range(n))<3e-9:
            break
    gaps=[times[0]]+[times[i]-times[i-1] for i in range(1,n)]
    return detect_probability(q,gaps),gaps


def uniformly_spaced_best(q, n):
    return golden_max(lambda h: detect_probability(q,[h]*n), 1e-8, 6.0,95)


def run():
    rng=random.Random(50711)
    for q in (0.25,0.5,1.0,2.0,3.0,5.0):
        for n in range(1,9):
            theoretical,gaps=exact_optimal_value(q,n)
            score=detect_probability(q,gaps)
            ensure(abs(theoretical-score)<3e-12, (q,n,'recurrence vs integral',theoretical,score))
            ensure(all(h>0 for h in gaps), (q,n,'positive gaps'))
            ensure(all(gaps[i]<gaps[i+1] for i in range(len(gaps)-1)), (q,n,'increasing gap sequence'))
            if n<=4:
                quadrature=detect_probability_by_direct_integrals(q,gaps)
                ensure(abs(quadrature-score)<5e-10, (q,n,'integral quadrature'))
                best,gap_est=independently_optimize_times(q,n,100*n+round(q*100))
                ensure(abs(best-theoretical)<1e-8,(q,n,'independent coordinate optimizer',best,theoretical,gap_est))
            for trial in range(180):
                random_gaps=[rng.expovariate(1.2) for _ in range(n)]
                ensure(detect_probability(q,random_gaps) <= theoretical+2e-13,(q,n,trial,'global counterexample'))
    for n in range(1,81):
        # With arrival rate twice exit rate, exp(-t_i) is rational.
        z_prev=Fraction(1)
        probability=Fraction(0)
        for i in range(1,n+1):
            z=Fraction(n-i+1,n+1)
            probability+=2*z*(z_prev-z)
            z_prev=z
        ensure(probability==Fraction(n,n+1), (n,'exact rational n/(n+1)'))
        score,gaps=exact_optimal_value(2,n)
        ensure(abs(score-n/(n+1))<2e-14, (n,'special case b_n'))
    for q in (0.5,1.0,2.0,4.0):
        for n in (300,1000,4000,10000):
            theory,gaps=exact_optimal_value(q,n)
            ratio=n*(1-theory)*q/2
            ensure(abs(ratio-1)< 0.08 if n==300 else abs(ratio-1)<0.03, (q,n,'large-n constant',ratio))
        for n in (200,1000,5000):
            h,score=uniformly_spaced_best(q,n)
            e=1-score
            # Leading-order bound only (convergence is slow).
            ratio=2*q*n*e/math.log(n)
            ensure(0.75<ratio<1.6, (q,n,'uniform-grid log law',ratio))
            ensure(h>0,(q,n,'positive uniform spacing'))
    print(f'PASS: {CHECKS} checks: exact rational identities, recurrence, direct quadrature,')
    print('independent numerical optimization, random schedules and asymptotic diagnostics.')

if __name__=='__main__':
    run()
