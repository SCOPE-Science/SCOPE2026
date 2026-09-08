"""Certified finite-word trace-minimum census over a Bolza-value Fricke window.

Coordinates: (x,y,z) = (tr A, tr B, tr AB), Fricke-Vogt coordinates on X(F2)
(no relation; every triple with z^2 > 4 occurs for real A,B in SL(2,R)).
Explicit lift: A = [[0,-1],[1,x]], B = [[y, z+c],[c, 0]], c = (-z+s)/2,
s^2 = D = z^2-4. det A = 1; det B = -c(z+c) = 1 since c^2+zc+1 = 0;
tr A = x, tr B = y, tr AB = z (checked exactly at every point).

Every word trace computed in Q(sqrt(D)) MUST have zero sqrt-part (it equals
the Fricke integer polynomial at (x,y,z)); asserted for every word at every
grid point (self-checking lift).

Words: all reduced words in F(a,b), length 1..8 = 13120 words.
L = 2*arccosh(|t|/2) enclosed by rigorous cosh-Taylor interval bounds;
collar w = arcsinh(1/sinh(L/2)) via rigorous sinh bounds (stdlib only).

Box B = [13/3, 16/3]^3 (center c0 = 29/6 within 0.005 of T = 2+2*sqrt(2),
the Bolza systole trace value). Base grid 5x5x5 step 1/4 + 3x3x3 half-step
refinement around the base argmax.
"""
import math
import csv
import json
import time
from fractions import Fraction as F


class QE:
    """a + b*sqrt(D); D class-level Fraction. No division is ever used."""
    __slots__ = ("p", "q")
    D = F(1)

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(a, b):
        return QE(a.p + b.p, a.q + b.q)

    def __sub__(a, b):
        return QE(a.p - b.p, a.q - b.q)

    def __mul__(a, b):
        return QE(a.p * b.p + QE.D * a.q * b.q,
                  a.p * b.q + a.q * b.p)


def mmul(M, N):
    a, b, c, d = M
    e, f, g, h = N
    return (a * e + b * g, a * f + b * h,
            c * e + d * g, c * f + d * h)


def build_mats(x, y, z, branch):
    D = z * z - 4
    assert D > 0
    QE.D = D
    Z = QE(F(0), F(0))
    A = (Z, QE(-F(1), F(0)), QE(F(1), F(0)), QE(x, F(0)))
    Ainv = (QE(x, F(0)), QE(F(1), F(0)), QE(-F(1), F(0)), Z)
    c = QE(-z / 2, F(branch, 2))
    b = QE(z, F(0)) + c
    B = (QE(y, F(0)), b, c, Z)
    Binv = (Z, QE(F(0), F(0)) - b, QE(F(0), F(0)) - c, QE(y, F(0)))
    dA = A[0] * A[3] - A[1] * A[2]
    dB = B[0] * B[3] - B[1] * B[2]
    assert dA.p == 1 and dA.q == 0
    assert dB.p == 1 and dB.q == 0
    assert (A[0] + A[3]).p == x and (B[0] + B[3]).p == y
    AB = mmul(A, B)
    assert (AB[0] + AB[3]).p == z and (AB[0] + AB[3]).q == 0
    return A, B, Ainv, Binv


LETS = ("a", "b", "A", "B")
GIDX = {"a": 0, "b": 1, "A": 2, "B": 3}
INV = (2, 3, 0, 1)


def min_trace_point(x, y, z, branch):
    """Return (tmin, wmin, t2, w2, nchecked). Exact Fractions."""
    gen = build_mats(x, y, z, branch)
    Z = QE(F(0), F(0))
    I = (QE(F(1), F(0)), Z, Z, QE(F(1), F(0)))
    best1 = None  # (abstrace, word, trace)
    best2 = None  # second DISTINCT abstrace value
    n = 0
    prev = [((), I)]
    for _ in range(8):
        cur = []
        for w, M in prev:
            li = GIDX[w[-1]] if w else -1
            for g in range(4):
                if w and g == INV[li]:
                    continue
                M2 = mmul(M, gen[g])
                tr = M2[0] + M2[3]
                assert tr.q == 0, f"sqrt-part nonzero at {w}: {tr.q}"
                t = tr.p
                at = abs(t)
                w2_ = w + (LETS[g],)
                n += 1
                if best1 is None or at < best1[0]:
                    if best1 is not None:
                        best2 = best1
                    best1 = (at, w2_, t)
                elif at > best1[0] and (best2 is None or at < best2[0]):
                    best2 = (at, w2_, t)
                cur.append((w2_, M2))
        prev = cur
    assert n == 13120, n
    return best1[2], "".join(best1[1]), best2[2], "".join(best2[1]), n


def cosh_bounds(v, N=20):
    assert v >= 0
    s = F(0)
    term = F(1)
    for k in range(1, N + 1):
        term = term * v * v / ((2 * k - 1) * (2 * k))
        s += term
    lo = F(1) + s
    r = v * v / ((2 * N + 3) * (2 * N + 4))
    assert r < 1
    tNp1 = term * v * v / ((2 * N + 1) * (2 * N + 2))
    return lo, lo + tNp1 / (1 - r)


def sinh_bounds(v, N=20):
    assert v >= 0
    s = F(0)
    term = v
    for k in range(1, N + 1):
        term = term * v * v / ((2 * k) * (2 * k + 1))
        s += term
    lo = v + s
    r = v * v / ((2 * N + 4) * (2 * N + 5))
    assert r < 1
    tNp1 = term * v * v / ((2 * N + 2) * (2 * N + 3))
    return lo, lo + tNp1 / (1 - r)


def certify_length(u, est):
    assert u >= 1
    e = F(1, 10**6)
    while True:
        Llo, Lhi = F(est) - e, F(est) + e
        assert Llo > 0
        _, chi = cosh_bounds(Llo / 2)
        clo, _ = cosh_bounds(Lhi / 2)
        if chi <= u and clo >= u:
            return Llo, Lhi
        e *= 10
        assert e < 1, "length certification failed"


def certify_collar(Llo, Lhi, est):
    slo, _ = sinh_bounds(Llo / 2)
    _, shi = sinh_bounds(Lhi / 2)
    assert slo > 0
    v_lo, v_hi = 1 / shi, 1 / slo
    e = F(1, 10**6)
    while True:
        wlo, whi = F(est) - e, F(est) + e
        assert wlo > 0
        _, shi_w = sinh_bounds(wlo)
        slo_w, _ = sinh_bounds(whi)
        if shi_w <= v_lo and slo_w >= v_hi:
            return wlo, whi
        e *= 10
        assert e < F(1, 100), "collar certification failed"


def process_point(x, y, z, branch, kind):
    t, w, t2, w2, n = min_trace_point(x, y, z, branch)
    assert abs(t) > 2, f"non-hyperbolic min trace {t}"
    u = abs(t) / 2
    est = 2.0 * math.acosh(float(u))
    Llo, Lhi = certify_length(u, est)
    west = math.asinh(1.0 / math.sinh(est / 2.0))
    wlo, whi = certify_collar(Llo, Lhi, west)
    return {
        "kind": kind, "x": str(x), "y": str(y), "z": str(z),
        "word": w, "wlen": len(w), "trace": str(t), "trace_f": float(t),
        "run_word": w2, "run_trace": str(t2),
        "tie": str(abs(t2) == abs(t)), "nchecked": n,
        "Llo": str(Llo), "Lhi": str(Lhi),
        "Lmid": (float(Llo) + float(Lhi)) / 2,
        "Lwid": float(Lhi) - float(Llo),
        "wlo": str(wlo), "whi": str(whi),
    }


def main(artdir):
    t0 = time.time()
    c0 = F(29, 6)
    half = F(1, 2)
    BLO, BHI = c0 - half, c0 + half
    assert (BLO, BHI) == (F(13, 3), F(16, 3))
    steps = [F(k, 4) for k in (-2, -1, 0, 1, 2)]

    rows = []
    for dx in steps:
        for dy in steps:
            for dz in steps:
                rows.append(process_point(c0 + dx, c0 + dy, c0 + dz, 1,
                                          "base"))
                if len(rows) % 25 == 0:
                    print(f"  base {len(rows)}/125 ({time.time()-t0:.0f}s)",
                          flush=True)

    def ka(i):
        return abs(F(rows[i]["trace"]))

    imax = max(range(len(rows)), key=ka)
    imin = min(range(len(rows)), key=ka)
    print(f"base argmax {rows[imax]['x']},{rows[imax]['y']},{rows[imax]['z']}"
          f" {rows[imax]['word']} tr={rows[imax]['trace']}", flush=True)
    print(f"base argmin {rows[imin]['x']},{rows[imin]['y']},{rows[imin]['z']}"
          f" {rows[imin]['word']} tr={rows[imin]['trace']}", flush=True)

    mx = [F(rows[imax][k]) for k in ("x", "y", "z")]
    added = 0
    for jx in (-1, 0, 1):
        for jy in (-1, 0, 1):
            for jz in (-1, 0, 1):
                pt = [mx[0] + F(jx, 8), mx[1] + F(jy, 8),
                      mx[2] + F(jz, 8)]
                if not all(BLO <= v <= BHI for v in pt):
                    continue
                if all((v - c0) * 4 == int((v - c0) * 4)
                       and abs((v - c0) * 4) <= 2 for v in pt):
                    continue
                rows.append(process_point(*pt, 1, "refined"))
                added += 1
    print(f"refinement added {added}", flush=True)

    J = max(range(len(rows)), key=ka)
    K = min(range(len(rows)), key=ka)
    gap_lo = F(rows[J]["Llo"]) - F(rows[K]["Lhi"])

    u = BHI / 2
    estU = 2.0 * math.acosh(float(u))
    e = F(1, 10**6)
    while True:
        U = F(estU) + e
        clo, _ = cosh_bounds(U / 2)
        if clo >= u:
            break
        e *= 10
    print(f"grid max: {rows[J]['word']} Lmid={rows[J]['Lmid']:.9f} "
          f"[{rows[J]['Llo']},{rows[J]['Lhi']}]", flush=True)
    print(f"grid min: {rows[K]['word']} Lmid={rows[K]['Lmid']:.9f}",
          flush=True)
    print(f"certified gap >= {float(gap_lo):.9f}", flush=True)
    print(f"U(B) <= {float(U):.9f}", flush=True)

    import os
    os.makedirs(artdir, exist_ok=True)
    with open(f"{artdir}/table.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    summary = {
        "box": [str(BLO), str(BHI)], "center": str(c0),
        "T_value": "2+2*sqrt(2) = Bolza systole trace (L1~3.057)",
        "word_cap": 8, "nwords": 13120,
        "base_grid": 125, "refinement_added": added, "total": len(rows),
        "grid_max": rows[J], "grid_min": rows[K],
        "gap_lo": str(gap_lo), "gap_lo_f": float(gap_lo),
        "U_hi": str(U), "U_hi_f": float(U),
        "elapsed_s": round(time.time() - t0, 1),
    }
    with open(f"{artdir}/summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("wrote table.csv summary.json", flush=True)


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "output/artifacts")
