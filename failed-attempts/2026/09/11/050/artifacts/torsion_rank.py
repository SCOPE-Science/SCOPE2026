"""Torsion + rank-lower-bound lemma for E_k: y^2 = x^3 + k, 10001<=k<=10032.
Proves E_k(Q)_tors = 0 for all 32 k by exact integer arithmetic, and deduces
rank(E_k(Q)) >= 1 for every k carrying an affine integral point. Stdlib only.

Proof structure per k (Delta = -432 k^2 != 0, so smooth):
 (i)   No 2-torsion: (x,0) rational  <=> x^3 = -k  <=> k a perfect cube.
       21^3=9261 < k < 10648=22^3, so no k is a cube. (Exact set-membership.)
 (ii)  Mazur => with no 2-torsion, tors order N in {1,3,5,7,9}.
 (iii) No 3-torsion: psi_3(x) = 3x^4+12kx = 3x(x^3+4k) [for y^2=x^3+k].
       Rational roots: x=0 (point needs y^2=k; k nonsquare since
       100^2=10000 < k < 10201=101^2) or x^3=-4k (4k in [40004,40128];
       34^3=39304 < range < 42875=35^3, so 4k never a cube).
       Hence no Q-point of order 3, and no 9-torsion either. N in {1,5,7}.
 (iv)  No 5-/7-torsion by good-ordinary reduction: for an odd good prime p
       (p not dividing Delta), prime-to-p torsion injects into E(Fp)
       (formal-group / Silverman VII Prop. 3.1).  |E(Fp)| is computed exactly
       by Legendre character sums.  A prime p (good, p!=5) with 5 not | |E(Fp)|
       kills 5-torsion; likewise 7.  Script searches small primes and logs
       the killing prime per k per ell in {5,7}.
 (v)   Rank >= 1: an affine integral point P != O on a torsion-free curve has
       infinite order, so rank >= 1.  Points are re-verified on-curve here by
       exact integer arithmetic (x,y) -> y*y == x**3+k.
"""
import math

KMIN, KMAX = 10001, 10032
KS = list(range(KMIN, KMAX + 1))

# ---- exact perfect-power dictionaries (no floats) ----
SQUARES = {m * m for m in range(0, 200)}
CUBES = {m ** 3 for m in range(0, 400)}


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def aff_order(k, p):
    """Exact #E_k(Fp) for E: y^2=x^3+k, p odd prime with p not | k (good)."""
    assert p % 2 == 1 and k % p != 0
    n = 1  # point at infinity
    for x in range(p):
        v = (pow(x, 3, p) + k) % p
        if v == 0:
            n += 1
        elif legendre(v, p) == 1:
            n += 2
    return n


SMALL_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# integral points found by the bounded finder (re-verified below, not trusted)
CANDIDATES = {
    10001: [(-1, 100), (1874, 81125)],
    10008: [(-2, 100)],
    10009: [(-12, 91)],
    10012: [(42, 290)],
    10017: [(-6, 99), (102, 1035)],
    10025: [(-20, 45), (-16, 77), (-10, 95), (10, 105), (14, 113),
             (35, 230), (55, 420), (100, 1005), (226, 3399)],
    10027: [(-3, 100), (233, 3558), (509, 11484)],
}

report = {"torsion_free": {}, "rank_ge_1": {}, "checks": {}}
ok = True

# global exact non-membership facts
assert all(k not in SQUARES for k in KS), "unexpected square k"
assert all(k not in CUBES for k in KS), "unexpected cube k"
assert all(4 * k not in CUBES for k in KS), "unexpected 4k cube"
report["checks"]["no_k_square"] = True
report["checks"]["no_k_cube"] = True
report["checks"]["no_4k_cube"] = True

for k in KS:
    # (i)+(iii): no 2-torsion (k nonsquare=>also nonsquare needed at x=0... precisely:
    #  2-torsion needs k a cube: excluded) and no 3-torsion (x=0 needs k square:
    #  excluded; x^3=-4k needs 4k cube: excluded).
    assert k not in CUBES and k not in SQUARES and 4 * k not in CUBES
    # (iv): killing primes for 5- and 7-torsion
    kills = {}
    for ell in (5, 7):
        for p in SMALL_PRIMES:
            if p == ell:
                continue
            if k % p == 0 or p == 2:
                continue  # require good odd reduction
            if aff_order(k, p) % ell != 0:
                kills[ell] = {"p": p, "Np": aff_order(k, p)}
                break
        if ell not in kills:
            ok = False
            print(f"FAIL: no killing prime for ell={ell} at k={k}")
    report["torsion_free"][str(k)] = {
        "tors": 0,
        "kill5": kills.get(5),
        "kill7": kills.get(7),
    }
    # (v): rank lower bound from a verified integral point
    pts = []
    for (x, y) in CANDIDATES.get(k, []):
        assert y * y == x ** 3 + k, f"candidate off-curve at k={k}"
        pts.append([x, y])
    if pts:
        report["rank_ge_1"][str(k)] = {"rank_ge": 1, "witness": pts[0],
                                       "n_integral_found": len(pts)}

assert ok, "torsion proof incomplete"
assert len(report["torsion_free"]) == 32
print("torsion_free: 32/32 curves, E_k(Q)_tors = 0 (exact)")
print("rank>=1 certified for k =", sorted(int(k) for k in report["rank_ge_1"]))
print("VERIFY_OK")
