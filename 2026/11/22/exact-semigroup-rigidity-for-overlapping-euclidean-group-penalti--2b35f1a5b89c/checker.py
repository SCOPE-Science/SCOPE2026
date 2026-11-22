#!/usr/bin/env python3
"""Reproducibility checks for the group-Euclidean resolvent semigroup theorem.

Run: python check.py (requires numpy and scipy). Analytic arguments, not finite
sampling, establish the all-family assertion; this checks algebra and instances.
"""
import itertools
import math
import numpy as np
from scipy.optimize import root


def gradient_hessian(x, groups, weights):
    x = np.asarray(x, dtype=float)
    n = len(x)
    g = np.zeros(n)
    h = np.zeros((n, n))
    for S, weight in zip(groups, weights):
        S = np.asarray(S, dtype=int)
        v = x[S]
        r = np.linalg.norm(v)
        if r <= 0:
            raise ValueError("all active group subvectors must be nonzero")
        g[S] += weight * v / r
        h[np.ix_(S, S)] += weight * (np.eye(len(S))/r - np.outer(v,v)/(r**3))
    return g, h


def prox_smooth(x, step, groups, weights):
    x = np.asarray(x, dtype=float)
    def residual(z):
        return z + step * gradient_hessian(z, groups, weights)[0] - x
    sol = root(residual, x, tol=1e-12)
    if not sol.success and np.linalg.norm(residual(sol.x)) > 1e-10:
        raise RuntimeError(str(sol.message))
    assert np.linalg.norm(residual(sol.x)) < 1e-9
    return sol.x


def partition_type(groups):
    return all(set(a) == set(b) or set(a).isdisjoint(b)
               for a, b in itertools.combinations(groups,2))


def explicit_witness(n, groups, weights):
    """Produce the theorem's bounded positive vector when groups overlap."""
    for S in groups:
        for i,j in itertools.permutations(S,2):
            left = sum(w for G,w in zip(groups,weights) if i in G and j not in G)
            right = sum(w/math.sqrt(len(G)) for G,w in zip(groups,weights)
                        if j in G and i not in G)
            if left > 0 or right > 0:
                # If left=0, swap i,j to ensure it is strictly positive.
                if left == 0:
                    i,j=j,i
                    left = sum(w for G,w in zip(groups,weights) if i in G and j not in G)
                    right = sum(w/math.sqrt(len(G)) for G,w in zip(groups,weights)
                                if j in G and i not in G)
                M = 1.0 if right == 0 else 1.0+left/right
                x = np.ones(n)
                x[i] = M
                assert left > 0
                c_i = sum(w/np.linalg.norm(x[list(G)]) for G,w in zip(groups,weights) if i in G)
                c_j = sum(w/np.linalg.norm(x[list(G)]) for G,w in zip(groups,weights) if j in G)
                assert abs(c_i-c_j)>1e-10
                return x, (i,j)
    raise ValueError("no overlap pair")


def checks():
    count = 0
    # Exact smallest partially overlapping example:
    # groups {0,1},{1,2}, x=(1,1,1).
    G=[(0,1),(1,2)]
    W=[1.,1.]
    x=np.ones(3)
    g,h=gradient_hessian(x,G,W)
    expected = np.array([-0.25, 0.5,-0.25])
    assert np.allclose(h@g,expected,atol=1e-13)
    assert abs(g@h@g - math.sqrt(2)/4)<1e-13
    count += 2
    # Verify the coefficient of the two-step resolvent defect, not only Hg.
    for step in [1/25,1/50,1/100,1/200,1/400,1/800]:
        t=prox_smooth(x,step,G,W)
        delta=(prox_smooth(t,step,G,W)-prox_smooth(x,2*step,G,W))/step**2
        assert np.max(np.abs(delta+expected)) < 6*step
        count += 1
    # Check all group families of distinct nonempty subsets of 3 coordinates,
    # and many sampled 4-coordinate families (finite sanity checks only).
    rng=np.random.default_rng(12345)
    for n in [2,3,4]:
        subsets=[tuple(i for i in range(n) if mask & (1<<i)) for mask in range(1,1<<n)]
        families=[]
        if n<=3:
            for k in range(1,min(len(subsets),4)+1):
                families.extend(itertools.combinations(subsets,k))
        else:
            for _ in range(240):
                k=int(rng.integers(1,7))
                indices=rng.choice(len(subsets),size=k,replace=False)
                families.append(tuple(subsets[int(i)] for i in indices))
        for groups in families:
            weights=[float(1.0+0.25*j) for j in range(len(groups))]
            if partition_type(groups):
                # Exact formula for duplicate/disjoint blocks, sampled at h.
                y=np.arange(1,n+1,dtype=float)
                def blockprox(t):
                    out=y.copy()
                    for S in set(groups):
                        weight=sum(w for G,w in zip(groups,weights) if G==S)
                        vec=y[list(S)]
                        out[list(S)] = max(0.,1.-t*weight/np.linalg.norm(vec))*vec
                    return out
                def apply_block(z,t):
                    out=z.copy()
                    for S in set(groups):
                        weight=sum(w for G,w in zip(groups,weights) if G==S)
                        vec=z[list(S)]
                        out[list(S)]=max(0.,1.-t*weight/np.linalg.norm(vec))*vec if np.linalg.norm(vec)>0 else vec
                    return out
                for s,t in [(0.1,0.15),(0.4,0.8),(2.0,1.0)]:
                    assert np.allclose(apply_block(blockprox(t),s), blockprox(t+s),atol=1e-12)
                    count += 1
            else:
                xx, pair=explicit_witness(n,groups,weights)
                gg,hh=gradient_hessian(xx,groups,weights)
                assert np.linalg.norm(hh@gg)>1e-10, (n,groups,xx,pair,hh@gg)
                assert gg@hh@gg>1e-12
                assert np.linalg.eigvalsh(hh).min()>-2e-11
                count+=3
    # Diagnostic example from two nested groups, including a singleton.
    G=[(0,),(0,1)]; x=np.ones(2)
    gg,hh=gradient_hessian(x,G,[1.,1.])
    assert np.allclose(hh@gg,np.array([1.,-1.])/(2*math.sqrt(2)))
    count+=1
    return count

if __name__ == "__main__":
    print(f"PASS: {checks()} supplementary assertions; exact symbolic coefficients proved in RESULT.md")
