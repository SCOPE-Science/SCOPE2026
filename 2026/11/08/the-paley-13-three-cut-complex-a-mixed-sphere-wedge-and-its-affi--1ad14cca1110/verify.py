#!/usr/bin/env python3
"""Reconstruct the Paley-13 ordinary three-cut complex and its affine character."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import comb

N = 13
ALL = (1 << N) - 1
Q = {pow(x, 2, N) for x in range(1, N)}
assert Q == {1, 3, 4, 9, 10, 12}
ADJ = [sum(1 << j for j in range(N) if (j - i) % N in Q) for i in range(N)]
assert all(x.bit_count() == 6 for x in ADJ)


def edge_count_of_triple(triple):
    a, b, c = triple
    return int(bool(ADJ[a] & (1 << b))) + int(bool(ADJ[a] & (1 << c))) + int(bool(ADJ[b] & (1 << c)))


def generate_faces():
    faces = bytearray(1 << N)
    disconnected = []
    for triple in combinations(range(N), 3):
        if edge_count_of_triple(triple) <= 1:
            disconnected.append(triple)
            mask = ALL
            for v in triple:
                mask ^= 1 << v
            sub = mask
            while True:
                faces[sub] = 1
                if not sub:
                    break
                sub = (sub - 1) & mask
    assert len(disconnected) == 143
    return faces, disconnected


def independent_face_check(faces):
    # Check every subset using connectedness tests, without the downward-closure generator.
    connected = []
    for a, b, c in combinations(range(N), 3):
        if edge_count_of_triple((a, b, c)) >= 2:
            connected.append((1 << a) | (1 << b) | (1 << c))
    assert len(connected) == 143
    disconnected_masks = [((1 << a) | (1 << b) | (1 << c)) for a, b, c in combinations(range(N), 3)
                          if edge_count_of_triple((a, b, c)) <= 1]
    for mask in range(1 << N):
        complement = ALL ^ mask
        direct = any((t & complement) == t for t in disconnected_masks)
        assert bool(faces[mask]) == direct, mask
    # The Alexander dual has 13 vertices, all 78 edges, 143 triangles, 78 tetrahedra.
    counts = Counter(mask.bit_count()-1 for mask in range(1 << N)
                     if not faces[ALL ^ mask])
    assert counts == {-1:1, 0:13, 1:78, 2:143, 3:78}, counts
    # Cross-check the resulting homology by binary linear algebra on the much
    # smaller combinatorial Alexander dual. This does not replace the exact
    # integer Morse computation below.
    dual = {d: sorted(mask for mask in range(1 << N)
                      if not faces[ALL ^ mask] and mask.bit_count() == d + 1)
            for d in range(4)}
    def rank_mod_two(columns):
        basis = {}
        for vec in columns:
            while vec:
                pivot = vec.bit_length() - 1
                if pivot not in basis:
                    basis[pivot] = vec
                    break
                vec ^= basis[pivot]
        return len(basis)
    dual_ranks = {}
    for d in (1,2,3):
        pos = {mask: i for i,mask in enumerate(dual[d - 1])}
        columns = []
        for simplex in dual[d]:
            vector = 0
            for lower,_ in boundary(simplex):
                vector ^= 1 << pos[lower]
            columns.append(vector)
        dual_ranks[d] = rank_mod_two(columns)
    assert dual_ranks == {1:12, 2:66, 3:76}, dual_ranks
    assert (len(dual[2])-dual_ranks[2]-dual_ranks[3],
            len(dual[3])-dual_ranks[3]) == (1,2)
    return counts


def boundary(facet):
    position = 0
    rest = facet
    while rest:
        b = rest & -rest
        yield facet ^ b, (1 if position % 2 == 0 else -1)
        rest ^= b
        position += 1


def acyclic_matching(faces):
    remaining = {mask for mask, on in enumerate(faces) if on}
    up = {}
    reverse = {}
    for vertex in range(N):
        bit = 1 << vertex
        for face in tuple(sorted(remaining)):
            if face in remaining and face & bit == 0 and face | bit in remaining:
                partner = face | bit
                up[face] = partner
                reverse[partner] = face
                remaining.remove(face)
                remaining.remove(partner)
    assert len(up) == 3934
    assert len(remaining) == 11
    # Discard the augmented empty-face pair to get an ordinary Morse matching.
    # This leaves its vertex as a critical 0-cell and cannot create a cycle.
    assert up.pop(0) == 1
    reverse.pop(1)
    remaining.add(1)
    assert len(up) == 3933
    assert len(remaining) == 12
    c7 = sorted(mask for mask in remaining if mask.bit_count() == 8)
    c8 = sorted(mask for mask in remaining if mask.bit_count() == 9)
    assert c7 == [510, 1662, 3294, 3510, 4926, 6558]
    assert c8 == [3578, 3834, 6010, 7610, 8114]
    assert set(remaining) == set(c7+c8+[1])
    # Acyclicity of the entire ordinary (nonempty) Hasse diagram.
    indeg = [0] * (1 << N)
    outgoing = defaultdict(list)
    covers = 0
    for upper, on in enumerate(faces):
        if not on or upper == 0:
            continue
        for lower, _ in boundary(upper):
            if lower == 0 or not faces[lower]:
                continue
            if up.get(lower) == upper:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            outgoing[src].append(dst)
            indeg[dst] += 1
            covers += 1
    queue = deque(mask for mask, on in enumerate(faces) if on and mask and indeg[mask] == 0)
    reached = 0
    while queue:
        x = queue.popleft()
        reached += 1
        for y in outgoing[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    assert reached == sum(faces)-1
    assert covers == 50076
    return up, c7, c8, covers


def morse_boundary(up, c7, c8):
    target = set(c7)
    @lru_cache(None)
    def descend(cell):
        if cell in target:
            return {cell: 1}
        if cell not in up:
            # This lower cell was matched to a cell in the preceding dimension.
            return {}
        upper = up[cell]
        incidence = next(s for lower,s in boundary(upper) if lower == cell)
        total = defaultdict(int)
        for lower, signed in boundary(upper):
            if lower == cell:
                continue
            for critical, amount in descend(lower).items():
                total[critical] -= incidence * signed * amount
        return {k:v for k,v in total.items() if v}

    columns = []
    for upper in c8:
        total = defaultdict(int)
        for lower, signed in boundary(upper):
            for critical, amount in descend(lower).items():
                total[critical] += signed * amount
        columns.append([total[v] for v in c7])
    D = tuple(tuple(col[i] for col in columns) for i in range(len(c7)))
    expected = ((0,-1,0,1,1), (0,1,1,0,0), (-1,-1,0,0,0),
                (1,0,0,1,1), (0,0,-1,0,-1), (0,0,0,-1,0))
    assert D == expected
    # The six 5-by-5 minors vanish, and a displayed 4-by-4 minor equals 1.
    def det(matrix):
        a = tuple(tuple(row) for row in matrix)
        if len(a) == 1:
            return a[0][0]
        if len(a) == 0:
            return 1
        return sum((-1)**j * a[0][j] * det([row[:j]+row[j+1:] for row in a[1:]])
                   for j in range(len(a)))
    all_five_minors = [det([[D[r][c] for c in range(5)] for r in rows])
                       for rows in combinations(range(6),5)]
    assert all(x == 0 for x in all_five_minors)
    four_minor = det([[D[r][c] for c in (0,1,2,3)] for r in (0,1,2,4)])
    assert four_minor == 1
    return D, four_minor


def perm_sign(lst):
    return (-1)**sum(a > b for i,a in enumerate(lst) for b in lst[i+1:])


def lefschetz_reduced(faces, a, b):
    images = [(a*x+b)%N for x in range(N)]
    total = -1  # the augmented empty face in reduced chains
    for mask, on in enumerate(faces):
        if not on or not mask:
            continue
        xs = [i for i in range(N) if mask & (1 << i)]
        ys = [images[i] for i in xs]
        if sum(1 << y for y in ys) != mask:
            continue
        total += (-1)**(len(xs)-1) * perm_sign(ys)
    return total


def affine_characters(faces):
    power = {pow(4,k,N): k for k in range(6)}
    assert set(power) == Q
    observed = {}
    for a in sorted(Q):
        vals = {lefschetz_reduced(faces,a,b) for b in range(N)}
        assert len(vals) == 1
        observed[a] = vals.pop()
        k = power[a]
        predicted_h7 = 2 if k % 3 == 0 else -1
        predicted_h8 = (-1)**k
        assert observed[a] == -predicted_h7 + predicted_h8
    assert observed == {1:-1, 3:2, 4:0, 9:2, 10:0, 12:-3}
    # Since a nonidentity translation has order thirteen, its rational action
    # on a 1- or 2-dimensional vector space is trivial.
    return observed


def main():
    faces, disconnected = generate_faces()
    dual_counts = independent_face_check(faces)
    vector = [sum(1 for mask,on in enumerate(faces) if on and mask.bit_count() == dim+1)
              for dim in range(10)]
    assert vector == [13,78,286,715,1287,1716,1716,1287,637,143]
    assert sum(faces) == 7879
    up, c7,c8,covers = acyclic_matching(faces)
    D, minor = morse_boundary(up,c7,c8)
    characters = affine_characters(faces)
    print('VERIFY_OK')
    print('graph=Paley(13); edges=39; quadratic_residues='+str(sorted(Q)))
    print('cut_f_vector='+str(vector)+'; faces_including_empty='+str(sum(faces)))
    print('dual_f_vector='+str([13, 78, 143, 78])+'; GF2_boundary_ranks_1_2_3=[12,66,76]')
    print('matching_pairs='+str(len(up))+'; Hasse_covers='+str(covers)+'; critical_vertex_mask=1; acyclic=True')
    print('critical_7='+str(c7)+'; critical_8='+str(c8))
    print('morse_boundary_8_to_7='+str(D))
    print('all_5x5_minors_zero=True; 4x4_minor_rows_0_1_2_4_cols_0_1_2_3='+str(minor))
    print('reduced_lefschetz_for_multipliers='+str(characters))
    print('homotopy=S7_vee_S7_vee_S8; H7_Q=Q(zeta3); H8_Q=sign')

if __name__=='__main__':
    main()
