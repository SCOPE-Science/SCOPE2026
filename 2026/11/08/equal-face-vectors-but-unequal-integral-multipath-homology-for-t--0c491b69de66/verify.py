#!/usr/bin/env python3
"""Self-contained exact verification of the Wagner/cube bidirected multipath comparison.

Usage: python3 verify.py morse_certificate.json
       python3 verify.py --write-certificate
Python standard library only. An assertion failure means the check failed.
"""
import json
import sys
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product

N = 8
ARCS = []
ARC_INDEX = {}


def define_graph(name):
    global ARCS, ARC_INDEX
    if name == 'Wagner':
        ARCS = [(u, w) for u in range(N) for w in range(N)
                if (w-u) % 8 in (1, 4, 7)]
    elif name == 'Cube':
        ARCS = [(u, w) for u in range(N) for w in range(N)
                if (u ^ w).bit_count() == 1]
    else:
        raise ValueError(name)
    ARCS.sort()
    ARC_INDEX = {a: k for k, a in enumerate(ARCS)}
    assert len(ARCS) == 24


def enumerate_by_arcs():
    """Choose each arc in turn, preserving partial-injection and no-cycle rules."""
    faces = [0]
    for j, (u, v) in enumerate(ARCS):
        new = []
        for mask in faces:
            outgoing, incoming = [-1]*N, [-1]*N
            for k, (a,b) in enumerate(ARCS[:j]):
                if mask & (1 << k):
                    outgoing[a], incoming[b] = b, a
            if outgoing[u] != -1 or incoming[v] != -1:
                continue
            w = v
            while outgoing[w] != -1 and w != u:
                w = outgoing[w]
            if w != u:
                new.append(mask | (1 << j))
        faces.extend(new)
    return set(faces)


def enumerate_by_sources():
    """Independent exhaustive successor-map enumeration on eight graph vertices."""
    opts = [(-1,) + tuple(v for (a,v) in ARCS if a == u)
            for u in range(N)]
    faces = set()
    for successor in product(*opts):
        targets = [w for w in successor if w >= 0]
        if len(set(targets)) != len(targets):
            continue
        acyclic = True
        for start in range(N):
            visited = set()
            v = start
            while v >= 0:
                if v in visited:
                    acyclic = False
                    break
                visited.add(v)
                v = successor[v]
            if not acyclic:
                break
        if not acyclic:
            continue
        face = 0
        for u,v in enumerate(successor):
            if v >= 0:
                face |= 1 << ARC_INDEX[u,v]
        faces.add(face)
    return faces


def signed_boundary(face):
    for i, j in enumerate(k for k in range(len(ARCS)) if face & (1 << k)):
        yield face ^ (1 << j), (-1 if i % 2 else 1)


def matching(faces, order):
    """Lexicographic pivot matching of augmented face poset."""
    unpaired = set(faces)
    pairs = {}
    for j in order:
        flag = 1 << j
        for lower in sorted(x for x in unpaired
                            if not x & flag and x | flag in unpaired):
            upper = lower | flag
            if lower in unpaired and upper in unpaired:
                pairs[lower] = upper
                unpaired.remove(lower)
                unpaired.remove(upper)
    return pairs, unpaired


def check_gradient_acyclicity(faces, pairs):
    """Check all augmented Hasse edges, reversing exactly matching edges."""
    indegree = {f: 0 for f in faces}
    out = defaultdict(list)
    incidences = 0
    for upper in faces:
        for lower,_ in signed_boundary(upper):
            source,target = (lower,upper) if pairs.get(lower) == upper else (upper,lower)
            out[source].append(target)
            indegree[target] += 1
            incidences += 1
    queue = deque(f for f, d in indegree.items() if d == 0)
    count = 0
    while queue:
        source = queue.popleft()
        count += 1
        for target in out[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    assert count == len(faces)
    return incidences


def integral_morse_matrices(pairs, critical):
    """All gradient-path coefficients, with signed simplicial incidences.

    A paired upper face projects to 0, a critical face to itself.
    For a paired lower b and its matched upper U, replace b by
    -(boundary(U)[b])^{-1} * sum_{t!=b} boundary(U)[t] P(t).
    The matching acyclicity ensures that this recursion terminates.
    """
    paired_upper = set(pairs.values())
    @lru_cache(None)
    def project(face):
        if face in critical:
            return {face:1}
        if face in paired_upper:
            return {}
        upper = pairs[face]
        boundary = dict(signed_boundary(upper))
        unit = boundary[face]
        assert abs(unit) == 1
        output = defaultdict(int)
        for lower, sign in boundary.items():
            if lower == face:
                continue
            for c, coef in project(lower).items():
                output[c] -= unit * sign * coef
        return {c:coef for c,coef in output.items() if coef}

    basis = {d: sorted(x for x in critical if x.bit_count()-1 == d)
             for d in range(-1,7)}
    matrices = {}
    for degree in (4,5,6):
        low,high = basis[degree-1],basis[degree]
        ids = {x:i for i,x in enumerate(low)}
        a = [[0]*len(high) for _ in low]
        for j, upper in enumerate(high):
            for face, sign in signed_boundary(upper):
                for c,coef in project(face).items():
                    a[ids[c]][j] += sign*coef
        matrices[degree] = a
    return basis, matrices


def rank_with_integral_unit_certificate(matrix):
    """Exact elementary unimodular integer operations; require diagonal 1 and 0."""
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if a else 0
    i = 0
    while i < min(rows,cols):
        pivot = next(((r,c) for r in range(i,rows) for c in range(i,cols)
                      if abs(a[r][c]) == 1),None)
        if pivot is None:
            break
        r,c = pivot
        a[i],a[r] = a[r],a[i]
        for row in a:
            row[i],row[c] = row[c],row[i]
        if a[i][i] == -1:
            a[i] = [-z for z in a[i]]
        for r in range(rows):
            if r != i and a[r][i]:
                k = a[r][i]
                a[r] = [a[r][j]-k*a[i][j] for j in range(cols)]
        for c in range(cols):
            if c != i and a[i][c]:
                k = a[i][c]
                for r in range(rows):
                    a[r][c] -= k*a[r][i]
        i += 1
    assert all(a[r][c] == (1 if r == c and r < i else 0)
               for r in range(rows) for c in range(cols))
    return i


def direct_modular_rank(faces, degree, prime):
    """Full unreduced simplicial boundary over a prime field, no Morse projection."""
    lows = sorted(f for f in faces if f.bit_count() == degree)
    highs = sorted(f for f in faces if f.bit_count() == degree+1)
    ids = {x:i for i,x in enumerate(lows)}
    pivots = {}
    for upper in highs:
        vector = {ids[lower]:sign % prime for lower,sign in signed_boundary(upper)}
        while vector:
            lead = min(vector)
            if lead not in pivots:
                inverse = pow(vector[lead],-1,prime)
                pivots[lead] = {r:(v*inverse)%prime for r,v in vector.items() if v}
                break
            factor = vector[lead]
            for r,v in pivots[lead].items():
                w = (vector.get(r,0)-factor*v)%prime
                if w:vector[r]=w
                else:vector.pop(r,None)
    return len(pivots)


def run(cert_path=None):
    expected_f = {-1:1,0:24,1:216,2:928,3:2016,4:2160,5:1008,6:144}
    outcomes = {
      'Wagner': {'pairs':3194,'critical':{3:15,4:52,5:32,6:10},
                 'ranks':{4:11,5:0,6:0},
                 'modular':{1:23,2:193,3:735,4:1277,5:842,6:134},
                 'homology':[4,41,32,10]},
      'Cube': {'pairs':3193,'critical':{3:8,4:51,5:40,6:12},
               'ranks':{4:2,5:4,6:0},
               'modular':{1:23,2:193,3:735,4:1275,5:840,6:132},
               'homology':[6,45,36,12]}}
    certificate = {'graph_models':{},'results':{}}
    for name in ('Wagner','Cube'):
        define_graph(name)
        faces = enumerate_by_arcs()
        assert faces == enumerate_by_sources()
        assert Counter(f.bit_count()-1 for f in faces) == expected_f
        certificate['graph_models'][name] = {'arcs':ARCS[:], 'face_counts':expected_f}
        expected = outcomes[name]
        graph_result = []
        for label,order in [('forward',range(24)),('reverse',range(23,-1,-1))]:
            pairs,critical = matching(faces,order)
            assert len(pairs) == expected['pairs']
            assert Counter(f.bit_count()-1 for f in critical) == expected['critical']
            assert check_gradient_acyclicity(faces,pairs) == 29160
            basis, matrices = integral_morse_matrices(pairs,critical)
            for degree in (5,6):
                first, second = matrices[degree-1], matrices[degree]
                assert all(sum(first[i][k]*second[k][j]
                               for k in range(len(second))) == 0
                           for i in range(len(first))
                           for j in range(len(second[0])))
            ranks = {d:rank_with_integral_unit_certificate(matrices[d])
                     for d in (4,5,6)}
            assert ranks == expected['ranks']
            for d in (4,5,6):
                a = matrices[d]
                assert len(a) == len(basis[d-1])
                assert all(len(row) == len(basis[d]) for row in a)
            betti = [len(basis[d])-ranks.get(d,0)-ranks.get(d+1,0)
                     for d in (3,4,5,6)]
            assert betti == expected['homology']
            graph_result.append({
                'matching':label, 'pairs':len(pairs), 'Hasse_incidences':29160,
                'critical_masks_by_dim':{str(d):basis[d] for d in range(3,7)},
                'boundary_matrices':{str(d):{
                    'shape':[len(basis[d-1]),len(basis[d])],
                    'entries':[[i,j,value] for i,row in enumerate(matrices[d])
                               for j,value in enumerate(row) if value]}
                    for d in (4,5,6)},
                'unit_diagonal_ranks':ranks})
        for p in (2,3):
            ordinary_ranks = {d:direct_modular_rank(faces,d,p) for d in range(1,7)}
            assert ordinary_ranks == expected['modular']
        certificate['results'][name] = graph_result
    # Both models have the same f-vector, but H_3, H_4, H_5, H_6 differ.
    if cert_path:
        with open(cert_path,encoding='utf-8') as f:
            assert json.load(f) == json.loads(json.dumps(certificate))
    print('WAGNER_CUBE_MULTIPATH_INTEGRAL_COMPARISON_VERIFIED')
    print('both_faces=6497; f=(24,216,928,2016,2160,1008,144); two_enumerators_agree')
    print('Wagner: critical=(15,52,32,10), unit_ranks=(11,0,0), H=(4,41,32,10)')
    print('Cube: critical=(8,51,40,12), unit_ranks=(2,4,0), H=(6,45,36,12)')
    print('both orders acyclic; all 29160 incidences checked per matching')
    print('integral diagonal factors all units; direct mod2 and mod3 ranks agree')
    return certificate


if __name__=='__main__':
    c = run(None if len(sys.argv)==1 or sys.argv[1]=='--write-certificate'
            else sys.argv[1])
    if '--write-certificate' in sys.argv:
        with open('morse_certificate.json','w',encoding='utf-8') as f:
            json.dump(c,f,ensure_ascii=False,separators=(',',':'))
            f.write('\n')
