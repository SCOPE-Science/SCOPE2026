"""Torsion triviality check for S: no k is a square or cube.
For E_k: y^2=x^3+k (k>0 sixth-power-free), nontrivial torsion => k square (Z/3) or k cube (Z/2).
Since interval contains no squares/cubes, all torsions trivial.
Exact integer checks (isqrt + integer cbrt via binary search)."""
import csv, math, os
HERE = os.path.dirname(os.path.abspath(__file__))

def is_square(n):
    r = math.isqrt(n)
    return r * r == n

def icbrt(n):
    # exact integer cbrt test for n>0 via binary search
    lo, hi = 0, 5000
    while lo <= hi:
        mid = (lo + hi) // 2
        c = mid * mid * mid
        if c == n:
            return True, mid
        elif c < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False, None

S = []
with open(os.path.join(HERE, "S.csv")) as f:
    r = csv.DictReader(f)
    for row in r:
        S.append(int(row["k"]))

# interval-level: sqrt/cbrt boundaries
print(f"3162^2={3162**2}, 3163^2={3163**2}")
print(f"215^3={215**3}, 216^3={216**3}")
sq = [k for k in S if is_square(k)]
cb = [k for k in S if icbrt(k)[0]]
print(f"squares in S: {sq}")
print(f"cubes in S: {cb}")
assert sq == [] and cb == [], "unexpected square/cube!"
# per-k logs
with open(os.path.join(HERE, "torsion.csv"), "w", newline="") as f:
    import csv as _csv
    w = _csv.writer(f)
    w.writerow(["k", "is_square", "is_cube", "torsion_claim"])
    for k in S:
        w.writerow([k, False, False, "trivial"])
print("wrote torsion.csv: all 196 trivial (conditional on classification lemma, see DRAFT)")
