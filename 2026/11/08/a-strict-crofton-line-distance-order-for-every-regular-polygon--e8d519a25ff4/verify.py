"""Independent numerical tests for a regular polygon's Crofton dual-hit law.

Uses only Python's standard library and fixed quadrature/trials; analytic
proofs in RESULT.md, not replaced by these numerical diagnostics.
"""
import math
import random

RNG = random.Random(2718281828)

def prediction(n, radius, circumradius=1.0):
    beta = math.pi / n
    ratio = radius / circumradius
    if ratio <= 0:
        return 0.0
    if ratio >= 1:
        return 1.0
    if ratio <= math.cos(beta):
        return ratio * beta / math.sin(beta)
    alpha = math.acos(ratio)
    return 1.0 + (ratio * alpha - math.sin(alpha)) / math.sin(beta)

def support(n, theta):
    return max(math.cos(theta-2*math.pi*k/n) for k in range(n))

def grid_integral(n, radius, steps=16000):
    # Independent kinematic line-offset integral, not the closed formula.
    numerator = denominator = 0.0
    for j in range(steps):
        angle = 2*math.pi*(j + 0.5)/steps
        h = support(n, angle)
        numerator += min(radius, h)
        denominator += h
    return numerator / denominator

def rejection_sample(n, radius, samples=120000):
    # Draw oriented lines with normal theta and signed offset p from
    # the ambient rectangle [0,pi) x [-1,1]. Reject lines missing K.
    kept = hits = 0
    for _ in range(samples):
        theta = math.pi * RNG.random()
        offset = 2*RNG.random()-1
        if -support(n, theta + math.pi) <= offset <= support(n, theta):
            kept += 1
            hits += abs(offset) < radius
    return hits / kept, kept

def main():
    pairs = 0
    for n in (3, 4, 5, 7, 12, 24):
        for rho in (0.07, 0.4, 0.6, 0.8, 0.94, 0.995):
            calc = prediction(n, rho)
            quad = grid_integral(n, rho)
            assert abs(calc - quad) < 1.2e-5, (n, rho, calc, quad)
            pairs += 1
    trials = 0
    for n,rho in ((3,0.25), (3,0.93), (4,0.8), (7,0.85), (12,0.9)):
        estimate, kept = rejection_sample(n,rho,180000)
        assert abs(estimate-prediction(n,rho)) < 0.01,(n,rho,estimate,kept)
        trials += kept
    for rho in (0.05,0.15,0.5,0.8,0.96,0.995):
        prev=prediction(3,rho)
        for n in range(4,101):
            val=prediction(n,rho)
            assert prev>val,(rho,n,prev,val)
            prev=val
    print(f'VERIFY_OK quadrature_pairs={pairs} accepted_rejection_lines={trials} ordered_n=3..100 radii=6')

if __name__=='__main__':
    main()
