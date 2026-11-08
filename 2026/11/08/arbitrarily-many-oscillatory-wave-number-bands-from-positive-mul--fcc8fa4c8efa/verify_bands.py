#!/usr/bin/env python3
"""Reproduce finite witnesses and normalized discriminant in a Gaussian-mixture closure.

This checks arithmetic, not the universal zero-count theorem.
"""
import math

def interaction_t(q, peaks):
    total = 0.0
    for z in peaks:
        u = q / z
        total += 2.0 * math.e * u * u * math.exp(-u * u)
    return total

def bisect_root(f, lo, hi, iterations=90):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(iterations):
        mid = (lo + hi) * 0.5
        fm = f(mid)
        if fm == 0:
            return mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) * 0.5

checks = 0
for count in range(1, 6):
    R = 32 * count
    peaks = [float(R ** j) for j in range(count)]
    witnesses = [0.0]
    for j, peak in enumerate(peaks):
        witnesses.append(peak)
        if j + 1 < count:
            witnesses.append(math.sqrt(peak * peaks[j + 1]))
    witnesses.append(50.0 * peaks[-1])
    vals = [interaction_t(z, peaks) - 1.0 for z in witnesses]
    for j, val in enumerate(vals):
        expected_positive = (j % 2 == 1)
        assert (val > 0) == expected_positive, (count, j, val)
        checks += 1
    zeros = []
    for a, b in zip(witnesses, witnesses[1:]):
        zero = bisect_root(lambda x: interaction_t(x, peaks) - 1.0, a, b)
        assert abs(interaction_t(zero, peaks)-1.0) < 1.e-9
        zeros.append(zero)
        checks += 1
    assert len(zeros) == 2 * count
    assert zeros == sorted(zeros)
    checks += 2
    print('K',count,'R',R,'zero_witnesses', ['%.8g'%x for x in zeros])

peaks = [1.0, 64.0]
P = 0.001
rho = Dr = Dt = 1.0
v0 = P / math.sqrt(2)
for q in [0.05, 0.5, 1, 1.5, 2.5, 8, 20, 40, 64, 100, 1000]:
    Vtilde = sum((2 * math.e / z**2) * math.exp(-(q/z)**2) for z in peaks)
    T = interaction_t(q, peaks)
    assert abs(T - q*q*Vtilde) <= 1e-12 * max(1,T)
    a = (Dt + rho*Vtilde) * q*q
    b = rho*v0
    c = -v0*q*q/(2*rho)
    d = Dr + Dt*q*q
    discriminant = (a-d)**2 + 4*b*c
    G = (1-T)/q
    target = Dr**2*q*q*(G**2-P**2)
    assert abs(discriminant-target) < 2e-10 * max(1,abs(target))
    checks += 2
print('PASS', checks, 'finite arithmetic and discriminant checks')
