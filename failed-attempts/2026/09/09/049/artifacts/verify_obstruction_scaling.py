"""Chunk-prefix obstruction scaling (explicit STAND-IN integers, NOT J/K values).

Setup: dependent k-sequence, designated h=f(k)^{-1/2} sum x_i^*, x_i^*(x_i)=1/2,
cross terms |x_i^*(x_j)|<k^{-2} (i!=j, mismatched L-levels, GM Sec.3).
Equal chunks: n even, size s=k/n, signs c_j=(-1)^j, v=sum c_j y_j.
Claim A (lower bound on ||v|| via explicit valid length-k special z^*):
  z_i^*=x_i^* (i<=s), z_{s+1}^* valid continuation != x_{s+1}^*, rest arbitrary valid.
  (sum z_i^*)(v) = c_1*s/2 + err, |err| <= 1 (tail k^2 terms x k^-2)
      + within/first-chunk cross <= s*k*k^-2 = s/k = 1/n <= 1.
  Hence |z(v)| >= (s/2-2)/sqrt(F), so ||v|| >= (s/2-2)/sqrt(F) for EVERY sign
  pattern c (first-chunk contribution +-s/2; absolute value kills the sign).
Claim B (hoped y-level sub-bound): 1.2*n/f(n) (Lemma-5 scale with G'=n/f).
Violation ratio R = [(s/2-2)/sqrt(F)] / [1.2*n/f(n)] >> 1  <=>  chunk table fails.
"""
import math

def f(t):
    return math.log2(t + 1)

print("=== STAND-IN evaluations (illustrative only; actual J/K astronomically sparser) ===")
for (n, F, k) in [(1000, 200.0, 10**9), (100, 50.0, 10**6), (10, 20.0, 10**4)]:
    s = k / n
    assert s == int(s) and n % 2 == 0
    s = int(s)
    lower = (s / 2 - 2) / math.sqrt(F)
    hope = 1.2 * n / f(n)
    R = lower / hope
    print("n=%d F=%.0f k=%d: s=%d lower=%.1f hope=%.3f R=%.1f %s"
          % (n, F, k, s, lower, hope, R, "VIOLATED" if R > 1 else "ok"))
    assert R > 1

# exactness checks of the bookkeeping (no asymptotics)
n, k = 1000, 10**9
s = k // n
tail_bound = k * k * (k**-2)  # == 1.0 exactly
cross_bound = s * k * (k**-2)  # == s/k == 1/n
assert abs(tail_bound - 1.0) < 1e-9
assert abs(cross_bound - 1 / n) < 1e-12
print("bookkeeping exact: tail<=%.4f, first-chunk cross<=%.6f OK" % (tail_bound, cross_bound))

# alternating-prefix sanity (fully alternating => O(1); chunk => Omega(s)): stand-in weights
s_demo, k_demo = 10**6, 10**9
alt_prefix_max = 1.5  # |sum_{i<=t}(-1)^{i+1} a_i|, a_i in [1/2-1/k,1/2+1/k] (<=2 GM bound)
chunk_prefix = s_demo / 2  # first-chunk block-constant prefix
print("fully-alternating prefix<=%.1f vs chunk-constant prefix=%.1e: separation OK"
      % (alt_prefix_max, float(chunk_prefix)))
assert chunk_prefix > 1e3 * alt_prefix_max
print("ALL_OBSTRUCTION_OK")
