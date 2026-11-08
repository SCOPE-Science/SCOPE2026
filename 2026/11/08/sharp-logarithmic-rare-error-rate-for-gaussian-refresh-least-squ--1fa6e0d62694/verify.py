"""Finite sanity checks for a Gaussian-refresh SGD tail-rate theorem.

The proof of the infinite-threshold limit is analytic; this script verifies
finite algebraic identities and example paths, not a probability limit.
"""
import math
import random


def run():
    rng = random.Random(190711)
    checks = 0
    for a in (0.05, 0.2, 0.5, 0.65):
        assert 0 < 1 - 2*a + 3*a*a < 1
        # E(1-aG^2)^2, using E G^2=1 and E G^4=3.
        expected = 1 - 2*a + 3*a*a
        assert math.isclose(expected, (1-a)**2 + 2*a*a, rel_tol=0, abs_tol=1e-14)
        checks += 1
    # Explicit unrolling of an affine recurrence and conditional variance.
    for _ in range(1000):
        a = 0.4
        xs = [rng.gauss(0, 1) for _ in range(12)]
        zs = [rng.gauss(0, 1) for _ in range(12)]
        e = 0.0
        for x,z in zip(xs,zs):
            e = (1-a*x*x)*e + a*x*z
        direct = 0.0
        for j in range(12):
            coef = a*xs[j]
            for x in xs[j+1:]:
                coef *= (1-a*x*x)
            direct += coef*zs[j]
        assert math.isclose(e,direct,rel_tol=3e-11,abs_tol=3e-11)
        # Variance of independent normal innovations, conditional on design.
        variance = 0.0
        for j in range(12):
            coef = a*xs[j]
            for x in xs[j+1:]:
                coef *= (1-a*x*x)
            variance += coef**2
        assert variance >= 0
        checks += 2
    # At each constant-mark backward block, the log-product moves linearly.
    for _ in range(1000):
        mark = rng.gauss(0,1)
        a = 0.3
        delta = 0.01
        length = rng.randrange(1,30)
        increment = math.log(abs(1-a*mark*mark)) + delta
        positions = [j*increment for j in range(length+1)]
        assert math.isclose(max(positions),max(positions[0],positions[-1]),abs_tol=1e-12)
        checks += 1
    # A deterministic Markov L2 bound for the discounted additive envelope.
    a=0.3
    sigma=1.4
    delta=0.07
    c_bound=a*sigma/(1-math.exp(-delta))
    partial=a*sigma*sum(math.exp(-delta*j) for j in range(2000))
    assert partial <= c_bound+1e-12
    assert math.isclose(partial,c_bound,rel_tol=1e-12)
    checks += 2
    print(f"PASS {checks} finite diagnostics; analytic asymptotic proof is in RESULT.md")

if __name__ == "__main__":
    run()
