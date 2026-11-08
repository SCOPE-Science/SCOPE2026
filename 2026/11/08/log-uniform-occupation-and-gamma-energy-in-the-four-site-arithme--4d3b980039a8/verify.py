"""Independent finite checks for the four-site nonnegative-occupation Gibbs model.

Requires Python 3 and NumPy. Finite computations are diagnostics, not an
infinite-temperature proof. All couplings are positive.
"""
from fractions import Fraction
from itertools import product
import math
import numpy as np


def counts_with_cap(total, cap):
    return sum(1 for x in range(cap + 1) if 0 <= total - x <= cap)


def check_finite_enumeration():
    tested = 0
    for cap in range(1, 5):
        for fugacity, edgeweight in [(Fraction(2, 3), Fraction(1, 4)),
                                     (Fraction(3, 5), Fraction(4, 7))]:
            direct = Fraction(0)
            for n1, n2, n3, n4 in product(range(cap + 1), repeat=4):
                A, B = n1 + n3, n2 + n4
                direct += fugacity ** (A + B) * edgeweight ** (A * B)
            grouped = sum(
                (counts_with_cap(a, cap) * counts_with_cap(b, cap)
                 * fugacity ** (a + b) * edgeweight ** (a * b))
                for a in range(2 * cap + 1)
                for b in range(2 * cap + 1)
            )
            assert direct == grouped
            tested += 1
    return tested


def moments(beta, kappa, mu, cutoff=25.0):
    """Single series with tail controlled by exp(-beta*mu*b)."""
    maximum = int(math.ceil(cutoff / (beta * mu)))
    b = np.arange(maximum + 1, dtype=np.float64)
    lam = beta * (mu + kappa * b)
    den = -np.expm1(-lam)
    w = (b + 1) * np.exp(-beta * mu * b) / den**2
    Z = float(np.sum(w))
    prob = w / Z
    L = math.log(1 / (beta * kappa))
    t = np.log1p(b) / L
    mean_t = float(np.dot(prob, t))
    var_t = float(np.dot(prob, (t - mean_t)**2))
    cond_energy = 2 * beta * (mu + kappa * b) / np.expm1(lam) + beta * mu * b
    # The conditional mean total energy also follows directly from -d log Z / d beta.
    scaled_energy = float(np.dot(prob, cond_energy))
    # Exact conditional Laplace transform of beta*kappa*A*B.
    s = 1.0
    cond_laplace = (den / (-np.expm1(-(lam + s * beta * kappa * b))))**2
    laplace = float(np.dot(prob, cond_laplace))
    return dict(Z=Z, amplitude=(beta*kappa)**2 * Z / L,
                tmean=mean_t, tvariance=var_t, scaled_energy=scaled_energy,
                laplace=laplace)


def main():
    exact = check_finite_enumeration()
    cases = [0.002, 0.0005, 0.0001, 0.00002]
    kappa, mu = 2.0, 1.0
    outputs = []
    for beta in cases:
        d = moments(beta, kappa, mu)
        assert d['Z'] > 1 and 0 <= d['laplace'] <= 1
        assert 0.4 < d['tmean'] < 0.6
        assert 0 < d['scaled_energy'] < 3
        outputs.append(d)
        print('beta=',beta,'amplitude-ratio=',round(d['amplitude'],9),
              'log-B mean=',round(d['tmean'],9),
              'log-B variance=',round(d['tvariance'],9),
              'scaled total E=',round(d['scaled_energy'],9),
              'laplace(s=1)=',round(d['laplace'],9))
    # Directional asymptotic diagnostics, not error bars or proofs of limits.
    assert all(outputs[i+1]['amplitude'] < outputs[i]['amplitude']
               for i in range(len(outputs)-1))
    assert all(abs(outputs[i+1]['tmean']-0.5) < abs(outputs[i]['tmean']-0.5)
               for i in range(len(outputs)-1))
    assert all(outputs[i+1]['tvariance'] < outputs[i]['tvariance']
               for i in range(len(outputs)-1))
    assert all(outputs[i+1]['scaled_energy'] < outputs[i]['scaled_energy']
               for i in range(len(outputs)-1))
    print(f'PASS: {exact} exact finite-cap comparisons; {len(cases)} positive-series asymptotic diagnostics')


if __name__ == '__main__':
    main()
