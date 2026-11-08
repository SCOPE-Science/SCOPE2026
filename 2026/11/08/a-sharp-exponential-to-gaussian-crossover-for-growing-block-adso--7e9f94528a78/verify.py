#!/usr/bin/env python3
"""Exact finite checks and numerical scaling diagnostics for growing-block near-saturation adsorption.

This program does not prove the infinite-volume scaling theorem; the analytic proof
is contained in RESULT.md. Only Python's standard library is needed.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, exp, log, isclose

checks = 0

def check(condition, context):
    global checks
    if not condition:
        raise AssertionError(context)
    checks += 1

def probability(n, k, j):
    return Fraction(comb(k*j, k), comb(k*n, k))

def weights(n, k, u):
    r = u + 1
    return [Fraction(comb(k*r, k), comb(k*j, k)) for j in range(r, n+1)]

# Independent combinatorial sampling of every possible proposed block:
# the success count must not depend on the particular occupied positions.
for n in range(2, 6):
    for k in range(1, 4):
        N = n*k
        if comb(N, k) > 2500:
            continue
        all_attempts = list(combinations(range(N), k))
        for j in range(1, n+1):
            free = set(range(k*j))
            successes = sum(set(e) <= free for e in all_attempts)
            check(Fraction(successes, len(all_attempts)) == probability(n, k, j),
                  ('attempt probability', n, k, j))

# Distribution of the hitting time through two independently implemented
# finite-state calculations: absorption in the number-deposited chain
# versus convolution of geometric waiting-time masses.
for n in range(2, 8):
    for k in range(1, 5):
        for u in range(n):
            target = n-u
            hit = [Fraction(0) for _ in range(target+1)]
            hit[0] = Fraction(1)
            geom = [Fraction(1)]
            for t in range(1, 19):
                nxt = [Fraction(0) for _ in hit]
                for s in range(target):
                    p = probability(n, k, n-s)
                    nxt[s] += hit[s]*(1-p)
                    nxt[s+1] += hit[s]*p
                nxt[target] += hit[target]
                # Independently build the product of geometric PGFs up to z^t.
                if t == 1:
                    convolved = [Fraction(1)]
                    for s in range(target):
                        p = probability(n, k, n-s)
                        new = [Fraction(0) for _ in range(19)]
                        for i, a in enumerate(convolved):
                            if i >= 19: break
                            b = p
                            for h in range(1, 19-i):
                                new[i+h] += a*b
                                b *= 1-p
                        convolved = new
                check(nxt[target]-hit[target] == convolved[t],
                      ('hitting-time exact pmf', n, k, u, t))
                hit = nxt
            ws=weights(n,k,u)
            p0=probability(n,k,u+1)
            # Compare scaled moments by two algebraically separate expressions.
            scaled_mean = sum(ws, Fraction(0))
            scaled_var = sum(w*w*(1-probability(n,k,j))
                             for j,w in zip(range(u+1,n+1),ws))
            check(scaled_var == sum((w*w for w in ws), Fraction(0)) - p0*scaled_mean,
                  ('variance identity',n,k,u))
            check(ws[0]==1 and all(ws[i]>=ws[i+1] for i in range(len(ws)-1)),
                  ('decreasing weights',n,k,u))

# Floating-point only checks of the scaling parameters, not certificates.
def weight_float(k, r, ell):
    # Stable product expression for binomial coefficient ratios.
    return exp(-sum(log(1+ell/(r-i/k)) for i in range(k)))

for theta in (0.5,1.,2.,4.):
    predicted_mean=1/(1-exp(-1/theta))
    predicted_var=1/(1-exp(-2/theta))
    errors=[]
    for k in (20,40,80):
        u=round(theta*k)
        r=u+1
        a=[weight_float(k,r,j) for j in range(2000)]
        mean=sum(a); variance=sum(x*x for x in a)
        errors.append(abs(mean-predicted_mean))
        check(mean>=1 and variance>=1 and mean*mean>=variance,
              ('finite critical moments',theta,k))
        check(isclose(a[1],exp(-1/theta),rel_tol=0.2),
              ('rate-ratio approximation',theta,k))
    check(errors[2]<errors[0],('critical mean convergence',theta,errors))

# Gaussian-regime growth: k/u -> 0, summed mth powers grow as u/(mk).
for k,u in ((20,1000),(40,2000),(80,4000)):
    r=u+1
    for m in (1,2,3):
        total=sum(weight_float(k,r,j)**m for j in range(7000))
        prediction=r/(m*k)
        check(abs(total/prediction-1)<0.08,
              ('Gaussian scaling power sum',k,u,m,total,prediction))

# q-product moments: direct infinite-series truncations converge to formulas.
for theta in (0.2,0.5,1,2,4):
    q=exp(-1/theta)
    w=[q**j for j in range(400)]
    check(isclose(sum(w),1/(1-q),rel_tol=1e-12),('q mean',theta))
    check(isclose(sum(x*x for x in w),1/(1-q*q),rel_tol=1e-12),('q var',theta))

print('PASS', checks, 'exact and diagnostic assertions')
