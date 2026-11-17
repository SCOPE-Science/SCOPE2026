"""Exact integer verification of the cyclic-fixed triangle-free graph complex.

Run: python verify_trianglefree_fixed.py (requires SymPy >=1.12).
All graph orders from 3 through 21 are enumerated exhaustively.
"""
from itertools import combinations
from collections import Counter
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def cyclic_distance(n, a):
    a %= n
    return min(a, n-a)


def forbidden_sets(n):
    return {frozenset((cyclic_distance(n, j-i),
                       cyclic_distance(n, k-j),
                       cyclic_distance(n, k-i)))
            for i, j, k in combinations(range(n), 3)}


def valid_by_triangles(n, D, forbidden):
    A = set(D)
    return all(not T <= A for T in forbidden)


def valid_by_schur(n, D):
    S = {s for d in D for s in (d % n, (-d) % n)}
    return all((x+y) % n not in S for x in S for y in S)


def simplices(n):
    forbidden = forbidden_sets(n)
    vertices = list(range(1, n//2+1))
    faces = {-1: [()]}
    for r in range(1, len(vertices)+1):
        faces[r-1] = []
        for D in combinations(vertices, r):
            a = valid_by_triangles(n, D, forbidden)
            b = valid_by_schur(n, D)
            assert a == b, ('independent predicates disagree', n, D)
            if a:
                faces[r-1].append(D)
    return {i: v for i, v in faces.items() if v}


def boundary_diagonal(faces, degree):
    columns = faces.get(degree, [])
    rows = faces.get(degree-1, [])
    if not columns or not rows:
        return []
    row_index = {face: j for j, face in enumerate(rows)}
    entries = {}
    for col, face in enumerate(columns):
        for j in range(len(face)):
            lower = face[:j]+face[j+1:]
            entries[row_index[lower], col] = (-1)**j
    matrix = SparseMatrix(len(rows), len(columns), entries)
    normal = smith_normal_form(matrix, domain=ZZ)
    return [abs(int(normal[i,i])) for i in range(min(normal.shape)) if normal[i,i]]


def check_surface(faces):
    vertices = {v[0] for v in faces[0]}
    edges = set(faces[1]); triangles = faces[2]
    assert len(vertices) == 9 and len(edges) == 27 and len(triangles) == 18
    edge_counts = Counter(e for t in triangles for e in combinations(t,2))
    assert all(edge_counts[e] == 2 for e in edges)
    assert set(edge_counts) == edges
    for v in vertices:
        link_vertices = {w for e in edges if v in e for w in e if w != v}
        link_edges = {tuple(w for w in t if w != v) for t in triangles if v in t}
        deg = Counter(w for e in link_edges for w in e)
        assert len(link_vertices) == 6 and len(link_edges) == 6
        assert all(deg[w] == 2 for w in link_vertices)
        found = {next(iter(link_vertices))}
        while True:
            more = {w for e in link_edges for w in e if any(x in found for x in e)}
            if more <= found:
                break
            found |= more
        assert found == link_vertices
    found = {next(iter(vertices))}
    while True:
        more = {w for e in edges for w in e if any(x in found for x in e)}
        if more <= found:
            break
        found |= more
    assert found == vertices
    # Test orientability directly, independently of integer Smith reduction.
    adjacency = {t: [] for t in triangles}
    for t in triangles:
        for j in range(3):
            e = t[:j]+t[j+1:]
            adjacent = [u for u in triangles if u != t and set(e) <= set(u)]
            assert len(adjacent) == 1
            u = adjacent[0]
            k = next(k for k in range(3) if u[:k]+u[k+1:] == e)
            adjacency[t].append((u, -((-1)**j)*((-1)**k)))
    orientations = {triangles[0]: 1}
    inconsistent = False
    todo = [triangles[0]]
    while todo:
        t = todo.pop()
        for u, transition in adjacency[t]:
            desired = orientations[t]*transition
            if u in orientations:
                if orientations[u] != desired:
                    inconsistent = True
            else:
                orientations[u] = desired
                todo.append(u)
    assert len(orientations) == len(triangles) and inconsistent
    print('n=21: signed dual-graph orientation transport has a contradiction')
    return True


def main():
    table = []
    for n in range(3,22):
        faces = simplices(n)
        dims = sorted(d for d in faces if d>=0)
        diag = {d:boundary_diagonal(faces,d) for d in dims if d>0}
        bad = [(d, v) for d, vals in diag.items() for v in vals if v != 1]
        ranks = {d:len(diag[d]) for d in diag}
        if n < 21:
            assert not bad, ('unexpected torsion', n, bad)
        else:
            assert bad == [(2,2)], bad
            assert [len(faces.get(d, [])) for d in (0,1,2,3)] == [9,27,18,0]
            assert diag[1] == [1]*8
            assert sorted(diag[2]) == [1]*17+[2]
            check_surface(faces)
            print('n=21 facets:', ' '.join(str(t) for t in faces[2]))
            print('n=21: connected closed 9-vertex surface, each link a 6-cycle')
            print('n=21: SNF boundary_1 = 1^8; boundary_2 = 1^17, 2')
        betti = {d:len(faces.get(d,[])) - ranks.get(d,0)-ranks.get(d+1,0)
                 for d in dims}
        if 0 in betti:
            betti[0] -= 1
        table.append((n, [len(faces.get(d,[])) for d in dims],
                      {d:v for d,v in betti.items() if v}, bad))
    for n, fvector, betti, bad in table:
        print(f'n={n}: fvector={fvector}; free reduced betti={betti}; '
              f'nonunit boundary Smith factors={bad}')
    print('TRIANGLE_FREE_CYCLIC_FIXED_INTEGRAL_21_PASS')

if __name__ == '__main__':
    main()
