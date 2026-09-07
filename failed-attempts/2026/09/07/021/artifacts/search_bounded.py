"""Bounded exhaustive integral-point search for S.
For each k in S.csv, enumerates ALL (x,y) in Z^2 with y^2=x^3+k and x<=B.
Since k>0, x^3+k<0 for x < -cbrt(k); XMIN=-1000 < -215 safely below, so
loop x in [XMIN,B] is exhaustive for {x<=B}. Exact integer arithmetic only
(math.isqrt). Writes points.json, hall.csv, summary.
B=1000000.
"""
import csv, json, math, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
B = 1_000_000
XMIN = -1000

S = []
with open(os.path.join(HERE, "S.csv")) as f:
    for row in csv.DictReader(f):
        S.append(int(row["k"]))

# sanity: XMIN^3 + max(k) < 0
assert XMIN**3 + max(S) < 0, "XMIN not low enough"
print(f"B={B}, XMIN={XMIN}, ncurves={len(S)}")
print(f"check XMIN^3+max(S)={XMIN**3+max(S)}<0 ok")

t0 = time.time()
data = {}
curves_with = 0
total_xvals = 0
for idx, k in enumerate(S):
    pts = []  # [x, y] with y>=0
    # local bind for speed
    isq = math.isqrt
    for x in range(XMIN, B + 1):
        v = x * x * x + k
        if v < 0:
            continue
        y = isq(v)
        if y * y == v:
            pts.append([x, y])
    data[str(k)] = pts
    if pts:
        curves_with += 1
        total_xvals += len(pts)
    if (idx + 1) % 20 == 0:
        print(f"  {idx+1}/{len(S)} curves, elapsed {time.time()-t0:.1f}s", flush=True)

dt = time.time() - t0
print(f"done in {dt:.1f}s: {curves_with}/{len(S)} curves have points, {total_xvals} x-values (y>=0)")
with open(os.path.join(HERE, "points.json"), "w") as f:
    json.dump({"B": B, "XMIN": XMIN, "points": data}, f)
print("wrote points.json")

# Hall ratios: R=sqrt(|x|)/k for x!=0. Exact maximizer via cross-multiplication
# Compare |x1|*k2^2 vs |x2|*k1^2
best = None  # (k,x,y)
for k in S:
    for x, y in data[str(k)]:
        if x == 0:
            continue
        if best is None:
            best = (k, x, y)
        else:
            k0, x0, y0 = best
            if abs(x) * k0 * k0 > abs(x0) * k * k:
                best = (k, x, y)
print(f"Hall maximizer among found (x!=0): {best}")
if best is not None:
    k, x, y = best
    import decimal
    print(f"  |x|={abs(x)}, k={k}, R^2=|x|/k^2={abs(x)/(k*k):.6e}")

# summary per curve
with open(os.path.join(HERE, "bounded_summary.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["k", "n_xvals_yge0", "n_affine_pts", "has_point", "xs"])
    for k in S:
        pts = data[str(k)]
        n = len(pts)
        aff = sum(1 if y == 0 else 2 for _, y in pts)
        w.writerow([k, n, aff, int(n > 0), ";".join(str(x) for x, _ in pts)])
print("wrote bounded_summary.csv")
