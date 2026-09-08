"""Counterexample: graph shifting does NOT preserve C4-freeness.

Exhausts all 2^15 graphs on vertex set {0..5} (edges listed canonically) and
checks every graph that is C4-free but whose standard (i,j)=(0,1) shift
contains a C4. Prints the first witness with full edge lists.

Definitions (standard):
- C4 test: 4 distinct vertices a,b,c,d with edges ab,bc,cd,da (any K_{2,2}).
- Shift S_ij (i<j): for each k != i,j with edge jk present and ik absent,
  replace jk by ik; else keep edge. (Multiple k resolved simultaneously from
  the original edge set; pairs not incident to j are untouched.)
"""
import itertools

N = 6
PAIRS = [(a, b) for a in range(N) for b in range(a + 1, N)]
P2I = {p: i for i, p in enumerate(PAIRS)}


def has_c4(mask):
    adj = [[False] * N for _ in range(N)]
    for i, (a, b) in enumerate(PAIRS):
        if mask >> i & 1:
            adj[a][b] = adj[b][a] = True
    for a in range(N):
        for b in range(a + 1, N):
            common = [c for c in range(N) if c != a and c != b and adj[a][c] and adj[b][c]]
            if len(common) >= 2:
                return True
    return False


def shift01(mask):
    edges = set(PAIRS[i] for i in range(len(PAIRS)) if mask >> i & 1)
    i, j = 0, 1
    out = set()
    for (a, b) in edges:
        if b == j and a != i:
            k = a
            if (min(i, k), max(i, k)) not in edges:
                out.add((min(i, k), max(i, k)))
            else:
                out.add((a, b))
        elif a == j and b != i:
            k = b
            if (min(i, k), max(i, k)) not in edges:
                out.add((min(i, k), max(i, k)))
            else:
                out.add((a, b))
        else:
            out.add((a, b))
    m2 = 0
    for p in out:
        m2 |= 1 << P2I[p]
    return m2


def edges_of(mask):
    return sorted(PAIRS[i] for i in range(len(PAIRS)) if mask >> i & 1)


found = None
total = 0
for mask in range(1 << len(PAIRS)):
    total += 1
    if has_c4(mask):
        continue
    if has_c4(shift01(mask)):
        found = mask
        break

assert found is not None, "expected a counterexample on 6 vertices"
print(f"enumerated {total} graphs (up to first witness) on 6 vertices")
print("witness G (C4-free):", edges_of(found))
print("shifted S_01(G) (contains C4):", edges_of(shift01(found)))
print("C4 in G:", has_c4(found), "| C4 in S_01(G):", has_c4(shift01(found)))
print("COUNTEREXAMPLE CONFIRMED: shifting does not preserve C4-freeness.")
