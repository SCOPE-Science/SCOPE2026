"""Fallback scale audit (stdlib only): unknown count for the EXACT fallback system.
Uses Hou et al. Sec 4.5 degree formula deg K^_{j,k}=(m-2k)(d-1)-m+j+k-t with
deg_Y<d, for (m,t)=(12,2), d=16, k=2 strata (j+3k<=m); k=3 invariant ansatz has
~2x the jet monomials (74 vs 35 coefficient functions), so k=2 count is a LOWER bound.
Monomials counted: x^a y^b z^c with a+b+c<=D, b<=15 (exact combinatorics)."""
def nmono(D, ymax=15):
    n = 0
    for b in range(min(ymax, D) + 1):
        r = D - b
        n += (r + 1) * (r + 2) // 2
    return n
d, m, t = 16, 12, 2
tot = 0
detail = []
k = 0
while 3 * k <= m:
    for j in range(m - 3 * k + 1):
        D = (m - 2 * k) * (d - 1) - m + j + k - t
        n = nmono(D)
        detail.append((j, k, D, n))
        tot += n
    k += 1
print(f"k=2-style coefficient functions: {len(detail)}")
for j, k, D, n in detail:
    print(f"  (j,k)=({j},{k}): deg<={D} unknowns={n}")
print(f"TOTAL unknowns (k=2 lower bound): {tot}")
print("k=3 invariant ansatz: 74 jet monomials vs 35 here -> estimated unknowns ~2x, i.e. ~15M.")
print("Equations: z-divisibility (4.31) yields several-x unknowns; T-system (4.32) similar size.")
print("Hou et al. largest Maple system: ~600k unknowns. Fallback needs ~10-30x that + exact F_251 rank.")
print("VERDICT: exact fallback matrix not assemblable/solvable in bounded in-hour stdlib session.")
