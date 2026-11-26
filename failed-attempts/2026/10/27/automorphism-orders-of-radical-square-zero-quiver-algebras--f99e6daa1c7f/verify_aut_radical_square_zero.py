from itertools import permutations

# Basis: vertices first, then arrows. Products of arrows are zero.
def invertible_columns_gf2(n):
    def rec(chosen, span):
        if len(chosen) == n:
            yield tuple(chosen)
            return
        for v in range(1 << n):
            if v not in span:
                newspan = set(span)
                for x in span:
                    newspan.add(x ^ v)
                yield from rec(chosen + [v], newspan)
    yield from rec([], {0})

def multiplication_table(n_vertices, arrows):
    n = n_vertices + len(arrows)
    mult = [[0] * n for _ in range(n)]
    for v in range(n_vertices):
        mult[v][v] = 1 << v
    for i, (s, t) in enumerate(arrows):
        a = n_vertices + i
        mult[s][a] = 1 << a
        mult[a][t] = 1 << a
    return mult

def product_vec(x, y, mult, n):
    out = 0
    for i in range(n):
        if (x >> i) & 1:
            for j in range(n):
                if (y >> j) & 1:
                    out ^= mult[i][j]
    return out

def apply_columns(cols, x):
    out = 0
    i = 0
    while x:
        if x & 1:
            out ^= cols[i]
        x >>= 1
        i += 1
    return out

def brute_force_aut_count(n_vertices, arrows):
    n = n_vertices + len(arrows)
    mult = multiplication_table(n_vertices, arrows)
    count = 0
    for cols in invertible_columns_gf2(n):
        if all(apply_columns(cols, mult[i][j]) == product_vec(cols[i], cols[j], mult, n)
               for i in range(n) for j in range(n)):
            count += 1
    return count

def formula_gf2(n_vertices, arrows):
    multiplicity = {}
    for s, t in arrows:
        multiplicity[s, t] = multiplicity.get((s, t), 0) + 1
    e = len(arrows)
    loops = sum(s == t for s, t in arrows)
    vertex_symmetries = sum(
        all(multiplicity.get((u, v), 0) == multiplicity.get((p[u], p[v]), 0)
            for u in range(n_vertices) for v in range(n_vertices))
        for p in permutations(range(n_vertices))
    )
    gl_order = {0: 1, 1: 1, 2: 6}
    arrow_block_factor = 1
    for m in multiplicity.values():
        arrow_block_factor *= gl_order[m]
    return (2 ** (e - loops)) * vertex_symmetries * arrow_block_factor

CASES = [
    (2, [(0, 1)]),                 # one arrow
    (2, [(0, 1), (0, 1)]),         # two parallel arrows
    (2, [(0, 1), (1, 0)]),         # directed 2-cycle
    (2, [(0, 0), (0, 1)]),         # one loop and one non-loop arrow
    (2, []),                       # two isolated vertices
    (1, [(0, 0), (0, 0)]),         # one vertex with two loops
]
EXPECTED = [2, 24, 8, 2, 2, 6]
for (n_vertices, arrows), expected in zip(CASES, EXPECTED):
    observed = brute_force_aut_count(n_vertices, arrows)
    predicted = formula_gf2(n_vertices, arrows)
    assert observed == predicted == expected, (n_vertices, arrows, observed, predicted, expected)
print("VERIFY_OK: six exhaustive F_2 cases agree with the formula")
