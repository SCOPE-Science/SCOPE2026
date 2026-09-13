"""Verify Lemma 1 (symmetrized path-LP point in spanning-tree polytope).
Full s-t path LP cut family (both s-t directions + undirected >=2 for
non-separating sets). Checks mass n-1 and all rank constraints on 20 random
metric-closure instances (n=4,5). Also certifies the naive tour-via-path
reduction is unbounded (D/LP=50 on 3-node TI instance).
Repro: python3 output/artifacts/verify_symmetrization.py
"""
import itertools
import pulp


def metric_closure(w):
    n = len(w)
    c = [row[:] for row in w]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if c[i][j] > c[i][k] + c[k][j]:
                    c[i][j] = c[i][k] + c[k][j]
    return c


def solve_path(c, s, t):
    n = len(c)
    prob = pulp.LpProblem("path", pulp.LpMinimize)
    x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", lowBound=0, upBound=1)
         for i in range(n) for j in range(n) if i != j}
    prob += pulp.lpSum(c[i][j] * x[i, j]
                       for i in range(n) for j in range(n) if i != j)
    for v in range(n):
        outv = pulp.lpSum(x[v, j] for j in range(n) if j != v)
        inv = pulp.lpSum(x[i, v] for i in range(n) if i != v)
        if v == s:
            prob += (outv == 1)
            prob += (inv == 0)
        elif v == t:
            prob += (inv == 1)
            prob += (outv == 0)
        else:
            prob += (outv == 1)
            prob += (inv == 1)
    verts = list(range(n))
    for r in range(1, n):
        for S in itertools.combinations(verts, r):
            S = set(S)
            if s in S and t not in S:
                prob += (pulp.lpSum(x[i, j] for i in S for j in range(n)
                                    if j not in S and i != j) >= 1)
            elif t in S and s not in S:
                prob += (pulp.lpSum(x[i, j] for i in range(n) if i not in S
                                    for j in S if i != j) >= 1)
            elif 2 <= len(S) <= n - 2:
                prob += (pulp.lpSum(x[i, j] for i in S for j in range(n)
                                    if j not in S and i != j)
                         + pulp.lpSum(x[i, j] for i in range(n) if i not in S
                                      for j in S if i != j) >= 2)
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    assert pulp.LpStatus[prob.status] == "Optimal"
    xv = {(i, j): x[i, j].value()
          for i in range(n) for j in range(n) if i != j}
    return pulp.value(prob.objective), xv


def check_instance(c, s, t):
    n = len(c)
    lp, xv = solve_path(c, s, t)
    z = {(i, j): xv[i, j] + xv[j, i]
         for i in range(n) for j in range(i + 1, n)}
    mass = sum(z.values())
    worst = 0.0
    worstS = None
    verts = list(range(n))
    for r in range(1, n + 1):
        for S in itertools.combinations(verts, r):
            S = set(S)
            m = sum(z[(min(i, j), max(i, j))] for i in S for j in S if i < j)
            if m - (len(S) - 1) > worst + 1e-6:
                worst = m - (len(S) - 1)
                worstS = S
    return lp, mass, worst, worstS


if __name__ == "__main__":
    import random
    # A: naive tour-via-path reduction unbounded
    c3 = [[0, 1, 2], [101, 0, 1], [100, 101, 0]]
    n = 3
    assert all(c3[i][j] <= c3[i][k] + c3[k][j] + 1e-9
               for i in range(n) for j in range(n) for k in range(n))
    lp3, _, _, _ = check_instance(c3, 0, 2)
    print(f"A: LP_path={lp3} D={c3[2][0]} D/LP={c3[2][0]/lp3} "
          f"-> tour(8x) bound {8*lp3+7*c3[2][0]} vs OPT=2: naive route blocked")
    # B: Lemma 1 on random instances
    random.seed(1)
    nfail = 0
    for nn in (4, 5):
        for trial in range(10):
            w = [[0 if i == j else random.randint(1, 15) for j in range(nn)]
                 for i in range(nn)]
            c = metric_closure(w)
            lp, mass, worst, worstS = check_instance(c, 0, nn - 1)
            status = "OK" if abs(mass - (nn - 1)) < 1e-5 and worst <= 1e-5 else "FAIL"
            if status == "FAIL":
                nfail += 1
            print(f"B: n={nn} t={trial} LP={lp:.2f} mass={mass:.4f} "
                  f"expect={nn-1} max_viol={worst:.6f} {status}")
    print(f"B done, failures={nfail}")
    # C: counting identities
    ok = all(min(3*k, k*(k-1)//2) <= 4*(k-1) or k <= 1 for k in range(1, 50))
    print(f"C: toroidal m<=3n -> arboricity<=4 check passed={ok}")
