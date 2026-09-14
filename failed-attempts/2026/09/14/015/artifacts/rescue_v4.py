"""Lane-1844 recovery test (v4): joint second-order correction re-examined.

v3 anomaly: fixing (a,c) at the q=4 optimum, then scanning b, left q=6 slope ~1.3
suggesting a possible q=4/q=6 conflict. But theory says the q=6 residual at
O(e^2) comes only from pair products with (k1+k2) or (k1-k2) divisible by 6.
Contributors at order e^2: (10,10) only (sum 20, diff 0 — neither divisible
by 6 => q=6 residual should be O(e^3) already WITHOUT correction). The v3 q=6
"base" R~7.9e-6 at e=2e-3 with slope 3 confirms exactly that. So scanning b
for a first-order q=6 resonance injects an O(e^2*b) term that can only worsen
q=6 — the correct joint correction is (a,c) for q=4 and b=0 for q=6.

This script: (1) confirms q=6 needs no correction (slope 3 at b=0);
(2) confirms (a,c)=(-0.25,0) pushes q=4 from slope 2 to slope 3 with b=0;
(3) checks the residual profiles are the predicted harmonics;
(4) attempts the NEXT order: with q=4 at O(e^3) and q=6 at O(e^3), fit
third-order corrections and see whether a joint O(e^3)->O(e^4) rescue exists.
"""
import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_v4.json")

def mk2(e, a=0.0, c=0.0):
    h = lambda th: 1.0 + e * np.cos(10 * th) + e**2 * (
        a * np.cos(20 * th) + c * np.cos(40 * th))
    hp = lambda th: (-10 * e * np.sin(10 * th) + e**2 * (
        -20 * a * np.sin(20 * th) - 40 * c * np.sin(40 * th)))
    return h, hp

def frozen(h, hp, q, M=512):
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

EPS = [0.0005, 0.001, 0.002, 0.004]
# (1) q=6 uncorrected scaling (b=0)
R6u = [frozen(*mk2(x), 6)[2] for x in EPS]
# (2) q=4 corrected scaling with (a,c)=(-0.25,0), b=0; and q=6 with same shape
R4c = [frozen(*mk2(x, a=-0.25), 4)[2] for x in EPS]
R6c = [frozen(*mk2(x, a=-0.25), 6)[2] for x in EPS]
# (3) harmonic content of corrected q=4 residual at e=0.004
s, prof, _ = frozen(*mk2(0.004, a=-0.25), 4)
F = np.fft.rfft(prof)
amps = {int(k): float(abs(F[k]) / len(s)) for k in range(0, 24)}
# (4) third-order attempt: add e^3*(p cos20 + r cos40) [q=4 killers]
#     + e^3*(w cos30 + v cos60) [q=6 killers]; cross-invisibility holds
#     (20,40 vs 30,60 disjoint divisor classes), so fit separately.
def mk3(e, p=0.0, r=0.0, w=0.0, v=0.0):
    h = lambda th: (1.0 + e * np.cos(10 * th)
                    - 0.25 * e**2 * np.cos(20 * th)
                    + e**3 * (p * np.cos(20 * th) + r * np.cos(40 * th)
                              + w * np.cos(30 * th) + v * np.cos(60 * th)))
    hp = lambda th: (-10 * e * np.sin(10 * th)
                     + 5.0 * e**2 * np.sin(20 * th)
                     + e**3 * (-20 * p * np.sin(20 * th)
                               - 40 * r * np.sin(40 * th)
                               - 30 * w * np.sin(30 * th)
                               - 60 * v * np.sin(60 * th)))
    return h, hp

e = 0.002
best4 = None
for p in np.linspace(-2, 2, 17):
    for r in np.linspace(-2, 2, 17):
        R = frozen(*mk3(e, p=p, r=r), 4)[2]
        if best4 is None or R < best4[0]:
            best4 = (R, float(p), float(r))
best6 = None
for w in np.linspace(-2, 2, 17):
    for v in np.linspace(-2, 2, 17):
        R = frozen(*mk3(e, p=best4[1], r=best4[2], w=w, v=v), 6)[2]
        if best6 is None or R < best6[0]:
            best6 = (R, float(w), float(v))
R43 = [frozen(*mk3(x, p=best4[1], r=best4[2], w=best6[1], v=best6[2]), 4)[2]
       for x in EPS]
R63 = [frozen(*mk3(x, p=best4[1], r=best4[2], w=best6[1], v=best6[2]), 6)[2]
       for x in EPS]
out = {
    "q6_uncorrected": {"Rs": R6u, "slope": fit_slope(EPS, R6u)},
    "q4_corrected_a_-0.25": {"Rs": R4c, "slope": fit_slope(EPS, R4c)},
    "q6_with_a_-0.25": {"Rs": R6c, "slope": fit_slope(EPS, R6c)},
    "q4_residual_harmonics_e0.004": amps,
    "third_order": {"p": best4[1], "r": best4[2], "w": best6[1],
                    "v": best6[2],
                    "q4_R_at_e": best4[0], "q6_R_at_e": best6[0],
                    "R4s": R43, "R6s": R63,
                    "slope4": fit_slope(EPS, R43),
                    "slope6": fit_slope(EPS, R63)},
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
