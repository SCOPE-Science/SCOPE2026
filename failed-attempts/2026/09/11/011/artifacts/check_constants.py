"""Rigorous interval check for lane-692 target constant.

Target: log2 S + D/100 >= n/200 for Tseitin on LPS X^{5,q} (6-reg, N=3n vars).
Width lemma: w >= h*n/3, h >= 3-sqrt(5) (Cheeger + Ramanujan black box).
Generic size-width (closed, fixed-t subset argument): S >= exp((w^2-w0^2)/(8N))
  i.e. log2 S >= (w^2-w0^2)/(8 N ln2), N=3n, w0=6.
Optimistic variant (denominator 4N) is NOT closed; shown for comparison only.

Uses only explicit rational upper/lower bounds:
  sqrt(5) < 2.23606797749979  (since 2.23606797749979^2 > 5, verified below)
  ln2 < 0.6931471805599454
All arithmetic rounded conservatively (lower bounds use hi denominators).
"""
import math

sqrt5_hi = 2.23606797749979
assert sqrt5_hi**2 > 5, "sqrt5 upper bound invalid"
ln2_hi = 0.6931471805599454  # standard double upper bound; math.log(2)<this
assert math.log(2) < ln2_hi

h_lo = 3 - sqrt5_hi          # Cheeger lower bound
beta_lo = h_lo / 3.0         # width factor w >= beta*n
w0 = 6
print(f"h_lo={h_lo:.10f} beta_lo={beta_lo:.10f}")

def cert_per_n_closed(n):
    # closed denominator-8N bound, lower bound on (log2 S)/n
    w_lo = beta_lo * n - 0  # w >= beta*n (ignore -w0 in w, handle via w^2-w0^2)
    num = w_lo**2 - w0**2
    if num < 0:
        num = 0.0
    # log2 S >= num/(8*N*ln2), N=3n
    return num / (8 * 3 * n * ln2_hi * n) * n  # per-n: num/(24 n^2 ln2)

print("closed (8N) per-n certifiable vs required 0.005:")
ok_all = True
for q, n in [(13, 1092), (17, 2448), (29, 12180), (101, 515100)]:
    w_lo = beta_lo * n
    lb = (w_lo**2 - w0**2) / (8 * 3 * n * ln2_hi)  # log2 S lower bound
    per = lb / n
    req = 1 / 200
    print(f"  q={q} n={n}: w_lo={w_lo:.2f} log2S>={lb:.3f} per-n={per:.7f} req={req} {'PASS' if per >= req else 'FAIL'}")
    if per >= req:
        ok_all = False  # would-be pass; check
print("closed bound reaches 1/200 for all q:", ok_all)

# required beta for closed bound: beta^2/(24 ln2) >= 1/200
need_beta = math.sqrt(24 * 0.6931471805599453 / 200)
print(f"beta_lo={beta_lo:.6f} need_beta(closed)={need_beta:.6f} shortfall={need_beta-beta_lo:.6f}")

# trivial S>=n check
print("trivial S>=n (log2 S>=log2 n) vs n/200:")
for n in [1092, 2448]:
    print(f"  n={n}: log2n={math.log2(n):.3f} req={n/200:.3f} {'PASS' if math.log2(n)>=n/200 else 'FAIL'}")

# optimistic (UNPROVEN 4N) for comparison only
print("optimistic UNPROVEN (4N) per-n (for comparison, not claimed):")
for n in [1092, 2448]:
    w_lo = beta_lo * n
    lb = (w_lo**2 - w0**2) / (4 * 3 * n * ln2_hi)
    print(f"  n={n}: per-n={lb/n:.7f}")
