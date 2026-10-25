"""Exact reduced simplicial homology check over the two-element field.

The bitwise column elimination independently checks the dimensions predicted
by the wheel matching-complex theorem in finite cases. This is not a proof
of its infinite-family character formula.
"""


def chain_groups(n):
    edges = [(i, (i + 1) % n) for i in range(n)] + [(i, n) for i in range(n)]
    groups = {0: [()]}
    def visit(start, occupied, face):
        if face:
            groups.setdefault(len(face), []).append(tuple(face))
        for j in range(start, 2 * n):
            a, b = edges[j]
            if occupied & ((1 << a) | (1 << b)):
                continue
            visit(j + 1, occupied | (1 << a) | (1 << b), face + [j])
    visit(0, 0, [])
    return groups


def binary_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            top = col.bit_length() - 1
            if top not in pivots:
                pivots[top] = col
                break
            col ^= pivots[top]
    return len(pivots)


def reduced_betti(n):
    groups = chain_groups(n)
    ranks = {}
    for k in sorted(groups):
        if k == 0:
            continue
        prior = {face: index for index, face in enumerate(groups[k - 1])}
        columns = []
        for face in groups[k]:
            col = 0
            for j in range(k):
                subface = face[:j] + face[j + 1:]
                col ^= 1 << prior[subface]
            columns.append(col)
        ranks[k] = binary_rank(columns)
    return {k - 1: len(groups[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
            for k in sorted(groups) if k > 0}


def main():
    for n in (4, 5, 7, 8, 10, 11, 13):
        betti = reduced_betti(n)
        expected_degree = n // 3
        expected_rank = n - 1 if n % 3 == 1 else n + 1
        assert betti.get(expected_degree) == expected_rank
        assert all(rank == 0 for degree, rank in betti.items() if degree != expected_degree)
        print(f'PASS n={n}, nonzero_degree={expected_degree}, rank_mod2={expected_rank}')
    print('FINITE_MOD2_CHECK_OK')


if __name__ == '__main__':
    main()
