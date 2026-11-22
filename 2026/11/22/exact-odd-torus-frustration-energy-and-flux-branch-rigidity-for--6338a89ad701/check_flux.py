"""Direct finite-torus test of the uniform-flux construction and action identity.

This tests finitely many sizes and sign sectors. The proof in RESULT.md,
not this numerical test, establishes the theorem for all allowed sizes.
"""
import cmath
import itertools
import math


def make_links(sizes, branch):
    """Pairwise seam-gauge construction for oriented plaquettes i<j."""
    dims = len(sizes)
    assert dims == 3 and all(L >= 2 for L in sizes)
    edges = {}
    angles = {}
    for i, j in itertools.combinations(range(3), 2):
        area = sizes[i] * sizes[j]
        k = area // 2 if area % 2 == 0 else (area + branch[(i, j)]) // 2
        assert 0 <= k < area or area == 2
        angles[(i, j)] = 2 * math.pi * k / area
    for x in itertools.product(*(range(L) for L in sizes)):
        for axis in range(3):
            val = 0.0
            for (i, j), phi in angles.items():
                if axis == i:
                    val -= phi * x[j]
                if axis == j and x[j] == sizes[j] - 1:
                    val += phi * sizes[j] * x[i]
            edges[(x, axis)] = cmath.exp(1j * val)
    return edges, angles


def plaquette(edges, x, i, j, sizes):
    xi = tuple((z + int(k == i)) % sizes[k] for k, z in enumerate(x))
    xj = tuple((z + int(k == j)) % sizes[k] for k, z in enumerate(x))
    return edges[(x, i)] * edges[(xi, j)] * edges[(xj, i)].conjugate() * edges[(x, j)].conjugate()


def run():
    tests = 0
    for sizes in [(2,2,2), (3,3,3), (3,3,4), (3,4,5), (2,3,5), (5,5,3), (2,2,3), (2,3,3), (3,5,7)]:
        pairs = list(itertools.combinations(range(3), 2))
        odd_pairs = [p for p in pairs if sizes[p[0]] * sizes[p[1]] % 2]
        for vals in itertools.product((-1, 1), repeat=len(odd_pairs)):
            signs = dict(zip(odd_pairs, vals))
            edges, angles = make_links(sizes, signs)
            V = math.prod(sizes)
            action = 0.0
            for x in itertools.product(*(range(L) for L in sizes)):
                for i, j in pairs:
                    P = plaquette(edges, x, i, j, sizes)
                    goal = cmath.exp(1j * angles[(i,j)])
                    assert abs(P-goal) < 2e-11, (sizes,x,i,j,P,goal)
                    action += P.real
                    tests += 1
            target = -V*sum(1.0 if (sizes[i]*sizes[j])%2==0
                            else math.cos(math.pi/(sizes[i]*sizes[j]))
                            for i,j in pairs)
            assert abs(action-target)<4e-10, (sizes, action,target)
    print(f'PASS: {tests} oriented plaquettes; exact global energies for all tested dimensions and flux choices')

if __name__ == '__main__':
    run()
