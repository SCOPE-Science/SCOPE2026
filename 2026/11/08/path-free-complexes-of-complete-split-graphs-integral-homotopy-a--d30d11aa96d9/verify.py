"""Reproduce graph-face, relative-chain, homology and character checks.

Only Python standard library. This finite test accompanies, but does not
replace, the all-parameter mathematical proof in RESULT.md.
"""
from itertools import combinations, permutations, product
from math import comb


def graph(n, r):
    vertices = list(range(n + r))
    adjacent = [set() for _ in vertices]
    for u, v in combinations(vertices, 2):
        if not (u < n and v < n):
            adjacent[u].add(v)
            adjacent[v].add(u)
    return adjacent


def has_path(adjacency, selected, length):
    if len(selected) < length:
        return False
    S = set(selected)
    def visit(last, used, depth):
        if depth == length:
            return True
        for other in adjacency[last] & S:
            if other not in used and visit(other, used | {other}, depth + 1):
                return True
        return False
    return any(visit(vertex, {vertex}, 1) for vertex in selected)


def allowed(p, q, t):
    return min(p + q, 2 * p + 1) < t


def predicted_beta(n, r, t):
    return sum(
        comb(r, p) * comb(n - 1, t - 1 - p)
        for p in range((t // 2), min(r, t - 1) + 1)
        if 0 <= t - 1 - p <= n - 1
    )


def rank_gf2(columns):
    pivots = {}
    for value in columns:
        while value:
            lead = value.bit_length() - 1
            if lead in pivots:
                value ^= pivots[lead]
            else:
                pivots[lead] = value
                break
    return len(pivots)


def reduced_betti(faces, nvertices):
    by_degree = [[f for f in faces if len(f) == j + 1]
                 for j in range(nvertices)]
    ranks = [0]
    for j in range(1, nvertices):
        lower = {f: i for i, f in enumerate(by_degree[j - 1])}
        boundary_columns = [sum(1 << lower[sub]
                                for sub in combinations(face, j))
                            for face in by_degree[j]]
        ranks.append(rank_gf2(boundary_columns))
    ranks.append(0)
    betti = {j: len(by_degree[j]) - ranks[j] - ranks[j + 1]
             for j in range(nvertices)}
    betti[0] -= 1
    return {j: b for j, b in betti.items() if b != 0}


def finite_topology_checks():
    cases = 0
    max_faces = 0
    total_face_tests = 0
    for n in range(2, 6):
        for r in range(2, 6):
            if n + r > 9:
                continue
            adjacency = graph(n, r)
            for t in range(5, min(n + r + 2, 8)):
                vertices = range(n + r)
                faces = [face for length in range(1, n + r + 1)
                         for face in combinations(vertices, length)
                         if not has_path(adjacency, face, t)]
                face_set = set(faces)
                total_face_tests += (1 << (n + r)) - 1
                max_faces = max(max_faces, len(faces))
                for face in faces:
                    p = sum(v >= n for v in face)
                    assert allowed(p, len(face)-p, t)
                # For the fixed leaf v=0, check the star/critical dichotomy
                # against the independent DFS-defined face set.
                critical = []
                for face in faces:
                    if 0 in face:
                        continue
                    if tuple(sorted(face + (0,))) not in face_set:
                        p = sum(v >= n for v in face)
                        assert len(face) == t - 1
                        assert 2 * p + 1 >= t
                        assert all(tuple(sub) in face_set and
                                   tuple(sorted(sub + (0,))) in face_set
                                   for sub in combinations(face, len(face) - 1))
                        critical.append(face)
                expected = predicted_beta(n, r, t)
                assert len(critical) == expected, (n, r, t, len(critical), expected)
                target = {t-2: expected} if expected else {}
                actual = reduced_betti(faces, n+r)
                assert actual == target, (n,r,t,target,actual)
                cases += 1
    return cases, total_face_tests, max_faces


def permutation_cycle_sizes(perm):
    visited = set()
    output = []
    for start in range(len(perm)):
        if start in visited:
            continue
        x = start
        length = 0
        while x not in visited:
            visited.add(x)
            length += 1
            x = perm[x]
        output.append(length)
    return output


def cycle_polynomial_coefficients(perm):
    coefficients = [1]
    for size in permutation_cycle_sizes(perm):
        next_coefficients = coefficients + [0] * size
        for j, value in enumerate(coefficients):
            next_coefficients[j+size] -= value
        coefficients = next_coefficients
    return coefficients


def predicted_character(sigma, tau, t):
    a = cycle_polynomial_coefficients(sigma)
    b = cycle_polynomial_coefficients(tau)
    signed_sum = sum(u*v for p, u in enumerate(a)
                     for q, v in enumerate(b) if allowed(p, q, t))
    return (-1)**(t-1) * signed_sum


def orientation_sign(face, perm):
    mapped = [perm[v] for v in face]
    inversions = sum(mapped[i] > mapped[j]
                     for i in range(len(mapped))
                     for j in range(i+1, len(mapped)))
    return -1 if inversions % 2 else 1


def finite_character_checks():
    cases = 0
    critical_checks = 0
    for n, r in ((2,2),(3,2),(2,3),(3,3),(4,2),(2,4),(3,4)):
        for t in range(5, min(8, n+r+2)):
            N = n+r
            for sigma, tau in product(permutations(range(r)),
                                      permutations(range(n))):
                perm = list(tau) + [n+sigma[j] for j in range(r)]
                actual_alternating = -1  # Reduced augmented degree -1.
                for mask in range(1, 1 << N):
                    face = tuple(v for v in range(N) if mask >> v & 1)
                    p = sum(v >= n for v in face)
                    if not allowed(p, len(face)-p, t):
                        continue
                    if {perm[v] for v in face} != set(face):
                        continue
                    actual_alternating += ((-1)**(len(face)-1)
                                           * orientation_sign(face, perm))
                actual = (-1)**(t-2) * actual_alternating
                predicted = predicted_character(sigma, tau, t)
                assert actual == predicted, (n,r,t,sigma,tau,actual,predicted)
                cases += 1
                # Stabilizer representation from the relative fundamental cycles.
                if tau[0] == 0:
                    relative_trace = 0
                    for p in range(t//2, min(r, t-1)+1):
                        q = t-1-p
                        for H in combinations(range(n, N), p):
                            for L in combinations(range(1, n), q):
                                face = tuple(sorted(H+L))
                                if {perm[v] for v in face} == set(face):
                                    relative_trace += orientation_sign(face, perm)
                    assert relative_trace == predicted
                    critical_checks += 1
    return cases, critical_checks


def full_symmetry_invariant_checks():
    cases = 0
    for n, r, t in ((3,3,5),(4,3,5),(4,4,6),(5,2,5),(5,4,6)):
        total = sum(predicted_character(sigma, tau, t)
                    for sigma, tau in product(permutations(range(r)),
                                              permutations(range(n))))
        assert total == 0
        cases += 1
    return cases


if __name__ == '__main__':
    top, face_tests, max_faces = finite_topology_checks()
    chars, stable = finite_character_checks()
    invariant = full_symmetry_invariant_checks()
    print('GRAPH_DFS_RELATIVE_HOMOLOGY_OK', top, 'cases',
          face_tests, 'vertex-subsets', 'max_faces', max_faces)
    print('SIGNED_CHARACTER_OK', chars, 'automorphisms',
          stable, 'leaf-stabilizer tests')
    print('FULL_INVARIANT_OK', invariant, 'parameter triples')
    print('ALL_VERIFY_OK')
