#!/usr/bin/env python3
"""Numerical diagnostics for a fixed-pole spherical-hull clearance law.
Uses only numpy; run: python check.py
"""
import math
import itertools
import numpy as np

rng = np.random.default_rng(20261109)

def trial(n, mode, sample_count=1_000_000):
    epsilons = np.array([0.009, 0.018])
    counts = np.zeros(len(epsilons), dtype=int)
    contained_count = 0
    marked_cos_total = 0.0
    marked_count = 0
    for _ in range(sample_count // 50_000):
        z = rng.random((50_000, n))
        if mode == 'projected':
            z = np.sqrt(z)  # g(r)=2 sin(r) cos(r)
        phi = 2 * np.pi * rng.random((50_000, n))
        sin_r = np.sqrt(1 - z*z)
        xyz = np.stack([sin_r*np.cos(phi), sin_r*np.sin(phi), z], axis=2)
        az = np.sort(phi, axis=1)
        gaps = np.diff(np.concatenate([az, az[:, :1] + 2*np.pi], axis=1), axis=1)
        contains = gaps.max(axis=1) < np.pi
        contained_count += int(contains.sum())
        best = np.full(50_000, np.inf)
        best_cos = np.zeros(50_000)
        for i, j in itertools.combinations(range(n), 2):
            cross = np.cross(xyz[:,i,:], xyz[:,j,:])
            other_ids = [k for k in range(n) if k not in (i,j)]
            others = xyz[:,other_ids,:]
            # The north pole and all non-edge vertices must be on the same side.
            supporting = np.all(np.einsum('mki,mi->mk', others, cross) * cross[:, 2:3] >= 0, axis=1)
            d = np.arcsin(np.minimum(1, np.abs(cross[:,2]) / np.linalg.norm(cross, axis=1)))
            improvement = supporting & (d < best)
            best = np.where(improvement, d, best)
            best_cos = np.where(improvement, (z[:,i]+z[:,j])/2, best_cos)
        for idx, eps in enumerate(epsilons):
            counts[idx] += int(np.sum(contains & (best < eps)))
        marked = contains & (best < epsilons[0])
        marked_count += int(marked.sum())
        marked_cos_total += float(np.sum(best_cos[marked]))
    m_cot = 1.0 if mode == 'hemisphere' else math.pi / 2.0
    coefficient = n*(n-1)*m_cot/(math.pi * 2**(n-2))
    p_contain = 1 - n/2**(n-1)
    p_emp = contained_count/sample_count
    assert abs(p_emp-p_contain) < 0.004
    ratios = counts / (sample_count*epsilons*coefficient)
    # Simulations at nonzero epsilon have small systematic corrections.
    assert all(abs(ratio - 1) < 0.095 for ratio in ratios), ratios
    if mode == 'hemisphere' and n == 3:
        expected_mean_cos = 1/4+math.pi/8
        measured = marked_cos_total/marked_count
        assert abs(measured-expected_mean_cos) < 0.04, measured
        print('marked_cos', measured, 'theory', expected_mean_cos)
    print('n',n,'mode',mode,'inside',round(p_emp,7),'theory',round(p_contain,7),
          'coefficient',round(coefficient,8),'tail_ratios',np.round(ratios,5).tolist(),
          'rare_samples',counts.tolist())

if __name__ == '__main__':
    for n in (3,4,5,6): trial(n,'hemisphere')
    for n in (3,5): trial(n,'projected')
    print('POLE_CLEARANCE_COTANGENT_MARKED_LAW_DIAGNOSTIC_OK')
