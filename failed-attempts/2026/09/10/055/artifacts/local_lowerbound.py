"""Route D probe: exact freeness of <a, v=cac> and the LOCAL lower-bound
transfer blocking the audit plan's Step-3 premise.

D1. EXACT freeness proof (by free-product normal form; machine-corroborated
to word-length 8 in cayley_cell.py):
  In Gamma = Z^2 * C2, every element has a unique normal form alternating
  non-identity Z^2-blocks and c's: B0 c B1 c ... c Bk, interior Bi != 0.
  Put v = c a c. A reduced word w = a^{e0} v^{k1} a^{e1} ... v^{km} a^{em}
  (all ki != 0, ei != 0 except possibly e0, em) expands to
    a^{e0} c a^{k1} c a^{e1} c ... c a^{km} c a^{em}.
  Fusing adjacent Z^2-blocks gives an alternating word in which every c is
  separated by a NONZERO Z^2 power (ki != 0 guaranteed; ei != 0 interior
  guaranteed by reducedness). If e0 != 0 or em != 0 the end blocks are
  nonzero too. Hence the fused form is a valid normal form of positive
  length (>= 1 c-symbol since m >= 1 when w is nonempty... if m = 0 then
  w = a^{e0} != e as e0 != 0). By uniqueness of normal forms, w != e.
  Therefore <a, v> is free of rank 2. QED (exact, no computation needed;
  the length-8 enumeration in cell_census.json corroborates).

D2. Consequence: the Schreier graph G contains, on each <a,v>-orbit, a
  4-regular infinite tree (Cayley graph of F2). Any LOCAL 3-coloring rule
  for the cell restricts to a LOCAL 3-coloring of trees.

D3. Known LOCAL lower bound (literature): 3-coloring n-vertex trees of
  bounded degree requires Omega(log n) deterministic LOCAL rounds
  (in particular NOT O(log* n)); cf. Chang-Kopelowitz-Pettie / Brandt et
  al. line of work; the path/cycle already needs Theta(log* n) and trees
  need Theta(log n). Hence NO O(log* n) LOCAL 3-coloring rule exists for
  this cell.

D4. This BLOCKS audit_plan Step 3 as literally stated ("lift an O(log* n)
  LOCAL 3-coloring rule through an explicit toast"): the required rule
  does not exist. A Borel 3-coloring via toast would need a different
  ingredient (e.g. an O(log n)-round rule combined with toast, which is
  the Bernshteyn-type machinery that fails here for growth reasons), and
  the Marks-game obstruction route is untouched by this observation.

This script records the formal statement + checks the tree embedding to
depth 6 (BFS from e using only {a,a^-1,v,v^-1} is a 4-regular tree ball:
nodes = 1+4+4*3+... and no collisions / no short cycles).
Stdlib only. Writes local_lowerbound.json.
"""
import json
from collections import deque

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
def apply(T, g):
    s = GENS[g]
    if s[0] == 'A':
        return mul_A(T, s[1], s[2])
    return mul_c(T)

V = [apply(apply(apply(E, 'c'), 'a'), 'c')]  # v = cac
Vm = E
for g in ['c', 'ai', 'c']:
    Vm = apply(Vm, g)  # v^-1 = c a^-1 c
V = V[0]
TV = {'v': ['c', 'a', 'c'], 'vi': ['c', 'ai', 'c'],
      'u': ['a'], 'ui': ['ai']}
INV = {'v': 'vi', 'vi': 'v', 'u': 'ui', 'ui': 'u'}
KEYS = ['u', 'ui', 'v', 'vi']

def step(T, k):
    for g in TV[k]:
        T = apply(T, g)
    return T

# BFS tree ball using {u,ui,v,vi} with non-backtracking = full tree ball
dist = {E: 0}
q = deque([(E, None)])
while q:
    g, last = q.popleft()
    if dist[g] >= 6:
        continue
    for k in KEYS:
        if last is not None and k == INV[last]:
            continue
        h = step(g, k)
        if h not in dist:
            dist[h] = dist[g] + 1
            q.append((h, k))
sizes = {}
for d in dist.values():
    sizes[d] = sizes.get(d, 0) + 1
# ideal 4-regular tree ball layer sizes: 1,4,12,36,108,324,972
ideal = {0: 1}
for i in range(1, 7):
    ideal[i] = 4 * (3 ** (i - 1))
tree_ok = all(sizes.get(i, -1) == ideal[i] for i in range(7))

out = {
    'free_subgroup': '<a, cac> free of rank 2 (exact normal-form proof)',
    'tree_ball_layers': sizes,
    'ideal_tree_layers': ideal,
    'tree_embedding_exact_to_depth6': tree_ok,
    'conclusion': ('<a,cac>-orbits are 4-regular infinite trees; '
                   '3-coloring trees needs Omega(log n) LOCAL rounds, '
                   'so no O(log* n) LOCAL 3-coloring rule exists: '
                   'audit Step 3 premise BLOCKED as stated'),
}
with open('local_lowerbound.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
