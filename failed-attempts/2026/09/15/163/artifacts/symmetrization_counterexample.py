"""Zykov symmetrization does NOT preserve linearity (hence not Berge-C5-freeness
arguments that assume staying inside the linear class).

Instance: V={u,v,a,b,c}, E={ {u,a,b}, {v,a,c} }.
Checks: linear, Berge-C5-free, u,v nonadjacent. Symmetrize v -> u:
delete edges at v, add (e\\{u})U{v} for each edge e at u.
Result E'={ {u,a,b}, {v,a,b} } shares pair {a,b}: linearity broken.
"""
from itertools import combinations

def is_linear(edges):
    seen = {}
    for e in edges:
        for p in combinations(sorted(e), 2):
            if p in seen:
                return False, p
            seen[p] = e
    return True, None

def berge_cycle(edges, k):
    # distinct edges e_1..e_k and distinct vertices x_1..x_k (cyclic) with
    # {x_i, x_{i+1}} subset of e_i. Brute force over edge tuples (tiny input).
    E = [set(e) for e in edges]
    n = len(E)
    if n < k:
        return False
    verts = sorted({x for e in E for x in e})
    from itertools import permutations
    for etuple in permutations(range(n), k):
        eidx = list(etuple)
        # ordered distinct vertices x_1..x_k with x_i,x_{i+1} in E[eidx_i]
        for xtuple in permutations(verts, k):
            ok = True
            for i in range(k):
                x, y = xtuple[i], xtuple[(i + 1) % k]
                if not ({x, y} <= E[eidx[i]]):
                    ok = False
                    break
            if ok:
                return True
    return False

u, v, a, b, c = "u", "v", "a", "b", "c"
E = [frozenset({u, a, b}), frozenset({v, a, c})]

lin, wit = is_linear(E)
print("original linear:", lin); assert lin
print("original Berge-C5-free:", not berge_cycle(E, 5)); assert not berge_cycle(E, 5)
nonadj = not any({u, v} <= set(e) for e in E)
print("u,v nonadjacent:", nonadj); assert nonadj

# symmetrize v -> u
Eu = [e for e in E if u in e]
Ep = [e for e in E if v not in e] + [frozenset((set(e) - {u}) | {v}) for e in Eu]
print("symmetrized edges:", sorted(map(sorted, Ep)))
lin2, wit2 = is_linear(Ep)
print("symmetrized linear:", lin2, "| offending pair:" , wit2)
assert not lin2, "expected linearity to break"
print("PASS: Zykov symmetrization breaks linearity on a linear Berge-C5-free input")
