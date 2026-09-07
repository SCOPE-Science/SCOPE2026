#!/usr/bin/env python3
"""Bit-reproducible rigorous certificate for a period-7 saddle of the Henon map.

Map: H_{a,b}(x,y) = (1 - a*x^2 + y, b*x), b=0.3, a=1.4 = 7/5 exactly.
Stacked system in R^14: F(z) = (H(z0)-z1, ..., H(z6)-z0), z_i=(x_i,y_i).

Proof method: exact rational (Fraction) interval arithmetic. All inclusion
inequalities are checked with exact comparisons. Float values are only used
as human-readable outward-rounded logs (math.nextafter 2-ulp inflation).

Usage:
  python3 prove_henon_p7.py --verify   # full check, <10 min, stdlib only
"""
import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction

# ---------------------------------------------------------------- constants
A_MID = Fraction(7, 5)     # 1.4 exactly
B_PAR = Fraction(3, 10)    # 0.3 exactly

# Midpoints (float literals, repr round-trip exact on CPython IEEE-754).
# Orbit P7-A in H-cyclic order: H(p_i)=p_{i+1 mod 7}, tr(DH^7)~35.74.
MIDS_FLOATS = [
    1.1789439679953058, 0.06536705795928303,
    -0.8805053735822396, 0.3536831903985917,
    0.2682775923285127, -0.26415161207467186,
    0.635086374761511, 0.08048327769855382,
    0.5158146929277482, 0.1905259124284533,
    0.8180351960122474, 0.15474440787832444,
    0.2178901931976101, 0.2454105588036742,
]

# Approximate inverse C = DF(mid)^{-1} computed once with numpy (offline),
# hardcoded as floats. ANY matrix C works for Krawczyk soundness; this one
# gives strong contraction. Stored with repr so float->Fraction is exact.
C_FLOATS = [
 [-0.28810825319728456, -0.13503089110645156, -0.13503089110645153, 0.1493297913847871, 0.1493297913847871, -0.07619249266229396, -0.07619249266229396, 0.04613704109252361, 0.04613704109252361, -0.03185878115945361, -0.03185878115945361, -0.08945150306944734, -0.08945150306944734, -0.2881082531972846],
 [0.1182406946759861, 0.055490007389530326, 0.055490007389530326, -0.06188401482164291, -0.06188401482164291, 0.030013809298692438, 0.030013809298692438, -0.02837401022943722, -0.02837401022943722, -0.03655412849153404, -0.03655412849153404, -0.3736706283106607, -0.3736706283106607, -0.8817593053240139],
 [0.06929845893847425, 0.50123280016588, 0.5012328001658799, -0.5548280938479009, -0.5548280938479009, 0.281528512264759, 0.281528512264759, -0.18067437186154756, -0.18067437186154756, 0.06861308156020289, 0.06861308156020289, -0.07838736038951288, -0.07838736038951288, 0.06929845893847425],
 [-0.08643247595918538, -1.0405092673319356, -0.04050926733193546, 0.04479893741543613, 0.04479893741543613, -0.02285774779868819, -0.02285774779868819, 0.013841112327757083, 0.013841112327757083, -0.009557634347836085, -0.009557634347836085, -0.026835450920834204, -0.026835450920834204, -0.08643247595918538],
 [0.08441698737443996, 0.19523761976090903, 0.19523761976090903, -1.323082593117474, -1.323082593117474, 0.6712268822253663, 0.6712268822253663, -0.43159620249177044, -0.43159620249177044, 0.15960208928519026, 0.15960208928519026, -0.22009282864373653, -0.22009282864373653, 0.08441698737443996],
 [0.020789537681542278, 0.15036984004976398, 0.15036984004976398, -1.1664484281543703, -0.16644842815437028, 0.08445855367942769, 0.08445855367942769, -0.05420231155846426, -0.05420231155846426, 0.020583924468060864, 0.020583924468060864, -0.02351620811685386, -0.02351620811685386, 0.020789537681542278],
 [-0.042622583466893106, 0.003711780077826241, 0.003711780077826241, -0.17257887306107106, -0.17257887306107106, -0.41975181555543956, -0.41975181555543956, 0.2700029406168757, 0.2700029406168757, -0.09930553541522638, -0.09930553541522638, 0.1418125195236241, 0.1418125195236241, -0.042622583466893106],
 [0.025325096212331984, 0.058571285928272716, 0.058571285928272716, -0.3969247779352421, -0.3969247779352421, -0.7986319353323901, 0.20136806466760987, -0.12947886074753112, -0.12947886074753112, 0.04788062678555707, 0.04788062678555707, -0.06602784859312096, -0.06602784859312096, 0.025325096212331984],
 [0.10111835785981733, 0.05197084325836445, 0.05197084325836445, -0.09003780354745082, -0.09003780354745082, -0.05221169057852391, -0.05221169057852395, -0.6096093891952246, -0.6096093891952246, 0.22446988573125654, 0.22446988573125654, -0.3182048055692733, -0.3182048055692733, 0.10111835785981733],
 [-0.012786775040067932, 0.001113534023347869, 0.001113534023347869, -0.05177366191832134, -0.05177366191832134, -0.12592554466663186, -0.12592554466663192, -0.9189991178149374, 0.08100088218506271, -0.029791660624567923, -0.029791660624567923, 0.04254375585708724, 0.04254375585708724, -0.012786775040067932],
 [-0.15883011222476343, -0.07394697473487842, -0.07394697473487842, 0.07826623965008696, 0.07826623965008696, -0.05051718466623212, -0.05051718466623212, -0.03855177411283817, -0.03855177411283817, -0.3539892831285534, -0.3539892831285533, 0.502120955261063, 0.502120955261063, -0.15883011222476343],
 [0.030335507357945192, 0.015591252977509334, 0.015591252977509334, -0.027011341064235236, -0.027011341064235236, -0.015663507173557172, -0.01566350717355718, -0.18288281675856735, -0.18288281675856735, -0.9326590342806231, 0.06734096571937695, -0.09546144167078198, -0.09546144167078198, 0.030335507357945192],
 [0.3941356489199537, 0.18496669129843443, 0.18496669129843443, -0.20628004940547637, -0.20628004940547637, 0.10004603099564147, 0.10004603099564147, -0.09458003409812407, -0.09458003409812407, -0.12184709497178013, -0.12184709497178013, -1.2455687610355357, -1.2455687610355357, 0.3941356489199537],
 [-0.047649033667429036, -0.02218409242046352, -0.02218409242046352, 0.023479871895026084, 0.023479871895026084, -0.015155155399869636, -0.015155155399869636, -0.011565532233851454, -0.011565532233851454, -0.106196784938566, -0.106196784938566, -0.8493637134216812, 0.1506362865783189, -0.047649033667429036],
]

R_POINT = Fraction(1, 2000000000)   # 5e-10 radius -> width 1e-09
R_PERSIST = Fraction(1, 2000)       # 5e-04 radius -> width 1e-03
D_PERSIST = Fraction(1, 20000)      # 5e-05 half-width in a
MU_FRAC = Fraction(1, 5)            # cone Q=diag(1,-mu)
LAM_FRAC = Fraction(10, 1)          # cone expansion

# ---------------------------------------------------------------- helpers

def outward_floats(lo, hi):
    """Outward 2-ulp float enclosure of Fraction interval [lo,hi]."""
    lof = float(lo)
    hif = float(hi)
    # 2 ulps outward each side (covers any 1-ulp conversion error)
    lof = math.nextafter(math.nextafter(lof, -math.inf), -math.inf)
    hif = math.nextafter(math.nextafter(hif, math.inf), math.inf)
    # handle exact endpoints that may be -0.0 etc: ensure lof<=float(lo), hif>=float(hi)
    return lof, hif


def solve_14_float(A, b):
    """Deterministic Gaussian elimination with partial pivoting (floats)."""
    n = 14
    M = [row[:] + [bi] for row, bi in zip(A, b)]
    for k in range(n):
        # pivot
        piv = max(range(k, n), key=lambda i: abs(M[i][k]))
        if M[piv][k] == 0.0:
            raise RuntimeError("singular")
        M[k], M[piv] = M[piv], M[k]
        pivv = M[k][k]
        for i in range(k + 1, n):
            f = M[i][k] / pivv
            if f != 0.0:
                for j in range(k, n + 1):
                    M[i][j] -= f * M[k][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = s / M[i][i]
    return x


def F_float(z, a=1.4, b=0.3):
    out = [0.0] * 14
    for i in range(7):
        xi, yi = z[2 * i], z[2 * i + 1]
        xn = z[2 * ((i + 1) % 7)]
        yn = z[2 * ((i + 1) % 7) + 1]
        out[2 * i] = 1 - a * xi * xi + yi - xn
        out[2 * i + 1] = b * xi - yn
    return out


def J_float(z, a=1.4, b=0.3):
    J = [[0.0] * 14 for _ in range(14)]
    for i in range(7):
        x = z[2 * i]
        J[2 * i][2 * i] = -2 * a * x
        J[2 * i][2 * i + 1] = 1.0
        J[2 * i][2 * ((i + 1) % 7)] -= 1.0
        J[2 * i + 1][2 * i] = b
        J[2 * i + 1][2 * ((i + 1) % 7) + 1] -= 1.0
    return J


def mul_ii_scalar(alo, ahi, blo, bhi):
    c = (alo * blo, alo * bhi, ahi * blo, ahi * bhi)
    return (min(c), max(c))


def cert_sqrt_interval(dlo, dhi):
    """Rigorous [slo,shi] with slo^2<=dlo, shi^2>=dhi (Fractions, dlo>0)."""
    assert dlo > 0 and dhi >= dlo
    flo, fhi = float(dlo), float(dhi)
    slo = Fraction(math.sqrt(flo)) - Fraction(1, 10 ** 12)
    shi = Fraction(math.sqrt(fhi)) + Fraction(1, 10 ** 12)
    if slo < 0:
        slo = Fraction(0)
    guard = 0
    while slo * slo > dlo:
        slo -= Fraction(1, 10 ** 12)
        guard += 1
        assert guard < 10000
    guard = 0
    while shi * shi < dhi:
        shi += Fraction(1, 10 ** 12)
        guard += 1
        assert guard < 10000
    return slo, shi


# ---------------------------------------------------------------- main verify
def verify(log_path=None):
    logs = []

    def emit(rec):
        logs.append(rec)

    M = [Fraction(x) for x in MIDS_FLOATS]
    C = [[Fraction(x) for x in row] for row in C_FLOATS]

    # ---- (1) Newton seed-search reproducibility (pure-python floats)
    seed = [round(x, 6) for x in MIDS_FLOATS]
    z = list(seed)
    for _ in range(6):
        f = F_float(z)
        J = J_float(z)
        dz = solve_14_float(J, [-v for v in f])
        z = [zi + d for zi, d in zip(z, dz)]
    fres = math.sqrt(sum(v * v for v in F_float(z)))
    maxdev = max(abs(a - b) for a, b in zip(z, MIDS_FLOATS))
    emit({"step": "newton_seed", "seed_rounded_6dp": seed,
          "final_residual_norm": fres,
          "max_deviation_to_midpoints": maxdev,
          "pass": bool(fres < 1e-13 and maxdev < 1e-9)})
    assert fres < 1e-13, fres
    assert maxdev < 1e-9, maxdev
    # minimal-period separation of seed (float)
    pts = [(z[2 * i], z[2 * i + 1]) for i in range(7)]
    dmin = min(math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
               for i in range(7) for j in range(i + 1, 7))
    emit({"step": "seed_minimal_period", "pairwise_dmin": dmin, "pass": bool(dmin > 1e-6)})
    assert dmin > 1e-6

    # ---- (2) exact residual at M
    fvec = []
    for i in range(7):
        xi, yi = M[2 * i], M[2 * i + 1]
        xn = M[2 * ((i + 1) % 7)]
        yn = M[2 * ((i + 1) % 7) + 1]
        fvec.append(Fraction(1, 1) - A_MID * xi * xi + yi - xn)
        fvec.append(B_PAR * xi - yn)
    max_abs_f = max(abs(v) for v in fvec)
    emit({"step": "residual", "max_abs_F_mid_exact": str(max_abs_f),
          "max_abs_F_mid_float": float(max_abs_f), "pass": bool(max_abs_f < Fraction(1, 10 ** 13))})
    assert max_abs_f < Fraction(1, 10 ** 13)

    # ---- (3) point Krawczyk, R_POINT
    r = R_POINT
    CF = [sum(C[i][j] * fvec[j] for j in range(14)) for i in range(14)]
    max_CF = max(abs(v) for v in CF)
    Xlo = [M[2 * i] - r for i in range(7)]
    Xhi = [M[2 * i] + r for i in range(7)]
    Jlo = [[Fraction(0)] * 14 for _ in range(14)]
    Jhi = [[Fraction(0)] * 14 for _ in range(14)]
    for i in range(7):
        Jlo[2 * i][2 * i] = -2 * A_MID * Xhi[i]
        Jhi[2 * i][2 * i] = -2 * A_MID * Xlo[i]
        Jlo[2 * i][2 * i + 1] = Jhi[2 * i][2 * i + 1] = Fraction(1)
        Jlo[2 * i][2 * ((i + 1) % 7)] = Jhi[2 * i][2 * ((i + 1) % 7)] = Fraction(-1)
        Jlo[2 * i + 1][2 * i] = Jhi[2 * i + 1][2 * i] = B_PAR
        Jlo[2 * i + 1][2 * ((i + 1) % 7) + 1] = Jhi[2 * i + 1][2 * ((i + 1) % 7) + 1] = Fraction(-1)
    Elo = [[Fraction(0)] * 14 for _ in range(14)]
    Ehi = [[Fraction(0)] * 14 for _ in range(14)]
    for i in range(14):
        for k in range(14):
            slo = Fraction(0)
            shi = Fraction(0)
            for j in range(14):
                c = C[i][j]
                lo, hi = Jlo[j][k], Jhi[j][k]
                if lo == 0 and hi == 0:
                    continue
                if lo == hi:
                    slo += c * lo
                    shi += c * lo
                else:
                    if c >= 0:
                        slo += c * lo
                        shi += c * hi
                    else:
                        slo += c * hi
                        shi += c * lo
            if i == k:
                Elo[i][k] = Fraction(1) - shi
                Ehi[i][k] = Fraction(1) - slo
            else:
                Elo[i][k] = -shi
                Ehi[i][k] = -slo
    q = max(sum(max(abs(Elo[i][j]), abs(Ehi[i][j])) for j in range(14)) for i in range(14))
    centers = [M[i] - CF[i] for i in range(14)]
    S = [sum(max(abs(Elo[i][j]), abs(Ehi[i][j])) for j in range(14)) * r for i in range(14)]
    Klo = [centers[i] - S[i] for i in range(14)]
    Khi = [centers[i] + S[i] for i in range(14)]
    Blo = [M[i] - r for i in range(14)]
    Bhi = [M[i] + r for i in range(14)]
    margins = [min(Bhi[i] - Khi[i], Klo[i] - Blo[i]) for i in range(14)]
    ok = all(Klo[i] > Blo[i] and Khi[i] < Bhi[i] for i in range(14))
    min_margin = min(margins)
    emit({"step": "krawczyk_point", "r": str(r), "width": str(2 * r),
          "max_abs_CF_float": float(max_CF), "q_float": float(q), "q_exact": str(q),
          "min_margin_float": float(min_margin), "min_margin_exact": str(min_margin),
          "pass": bool(ok and min_margin >= Fraction(1, 10 ** 12))})
    assert ok and min_margin >= Fraction(1, 10 ** 12), "point Krawczyk failed"
    # log boxes with outward floats
    for i in range(7):
        for c, nm in ((2 * i, "x"), (2 * i + 1, "y")):
            lof, hif = outward_floats(Blo[c], Bhi[c])
            klo, khi = outward_floats(Klo[c], Khi[c])
            emit({"step": "box_point", "box": i, "coord": nm,
                  "mid": MIDS_FLOATS[c], "r": float(r),
                  "Blo": lof, "Bhi": hif, "Klo": klo, "Khi": khi,
                  "width": hif - lof})

    # ---- (4) pairwise disjointness + minimal period (exact, Linf)
    # boxes in R2: Bi = [M_x-r,M_x+r]x[M_y-r,M_y+r]
    def box_xy(i):
        return (M[2 * i] - r, M[2 * i] + r, M[2 * i + 1] - r, M[2 * i + 1] + r)
    pairs_ok = True
    min_gap = None
    for i in range(7):
        for j in range(i + 1, 7):
            xlo0, xhi0, ylo0, yhi0 = box_xy(i)
            xlo1, xhi1, ylo1, yhi1 = box_xy(j)
            gx = max(xlo1 - xhi0, xlo0 - xhi1)
            gy = max(ylo1 - yhi0, ylo0 - yhi1)
            gap = max(gx, gy)  # Linf gap; >0 iff disjoint
            if min_gap is None or gap < min_gap:
                min_gap = gap
            if gap <= 0:
                pairs_ok = False
            emit({"step": "disjoint_pair", "i": i, "j": j,
                  "gap_Linf_float": float(gap), "gap_Linf_exact": str(gap),
                  "disjoint": bool(gap > 0)})
    emit({"step": "disjoint_all", "min_gap_Linf_float": float(min_gap),
          "min_gap_Linf_exact": str(min_gap),
          "pass": bool(pairs_ok and min_gap > Fraction(1, 10 ** 6))})
    assert pairs_ok and min_gap > Fraction(1, 10 ** 6)
    emit({"step": "minimal_period",
          "argument": "7 prime; F=0 gives H(p_i)=p_{i+1}; disjointness forbids period 1, hence minimal period exactly 7",
          "pass": True})

    # ---- (5) interval monodromy M=DH^7 over point boxes
    J2lo, J2hi = [], []
    for i in range(7):
        J2lo.append([[-2 * A_MID * Xhi[i], Fraction(1)], [B_PAR, Fraction(0)]])
        J2hi.append([[-2 * A_MID * Xlo[i], Fraction(1)], [B_PAR, Fraction(0)]])

    def matmul2(Alo, Ahi, Blo, Bhi):
        Clo = [[Fraction(0)] * 2 for _ in range(2)]
        Chi = [[Fraction(0)] * 2 for _ in range(2)]
        for ii in range(2):
            for kk in range(2):
                sl = Fraction(0)
                sh = Fraction(0)
                for jj in range(2):
                    plo, phi = mul_ii_scalar(Alo[ii][jj], Ahi[ii][jj], Blo[jj][kk], Bhi[jj][kk])
                    sl += plo
                    sh += phi
                Clo[ii][kk] = sl
                Chi[ii][kk] = sh
        return Clo, Chi

    Mlo = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    Mhi = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    for i in range(7):
        Mlo, Mhi = matmul2(J2lo[i], J2hi[i], Mlo, Mhi)
    tr_lo, tr_hi = Mlo[0][0] + Mlo[1][1], Mhi[0][0] + Mhi[1][1]
    p1 = mul_ii_scalar(Mlo[0][0], Mhi[0][0], Mlo[1][1], Mhi[1][1])
    p2 = mul_ii_scalar(Mlo[0][1], Mhi[0][1], Mlo[1][0], Mhi[1][0])
    det_lo, det_hi = p1[0] - p2[1], p1[1] - p2[0]
    tr2 = mul_ii_scalar(tr_lo, tr_hi, tr_lo, tr_hi)
    Dlo = tr2[0] - 4 * det_hi
    Dhi = tr2[1] - 4 * det_lo
    assert Dlo > 0
    slo, shi = cert_sqrt_interval(Dlo, Dhi)
    lam1_lo, lam1_hi = (tr_lo + slo) / 2, (tr_hi + shi) / 2
    lam2_lo, lam2_hi = (tr_lo - shi) / 2, (tr_hi - slo) / 2
    # saddle: |lam1|>1, |lam2|<1, both off unit circle
    assert lam1_lo > 1
    assert lam2_lo > -1 and lam2_hi < 1
    # also det magnitude check
    assert abs(float(det_lo)) < 1 and abs(float(det_hi)) < 1
    emit({"step": "monodromy", "Mlo": [[float(v) for v in row] for row in Mlo],
          "Mhi": [[float(v) for v in row] for row in Mhi],
          "tr": [float(tr_lo), float(tr_hi)], "det": [float(det_lo), float(det_hi)],
          "disc": [float(Dlo), float(Dhi)], "sqrt": [float(slo), float(shi)],
          "lam_u": [float(lam1_lo), float(lam1_hi)],
          "lam_s": [float(lam2_lo), float(lam2_hi)],
          "lam_u_margin": float(lam1_lo - 1),
          "lam_s_margin": float(1 - max(abs(lam2_lo), abs(lam2_hi))),
          "pass": True})

    # ---- (6) cone Q=diag(1,-mu), N=M^T Q M - lam Q >> 0
    mu, lam = MU_FRAC, LAM_FRAC
    QMlo = [[Mlo[0][0], Mlo[0][1]], [-mu * Mhi[1][0], -mu * Mhi[1][1]]]
    QMhi = [[Mhi[0][0], Mhi[0][1]], [-mu * Mlo[1][0], -mu * Mlo[1][1]]]
    t1 = mul_ii_scalar(Mlo[0][0], Mhi[0][0], QMlo[0][0], QMhi[0][0])
    t2 = mul_ii_scalar(Mlo[1][0], Mhi[1][0], QMlo[1][0], QMhi[1][0])
    N11lo, N11hi = t1[0] + t2[0] - lam, t1[1] + t2[1] - lam
    t3 = mul_ii_scalar(Mlo[0][1], Mhi[0][1], QMlo[0][1], QMhi[0][1])
    t4 = mul_ii_scalar(Mlo[1][1], Mhi[1][1], QMlo[1][1], QMhi[1][1])
    N22lo, N22hi = t3[0] + t4[0] + lam * mu, t3[1] + t4[1] + lam * mu
    t5 = mul_ii_scalar(Mlo[0][0], Mhi[0][0], QMlo[0][1], QMhi[0][1])
    t6 = mul_ii_scalar(Mlo[1][0], Mhi[1][0], QMlo[1][1], QMhi[1][1])
    N12lo, N12hi = t5[0] + t6[0], t5[1] + t6[1]
    d1 = mul_ii_scalar(N11lo, N11hi, N22lo, N22hi)
    e1 = mul_ii_scalar(N12lo, N12hi, N12lo, N12hi)
    detNlo, detNhi = d1[0] - e1[1], d1[1] - e1[0]
    assert N11lo > 0 and detNlo > 0
    emit({"step": "cone", "mu": str(mu), "lambda": str(lam),
          "N11": [float(N11lo), float(N11hi)],
          "N22": [float(N22lo), float(N22hi)],
          "N12": [float(N12lo), float(N12hi)],
          "detN": [float(detNlo), float(detNhi)],
          "N11_margin": float(N11lo), "detN_margin": float(detNlo),
          "pass": True})

    # ---- (7) uniform persistence over A=[1.4-d,1.4+d], d=5e-05, tubes R_PERSIST
    R = R_PERSIST
    d = D_PERSIST
    Alo, Ahi = A_MID - d, A_MID + d
    Flo = [None] * 14
    Fhi = [None] * 14
    for i in range(7):
        xi, yi = M[2 * i], M[2 * i + 1]
        xn = M[2 * ((i + 1) % 7)]
        Flo[2 * i] = Fraction(1, 1) - Ahi * xi * xi + yi - xn
        Fhi[2 * i] = Fraction(1, 1) - Alo * xi * xi + yi - xn
        fy = B_PAR * xi - M[2 * ((i + 1) % 7) + 1]
        Flo[2 * i + 1] = Fhi[2 * i + 1] = fy
    CFlo = [Fraction(0)] * 14
    CFhi = [Fraction(0)] * 14
    for i in range(14):
        slo = Fraction(0)
        shi = Fraction(0)
        for j in range(14):
            c = C[i][j]
            lo, hi = Flo[j], Fhi[j]
            if lo == hi:
                slo += c * lo
                shi += c * lo
            else:
                if c >= 0:
                    slo += c * lo
                    shi += c * hi
                else:
                    slo += c * hi
                    shi += c * lo
        CFlo[i], CFhi[i] = slo, shi
    PXlo = [M[2 * i] - R for i in range(7)]
    PXhi = [M[2 * i] + R for i in range(7)]

    def mul_ii2(alo, ahi, blo, bhi):
        c = (alo * blo, alo * bhi, ahi * blo, ahi * bhi)
        return (min(c), max(c))

    PJlo = [[Fraction(0)] * 14 for _ in range(14)]
    PJhi = [[Fraction(0)] * 14 for _ in range(14)]
    for i in range(7):
        plo, phi = mul_ii2(Alo, Ahi, PXlo[i], PXhi[i])
        PJlo[2 * i][2 * i] = -2 * phi
        PJhi[2 * i][2 * i] = -2 * plo
        PJlo[2 * i][2 * i + 1] = PJhi[2 * i][2 * i + 1] = Fraction(1)
        PJlo[2 * i][2 * ((i + 1) % 7)] = PJhi[2 * i][2 * ((i + 1) % 7)] = Fraction(-1)
        PJlo[2 * i + 1][2 * i] = PJhi[2 * i + 1][2 * i] = B_PAR
        PJlo[2 * i + 1][2 * ((i + 1) % 7) + 1] = PJhi[2 * i + 1][2 * ((i + 1) % 7) + 1] = Fraction(-1)
    PElo = [[Fraction(0)] * 14 for _ in range(14)]
    PEhi = [[Fraction(0)] * 14 for _ in range(14)]
    for i in range(14):
        for k in range(14):
            slo = Fraction(0)
            shi = Fraction(0)
            for j in range(14):
                c = C[i][j]
                lo, hi = PJlo[j][k], PJhi[j][k]
                if lo == 0 and hi == 0:
                    continue
                if lo == hi:
                    slo += c * lo
                    shi += c * lo
                else:
                    if c >= 0:
                        slo += c * lo
                        shi += c * hi
                    else:
                        slo += c * hi
                        shi += c * lo
            if i == k:
                PElo[i][k] = Fraction(1) - shi
                PEhi[i][k] = Fraction(1) - slo
            else:
                PElo[i][k] = -shi
                PEhi[i][k] = -slo
    pq = max(sum(max(abs(PElo[i][j]), abs(PEhi[i][j])) for j in range(14)) for i in range(14))
    PKlo, PKhi, PBlo, PBhi = [], [], [], []
    for i in range(14):
        clo, chi = M[i] - CFhi[i], M[i] - CFlo[i]
        S = sum(max(abs(PElo[i][j]), abs(PEhi[i][j])) for j in range(14)) * R
        PKlo.append(clo - S)
        PKhi.append(chi + S)
        PBlo.append(M[i] - R)
        PBhi.append(M[i] + R)
    pok = all(PKlo[i] > PBlo[i] and PKhi[i] < PBhi[i] for i in range(14))
    pmargins = [min(PBhi[i] - PKhi[i], PKlo[i] - PBlo[i]) for i in range(14)]
    pmin = min(pmargins)
    emit({"step": "persistence", "A": [float(Alo), float(Ahi)], "d": str(d),
          "R": str(R), "tube_width": str(2 * R), "q_float": float(pq),
          "min_margin_float": float(pmin), "min_margin_exact": str(pmin),
          "pass": bool(pok)})
    assert pok, "persistence Krawczyk failed"
    for i in range(7):
        for c, nm in ((2 * i, "x"), (2 * i + 1, "y")):
            lof, hif = outward_floats(PBlo[c], PBhi[c])
            emit({"step": "tube_persist", "box": i, "coord": nm,
                  "Blo": lof, "Bhi": hif, "width": hif - lof})

    # persistence tubes disjointness (Linf, radius R)
    pgap = None
    pall = True
    for i in range(7):
        for j in range(i + 1, 7):
            xlo0, xhi0 = M[2 * i] - R, M[2 * i] + R
            ylo0, yhi0 = M[2 * i + 1] - R, M[2 * i + 1] + R
            xlo1, xhi1 = M[2 * j] - R, M[2 * j] + R
            ylo1, yhi1 = M[2 * j + 1] - R, M[2 * j + 1] + R
            gx = max(xlo1 - xhi0, xlo0 - xhi1)
            gy = max(ylo1 - yhi0, ylo0 - yhi1)
            gap = max(gx, gy)
            if pgap is None or gap < pgap:
                pgap = gap
            if gap <= 0:
                pall = False
    emit({"step": "persistence_disjoint", "min_gap_Linf_float": float(pgap),
          "min_gap_Linf_exact": str(pgap), "pass": bool(pall)})
    assert pall

    # ---- summary
    emit({"step": "summary", "claim": "period-7 saddle at (1.4,0.3), boxes width 1e-09, cone, persistence d=5e-05",
          "all_pass": True})
    if log_path is not None:
        with open(log_path, "w") as fh:
            for rec in logs:
                fh.write(json.dumps(rec, sort_keys=True, separators=(",", ":")) + "\n")
        with open(log_path, "rb") as fh:
            h = hashlib.sha256(fh.read()).hexdigest()
        print("wrote", log_path, "records", len(logs), "sha256", h)
        return logs, h
    return logs, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--log", default=None)
    args = ap.parse_args()
    if not args.verify:
        ap.print_help()
        sys.exit(2)
    import os
    log_path = args.log or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        "interval_log.jsonl")
    logs, h = verify(log_path)
    print("VERIFY OK: %d records, sha256=%s" % (len(logs), h))
    # print key margins for audit
    for rec in logs:
        if rec.get("step") in ("krawczyk_point", "monodromy", "cone", "persistence",
                               "disjoint_all", "residual"):
            print(json.dumps(rec, sort_keys=True))


if __name__ == "__main__":
    main()
