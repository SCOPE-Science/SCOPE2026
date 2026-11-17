"""Independent finite checks of two-colour strong-majority colourings.

Standard-library-only. This enumerates raw edge colourings and vertex
subsets independently and compares their complete sets, not just totals.
"""
from itertools import combinations
from random import Random


def graph(n, edges):
    ee = sorted({tuple(sorted((u, v))) for u, v in edges})
    assert all(0 <= u < v < n for u, v in ee)
    adj = [0] * n
    for u, v in ee:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    assert all(x.bit_count() == 3 for x in adj)
    seen, pending = {0}, [0]
    while pending:
        v = pending.pop()
        for u in range(n):
            if (adj[v] >> u) & 1 and u not in seen:
                seen.add(u)
                pending.append(u)
    assert len(seen) == n
    return ee, adj


def all_codes(n, adj):
    if n % 4:
        return set()
    hood = [x | (1 << v) for v, x in enumerate(adj)]
    codes = set()
    for inds in combinations(range(n), n // 4):
        s = sum(1 << v for v in inds)
        if all((s & h).bit_count() == 1 for h in hood):
            codes.add(s)
    return codes


def all_balanced_colours(edges):
    m = len(edges)
    neigh = []
    for i, (u, v) in enumerate(edges):
        neigh.append(sum(1 << j for j, (a, b) in enumerate(edges)
                         if i != j and (u == a or u == b or v == a or v == b)))
    assert all(x.bit_count() == 4 for x in neigh)
    return {colour for colour in range(1 << m)
            if all((colour & h).bit_count() == 2 for h in neigh)}


def test_edges(n, edge_list, label):
    edges, adj = graph(n, edge_list)
    codes = all_codes(n, adj)
    observed = all_balanced_colours(edges)
    predicted = set()
    for s in codes:
        star = sum(1 << j for j, (u, v) in enumerate(edges)
                   if ((s >> u) & 1) or ((s >> v) & 1))
        predicted.add(star)
        predicted.add(star ^ ((1 << len(edges)) - 1))
    assert observed == predicted, (label, len(observed), len(predicted))
    print("RAW_EDGE_COLOURS_OK", label, n, len(codes), len(observed))


def prism(n):
    return 2 * n, [(i, (i + 1) % n) for i in range(n)] + [
        (n + i, n + (i + 1) % n) for i in range(n)] + [
        (i, n + i) for i in range(n)]


def mobius(n):
    # The Möbius ladder on an even number n>=6 of vertices.
    return n, [(i, (i+1) % n) for i in range(n)] + [
        (i, i+n//2) for i in range(n//2)]


def random_cubic(n, seed):
    rng = Random(seed)
    for _ in range(20000):
        stubs = [v for v in range(n) for _ in range(3)]
        rng.shuffle(stubs)
        ee = [tuple(sorted(stubs[i:i+2])) for i in range(0, len(stubs), 2)]
        if any(u == v for u, v in ee) or len(set(ee)) < len(ee):
            continue
        try:
            graph(n, ee)
        except AssertionError:
            continue
        return n, ee
    raise AssertionError("simple connected cubic sampler exhausted")


def main():
    test_edges(4, list(combinations(range(4), 2)), "K4")
    test_edges(6, [(i, j) for i in range(3) for j in range(3, 6)], "K33")
    # Petersen graph as outer 5-cycle, inner step-2 5-cycle and spokes.
    pet = [(i, (i+1) % 5) for i in range(5)] + [
        (5+i, 5+(i+2) % 5) for i in range(5)] + [(i, i+5) for i in range(5)]
    test_edges(10, pet, "Petersen")
    for n in range(3, 7):
        N, ee = prism(n)
        test_edges(N, ee, "prism" + str(n))
    for n in (8, 10, 12):
        N, ee = mobius(n)
        test_edges(N, ee, "mobius" + str(n))
    for n in (8, 10, 12):
        for seed in (11, 29, 43):
            N, ee = random_cubic(n, seed)
            test_edges(N, ee, "sample%d_%d" % (n, seed))
    for n in range(3, 13):
        N, ee = prism(n)
        _, adj = graph(N, ee)
        ncodes = len(all_codes(N, adj))
        assert ncodes == (4 if n % 4 == 0 else 0)
        print("PRISM_CODE_CENSUS_OK", n, ncodes)
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
