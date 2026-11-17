#!/usr/bin/env python3
"""Exact integer chain verifier for small unlabeled directed-forest quotients.

Requirements: Python 3.10+ and SymPy. No internet or stored input data needed.
Usage: python verify.py
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def verify(n):
    arcs = tuple((a, b) for a in range(n) for b in range(n) if a != b)
    position = {arc: i for i, arc in enumerate(arcs)}
    actions = tuple(tuple(position[(p[a], p[b])] for a, b in arcs)
                    for p in permutations(range(n)))

    def moved(mask, action):
        result = 0
        while mask:
            low = mask & -mask
            result |= 1 << action[low.bit_length() - 1]
            mask -= low
        return result

    def is_forest(mask):
        parent = {}
        for i, (a, b) in enumerate(arcs):
            if mask & (1 << i):
                if b in parent:
                    return False
                parent[b] = a
        for start in range(n):
            v = start
            seen = {v}
            while v in parent:
                v = parent[v]
                if v in seen:
                    return False
                seen.add(v)
        return True

    faces = [[] for _ in range(n)]
    for size in range(1, n):
        for combination in combinations(range(len(arcs)), size):
            mask = sum(1 << i for i in combination)
            if is_forest(mask):
                faces[size].append(mask)

    @lru_cache(None)
    def canonical(flag):
        return min(tuple(moved(face, p) for face in flag) for p in actions)

    levels = [sorted({canonical((face,)) for part in faces for face in part})]
    for dim in range(1, n - 1):
        following = set()
        for flag in levels[-1]:
            last = flag[-1]
            for size in range(last.bit_count() + 1, n):
                for larger in faces[size]:
                    if larger & last == last:
                        following.add(canonical(flag + (larger,)))
        if not following:
            break
        levels.append(sorted(following))

    boundary = []
    for dim in range(1, len(levels)):
        index = {flag: i for i, flag in enumerate(levels[dim - 1])}
        mat = [[0] * len(levels[dim]) for _ in levels[dim - 1]]
        for col, flag in enumerate(levels[dim]):
            for k in range(len(flag)):
                mat[index[canonical(flag[:k] + flag[k + 1:])]][col] += (-1) ** k
        boundary.append(Matrix(mat))
    for d in range(len(boundary) - 1):
        assert boundary[d] * boundary[d + 1] == Matrix.zeros(*(
            boundary[d].rows, boundary[d + 1].cols))

    diagonal = []
    for mat in boundary:
        smith = smith_normal_form(mat, domain=ZZ)
        diagonal.append([abs(int(smith[i, i])) for i in range(min(smith.shape))
                         if smith[i, i]])
    ranks = [len(diag) for diag in diagonal]
    betti = [len(c) - (ranks[d - 1] if d else 0) -
             (ranks[d] if d < len(ranks) else 0)
             for d, c in enumerate(levels)]

    # Independent signed Burnside-Lefschetz Euler check on original faces.
    original_faces = [x for part in faces for x in part]
    euler_sum = 0
    for action in actions:
        local = 0
        for face in original_faces:
            if moved(face, action) != face:
                continue
            selected = [j for j in range(len(arcs)) if face & (1 << j)]
            image = [action[j] for j in selected]
            ordinal = {j: i for i, j in enumerate(selected)}
            permuted = [ordinal[j] for j in image]
            inversions = sum(permuted[i] > permuted[j] for i in range(len(permuted))
                             for j in range(i + 1, len(permuted)))
            local += (-1) ** (len(selected) - 1 + inversions)
        euler_sum += local
    assert euler_sum % len(actions) == 0
    euler_burnside = euler_sum // len(actions)
    euler_chain = sum((-1) ** d * len(c) for d, c in enumerate(levels))
    assert euler_burnside == euler_chain

    assert all(all(factor == 1 for factor in ds) for ds in diagonal)
    target = {2: ([1], [1]),
              3: ([3, 3], [1, 1]),
              4: ([8, 22, 16], [1, 0, 1]),
              5: ([19, 121, 226, 125], [1, 0, 0, 2])}
    assert ([len(c) for c in levels], betti) == target[n]
    return {'n': n, 'simplices_in_quotient_by_dimension': [len(x) for x in levels],
            'boundary_ranks': ranks,
            'smith_nonzero_factor_counts': [dict(Counter(a)) for a in diagonal],
            'integral_betti': betti,
            'euler_burnside': euler_burnside}


if __name__ == '__main__':
    for n in (2, 3, 4, 5):
        print(verify(n))
    print('ALL EXACT CHECKS PASSED')
