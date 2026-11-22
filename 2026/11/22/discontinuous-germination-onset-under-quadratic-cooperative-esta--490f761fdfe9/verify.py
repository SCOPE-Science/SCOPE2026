#!/usr/bin/env python3
"""Arithmetic diagnostics for an explicit two-season germination payoff.

Finite checks accompany, and do not replace, the analytic proof.
"""
import math


def h(r, t):
    return math.log1p(2.0 * r * (math.cosh(t) - 1.0))


def hp(r, t):
    return 2.0 * r * math.sinh(t) / (1.0 + 2.0 * r * (math.cosh(t) - 1.0))


def hpp(r, t):
    c = math.cosh(t)
    z = 1.0 + 2.0 * r * (c - 1.0)
    return 2.0 * r * ((1.0 - 2.0 * r) * c + 2.0 * r) / (z * z)


def bisect(f, lo, hi, n=110):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0, (flo, fhi)
    for _ in range(n):
        m = (lo + hi) / 2.0
        if f(m) * flo > 0:
            lo, flo = m, f(m)
        else:
            hi = m
    return (lo + hi) / 2.0


def critical(r):
    assert r > 1.0
    t0 = math.acosh(2.0 * r / (2.0 * r - 1.0))
    assert hpp(r, t0 * 0.5) > 0 and hpp(r, t0 * 2) < 0
    fun = lambda t: t * hp(r, t) - h(r, t)
    tc = bisect(fun, t0, 40.0)
    pc = 1.0 / hp(r, tc)
    return t0, tc, pc


checks = 0
for r, tc_expected, pc_expected, gc_expected in [
    (2.0, 1.8059261854298116, 0.8021787500060076, 0.8356778067451832),
    (4.0, 1.1041718746824627, 0.5951834959335222, 0.6685147200388231),
    (10.0, 0.6520870923803185, 0.3864620696083972, 0.47904264478858505),
    (100.0, 0.1988005170718255, 0.12406010900953593, 0.18028660414712872),
    (10000.0, 0.01980367964643721, 0.012426134517116605, 0.019608874852650726),
]:
    t0, tc, pc = critical(r)
    assert abs(tc - tc_expected) < 1e-10
    assert abs(pc - pc_expected) < 1e-10
    assert abs(1.0-math.exp(-tc) - gc_expected) < 1e-10
    checks += 3
    assert 0.0 < t0 < tc and 0.0 < pc < 1.0
    assert abs(pc * h(r, tc) - tc) < 1e-10
    assert abs(pc * hp(r, tc) - 1.0) < 1e-10
    checks += 3
    for p in [pc-0.01 * pc, pc, pc+0.01 * (1-pc)]:
        values = [-t + p * h(r, t) for t in [j / 500.0 for j in range(0, 10001)]]
        if p < pc:
            assert max(values) <= 1e-12
        elif p > pc:
            assert max(values) > 0
        else:
            assert abs(-tc+p*h(r,tc)) < 1e-10
        checks += 1

# The analogous linear return has a continuous optimizer after p = 1/r.
for r in [2,4,10,100]:
    p0 = 1/r
    for p in [p0*.9, p0, p0 + .1*(1-p0)]:
        gmax = max(0.,(p*r-1.)/(r-1.))
        linear = lambda g: (1-p)*math.log1p(-g) + p*math.log1p((r-1.)*g)
        assert all(linear(gmax) >= linear(g)-1e-10 for g in [j/1000 for j in range(1000)])
        checks += 1

u = bisect(lambda u: math.log(u)-2*(1.-1./u), 2.01, 10.0)
x = math.sqrt(u-1.0)
c = x/math.log(u)
assert abs(u-4.921553634567505)<1e-11
assert abs(x-1.980291300432213)<1e-11
assert abs(c-1.2426337563300258)<1e-11
checks += 3
for r in [10**4,10**5,10**6]:
    _, tc, pc = critical(r)
    assert abs(tc*math.sqrt(r)/x-1) < 0.003
    assert abs(pc*math.sqrt(r)/c-1) < 0.003
    checks += 2
print('PASS', checks, 'assertion groups; all numeric checks supplement the exact proof')
