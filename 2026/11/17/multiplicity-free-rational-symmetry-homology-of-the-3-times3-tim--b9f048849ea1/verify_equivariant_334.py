#!/usr/bin/env python3
"""Exact combinatorial verification for the radius-two (3,3,4) Hamming Rips complex.

Reconstructs all simplices, an acyclic discrete Morse matching, 45 homology
character values by two independent signed-chain methods, and the rational
irreducible decomposition. Requires only Python 3 standard library.
"""
import collections
import itertools
import math

WORDS = list(itertools.product(range(3), range(3), range(4)))
INDEX = {x: i for i, x in enumerate(WORDS)}
N = len(WORDS)
BIT = lambda i: 1 << i
ALL = (1 << N) - 1
COMPAT = [sum(BIT(j) for j, y in enumerate(WORDS)
              if sum(a != b for a, b in zip(x, y)) <= 2)
          for x in WORDS]


def faces_complete():
    # Independently exhaust every clique using its least vertex.
    result = [0]
    def extend(prefix, candidates):
        while candidates:
            lowest = candidates & -candidates
            i = lowest.bit_length() - 1
            candidates ^= lowest
            face = prefix | lowest
            result.append(face)
            extend(face, candidates & COMPAT[i])
    extend(0, ALL)
    assert len(result) == len(set(result))
    return result


def morse_check(faces):
    present = set(faces)
    matching = {}
    for i in range(N):
        pivot = BIT(i)
        for face in sorted(present):
            upper = face | pivot
            if face & pivot or face not in present or upper not in present:
                continue
            present.remove(face)
            present.remove(upper)
            matching[face] = upper
    critical_sizes = collections.Counter(x.bit_count() for x in present)
    assert critical_sizes == {4: 96}, critical_sizes
    assert matching.get(0) == 1
    assert len(matching) == 15448

    # Exhaustively check acyclicity of the oriented Hasse diagram, not just
    # the counts of critical cells. Ordinary covers point down, matched up.
    outgoing = {face: [] for face in faces}
    indegree = {face: 0 for face in faces}
    covers = 0
    for upper in faces:
        rest = upper
        while rest:
            v = rest & -rest
            rest ^= v
            lower = upper ^ v
            if matching.get(lower) == upper:
                start, end = lower, upper
            else:
                start, end = upper, lower
            outgoing[start].append(end)
            indegree[end] += 1
            covers += 1
    queue = collections.deque(face for face in faces if indegree[face] == 0)
    processed = 0
    while queue:
        face = queue.popleft()
        processed += 1
        for upper in outgoing[face]:
            indegree[upper] -= 1
            if indegree[upper] == 0:
                queue.append(upper)
    assert processed == len(faces), (processed, len(faces))
    assert covers == 178704, covers
    return {"faces_including_empty": len(faces), "matching_pairs": len(matching),
            "critical_faces_of_size_four": critical_sizes[4],
            "directed_covers": covers, "acyclic": True}

S3 = [tuple(range(3)), (1, 0, 2), (1, 2, 0)]
S4 = [tuple(range(4)), (1, 0, 2, 3), (1, 0, 3, 2),
      (1, 2, 0, 3), (1, 2, 3, 0)]
# H = (S_3 x S_3) semidirect C_2, with the last factor exchanging positions.
# Representatives and class sizes, first six nonswapping, last three swapping.
H = [(0,0,0,1),(0,1,0,6),(0,2,0,4),
     (1,1,0,9),(1,2,0,12),(2,2,0,4),
     (0,0,1,6),(1,0,1,18),(2,0,1,12)]
S4_SIZES = [1,6,3,8,6]


def permutation(h, j):
    a, b, swap, _ = h
    f = []
    for x, y, z in WORDS:
        if swap:
            p = (S3[a][y], S3[b][x], S4[j][z])
        else:
            p = (S3[a][x], S3[b][y], S4[j][z])
        f.append(INDEX[p])
    assert sorted(f) == list(range(N))
    return f


def trace_by_orbit_cliques(perm):
    seen = set()
    orbits = []
    for i in range(N):
        if i in seen:
            continue
        mask = 0
        u = i
        while u not in seen:
            seen.add(u)
            mask |= BIT(u)
            u = perm[u]
        if all(COMPAT[k] & mask == mask for k in range(N) if mask & BIT(k)):
            orbits.append(mask)
    compatible = [0] * len(orbits)
    for i, a in enumerate(orbits):
        for j, b in enumerate(orbits):
            if i != j and all(COMPAT[k] & b == b
                              for k in range(N) if a & BIT(k)):
                compatible[i] |= BIT(j)
    def signed_sum(available):
        count = 1  # include the empty orbit family
        while available:
            v = available & -available
            i = v.bit_length() - 1
            available ^= v
            count -= signed_sum(available & compatible[i])
        return count
    return signed_sum((1 << len(orbits)) - 1)


def trace_by_oriented_faces(perm, faces):
    answer = 0
    for face in faces:
        vertices = [i for i in range(N) if face & BIT(i)]
        moved = [perm[i] for i in vertices]
        if sorted(moved) != vertices:
            continue
        inversions = sum(moved[i] > moved[j]
                         for i in range(len(moved))
                         for j in range(i + 1, len(moved)))
        answer += -1 if (len(vertices) + inversions) % 2 else 1
    return answer


def character_table(faces):
    chars = []
    for h in H:
        row = []
        for j in range(5):
            g = permutation(h, j)
            trace_a = trace_by_orbit_cliques(g)
            trace_b = trace_by_oriented_faces(g, faces)
            assert trace_a == trace_b, (h, j, trace_a, trace_b)
            row.append(trace_a)
        chars.append(row)
    return chars

S3_CHI = [[1, 1, 2], [1, -1, 0], [1, 1, -1]]
S4_IRREPS = [
    ("(4)", [1,1,1,1,1],1),
    ("(3,1)", [3,1,-1,0,-1],3),
    ("(2,2)", [2,0,2,-1,0],2),
    ("(2,1,1)", [3,-1,-1,0,1],3),
    ("(1,1,1,1)", [1,-1,1,1,-1],1),
]


def w_character(label, h):
    a,b,swap,_=h
    if len(label) == 2:
        i,j=label
        return (0 if swap else S3_CHI[a][i]*S3_CHI[b][j]
                + S3_CHI[a][j]*S3_CHI[b][i])
    i,sign,_=label
    return sign*S3_CHI[a][i] if swap else S3_CHI[a][i]*S3_CHI[b][i]


def decomposition(chars):
    # W = S_3 wr S_2. The nine irreducible characters comprise three induced
    # distinct-label pairs and six +- extensions of equal-label tensor pairs.
    W_REPS=[]
    for i,j in itertools.combinations(range(3),2):
        W_REPS.append(((i,j),2*S3_CHI[0][i]*S3_CHI[0][j]))
    for i in range(3):
        for sign in (1,-1):
            W_REPS.append(((i,sign,'equal'),S3_CHI[0][i]**2))
    assert sum(d*d for _,d in W_REPS) == 72
    assert sum(h[3] for h in H) == 72
    assert sum(S4_SIZES) == 24
    multiplicities=[]
    for label, wd in W_REPS:
        for name, char, sd in S4_IRREPS:
            dot = sum(h[3]*S4_SIZES[j]*chars[i][j]
                      *w_character(label,h)*char[j]
                      for i,h in enumerate(H) for j in range(5))
            assert dot % 1728 == 0, (label,name,dot)
            m=dot//1728
            assert m in (0,1), (label,name,m)
            if m:
                multiplicities.append((str(label),name,wd*sd,m))
    assert len(multiplicities)==14
    assert sum(d*m for _,_,d,m in multiplicities)==96
    assert not any(l==str((0,1,'equal')) and s=="(4)" for l,s,_,_ in multiplicities)
    return multiplicities


def main():
    faces = faces_complete()
    fvector=collections.Counter(f.bit_count() for f in faces)
    assert [fvector[k] for k in range(13)] == [1,36,414,2028,4869,6804,
                                6816,5184,3042,1324,396,72,6]
    morse=morse_check(faces)
    chars=character_table(faces)
    expected=[
       [96,14,4,0,4],
       [0,6,12,0,0],
       [6,2,-2,0,-2],
       [12,2,0,0,0],
       [0,0,0,0,0],
       [-3,-1,1,0,1],
       [-30,-4,-2,0,-2],
       [0,-2,-4,0,0],
       [-3,-1,1,0,1],
    ]
    assert chars==expected
    pieces=decomposition(chars)
    print("MORSE",morse)
    print("CHARACTER_ROWS",chars)
    print("IRREDUCIBLE_PIECES",pieces)
    print("VERIFIED_FULL_334_SYMMETRY_CHARACTER")

if __name__=='__main__':main()
