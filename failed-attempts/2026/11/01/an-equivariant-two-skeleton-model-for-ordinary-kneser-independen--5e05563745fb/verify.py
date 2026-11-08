"""Finite corroborating checks for the pair-intersection complex on n labels.
No external dependencies; exact arithmetic throughout.
"""
from itertools import combinations, permutations
from math import comb


def parity_of_image(a):
    inv = sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    return -1 if inv % 2 else 1


def simplices(n):
    edges = list(combinations(range(n), 2))
    index = {a: j for j, a in enumerate(edges)}
    by_degree = {}
    for size in range(1, n):
        chosen = set()
        for v in range(n):
            star = [index[e] for e in edges if v in e]
            chosen.update(combinations(star, size))
        if size <= 3:
            for triple in combinations(range(n), 3):
                face = tuple(index[e] for e in combinations(triple, 2))
                chosen.update(combinations(face, size))
        if not chosen:
            break
        by_degree[size - 1] = sorted(chosen)
    return edges, by_degree


def gf2_rank(columns):
    pivots = {}
    for v in columns:
        while v:
            bit = v.bit_length() - 1
            if bit not in pivots:
                pivots[bit] = v
                break
            v ^= pivots[bit]
    return len(pivots)


def betti_mod2(by_degree):
    rank = {0: 1}  # Reduced augmentation, for a nonempty complex.
    for d in sorted(by_degree):
        if d == 0:
            continue
        prev = {face: j for j, face in enumerate(by_degree[d - 1])}
        columns = []
        for face in by_degree[d]:
            col = 0
            for i in range(len(face)):
                sub = face[:i] + face[i+1:]
                col ^= 1 << prev[sub]
            columns.append(col)
        rank[d] = gf2_rank(columns)
    return {d: len(faces)-rank.get(d,0)-rank.get(d+1,0)
            for d,faces in by_degree.items()}


def exterior_cube_character(permutation):
    n = len(permutation)
    numerator = [1]
    visited = set()
    for start in range(n):
        if start in visited:
            continue
        ell = 0
        i = start
        while i not in visited:
            visited.add(i)
            ell += 1
            i = permutation[i]
        new = numerator + [0] * ell
        for j, a in enumerate(numerator):
            new[j + ell] += (-1)**(ell+1)*a
        numerator = new
    quotient = []
    for coefficient in numerator:
        quotient.append(coefficient-(quotient[-1] if quotient else 0))
    return quotient[3]


def reduced_lefschetz(permutation, edges, by_degree):
    ix = {e:i for i,e in enumerate(edges)}
    action = tuple(ix[tuple(sorted((permutation[u], permutation[v])))]
                   for u,v in edges)
    result = -1
    for dim, faces in by_degree.items():
        for face in faces:
            image = tuple(action[u] for u in face)
            if tuple(sorted(image)) == face:
                result += (-1)**dim * parity_of_image(image)
    return result


def main():
    for n in (4,5,6,7):
        edges, by_degree = simplices(n)
        betti = betti_mod2(by_degree)
        expected = {i: (comb(n-1,3) if i == 2 else 0)
                    for i in by_degree}
        assert betti == expected, (n,betti,expected)
        count = 0
        if n <= 6:  # All permutations exhaustively; 24+120+720 cases.
            for p in permutations(range(n)):
                lhs = reduced_lefschetz(p,edges,by_degree)
                rhs = exterior_cube_character(p)
                assert lhs == rhs, (n,p,lhs,rhs)
                count += 1
        print('n=%d face_vector=%s reduced_F2_betti=%s character_checks=%d PASS' %
              (n, [len(by_degree[d]) for d in sorted(by_degree)], betti, count))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
