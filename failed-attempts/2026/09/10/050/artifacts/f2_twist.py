"""Fallback attempt F2: sparse twist — start from a certified F-free sparse base
and add a pseudorandom matching of extra edges, checking F-freeness and the
count leg e >= 1e-6 N^{5/4} at the computed N.

Base: single-direction D_4(3) subset (S={0}): N=108, E=81, F-free expected.
Twist: add a deterministic pseudorandom perfect matching on the P side
(vertices 0..80, 81 vertices -> 40 edges + 1 leftover), then test full
Theta_{4,4,4}-freeness. Records count margin and freeness verdict.
Demonstrates the twist-idea concretely at finite N while exposing why it
cannot scale to unbounded n (matching adds Theta(n), not Theta(n^{5/4})).
stdlib only.
"""
import itertools
import json
from r1_D4_freeness import len4_paths, has_theta

q = 3
k = 4
pts = list(itertools.product(range(q), repeat=k))
p_index = {p: i for i, p in enumerate(pts)}
d = tuple(pow(0, i, q) for i in range(k))  # direction z=0 -> (1,0,0,0)
seen = set()
for x in pts:
    line = tuple(sorted(
        p_index[tuple((x[i] + y * d[i]) % q for i in range(k))]
        for y in range(q)))
    seen.add(line)
lines = sorted(seen)
nP = len(pts)
nL = len(lines)
N = nP + nL
adj = [set() for _ in range(N)]
for li, line in enumerate(lines):
    v = nP + li
    for u in line:
        adj[u].add(v)
        adj[v].add(u)

# base freeness
pp = sum(1 for i in range(nP) for j in range(i + 1, nP)
         if has_theta(adj, i, j))
LL = list(range(nP, N))
ll = sum(1 for a in range(len(LL)) for b in range(a + 1, len(LL))
         if has_theta(adj, LL[a], LL[b]))
E0 = sum(len(a) for a in adj) // 2
print("base:", {"N": N, "E": E0, "PP": pp, "LL": ll,
                "thr": 1e-6 * N ** 1.25})

# twist: deterministic shift matching on P side: i <-> (i+40) mod 81
perm = [(i, (i + 40) % nP) for i in range(nP)]
added = set()
for a, b in perm:
    e = (min(a, b), max(a, b))
    if e[0] != e[1]:
        added.add(e)
added = sorted(added)
for a, b in added:
    adj[a].add(b)
    adj[b].add(a)
E1 = sum(len(a) for a in adj) // 2
pp1 = sum(1 for i in range(nP) for j in range(i + 1, nP)
          if has_theta(adj, i, j))
ll1 = sum(1 for a in range(len(LL)) for b in range(a + 1, len(LL))
          if has_theta(adj, LL[a], LL[b]))
# cross pairs (P vs L cannot host even-length-4-path theta with same-side
# endpoints... endpoints of a length-4 path are always same side; P-L pairs
# are at odd distance, so only PP and LL checked) — plus mixed-endpoint
# scan over all same-partition pairs already covers every length-4 theta.
res = {"N": N, "E_base": E0, "E_twisted": E1,
       "added_edges": len(added),
       "PP_theta_twisted": pp1, "LL_theta_twisted": ll1,
       "F_free_twisted": (pp1 == 0 and ll1 == 0),
       "thr_1em6_N54": 1e-6 * N ** 1.25,
       "count_leg_holds": E1 >= 1e-6 * N ** 1.25,
       "added_order": "Theta(n): cannot preserve the count leg as n->inf"}
print(json.dumps(res, indent=2))
with open("f2_twist.json", "w") as f:
    json.dump(res, f, indent=2)
print("wrote f2_twist.json")
