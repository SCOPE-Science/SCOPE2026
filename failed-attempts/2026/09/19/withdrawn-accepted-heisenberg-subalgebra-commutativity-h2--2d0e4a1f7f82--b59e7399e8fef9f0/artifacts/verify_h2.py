from itertools import combinations, product

def inv_mod(a, q):
    return pow(a, -1, q)

def rank_mod(rows, q):
    a = [list(r) for r in rows if any(x % q for x in r)]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] % q), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = inv_mod(a[r][c] % q, q)
        a[r] = [(x * inv) % q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] % q:
                f = a[i][c] % q
                a[i] = [(a[i][j] - f * a[r][j]) % q for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def rref_subspaces(n, q):
    ans = []
    for d in range(n + 1):
        if d == 0:
            ans.append(())
            continue
        for pivots in combinations(range(n), d):
            free = []
            nonpivots = [j for j in range(n) if j not in pivots]
            for j in nonpivots:
                for i, p in enumerate(pivots):
                    if j > p:
                        free.append((i, j))
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * n for _ in range(d)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), value in zip(free, values):
                    rows[i][j] = value
                ans.append(tuple(tuple(row) for row in rows))
    return ans

def bracket(a, b, q):
    c = (a[0] * b[1] - a[1] * b[0]
         + a[2] * b[3] - a[3] * b[2]) % q
    return (0, 0, 0, 0, c)

def is_subalgebra(basis, q):
    d = len(basis)
    for i in range(d):
        for j in range(i + 1, d):
            c = bracket(basis[i], basis[j], q)
            if any(c) and rank_mod(list(basis) + [c], q) > d:
                return False
    return True

def has_nonzero_cross_bracket(a_basis, b_basis, q):
    return any(any(bracket(a, b, q)) for a in a_basis for b in b_basis)

def z_in_sum(a_basis, b_basis, q):
    z = (0, 0, 0, 0, 1)
    rows = list(a_basis) + list(b_basis)
    return rank_mod(rows + [z], q) == rank_mod(rows, q)

def formula(q):
    s = q**5 + 3*q**4 + 5*q**3 + 6*q**2 + 4*q + 6
    bad = q**4 * (q + 1) * (q**2 + 1) * (q**3 + 2*q**2 + 4*q + 1)
    return s, bad

def exhaustive(q):
    subalgebras = [b for b in rref_subspaces(5, q) if is_subalgebra(b, q)]
    bad = 0
    for a_basis in subalgebras:
        for b_basis in subalgebras:
            if has_nonzero_cross_bracket(a_basis, b_basis, q) and not z_in_sum(a_basis, b_basis, q):
                bad += 1
    return len(subalgebras), bad

if __name__ == "__main__":
    for q in (2, 3):
        observed = exhaustive(q)
        expected = formula(q)
        assert observed == expected, (q, observed, expected)
        s, bad = observed
        print(f"q={q}: subalgebras={s}, nonpermutable_ordered_pairs={bad}, permutable_ordered_pairs={s*s-bad}")
