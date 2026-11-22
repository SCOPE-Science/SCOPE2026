"""Independent finite certificate checker for two-punctured Hamming Rips complexes.
Requires Python 3.9+ standard library only; run with morse_cases.json.gz alongside.
A pair step removes a free face and its unique maximal coface; a critical
step removes one maximal face. This peeling is an acyclic discrete Morse
matching (reverse filtration prohibits directed gradient cycles).
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import gzip
import json


def all_hamming_cliques(n, d):
    """Enumerate every nonempty clique by lexicographic extension, not maximal cliques."""
    v = [i for i in range(1 << n) if i not in (0, (1 << d) - 1)]
    neighbor = {i: {j for j in v if j != i and (i ^ j).bit_count() <= 2}
                for i in v}
    faces = set()
    def extend(prefix, later):
        for k, u in enumerate(later):
            face = prefix + (u,)
            assert face not in faces
            faces.add(face)
            extend(face, [w for w in later[k+1:] if w in neighbor[u]])
    extend((), v)
    return faces


def verify_case(case):
    n, d = case['n'], case['d']
    assert 3 <= n <= 6 and 1 <= d <= n
    faces = all_hamming_cliques(n, d)
    assert len(faces) == case['face_count']
    cofaces = {face: set() for face in faces}
    for face in faces:
        for j in range(len(face)) if len(face)>1 else ():
            lower = face[:j] + face[j+1:]
            assert lower in faces
            cofaces[lower].add(face)
    live = set(faces)
    critical = Counter()
    for op in case['operations']:
        assert op[0] in ('p', 'c')
        cells = [tuple(x) for x in op[1:]]
        assert all(c in live and tuple(sorted(set(c))) == c for c in cells)
        if op[0] == 'p':
            assert len(cells) == 2
            small, big = cells
            assert len(big) == len(small) + 1
            assert set(small).issubset(big)
            assert cofaces[small] == {big}, (n,d,'not unique',op)
            assert not cofaces[big], (n,d,'not maximal',op)
        else:
            assert len(cells) == 1
            assert not cofaces[cells[0]], (n,d,'critical not maximal',op)
            critical[len(cells[0])-1] += 1
        for face in cells:
            assert face in live
            live.remove(face)
            for j in range(len(face)) if len(face)>1 else ():
                lower = face[:j] + face[j+1:]
                if lower in live:
                    cofaces[lower].remove(face)
    assert not live, (n,d,'unremoved',len(live))
    observed = {str(k):v for k,v in critical.items()}
    assert observed == case['critical_dimensions']
    assert critical[0] == 1
    if n == 3:
        assert critical == (Counter({0:1,2:1}) if d == 3 else Counter({0:1}))
    else:
        ranks = {4:(3,1),5:(32,29),6:(173,169)}
        b = ranks[n][0] if d <= 2 else ranks[n][1]
        assert critical == Counter({0:1,3:b})
    return n,d,len(faces),dict(sorted(critical.items()))


def main():
    p = Path(__file__).resolve().parent/'morse_cases.json.gz'
    doc = json.loads(gzip.decompress(p.read_bytes()))
    assert doc['format'] == 'free-face-critical-facet-peeling-v1' and doc['scale'] == 2
    assert {(c['n'],c['d']) for c in doc['cases']} == {(n,d) for n in range(3,7) for d in range(1,n+1)}
    total = 0
    for c in doc['cases']:
        n,d,f,crit = verify_case(c)
        total += f
        print(f'n={n} distance={d} faces={f} critical={crit}')
    print(f'PASS: {len(doc["cases"])} pair-orbit cases; {total} face occurrences; exhaustive free-face/critical-facet certificate verified')

if __name__ == '__main__':
    main()
