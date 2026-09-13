"""Pentas flower-center frequency + Bragg intensity via cut-and-project dualization.
Methods: window-area frequency (dualization), window-Fourier intensity, regular
model-set pure-point certificate inputs. Verifies exact tau-closed forms numerically.

Conventions: F(k) = int_W exp(-i k.x) dx, so F(0) = |W|.

Lattice/CPS: Minkowski L={(x,x*): x in Z[zeta5]} with *=Gal(zeta->zeta^2);
single-decagon window W (edge 1) is the effective CPS used here; the published
5D P3* scheme (Fujita-Niizeki, Sci Rep 15:41523) uses five class ADs Wp whose
relevant section (S1 flower centers, W2/W3 regular pentagons of radius 1/tau)
is reconciled with the 21-offset acceptance domain in DRAFT Sec. 2b.
"""
import json, math, cmath
import numpy as np

TAU = (1 + math.sqrt(5)) / 2
Z = np.exp(2j * math.pi / 5)          # zeta_5

# ---------- exact Z[zeta5] arithmetic: coeffs of (1,z,z^2,z^3) ----------
def zp(e):
    e %= 5
    if e == 4:
        return (-1, -1, -1, -1)
    v = [0, 0, 0, 0]
    v[e] = 1
    return tuple(v)

def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)

def cint(a):  return sum(c * ((Z ** 2) ** j) for j, c in enumerate(a))

# ---------- convex polygon helpers (CCW), float ----------
def shoelace(p):
    p = np.asarray(p, dtype=float)
    return 0.5 * abs(np.sum(p[:, 0] * np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1) * p[:, 1]))

def clip_half(subject, a, b):
    """Clip convex polygon `subject` to left half-plane of directed edge a->b."""
    out = []
    e = np.asarray(b, float) - np.asarray(a, float)
    for i, p in enumerate(subject):
        q = subject[i - 1]
        p = np.asarray(p, float); q = np.asarray(q, float)
        dp = e[0] * (p[1] - a[1]) - e[1] * (p[0] - a[0])  # cross(e, p-a): >0 left
        dq = e[0] * (q[1] - a[1]) - e[1] * (q[0] - a[0])
        if dp >= -1e-12:
            if dq < -1e-12:
                t = dq / (dq - dp)
                out.append(q + t * (p - q))
            out.append(p)
        elif dq >= -1e-12:
            t = dq / (dq - dp)
            out.append(q + t * (p - q))
    return [np.asarray(x, float) for x in out]

def intersect_convex(P, Q):
    S = [np.asarray(p, float) for p in P]
    n = len(Q)
    for i in range(n):
        S = clip_half(S, np.asarray(Q[i], float), np.asarray(Q[(i + 1) % n], float))
        if len(S) == 0:
            return S
    return S

def regular_poly(n, R, phase=0.0):
    return [np.array([R * math.cos(phase + 2 * math.pi * k / n),
                      R * math.sin(phase + 2 * math.pi * k / n)]) for k in range(n)]

# ---------- 1. tau identities ----------
t = TAU
assert abs(t**2 - (t + 1)) < 1e-15
tinv2 = t ** -2
assert abs(tinv2 - ((3 - math.sqrt(5)) / 2)) < 1e-15
tinv4 = t ** -4
assert abs(tinv4 - ((7 - 3 * math.sqrt(5)) / 2)) < 1e-15

# ---------- 2. window areas: decagon edge 1 (R=tau), pentagon edge 1 ----------
Rdec = 1.0 / (2 * math.sin(math.pi / 10))   # == tau
assert abs(Rdec - TAU) < 1e-12
W = regular_poly(10, Rdec)
Adec = shoelace(W)
Adec_exact = 2.5 * math.sqrt(5 + 2 * math.sqrt(5))   # (5/2)sqrt(5+2sqrt5), edge 1
Rpent = 1.0 / (2 * math.sin(math.pi / 5))
P1 = regular_poly(5, Rpent)
Apent1 = shoelace(P1)
Apent_exact = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))
assert abs(Adec - Adec_exact) < 1e-9, (Adec, Adec_exact)
assert abs(Apent1 - Apent_exact) < 1e-9
ratio_dp = Apent1 / Adec
assert abs(ratio_dp - math.sqrt(5) / 10) < 1e-12, ratio_dp  # exact sqrt5/10

# ---------- 3. pentagram inner-pentagon ratio (pure-geometry check) ----------
V5 = [np.array([Rpent * math.cos(math.pi / 2 + 2 * math.pi * k / 5),
                Rpent * math.sin(math.pi / 2 + 2 * math.pi * k / 5)]) for k in range(5)]
def line_int(p1, p2, p3, p4):
    A = np.column_stack([p2 - p1, -(p4 - p3)])
    s = np.linalg.solve(A, p3 - p1)
    return p1 + s[0] * (p2 - p1)
inner = [line_int(V5[(k - 1) % 5], V5[(k + 1) % 5], V5[k], V5[(k + 2) % 5]) for k in range(5)]
Ainner = shoelace(inner)
assert abs(Ainner / Apent1 - tinv4) < 1e-9, Ainner / Apent1
e_in = float(np.linalg.norm(inner[1] - inner[0]))
assert abs(e_in - tinv2) < 1e-9, e_in

# ---------- 4. two-tier flower patch -> acceptance domain by dualization ----------
ZERO = (0, 0, 0, 0)
verts = set([ZERO])
for j in range(5):
    zj, zj1 = zp(j), zp(j + 1)
    bj = add(zj, zj1)
    verts.update([zj, zj1, bj])                       # inner thick rhomb j
    wj = neg(zp(j + 3))
    verts.update([add(bj, wj), add(zj, wj)])          # outer thin petal j
V = list(verts)
assert len(V) == 1 + 5 + 5 + 10, len(V)               # 0, zj(5), bj(5), petal tips(10)

def c2c(z): return np.array([float(z.real), float(z.imag)])
WF = [np.array(p, float) for p in W]
for v in V:
    sh = c2c(cint(v))
    Q = [np.array(p, float) + np.array(sh, float) for p in W]  # W - v*; intersect
    WF = intersect_convex(WF, Q)
    if len(WF) == 0:
        break
nWF = len(WF)
AWF = shoelace(WF) if nWF >= 3 else 0.0
freq = AWF / Adec
edges = [float(np.linalg.norm(WF[(i + 1) % nWF] - WF[i])) for i in range(nWF)] if nWF >= 3 else []
rel_spread = (max(edges) - min(edges)) / (sum(edges) / len(edges)) if edges else float('nan')

s5 = math.sqrt(5)
best = None
for d in range(1, 41):
    for an in range(-40, 41):
        for bn in range(-40, 41):
            v = an / d + (bn / d) * s5
            err = abs(v - freq)
            if best is None or err < best[0]:
                best = (err, an / d, bn / d, d)
fit_err, fit_a, fit_b, fit_d = best

# ---------- 5. lattice, covolume, density (correct exact constant), Fourier module --
Mp = np.array([[math.cos(2 * math.pi * j / 5), math.sin(2 * math.pi * j / 5)] for j in range(4)]).T  # 2x4
Mq = np.array([[math.cos(4 * math.pi * j / 5), math.sin(4 * math.pi * j / 5)] for j in range(4)]).T  # 2x4
B = np.vstack([Mp, Mq])            # 4x4, columns = lattice basis of R^4
covol = abs(np.linalg.det(B))
assert abs(covol - 5 * s5 / 4) < 1e-9, covol
C = np.linalg.inv(B).T             # dual basis in columns
Cp, Cq = C[:2, :], C[2:, :]
best = None
rng = range(-3, 4)
for n1 in rng:
    for n2 in rng:
        for n3 in rng:
            for n4 in rng:
                if (n1, n2, n3, n4) == (0, 0, 0, 0):
                    continue
                n = np.array([n1, n2, n3, n4], float)
                k = Cp @ n
                m = float(np.linalg.norm(k))
                if best is None or m < best[0]:
                    best = (m, k.copy(), Cq @ n, tuple(n))
mmin, k1, q1, nvec = best
dens = Adec / covol
dens_exact = math.sqrt(4 + 8 / s5)   # = 2*sqrt(1+2/sqrt5); corrected (was sqrt(5+2sqrt5)/2)
assert abs(dens - dens_exact) < 1e-9, (dens, dens_exact)
kstar1 = q1
print(json.dumps({
    "tau": t, "tau_m2": tinv2, "tau_m4": tinv4,
    "Adec": Adec, "Adec_exact_check": Adec_exact,
    "Apent1": Apent1, "pent_over_dec": ratio_dp, "pent_over_dec_exact": math.sqrt(5) / 10,
    "inner_over_outer": Ainner / Apent1, "inner_edge": e_in, "tau_m2_check": tinv2,
    "nWF": nWF, "AWF": AWF, "freq": freq,
    "fit_a": fit_a, "fit_b": fit_b, "fit_err": fit_err,
    "edge_rel_spread": rel_spread, "edges": edges,
    "covol": covol, "covol_exact": 5 * s5 / 4,
    "dens": dens, "dens_exact": dens_exact,
    "k1norm": mmin, "k1": [float(k1[0]), float(k1[1])],
    "kstar1": [float(kstar1[0]), float(kstar1[1])],
    "kstar1_norm": float(np.linalg.norm(kstar1)),
    "nvec": list(nvec),
}, indent=1))

# ---------- 6. window Fourier transform (repaired) ----------
# Fan-triangulation exact FT: F(k)=sum over fan triangles (0,a,b) of the exact
# analytic triangle integral (E-factors with the (1-i u-e^{-iu})/u^2 small-arg
# branches). Cross-checked against divergence-theorem edge sum and Gauss-Legendre
# quadrature on the same decagon.
def _E(z):
    if abs(z) < 1e-9:
        return 1 - 1j * z / 2 - z * z / 6
    return (cmath.exp(-1j * z) - 1) / (-1j * z)

def tri_ft_exact(p0, p1, p2, k):
    kx, ky = float(k[0]), float(k[1])
    ka = kx * (p1[0] - p0[0]) + ky * (p1[1] - p0[1])
    kb = kx * (p2[0] - p0[0]) + ky * (p2[1] - p0[1])
    det = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])
    ph = cmath.exp(-1j * (kx * p0[0] + ky * p0[1]))
    tiny = 1e-9
    if abs(ka) < tiny and abs(kb) < tiny:
        I = 0.5
    elif abs(kb) < tiny:
        I = (1 - 1j * ka - cmath.exp(-1j * ka)) / (ka * ka)
    elif abs(ka) < tiny:
        I = (1 - 1j * kb - cmath.exp(-1j * kb)) / (kb * kb)
    else:
        I = (cmath.exp(-1j * kb) * _E(ka - kb) - _E(ka)) / (-1j * kb)
    return det * ph * I

def fan_ft(poly, k):
    o = np.zeros(2)
    return sum(tri_ft_exact(o, np.asarray(poly[i], float),
                            np.asarray(poly[(i + 1) % len(poly)], float), k)
               for i in range(len(poly)))

def stokes_ft(poly, k):
    # divergence form: F = sum_e i(n_e.k)/|k|^2 L_e e^{-ik.m_e} sinc(k.e_e/2),
    # n_e outward unit normal (CCW), m_e edge midpoint; F(0)=area branch.
    kx, ky = float(k[0]), float(k[1])
    k2 = kx * kx + ky * ky
    if k2 == 0.0:
        return shoelace(poly) + 0j
    s = 0j
    m = len(poly)
    for i in range(m):
        p = np.asarray(poly[i], float); q = np.asarray(poly[(i + 1) % m], float)
        ex, ey = float(q[0] - p[0]), float(q[1] - p[1])
        mx, my = 0.5 * (p[0] + q[0]), 0.5 * (p[1] + q[1])
        kd = kx * ex + ky * ey
        sinc = (1 - kd * kd / 24) if abs(kd) < 1e-9 else math.sin(kd / 2) / (kd / 2)
        s += 1j * (ey * kx - ex * ky) / k2 * cmath.exp(-1j * (kx * mx + ky * my)) * sinc
    return s

def quad_ft(poly, k, order=40):
    x, w = np.polynomial.legendre.leggauss(order)
    tot = 0j
    for i in range(len(poly)):
        a = np.asarray(poly[i], float); b = np.asarray(poly[(i + 1) % len(poly)], float)
        det = abs(a[0] * b[1] - a[1] * b[0])
        for ii in range(order):
            for jj in range(order):
                u = x[ii]; v = x[jj]
                alpha = (1 + u) / 2; beta = (1 - alpha) * (1 + v) / 2
                px = alpha * a[0] + beta * b[0]; py = alpha * a[1] + beta * b[1]
                tot += w[ii] * w[jj] * cmath.exp(-1j * (k[0] * px + k[1] * py)) * (1 - alpha) / 4 * det
    return tot

o = np.zeros(2)
F0_fan = fan_ft(W, o)
F0_stokes = stokes_ft(W, o)
F0_quad = quad_ft(W, o)
print(json.dumps({"F0_fan": [F0_fan.real, F0_fan.imag], "F0_stokes": [F0_stokes.real, F0_stokes.imag],
                  "F0_quad": [F0_quad.real, F0_quad.imag], "Adec": Adec}))
assert abs(F0_fan - Adec) < 1e-9 and abs(F0_stokes - Adec) < 1e-9 and abs(F0_quad - Adec) < 1e-6

# Bragg evaluation at the INTERNAL coordinate q1 = k1* (|q|~3.223), NOT physical k1.
F_fan = fan_ft(W, kstar1)
F_stokes = stokes_ft(W, kstar1)
F_quad = quad_ft(W, kstar1)
print(json.dumps({"Fq_fan_abs": abs(F_fan), "Fq_stokes_abs": abs(F_stokes), "Fq_quad_abs": abs(F_quad),
                  "Fq_phase_pi": cmath.phase(F_fan) / math.pi}))
assert abs(abs(F_fan) - abs(F_stokes)) < 1e-9 and abs(abs(F_fan) - abs(F_quad)) < 1e-6
amp = dens * F_fan
I1 = abs(amp) ** 2
print(json.dumps({"amp_abs": abs(amp), "I1": I1, "I1_over_dens2": I1 / dens**2}))
rots = []
for j in range(10):
    th = j * math.pi / 5
    R = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
    r = R @ np.asarray(kstar1, float)
    rots.append(abs(fan_ft(W, r)))
print(json.dumps({"tenfold_spread": (max(rots) - min(rots)) / (sum(rots) / len(rots)), "rots": rots}))
print(json.dumps({"WF_vertices": [[float(a), float(b)] for a, b in WF]}))
