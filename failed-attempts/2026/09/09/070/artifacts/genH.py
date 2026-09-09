"""H = stabilizer of l*=span(e1,e2) in PGL(4,7): generators, BFS orbits, matrix.

H = block upper-triangular [[A,B],[0,D]] (A,D in GL(2,7), B in M2(7)) modulo
scalars. Generators act on F7^4 column vectors; induced action on normalized
points and on lines (2-spaces). BFS verifies:
  point orbits: 8 (on l*) + 392 (off)
  line orbits: 1 (l*) + 448 (concurrent) + 2401 (skew)
Meeting matrix re-verified per line (no transitivity assumed for numbers).
"""
import itertools
from collections import deque

Q = 7

def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) % Q for i in range(4))

def norm_point(v):
    for c in v:
        if c % Q != 0:
            inv = pow(c, -1, Q)
            return tuple((x * inv) % Q for x in v)
    raise ValueError

def all_points():
    pts = set()
    for v in itertools.product(range(Q), repeat=4):
        if any(v):
            pts.add(norm_point(v))
    return sorted(pts)

def line_key(a, b):
    pts = set()
    for s in range(Q):
        for t in range(Q):
            if s or t:
                pts.add(norm_point(tuple((s * x + t * y) % Q for x, y in zip(a, b))))
    assert len(pts) == Q + 1
    return tuple(sorted(pts))

def I4():
    return [[1 if i == j else 0 for j in range(4)] for i in range(4)]

def shear(i, j, c=1):
    # e_i += c*e_j  (adds c*coord_j to coord_i): preserves l* iff not (i in {2,3} and j in {0,1})
    M = I4(); M[i][j] = (M[i][j] + c) % Q; return M

def swap(i, j):
    M = I4(); M[i], M[j] = M[j], M[i]; return M

def diag(i, c):
    M = I4(); M[i][i] = c % Q; return M

# A-block GL(2) on coords 0,1 ; D-block GL(2) on coords 2,3 ; B-block shears 0,1 += coords 2,3
GENS = [
    swap(0, 1), diag(0, 3), shear(0, 1),          # A-block: GL(2,7)
    swap(2, 3), diag(2, 3), shear(2, 3),          # D-block: GL(2,7)
    shear(0, 2), shear(0, 3), shear(1, 2), shear(1, 3),  # B-block
]
NAMES = ["sw01", "dg0", "sh01", "sw23", "dg2", "sh23",
         "sh02", "sh03", "sh12", "sh13"]

def main():
    points = all_points()
    assert len(points) == 400
    pidx = {p: i for i, p in enumerate(points)}
    # action of generators on point indices
    gact = []
    for M in GENS:
        gact.append([pidx[norm_point(mat_vec(M, v))] for v in points])

    def orbits(n, act):
        seen = [-1] * n
        norb = 0
        for s in range(n):
            if seen[s] == -1:
                dq = deque([s]); seen[s] = norb
                while dq:
                    u = dq.popleft()
                    for g in act:
                        w = g[u]
                        if seen[w] == -1:
                            seen[w] = norb; dq.append(w)
                norb += 1
        return seen, norb

    porb, np = orbits(400, gact)
    from collections import Counter
    print("point orbit sizes:", sorted(Counter(porb).values()))
    assert sorted(Counter(porb).values()) == [8, 392]

    # lines
    lines = sorted({line_key(points[i], points[j])
                    for i in range(400) for j in range(i + 1, 400)
                    if line_key(points[i], points[j])})
    assert len(lines) == 2850, len(lines)
    lidx = {L: i for i, L in enumerate(lines)}
    # generator action on lines: image of spanning pair
    lact = []
    for M in GENS:
        mp = [pidx[norm_point(mat_vec(M, v))] for v in points]
        def img(L):
            a = points[mp[points.index(L[0])]] if False else None
            return None
        # map via point images of the 8 points
        perm = []
        for L in lines:
            a = points[mp[pidx[L[0]]]]
            # find second image point distinct from first
            for p in L[1:]:
                b = points[mp[pidx[p]]]
                if b != a:
                    break
            perm.append(lidx[line_key(a, b)])
        lact.append(perm)
    lorb, nl = orbits(2850, lact)
    print("line orbit sizes:", sorted(Counter(lorb).values()))
    assert sorted(Counter(lorb).values()) == [1, 448, 2401]

    e1 = (1, 0, 0, 0); e2 = (0, 1, 0, 0)
    lstar = line_key(e1, e2)
    assert lorb[lidx[lstar]] == lorb[lidx[lstar]]
    # l* orbit is the singleton
    assert Counter(lorb)[lorb[lidx[lstar]]] == 1
    print("l* lies in singleton orbit: OK")

    # meeting matrix (per-line verified, independent of generators)
    pt_lines = {p: [] for p in points}
    for i, L in enumerate(lines):
        for p in L:
            pt_lines[p].append(i)
    import functools
    sizes = sorted(Counter(lorb).values())  # [1,448,2401]
    # map orbit id -> column by size order
    ids = sorted(set(lorb), key=lambda o: Counter(lorb)[o])
    assert [Counter(lorb)[o] for o in ids] == [1, 448, 2401]
    mat = {}
    for L in lines:
        o = lorb[lidx[L]]
        seen = set()
        for p in L:
            seen.update(pt_lines[p])
        seen.discard(lidx[L])
        row = tuple(sum(1 for s in seen if lorb[s] == oo) for oo in ids)
        assert sum(row) == 448, row
        if o in mat:
            assert mat[o] == row, (o, mat[o], row)
        else:
            mat[o] = row
    print("meeting matrix rows (orbits size 1,448,2401):")
    for o in ids:
        print("  n=%d row=%s" % (Counter(lorb)[o], mat[o]))
    assert [mat[o] for o in ids] == [(0, 448, 0), (1, 104, 343), (0, 64, 384)]
    print("H-ORBIT VERIFICATION PASSED")
    # log generators
    import json
    json.dump({"generators": GENS, "names": NAMES,
               "point_orbits": [8, 392], "line_orbits": [1, 448, 2401],
               "meeting": [[0, 448, 0], [1, 104, 343], [0, 64, 384]]},
              open("output/artifacts/H_orbits.json", "w"))

if __name__ == "__main__":
    main()
