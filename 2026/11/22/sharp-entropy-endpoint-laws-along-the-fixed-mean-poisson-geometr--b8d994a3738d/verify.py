#!/usr/bin/env python3
"""Numerical checks for the stated Poisson--geometric entropy path.
No network access, external files, or third-party Python packages required.
All analytical infinite/continuum conclusions belong to the accompanying proof.
"""
import math


def pmf(mu, t, nmax=1400):
    if not (mu > 0 and 0 <= t <= mu):
        raise ValueError('mu > 0 and 0 <= t <= mu are required')
    lam = mu - t
    q = t / (1.0 + t)
    poisson = math.exp(-lam)
    a = math.exp(-lam) / (1.0 + t)
    result = [a]
    for n in range(1, nmax):
        poisson *= lam / n
        a = q * a + (1.0 - q) * poisson
        result.append(a)
    return result


def entropy(p):
    return -sum(v * math.log(v) for v in p if v > 0)


def poisson_endpoint_coefficient(mu):
    p = math.exp(-mu)
    total = 0.0
    for n in range(1200):
        total += p * math.log((n + 2) / (n + 1))
        p *= mu / (n + 1)
    return total / 2.0


def near(a, b, absolute, relative=0):
    if abs(a - b) > absolute + relative * abs(b):
        raise AssertionError(f'mismatch {a!r} != {b!r}')


def main():
    # Finite verification is not used as proof of monotonicity or convex ordering.
    for mu in (0.5, 2.0, 5.0):
        hs = []
        for j in range(21):
            t = mu * j / 20
            p = pmf(mu, t)
            near(sum(p), 1.0, 3e-12)
            mean = sum(n * v for n, v in enumerate(p))
            var = sum((n - mu) ** 2 * v for n, v in enumerate(p))
            near(mean, mu, 3e-9)
            near(var, mu + t * t, 5e-8)
            hs.append(entropy(p))
            if 0 < j < 20:
                # Avoid underflow by testing strictly positive mass positions.
                for n in range(1, 70):
                    if p[n - 1] * p[n + 1] > 1e-285:
                        if p[n] ** 2 <= p[n - 1] * p[n + 1] * (1 - 2e-13):
                            raise AssertionError('log-concavity violated')
        if not all(x < y for x, y in zip(hs, hs[1:])):
            raise AssertionError('entropy grid not increasing')
        # First endpoint: (H(t)-H(0))/t^2 --> E log((N+2)/(N+1))/2.
        c0 = poisson_endpoint_coefficient(mu)
        tsmall = 0.0005
        ratio0 = (entropy(pmf(mu, tsmall)) - hs[0]) / (tsmall ** 2)
        near(ratio0, c0, 1.3e-3)
        # Other endpoint: (H(mu)-H(mu-eps))/eps^2 --> 1/[2(1+mu)].
        eps = 0.0006
        ratio1 = (hs[-1] - entropy(pmf(mu, mu - eps))) / eps ** 2
        near(ratio1, 1 / (2 * (1 + mu)), 1.3e-3)
        # The coefficientwise endpoint score is exactly mean-zero and has
        # squared norm 1/(1+mu) under the geometric reference law.
        q = mu / (1 + mu)
        g0 = 1 - q
        s0 = q
        score_mean = g0 * s0
        fisher = g0 * s0 * s0
        g = g0
        for n in range(1, 1400):
            g *= q
            s = (n - 1 - 2 * mu) / (mu * (1 + mu))
            score_mean += g * s
            fisher += g * s * s
        near(score_mean, 0, 1e-10)
        near(fisher, 1 / (1 + mu), 1e-10)
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
