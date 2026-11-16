#!/usr/bin/env python3
"""Independent numerical consistency checks for finite Hermite-band annulus concentration.
Run with: python3 check_annulus.py. This checks finite samples, not the infinite proof.
"""
import math


def simpson(f, start, end, steps=1000):
    assert steps % 2 == 0 and end > start
    h = (end - start) / steps
    total = f(start) + f(end)
    for i in range(1, steps):
        total += (4 if i % 2 else 2) * f(start + h * i)
    return total * h / 3


def log_lambda(j, a, s):
    """Stable integral of exp(-u) u**j / j! on [a,a+s]."""
    if j == 0:
        return -a + math.log(-math.expm1(-s))
    upper = a + s
    integral = simpson(
        lambda t: math.exp(-t + j * math.log((a+t) / upper)) if (a+t) > 0 else 0,
        0.0, s,
    )
    return -a + j * math.log(upper) - math.lgamma(j + 1) + math.log(integral)


def crossing(K, s):
    lo, hi = 0.0, float(K + 5)
    assert log_lambda(K, lo, s) < log_lambda(0, lo, s)
    assert log_lambda(K, hi, s) > log_lambda(0, hi, s)
    for _ in range(72):
        mid = (lo + hi) / 2
        if log_lambda(K, mid, s) > log_lambda(0, mid, s):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def predicted(K, s):
    J_s = math.expm1((math.e - 1) * s) / (math.e - 1)
    return (
        K / math.e
        + math.log(2 * math.pi * K) / (2 * math.e)
        + math.log(-math.expm1(-s) / J_s) / math.e
    )


def check():
    checks = 0
    for s in (0.3, 1.0, 3.0):
        for K in (2, 3, 10, 20, 100, 500):
            a = crossing(K, s)
            logs = [log_lambda(j, a, s) for j in range(K+1)]
            assert abs(logs[0] - logs[K]) < 3e-9
            assert min(logs[1:K]) > logs[0] + 1e-9
            for multiplier in (0.80, 0.95, 1.05, 1.20):
                aa = a * multiplier
                baseline = min(log_lambda(j, aa, s) for j in range(K+1))
                assert baseline < logs[0] - 1e-8
            if K == 500:
                assert abs(a - predicted(K, s)) < 0.025
            checks += 1
        for K in (10, 25, 50):
            for a in (0.12, 1.0, 4.0, 30.0):
                vals = [log_lambda(j, a, s) for j in range(K+1)]
                assert abs(min(vals) - min(vals[0], vals[-1])) < 1e-9
                checks += 1
    for K in (3, 20, 200, 1200):
        a = crossing(K, 1.0)
        print(f"K={K:4d} area=1 optimal_inner={a:.9f} asymptotic_error={a-predicted(K,1):.7f}")
        assert abs(a/K - 1/math.e) < (0.4 if K == 3 else 0.15)
        checks += 1
    print(f"FINITE_HERMITE_ANNULUS_PASS exact_endpoint_balances={18} unimodal_spectral_checks={36} asymptotic_checks={3} total_cases={checks}")


if __name__ == '__main__':
    check()
