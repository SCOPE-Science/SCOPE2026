"""Reproducible numerical checks for a fixed-sample high-dimensional xMMD null law.
These checks supplement, and do not replace, the proof in RESULT.md.
Run: python check.py
"""
import json
import math
import numpy as np
from scipy.stats import norm, t


def statistic(a, b):
    """Two s-by-d samples in each half, using the published biased variances."""
    s = a.shape[0]//2
    assert a.shape == b.shape and s >= 2
    u = np.exp(-np.sum((a[:s,None,:]-a[None,s:,:])**2,axis=2)/(2*a.shape[1]))
    u -= np.exp(-np.sum((a[:s,None,:]-b[None,s:,:])**2,axis=2)/(2*a.shape[1]))
    v = np.exp(-np.sum((b[:s,None,:]-a[None,s:,:])**2,axis=2)/(2*a.shape[1]))
    v -= np.exp(-np.sum((b[:s,None,:]-b[None,s:,:])**2,axis=2)/(2*a.shape[1]))
    u = np.mean(u,axis=1)
    v = np.mean(v,axis=1)
    den = math.sqrt((np.mean((u-u.mean())**2)+np.mean((v-v.mean())**2))/s)
    return (u.mean()-v.mean())/den if den>0 else float('nan')


def linear_statistic(a,b):
    s = a.shape[0]//2
    g = a[s:].mean(axis=0)-b[s:].mean(axis=0)
    u = a[:s] @ g
    v = b[:s] @ g
    den = math.sqrt((np.mean((u-u.mean())**2)+np.mean((v-v.mean())**2))/s)
    return (u.mean()-v.mean())/den if den > 0 else float('nan')


def run():
    target = {}
    z = norm.ppf(0.95)
    for s in [2,3,4,5,10,20,50]:
        p = float(t.sf(z*math.sqrt((s-1)/s),df=2*s-2))
        assert p > .05 and p < .5
        target[str(s)] = p
    assert abs(target['2']-0.18240016325464486)<1e-12
    assert abs(target['3']-0.125203944838807)<1e-12
    assert abs(target['4']-0.10208843423911236)<1e-12
    assert abs(target['2']-(.5*(1-z/math.sqrt(z*z+4))))<1e-14
    assert all(target[str(a)]>target[str(b)] for a,b in [(2,3),(3,4),(4,5),(5,10),(10,20),(20,50)])

    rng = np.random.default_rng(970321)
    # The *linear* statistic has exactly the scaled t null law under normality
    # for any finite dimension, conditional on the second split.
    s = 2
    draws = 3000
    lin = np.empty(draws)
    for j in range(draws):
        x,y = rng.normal(size=(2,2*s,4))
        lin[j] = linear_statistic(x,y)
    lin_emp = float(np.mean(lin>z))
    assert abs(lin_emp-target['2']) < .025

    # A finite-dimensional RBF check at the prescribed squared bandwidth = d.
    # It checks implementation and the predicted limit, not convergence itself.
    empirical = {}
    for d in [128, 512, 2048]:
        r = np.empty(1200)
        for j in range(len(r)):
            a = rng.normal(size=(4,d))
            b = rng.normal(size=(4,d))
            r[j] = statistic(a,b)
        assert np.all(np.isfinite(r))
        empirical[str(d)] = float(np.mean(r>z))
    assert abs(empirical['2048']-target['2']) < .045
    # Compare RBF and linear approximations on the same coupled coordinates.
    a,b = rng.normal(size=(2,4,8192))
    comparisons = {}
    for d in [256,1024,4096,8192]:
        comparisons[str(d)] = float(abs(statistic(a[:,:d],b[:,:d])-linear_statistic(a[:,:d],b[:,:d])))
    assert comparisons['8192'] < 0.15
    return {"limiting_one_sided_size_at_normal_0_05":target,
            "linear_gaussian_null_empirical_size_3000_draws":lin_emp,
            "rbf_gaussian_empirical_size_1200_draws":empirical,
            "coupled_rbf_vs_linear_absolute_difference":comparisons,
            "assertions": "passed", "limitations": "Finite Monte Carlo checks, not mathematical proof."}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
