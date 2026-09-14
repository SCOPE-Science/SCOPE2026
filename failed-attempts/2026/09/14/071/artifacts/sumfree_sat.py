"""SAT harness for sum-free partitions of F2^n \\ {0} (weak colorings of PG(n-1,2))."""
import time
from pysat.solvers import Glucose3


def points(n):
    return list(range(1, 1 << n))


def all_lines(n):
    m = 1 << n
    L = []
    for x in range(1, m):
        for y in range(x + 1, m):
            z = x ^ y
            if z > y:
                L.append((x, y, z))
    return L


def V(x, c, k):
    # x >= 1 (point id), c in 0..k-1
    return (x - 1) * k + c + 1


def build_cnf(n, k, subset=None, basis_ladder=True):
    """Returns (clauses, nvars, lines_used, pts). subset: iterable of point ids or None."""
    if subset is None:
        P = points(n)
    else:
        P = sorted(subset)
    S = set(P)
    L = [(x, y, z) for (x, y, z) in all_lines(n) if x in S and y in S and z in S]
    clauses = []
    for x in P:
        clauses.append([V(x, c, k) for c in range(k)])  # >= 1 color
        for i in range(k):
            for j in range(i + 1, k):
                clauses.append([-V(x, i, k), -V(x, j, k)])  # <= 1 color
    for (x, y, z) in L:
        for c in range(k):
            clauses.append([-V(x, c, k), -V(y, c, k), -V(z, c, k)])
    if basis_ladder and subset is None:
        # fix e1 -> 0; e_i in colors 0..min(i-1,k-1) (safe under color permutation)
        for i in range(1, n + 1):
            e = 1 << (i - 1)
            allowed = list(range(min(i, k)))
            if len(allowed) == 1:
                clauses.append([V(e, allowed[0], k)])
            else:
                clauses.append([V(e, c, k) for c in allowed])
    elif subset is not None and len(P) > 0:
        clauses.append([V(P[0], 0, k)])  # fix min point to color 0 (safe)
    return clauses, len(P) * k, L, P


def solve_coloring(n, k, subset=None, basis_ladder=True, timeout=None, verbose=False):
    clauses, nvars, L, P = build_cnf(n, k, subset=subset, basis_ladder=basis_ladder)
    t0 = time.time()
    with Glucose3() as s:
        for cl in clauses:
            s.add_clause(cl)
        sat = s.solve()
        model = s.get_model() if sat else None
    dt = time.time() - t0
    if verbose:
        print(f"n={n} k={k} |P|={len(P)} lines={len(L)} clauses={len(clauses)} "
              f"-> {'SAT' if sat else 'UNSAT'} ({dt:.2f}s)", flush=True)
    coloring = None
    if sat:
        truth = {abs(v): v > 0 for v in model}
        coloring = {}
        for x in P:
            for c in range(k):
                if truth.get(V(x, c, k), False):
                    coloring[x] = c
                    break
    return sat, coloring, dt, (len(clauses), len(L))


def check_coloring(n, coloring, k, subset=None):
    """Independent verifier. Returns (ok, msg)."""
    P = points(n) if subset is None else sorted(subset)
    for x in P:
        if x not in coloring or not (0 <= coloring[x] < k):
            return False, f"point {x} uncolored/out of range"
    for (x, y, z) in all_lines(n):
        if subset is not None and not (x in coloring and y in coloring and z in coloring):
            continue
        if coloring[x] == coloring[y] == coloring[z]:
            return False, f"monochromatic line {(x, y, z)} color {coloring[x]}"
    # partition check: every point exactly one color
    if subset is None and set(coloring.keys()) != set(P):
        return False, "not a full partition"
    return True, "ok"
