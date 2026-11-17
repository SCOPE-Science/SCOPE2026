"""Verify an exact discrete-Morse certificate for a finite torus-grid Rips complex.

Run: python3 VERIFY.py CERTIFICATE.json
Requires Python 3.9+ standard library only.
"""
import collections
import functools
import json
import sys


def dim(m):
    return m.bit_count()-1


def faces(n, radius):
    pts = [(i, j) for i in range(n) for j in range(n)]
    adjacency = []
    for i, (x, y) in enumerate(pts):
        edges = 0
        for j, (a, b) in enumerate(pts):
            if i == j:
                continue
            dx = min(abs(x-a), n-abs(x-a))
            dy = min(abs(y-b), n-abs(y-b))
            if dx+dy <= radius:
                edges |= (1 << j)
        adjacency.append(edges)
    result = set()
    def visit(simplex, candidates):
        if simplex:
            result.add(simplex)
        while candidates:
            b = candidates & -candidates
            candidates -= b
            j = b.bit_length()-1
            visit(simplex | b, candidates & adjacency[j])
    visit(0, (1 << (n*n))-1)
    return result


def codim_one_faces(m):
    bits = m
    while bits:
        b = bits & -bits
        bits -= b
        yield m ^ b


def upper_neighbors(m, active, allbits):
    missing = allbits ^ m
    while missing:
        b = missing & -missing
        missing -= b
        coface = m | b
        if coface in active:
            yield coface


def boundary_sign(f, g):
    b = g ^ f
    assert b.bit_count() == 1 and (g & f) == f
    return -1 if ((g & (b-1)).bit_count() % 2) else 1


def verify(cert):
    assert cert['schema_version'] == 1
    n = cert['torus_side']; radius = cert['inclusive_radius']
    assert (n, radius) == (7, 3)
    original = faces(n, radius)
    counts = dict(sorted(collections.Counter(dim(f) for f in original).items()))
    expected = {int(k): v for k, v in cert['f_vector'].items()}
    assert counts == expected, (counts, expected)
    active = set(original)
    allbits = (1 << n*n)-1
    matching = {}
    critical = []
    pairs = 0
    for event in cert['events']:
        if event[0] == 0:
            assert len(event) == 3
            f, g = event[1:]
            assert f in active and g in active and (g & f) == f and dim(g) == dim(f)+1
            assert list(upper_neighbors(f, active, allbits)) == [g], ('not a free face', f, g)
            assert not list(upper_neighbors(g, active, allbits)), ('upper cell not maximal', f, g)
            matching[f] = ('up', g)
            matching[g] = ('down', f)
            active.remove(g)
            active.remove(f)
            pairs += 1
        else:
            assert event[0] == 1 and len(event) == 2
            m = event[1]
            assert m in active
            assert not list(upper_neighbors(m, active, allbits)), ('critical face not maximal', m)
            critical.append(m)
            active.remove(m)
    assert not active
    assert len(original) == 2*pairs + len(critical)
    critical_counts = dict(sorted(collections.Counter(dim(f) for f in critical).items()))
    assert critical_counts == {0:1, 3:1, 4:14}
    critical_three = [f for f in critical if dim(f)==3]
    critical_four = [f for f in critical if dim(f)==4]
    assert len(critical_three)==1 and len(critical_four)==14

    # Evaluate the integral Morse differential by signed gradient-path recursion.
    # A matched lower three-face is replaced by the signed sum of the
    # other three-faces in its matched upper four-face.
    visiting = set()
    @functools.lru_cache(maxsize=None)
    def project_three(m):
        if m==critical_three[0]:
            return 1
        status, other = matching[m]
        if status == 'down':
            return 0
        assert m not in visiting
        visiting.add(m)
        g = other
        result = -boundary_sign(m, g) * sum(
            boundary_sign(f, g)*project_three(f)
            for f in codim_one_faces(g) if f != m
        )
        visiting.remove(m)
        return result
    degrees = []
    for c in critical_four:
        degree = sum(boundary_sign(f, c)*project_three(f) for f in codim_one_faces(c))
        degrees.append(degree)
    assert degrees == [0]*14, degrees
    return {'vertices': n*n, 'face_vector': counts,
            'pair_count': pairs, 'critical_counts': critical_counts,
            'critical_vertex': next(m for m in critical if dim(m)==0),
            'critical_three_cell': critical_three[0],
            'critical_four_cells': critical_four,
            'integral_morse_boundary_four_to_three': degrees,
            'gradient_three_faces_visited': project_three.cache_info().currsize}


def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python3 VERIFY.py CERTIFICATE.json')
    with open(sys.argv[1], encoding='utf-8') as fp:
        cert = json.load(fp)
    result = verify(cert)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
    print('VERIFIED: exact Morse certificate; homotopy type S^3 wedge 14 S^4')

if __name__=='__main__':
    main()
