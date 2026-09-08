"""Verifier for lane-170 artifacts (stdlib only).
Checks: witnesses.json (edge counts, C4-freeness via pair common-neighbourhood),
elimination.json (pair-counting consistency, Lemma-N soundness spot checks,
max-degree range, ex-table exactness range).
"""
import json
import os
from math import comb

_HERE = os.path.dirname(os.path.abspath(__file__))

def check_witnesses(path=None):
    path = path or os.path.join(_HERE, "witnesses.json")
    with open(path) as f:
        out = json.load(f)
    # recorded McKay lower bounds (baseline to beat; we document we are below)
    LB = {"41": 132, "42": 137, "43": 142, "44": 148,
          "45": 154, "46": 157, "47": 163, "48": 168}
    for k, g in out.items():
        n, m, el = g["n"], g["edges"], g["edgelist"]
        assert str(n) == str(k), (k, n)
        assert len(el) == m, (n, len(el), m)
        adj = [set() for _ in range(n)]
        for u, v in el:
            assert 0 <= u < v < n, (u, v)
            assert v not in adj[u]
            adj[u].add(v); adj[v].add(u)
        for u in range(n):
            for v in range(u + 1, n):
                if len(adj[u] & adj[v]) > 1:
                    raise AssertionError(f"C4 at n={n} pair {(u, v)}")
        print(f"witness n={n}: edges={m} C4-free OK "
              f"(recorded lower bound {LB[str(n)]}, delta {m - LB[str(n)]})")
    print("witnesses: ALL OK")

EX = {0: 0, 1: 0, 2: 1, 3: 3, 4: 4, 5: 6, 6: 7, 7: 9,
      8: 11, 9: 13, 10: 16, 11: 18, 12: 21, 13: 24, 14: 27, 15: 30,
      16: 33, 17: 36, 18: 39, 19: 42, 20: 46}
# NOTE: rows through a(20)=42 are exact in OEIS A006855 (b-file to n=40);
# the run asserts max degree <= 20 so EX is applied inside the exact range.

def lemma_n_violated(seq, n):
    """True iff seq violates Lemma N (sound elimination criterion)."""
    desc = sorted(seq, reverse=True)
    for i, dv in enumerate(desc):
        rest = desc[:i] + desc[i + 1:]
        if sum(rest[:dv]) > (n - 1) + dv + EX.get(dv, 999):
            return True
    return False

def check_elimination(path=None):
    path = path or os.path.join(_HERE, "elimination.json")
    with open(path) as f:
        table = json.load(f)
    for k, row in table.items():
        n, m = row["n"], row["top_m"]
        assert str(n) == str(k)
        C = comb(n, 2)
        surv = row["survivor_list"]
        assert row["nb_survivors"] == len(surv)
        assert row["eliminated"] == row["pair_seqs"] - row["nb_survivors"]
        assert row["pair_seqs"] > row["nb_survivors"] >= 0
        for s in surv:
            assert len(s) == n and sum(s) == 2 * m, (n, m)
            assert all(0 <= d < n for d in s)
            assert max(s) <= 20, (n, max(s))  # ex-table range guard
            assert sum(d * (d - 1) // 2 for d in s) <= C, (n, m)
            assert not lemma_n_violated(s, n), (n, m, s)
        print(f"elimination n={n} m={m}: pair_seqs={row['pair_seqs']} "
              f"survivors={len(surv)} eliminated={row['eliminated']} OK")
    print("elimination: ALL OK")

if __name__ == "__main__":
    check_witnesses()
    check_elimination()
    print("VERIFY PASS")
