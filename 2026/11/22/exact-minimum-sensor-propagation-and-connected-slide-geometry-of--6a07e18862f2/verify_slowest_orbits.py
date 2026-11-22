"""Check the two full symmetry orbits of maximal-duration Gray sensor sets.

Run with Python 3; no third-party modules or input data are required.
Point indices are 9a+3b+c. Line indices 27+9d+3u+v for axis d
and the fixed coordinates u,v in the two other axes in ascending order.
"""
from itertools import permutations, product

SYMBOL_PERMS = list(permutations(range(3)))


def point_coords(v):
    return (v // 9, v // 3 % 3, v % 3)


def line_coords(v):
    code = v - 27
    axis = code // 9
    rest = (code // 3 % 3, code % 3)
    fixed = [-1, -1, -1]
    i = 0
    for a in range(3):
        if a != axis:
            fixed[a] = rest[i]
            i += 1
    return fixed


def line_index(fixed):
    axis = fixed.index(-1)
    keep = [fixed[d] for d in range(3) if d != axis]
    return 27 + 9 * axis + 3 * keep[0] + keep[1]


def graph():
    edges = set()
    adj = [set() for _ in range(54)]
    for a, b, c in product(range(3), repeat=3):
        p = 9 * a + 3 * b + c
        for l in (27 + 3 * b + c, 36 + 3 * a + c, 45 + 3 * a + b):
            edges.add((p, l))
            adj[p].add(l)
            adj[l].add(p)
    assert len(edges) == 81 and all(len(x) == 3 for x in adj)
    return edges, adj


def apply_group(axes, symbols):
    result = []
    for index in range(54):
        if index < 27:
            source = point_coords(index)
        else:
            source = line_coords(index)
        dest = [(-1 if source[axes[d]] == -1 else symbols[d][source[axes[d]]])
                for d in range(3)]
        if -1 in dest:
            result.append(line_index(dest))
        else:
            result.append(9 * dest[0] + 3 * dest[1] + dest[2])
    assert len(set(result)) == 54
    return result


def observation_time(selected, adj):
    seen = set(selected)
    for v in selected:
        seen.update(adj[v])
    t = 1  # domination is round 1
    while len(seen) < 54:
        force = set()
        for v in seen:
            white = adj[v] - seen
            if len(white) == 1:
                force.update(white)
        if not force:
            return None
        seen.update(force)
        t += 1
    return t


def check_lcf_isomorphism(edges):
    # The following explicit bijection maps lattice points to even labels
    # and axis lines to odd labels of the published LCF representation.
    iso = [
        0, 52, 24, 30, 38, 32, 28, 40, 26,
        2, 50, 48, 4, 44, 46, 16, 42, 18,
        8, 10, 22, 6, 36, 34, 14, 12, 20,
        1, 51, 23, 5, 37, 33, 15, 41, 19,
        29, 39, 25, 3, 43, 47, 7, 11, 21,
        53, 31, 27, 49, 45, 17, 9, 35, 13
    ]
    assert sorted(iso) == list(range(54))
    shifts = (-25, 7, -7, 13, -13, 25)
    lcf_edges = {tuple(sorted((i, (i + 1) % 54))) for i in range(54)}
    for i in range(54):
        j = (i + shifts[i % 6]) % 54
        lcf_edges.add(tuple(sorted((i, j))))
    assert len(lcf_edges) == 81
    mapped = {tuple(sorted((iso[p], iso[l]))) for p, l in edges}
    assert mapped == lcf_edges


def main():
    edges, adj = graph()
    check_lcf_isomorphism(edges)
    seeds = ((0, 4, 11, 33, 43, 52), (0, 4, 8, 10, 39, 52))
    orbits = [set(), set()]
    group_count = 0
    for axes in SYMBOL_PERMS:
        for symbols in product(SYMBOL_PERMS, repeat=3):
            trans = apply_group(axes, symbols)
            assert all((trans[p], trans[l]) in edges for p, l in edges)
            for which, seed in enumerate(seeds):
                orbits[which].add(tuple(sorted(trans[v] for v in seed)))
            group_count += 1
    assert group_count == 1296
    assert tuple(len(orb) for orb in orbits) == (1296, 1296)
    assert orbits[0].isdisjoint(orbits[1])
    for orb in orbits:
        assert all(observation_time(S, adj) == 10 for S in orb)
    assert all(sum(v < 27 for v in S) == 3 for S in orbits[0])
    assert all(sum(v < 27 for v in S) == 4 for S in orbits[1])
    print("symmetry_actions=1296 maximal_round_orbits=2 orbit_sizes=1296,1296")
    print("maximal_duration_sets=2592; PASS")


if __name__ == "__main__":
    main()
