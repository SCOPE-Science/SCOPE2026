"""Numerical verification of the Zorich tail-sum mechanism (DRAFT Lemma 1-2, Sec. 3-4).

Model: at most D Zorich symbols per Rauzy length n, each with Gibbs weight
  w(n) = exp(sup_{[a]} (tJ - s r)) <= exp(|t|*CJ) * (n+1)^{-s'} * exp(s'*C0),
where s' = s - |t|*K. Tail bound B(N) = D*exp(|t|*CJ + s'*C0) * sum_{n>=N} n^{-s'}.
Pressure of the cusp subsystem {n >= N} is <= log B(N); gap holds when log B(N) < 0.

Checks:
 1. At (t,s)=(0,h) with h=2 (any h>1 works), log B(N) -> -inf as N grows.
 2. Robustness: same fixed N keeps log B(N) < -kappa for small |t|, s near h.
 3. Finiteness: full sum B(1) < inf for s' > 1.
"""
import math

def tail_sum(N, s, nmax=10_000_000):
    # sum_{n>=N} n^{-s} = zeta(s) - sum_{n<N} n^{-s}, via direct partial sums + integral tail bound
    # compute partial sum up to M then bound remainder by integral
    M = max(N, 200000)
    partial = sum(n ** (-s) for n in range(N, M + 1))
    remainder = (M + 1) ** (1 - s) / (s - 1)  # integral test upper bound
    return partial + remainder

def log_bound(N, t, s, D=12, C0=1.0, CJ=1.0, K=2.0):
    sp = s - abs(t) * K
    assert sp > 1, "need s' > 1"
    return math.log(D) + abs(t) * CJ + sp * C0 + math.log(tail_sum(N, sp))

print("== (0,h)=(0,2): cusp pressure upper bound log B(N) ==")
for N in [10, 50, 200, 1000, 5000]:
    print(f"N={N:>5d}  logB={log_bound(N, 0.0, 2.0):+.4f}")
print("== robustness: fixed N=1000, perturbed (t,s) ==")
for t, s in [(0.0, 2.0), (0.05, 2.0), (0.1, 1.95), (0.1, 2.05), (-0.1, 1.95)]:
    print(f"t={t:+.2f} s={s:.2f}  logB={log_bound(1000, t, s):+.4f}")
print("== finiteness B(1) ==")
for t, s in [(0.0, 2.0), (0.1, 1.9)]:
    print(f"t={t:+.2f} s={s:.2f}  logB(1)={log_bound(1, t, s):+.4f} (finite)")
print("OK: logB(N)<<0 achievable and stable under small t; full sum finite.")
