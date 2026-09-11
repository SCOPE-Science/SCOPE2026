"""FALLBACK bounded attempts F2+F2b (numpy):
 F2:  sup-ratio scan R(t) = t^{0.9} sigma(t) over resolved grid in [1,8000]
       -> tests truth (bounded ratios suggest TRUE-but-unprovable) and shows a
       finite audit can never close sup over the infinite tail.
 F2b: rigorous axial lower envelope sigma(20^m) >= c/20^m with explicit c,
       from Knapp caps + certified |c0|>=0.206 (Route A) + Lipschitz data:
         L = 5*pi/19 (d mu1hat/d xi), slow(u) = 1-5*pi*|u|/19,
         cap |th| <= 1/(20 t) around 4 axial points, fraction 1/(5 pi t).
"""
import cmath
import math

import numpy as np

PI = math.pi
LIP = 5 * PI / 19.0          # |d mu1hat/d xi| <= sum_k 5pi/20^k
C0 = 0.205748                # certified |c0| lower bound (Route A replay value)
SLOW20 = 1 - 5 * PI / (20 * 19.0)  # <= |mu1hat(u)| for |u| <= 1/20


def mu1hat_vec(x, K=8):
    x = np.asarray(x, dtype=float)
    out = np.ones(x.shape, dtype=complex)
    for k in range(1, K + 1):
        y = x / (20.0 ** k)
        jj = np.arange(6)[None, :]
        out = out * (np.exp(-2j * math.pi * jj * y[:, None]).sum(axis=1) / 6.0)
    return out


def sigma(t, n, K=8):
    TH = np.linspace(0, 2 * PI, n + 1)[:-1]
    v = np.abs(mu1hat_vec(t * np.cos(TH), K=K) * mu1hat_vec(t * np.sin(TH), K=K)) ** 2
    return float(v.mean())


print("=== F2: sup-ratio scan R(t)=t^0.9 sigma(t) (resolved quadrature) ===")
rs = []
ts = list(np.exp(np.linspace(0, math.log(8000), 100))) + [20.0, 400.0, 8000.0]
for t in sorted(ts):
    n = 20001 if t <= 2000 else 80001
    s = sigma(t, n)
    r = (t ** 0.9) * s
    rs.append(r)
print(f"scanned {len(ts)} t-values in [1,8000]; max R(t) = {max(rs):.3f}")
print(f"R(20)={(20**0.9)*sigma(20.0,20001):.3f} R(400)={(400**0.9)*sigma(400.0,20001):.3f} "
      f"R(8000)={(8000**0.9)*sigma(8000.0,80001):.3f}")
print("READING: ratios bounded (~2-3) on tested range -> fallback plausibly TRUE,")
print("but a finite grid cannot certify sup over [1,oo); resonances 20^m, m>=4,")
print("and near-resonant t are outside every finite audit. Truth != provability.")

print()
print("=== F2b: certified axial lower envelope ===")
delta_cap = 1 / 16000.0      # |t cos th - 20^m| <= 1/(800 t) <= 1/16000 on cap
first = C0 - LIP * delta_cap
assert first > 0
h = (first * SLOW20) ** 2     # min |muhat|^2 on each cap
c_env = h / (5 * PI)          # sigma(20^m) >= c_env / 20^m
print(f"L={LIP:.6f} SLOW20={SLOW20:.6f} first-coord min={first:.6f}")
print(f"cap height h={h:.6f}  envelope c={c_env:.6f}")
print(f"CERTIFIED: sigma(20^m) >= {c_env:.4f} * 20^(-m) for all m >= 1.")
for m in (1, 2, 3):
    t = 20.0 ** m
    print(f"  m={m}: bound {c_env/t:.3e} vs computed sigma {sigma(t, 80001):.3e}  "
          f"{'OK' if sigma(t, 80001) >= c_env/t else 'VIOLATION'}")
print("VALUE: decay exponent can never exceed 1.0 for this measure (t^-1 floor);")
print("compatible with both target and fallback -- a routine Knapp-cap lemma,")
print("not an independently valuable result (kept as attempt evidence).")
