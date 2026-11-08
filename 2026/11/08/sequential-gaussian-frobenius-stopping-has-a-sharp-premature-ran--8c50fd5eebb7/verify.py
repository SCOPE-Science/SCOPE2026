"""Finite checks for a Gaussian adaptive single-node range-stopping law.

Requires Python >=3.9, numpy and scipy. No network, no external data.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import betainc

checks = 0

def check(statement, label):
    global checks
    assert bool(statement), label
    checks += 1


def prob(r, width, tau, k):
    if k == 0:
        return 0.0
    if k == r:
        return 1.0
    return float(betainc(width * (r-k) / 2, width * k / 2, tau))


def law(r, width, tau):
    assert r % width == 0
    survival = 1.0
    ans = []
    for k in range(0, r + 1, width):
        p = prob(r, width, tau, k)
        ans.append(survival * p)
        survival *= 1.0-p
    return np.array(ans)


# For integral beta shapes, I_t(a,d) is a finite binomial tail.
for r in (4, 8, 12, 16, 24):
    for width in (2, 4):
        if r % width:
            continue
        for tau in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
            for k in range(width, r, width):
                a = width*(r-k)//2
                d = width*k//2
                exact = sum(Fraction(math.comb(a+d-1,j)) *
                            tau**j * (1-tau)**(a+d-1-j)
                            for j in range(a, a+d))
                check(abs(prob(r,width,float(tau),k)-float(exact)) < 2e-14,
                      'beta/integer binomial identity')
                check(0 < exact < 1, 'strict intermediate beta tails')
            dist = law(r,width,float(tau))
            check(abs(sum(dist)-1) < 2e-13, 'total stopping probability')
            kstar = math.ceil((1-float(tau))*r/width)*width
            early1 = sum(dist[j] for j in range(len(dist)) if j*width < kstar)
            prior_product = math.prod(1-prob(r,width,float(tau),k)
                                      for k in range(0,kstar,width))
            check(abs(early1-(1-prior_product)) < 2e-13,
                  'exact first-stop failure probability')

# Direct adaptive QR checks: the probes used for a successful test are
# not included in its returned basis. The coordinate orientation is random.
rng = np.random.default_rng(437219)
for r, width, tau, replicates in ((12, 2, 0.25, 2300), (18, 3, 0.5, 2300),
                                  (24, 4, 0.4, 2300)):
    counts = np.zeros(r//width + 1, dtype=int)
    for _ in range(replicates):
        basis = np.empty((r,0))
        for k in range(0,r+1,width):
            G = rng.standard_normal((r,width))
            E = G - basis @ (basis.T @ G)
            if np.sum(E*E) <= tau*np.sum(G*G) or k == r:
                counts[k//width] += 1
                check(abs(np.linalg.norm(basis.T @ basis-np.eye(k))) < 1e-9,
                      'orthonormal retained basis')
                break
            Q, R = np.linalg.qr(E, mode='reduced')
            check(np.min(np.abs(np.diag(R))) > 1e-9,
                  'full residual block rank')
            basis = np.column_stack((basis,Q))
    theoretical = law(r,width,tau)
    empirical = counts/replicates
    for j in range(len(theoretical)):
        p = float(sum(theoretical[:j+1]))
        e = float(sum(empirical[:j+1]))
        safety = 7*math.sqrt(max(p*(1-p),0)/replicates)+0.005
        check(abs(p-e) <= safety, 'Gaussian adaptive QR rank CDF')

# Check the single-look moderate-deviation exponent against beta CDF.
# The finite-rank correction from the prefactor is only O(log(log r)/log r).
for r in (2**15,2**17,2**19):
    for c in (0.3, 0.5, 0.7):
        width = 2
        tau = 0.25
        target = (1-tau)*r-c*math.sqrt(r*math.log(r))
        k = int(target//width)*width
        q = (r-k)/r
        p = prob(r,width,tau,k)
        predicted = ((math.sqrt(tau*(1-tau)) /
                      (c*math.sqrt(math.pi*width*math.log(r)))) *
                     r**(-width*c*c/(4*tau*(1-tau))))
        check(0.75 < p/predicted < 1.2,
              'moderate-deviation density/Laplace approximation')

# Finite example reported in the theorem.
dist = law(2048,2,0.25)
false = sum(dist[:math.ceil((1-0.25)*2048/2)])
check(abs(false-0.987911) < 8e-7, 'reported finite illustration')

print(f'PASS: {checks} exact-rational identities, first-passage checks, '
      'adaptive-QR assertions and moderate-deviation comparisons')
