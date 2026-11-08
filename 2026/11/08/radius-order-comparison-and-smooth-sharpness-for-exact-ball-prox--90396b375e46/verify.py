"""Reproducible arithmetic spot checks for a ball-constrained separable quadratic.
Run: python verify.py. Analytic universal statements are proved in RESULT.md.
"""
from decimal import Decimal, localcontext
from random import Random


def exact_ball_step(x, a, radius):
    """Numerically solve the exact trust-region KKT equations by Decimal bisection."""
    zero = Decimal(0)
    if sum(z * z for z in x) <= radius * radius:
        return [zero] * len(x)
    def displacement_sq(mu):
        return sum((aa * xx / (aa + mu)) ** 2 for xx, aa in zip(x, a))
    lo, hi = zero, Decimal(1)
    while displacement_sq(hi) > radius * radius:
        hi *= 2
    for _ in range(520):
        mu = (lo + hi) / 2
        if displacement_sq(mu) > radius * radius:
            lo = mu
        else:
            hi = mu
    mu = hi
    return [mu * xx / (aa + mu) for xx, aa in zip(x, a)]


def count_steps(x, a, radius):
    for k in range(len(x) + 4):
        if all(v == 0 for v in x):
            return k
        x = exact_ball_step(x, a, radius)
    raise AssertionError('finite-step bound failed')


def run():
    with localcontext() as ctx:
        ctx.prec = 170
        rng = Random(531823)
        tol = Decimal('1e-65')
        samples = 0
        for d in range(2, 7):
            for _ in range(48):
                a = [Decimal(str(10 ** rng.uniform(-3, 5))) for _ in range(d)]
                start = [Decimal(str(rng.uniform(0.1, 2.3))) for _ in range(d)]
                small = list(start)
                large = list(start)
                for k in range(4):
                    r = Decimal(str(rng.uniform(0.05, 1.15)))
                    R = r + Decimal(str(rng.uniform(0, 1.1)))
                    small = exact_ball_step(small, a, r)
                    large = exact_ball_step(large, a, R)
                    assert all(u <= v + tol for u, v in zip(large, small))
                    samples += 1
        for d in range(2, 8):
            success = False
            for eps_text in ['.01', '.000001', '1e-20', '1e-50']:
                eps = Decimal(eps_text)
                a = [eps ** (-j) for j in range(d - 1, -1, -1)]
                x = [Decimal(1)] * d
                if count_steps(x, a, Decimal(1)) == d:
                    success = True
                    break
            assert success, ('missing sharp witness', d)
        print('VERIFY_OK', samples, 'ordered-trajectory checks; smooth sharpness d=2..7')


if __name__ == '__main__':
    run()
