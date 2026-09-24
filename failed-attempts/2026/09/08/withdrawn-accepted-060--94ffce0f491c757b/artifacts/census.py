"""Vieta-orbit census for S_k: x^2+y^2+z^2 = 3xyz + k, k=0,1,2, max|x|,|y|,|z| <= H.
Exact integer arithmetic throughout. BFS from canonical ordered seeds; components are
Vieta-connected components of the box graph (single-seed floods are pairwise disjoint,
checked by assertion). Writes census.json."""
import json
from collections import deque

H = 10000

def on_surface(k, t):
    x, y, z = t
    return x*x + y*y + z*z == 3*x*y*z + k

def flips(t):
    x, y, z = t
    return [(3*y*z - x, y, z), (x, 3*x*z - y, z), (x, y, 3*x*y - z)]

# Canonical roots, one per box-component (disjointness asserted below):
# k=0: origin; positive tree; 3 two-negative trees (proved no one-neg/three-neg).
# k=1: 3 axis pairs (S_1 finite: 6 points).
# k=2: main tree (contains all nonneg, all one-neg, and (0,-1,-1)-pattern two-neg);
#      plus 2 remaining two-neg trees. ((0,-1,-1) is IN the main tree, not a 4th root.)
ROOTS = {
    0: [(0,0,0), (1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,-1)],
    1: [(0,0,1), (0,1,0), (1,0,0)],
    2: [(0,1,1), (-1,-1,0), (-1,0,-1)],
}

data = {"H": H, "k": {}}
for k, roots in ROOTS.items():
    # pairwise-disjointness of single-seed floods => roots index true box-components
    floods = []
    for s in roots:
        assert on_surface(k, s)
        seen = {s}
        q = deque([s])
        while q:
            t = q.popleft()
            for nb in flips(t):
                if max(abs(c) for c in nb) > H:
                    continue
                assert on_surface(k, nb)
                if nb not in seen:
                    seen.add(nb)
                    q.append(nb)
        floods.append(seen)
    for i in range(len(floods)):
        for j in range(i+1, len(floods)):
            assert not (floods[i] & floods[j]), (k, roots[i], roots[j])
    comp, parent = {}, {}
    for i, fl in enumerate(floods):
        for t in fl:
            comp[t] = i
    # parent pointers from a joint BFS (valid ordered single-flip spanning forest)
    q = deque()
    for s in roots:
        parent[s] = None
        q.append(s)
    while q:
        t = q.popleft()
        for nb in flips(t):
            if max(abs(c) for c in nb) > H or nb not in comp:
                continue
            if nb not in parent:
                parent[nb] = t
                q.append(nb)
    assert set(parent) == set(comp)
    pts = sorted(comp)
    sizes = sorted(sum(1 for t in pts if comp[t] == c) for c in range(len(roots)))
    nonneg = sorted(set(tuple(sorted(t)) for t in pts if all(c >= 0 for c in t)))
    assert all(on_surface(k, t) and max(t) <= H for t in nonneg)
    maxcoord = max(max(t) for t in nonneg)
    depth = {}
    for t in pts:
        d, u = 0, t
        while parent[u] is not None:
            u = parent[u]
            d += 1
        depth[t] = d
    maxdepth = max(depth.values())
    deep0 = sorted(t for t in pts if depth[t] == maxdepth)[0]
    def chain(t):
        p = [t]
        while parent[p[-1]] is not None:
            p.append(parent[p[-1]])
        return p
    data["k"][str(k)] = {
        "count": len(pts),
        "component_sizes": sizes,
        "n_components": len(roots),
        "roots": roots,
        "nonneg_sorted": nonneg,
        "n_nonneg_sorted": len(nonneg),
        "maxcoord": maxcoord,
        "maxcoord_examples": sorted(t for t in nonneg if max(t) == maxcoord),
        "maxdepth": maxdepth,
        "deepest_example": list(deep0),
        "witness_chain": [list(t) for t in chain(deep0)],
        "points": [{"t": list(t), "comp": comp[t],
                    "parent": list(parent[t]) if parent[t] else None} for t in pts],
    }
    print(f"k={k}: total={len(pts)} compsizes={sizes} nonneg_sorted={len(nonneg)} "
          f"maxcoord={maxcoord} maxdepth={maxdepth}")
    print(f"   deepest: {deep0} chain: {chain(deep0)}")

json.dump(data, open("output/artifacts/census.json", "w"))
print("wrote output/artifacts/census.json")
