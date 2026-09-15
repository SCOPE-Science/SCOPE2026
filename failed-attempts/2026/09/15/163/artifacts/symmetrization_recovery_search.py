"""Recovery test: can a linearity-preserving symmetrization step still create a
Berge C5? Random-search tiny linear Berge-C5-free hypergraphs for a nonadjacent
pair (u,v) whose symmetrization v->u keeps linearity but creates a Berge C5.
Either outcome is recorded; a hit gives a second, stronger obstruction, while a
miss still leaves the proven linearity-breaking counterexample intact.
"""
import random
from itertools import combinations, permutations

def is_linear(edges):
    seen = set()
    for e in edges:
        for p in combinations(sorted(e), 2):
            if p in seen:
                return False
            seen.add(p)
    return True

def berge_cycle(edges, k):
    E = [set(e) for e in edges]
    if len(E) < k:
        return False
    verts = sorted({x for e in E for x in e})
    for et in permutations(range(len(E)), k):
        EE = [E[i] for i in et]
        for xt in permutations(verts, k):
            ok = True
            for i in range(k):
                if not ({xt[i], xt[(i + 1) % k]} <= EE[i]):
                    ok = False
                    break
            if ok:
                return True
    return False

def symmetrize(edges, u, v):
    Eu = [e for e in edges if u in e]
    rest = [e for e in edges if v not in e]
    return rest + [frozenset((set(e) - {u}) | {v}) for e in Eu]

random.seed(20421)
hits_c5 = 0
hits_linbreak = 0
tried = 0
hit_example = None
for trial in range(4000):
    n = 8
    verts = list(range(n))
    # random linear hypergraph: greedily add random triples keeping linearity
    edges = []
    used_pairs = set()
    triples = [frozenset(t) for t in combinations(verts, 3)]
    random.shuffle(triples)
    for t in triples:
        ps = [tuple(sorted(p)) for p in combinations(sorted(t), 2)]
        if any(p in used_pairs for p in ps):
            continue
        if random.random() < 0.25:
            edges.append(t)
            used_pairs.update(ps)
    if len(edges) < 4:
        continue
    if not is_linear(edges) or berge_cycle(edges, 5):
        continue
    for u in verts:
        for v in verts:
            if u == v:
                continue
            if any({u, v} <= set(e) for e in edges):
                continue
            Ep = symmetrize(edges, u, v)
            tried += 1
            if not is_linear(Ep):
                hits_linbreak += 1
            elif berge_cycle(Ep, 5):
                hits_c5 += 1
                if hit_example is None:
                    hit_example = (edges, u, v, Ep)

print(f"symmetrizations tried on linear C5-free inputs: {tried}")
print(f"linearity-breaking outcomes: {hits_linbreak}")
print(f"linearity-preserving but C5-creating outcomes: {hits_c5}")
if hit_example:
    E, u, v, Ep = hit_example
    print("example input:", sorted(map(sorted, E)), "u,v =", u, v)
    print("symmetrized:", sorted(map(sorted, Ep)))
print("PASS: recovery test completed (primary obstruction already proven analytically)")
