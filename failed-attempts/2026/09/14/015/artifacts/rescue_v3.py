"""Lane-1844 recovery test (v3): second-order rescue attempt for the k=10 joint survivor.

Question: can h = 1 + e cos(10t) + e^2 (a cos(20t) + b cos(30t) + c cos(40t))
kill the q=4 residual to O(e^2) and the q=6 residual to O(e^2)?
First-order resonances: q=4 killed by modes divisible by 4 (20, 40);
q=6 killed by modes divisible by 6 (30). Because 20,40 do not touch q=6 at
first order and 30 does not touch q=4 at first order, the two corrections
decouple: fit (a,c) against the q=4 second-order profile and b against q=6.
Grid-searches the (a,c) and b coefficients by minimizing the frozen-range
residual; reports best residual and scaling. Success = residual pushed to
O(e^3) for q=4 and O(e^3) for q=6 simultaneously (would give a 2nd-order
joint flattener, blocking any low-order rigidity proof and keeping a formal
power-series counterexample route alive).
"""
import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_v3.json")

def mk(e, a=0.0, b=0.0, c=0.0):
    h = lambda th: (1.0 + e * np.cos(10 * th) + e**2 * (
        a * np.cos(20 * th) + b * np.cos(30 * th) + c * np.cos(40 * th)))
    hp = lambda th: (-10 * e * np.sin(10 * th) + e**2 * (
        -20 * a * np.sin(20 * th) - 30 * b * np.sin(30 * th)
        - 40 * c * np.sin(40 * th)))
    return h, hp

def frozen_profile(h, hp, q, M=256):
    s = np.linspace(0, 2 * np.pi, M, endpoint=False)
    th = s[:, None] + 2 * np.pi * np.arange(q)[None, :] / q
    n = np.stack([np.cos(th), np.sin(th)], axis=-1)
    t = np.stack([-np.sin(th), np.cos(th)], axis=-1)
    X = h(th)[..., None] * n + hp(th)[..., None] * t
    d = np.roll(X, -1, axis=-2) - X
    P = np.sqrt((d ** 2).sum(axis=-1)).sum(axis=-1)
    return s, P - P.mean(), float(P.max() - P.min())

def fit_slope(eps, R):
    x = np.log(np.asarray(eps)); y = np.log(np.asarray(R))
    A = np.vstack([x, np.ones_like(x)]).T
    m, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(m)

e = 0.002
# --- q=4 correction scan over (a,c); b=0 fixed (b invisible to q=4) ---
best4 = None
for a in np.linspace(-3, 3, 25):
    for c in np.linspace(-3, 3, 25):
        R = frozen_profile(*mk(e, a=a, c=c), 4)[2]
        if best4 is None or R < best4[0]:
            best4 = (R, float(a), float(c))
R4, a4, c4 = best4
# --- q=6 correction scan over b; (a,c) fixed at q=4-optimal values ---
# NOTE: a,c invisible to q=6 at first order, so the q=4-optimal pair is safe.
best6 = None
for b in np.linspace(-4, 4, 33):
    R = frozen_profile(*mk(e, a=a4, b=b, c=c4), 6)[2]
    if best6 is None or R < best6[0]:
        best6 = (R, float(b))
R6, b6 = best6
abase = frozen_profile(*mk(e), 4)[2]
bbase = frozen_profile(*mk(e), 6)[2]

# --- scaling of the jointly corrected shape ---
EPS = [0.0005, 0.001, 0.002, 0.004]
R4s = [frozen_profile(*mk(x, a=a4, b=b6, c=c4), 4)[2] for x in EPS]
R6s = [frozen_profile(*mk(x, a=a4, b=b6, c=c4), 6)[2] for x in EPS]
out = {
    "e": e, "a_q4": a4, "c_q4": c4, "b_q6": b6,
    "q4_base": abase, "q4_corrected": R4,
    "q6_base": bbase, "q6_corrected": R6,
    "EPS": EPS, "R4s": R4s, "R6s": R6s,
    "slope4": fit_slope(EPS, R4s), "slope6": fit_slope(EPS, R6s),
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
