"""Finite exact checks for critical cycle-power Vietoris--Rips characters.

Reconstructs the flag complex from graph adjacency using a standalone
Bron--Kerbosch maximal-clique search and enumerates all its faces. No packages
beyond Python's standard library are required. All tests are finite tests;
the general theorem is proved separately by a uniform cellular argument.
"""
from itertools import combinations


def inversion_sign(values):
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i + 1, len(values))) % 2 else 1


def maximal_cliques(adjacency):
    """Enumerate maximal cliques using pivoted Bron--Kerbosch."""
    maxima = []
    def recur(R, P, X):
        if not P and not X:
            maxima.append(frozenset(R))
            return
        if P or X:
            pivot = max(P | X, key=lambda u: len(P & adjacency[u]))
            choices = sorted(P - adjacency[pivot])
        else:
            choices = []
        for v in choices:
            recur(R | {v}, P & adjacency[v], X & adjacency[v])
            P.remove(v)
            X.add(v)
    recur(set(), set(adjacency), set())
    return set(maxima)


def all_nonempty_faces(maxima):
    return {t for clique in maxima for size in range(1, len(clique) + 1)
            for t in combinations(sorted(clique), size)}


def equivariant_reduced_lefschetz(faces, transform):
    ans = -1
    for simplex in faces:
        image = [transform[v] for v in simplex]
        if set(image) == set(simplex):
            indices = {v:i for i, v in enumerate(simplex)}
            ans += (-1)**(len(simplex) - 1) * inversion_sign(
                [indices[w] for w in image])
    return ans


def verify(k):
    n = 3 * k
    adjacency = {i: {j for j in range(n) if j != i
                      and min((i-j) % n, (j-i) % n) <= k}
                 for i in range(n)}
    maxima = maximal_cliques(adjacency)
    # Predicted maximal cliques: 3k consecutive (k+1)-sets and k triangles.
    arc_max = {frozenset((i + a) % n for a in range(k + 1))
               for i in range(n)}
    exceptional = {frozenset((j, j+k, j+2*k)) for j in range(k)}
    assert maxima == arc_max | exceptional, (k, maxima ^ (arc_max | exceptional))
    faces = all_nonempty_faces(maxima)
    arc_faces = all_nonempty_faces(arc_max)
    assert faces - arc_faces == {tuple(sorted(t)) for t in exceptional}
    assert sum((-1)**(len(s)-1) for s in arc_faces) - 1 == -1
    assert sum((-1)**(len(s)-1) for s in faces) - 1 == k - 1
    for a in range(n):
        for reflected in (False, True):
            transform = {i: (a-i if reflected else a+i) % n
                         for i in range(n)}
            assert all(transform[j] in adjacency[transform[i]]
                       for i in range(n) for j in adjacency[i])
            lefschetz = equivariant_reduced_lefschetz(faces, transform)
            if reflected:
                fixed = sum(2*j % k == a % k for j in range(k))
                expected = 1 - fixed
            else:
                expected = k-1 if a % k == 0 else -1
            assert lefschetz == expected, (k, a, reflected, lefschetz, expected)
    return len(faces), len(arc_faces), len(maxima), 2*n


if __name__ == '__main__':
    for k in range(2, 9):
        nf, na, mc, nauts = verify(k)
        print(f'k={k} vertices={3*k} faces={nf} arc_faces={na} '
              f'maximal_cliques={mc} checked_actions={nauts}')
    print('CRITICAL_CYCLE_INTEGRAL_DIHEDRAL_CHARACTER_PASS')
