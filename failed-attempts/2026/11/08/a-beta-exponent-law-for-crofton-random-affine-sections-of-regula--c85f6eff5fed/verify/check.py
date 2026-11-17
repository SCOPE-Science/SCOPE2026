"""Reproduce finite-dimensional checks for Gaussian-spacing simplex section law.

Dependencies: numpy, scipy. This is a finite diagnostic, not an asymptotic proof.
"""
from math import comb, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr


def exact_probabilities(n):
    # Expected spacing between consecutive standard-normal order statistics.
    # Integral = E[Z_(k+1)-Z_(k)] by the binomial counting identity.
    a = np.array([
        quad(lambda t: comb(n, k)*ndtr(t)**k*ndtr(-t)**(n-k),
             -12, 12, epsabs=1e-12, epsrel=1e-12)[0]
        for k in range(1, n)
    ])
    return a/a.sum()


def crofton_direct(n, samples=100_000, seed=1234):
    # Unit normals in the affine span of conv(e_1,...,e_n).
    # Offsets sampled independently over the full enclosing support interval.
    # Conditioning on actual intersection implements invariant affine-hyperplane measure.
    rng = np.random.default_rng(seed+n)
    z = rng.standard_normal((samples, n))
    u = z-z.mean(axis=1, keepdims=True)
    u /= np.linalg.norm(u, axis=1, keepdims=True)
    H = sqrt((n-1)/n)
    t = rng.uniform(-H, H, samples)
    hits = (t > u.min(axis=1)) & (t < u.max(axis=1))
    count = np.count_nonzero(u[hits] < t[hits, None], axis=1)
    frequencies = np.bincount(count, minlength=n+1)[1:n].astype(float)
    frequencies /= frequencies.sum()
    return np.count_nonzero(hits), frequencies


def validate_combinatorial_face_rule():
    # For each nontrivial split, every vertex is an intersection of a pair of
    # simplex vertices with heights on opposite sides of the hyperplane.
    for n in range(4, 11):
        for k in range(1, n):
            a = np.r_[-np.arange(1,k+1,dtype=float),
                      np.arange(1,n-k+1,dtype=float)]
            points = []
            for i in range(n):
                for j in range(i+1,n):
                    if a[i]*a[j] < 0:
                        lam = a[j]/(a[j]-a[i])
                        x = np.zeros(n)
                        x[i] = lam
                        x[j] = 1-lam
                        assert abs(x@a) < 1e-10
                        assert abs(sum(x)-1) < 1e-10
                        points.append(x)
            assert len(points) == k*(n-k)
            assert len({tuple(v.round(12)) for v in points}) == len(points)
    print('COMBINATORIAL_EDGE_CHECK_OK n=4..10')


def main():
    validate_combinatorial_face_rule()
    for n in (4,5,8):
        expected = exact_probabilities(n)
        hits, empirical = crofton_direct(n, samples=240_000)
        err = np.max(np.abs(expected-empirical))
        assert err < .012, (n, hits, err)
        print(f'FINITE_CROFTON_CHECK_OK n={n} hits={hits} max_abs_error={err:.5f}')
    p4=exact_probabilities(4)[1]
    assert abs(p4-0.288535543072)<1e-10
    print(f'FOUR_VERTEX_SIMPLEX_REFERENCE_OK p_quadrilateral={p4:.12f}')
    rng=np.random.default_rng(49091)
    x=0.5
    previous=1.
    for n in (200, 800, 3200):
        # This direct weighted-space statistic estimates the Crofton
        # probability; finite-n drift toward a slow extreme-value limit.
        total=0.; part=0.; k=int(n**x)
        for _ in range(7):
            z=np.sort(rng.standard_normal((1300,n)),axis=1)
            total += np.sum(z[:,-1]-z[:,0])
            part += np.sum(z[:,k]-z[:,0]+z[:,-1]-z[:,-k-1])
        p=part/total
        print(f'ASYMPTOTIC_DIAGNOSTIC n={n} x={x} finite_CDF={p:.6f} limit_CDF={1-sqrt(1-x):.6f}')
        assert p<previous
        previous=p
    print('GAUSSIAN_SPACING_SIMPLEX_CHECK_OK')

if __name__=='__main__': main()
