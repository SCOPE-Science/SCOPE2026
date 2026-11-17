"""Exact orbit certificate for vertex triples of the regular 600-cell.

Run: python3 check_600cell.py. No third-party dependencies. All arithmetic
lies in the ring Z[phi] with phi^2=phi+1; coordinates are twice vertices.
"""
import itertools
from collections import Counter, defaultdict, deque


def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])


def times(a, b):
    return (a[0]*b[0]+a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1])


def dot(v, w):
    z = (0, 0)
    for a, b in zip(v, w):
        z = plus(z, times(a, b))
    return z


def scalar(a, sign):
    return (sign*a[0], sign*a[1])


def vertices():
    zero, one, two, phi, phiinverse = (0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)
    out = set()
    for k in range(4):
        for s in (-1, 1):
            x = [zero]*4
            x[k] = scalar(two, s)
            out.add(tuple(x))
    for ss in itertools.product((-1, 1), repeat=4):
        out.add(tuple(scalar(one, s) for s in ss))
    for p in itertools.permutations(range(4)):
        if sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2:
            continue
        for ss in itertools.product((-1, 1), repeat=3):
            x = [zero, scalar(one, ss[0]), scalar(phi, ss[1]), scalar(phiinverse, ss[2])]
            out.add(tuple(x[i] for i in p))
    return sorted(out)


def reflection(a, verts, idx):
    """For doubled roots with squared norm four: x -> x-(x.a)a/2."""
    perm = []
    for x in verts:
        x_a = dot(x, a)
        v = []
        for xi, ai in zip(x, a):
            prod = times(x_a, ai)
            pair = (2*xi[0]-prod[0], 2*xi[1]-prod[1])
            assert pair[0] % 2 == 0 and pair[1] % 2 == 0
            v.append((pair[0]//2, pair[1]//2))
        perm.append(idx[tuple(v)])
    return tuple(perm)


def simple_generators(verts, idx):
    # For the H4 Coxeter diagram 5-3-3, the simple-root inner products
    # in doubled coordinates are -2phi, -2, -2, with non-neighboring 0.
    for ai, a in enumerate(verts):
        for bi, b in enumerate(verts):
            if dot(a, b) != (0, -2):
                continue
            for ci, c in enumerate(verts):
                if dot(b, c) != (-2, 0) or dot(a, c) != (0, 0):
                    continue
                for di, d in enumerate(verts):
                    if (dot(c, d) == (-2, 0) and dot(b, d) == (0, 0)
                            and dot(a, d) == (0, 0)):
                        return tuple(reflection(verts[i], verts, idx) for i in (ai, bi, ci, di))
    raise AssertionError('H4 simple roots not found')


def full_group(generators, n):
    identity = tuple(range(n))
    all_group = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for s in generators:
            h = tuple(g[s[i]] for i in range(n))
            if h not in all_group:
                all_group.add(h)
                queue.append(h)
    return all_group


def triple_orbits(generators, n):
    remaining = set(itertools.combinations(range(n), 3))
    orbits = []
    while remaining:
        root = min(remaining)
        queue = deque([root])
        remaining.remove(root)
        count = 0
        while queue:
            x = queue.popleft()
            count += 1
            for s in generators:
                y = tuple(sorted((s[x[0]], s[x[1]], s[x[2]])))
                if y in remaining:
                    remaining.remove(y)
                    queue.append(y)
        orbits.append((root, count))
    return orbits


def run():
    v = vertices()
    assert len(v) == 120 and set(dot(x, x) for x in v) == {(4, 0)}
    idx = {x:i for i, x in enumerate(v)}
    simple = simple_generators(v, idx)
    group = full_group(simple, 120)
    assert len(group) == 14400

    u = idx[((2,0),(0,0),(0,0),(0,0))]
    stab = [g for g in group if g[u] == u]
    assert len(stab) == 120
    layer_orbits = []
    remaining = set(range(120)) - {u}
    while remaining:
        w = min(remaining)
        orb = {g[w] for g in stab}
        assert len({dot(v[u], v[i]) for i in orb}) == 1
        remaining.difference_update(orb)
        layer_orbits.append((dot(v[u], v[w]), len(orb)))
    assert len(layer_orbits) == 8 and len({z for z, _ in layer_orbits}) == 8, ('not two-point homogeneous', layer_orbits)

    triples = triple_orbits(simple, 120)
    assert len(triples) == 56 and sum(s for _,s in triples) == 280840
    signatures = set()
    exceptional = []
    catalogue = []
    for tri, size in triples:
        sig = tuple(sorted((dot(v[tri[0]], v[tri[1]]),
                            dot(v[tri[0]], v[tri[2]]),
                            dot(v[tri[1]], v[tri[2]]))))
        assert sig not in signatures, ('same metric, different orbits', sig)
        signatures.add(sig)
        permutations = [pi for pi in itertools.permutations(range(3))
                        if all(dot(v[tri[i]], v[tri[j]]) ==
                               dot(v[tri[pi[i]]], v[tri[pi[j]]])
                               for i in range(3) for j in range(i+1, 3))]
        inducing = set()
        pointwise = 0
        for g in group:
            image = tuple(g[z] for z in tri)
            if image == tri:
                pointwise += 1
            if set(image) == set(tri):
                inducing.add(tuple(tri.index(z) for z in image))
        assert size == len(group) // (len(inducing) * pointwise)
        missing = set(permutations) - inducing
        if missing:
            exceptional.append((tri, size, sig, pointwise, len(inducing), len(permutations)))
        catalogue.append((tri, sig, size, len(permutations), len(inducing), pointwise))
    assert len(signatures) == 56
    assert len(exceptional) == 1 and exceptional[0][1:]==(2400, ((0,0),(0,0),(0,0)), 2,3,6), exceptional
    assert all(a==b for _,_,_,a,b,_ in catalogue if a!=6 or b!=3)

    # Direct parity witness: orthogonal coordinate-axis triple, whose swapping
    # two axes cannot preserve the 96 even-permutation vertices.
    a = idx[((2,0),(0,0),(0,0),(0,0))]
    b = idx[((0,0),(2,0),(0,0),(0,0))]
    c = idx[((0,0),(0,0),(2,0),(0,0))]
    assert all(dot(v[x],v[y])==(0,0) for x,y in ((a,b),(a,c),(b,c)))
    assert not any(g[a]==b and g[b]==a and g[c]==c for g in group)
    print('600_CELL_TRIPLES_PASS vertices=120 group=14400 two_point_shells=8 '
          'triangles=280840 orbits=56 distance_signatures=56 '
          'exceptional_orthogonal_orbit=2400 induced_C3=1')
    return catalogue

if __name__=='__main__':
    run()
