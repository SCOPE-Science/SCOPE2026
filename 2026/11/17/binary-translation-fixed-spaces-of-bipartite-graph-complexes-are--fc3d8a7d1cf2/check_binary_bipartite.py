"""Finite reproducibility checks for binary-translation bipartite graph fixed spaces."""
from collections import defaultdict, deque
from math import prod


def gaussian(n, k):
    if k < 0 or k > n:
        return 0
    v = 1
    for i in range(k):
        v = v * (2 ** (n - i) - 1) // (2 ** (i + 1) - 1) if False else v
    num = prod(2 ** (n - i) - 1 for i in range(k))
    den = prod(2 ** (k - i) - 1 for i in range(k))
    assert num % den == 0
    return num // den


def sphere_counts(limit=6):
    mu = [1]
    nums = {}
    for k in range(1, limit + 1):
        mk = -1 - sum((gaussian(k, j) - gaussian(k - 1, j)) * mu[j] for j in range(1, k))
        mu.append(mk)
        s = 1 + sum(gaussian(k, j) * (2 ** j - 1) * mu[j] for j in range(1, k + 1))
        nums[k] = (-1) ** k * s
    return mu, nums


def facet_faces(r):
    n = 1 << r
    facets = [sum(1 << (v - 1) for v in range(1, n) if (a & v).bit_count() % 2)
              for a in range(1, n)]
    all_faces = {0}
    for f in facets:
        s = f
        while s:
            all_faces.add(s)
            s = (s - 1) & f
    return facets, all_faces


def graph_bipartite(r, mask):
    """Construct all *edges* of each chosen translation edge orbit and 2-color."""
    n = 1 << r
    graph = [[] for _ in range(n)]
    for v in range(1, n):
        if mask >> (v - 1) & 1:
            for x in range(n):
                graph[x].append(x ^ v)
    color = [-1] * n
    for x in range(n):
        if color[x] != -1:
            continue
        color[x] = 0
        stack = [x]
        while stack:
            y = stack.pop()
            for z in graph[y]:
                if color[z] == -1:
                    color[z] = 1 - color[y]
                    stack.append(z)
                elif color[z] == color[y]:
                    return False
    return True


def mod2_rank(columns):
    pivots = {}
    for v in columns:
        while v:
            top = v.bit_length() - 1
            if top in pivots:
                v ^= pivots[top]
            else:
                pivots[top] = v
                break
    return len(pivots)


def homology(faces):
    bydim = defaultdict(list)
    for face in faces:
        if face:
            bydim[face.bit_count() - 1].append(face)
    upper = max(bydim)
    ranks = {}
    for j in range(1, upper + 1):
        labels = {f: i for i, f in enumerate(bydim[j - 1])}
        columns = []
        for f in bydim[j]:
            v, boundary = f, 0
            while v:
                one = v & -v
                v ^= one
                boundary ^= 1 << labels[f ^ one]
            columns.append(boundary)
        ranks[j] = mod2_rank(columns)
    beta = {}
    for j in range(upper + 1):
        down = 1 if j == 0 else ranks[j]
        up = ranks.get(j + 1, 0)
        beta[j] = len(bydim[j]) - down - up
    return [len(bydim[j]) for j in range(upper + 1)], {j: v for j, v in beta.items() if v}


def main():
    mu, counts = sphere_counts(6)
    assert mu[:6] == [1, -1, 1, -3, 21, -315], mu
    assert [counts[i] for i in range(1, 6)] == [0, 1, 6, 91, 2820]
    print('mobius=' + str(mu))
    print('sphere_multiplicities=' + str(counts))
    expected = {1: {}, 2: {1: 1}, 3: {2: 6}, 4: {3: 91}}
    for r in range(1, 5):
        facets, faces = facet_faces(r)
        n = 1 << r
        # Independent verification by constructing graph edge sets, with no linear functionals.
        for face in range(1 << (n - 1)):
            assert graph_bipartite(r, face) == (face in faces), (r, face)
        f, beta = homology(faces)
        assert beta == expected[r], (r, beta)
        if r >= 2:
            assert max(beta) == r - 1
            assert beta[r - 1] == counts[r]
        print(f'rank={r} graph_masks={1 << (n-1)} faces={len(faces)} f_vector={f} reduced_mod2_betti={beta}')
    print('BINARY_TRANSLATION_BIPARTITE_FIXED_CHECKS_PASS')


if __name__ == '__main__':
    main()
