#!/usr/bin/env python3
"""Finite arithmetic and independent matrix checks for two-tap affine frames.

Run with: python3 verify_wavelet_two_tap.py
The universal proof is in RESULT.md; finite tests do not replace it.
"""
import cmath
import math


def predicted(p, scales, cross):
    scales = set(scales)
    negatives = {(-s) % p for s in scales}
    all_scales = set(range(1, p))
    symmetric = scales == negatives
    skew = not (scales & negatives) and (scales | negatives) == all_scales
    mean_zero_tight = (scales == all_scales or
                       (symmetric and cross.real == 0) or
                       (skew and cross.imag == 0))
    full_tight = symmetric and cross.real == 0
    return mean_zero_tight, full_tight


def eigenvalues(p, scales, a, b):
    omega = cmath.exp(2j * math.pi / p)
    return [sum(abs(a + b * omega ** (s * k)) ** 2 for s in scales)
            for k in range(p)]


def weighted_predicted(p, weights, cross):
    weights = {s: weights.get(s,0) for s in range(1,p)}
    equal_pairs = all(weights[s] == weights[p-s] for s in range(1,p))
    sums = [weights[s]+weights[p-s] for s in range(1,p)]
    balanced_pairs = len(set(sums)) == 1
    uniform = len(set(weights.values())) == 1
    u,v = cross.real,cross.imag
    if abs(u)<1e-12:
        projected_tight = equal_pairs
    elif abs(v)<1e-12:
        projected_tight = balanced_pairs
    else:
        projected_tight = uniform
    full_tight = abs(u)<1e-12 and equal_pairs
    return projected_tight,full_tight


def weighted_eigenvalues(p, weights, a, b):
    omega = cmath.exp(2j * math.pi / p)
    return [sum(w*abs(a+b*omega**(s*k))**2 for s,w in weights.items())
            for k in range(p)]


def run():
    tested = 0
    phases = [(1, 1), (1, -1), (1, 1j), (1, 1+1j), (1, 2j), (1, 2)]
    for p in (3, 5, 7, 11):
        count = 0
        for bits in range(1, 1 << (p-1)):
            scales = [s + 1 for s in range(p-1) if bits & (1 << s)]
            for a,b in phases:
                vals = eigenvalues(p, scales, a, b)
                cross = a * complex(b).conjugate()
                actual = (max(vals[1:]) - min(vals[1:]) < 1e-8,
                          max(vals) - min(vals) < 1e-8)
                assert predicted(p, scales, cross) == actual, (p,scales,a,b)
                count += 1
        tested += count
        print(f'CLASSIFICATION_PASS p={p} cases={count}')
    p = 7
    scales = (1, 2, 4)
    # Exhaust nonnegative integer weights for all nonzero scales.
    weighted_count = 0
    for p in (3,5,7):
        for index in range(1,3**(p-1)):
            digits = []
            x = index
            for _ in range(p-1):
                digits.append(x%3);x//=3
            weights={s+1:digits[s] for s in range(p-1)}
            for a,b in phases:
                vals=weighted_eigenvalues(p,weights,a,b)
                actual=(max(vals[1:])-min(vals[1:])<1e-8,
                        max(vals)-min(vals)<1e-8)
                assert weighted_predicted(p,weights,a*complex(b).conjugate())==actual,(p,weights,a,b)
                weighted_count+=1
        print(f'WEIGHTED_CLASSIFICATION_PASS p={p}')
    # An independent time-coordinate computation of the frame matrix.
    S = [[0j for _ in range(p)] for _ in range(p)]
    for s in scales:
        for k in range(p):
            y = [0j] * p
            y[k] += 1
            y[(k+s) % p] -= 1
            for i in range(p):
                for j in range(p):
                    S[i][j] += y[i] * y[j].conjugate()
    for f in range(p):
        v = [cmath.exp(2j*math.pi*f*j/p) / math.sqrt(p) for j in range(p)]
        image = [sum(S[i][j]*v[j] for j in range(p)) for i in range(p)]
        target = 0 if f == 0 else p
        assert max(abs(image[i] - target*v[i]) for i in range(p)) < 1e-11
    print('DIRECT_MATRIX_PASS p=7 scales=1,2,4')
    for p in (3, 5, 7, 11, 13, 17):
        scales = [j for j in range(1, p) if j < (-j) % p]
        vals = eigenvalues(p, scales, 1, -1)
        assert abs(vals[0]) < 1e-11
        assert max(abs(v-p) for v in vals[1:]) < 1e-10
        survivors = eigenvalues(p, scales[1:], 1, -1)[1:]
        lower = p-2-2*math.cos(math.pi/p)
        upper = p-2+2*math.cos(2*math.pi/p)
        assert abs(min(survivors)-lower) < 1e-10
        assert abs(max(survivors)-upper) < 1e-10
        print(f'ERASURE_PASS p={p} scales={len(scales)} normalized_lower={lower/p:.12g} normalized_upper={upper/p:.12g}')
    print(f'TWO_TAP_AFFINE_PASS unweighted_cases={tested} weighted_cases={weighted_count}')


if __name__ == '__main__':
    run()
