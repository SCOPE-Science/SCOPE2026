"""Reproducible homotopy certificate for the 2-tolerance of three disjoint filled triangles.

No non-standard Python packages are needed. Run as: python tolerance_three_triangles_checker.py
"""
from collections import Counter, defaultdict, deque

# Vertices are labelled 0..8, with filled triangle facets 012, 345 and 678.
BLOCKS = (0b000000111, 0b000111000, 0b111000000)
ORDER = (0, 6, 1, 4, 8, 7, 5, 2, 3)

def bit_faces():
    return [s for s in range(1, 1 << 9) if any((s & ~b).bit_count() <= 2 for b in BLOCKS)]

def boundary(s):
    return {s ^ (1 << i): (-1 if j % 2 else 1)
            for j, i in enumerate(i for i in range(9) if s & (1 << i))}

def lex_matching(faces):
    unmatched = set(faces)
    pairs = []
    for vertex in ORDER:
        bit = 1 << vertex
        for s in faces:
            if s in unmatched and not s & bit and s | bit in unmatched:
                hi = s | bit
                unmatched.remove(s)
                unmatched.remove(hi)
                pairs.append((s, hi))
    return pairs, unmatched

def certify_acyclic(faces, pairs):
    paired = set(pairs)
    adjacency = {f: [] for f in faces}
    indegree = {f: 0 for f in faces}
    for hi in faces:
        for lo in boundary(hi):
            if lo == 0: continue
            src, dst = (lo, hi) if (lo, hi) in paired else (hi, lo)
            adjacency[src].append(dst)
            indegree[dst] += 1
    q = deque(v for v in faces if indegree[v] == 0)
    seen = 0
    while q:
        v = q.popleft(); seen += 1
        for w in adjacency[v]:
            indegree[w] -= 1
            if indegree[w] == 0: q.append(w)
    assert seen == len(faces), ('gradient cycle',seen,len(faces))
    return sum(len(v) for v in adjacency.values())

def morse_boundary(pairs, critical):
    # Compute degree-4 to degree-3 Morse boundary by exact integral
    # gradient-path elimination. Its lower-to-upper incidence is +/-1.
    low_to_high = {lo: hi for lo, hi in pairs if lo.bit_count() == 4}
    critical_3 = set(s for s in critical if s.bit_count() == 4)
    critical_4 = sorted(s for s in critical if s.bit_count() == 5)
    results = {}
    for hi in critical_4:
        vec = defaultdict(int, boundary(hi))
        steps = 0
        while True:
            lower = next((s for s,c in vec.items() if c and s in low_to_high), None)
            if lower is None: break
            higher = low_to_high[lower]
            delta = boundary(higher)
            assert delta[lower] in (-1,1)
            scalar = vec[lower] * delta[lower]
            for s,c in delta.items(): vec[s] -= scalar*c
            steps += 1
            assert steps <= 10000
        assert all(c==0 for s,c in vec.items() if s not in critical_3)
        results[hi] = {s:c for s,c in vec.items() if c != 0}
    assert all(not v for v in results.values()), results
    return results

def mod2_rank(columns):
    pivot = {}
    for col in columns:
        x = col
        while x:
            top = x.bit_length()-1
            if top in pivot: x ^= pivot[top]
            else:
                pivot[top] = x
                break
    return len(pivot)

def independent_homology(faces):
    fsets = {d: sorted(s for s in faces if s.bit_count()==d+1) for d in range(5)}
    ranks = {}
    for d in range(1,5):
        idx = {s:i for i,s in enumerate(fsets[d-1])}
        columns = []
        for f in fsets[d]:
            c = 0
            for lo in boundary(f): c |= 1 << idx[lo]
            columns.append(c)
        ranks[d] = mod2_rank(columns)
    dims = [len(fsets[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(5)]
    assert dims == [1,0,0,28,3], dims
    return ranks,dims

def run():
    faces = bit_faces()
    assert Counter(s.bit_count()-1 for s in faces)=={0:9,1:36,2:84,3:126,4:45}
    pairs, critical = lex_matching(faces)
    assert len(pairs)==134, len(pairs)
    assert len(critical)==32, len(critical)
    assert Counter(s.bit_count()-1 for s in critical)=={0:1,3:28,4:3}
    incidence_count = certify_acyclic(faces,pairs)
    morse = morse_boundary(pairs,critical)
    ranks, dims = independent_homology(faces)
    print('PASS: 300 nonempty faces, f-vector (9,36,84,126,45)')
    print(f'PASS: {len(pairs)} matching pairs, {len(critical)} critical faces: 1 in dimension 0, 28 in dimension 3, 3 in dimension 4')
    print(f'PASS: no gradient cycle on {incidence_count} Hasse incidences')
    print(f'PASS: exact integral Morse differential d4=0 on all {len(morse)} critical 4-cells')
    print(f'PASS: independent mod-2 boundary ranks {ranks}, Betti numbers {dims}')

if __name__ == '__main__':run()
