#!/usr/bin/env python3
"""Lane-1354 recovery test (overflow-free, exponent-space).

Part A: factorial-block address combinatorics (bounded, aperiodic, not preperiodic).
Part B: uniform fixed-potential pullback bound along 0-blocks:
  for s = 0^M u (u over {0,1}), g_s(T) = L_0^M(g_u(F^M(T))),
  with F(t)=e^t-1, L_0(w)=1+Log(w). Assuming the cited uniform tail
  estimate |g_u(F^M(T)) - F^M(T)| <= C0, this shows |g_s(T)| is bounded
  independently of M. Computed entirely in exponent space so no
  M-fold exponential is ever formed (large levels contribute error 0).
  This SUPPORTS but does not complete the transfer lemma (boundedness of
  the landing points w themselves), which is the documented blockage.
"""
import math
import cmath

# ---- Part A: combinatorics of b = concat_{k>=1} 0^{k!} 1^{k!} ----
def build(K):
    b = []
    for k in range(1, K + 1):
        f = math.factorial(k)
        b += [0] * f + [1] * f
    return b

b = build(6)
runs = []
cur, n = b[0], 1
for x in b[1:]:
    if x == cur:
        n += 1
    else:
        runs.append((cur, n))
        cur, n = x, 1
runs.append((cur, n))
assert all(s in (0, 1) for s, _ in runs), "alphabet must be {0,1}"
assert runs[:10] == [(0, 1), (1, 1), (0, 2), (1, 2), (0, 6), (1, 6),
                     (0, 24), (1, 24), (0, 120), (1, 120)]
# Analytic fact checked here on the prefix: runs of BOTH symbols exceed any
# fixed q arbitrarily far out, so no eventual period q is possible
# (a period-q tail has runs <= q unless constant; both symbols recur).
for q in range(1, 11):
    assert sum(1 for s, r in runs if s == 0 and r > q) >= 3
    assert sum(1 for s, r in runs if s == 1 and r > q) >= 3
print("Part A OK: alphabet {0,1}; block runs = k! alternating; "
      "max run in prefix =", max(r for _, r in runs))

# ---- Part B: uniform fixed-potential bound, exponent-space recursion ----
def residual_bound(T, C0, M):
    """Bound |c_0| where L_0^M(F^M(T)+c) = T + c_0, |c| <= C0.

    Write w_j = F^j(T) + c_j. Then
      c_{j-1} = 1 + Log(F^j(T)+c_j) - F^{j-1}(T)
              = 1 + log1p((c_j-1) * exp(-F^{j-1}(T))),
    needing only exp(-x) (underflows to 0, never overflows).
    """
    xs = [float(T)]
    for _ in range(M):
        try:
            xs.append(math.exp(xs[-1]) - 1.0)
        except OverflowError:
            xs.append(float("inf"))
    cb = float(C0)
    for j in range(M, 0, -1):
        x = xs[j - 1]
        assert xs[j] - cb > 0.0, (j, xs[j], cb)  # Log domain: Re > 0
        einv = 0.0 if x == float("inf") else math.exp(-x)
        y = (cb + 1.0) * einv  # |arg| of log1p
        assert y < 0.5, (j, x, y)
        cb = 1.0 + y / (1.0 - y)  # |Log(1+y)| <= |y|/(1-|y|)
        assert cb < 3.0
    return cb

for M in [3, 10, 50, 200]:
    cb = residual_bound(2.0, 10.0, M)
    print(f"Part B: M={M:3d} -> |g_s(2)| <= 2 + {cb:.4f} = {2.0 + cb:.4f} "
          f"(M-independent)")
print("RECOVERY TEST PASSED: fixed-potential bound is uniform in block length.")
print("NOTE: transfer to landing-point boundedness (the blocked step) is NOT "
      "established by this test.")
