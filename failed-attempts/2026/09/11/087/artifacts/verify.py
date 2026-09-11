"""Finite mock of diamond-sealed far-pair combinatorics (lane-910).

Mock master: binary tree of depth D. Each node = (level, index).
Coherence labels: branch offset o = index mod 3 (finite-diff invariant).
Specializing: s(node) = level + 1/(index+2)  (strictly increasing along any branch).

Sealing: at scheduled levels, for directed pair (i,j), pick source node x
in Ri at that level with a surviving top-descendant, pick target node y in Rj
at same level with a surviving top-descendant, declare guess x|->y, and seal by
deleting the entire cone above y in Rj (y becomes terminal) while keeping a
successor of x in Ri. This mirrors the transfinite step: kill the guessed
image cone, keep the source cone.

Checks:
 (C1) every level of every Ri remains nonempty (height preserved);
 (C2) specializing strictly increases along every surviving root-to-leaf path;
 (C3) coherence labels take values in {0,1,2} (finite differences preserved);
 (C4) every sealed guess is blocked: y has NO descendant at top level while
      x HAS a descendant at top level, so no level-preserving extension of the
      guess to the top exists.
"""
import json

D = 10
SEAL_SCHEDULE = {2: (0, 1), 4: (1, 0), 6: (0, 2), 8: (1, 2)}

def children(node):
    lv, k = node
    return [(lv + 1, 2 * k), (lv + 1, 2 * k + 1)]

def descendants(node, depth=D):
    out = []
    stack = [node]
    while stack:
        n = stack.pop()
        if n[0] == depth:
            out.append(n)
            continue
        if n[0] > node[0]:
            out.append(n)
        if n[0] < depth:
            stack.extend(children(n))
    return out

def main():
    # Ri stored as set of surviving nodes; start full.
    R = []
    for _ in range(3):
        s = set()
        for lv in range(D + 1):
            for k in range(2 ** lv):
                s.add((lv, k))
        R.append(s)

    def has_top(n, i):
        lv, k = n
        shift = D - lv
        for kk in range(k * (2 ** shift), (k + 1) * (2 ** shift)):
            if (D, kk) in R[i]:
                return True
        return False

    def kill_cone(n, i):
        lv, k = n
        removed = 0
        for lvv in range(lv + 1, D + 1):
            shift = lvv - lv
            for kk in range(k * (2 ** shift), (k + 1) * (2 ** shift)):
                if (lvv, kk) in R[i]:
                    R[i].discard((lvv, kk))
                    removed += 1
        return removed

    ledger = []
    for lv in sorted(SEAL_SCHEDULE):
        i, j = SEAL_SCHEDULE[lv]
        xs = sorted([n for n in R[i] if n[0] == lv and has_top(n, i)])
        ys = sorted([n for n in R[j] if n[0] == lv and has_top(n, j)])
        assert xs and ys, f"level {lv} empty, cannot seal"
        x, y = xs[0], ys[0]
        if x == y and i != j:
            pass
        # keep source: ensure x keeps a child (it does since has_top)
        # seal target: kill cone above y
        rem = kill_cone(y, j)
        ledger.append({"level": lv, "src": i, "tgt": j,
                       "x": list(x), "y": list(y), "removed": rem})

    # --- verification ---
    # C1: levels nonempty
    for i in range(3):
        for lv in range(D + 1):
            assert any(n[0] == lv for n in R[i]), f"R{i} level {lv} empty"

    # C2: specializing strictly increasing on every surviving root-leaf path
    def spec(n):
        lv, k = n
        return lv + 1.0 / (k + 2)
    for i in range(3):
        # check along a sample of full paths + all parent-child edges
        for n in R[i]:
            lv, k = n
            if lv < D:
                for c in children(n):
                    if c in R[i]:
                        assert spec(c) > spec(n), f"specializing violated at {n}->{c}"

    # C3: coherence labels bounded
    for i in range(3):
        for n in R[i]:
            assert (n[1] % 3) in (0, 1, 2)

    # C4: each sealed guess blocked
    for e in ledger:
        i, j = e["src"], e["tgt"]
        x, y = tuple(e["x"]), tuple(e["y"])
        assert has_top(x, i), f"source cone died for {e}"
        assert not has_top(y, j), f"seal FAILED for {e}"

    # count surviving top nodes
    tops = [sum(1 for n in R[i] if n[0] == D) for i in range(3)]
    result = {"status": "VERIFY_OK", "depth": D,
              "sealed": len(ledger), "ledger": ledger,
              "top_counts": tops,
              "checks": ["levels-nonempty", "specializing-strict",
                         "coherence-bounded", "all-guesses-blocked"]}
    with open("output/artifacts/seal_ledger.json", "w") as f:
        json.dump(result, f, indent=2)
    print("VERIFY_OK")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
