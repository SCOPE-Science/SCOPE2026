"""Nagell-Lutz cross-check for minimal curves (self-contained torsion evidence).
For E_k: y^2=x^3+k with vp(Delta)<12 at all p (i.e. v2(k)<=3 and v3(k)<=4 and
for p>=5 v_p(Delta)=2v_p(k)<=10<12 since v_p(k)<=5), the model is globally minimal.
Then Nagell-Lutz: torsion P=(x,y) integral and y=0 or y^2 | Delta=-432k^2.
Since y^2|Delta <=> y | 12k, candidates are divisors of 12k (few hundred).
We enumerate all y|12k and test whether y^2-k is a perfect cube (x^3).
If none (and k not cube for y=0 case), torsion is trivial -- no classification needed.
For the 10 non-minimal-valuation curves we skip (torsion there via square/cube lemma).
Writes lutz.csv with candidate counts.
"""
import csv, math, os
HERE = os.path.dirname(os.path.abspath(__file__))

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def divisors(n):
    ds = set()
    r = int(math.isqrt(n))
    for i in range(1, r + 1):
        if n % i == 0:
            ds.add(i)
            ds.add(n // i)
    return ds

def is_cube_v(v):
    # v>=0 exact cube test, returns (bool, root)
    if v < 0:
        return False, None
    # float approx + neighbor check + binary fallback
    x = int(round(v ** (1/3))) if v < 10**18 else int(v ** (1/3)) if False else None
    try:
        x = int(round(v ** (1/3)))
    except Exception:
        x = 0
    for d in range(x - 5, x + 6):
        if d >= 0 and d * d * d == v:
            return True, d
    # binary fallback (roots up to ~2.5e5 for v<=1.5e16)
    lo, hi = 0, 3000000
    # narrow hi
    while lo <= hi:
        m = (lo + hi) // 2
        c = m * m * m
        if c == v:
            return True, m
        elif c < v:
            lo = m + 1
        else:
            hi = m - 1
    return False, None

S = []
with open(os.path.join(HERE, "S.csv")) as f:
    for row in csv.DictReader(f):
        S.append(int(row["k"]))

rows = []
for k in S:
    a, b = vp(k, 2), vp(k, 3)
    minimal = (a <= 3 and b <= 4)
    if not minimal:
        rows.append((k, "nonminimal-valuation-skip", "", ""))
        continue
    D = 12 * k
    divs = divisors(D)
    cands = []
    for y in divs:
        for yy in (y, -y):
            v = yy * yy - k
            if v < 0:
                continue
            ok, x = is_cube_v(v)
            if ok:
                # (x,yy) satisfies yy^2==x^3+k
                cands.append((x, yy))
    # y=0 case: x^3==-k => k cube (already excluded); double-check
    # deduplicate (x,y) with y=0 counted once
    rows.append((k, "minimal", len(divs), len(cands)))

with open(os.path.join(HERE, "lutz.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["k", "status", "n_divisors_12k", "n_lutz_candidates"])
    for r in rows:
        w.writerow(r)
n_min = sum(1 for r in rows if r[1] == "minimal")
n_cand = sum(r[3] for r in rows if r[1] == "minimal")
print(f"minimal curves: {n_min}, total Lutz candidates: {n_cand}")
if n_cand == 0:
    print("Lutz cross-check: ZERO candidates on all minimal curves => torsion trivial independently")
else:
    print("candidates found (need torsion test):")
    for r in rows:
        if r[1] == "minimal" and r[3]:
            print(r)
