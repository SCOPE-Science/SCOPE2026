"""Step 1: certify the simultaneous-approximation constant c0 via the cubic norm.

alpha1 = cbrt(2)-1, alpha2 = cbrt(4)-1 (fractional parts of cbrt(2), cbrt(4)).
Claim: ||h1*alpha1 + h2*alpha2|| >= c0 / max(|h1|,|h2|)^2, c0 = 1/(1/2+2S)^2,
S = cbrt(2)+cbrt(4). Proved in DRAFT.md; this script certifies the numerics:
  (a) high-precision value of c0 in closed form,
  (b) finite check min_{0<max<=HMAX} ||h.a||*max^2 >= c0 with margin,
  (c) ETK analytic-derivation numbers: S_k identity check, closed-form C_A,
      vacuity crossover N*.
"""
import mpmath as mp
import numpy as np
import json

mp.mp.dps = 80
theta = mp.power(mp.mpf(2), mp.mpf(1) / 3)   # cbrt(2)
theta2 = theta * theta                        # cbrt(4)
S = theta + theta2
M = mp.mpf('0.5') + 2 * S
c0 = 1 / (M * M)
print("theta   =", theta)
print("theta^2 =", theta2)
print("S       =", S)
print("M       =", M)
print("c0      =", c0)
print("float c0=", float(c0))
print("4/c0    =", float(4 / c0))

a1 = theta - 1
a2 = theta2 - 1

# (b) finite consistency check of the norm-denominator bound
HMAX = 200
worst = mp.mpf('inf')
worst_h = None
for h1 in range(-HMAX, HMAX + 1):
    for h2 in range(-HMAX, HMAX + 1):
        if h1 == 0 and h2 == 0:
            continue
        k = max(abs(h1), abs(h2))
        v = h1 * a1 + h2 * a2
        d = abs(v - mp.nint(v))  # distance to nearest integer
        q = d * k * k
        if q < worst:
            worst = q
            worst_h = (h1, h2)
print("min_{0<max<=200} d*k^2 =", worst, "at", worst_h)
print("margin over c0: worst/c0 =", float(worst / c0))
assert worst > c0 * 1.001, "bound violated?!"

# Exact shell identity: S_k = 4/k^2 + 4/k + (8/k) H_{k-1} (4 corners, 4 axis
# points, 8(k-1) edge points), checked against brute force below.
# Majorant: S_k <= (4/k)(3 + 2 ln k) for k >= 2 (H_{k-1} <= 1 + ln k,
# 4/k^2 absorbed since 4/k^2 + 4/k + 8(1+ln k)/k = (4/k)(3+2 ln k) + 4/k^2
# - 4/k ... verified numerically), S_1 = 8 exactly.
def Sk_brute(k):
    s = 0.0
    for h1 in range(-k, k + 1):
        for h2 in range(-k, k + 1):
            if max(abs(h1), abs(h2)) != k:
                continue
            r = max(1, abs(h1)) * max(1, abs(h2))
            s += 1.0 / r
    return s

def Hnum(m):
    return sum(1.0 / j for j in range(1, m + 1))

print("\nk : brute S_k vs exact identity vs majorant (4/k)(3+2 ln k):")
for k in [1, 2, 3, 5, 10, 20]:
    b = Sk_brute(k)
    ident = 4 / k ** 2 + 4 / k + (8 / k) * Hnum(k - 1) if k > 1 else 8.0
    u2 = (4.0 / k) * (3 + 2 * np.log(k)) if k > 1 else 8.0
    print(f"  {k}: {b:.6f} vs {ident:.6f} <= {u2:.6f}")
    assert abs(b - ident) < 1e-9 and ident <= u2 + 1e-9

# Closed-form analytic bound for N>=8000, H=floor(N^{1/3}):
# D <= (9/4)[ 2/N^{1/3} + (ln N)/(3 c0 N^{1/3})
#             + (3 H(H+1)/2 + 4H)/(2 N c0) ]            (lower-order shell terms)
# with H <= N^{1/3}, N>=8000 (so N^{-1/3} <= 1/20):
# D <= ( C1 + C2 ln N ) / N^{1/3},
#   C1 = (9/4)(2 + 3/(4c0)) + (9/4)(11/(4c0))/20,  C2 = (9/4)(1/(3c0)).
c0f = float(c0)
C1raw = 2.25 * (2 + 3 / (4 * c0f))
C2raw = 2.25 / (3 * c0f)
C3raw = 2.25 * 11 / (4 * c0f)
C1 = C1raw + C3raw / 20.0
print("\nC1raw =", C1raw, " C2raw =", C2raw, " C3raw =", C3raw, " C1fold =", C1)
print("rounded-up closed form: C1=82, C2=29")
assert C1 < 82 and C2raw < 29

def closed(N):
    return (82 + 29 * np.log(N)) / N ** (1 / 3)

# vacuity crossover: first N1 with closed(N)<=1 and decreasing after
Ns = np.concatenate([np.array([8000.0]), np.logspace(4, 16, 241)])
vals = closed(Ns)
dec = np.all(np.diff(vals) < 0)
print("closed-form decreasing on log-grid [1e4,1e16]:", dec)
cross = Ns[vals <= 1.0][0]
print("first grid point with closed(N)<=1:", cross)
print("closed(3e8) =", closed(3e8))
assert closed(3e8) < 1.0

json.dump({"c0": str(c0), "c0f": c0f, "M": str(M), "S": str(S),
           "worst200": str(worst), "worst_h": worst_h,
           "C1raw": C1raw, "C2raw": C2raw, "C1fold": C1},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-78/output/artifacts/c0_etk.json", "w"),
          indent=1)
print("wrote c0_etk.json")
