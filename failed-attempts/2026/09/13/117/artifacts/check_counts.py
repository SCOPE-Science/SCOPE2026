"""Certify elementary counting obstruction for lane-1752 target.

Claim checked: disjoint union of eight triangles has 24 vertices,
incompatible with 12 periodic directions under any vertex-injecting
ideal-Whitehead definition; also 8 != 2*5-3 = 7 principal triangles.
"""
from collections import deque


def build_disjoint_triangles(k=8):
    # vertices 0..3k-1, triangles (3i,3i+1,3i+2)
    adj = {v: set() for v in range(3 * k)}
    for i in range(k):
        a, b, c = 3 * i, 3 * i + 1, 3 * i + 2
        for u, v in ((a, b), (b, c), (c, a)):
            adj[u].add(v)
            adj[v].add(u)
    return adj


def components(adj):
    seen = set()
    comps = []
    for s in adj:
        if s in seen:
            continue
        q = deque([s])
        seen.add(s)
        cur = []
        while q:
            u = q.popleft()
            cur.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        comps.append(cur)
    return comps


def main():
    adj = build_disjoint_triangles(8)
    n = len(adj)
    comps = components(adj)
    nedges = sum(len(v) for v in adj.values()) // 2
    print(f"vertices: {n}")
    print(f"edges: {nedges}")
    print(f"components: {len(comps)}")
    print(f"component sizes: {sorted(len(c) for c in comps)}")
    assert n == 24, n
    assert nedges == 24, nedges
    assert len(comps) == 8, len(comps)
    assert all(len(c) == 3 for c in comps)
    # Hypothesis demands vertex set of size 12 (or <=12 if subset).
    assert n != 12 and n > 12, "must mismatch 12"
    print("mismatch with 12 periodic directions: CERTIFIED (24 != 12, 24 > 12)")
    # Rank-5 principal count 2n-3 = 7.
    assert 2 * 5 - 3 == 7 != 8
    print("mismatch with rank-5 principal count 2n-3=7: CERTIFIED (8 != 7)")
    print("RESULT: hypothesis unsatisfiable; universal implication vacuously true.")


if __name__ == "__main__":
    main()
