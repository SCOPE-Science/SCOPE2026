"""Bounded recovery probe for the mating-rigidity target.

Target: mate non-renormalizable boundary f_b in Zakeri slice P^{cm}(theta)
with fixed star-like PCF cubic P3; realize as cubic rational with fixed
Siegel disk; uniqueness from (Siegel-tree address + lamination).

This script tests the FINITE-TRUNCATION route: whether the formal mating
admits any finite postcritical model (necessary for classical Thurston
obstruction theory to even be stated). Contents:
  A. Degree / critical-portrait count for the formal mating.
  B. Finiteness of the postcritical set of an explicit PCF cubic
     g(z) = z^3 - 3z (strictly preperiodic critical points).
  C. Zakeri-slice normal form f_c(z) = lam*(z - A z^2 + B z^3),
     critical points at 1 and c; scan of connectedness (both critical
     orbits bounded); deep iteration of the free critical orbit for a
     connected example, testing preperiodicity/stabilization at
     truncations N = 200, 500, 1000, 2000.
  D. Moduli dimension count (printed as text).

Writes output/artifacts/results.json with the computed numbers.
"""
import cmath
import json
import math
import os

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".")
OUT = os.path.join(ART, "results.json")

theta = (math.sqrt(5) - 1) / 2  # golden mean: bounded type
lam = cmath.exp(2j * math.pi * theta)

results = {"theta": theta, "lambda_real": lam.real, "lambda_imag": lam.imag}

# ---- A. portrait count ----
# mating of two degree-3 polynomials -> degree-3 branched cover of S^2;
# critical points: 2 + 2 = 4 = 2*3 - 2 (matches cubic rational).
results["A_portrait"] = {
    "deg_f_b": 3, "deg_P3": 3, "mating_degree": 3,
    "crit_f_b": 2, "crit_P3": 2, "crit_total": 4,
    "crit_cubic_rational": 2 * 3 - 2,
    "count_matches": True,
}

# ---- B. explicit PCF cubic g(z) = z^3 - 3z ----
def g(z):
    return z ** 3 - 3 * z

post = set()
for c in (1.0, -1.0):
    z = c
    orb = [z]
    for _ in range(10):
        z = g(z)
        orb.append(z)
    post.update([round(x.real, 12) for x in orb])
# exact check: 1 -> -2 -> -2 ; -1 -> 2 -> 2
results["B_pcf"] = {
    "map": "z^3 - 3z",
    "critical_points": [1.0, -1.0],
    "orbit_of_1": [1.0, -2.0, -2.0],
    "orbit_of_minus1": [-1.0, 2.0, 2.0],
    "postcritical_set": sorted(post),
    "finite": len(post) == 4,
}


# ---- C. Zakeri slice ----
def make_f(c):
    A = (1 + 1 / c) / 2
    B = 1 / (3 * c)
    def f(z):
        return lam * (z - A * z * z + B * z * z * z)
    return f


def bounded_orbit(f, z0, n=400, R=50.0):
    z = z0
    m = 0.0
    for _ in range(n):
        z = f(z)
        m = max(m, abs(z))
        if abs(z) > R:
            return False, m
    return True, m


# scan c-grid for connectedness-locus candidates (both critical orbits bounded)
grid = [0.5 + 0.2j * k + 0.2 * j for j in range(-3, 4) for k in range(-3, 4)]
connected = []
for c in grid:
    if abs(c) < 1e-9:
        continue
    f = make_f(c)
    b1, _ = bounded_orbit(f, 1.0 + 0j)
    b2, _ = bounded_orbit(f, c)
    if b1 and b2:
        connected.append((c.real, c.imag))
results["C_scan"] = {
    "grid_size": len(grid),
    "connected_candidates": connected,
    "n_connected": len(connected),
}

# deep free-critical-orbit analysis for first connected c (fallback: c=0.5)
c0 = complex(*connected[0]) if connected else complex(0.5, 0.0)
f = make_f(c0)
N = 3000
z = c0
orb = []
escaped = False
for _ in range(N):
    z = f(z)
    orb.append(z)
    if abs(z) > 50:
        escaped = True
        break
results["C_deep"] = {"c": [c0.real, c0.imag], "escaped": escaped, "n_iter": len(orb)}


def n_distinct(pts, tol=1e-6):
    seen = set()
    for p in pts:
        seen.add((round(p.real / tol), round(p.imag / tol)))
    return len(seen)


trunc = {}
for M in (200, 500, 1000, 2000, len(orb)):
    if M <= len(orb):
        trunc[str(M)] = n_distinct(orb[:M])
results["C_deep"]["distinct_vs_truncation"] = trunc
# stabilization? distinct(M) should saturate if postcritical set were finite
vals = [trunc[k] for k in sorted(trunc, key=int)]
results["C_deep"]["stabilized"] = (vals[-1] == vals[-2]) if len(vals) > 1 else False
# tail accumulation: spread of last 300 points (Siegel-boundary clustering)
tail = orb[-300:]
spread = 0.0
for i in range(0, 300, 11):
    for j in range(i + 11, 300, 11):
        d = abs(tail[i] - tail[j])
        spread = max(spread, d)
results["C_deep"]["tail_spread"] = spread
results["C_deep"]["max_modulus"] = max(abs(p) for p in orb)

# ---- D. dimension count (analytic, recorded as text) ----
results["D_dimension_count"] = (
    "dim_C(Rat_3 / PSL2) = (2*3+1) - 3 = 4. Fixing a Siegel fixed point with "
    "prescribed multiplier lam imposes 1 analytic condition -> 3-dimensional "
    "family. Discrete mating data (Siegel-tree address of free co-critical "
    "point + fixed rational lamination of P3) is 0-dimensional. Hence "
    "uniqueness over a discrete fiber inside a positive-dimensional analytic "
    "family requires full combinatorial=>conformal rigidity (no invariant "
    "line fields / no Siegel-disk deformations) for every non-renormalizable "
    "boundary map: an open theorem, not a finite computation."
)

with open(OUT, "w") as fh:
    json.dump(results, fh, indent=2)

print(json.dumps(results, indent=2))
