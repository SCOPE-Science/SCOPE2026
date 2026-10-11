from itertools import combinations, permutations, product
from math import factorial

EXPECTED_NAT = [1, 1, 2, 7, 40, 357, 4824]


def transitive_strict(n, rel):
    rel = set(rel)
    if any(a == b for a, b in rel):
        return False
    if any((b, a) in rel for a, b in rel):
        return False
    for a, b in tuple(rel):
        for bb, c in tuple(rel):
            if b == bb and (a, c) not in rel:
                return False
    return True


def naturally_labeled_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        rel = {pairs[t] for t in range(len(pairs)) if (mask >> t) & 1}
        if transitive_strict(n, rel):
            yield rel


def all_labeled_posets(n):
    pairs = list(combinations(range(n), 2))
    for states in product((0, 1, 2), repeat=len(pairs)):
        rel = set()
        for (i, j), s in zip(pairs, states):
            if s == 1:
                rel.add((i, j))
            elif s == 2:
                rel.add((j, i))
        if transitive_strict(n, rel):
            yield rel


def linear_extension_count(n, rel):
    ans = 0
    for p in permutations(range(n)):
        pos = {x: i for i, x in enumerate(p)}
        if all(pos[a] < pos[b] for a, b in rel):
            ans += 1
    return ans


def stirling2_table(N):
    S = [[0] * (N + 1) for _ in range(N + 1)]
    S[0][0] = 1
    for n in range(1, N + 1):
        for k in range(1, n + 1):
            S[n][k] = S[n - 1][k - 1] + k * S[n - 1][k]
    return S


def restricted_growth_strings(n):
    if n == 0:
        yield ()
        return
    def rec(prefix, mx):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for v in range(mx + 2):
            prefix.append(v)
            yield from rec(prefix, max(mx, v))
            prefix.pop()
    yield from rec([0], 0)


nat_counts = []
for n in range(7):
    c = sum(1 for _ in naturally_labeled_posets(n))
    nat_counts.append(c)
    assert c == EXPECTED_NAT[n], (n, c, EXPECTED_NAT[n])
print('natural_counts=', nat_counts)

# Independent identity: sum of numbers of linear extensions over all labeled posets
# equals n! times the number of naturally labeled posets.
for n in range(6):
    total_extensions = 0
    labeled_count = 0
    for rel in all_labeled_posets(n):
        labeled_count += 1
        total_extensions += linear_extension_count(n, rel)
    rhs = factorial(n) * EXPECTED_NAT[n]
    assert total_extensions == rhs, (n, total_extensions, rhs)
    print(f'n={n} labeled_posets={labeled_count} total_linear_extensions={total_extensions}')

# Injective orbit profile and repeated-coordinate Stirling transform.
a = [factorial(n) * EXPECTED_NAT[n] for n in range(7)]
S = stirling2_table(6)
b = [sum(S[n][k] * a[k] for k in range(n + 1)) for n in range(7)]
print('injective_profile=', a)
print('all_tuple_profile=', b)

# Independently count equality patterns by restricted-growth strings.
for n in range(7):
    by_blocks = [0] * (n + 1)
    for rgs in restricted_growth_strings(n):
        k = 0 if n == 0 else max(rgs) + 1
        by_blocks[k] += 1
    assert by_blocks == S[n][:n+1], (n, by_blocks, S[n][:n+1])
    assert sum(by_blocks[k] * a[k] for k in range(n + 1)) == b[n]

print('VERIFY_OK')
