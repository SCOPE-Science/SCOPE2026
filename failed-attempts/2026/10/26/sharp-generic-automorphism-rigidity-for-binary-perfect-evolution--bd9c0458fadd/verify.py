"""Exhaustive checks for binary perfect evolution-algebra symmetry statistics.
Run: python verify.py
No third-party packages are required.
"""
from itertools import permutations


def nonsingular(rows, n):
    rows = list(rows)
    for j in range(n):
        pivot = next((i for i in range(j, n) if (rows[i] >> j) & 1), None)
        if pivot is None:
            return False
        rows[j], rows[pivot] = rows[pivot], rows[j]
        for i in range(n):
            if i != j and ((rows[i] >> j) & 1):
                rows[i] ^= rows[j]
    return True


def fixes(mask, perm, n):
    # perm acts on both row and column coordinates of the structure matrix.
    for i in range(n):
        for j in range(n):
            if ((mask >> (i*n+j)) ^ (mask >> (perm[i]*n+perm[j]))) & 1:
                return False
    return True


def algebra_automorphism(Arows, columns, n):
    # Multiply images by the original evolution-algebra multiplication table;
    # check all images of natural-basis products directly.
    for i in range(n):
        for j in range(n):
            prod = 0
            overlap = columns[i] & columns[j]
            for k in range(n):
                if (overlap >> k) & 1:
                    prod ^= Arows[k]
            desired = 0
            if i == j:
                for k in range(n):
                    if (Arows[i] >> k) & 1:
                        desired ^= columns[k]
            if prod != desired:
                return False
    return True


def check(n):
    perms = list(permutations(range(n)))
    trans = [p for p in perms if sum(p[i] != i for i in range(n)) == 2]
    nons = event = event_one_trans = total_trans = exact_c2 = 0
    trans_counts = [0]*len(trans)
    group_sizes = {}
    maps = []
    if n <= 3:
        for t in range(1 << (n*n)):
            trows = [(t >> (i*n)) & ((1 << n)-1) for i in range(n)]
            if nonsingular(trows, n):
                cols = [sum(((trows[i] >> j) & 1) << i for i in range(n))
                        for j in range(n)]
                maps.append(cols)
    for mask in range(1 << (n*n)):
        rows = [(mask >> (i*n)) & ((1 << n)-1) for i in range(n)]
        if not nonsingular(rows, n):
            continue
        nons += 1
        stabilizer = [p for p in perms if fixes(mask, p, n)]
        if n <= 3:
            by_products = sum(algebra_automorphism(rows, cols, n)
                              for cols in maps)
            assert by_products == len(stabilizer), (n, mask, by_products, len(stabilizer))
        t_found = [p for p in trans if p in stabilizer]
        if len(stabilizer) > 1: event += 1
        if len(stabilizer) == 2: exact_c2 += 1
        if t_found: event_one_trans += 1
        total_trans += len(t_found)
        for i,p in enumerate(trans):
            if p in stabilizer: trans_counts[i] += 1
        group_sizes[len(stabilizer)] = group_sizes.get(len(stabilizer),0)+1
    expected_nons = 1
    for k in range(n):
        expected_nons *= (2**n - 2**k)
    assert nons == expected_nons, (n, nons, expected_nons)
    # For every transposition, the exact conditional centralizer probability is
    # 2^(-2n+1)/[(1-2^(-n+1))(1-2^(-n))].
    if n >= 2:
        # Number of invertible matrices commuting with a transposition equals
        # 2^{2n-3} |GL_{n-2}(F_2)|.
        expected_count = 2**(2*n-3)
        for k in range(n-2):
            expected_count *= (2**(n-2) - 2**k)
        assert all(x == expected_count for x in trans_counts), (n,trans_counts,expected_count)
    assert event >= event_one_trans
    print('dimension=',n,'GL_count=',nons,'nontrivial=',event,
          'at_least_one_transposition=',event_one_trans,'C2=',exact_c2,
          'sum_transposition_stabilizer=',total_trans,'group_sizes=',group_sizes)

for n in range(1,5):
    check(n)
print('ALL_BINARY_EVOLUTION_SYMMETRY_CHECKS_PASSED')
