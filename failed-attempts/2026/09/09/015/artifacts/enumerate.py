"""Enumerate stable sets of C5. Stdlib only, exact."""
import itertools, json
n = 5
edges = [(i, (i+1) % 5) for i in range(5)]
verts = []
for mask in range(1 << n):
    S = [i for i in range(n) if mask >> i & 1]
    ok = all(not (u in S and v in S) for u, v in edges)
    if ok:
        verts.append(S)
print("n_verts:", len(verts))
for S in verts:
    print(S)
# alpha
alpha = max(len(S) for S in verts)
print("alpha:", alpha)
with open("verts.json", "w") as f:
    json.dump({"n": n, "edges": edges, "verts": verts, "alpha": alpha}, f)
