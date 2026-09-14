"""Route A/B/C computations for lane-1844.

Supports h(theta) geometries (central symmetry <=> pi-periodic h):
 - frozen equal-spaced q-gon perimeter range R_q(eps) and log-log slope
   (slope 1 = first-order breaking; slope 2 = preserved to first order)
 - pinned minimal q-gon criterion m_q(s) = min perimeter over q-gons pinned
   at x(s); exact rational caustic of rotation 1/q requires m_q = const.
   Validated: circle/ellipse -> ~0; perturbed shapes -> >0.
 - second-order flattener attempt for k=10 mode.

No scipy dependency; numpy only.
"""
import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")

def boundary(h, hp, th):
    n = np.stack([np.cos(th), np.sin(th)], axis=-1)
    t = np.stack([-np.sin(th), np.cos(th)], axis=-1)
    return h(th)[..., None] * n + hp(th)[..., None] * t

def peri(pts):
    d = np.roll(pts, -1, axis=-2) - pts
    return np.sqrt((d ** 2).sum(axis=-1)).sum(axis=-1)

def frozen_range(h, hp, q, M=256):
    s = np.linspace(0, 2 * np.pi, M, endpoint=False)
    th = s[:, None] + 2 * np.pi * np.arange(q)[None, :] / q
    X = boundary(h, hp, th)
    P = peri(X)
    return float(P.max() - P.min()), float(P.mean())

def fit_slope(eps, R):
    x = np.log(np.asarray(eps)); y = np.log(np.asarray(R))
    A = np.vstack([x, np.ones_like(x)]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(m), float(c)

def cos_mode(k):
    return (lambda th, k=k: 1.0 + 0.0 * th,
            lambda th, k=k: 0.0 * th)

def pert_mode(k, eps):
    return (lambda th, k=k, eps=eps: 1.0 + eps * np.cos(k * th),
            lambda th, k=k, eps=eps: -eps * k * np.sin(k * th))

def ellipse(a, b):
    h = lambda th: np.sqrt((a * np.cos(th)) ** 2 + (b * np.sin(th)) ** 2)
    hp = lambda th: (b ** 2 - a ** 2) * np.sin(th) * np.cos(th) / h(th)
    return h, hp

# ---------- Route A: first-order slopes ----------
res = {"routeA_slopes": {}, "routeB": {}, "routeC": {}}
EPS_BASE = [0.002, 0.005, 0.01, 0.02, 0.04]
for k in [2, 4, 6, 8, 10, 12, 14]:
    cap = 0.3 / max(1, k * k - 1)  # convexity: e*(k^2-1) < 0.3
    EPS = [e for e in EPS_BASE if e < cap] or [cap / 2]
    for q in [4, 6]:
        Rs = []
        for e in EPS:
            h, hp = pert_mode(k, e)
            R, _ = frozen_range(h, hp, q)
            Rs.append(R)
        m, c = fit_slope(EPS, Rs)
        res["routeA_slopes"][f"k{k}_q{q}"] = {"slope": m, "Rs": Rs}

# ---------- Route C: pinned-min criterion ----------
def pinned_min_range(h, hp, q, M=16, sweeps=12):
    s = np.linspace(0, 2 * np.pi, M, endpoint=False)
    base = 2 * np.pi * np.arange(1, q)[None, :] / q  # (1,q-1)
    phi = np.zeros((M, q - 1))
    def obj(phi):
        th = s[:, None] + np.concatenate([np.zeros((M, 1)), base + phi], axis=1)
        X = boundary(h, hp, th)
        return peri(X)  # (M,)
    cur = obj(phi)
    for _ in range(sweeps):
        for j in range(q - 1):
            lo = phi[:, j] - 0.35; hi = phi[:, j] + 0.35
            # golden-section search, vectorized over M
            gr = (np.sqrt(5) - 1) / 2
            a = lo.copy(); b = hi.copy()
            c = b - gr * (b - a); d = a + gr * (b - a)
            for _ in range(40):
                pc = phi.copy(); pc[:, j] = c
                pd = phi.copy(); pd[:, j] = d
                fc = obj(pc); fd = obj(pd)
                msk = fc < fd
                b = np.where(msk, d, b); d = np.where(msk, c, d)
                c = np.where(msk, b - gr * (b - a), c)
                a = np.where(~msk, c, a); c = np.where(~msk, b - gr * (b - a), c)
                d = np.where(~msk, d, a + gr * (b - a))
            phi[:, j] = 0.5 * (a + b)
            cur = obj(phi)
    return float(cur.max() - cur.min()), float(cur.mean())

h0, hp0 = cos_mode(0)
for name, (h, hp) in {
    "circle": (h0, hp0),
    "ellipse_a1.2_b1.0": ellipse(1.2, 1.0),
    "k10_eps0.03": pert_mode(10, 0.03),
    "k14_eps0.03": pert_mode(14, 0.03),
}.items():
    for q in [4, 6]:
        R, mean = pinned_min_range(h, hp, q)
        res["routeC"][f"{name}_q{q}"] = {"range": R, "mean": mean}

# ---------- Route B: breaking-order check ----------
# pure mode k: frozen-range slope should be 1 iff q|k else 2 (first order),
# and second-order residual harmonic analysis predicts breaking at order
# m = q/gcd(k,q). Numerically confirm k=10,q=4 breaks at O(eps^2) while
# k=10,q=6 residual scales as O(eps^3) (slope 3 in range).
EPS2_BASE = [0.005, 0.01, 0.02, 0.04, 0.08]
for k, q in [(10, 4), (10, 6), (14, 4), (14, 6), (2, 4), (2, 6)]:
    cap = 0.3 / max(1, k * k - 1)
    EPS2 = [e for e in EPS2_BASE if e < cap] or [cap / 2]
    Rs = []
    for e in EPS2:
        h, hp = pert_mode(k, e)
        R, _ = frozen_range(h, hp, q, M=512)
        Rs.append(R)
    m, c = fit_slope(EPS2, Rs)
    import math
    pred = q // math.gcd(k, q)
    res["routeB"][f"k{k}_q{q}"] = {"slope": m, "predicted_break_order": pred,
                                   "Rs": Rs}

with open(OUT, "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
