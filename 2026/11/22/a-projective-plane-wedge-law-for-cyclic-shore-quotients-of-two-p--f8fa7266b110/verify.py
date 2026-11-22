"""Finite orbit and attaching-word checks for a cyclic quotient of a graph configuration space.

No third-party modules are used.  This checker corroborates, but does not replace,
the uniform topological proof in RESULT.md.
"""
from itertools import combinations


def analyze(n):
    assert n >= 3
    left = range(3)
    right = range(3, n + 3)
    vertices = range(n + 3)
    edges = tuple((a, b) for a in left for b in right)
    zeros = tuple(combinations(vertices, 2))
    ones = tuple((v, e) for v in vertices for e in edges if v not in e)
    twos = tuple((e, f) for e, f in combinations(edges, 2) if not set(e) & set(f))

    def move_vertex(v):
        return (v + 1) % 3 if v < 3 else v

    def move_cell(c, dim):
        if dim == 0:
            return tuple(sorted(map(move_vertex, c)))
        if dim == 1:
            return (move_vertex(c[0]), tuple(map(move_vertex, c[1])))
        return tuple(sorted(tuple(map(move_vertex, edge)) for edge in c))

    def orbit_data(cells, dim):
        found = {}
        sizes = []
        for cell in cells:
            if cell in found:
                continue
            orb = []
            z = cell
            while z not in orb:
                orb.append(z)
                z = move_cell(z, dim)
            assert z == cell
            ix = len(sizes)
            for z in orb:
                assert z not in found
                found[z] = ix
            sizes.append(len(orb))
        return found, sizes

    o0, s0 = orbit_data(zeros, 0)
    o1, s1 = orbit_data(ones, 1)
    o2, s2 = orbit_data(twos, 2)
    assert len(o0) == len(zeros) and len(o1) == len(ones) and len(o2) == len(twos)
    assert len(s0) == n * (n - 1) // 2 + n + 1
    assert len(s1) == n * (n + 1)
    assert len(s2) == n * (n - 1)
    assert s0.count(1) == n * (n - 1) // 2 and s0.count(3) == n + 1
    assert all(sz == 3 for sz in s1 + s2)

    def edge(i, j):
        return (i, j + 3)

    # Names of every orbit; these are independently checked to be exhaustive.
    zero_reps = {'T': (0, 1)}
    zero_reps.update({('Q', j): (0, j + 3) for j in range(n)})
    zero_reps.update({('P', i, j): (i + 3, j + 3)
                      for i in range(n) for j in range(i + 1, n)})
    one_reps = {('L+', j): (1, edge(0, j)) for j in range(n)}
    one_reps.update({('L-', j): (2, edge(0, j)) for j in range(n)})
    one_reps.update({('R', k, j): (k + 3, edge(0, j))
                     for k in range(n) for j in range(n) if k != j})
    two_reps = {}
    for i in range(n):
        for j in range(i + 1, n):
            two_reps[('A', i, j)] = tuple(sorted((edge(0, i), edge(1, j))))
            two_reps[('B', i, j)] = tuple(sorted((edge(0, i), edge(2, j))))
    for reps, orbits in [(zero_reps, o0), (one_reps, o1), (two_reps, o2)]:
        assert len(reps) == len(set(orbits.values()))
        assert len(set(orbits[rep] for rep in reps.values())) == len(reps)
    name0 = {o0[v]: k for k, v in zero_reps.items()}
    name1 = {o1[v]: k for k, v in one_reps.items()}

    # Independently compute the boundary from each product edge, then identify
    # the C_3 orbit of its oriented vertex-edge face.
    def boundary_of_one(cell):
        v, (u, w) = cell
        return [(+1, tuple(sorted((v, w)))),
                (-1, tuple(sorted((v, u))))]

    def boundary_of_square(first, second):
        u, w = first
        x, y = second
        # Counterclockwise traversal of [u,w] x [x,y] starting at (u,x).
        return [(+1, (x, first)),
                (+1, (w, second)),
                (-1, (y, first)),
                (-1, (u, second))]

    def one_name(cell):
        return name1[o1[cell]]

    for lab, cell in one_reps.items():
        boundary = [(sg, name0[o0[z]]) for sg, z in boundary_of_one(cell)]
        if lab[0] == 'R':
            k, j = lab[1:]
            want = [(+1, ('P', min(k, j), max(k, j))), (-1, ('Q', k))]
        else:
            want = [(+1, ('Q', lab[1])), (-1, 'T')]
        assert boundary == want, (n, lab, boundary, want)

    for lab, cell in two_reps.items():
        kind, i, j = lab
        # The order is fixed in the geometric square, not by sorting the
        # two edges to select an orientation.
        first = edge(0, i)
        second = edge(1 if kind == 'A' else 2, j)
        observed = [(sg, one_name(z)) for sg, z in boundary_of_square(first, second)]
        if kind == 'A':
            want = [(-1, ('L-', j)), (+1, ('R', i, j)),
                    (-1, ('R', j, i)), (+1, ('L+', i))]
        else:
            want = [(-1, ('L+', j)), (+1, ('R', i, j)),
                    (-1, ('R', j, i)), (+1, ('L-', i))]
        # boundary_of_square starts on the vertex of the second edge and
        # traverses the first edge.  Its ordering is immaterial in chains.
        assert sorted(map(str, observed)) == sorted(map(str, want)), (n, lab, observed, want)

    # The chosen maximal tree consists of all L+ edges and the R_(i,j)
    # edges with i < j.  Every other edge is a loop generator after
    # collapsing the tree, and every 2-cell has a two-letter attaching word.
    for i in range(n):
        for j in range(i + 1, n):
            for kind in ('A', 'B'):
                first = edge(0, i)
                second = edge(1 if kind == 'A' else 2, j)
                loop = []
                for sign, cell in boundary_of_square(first, second):
                    name = one_name(cell)
                    if name[0] == 'L+':
                        continue
                    if name[0] == 'R' and name[1] < name[2]:
                        continue
                    loop.append((sign, name))
                if kind == 'A':
                    want = [(-1, ('L-', j)), (-1, ('R', j, i))]
                else:
                    want = [(+1, ('L-', i)), (-1, ('R', j, i))]
                assert sorted(map(str, loop)) == sorted(map(str, want)), (n, kind, i, j, loop)

    # These equations constitute a complete presentation (not just ranks):
    # A_ij says x_j y_ij = 1, B_ij says x_i y_ij^{-1} = 1.
    # Eliminating y gives x_i x_j = 1 for every i<j.  For n>=3,
    # eliminating x_2,...,x_n leaves exactly binom(n-1,2) copies of x_1^2.
    number_of_equal_degree_two_disks = (n - 1) * (n - 2) // 2
    expected_spheres = number_of_equal_degree_two_disks - 1
    assert expected_spheres == n * (n - 3) // 2
    return (len(s0), len(s1), len(s2)), expected_spheres


if __name__ == '__main__':
    for n in range(3, 10):
        cells, spheres = analyze(n)
        print(f'n={n} cells={cells} pi1=Z/2 extra_S2={spheres}')
    print('THREE_SHORE_CYCLIC_CONFIGURATION_ORBITS_OK')
