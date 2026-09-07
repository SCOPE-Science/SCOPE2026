"""Build witness.json, heights.csv, hall.csv from points.json.
- witness.json: bounded-census metadata + Hall maximizer (exact) + largest-|x| point + counts.
- heights.csv: per found x-value (y>=0): k,x,y, naive heights log(max(|x|,1)), log(max(|y|,1)), Hall R^2=|x|/k^2 and R (float, for convenience; exact comparison via integers in verify.py).
- hall.csv: ranking by Hall ratio via exact cross-multiplication (no float ordering).
Floats are CONVENIENCE ONLY; exact claims use integers.
"""
import csv, json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "points.json")) as f:
    obj = json.load(f)
B, XMIN, pts = obj["B"], obj["XMIN"], obj["points"]
S = sorted(int(k) for k in pts.keys())

rows = []  # (k,x,y)
for k in S:
    for x, y in pts[str(k)]:
        rows.append((k, x, y))

# exact Hall ranking: R1>R2 <=> |x1|*k2^2 > |x2|*k1^2 (x!=0)
nonzero = [r for r in rows if r[0] != 0 and r[1] != 0]
nonzero_sorted = sorted(nonzero, key=lambda r: abs(r[1]) / (r[0] * r[0]))  # float sort for display
# exact max via cross-mult
best = None
for r in nonzero:
    if best is None or abs(r[1]) * best[0] * best[0] > abs(best[1]) * r[0] * r[0]:
        best = r
# largest |x|
bigx = max(rows, key=lambda r: abs(r[1])) if rows else None

with open(os.path.join(HERE, "heights.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["k", "x", "y", "naive_log_max_x", "naive_log_max_y", "hall_R2", "hall_R"])
    for k, x, y in sorted(rows):
        lx = math.log(max(abs(x), 1))
        ly = math.log(max(abs(y), 1))
        r2 = abs(x) / (k * k) if x != 0 else 0.0
        w.writerow([k, x, y, f"{lx:.12f}", f"{ly:.12f}", f"{r2:.12e}", f"{math.sqrt(r2):.12e}" if r2 else "0"])

with open(os.path.join(HERE, "hall.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["rank", "k", "x", "y", "hall_R2", "hall_R"])
    # order by exact comparison: sort with key as Fraction |x|/k^2 exactly via sort key tuple? use float then verify adjacent via cross-mult
    ordered = sorted(nonzero, key=lambda r: (abs(r[1]) / (r[0] * r[0])), reverse=True)
    # verify ordering is exact-consistent (no float ties misordered): check adjacent cross-mult
    for i in range(len(ordered) - 1):
        a, b = ordered[i], ordered[i + 1]
        # allow equal or a>=b; if float order contradicts exact, fix by exact sort (bubble? but n=29 tiny, do exact insertion)
        pass
    # exact sort via pairwise (n small): simple selection
    rem = nonzero[:]
    ordered_exact = []
    while rem:
        m = rem[0]
        for r in rem[1:]:
            if abs(r[1]) * m[0] * m[0] > abs(m[1]) * r[0] * r[0]:
                m = r
        ordered_exact.append(m)
        rem.remove(m)
    for i, (k, x, y) in enumerate(ordered_exact, 1):
        r2 = abs(x) / (k * k)
        w.writerow([i, k, x, y, f"{r2:.12e}", f"{math.sqrt(r2):.12e}"])

wit = {
    "B": B,
    "XMIN": XMIN,
    "n_curves": len(S),
    "n_curves_with_point": sum(1 for k in S if pts[str(k)]),
    "n_xvals_yge0": len(rows),
    "n_affine_pts_both_signs": sum(1 if y == 0 else 2 for _, _, y in rows),
    "hall_max": {"k": best[0], "x": best[1], "y": best[2]} if best else None,
    "largest_abs_x": {"k": bigx[0], "x": bigx[1], "y": bigx[2]} if bigx else None,
    "normalizations": "naive heights are natural-log; Hall R=sqrt(|x|)/|k| for x!=0; floats convenience-only, maximality by exact integer cross-multiplication",
    "completeness": f"exhaustive for x<=B with XMIN^3+max(S)<0; any unlisted integral point has x>B",
}
with open(os.path.join(HERE, "witness.json"), "w") as f:
    json.dump(wit, f, indent=2)
print(json.dumps(wit, indent=2))
print("wrote heights.csv, hall.csv, witness.json")
