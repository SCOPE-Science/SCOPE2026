#!/usr/bin/env python3
"""Exhaustive certificate for the five-robust clique complex of P4 square P5.
Pure Python 3, standard library only. Every vertex subset and Hasse cover is checked.
"""
from collections import Counter, deque
from itertools import combinations

ROWS, COLS, K = 4, 5, 5
N = ROWS * COLS
TOTAL = 1 << N


def adjacency():
    ans = [0] * N
    for r in range(ROWS):
        for c in range(COLS):
            u = r * COLS + c
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < ROWS and 0 <= cc < COLS:
                    ans[u] |= 1 << (rr * COLS + cc)
    return ans


def independent_number_dp(neighbors):
    # DP over all masks; both recursive branches are strict submasks.
    a = bytearray(TOTAL)
    for s in range(1, TOTAL):
        bit = s & -s
        v = bit.bit_length() - 1
        without = s ^ bit
        a[s] = max(a[without], 1 + a[without & ~neighbors[v]])
    return a


def independent_five_obstruction(neighbors):
    # A logically separate, exact face predicate by 5-set enumeration.
    forbidden = []
    bad = bytearray(TOTAL)
    for idx in combinations(range(N), K):
        b = 0
        for v in idx:
            b |= 1 << v
        if all((neighbors[v] & b) == 0 for v in idx):
            bad[b] = 1
            forbidden.append(b)
    for v in range(N):
        bit = 1 << v
        for base in range(0, TOTAL, 2 * bit):
            for i in range(base, base + bit):
                if bad[i]:
                    bad[i + bit] = 1
    return bad, forbidden


def match_faces(faces, set_faces):
    remaining = set_faces.copy()
    pair = {}
    for v in range(N):
        bit = 1 << v
        # Sorting is not needed for proof, but makes reproducibility transparent.
        for s in faces:
            if s in remaining and not (s & bit):
                t = s | bit
                if t in remaining:
                    remaining.remove(s)
                    remaining.remove(t)
                    pair[s] = t
    return pair, remaining


def verify_morse_acyclicity(faces, set_faces, pair):
    indegree = {s: 0 for s in faces}
    incidence_count = 0
    for t in faces:
        bits = t
        while bits:
            bit = bits & -bits
            bits ^= bit
            s = t ^ bit
            if s and s in set_faces:
                incidence_count += 1
                if pair.get(s) == t:
                    indegree[t] += 1
                else:
                    indegree[s] += 1
    dq = deque(s for s, degree in indegree.items() if degree == 0)
    sorted_count = 0
    while dq:
        t = dq.popleft()
        sorted_count += 1
        bits = t
        while bits:
            bit = bits & -bits
            bits ^= bit
            s = t ^ bit
            if s and s in set_faces and pair.get(s) != t:
                indegree[s] -= 1
                if indegree[s] == 0:
                    dq.append(s)
        upper = pair.get(t)
        if upper is not None:
            indegree[upper] -= 1
            if indegree[upper] == 0:
                dq.append(upper)
    assert sorted_count == len(faces), ('directed cycle', sorted_count, len(faces))
    assert all(d == 0 for d in indegree.values())
    return incidence_count, sorted_count


def reflection_character(faces):
    # Flags: row flip (1), column flip (2).
    result = []
    for mode in range(4):
        p = []
        for r in range(ROWS):
            for c in range(COLS):
                rr = ROWS - 1 - r if mode & 1 else r
                cc = COLS - 1 - c if mode & 2 else c
                p.append(rr * COLS + cc)
        L, fixed = 0, 0
        for mask in faces:
            old = [v for v in range(N) if mask & (1 << v)]
            images = [p[v] for v in old]
            if sum(1 << u for u in images) != mask:
                continue
            fixed += 1
            inversions = sum(images[i] > images[j] for i in range(len(images)) for j in range(i + 1, len(images)))
            L += (-1) ** (len(old) - 1 + inversions)
        result.append((fixed, L, 1 - L))
    traces = [z[2] for z in result]
    reps = {}
    for er in (1, -1):
        for ec in (1, -1):
            t = (traces[0] + er * traces[1] + ec * traces[2] + er * ec * traces[3])
            assert t % 4 == 0
            reps[(er, ec)] = t // 4
    assert all(v >= 0 for v in reps.values())
    assert sum(reps.values()) == traces[0]
    return result, reps


def main():
    adj = adjacency()
    alpha = independent_number_dp(adj)
    bad, forb = independent_five_obstruction(adj)
    for mask in range(TOTAL):
        assert (alpha[mask] >= K) == bool(bad[mask]), ('face discrepancy', mask)
    faces = [s for s in range(1, TOTAL) if not bad[s]]
    fvec = Counter(s.bit_count() - 1 for s in faces)
    euler = sum((-1) ** d * c for d, c in fvec.items())
    assert len(forb) == 1998
    assert len(faces) == 72568
    assert tuple(fvec[d] for d in range(8)) == (20, 190, 1140, 4845, 13506, 22831, 21374, 8662)
    assert euler == -488
    print('masks', TOTAL, 'independent-five obstructions', len(forb))
    print('faces', len(faces), 'f_vector', tuple(fvec[d] for d in range(8)), 'Euler', euler)
    fset = set(faces)
    pair, critical = match_faces(faces, fset)
    crit = Counter(s.bit_count() - 1 for s in critical)
    assert len(pair) == 36039
    assert crit == Counter({7: 489, 0: 1}), crit
    print('Morse_pairs', len(pair), 'critical_cells', sorted(crit.items()))
    incidences, sorted_count = verify_morse_acyclicity(faces, fset, pair)
    print('Hasse_covers', incidences, 'topologically_sorted', sorted_count)
    character, rep = reflection_character(faces)
    assert [z[0] for z in character] == [72568, 252, 444, 212]
    assert [z[1] for z in character] == [-488, -30, -12, -14]
    assert [z[2] for z in character] == [489, 31, 13, 15]
    assert rep == {(1, 1): 137, (1, -1): 123, (-1, 1): 114, (-1, -1): 115}
    print('fixed_faces_Lefschetz_trace', character)
    print('Klein_four_irreducibles', sorted(rep.items(), reverse=True))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
