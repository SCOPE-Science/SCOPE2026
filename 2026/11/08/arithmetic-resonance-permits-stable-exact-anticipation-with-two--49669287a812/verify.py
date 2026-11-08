"""Checks for exact multi-frequency anticipation under an aliased delay law."""
import cmath
import math

omega = (1.0, 2.0)
lead = math.pi / 6
common = 2 * math.pi
delays = (lead, lead + common)
weights = (0.5, 0.5)
max_delay = max(delays)
gain = 0.01
c = min(math.cos(w * lead) for w in omega)
assert gain < c / (4 * max_delay)

# Cancellation of the feedback term along the anticipated trajectory.
for w in omega:
    for t in (0.0, 0.2, 1.3, 4.7):
        x = cmath.exp(1j * w * t)
        feedback = sum(p * cmath.exp(1j * w * (t + lead - s)) for p,s in zip(weights, delays))
        assert abs(feedback - x) < 1e-13
    laplace = sum(p * cmath.exp(-1j * w * s) for p,s in zip(weights,delays))
    assert abs(laplace - cmath.exp(-1j * w * lead)) < 1e-13

# All characteristic roots with nonnegative real part, if any, lie in
# |lambda-i*omega| <= gain; on this disk the delayed multiplier has
# positive real part. The characteristic equation forbids such a root.
error_bound = max_delay * gain * math.exp(max_delay * gain)
assert error_bound < c

# Incommensurate frequency ratios have no nonzero common period; for
# commensurate 1:2 frequencies, the first positive common period is 2*pi.
for w in omega:
    assert abs(cmath.exp(1j * w * common) - 1) < 1e-14
assert abs(cmath.exp(1j * math.sqrt(2) * common) - 1) > 0.1
print('VERIFY_OK exact_feedback_cancellations=8 characteristic_root_exclusion=1 explicit_gain=0.01 commensurate_alias=2')
