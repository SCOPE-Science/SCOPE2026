"""Independent verification: re-solve primal LPs, retrieve B*, check all residuals."""
from math import comb
import pulp

def kraw(w, x, n):
    return sum((1 if j % 2 == 0 else -1)*comb(x, j)*comb(n-x, w-j)
               for j in range(0, min(w, x)+1))

def verify(n, k, dpn, w):
    Mp = 2**(n-k); M = 2**k
    K = [[kraw(i, j, n) for j in range(n+1)] for i in range(n+1)]
    prob = pulp.LpProblem("p", pulp.LpMaximize)
    B = [pulp.LpVariable(f"B{j}", lowBound=0) for j in range(n+1)]
    prob += B[0] == 1
    for j in range(1, dpn): prob += B[j] == 0
    prob += pulp.lpSum(B) == Mp
    for i in range(n+1):
        prob += pulp.lpSum(K[i][j]*B[j] for j in range(n+1)) >= 0
    prob += pulp.lpSum(K[w][j]*B[j] for j in range(n+1))/Mp
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    assert pulp.LpStatus[prob.status] == "Optimal"
    bv = [v.value() for v in B]
    A = [sum(K[i][j]*bv[j] for j in range(n+1))/Mp for i in range(n+1)]
    binom = M*comb(n, w)/2**n
    checks = {
        "B0-1": abs(bv[0]-1),
        "max|B[1..d'-1]|": max(abs(bv[j]) for j in range(1, dpn)),
        "sumB-Mp residual": abs(sum(bv)-Mp),
        "minB": min(bv),
        "minA": min(A),
        "Aw": A[w],
        "binom": binom,
        "ratio": A[w]/binom,
    }
    return checks

lines = []
for (n,k,dpn,w) in [(15,7,4,2),(31,15,7,4),(31,15,7,5)]:
    c = verify(n,k,dpn,w)
    lines.append(f"n={n} k={k} d'={dpn} w={w}: " +
                 ", ".join(f"{kk}={vv:.6g}" for kk,vv in c.items()))
    print(lines[-1])
open("output/artifacts/lp_verify.txt","w").write("\n".join(lines)+"\n")
