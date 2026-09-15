"""Finite-n Delsarte-MacWilliams primal duality barrier (TARGET horn-b localization).
Duality fact: primal max of A_w over the full MacWilliams polytope
  {B_0=1, B_j=0 (1<=j<d'), sum B = 2^{n-k}, all A_i = (K B)_i/2^{n-k} >= 0}
lower-bounds EVERY Krawtchouk (LP) certificate value valid on that polytope,
since a certificate is a linear consequence giving an upper bound on A_w.
The polytope encodes ALL linear MacWilliams data (vanishing + nonnegativity +
exact size), so the barrier covers the full-MacWilliams linear case.
A primal-feasible super-binomial max at (n,k,d',w) proves no such certificate
certifies the binomial bound there. Parameters use real codes => nonempty."""
import math, csv
from math import comb
import pulp

def kraw(w, x, n):
    return sum((1 if j % 2 == 0 else -1)*comb(x, j)*comb(n-x, w-j)
               for j in range(0, min(w, x)+1))

def lp_max_Aw(n, k, dpn, w):
    Mp = 2**(n-k)
    K = [[kraw(i, j, n) for j in range(n+1)] for i in range(n+1)]
    prob = pulp.LpProblem("primal", pulp.LpMaximize)
    B = [pulp.LpVariable(f"B{j}", lowBound=0) for j in range(n+1)]
    prob += B[0] == 1
    for j in range(1, dpn): prob += B[j] == 0
    prob += pulp.lpSum(B) == Mp
    for i in range(n+1):
        prob += pulp.lpSum(K[i][j]*B[j] for j in range(n+1)) >= 0
    prob += pulp.lpSum(K[w][j]*B[j] for j in range(n+1))/Mp
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    st = pulp.LpStatus[prob.status]
    assert st == "Optimal", f"LP status {st} n={n} k={k} dpn={dpn} w={w}"
    return pulp.value(prob.objective)

def xi1(dp):
    return 0.5*(1-math.sqrt(dp*(2-dp)))

cases = [
    (15, 7, 4, [2], [3, 4], "dual [15,8,4] exists (BCH dual)"),
    (31, 15, 7, [4, 5], [7, 8], "dual [31,16,7] BCH exists"),
]
rows = []
for (n, k, dpn, wbelow, wabove, note) in cases:
    M = 2**k; x1 = xi1(dpn/n)
    print(f"--- n={n} k={k} d'={dpn} xi1={x1:.4f} thr_w={x1*n:.2f} [{note}]")
    for w in wbelow + wabove:
        opt = lp_max_Aw(n, k, dpn, w)
        binom = M*comb(n, w)/2**n
        side = "BELOW" if w/n < x1 else "ABOVE"
        print(f"w={w} w/n={w/n:.4f} {side}: LPmax={opt:.6g} binom={binom:.6g} ratio={opt/binom:.4f}")
        rows.append([n, k, dpn, w, f"{w/n:.6f}", side,
                     f"{opt:.10g}", f"{binom:.10g}", f"{opt/binom:.6f}"])
with open("output/artifacts/lp_primal.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["n","k","dpn","w","w/n","side_vs_xi1","LPmax","binomial","ratio"])
    w.writerows(rows)

trows = []
for dp in [0.05, 0.1, 0.15, 0.2, 0.2258, 0.2667, 0.3]:
    x = xi1(dp)
    slope = -(2-2*dp)/(4*math.sqrt(dp*(2-dp)))
    trows.append([dp, f"{x:.6f}", f"{slope:.6f}"])
with open("output/artifacts/xi1_curve.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["dp","xi1","dxi1_ddp"]); w.writerows(trows)
print("WROTE lp_primal.csv + xi1_curve.csv")
