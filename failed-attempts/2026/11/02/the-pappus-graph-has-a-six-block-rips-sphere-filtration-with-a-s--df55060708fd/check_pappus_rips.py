"""Exact, dependency-free verification of Pappus graph Rips homotopy and symmetry.

Run: python3 check_pappus_rips.py
All graph data come from the LCF presentation [5,7,-7,7,-7,-5]^3.
"""
from collections import Counter, deque
from itertools import combinations

N = 18


def graph_and_distance():
    adj = [set() for _ in range(N)]

    def add(u, v):
        adj[u].add(v)
        adj[v].add(u)

    for u in range(N):
        add(u, (u + 1) % N)
    for u, offset in enumerate([5, 7, -7, 7, -7, -5] * 3):
        add(u, (u + offset) % N)
    assert all(len(x) == 3 for x in adj)
    assert sum(map(len, adj)) // 2 == 27
    dists = []
    for start in range(N):
        d = [-1] * N
        d[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        dists.append(d)
    assert all(-1 not in d for d in dists)
    assert max(max(d) for d in dists) == 4
    return adj, dists


def all_faces(dist, radius):
    neigh = [sum(1 << j for j in range(N) if j != i and dist[i][j] <= radius)
             for i in range(N)]
    faces = {0}
    for mask in range(1, 1 << N):
        low = mask & -mask
        vertex = low.bit_length() - 1
        rest = mask ^ low
        if rest in faces and rest & ~neigh[vertex] == 0:
            faces.add(mask)
    faces.remove(0)
    return faces


def count_dimensions(faces):
    return tuple(sum(x.bit_count() == k for x in faces)
                 for k in range(1, max(x.bit_count() for x in faces) + 1))


def morse_matching(faces):
    remaining = set(faces)
    pairs = []
    for vertex in range(N):
        bit = 1 << vertex
        for face in sorted(remaining, key=lambda x: (x.bit_count(), x)):
            bigger = face | bit
            if face & bit == 0 and face in remaining and bigger in remaining:
                remaining.remove(face)
                remaining.remove(bigger)
                pairs.append((face, bigger))
    return remaining, pairs


def assert_acyclic_morse(faces, pairs):
    matched = set(pairs)
    idx = {face: i for i, face in enumerate(sorted(faces))}
    nxt = [[] for _ in faces]
    indeg = [0] * len(faces)
    for face in faces:
        for v in range(N):
            bit = 1 << v
            if face & bit:
                small = face ^ bit
                if small not in faces:
                    continue
                # Ordinary Hasse arrows go downward; matched arrows upward.
                a, b = (small, face) if (small, face) in matched else (face, small)
                nxt[idx[a]].append(idx[b])
                indeg[idx[b]] += 1
    queue = deque(i for i, degree in enumerate(indeg) if degree == 0)
    seen = 0
    while queue:
        u = queue.popleft()
        seen += 1
        for v in nxt[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    assert seen == len(faces), ('cyclic Morse matching', seen, len(faces))
    return len(pairs), sum(map(len, nxt))


def automorphisms(dist):
    all_maps = []

    def extend(mp, used):
        if len(mp) == N:
            all_maps.append(tuple(mp[i] for i in range(N)))
            return
        best = None
        for i in range(N):
            if i in mp:
                continue
            candidates = [j for j in range(N) if j not in used and all(
                dist[i][a] == dist[j][b] for a, b in mp.items())]
            if not candidates:
                return
            if best is None or len(candidates) < len(best[1]):
                best = (i, candidates)
        i, candidates = best
        for j in candidates:
            mp[i] = j
            used.add(j)
            extend(mp, used)
            used.remove(j)
            del mp[i]

    extend({}, set())
    assert len(all_maps) == len(set(all_maps)) == 216
    assert tuple(range(N)) in all_maps
    return all_maps


def sign_of_images(images):
    parity = 0
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            parity ^= (images[i] > images[j])
    return 1 if parity == 0 else -1


def signed_lefschetz(perm, faces):
    total = 0
    for mask in faces:
        members = [i for i in range(N) if mask >> i & 1]
        images = [perm[i] for i in members]
        if sum(1 << v for v in images) != mask:
            continue
        sign = sign_of_images(images)
        total += sign if len(members) % 2 == 1 else -sign
    return total


def blocks_at_distance_four(dist):
    complement = [set(j for j in range(N) if dist[i][j] == 4) for i in range(N)]
    unseen = set(range(N))
    blocks = []
    while unseen:
        i = min(unseen)
        block = tuple(sorted({i} | complement[i]))
        assert len(block) == 3
        assert all(complement[j] == set(block) - {j} for j in block)
        blocks.append(block)
        unseen.difference_update(block)
    assert len(blocks) == 6
    assert sum(len(b) for b in blocks) == N
    return tuple(blocks)


def joined_sphere_character(perm, blocks):
    where = {v: b for b, block in enumerate(blocks) for v in block}
    block_map = tuple(where[perm[block[0]]] for block in blocks)
    assert len(set(block_map)) == 6
    assert all({where[perm[v]] for v in block} == {block_map[i]}
               for i, block in enumerate(blocks))
    parity = sign_of_images(block_map)
    visited = set()
    for b in range(6):
        if b in visited:
            continue
        sequence = []
        current = b
        while current not in visited:
            visited.add(current)
            sequence.append(current)
            current = block_map[current]
        assert current == b
        fixed = 0
        for v in blocks[b]:
            image = v
            for _ in sequence:
                image = perm[image]
            fixed += (image == v)
        parity *= (fixed - 1)
    return parity


def main():
    adj, dist = graph_and_distance()
    f1, f2, f3 = (all_faces(dist, radius) for radius in (1, 2, 3))
    assert count_dimensions(f1) == (18, 27)
    assert count_dimensions(f2) == (18, 81, 108, 18)
    assert count_dimensions(f3) == (18, 135, 540, 1215, 1458, 729)
    remaining, pairs = morse_matching(f2)
    assert len(pairs) == 99
    assert Counter(x.bit_count() - 1 for x in remaining) == {0: 1, 2: 26}
    assert Counter(a.bit_count() - 1 for a, _ in pairs) == {0: 17, 1: 64, 2: 18}
    count, arcs = assert_acyclic_morse(f2, pairs)
    assert count == 99
    blocks = blocks_at_distance_four(dist)
    # A join of six three-point sets has face polynomial (1+3t)^6.
    assert count_dimensions(f3) == (18, 135, 540, 1215, 1458, 729)
    autos = automorphisms(dist)
    c1, c2, c5 = [], [], []
    for perm in autos:
        trace1 = 1 - signed_lefschetz(perm, f1)
        trace2 = signed_lefschetz(perm, f2) - 1
        trace5 = 1 - signed_lefschetz(perm, f3)
        assert trace5 == joined_sphere_character(perm, blocks)
        c1.append(trace1)
        c2.append(trace2)
        c5.append(trace5)
    assert Counter(c1) == {1: 104, -2: 57, 0: 54, 10: 1}
    assert Counter(c2) == {-1: 92, 0: 54, 2: 48, 5: 12, -10: 9, 26: 1}
    assert Counter(c5) == {1: 56, 0: 54, 4: 42, -2: 36, -8: 18, 16: 9, 64: 1}
    assert (sum(c1), sum(c2), sum(c5)) == (0, 0, 216)
    print('LCF_GRAPH: vertices=18 edges=27 diameter=4 automorphisms=216')
    print('RIPS_F_VECTORS: 1=(18,27); 2=(18,81,108,18); 3=(18,135,540,1215,1458,729)')
    print('MORSE_2: pairs=99 critical=(one_vertex,26_two_cells) hasse_arcs=%d acyclic=YES' % arcs)
    print('DISTANCE_4: six_disjoint_triangles=', blocks)
    print('CHAR_H1:', sorted(Counter(c1).items()))
    print('CHAR_H2:', sorted(Counter(c2).items()))
    print('CHAR_H5:', sorted(Counter(c5).items()))
    print('CHARACTER_JOIN_IDENTITY: 216/216 PASS')
    print('QUOTIENT_RATIONAL_POSITIVE_BETTI: r1=none r2=none r3=H5_rank_1')
    print('PAPPUS_RIPS_HOMOTOPY_216_CHARACTERS_EXACT_OK')


if __name__ == '__main__':
    main()
