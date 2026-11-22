"""Exact edge-open-packing polynomials and orbit census for two line graphs.

Only the Python standard library is required. All edges and vertices are labelled.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations


def canonical(e):
    return tuple(sorted(e))


def base_graph(kind):
    if kind == "petersen":
        labels = tuple(map(frozenset, combinations(range(5), 2)))
        edges = tuple((i, j) for i in range(10) for j in range(i+1, 10)
                      if not (labels[i] & labels[j]))
        return labels, edges
    if kind == "prism":
        edges = tuple(canonical((5*r+i, 5*r+(i+1)%5))
                      for r in range(2) for i in range(5))
        edges += tuple((i, i+5) for i in range(5))
        return tuple(range(10)), tuple(sorted(edges))
    raise ValueError(kind)


def conflict_matrix(edges):
    # Vertices of L(H) are edges of H. Edges of L(H) are incident pairs.
    line_edges = tuple((i, j) for i in range(len(edges))
                       for j in range(i+1, len(edges))
                       if set(edges[i]).intersection(edges[j]))
    line_edge_set = set(line_edges)
    N = len(line_edges)
    masks = [0] * N
    for i, (a,b) in enumerate(line_edges):
        for j, (c,d) in enumerate(line_edges):
            if i == j:
                continue
            # A common third edge must be DIFFERENT from both selected edges.
            if any(canonical((x,y)) in line_edge_set - {line_edges[i],line_edges[j]}
                   for x in (a,b) for y in (c,d) if x!=y):
                masks[i] |= 1<<j
    assert all((masks[i] >> j)&1 == (masks[j]>>i)&1
               for i in range(N) for j in range(N))
    return line_edges, masks


def poly_count(masks):
    @lru_cache(None)
    def f(S):
        if S == 0:
            return (1,)
        bit = S & -S
        v = bit.bit_length() - 1
        # Either omit edge v or choose it and exclude its conflict neighbors.
        omit = f(S ^ bit)
        choose = f((S ^ bit) & ~masks[v])
        n = max(len(omit), len(choose)+1)
        return tuple((omit[k] if k < len(omit) else 0) +
                     (choose[k-1] if 1<=k<=len(choose) else 0)
                     for k in range(n))
    full = f((1 << len(masks)) - 1)
    return tuple(full), f.cache_info()


def independent_sets_exactly_four(masks):
    n = len(masks)
    result = set()
    for choice in combinations(range(n), 4):
        if all(not (masks[a]>>b & 1) for a,b in combinations(choice, 2)):
            result.add(sum(1<<a for a in choice))
    return result


def petersen_orbits(vertices, edges, line_edges, optimum):
    vertex_number = {v:i for i,v in enumerate(vertices)}
    edge_number = {e:i for i,e in enumerate(edges)}
    line_edge_number = {e:i for i,e in enumerate(line_edges)}
    actions = []
    for p in permutations(range(5)):
        vm = tuple(vertex_number[frozenset(p[x] for x in s)] for s in vertices)
        em = tuple(edge_number[canonical((vm[a],vm[b]))] for a,b in edges)
        lm = tuple(line_edge_number[canonical((em[a],em[b]))] for a,b in line_edges)
        assert len(set(lm)) == 30
        actions.append(lm)
    unseen = set(optimum)
    output = []
    while unseen:
        rep = min(unseen)
        idx = [i for i in range(30) if (rep>>i)&1]
        orb = {sum(1<<action[i] for i in idx) for action in actions}
        assert orb <= optimum
        assert orb <= unseen
        output.append((len(orb), idx))
        unseen.difference_update(orb)
    return sorted(output)


def main():
    expected = {"petersen":(1,30,225,530,330),
                "prism":(1,30,235,580,415)}
    for kind in ("petersen","prism"):
        vertices, edges = base_graph(kind)
        line_edges, masks = conflict_matrix(edges)
        assert (len(vertices),len(edges),len(line_edges)) == (10,15,30)
        coeff, memo = poly_count(masks)
        assert coeff == expected[kind], (kind,coeff)
        print(f"{kind}: {coeff}; memo_states={memo.currsize}; conflict_degree={Counter(x.bit_count() for x in masks)}")
        if kind == "petersen":
            opt = independent_sets_exactly_four(masks)
            assert len(opt) == 330
            orbits = petersen_orbits(vertices,edges,line_edges,opt)
            assert [x[0] for x in orbits] == [30,60,120,120]
            print("petersen_S5_orbits:",orbits)
    print("RECURRENCE_AND_ORBITS_OK")


if __name__ == "__main__":
    main()
