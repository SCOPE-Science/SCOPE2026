"""Independent verifier for the 0.007 Guy-Smith exclusion bound.

Checks (stdlib only):
 1. Recomputes G(0..200) from the octal rule with an independent loop structure
    (reachable set built via explicit option list incl. unsplit move), and
    compares against grundy_007_N200.csv entry-by-entry.
 2. Replays every witness row (q,p,n,g_n,g_np): asserts q<=n<=200-p,
    G[n]==g_n, G[n+p]==g_np, g_n!=g_np.
 3. Asserts coverage: every (q,p) in 0<=q<=100, 1<=p<=100 appears exactly once
    (no survivors, no duplicates, no missing pairs).
 4. Asserts the tight-corner case q=p=100 has witness n=100 (single test index).
 5. Prints SHA256 of both CSVs.

Exit 0 with VERIFY_OK iff all checks pass.
"""
import csv
import hashlib
import os
import sys

N, QMAX, PMAX = 200, 100, 100
BASE = os.path.dirname(os.path.abspath(__file__))
G_CSV = os.path.join(BASE, "grundy_007_N200.csv")
W_CSV = os.path.join(BASE, "witnesses_Q100_P100.csv")

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def recompute():
    # Independent structure: options(n) = [n-3] + [(i, n-3-i)]
    G = [0] * (N + 1)
    for n in range(3, N + 1):
        if n == 3:
            reach = {G[0]}
        else:
            reach = {G[n - 3]}
            m = n - 3
            for i in range(m + 1):
                reach.add(G[i] ^ G[m - i])
        g = 0
        while g in reach:
            g += 1
        G[n] = g
    return G

def main():
    G = recompute()
    # 1. table match
    with open(G_CSV) as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == N + 1, f"table rows {len(rows)}"
    for r in rows:
        n, g = int(r["n"]), int(r["g"])
        assert 0 <= n <= N and G[n] == g, f"mismatch at n={n}: csv={g} recompute={G[n]}"
    # 2. witness replay
    with open(W_CSV) as f:
        wrows = list(csv.DictReader(f))
    seen = set()
    for r in wrows:
        q, p, n = int(r["q"]), int(r["p"]), int(r["n"])
        a, b = int(r["g_n"]), int(r["g_np"])
        assert 0 <= q <= QMAX and 1 <= p <= PMAX, f"pair out of box {(q,p)}"
        assert q <= n <= N - p, f"index out of range {(q,p,n)}"
        assert G[n] == a and G[n + p] == b, f"value mismatch {(q,p,n)}"
        assert a != b, f"non-failing witness {(q,p,n)}"
        assert (q, p) not in seen, f"duplicate {(q,p)}"
        seen.add((q, p))
    # 3. full coverage
    expected = {(q, p) for q in range(QMAX + 1) for p in range(1, PMAX + 1)}
    assert seen == expected, f"missing={len(expected-seen)} extra={len(seen-expected)}"
    # 4. tight corner
    corner = [r for r in wrows if int(r["q"]) == 100 and int(r["p"]) == 100]
    assert len(corner) == 1 and int(corner[0]["n"]) == 100, "corner (100,100) must fail at n=100"
    assert G[100] != G[200], "corner values must differ"
    print(f"table OK: 201 rows, max G = {max(G)}")
    print(f"witnesses OK: {len(wrows)} rows covering all {(QMAX+1)*PMAX} pairs, 0 survivors")
    print(f"corner (100,100): n=100, G(100)={G[100]}, G(200)={G[200]}")
    print(f"sha256 grundy csv:    {sha256(G_CSV)}")
    print(f"sha256 witnesses csv: {sha256(W_CSV)}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
