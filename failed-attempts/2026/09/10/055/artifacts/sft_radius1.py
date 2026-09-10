"""Route C probe: radius-1 factor (clopen/SFT) 3-coloring search.

Window W = B_1 = {e,a,a^-1,b,b^-1,c} (6 vertices, 64 patterns).
A factor rule F:{0,1}^W -> {0,1,2} gives a clopen (hence Borel and
measurable) proper 3-coloring of X=Free(2^Gamma) iff for every s in S
and every pair (P,P') of W-patterns arising as (z|_W,(s.z)|_W) for a
free z, F(P)!=F(P'). Since every finite pattern extends to a free
global configuration (diagonalize against each non-identity group
element on fresh vertices; Gamma infinite), the realizable pairs are
exactly those from all assignments on W union sW. Build the 64-vertex
constraint graph and decide 3-colorability by certified backtracking.

If 3-colorable -> explicit Borel 3-coloring -> target's chi_B>=4 FALSE.
If not -> no radius-1 factor 3-coloring (consistent with gap).
Stdlib only. Writes sft_radius1.json.
"""
import json

# ---- group arithmetic (same normal form as cayley_cell.py) ----
def mul_A(T, dm, dn):
    L = list(T)
    L[-1] = (L[-1][0] + dm, L[-1][1] + dn)
    return tuple(L)

def reduce_blocks(L):
    L = list(L)
    while len(L) >= 3:
        hit = -1
        for i in range(1, len(L) - 1):
            if L[i] == (0, 0):
                hit = i
                break
        if hit < 0:
            break
        L = (L[:hit - 1]
             + [(L[hit - 1][0] + L[hit + 1][0],
                 L[hit - 1][1] + L[hit + 1][1])]
             + L[hit + 2:])
    return tuple(L)

def mul_c(T):
    return reduce_blocks(list(T) + [(0, 0)])

E = ((0, 0),)
GENS = {'a': ('A', 1, 0), 'ai': ('A', -1, 0), 'b': ('A', 0, 1),
        'bi': ('A', 0, -1), 'c': ('C',)}
SYMS = ['a', 'ai', 'b', 'bi', 'c']

def apply(T, g):
    s = GENS[g]
    if s[0] == 'A':
        return mul_A(T, s[1], s[2])
    return mul_c(T)

# balls
from collections import deque
dist = {E: 0}
q = deque([E])
while q:
    g = q.popleft()
    if dist[g] >= 2:
        continue
    for s in SYMS:
        h = apply(g, s)
        if h not in dist:
            dist[h] = dist[g] + 1
            q.append(h)
B1 = sorted(g for g, d in dist.items() if d <= 1)
B2 = sorted(dist)
assert len(B1) == 6 and len(B2) == 22, (len(B1), len(B2))
bidx = {g: i for i, g in enumerate(B2)}
W = B1  # window, ordered
wpos = [bidx[w] for w in W]

# constraint graph on 64 patterns
adj = [set() for _ in range(64)]
loops = []
n_pairs = 0
for s in SYMS:
    sW = [apply(w, s) for w in W]
    U = sorted(set(W) | set(sW), key=lambda g: bidx[g])
    upos = [bidx[u] for u in U]
    # positions within U of W-pattern bits and sW-pattern bits
    uidx = {u: k for k, u in enumerate(U)}
    w_at = [uidx[w] for w in W]
    s_at = [uidx[w] for w in sW]
    for r in range(1 << len(U)):
        P = 0
        for j, k in enumerate(w_at):
            if (r >> k) & 1:
                P |= (1 << j)
        Pp = 0
        for j, k in enumerate(s_at):
            if (r >> k) & 1:
                Pp |= (1 << j)
        n_pairs += 1
        if P == Pp:
            if P not in loops:
                loops.append(P)
        else:
            adj[P].add(Pp)
            adj[Pp].add(P)

nedges = sum(len(a) for a in adj) // 2
degs = sorted((len(a) for a in adj), reverse=True)

result = {'n_vertices': 64, 'n_edges': nedges,
          'n_pairs_enumerated': n_pairs,
          'max_degree': degs[0] if degs else 0,
          'degree_seq': degs, 'n_loops': len(loops), 'loops': loops}

F = None
if loops:
    result['factor3_exists'] = False
    result['reason'] = ('constraint graph has %d loop(s): those W-patterns '
                        'are forced unequal to themselves' % len(loops))
else:
    # DSATUR branch-and-bound 3-colorability
    order = sorted(range(64), key=lambda v: -len(adj[v]))
    color = [-1] * 64
    nodes_visited = [0]
    CAP = 4000000

    import sys
    sys.setrecursionlimit(10000)

    # order dynamically: pick uncolored vertex with most colored neighbours
    def solve(ncolored):
        nodes_visited[0] += 1
        if nodes_visited[0] > CAP:
            return None  # timeout: unknown
        if ncolored == 64:
            return True
        # select
        best, best_sat = -1, -1
        for v in range(64):
            if color[v] < 0:
                sat = len({color[u] for u in adj[v] if color[u] >= 0})
                if sat > best_sat or (sat == best_sat and len(adj[v]) > len(adj[best])):
                    best, best_sat = v, sat
        v = best
        used = {color[u] for u in adj[v] if color[u] >= 0}
        for c in range(3):
            if c not in used:
                color[v] = c
                r = solve(ncolored + 1)
                if r is not None:
                    if r:
                        return True
                else:
                    color[v] = -1
                    return None
                color[v] = -1
        return False

    r = solve(0)
    result['bb_nodes'] = nodes_visited[0]
    if r is True:
        F = list(color)
        result['factor3_exists'] = True
        # independent verification of F over all constraints
        ok = True
        for s in SYMS:
            sW = [apply(w, s) for w in W]
            U = sorted(set(W) | set(sW), key=lambda g: bidx[g])
            uidx = {u: k for k, u in enumerate(U)}
            w_at = [uidx[w] for w in W]
            s_at = [uidx[w] for w in sW]
            for rr in range(1 << len(U)):
                P = sum((((rr >> k) & 1) << j) for j, k in enumerate(w_at))
                Pp = sum((((rr >> k) & 1) << j) for j, k in enumerate(s_at))
                if F[P] == F[Pp]:
                    ok = False
                    break
            if not ok:
                break
        result['verification_pass'] = ok
        result['F'] = F
    elif r is False:
        result['factor3_exists'] = False
        result['reason'] = ('exhaustive backtracking: no proper 3-coloring '
                            'of the 64-vertex radius-1 constraint graph')
    else:
        result['factor3_exists'] = 'UNKNOWN (node cap)'
        result['reason'] = 'backtracking hit node cap'

with open('sft_radius1.json', 'w') as f:
    json.dump(result, f, indent=1)
print(json.dumps({k: v for k, v in result.items() if k != 'F'}, indent=1))
if F is not None:
    print('F =', F)
