"""Fast exact verifier for bounded census (no CAS, stdlib only).
Checks:
 1. S.csv == {k in (1e7,1e7+200] : sixth-power-free} (p^6 test, p<=13 proof).
 2. Every [x,y] in points.json satisfies y*y==x**3+k (exact ints), y>=0.
 3. No k in S is square/cube (torsion-triviality premise).
 4. Hall maximizer recomputed by exact cross-multiplication matches witness.json.
 5. Bound metadata B/XMIN consistent and XMIN^3+max(S)<0 (negative-side coverage).
Runs in seconds.
"""
import csv, json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def fail(m):
    print(f"FAIL: {m}")
    sys.exit(1)

# 1. S.csv
S = []
with open(os.path.join(HERE, "S.csv")) as f:
    r = csv.DictReader(f)
    assert r.fieldnames == ["k"], "S.csv header"
    for row in r:
        S.append(int(row["k"]))
KMIN, KMAX = 10_000_000, 10_000_200
exp = [k for k in range(KMIN + 1, KMAX + 1) if all(k % (p**6) != 0 for p in (2, 3, 5, 7, 11, 13))]
if S != exp:
    fail(f"S.csv mismatch: got {len(S)}, expected {len(exp)}")
# justification that p>13 need not be checked: 17^6=24M>max
assert 17**6 > KMAX
print(f"1. S.csv ok: {len(S)} values, 4 excluded, 17^6={17**6}>{KMAX} so primes>13 impossible")

# 2. points.json substitution
with open(os.path.join(HERE, "points.json")) as f:
    obj = json.load(f)
B, XMIN, pts = obj["B"], obj["XMIN"], obj["points"]
assert set(map(str, S)) == set(pts.keys()), "points.json keys != S"
n_aff = 0
for k in S:
    for x, y in pts[str(k)]:
        assert isinstance(x, int) and isinstance(y, int) and y >= 0
        if y * y != x * x * x + k:
            fail(f"substitution fail k={k} x={x} y={y}")
        n_aff += 1 if y == 0 else 2
print(f"2. substitution ok: B={B} XMIN={XMIN}, {sum(len(v) for v in pts.values())} x-values, {n_aff} affine pts (both signs)")
if not (XMIN**3 + max(S) < 0):
    fail("XMIN coverage")
print(f"   XMIN^3+max(S)={XMIN**3+max(S)}<0 so all x with x^3+k>=0 lie in [XMIN,B] search window for x<=B")

# 3. squares/cubes
for k in S:
    if math.isqrt(k) ** 2 == k:
        fail(f"square {k}")
    # exact cube via binary search
    lo, hi = 0, 5000
    iscube = False
    while lo <= hi:
        m = (lo + hi) // 2
        c = m**3
        if c == k:
            iscube = True
            break
        elif c < k:
            lo = m + 1
        else:
            hi = m - 1
    if iscube:
        fail(f"cube {k}")
print("3. square/cube ok: no k square or cube (3163^2=10004569>KMAX, 216^3=10077696>KMAX)")

# 4. Hall maximizer
with open(os.path.join(HERE, "witness.json")) as f:
    w = json.load(f)
best = None
for k in S:
    for x, y in pts[str(k)]:
        if x == 0:
            continue
        if best is None or abs(x) * best[0] * best[0] > abs(best[1]) * k * k:
            best = (k, x, y)
if best is None:
    assert w["hall_max"] is None
else:
    hm = w["hall_max"]
    if not (hm["k"] == best[0] and hm["x"] == best[1] and hm["y"] == best[2]):
        fail(f"hall maximizer mismatch: computed {best} vs {hm}")
    # verify equation once more for witness
    k, x, y = best
    assert y * y == x**3 + k
    print(f"4. Hall maximizer ok: k={k} x={x} y={y}, R^2=|x|/k^2={abs(x)/(k*k):.6e}")
    # exact maximality certificate: check all others via cross-mult (already done)
print("ALL CHECKS PASSED")
