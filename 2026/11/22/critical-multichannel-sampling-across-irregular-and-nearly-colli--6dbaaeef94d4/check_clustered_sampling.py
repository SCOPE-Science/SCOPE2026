"""Finite-section diagnostics for the clustered multi-channel sampling theorem.
These tests corroborate formulas; the infinite-dimensional result is analytic.
"""
import math
import numpy as np


def phi(u):
    return math.exp(u / 2 - math.exp(u)) if u < 600 else 0.0


def trial(r, clusters, separation, offset, seed):
    rng = np.random.default_rng(seed)
    x = np.array([(k + 1) * separation for k in range(clusters)])
    delta = rng.uniform(-offset, offset, (clusters, r))
    shift = (x[:, None] + delta).ravel()
    decay = np.exp(-shift)
    us = []
    for k in range(clusters):
        q, _ = np.linalg.qr(rng.standard_normal((r, r)))
        us.append(q)
    columns = np.concatenate([us[k] for k in range(clusters)], axis=1)
    f = np.empty((clusters * r, clusters * r))
    for k in range(clusters):
        for j in range(clusters):
            for a in range(r):
                for b in range(r):
                    f[k*r+a, j*r+b] = us[j][a, b] * phi(x[k] - shift[j*r+b])
    singular = np.linalg.svd(f, compute_uv=False)
    assert singular[-1] > .15, ('sample', r, singular[-1])
    # Exact summation of the original integer-time Gram series.
    g = np.empty((clusters*r, clusters*r))
    for k in range(clusters):
        for a in range(r):
            ia = k*r+a
            for j in range(clusters):
                for b in range(r):
                    ib = j*r+b
                    g[ia,ib] = (us[k][:,a] @ us[j][:,b]) * math.sqrt(decay[ia]*decay[ib]) / (-math.expm1(-decay[ia]-decay[ib]))
    eig = np.linalg.eigvalsh((g+g.T)/2)
    assert eig[0] > .30, ('original', r, eig[0])
    for k in range(clusters):
        for u in [x[k]-offset-.01, x[k]-.05, x[k]+.05, x[k]+offset+.01]:
            modes = int(np.count_nonzero(shift <= u))
            times = int(np.count_nonzero(x <= u))
            assert abs(modes-r*times) <= r
    return (r, clusters, float(singular[-1]), float(eig[0]))

if __name__ == '__main__':
    checks=[]
    for r in [2,3,4]:
        for n in [3,6,9]:
            for seed in [3,17,83]:
                checks.append(trial(r,n,12,.25,seed))
    for x in checks:
        print('r=%d clusters=%d sampled_min=%.7f original_gram_min=%.7f'%x)
    print('CLUSTERED_CRITICAL_MULTICHANNEL_OK',len(checks))
