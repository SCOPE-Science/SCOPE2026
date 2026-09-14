"""Lane-1844 recovery test (v2): first-order joint-survival classification + orders.

Theory (linearization of q-gon length functional around circle):
  d/ds L_q(s) at first order in deformation mu(th)=sum c_k e^{ik th} is
  proportional to sum_j mu(s+2pi j/q). Mode k contributes q*c_k*e^{iks}
  if q|k, else 0. Hence mode k breaks rotation-1/q caustic at FIRST order
  iff q divides k; otherwise it survives to first order (slope>=2 in the
  frozen equal-spaced perimeter range R_q(eps)).
  Joint 1/4+1/6 first-order survivors (central symmetry => k even):
  k even with 4-/->k and 6-/->k, i.e. k in {2,10,14,22,26,...}.
  k=2 is the ellipse (integrable) direction; k=10,14,... are non-elliptic
  joint survivors => linear theory alone cannot prove rigidity.

This script verifies the divisibility rule numerically (slope 1 iff q|k)
and measures the second-order residual of the lowest non-elliptic joint
survivor k=10 (expected slope ~2 = breaks at second order, but rescuable
in principle by order-eps^2 higher-mode corrections => formal problem open).
"""
import numpy as np
import json, os, math

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_v2.json")

def boundary(h, hp, th):
    n = np.stack([np.cos(th), np.sin(th)], axis=-1)
    t = np.stack([-np.sin(th), np.cos(th)], axis=-1)
    return h(th)[..., None] * n + hp(th)[..., None] * t

def peri(pts):
    d = np.roll(pts, -1, axis=-2) - pts
    return np.sqrt((d ** 2).sum(axis=-1)).sum(axis=-1)

def frozen_range(h, hp, q, M=512):
    s = np.linspace(0, 2 * np.pi, M, endpoint=False)
    th = s[:, None] + 2 * np.pi * np.arange(q)[None, :] / q
    P = peri(boundary(h, hp, th))
    return float(P.max() - P.min())

def fit_slope(eps, R):
    x = np.log(np.asarray(eps)); y = np.log(np.asarray(R))
    A = np.vstack([x, np.ones_like(x)]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(m)

def pert(k, e):
    return (lambda th: 1.0 + e * np.cos(k * th),
            lambda th: -e * k * np.sin(k * th))

rows = []
for k in [2, 4, 6, 8, 10, 12, 14]:
    cap = 0.25 / (k * k)           # keep h+h''>0 and eps*k small
    EPS = [cap * f for f in (0.05, 0.1, 0.2, 0.4, 0.8)]
    for q in [4, 6]:
        Rs = [frozen_range(*pert(k, e), q) for e in EPS]
        m = fit_slope(EPS, Rs)
        rows.append({"k": k, "q": q, "eps": EPS, "Rs": Rs, "slope": m,
                     "q_divides_k": (k % q == 0),
                     "verdict": ("BREAKS-1st" if (k % q == 0) else "SURVIVES-1st")})

# second-order residual size for k=10 joint survivor (coefficient of eps^2)
k = 10
cap = 0.25 / (k * k)
detail = {}
for q in [4, 6]:
    es = [cap * f for f in (0.1, 0.2, 0.4, 0.8)]
    Rs = [frozen_range(*pert(k, e), q) for e in es]
    coef2 = [r / e ** 2 for r, e in zip(Rs, es)]
    detail[f"q{q}"] = {"eps": es, "Rs": Rs, "R_over_eps2": coef2,
                       "slope": fit_slope(es, Rs)}

out = {"rows": rows, "k10_second_order": detail,
       "joint_survivors_even_le16": [kk for kk in range(2, 17, 2)
                                     if kk % 4 != 0 and kk % 6 != 0]}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
for r in rows:
    print(f"k={r['k']:3d} q={r['q']} q|k={int(r['q_divides_k'])} "
          f"slope={r['slope']:+.3f} {r['verdict']} Rs={['%.2e' % v for v in r['Rs']]}")
print("joint survivors (even,<=16):", out["joint_survivors_even_le16"])
print("k=10 2nd-order:", json.dumps(detail))
