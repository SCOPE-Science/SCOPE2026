"""Bounded recovery test: toy transfer-operator analogue of funnel-to-cusp degeneration.

Model: full-branch piecewise-linear expanding maps T_a : [0,1] -> [0,1] with two
linear branches. Breakpoint p(a) = 1/(1+a), slopes s1 = 1+a (nearly neutral as
a -> 0) and s2 = (1+a)/a (very expanding). This mimics the geometric degeneration:
one family of orbits loses hyperbolicity (Lyapunov exponent log(1+a) -> 0,
return time -> infinity) while distortion blows up -- the analytic reason no
uniform escape function / uniform FUP constant can persist down to a = 0.

We discretize the Perron-Frobenius operator L_a via Ulam's method on n equal
bins and track (i) the spectral gap gamma(a) = 1 - |lambda_2(a)| and
(ii) the analogue of the strip resonance count #{|lambda| > 1 - beta0}.
A genuine uniform gap would keep gamma(a) bounded away from 0 and the count
bounded as a -> 0. We observe the opposite: collapse.

Also records the collar-lemma width w(l1) = 2*arsinh(1/sinh(l1/2)) -> infinity
as l1 -> 0, documenting the geometric degeneration (injectivity radius -> 0).
"""
import json
import numpy as np

def ulam_matrix(a, n):
    p = 1.0 / (1.0 + a)
    s1 = 1.0 / p          # = 1 + a
    s2 = 1.0 / (1.0 - p)  # = (1+a)/a
    edges = np.linspace(0.0, 1.0, n + 1)
    P = np.zeros((n, n))
    for j in range(n):
        lo, hi = edges[j], edges[j + 1]
        hb = (hi - lo)
        if hi <= p:
            # bin fully in branch 1: image [s1*lo, s1*hi]
            y0, y1 = s1 * lo, s1 * hi
            for i in range(n):
                ov = max(0.0, min(y1, edges[i + 1]) - max(y0, edges[i]))
                P[i, j] = ov / (s1 * hb)
        elif lo >= p:
            # bin fully in branch 2: image [s2*(x-p)]
            y0, y1 = s2 * (lo - p), s2 * (hi - p)
            for i in range(n):
                ov = max(0.0, min(y1, edges[i + 1]) - max(y0, edges[i]))
                P[i, j] = ov / (s2 * hb)
        else:
            # straddling bin: split mass proportionally
            f1 = (p - lo) / hb
            y0, y1 = s1 * lo, s1 * p  # = [s1*lo, 1]
            row1 = np.zeros(n)
            for i in range(n):
                ov = max(0.0, min(y1, edges[i + 1]) - max(y0, edges[i]))
                row1[i] = ov / (s1 * hb)
            y0b, y1b = 0.0, s2 * (hi - p)
            row2 = np.zeros(n)
            for i in range(n):
                ov = max(0.0, min(y1b, edges[i + 1]) - max(y0b, edges[i]))
                row2[i] = ov / (s2 * hb)
            P[:, j] = row1 + row2
    return P, s1, s2

def gap_and_count(a, n=200, beta0=0.10):
    P, s1, s2 = ulam_matrix(a, n)
    ev = np.linalg.eigvals(P)
    mods = np.sort(np.abs(ev))[::-1]
    lam2 = mods[1]
    gap = 1.0 - lam2
    count = int(np.sum(np.abs(ev) > 1.0 - beta0))
    return gap, count, lam2, s1, s2

avalues = [1.0, 0.5, 0.2, 0.1, 0.05, 0.02]
rows = []
for a in avalues:
    g, c, l2, s1, s2 = gap_and_count(a)
    rows.append({"a": a, "min_slope": round(float(s1), 6),
                 "lyapunov_branch1": round(float(np.log(s1)), 6),
                 "gap": round(float(g), 6), "|lambda2|": round(float(l2), 6),
                 "count_|lam|>0.9": c})
    print(rows[-1])

# Collar lemma widths
l1vals = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.01]
collars = [{"l1": l, "collar_width": round(float(2 * np.arcsinh(1 / np.sinh(l / 2))), 6)}
           for l in l1vals]
print(collars)

# Pressure-regime note: model Hausdorff dimension of the degenerating limit set.
# For doubled pants with funnels bounded away from 0/oo, delta is typically > 1/2
# on an open set (funnel flare -> large limit set); continuity in (l1,l2) then
# forces any rectangle K of positive width to meet {delta > 1/2}, where the
# classical Patterson-Sullivan pressure gap gives nothing. Illustrative model:
# delta_model(l1,l2) = 0.5 + 0.25*tanh(1/l2_scale...) -- we simply record that a
# continuous delta with range straddling 1/2 exists generically, so the
# "unconditional (not conditional on delta<=1/2)" clause forces the proof into
# the regime where even the fixed-surface sharp gap is open.
note = ("Any K=[0,l*]x[w0,w1] of positive width contains an interval of l2 at "
        "l1=0; delta(0,l2) varies continuously in l2 and exceeds 1/2 for an open "
        "set of generic funnel parameters (large-flare pants have delta close "
        "to 1), so the target must work where the pressure gap is vacuous.")

out = {"toy_transfer_collapse": rows, "collar_widths": collars,
       "pressure_regime_note": note,
       "conclusion": ("gap(a) decreases monotonically toward 0 and the "
                      "near-unit eigenvalue count grows as a->0: no uniform "
                      "beta0/N persists in the toy degeneration.")}

with open("results.json", "w") as f:
    json.dump(out, f, indent=2)

# monotonicity checks (fail loudly if not reproduced)
gaps = [r["gap"] for r in rows]
assert all(g2 < g1 for g1, g2 in zip(gaps, gaps[1:])), "gap not monotone decreasing"
counts = [r["count_|lam|>0.9"] for r in rows]
assert counts[-1] > counts[0], "strip count did not grow"
print("MONOTONICITY CHECKS PASSED")
