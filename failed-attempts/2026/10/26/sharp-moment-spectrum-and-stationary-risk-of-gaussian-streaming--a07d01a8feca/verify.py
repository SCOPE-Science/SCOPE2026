"""Numerical diagnostics for Gaussian row-weighted Kaczmarz moment laws.

The accompanying proof, not these finite checks, establishes the theorem.
Run: python verify.py
"""
import math
import numpy as np
from scipy.special import gammaln


def inverse_moment(m, d, p, sigma=1.0):
    """Exact E[||a_selected||**(-p)] for squared-norm row weighting."""
    if not 0 <= p < min(d + 2, m * d):
        raise ValueError("p outside finite-moment domain")
    return math.exp(-p * math.log(2) / 2 - p * math.log(sigma)
                    + math.log(m * d / (m * d - p))
                    + gammaln((d + 2 - p) / 2)
                    - gammaln((d + 2) / 2))


def sample_selected(m, d, alpha, count, rng):
    """Draw the chosen Gaussian row, not a value of a normalized sketch."""
    rows = rng.standard_normal((count, m, d))
    r = np.linalg.norm(rows, axis=2)
    weights = r ** alpha
    probs = weights / weights.sum(axis=1, keepdims=True)
    u = rng.random(count)
    ix = np.sum(u[:, None] > np.cumsum(probs, axis=1), axis=1)
    ix = np.minimum(ix, m-1)
    return rows[np.arange(count), ix], r[np.arange(count), ix]


def run():
    rng = np.random.default_rng(1827)
    checks = 0
    # Direct exact finite-row conditional expectation identity (all rational).
    from fractions import Fraction
    for ss in ([1, 2], [1, 3, 8], [2, 3, 5, 7], [1, 1, 1, 1, 1]):
        total = sum(ss)
        lhs = sum(Fraction(z, total) * Fraction(1, z) for z in ss)
        assert lhs == Fraction(len(ss), total)
        checks += 1
    # Beta--Gamma reduction and its second-moment corollary.
    for m in range(1, 9):
        for d in range(1, 7):
            if m * d > 2:
                assert abs(inverse_moment(m,d,2) - m/(m*d-2)) < 5e-12
                checks += 1
    # The selected row's first inverse moment is tested against its closed form.
    for m, d, alpha, p in [(2,1,2,0.6),(3,1,2,0.7),(2,2,2,1.0),
                            (3,2,2,1.0),(4,3,2,1.0)]:
        _, radius = sample_selected(m,d,alpha,400_000,rng)
        empirical = np.mean(radius**(-p))
        expected = inverse_moment(m,d,p)
        rel = abs(empirical - expected)/expected
        assert rel < 0.035, (m,d,p,empirical,expected,rel)
        checks += 1
    # Independently simulate multi-step Kaczmarz and compare exact MSE recursion.
    cases = [(3,3),(2,4),(4,3),(3,4)]
    n=100_000
    for m,d in cases:
        x=np.zeros((n,d))
        x[:,0]=1.0
        initial_mse=1.0
        q=1-1/d
        for k in range(1,5):
            rows, radii = sample_selected(m,d,2,n,rng)
            b = rng.standard_normal(n)
            u = rows/radii[:,None]
            x = x - np.einsum('ij,ij->i',x,u)[:,None]*u + (b/radii)[:,None]*u
            empirical=np.mean(np.sum(x*x,axis=1))
            expected=q**k*initial_mse + d*m/(m*d-2)*(1-q**k)
            assert abs(empirical-expected)/expected < .055,(m,d,k,empirical,expected)
            checks += 1
    print(f'PASS: {checks} exact-identity and independent stochastic diagnostics.')
    print('Boundary: for squared-norm sampling the second moment exists iff m*d>2.')
    print('All finite-sample diagnostics support, but do not establish, universal claims.')

if __name__=='__main__': run()
