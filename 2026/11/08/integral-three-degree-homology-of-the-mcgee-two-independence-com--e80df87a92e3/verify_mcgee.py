"""Exact integral algebraic-Morse verification of the McGee graph's two-independence complex.

Requires Python >=3.10 and SymPy. All graph data and simplices are generated here.
No network access and no precomputed certificates are needed.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 24
LCF = (12, 7, -7) * 8
adj = [0] * N
for i in range(N):
    for j in ((i + 1) % N, (i + LCF[i]) % N):
        adj[i] |= 1 << j
        adj[j] |= 1 << i
assert all(mask.bit_count() == 3 for mask in adj)
assert sum(mask.bit_count() for mask in adj) // 2 == 36


def graph_girth():
    answer = N + 1
    for root in range(N):
        distance = [-1] * N
        parent = [-1] * N
        distance[root] = 0
        queue = deque((root,))
        while queue:
            x = queue.popleft()
            for y in range(N):
                if not ((adj[x] >> y) & 1):
                    continue
                if distance[y] < 0:
                    distance[y] = distance[x] + 1
                    parent[y] = x
                    queue.append(y)
                elif parent[x] != y:
                    answer = min(answer, distance[x] + distance[y] + 1)
    return answer


assert graph_girth() == 7


# Each valid face has all induced vertex degrees at most one.
# The incremental predicate uses the current old neighbor and its adjacency.
faces = []
face_numbers = Counter()

def enumerate_faces(mask=0, start=0):
    for v in range(start, N):
        existing = adj[v] & mask
        if existing and ((existing & (existing - 1)) or
                         (adj[existing.bit_length() - 1] & mask)):
            continue
        new = mask | (1 << v)
        faces.append(new)
        face_numbers[new.bit_count() - 1] += 1
        enumerate_faces(new, v + 1)


enumerate_faces()
face_set = set(faces)
assert len(faces) == len(face_set) == 553301
assert [face_numbers[d] for d in range(13)] == [
    24, 276, 1952, 9306, 31080, 73624, 122944,
    141457, 107504, 50448, 13112, 1542, 32]

# Independent induced-degree membership predicate, applied to EVERY face.
def valid_independently(mask):
    x = mask
    while x:
        bit = x & -x
        x -= bit
        if (adj[bit.bit_length() - 1] & mask).bit_count() > 1:
            return False
    return True

assert all(valid_independently(face) for face in faces)
assert all((face ^ (1 << i)) in face_set for face in faces
           for i in range(N) if face & (1 << i) and face.bit_count() > 1)


def matching(order):
    unmatched = set(face_set)
    low_to_high = {}
    high_to_low = {}
    for v in order:
        bit = 1 << v
        pairs = [(s, s | bit) for s in unmatched
                 if not s & bit and (s | bit) in unmatched]
        for a, b in pairs:
            unmatched.remove(a)
            unmatched.remove(b)
            low_to_high[a] = b
            high_to_low[b] = a
    assert 2 * len(low_to_high) + len(unmatched) == len(faces)
    assert len(low_to_high) == len(high_to_low)
    critical = {d: sorted(s for s in unmatched if s.bit_count() - 1 == d)
                for d in range(13)}
    return low_to_high, high_to_low, unmatched, critical


def assert_acyclic(low_to_high):
    # Orient each unmatched covering relation high-to-low, matched low-to-high.
    # Complete Kahn topological sort of the actual finite directed Hasse graph.
    indegree = {face: 0 for face in face_set}
    incidence = 0
    for high in faces:
        if high.bit_count() == 1:
            continue  # empty face is not a CW cell
        t = high
        while t:
            bit = t & -t
            t -= bit
            low = high ^ bit
            incidence += 1
            if low_to_high.get(low) == high:
                indegree[high] += 1
            else:
                indegree[low] += 1
    queue = deque(s for s in faces if indegree[s] == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        if face.bit_count() > 1:
            t = face
            while t:
                bit = t & -t
                t -= bit
                low = face ^ bit
                if low_to_high.get(low) != face:
                    indegree[low] -= 1
                    if indegree[low] == 0:
                        queue.append(low)
        if face in low_to_high:
            high = low_to_high[face]
            indegree[high] -= 1
            if indegree[high] == 0:
                queue.append(high)
    assert visited == len(face_set), (visited, len(face_set))
    return incidence


def signed_morse_boundary(k, low_to_high, high_to_low, unmatched, critical):
    target = critical[k - 1]
    index = {c: i for i, c in enumerate(target)}

    @lru_cache(maxsize=None)
    def reduction(face):
        # Algebraic elimination of an acyclic unit incidence pair.
        if face in unmatched:
            return {face: 1}
        if face in high_to_low:
            return {}
        high = low_to_high[face]
        pivot = high ^ face
        sign_pivot = (-1) ** ((face & (pivot - 1)).bit_count())
        answer = {}
        t = high
        while t:
            bit = t & -t
            t -= bit
            if bit == pivot:
                continue
            coefficient = -sign_pivot * (-1) ** ((high & (bit - 1)).bit_count())
            for crit, value in reduction(high ^ bit).items():
                answer[crit] = answer.get(crit, 0) + coefficient * value
        return {crit: value for crit, value in answer.items() if value}

    columns = []
    for top in critical[k]:
        column = [0] * len(target)
        t = top
        while t:
            bit = t & -t
            t -= bit
            incidence_sign = (-1) ** ((top & (bit - 1)).bit_count())
            for crit, value in reduction(top ^ bit).items():
                column[index[crit]] += incidence_sign * value
        columns.append(column)
    M = Matrix(list(map(list, zip(*columns)))) if columns else Matrix.zeros(len(target), 0)
    del reduction
    return M


def smith_invariants(M):
    D = smith_normal_form(M, domain=ZZ)
    return [abs(int(D[i, i])) for i in range(min(D.rows, D.cols)) if D[i, i]]

# The two pivot orders are combinatorially different and induce different
# small chain complexes. Agreement provides a useful independent algebraic check.
orders = {
    'residue_classes_mod_3': list(range(0, N, 3)) + list(range(1, N, 3)) + list(range(2, N, 3)),
    'ascending': list(range(N)),
}
for label, order in orders.items():
    low, high, critical_set, critical = matching(order)
    counts = {d: len(a) for d, a in critical.items() if a}
    total = sum(counts.values())
    assert counts.get(0) == 1
    assert not any(d in counts for d in range(1, 7))
    assert not any(d in counts for d in range(10, 13))
    inc = assert_acyclic(low)
    # No critical cells in dimension 6 or below except one vertex, or above 9.
    A = signed_morse_boundary(8, low, high, critical_set, critical)
    B = signed_morse_boundary(9, low, high, critical_set, critical)
    assert A * B == Matrix.zeros(A.rows, B.cols)
    diag_a = smith_invariants(A)
    diag_b = smith_invariants(B)
    assert all(x == 1 for x in diag_a + diag_b)
    b7 = len(critical[7]) - len(diag_a)
    b8 = len(critical[8]) - len(diag_a) - len(diag_b)
    b9 = len(critical[9]) - len(diag_b)
    assert (b7, b8, b9) == (5, 1, 2), (label, counts, diag_a, diag_b)
    # All torsion in H7 or H8 could only arise from non-unit Smith factors.
    assert len(diag_b) == B.rank() and len(diag_a) == A.rank()
    print('ORDER', label, 'critical', counts, 'matched_pairs', len(low),
          'oriented_hasse_incidences', inc, 'SNF_d8', diag_a, 'SNF_d9', diag_b,
          'reduced_integral_Betti_7_8_9', (b7, b8, b9), flush=True)
    del low, high, critical_set, critical, A, B

print('GRAPH cubic vertices=24 edges=36 girth=7 LCF=(12,7,-7)*8')
print('FACES', len(faces), 'vector', [face_numbers[d] for d in range(13)])
print('ALL_CHECKS_PASS')
