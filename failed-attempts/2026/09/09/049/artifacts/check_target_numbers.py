"""Verify numeric thresholds behind the X_GM target claim (stdlib only).

Checks:
 1. Trivial regime: K>=1 always, so K>=(1/4)sqrt(f(n)) is vacuous for small n.
    Find max n with (1/4)*sqrt(log2(n+1)) <= 1.
 2. GM parameter floor: f(j1)>=36 -> j1 >= 2^36-1.
 3. One-level HI ratio: (k/2-1)/sqrt(f(k)) vs 1.2*k/f(k) gives ratio >= (1/3)sqrt(f(k))
    for all k with f(k)>=36 (in fact much smaller suffices); verify symbolically
    over a range of f values and confirm constant 1/4 has slack.
 4. Sparsity illustration: log log log growth forces triple-exponential gaps;
    demonstrate with moderate stand-ins (NOT actual J, which is astronomically sparse).
"""
import math

def f(t):
    return math.log2(t + 1)

# 1. trivial threshold
n_star = 2**16 - 2  # 65534: f = log2(65535) = ~16 - tiny; (1/4)*4 = 1 boundary
print("f(65534) =", f(65534), " (1/4)sqrt =", 0.25 * math.sqrt(f(65534)))
print("f(65535) =", f(65535), " (1/4)sqrt =", 0.25 * math.sqrt(f(65535)))
assert 0.25 * math.sqrt(f(65534)) <= 1.0
assert 0.25 * math.sqrt(f(65535)) >= 1.0 - 1e-9  # boundary ~1
print("TRIVIAL_THRESHOLD_OK: n<=65534 vacuous (any normalized block works)")

# 2. j1 floor
j1min = 2**36 - 1
print("j1min =", j1min, " f(j1min) =", f(j1min))
assert f(j1min) >= 36 - 1e-9
print("J1_FLOOR_OK")

# 3. ratio constant: lower L(k)=(k/2-1)/sqrt(F), upper U(k)=1.2*k/F, ratio R=L/U
# R = F*(k/2-1)/(1.2*k*sqrt(F)) = sqrt(F)*(k-2)/(2.4*k) = sqrt(F)*(1/2.4)*(1-2/k)
# Claim R >= (1/3)*sqrt(F) iff (1-2/k)/2.4 >= 1/3 iff 1-2/k >= 0.8 iff k>=10.
for k in [10, 100, 1000, 10**6, j1min]:
    F = f(k)
    L = (k / 2 - 1) / math.sqrt(F)
    U = 1.2 * k / F
    R = L / U
    assert R >= (1 / 3) * math.sqrt(F) - 1e-9, (k, R)
print("RATIO_CONSTANT_OK: k>=10 gives >=(1/3)sqrt(f(k)), hence >=(1/4)sqrt(f(k))")

# 4. sparsity stand-in: if logloglog(n) >= 2m with m=5, then (natural logs)
# loglog(n) >= e^10, log(n) >= e^{e^10}, n >= e^{e^{e^10}} (triple exp, far
# beyond float range). Report the tower height in log10-scale instead.
import decimal
L2 = math.exp(10)  # log log n >= this
log10_L1 = L2 / math.log(10)  # log10(log n) >= this
print("stand-in: m=5 forces loglog(n) >= e^10 = %.3f," % L2)
print("  i.e. log10(log(n)) >= %.3f, i.e. n >= 10^(10^%.3f)" % (log10_L1, math.log10(log10_L1)))
print("  (tower of height 3; actual J gaps use m>=j1>=6.9e10, vastly taller)")
print("ALL_VERIFY_OK")
