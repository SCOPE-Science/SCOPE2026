#!/usr/bin/env python3
"""Finite corroboration of the cycle-multipath wedge theorem; no third-party dependencies.

All infinite-parameter arguments are given in RESULT.md, not inferred from this test.
"""
from collections import Counter, defaultdict, deque


def faces_of_cycle(N):
    arcs = [(i, (i + 1) % N) for i in range(N)] + [((i + 1) % N, i) for i in range(N)]
    faces = {0}
    for j, (a, b) in enumerate(arcs):
        for mask in list(faces):
            selected = [arcs[i] for i in range(2*N) if mask & (1 << i)]
            if any(u == a or v == b for u, v in selected):
                continue
            outgoing = {u: v for u, v in selected}
            outgoing[a] = b
            if len(outgoing) != len(selected) + 1:
                continue
            cycle = False
            for start in outgoing:
                seen = set()
                x = start
                while x in outgoing:
                    if x in seen:
                        cycle = True
                        break
                    seen.add(x)
                    x = outgoing[x]
                if cycle:
                    break
            if not cycle:
                faces.add(mask | (1 << j))
    return arcs, faces


def mod2_rank(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            i = x.bit_length() - 1
            if i in pivots:
                x ^= pivots[i]
            else:
                pivots[i] = x
                break
    return len(pivots)


def betti_numbers(faces):
    by_dim = defaultdict(list)
    for f in faces:
        if f:
            by_dim[f.bit_count() - 1].append(f)
    ranks = {}
    for d in range(1, max(by_dim) + 1):
        row = {f: i for i, f in enumerate(by_dim[d - 1])}
        columns = []
        for f in by_dim[d]:
            boundary = 0
            for v in range(f.bit_length()):
                if f >> v & 1:
                    boundary |= 1 << row[f ^ (1 << v)]
            columns.append(boundary)
        ranks[d] = mod2_rank(columns)
    return {d:len(fs) - ranks.get(d,0) - ranks.get(d+1,0) - (1 if d == 0 else 0)
            for d,fs in by_dim.items()}


def matching_and_dag(faces, N):
    # Augmented greedy toggle, with the empty-singleton pair omitted from
    # the ordinary matching: the singleton becomes the critical base vertex.
    remaining = set(faces)
    matches = []
    empty_partner = None
    for i in range(2*N):
        for f in sorted(remaining, key=lambda a:(a.bit_count(),a)):
            g = f | (1<<i)
            if f not in remaining or g == f or g not in remaining:
                continue
            remaining.remove(f)
            remaining.remove(g)
            if f == 0:
                empty_partner = g
            else:
                matches.append((f,g))
    assert empty_partner is not None
    critical = remaining | {empty_partner}
    critical.discard(0)
    forward = {(f,g) for f,g in matches}
    nodes = set(faces) - {0}
    adjacency = {f:[] for f in nodes}
    indegree = {f:0 for f in nodes}
    covers = 0
    for upper in nodes:
        for j in range(2*N):
            if not upper >> j & 1:
                continue
            lower = upper ^ (1<<j)
            if lower == 0:
                continue
            covers += 1
            a,b = (lower,upper) if (lower,upper) in forward else (upper,lower)
            adjacency[a].append(b)
            indegree[b] += 1
    q = deque(v for v in nodes if indegree[v] == 0)
    visited = 0
    while q:
        x = q.popleft()
        visited += 1
        for y in adjacency[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert visited == len(nodes), (visited,len(nodes))
    assert len(matches)*2 + len(critical) == len(nodes)
    return Counter(f.bit_count()-1 for f in critical),len(matches),covers


def predicted(N):
    n = N-1
    if n%4 == 0:
        low = (n-1)//2 + 1; multiplicity = 1
    else:
        low = (n-1)//2; multiplicity = 3 if n%4 == 3 else 1
    return {low:multiplicity,n-1:2}


def main():
    for N in range(4,10):
        arcs, faces = faces_of_cycle(N)
        top = {f for f in faces if f.bit_count() == N-1}
        forward = (1<<N)-1
        reverse = forward<<N
        expected_top = {forward ^ (1<<j) for j in range(N)} | \
                       {reverse ^ (1<<(N+j)) for j in range(N)}
        assert top == expected_top, ('top classification',N)
        assert not any(f.bit_count()>=N for f in faces)
        betti = {i:r for i,r in betti_numbers(faces).items() if r}
        assert betti == predicted(N), ('homology',N,betti,predicted(N))
        if N == 4:
            mixed_edges = [f for f in faces if f.bit_count()==2 and
                           (f & forward) and (f & reverse)]
            assert len(mixed_edges) == 4
            assert not any(f.bit_count()==3 and (f & forward) and
                           (f & reverse) for f in faces)
        if N == 5:
            crit,pairs,covers=matching_and_dag(faces,N)
            assert crit == Counter({0:1,2:1,3:2}),crit
            print('PENTAGON_MORSE',len(faces),'faces',pairs,'pairs',covers,
                  'Hasse covers; critical',dict(crit))
        print('CYCLE',N,'faces',len(faces),'top simplices',len(top),
              'mod2 reduced Betti',betti)
    print('ALL_BIDIRECTED_CYCLE_CHECKS_OK')

if __name__=='__main__':
    main()
