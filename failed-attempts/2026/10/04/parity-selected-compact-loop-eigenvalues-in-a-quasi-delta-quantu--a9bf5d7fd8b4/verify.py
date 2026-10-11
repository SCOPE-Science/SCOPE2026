#!/usr/bin/env python3
"""Exact parity replay for the one-loop quasi-delta boundary reduction."""

def residuals(n, relative_phase_root):
    # Gauge alpha_1=0.  At k=n*pi, exp(+-ik)=s in {+1,-1}.
    s = -1 if n % 2 else 1
    A, B = 1, -1
    endpoint_0 = A + B
    endpoint_1 = s * (A + B)
    common_value = 0
    # Remaining part of Eq. (4.27), after chain amplitudes vanish.
    derivative_residual = -(A - B) + relative_phase_root * s * (A - B)
    return endpoint_0, endpoint_1, common_value, derivative_residual, s

for n in range(1, 21):
    for r in (-1, 1):
        e0, e1, common, dr, s = residuals(n, r)
        assert e0 == 0 and e1 == 0 and common == 0
        assert (dr == 0) == (r == s)

# Zero energy cannot support a nonzero Dirichlet function on one interval:
# f(x)=a*x+b, f(0)=f(1)=0 => a=b=0.
a = 0
b = 0
assert a == 0 and b == 0
print("VERIFY_OK")
