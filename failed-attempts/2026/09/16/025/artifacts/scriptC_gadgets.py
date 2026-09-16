"""Script C: gadget refinement. Recap-style ladder gadget inside top V1 of B_rec,
and generic gadget+C7 detector for small n. Tests bounded (O(n^2) with const) C7-free extras."""
import itertools
from math import comb

def brec_dp(N):
    b = [0]*(N+1); ch = [None]*(N+1)
    for n in range(3, N+1):
        best = -1; ba = 0
        for a in range(n+1):
            v = comb(a, 2)*(n-a) + b[n-a]
            if v > best: best = v; ba = a
        b[n] = best; ch[n] = ba
    return b, ch

B, CH = brec_dp(40)

def build_brec(n, offset=0):
    edges = set(); blocks = []
    def rec(verts):
        m = len(verts)
        if m <= 2: return
        a = CH[m]
        V1 = verts[:a]; V2 = verts[a:]
        blocks.append(list(V1))
        for i in range(len(V1)):
            for j in range(i+1, len(V1)):
                for w in V2:
                    edges.add(tuple(sorted((V1[i], V1[j], w))))
        rec(V2)
    rec(list(range(offset, offset+n)))
    top = set(blocks[0]) if blocks else set()
    return edges, blocks, top

def has_C7(edges, n, cap=1):
    """Return up to `cap` C7 cyclic orderings (tuple of 7 verts) in vertex set range(n)."""
    found = []
    for tup in itertools.permutations(range(n), 7):
        ok = True
        for i in range(7):
            t = tuple(sorted((tup[i], tup[(i+1)%7], tup[(i+2)%7])))
            if t not in edges:
                ok = False; break
        if ok:
            found.append(tup)
            if len(found) >= cap: break
    return found

def ladder_inside_V1(V1, rungs):
    """Ladder/path-like gadget: order V1 and take triples {v_i, v_{i+1}, v_{i+3]} style.
    Returns edge set of gadget with ~|V1| edges (linear, hence safe direction)."""
    V1 = sorted(V1); add = set(); m = len(V1)
    for i in range(m-3):
        add.add(tuple(sorted((V1[i], V1[i+1], V1[i+3]))))
    return add

def matching_inside_V1(V1):
    """Linear gadget: disjoint triples inside V1."""
    V1 = sorted(V1); add = set()
    for i in range(0, len(V1)-2, 3):
        add.add(tuple(sorted((V1[i:i+3]))))
    return add

print("== linear gadgets added to B_rec: C7 check ==")
for n in range(3, 13):
    E, blocks, top = build_brec(n)
    for name, g in [("ladder", ladder_inside_V1(top, None)), ("matching", matching_inside_V1(top))]:
        E2 = E | g
        cyc = has_C7(E2, n, cap=1)
        print(f"n={n} {name}: |V1|={len(top)} +{len(g)} C7={cyc if cyc else None}")

print("== sparse rung gadget scaled: does B_rec+ladder stay C7-free? (n<=12) ==")
for n in [11, 12]:
    E, blocks, top = build_brec(n)
    g = ladder_inside_V1(top, None)
    E2 = E | g
    cyc = has_C7(E2, n, cap=3)
    print(f"n={n} +{len(g)} C7list={cyc if cyc else None}")

print("== key structural question: which vertex-sets S (size 7) force C7 in B_rec+extra? ==")
# For n=10 star case: enumerate all 7-subsets containing the star center pattern
n = 10
E, blocks, top = build_brec(n)
V1 = sorted(top); x = V1[0]
rest = [v for v in V1 if v != x]
add = set()
for i in range(len(rest)):
    for j in range(i+1, len(rest)):
        add.add(tuple(sorted((x, rest[i], rest[j]))))
E2 = E | add
cycs = has_C7(E2, n, cap=50)
print(f"n={n} star: total C7 orderings (cap 50): {len(cycs)}")
for c in cycs[:10]: print("  ", c)
