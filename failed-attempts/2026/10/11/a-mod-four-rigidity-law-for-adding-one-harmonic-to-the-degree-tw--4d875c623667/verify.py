import math

SQ2 = math.sqrt(2.0)

def Q(t):
    return 1.0 + SQ2*math.cos(t) + 0.5*math.cos(2.0*t)

def T(n,t,eps):
    cn = math.cos(3.0*math.pi*n/4.0)
    if abs(cn) < 1e-12:
        c = 0.0
    else:
        c = 2.0*eps*(1.0 if cn > 0 else -1.0)
    return 1.0 + (SQ2+eps)*math.cos(t) + 0.5*math.cos(2.0*t) + c*math.cos(n*t)

# Exact-pattern checks at the degree-two contact angle.
for n in range(3,65):
    cn = math.cos(3.0*math.pi*n/4.0)
    zero = abs(cn) < 1e-12
    assert zero == (n % 4 == 2), (n, cn)
    if zero:
        t0 = 3.0*math.pi/4.0
        assert abs(math.cos(2.0*t0)) < 1e-12
        assert abs(math.cos(n*t0)) < 1e-11
        assert abs((1.0 + SQ2*math.cos(t0)) - 0.0) < 1e-12
    else:
        p0 = -1.0/SQ2 + 2.0*abs(cn)
        assert p0 > 0.7 - 1e-12

# Numerical stress test of the strict-improvement perturbation.
# This is corroborative only; the proof uses compactness and positivity near the two contacts.
NGRID = 120000
worst = 1.0
cases = 0
for n in range(3,41):
    if n % 4 == 2:
        continue
    eps = min(1e-6, 1e-4/(n*n))
    mn = float('inf')
    for j in range(NGRID):
        t = 2.0*math.pi*j/NGRID
        v = T(n,t,eps)
        if v < mn:
            mn = v
    worst = min(worst,mn)
    assert mn > -2e-10, (n, eps, mn)
    cases += 1

print(f"VERIFY_OK parity_n=3..64 strict_cases={cases} grid={NGRID} worst_sample={worst:.3e}")
