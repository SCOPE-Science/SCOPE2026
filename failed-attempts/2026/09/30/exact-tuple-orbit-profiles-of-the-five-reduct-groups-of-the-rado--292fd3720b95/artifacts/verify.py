from math import comb


def edge_list(k):
    return [(i, j) for i in range(k) for j in range(i + 1, k)]


def cut_mask(k, subset_mask):
    out = 0
    for bit, (i, j) in enumerate(edge_list(k)):
        if ((subset_mask >> i) & 1) ^ ((subset_mask >> j) & 1):
            out |= 1 << bit
    return out


def translations(kind, k):
    t = {0}
    if kind in ("Switch", "Both"):
        t = {cut_mask(k, s) for s in range(1 << k)}
    if kind in ("Comp", "Both"):
        all_ones = (1 << comb(k, 2)) - 1
        t |= {x ^ all_ones for x in tuple(t)}
    return t


def injective_formula(kind, k):
    if kind == "Aut":
        return 1 << comb(k, 2)
    if kind == "Comp":
        return 1 if k <= 1 else 1 << (comb(k, 2) - 1)
    if kind == "Switch":
        return 1 if k == 0 else 1 << comb(k - 1, 2)
    if kind == "Both":
        return 1 if k <= 2 else 1 << (comb(k - 1, 2) - 1)
    if kind == "Sym":
        return 1
    raise ValueError(kind)


def stirling2(n, k):
    row = [1]
    for i in range(1, n + 1):
        nxt = [0] * (i + 1)
        for j in range(1, i + 1):
            nxt[j] = (row[j - 1] if j - 1 < len(row) else 0) + (j * row[j] if j < len(row) else 0)
        row = nxt
    return row[k] if k < len(row) else 0


# Exhaustive graph-orbit check on all labeled graphs through five vertices.
for k in range(6):
    graph_count = 1 << comb(k, 2)
    for kind in ("Aut", "Comp", "Switch", "Both"):
        trans = translations(kind, k)
        reps = {min(graph ^ t for t in trans) for graph in range(graph_count)}
        assert len(reps) == injective_formula(kind, k), (kind, k, len(reps))

expected = {
    "Aut": [1, 1, 3, 15, 127, 1895, 53071, 2953575, 337064047],
    "Comp": [1, 1, 2, 8, 64, 948, 26536, 1476788, 168532024],
    "Switch": [1, 1, 2, 6, 28, 210, 2716, 66698, 3369908],
    "Both": [1, 1, 2, 5, 18, 113, 1374, 33381, 1685018],
    "Sym": [1, 1, 2, 5, 15, 52, 203, 877, 4140],
}

for kind, target in expected.items():
    got = []
    for n in range(9):
        got.append(sum(stirling2(n, k) * injective_formula(kind, k) for k in range(n + 1)))
    assert got == target, (kind, got, target)

print("VERIFY_OK")
