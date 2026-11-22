"""Independent finite checks for Fourier multipliers of proper graph colorings.
Uses exact residue counts for cyclic groups and integers for the Klein group.
No symbolic theorem is inferred from the finite checks.
"""
from itertools import product
from math import factorial


def graph(cycle_len, leaves=()):
    # cycle occupies 0,...,cycle_len-1; each leaf attaches to given vertex
    edges = [(i, (i + 1) % cycle_len) for i in range(cycle_len)]
    edges += [(parent, cycle_len + t) for t, parent in enumerate(leaves)]
    return cycle_len + len(leaves), edges


def colorings(n, edges, q):
    for x in product(range(q), repeat=n):
        if all(x[u] != x[v] for u, v in edges):
            yield x


def integer_fourier_value(x_list, freq, q, klein):
    if klein:
        return sum((-1) ** sum((a & b).bit_count() for a, b in zip(freq, x)) for x in x_list)
    counts = [0] * q
    for x in x_list:
        counts[sum(a * b for a, b in zip(freq, x)) % q] += 1
    if q in (3, 5):
        assert len(set(counts[1:])) == 1, ('Noninteger Fourier coefficient', q, freq, counts)
        return counts[0] - counts[1]
    if q == 4:
        assert counts[1] == counts[3], ('Noninteger Fourier coefficient', q, freq, counts)
        return counts[0] - counts[2]
    raise NotImplementedError


def predict(freq, c, leaves, q, klein):
    op = (lambda a, b: a ^ b) if klein else (lambda a, b: (a + b) % q)
    tot = 0
    for u in freq:
        tot = op(tot, u)
    if tot != 0:
        return 0
    # Remove closing edge and root the remaining tree at 0.
    n, edges = graph(c, leaves)
    adjacency = [[] for _ in range(n)]
    for a, b in edges[0:c-1] + edges[c:]:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = [-1] * n
    order = [0]
    for v in order:
        for u in adjacency[v]:
            if u == parent[v]:
                continue
            assert u not in order
            parent[u] = v
            order.append(u)
    assert len(order) == n
    subsum = list(freq)
    for u in reversed(order[1:]):
        subsum[parent[u]] = op(subsum[parent[u]], subsum[u])
    s_cycle = [subsum[v] for v in range(1, c)] + [0]
    tree_factor = 1
    for v in range(c, n):
        tree_factor *= (q - 1) if subsum[v] == 0 else -1
    cycle_sum = 0
    for t in range(q):
        p = 1
        for s in s_cycle:
            p *= (q - 1) if op(s, t) == 0 else -1
        cycle_sum += p
    return tree_factor * cycle_sum


def test(q, c, leaves=(), klein=False):
    n, edges = graph(c, leaves)
    xs = list(colorings(n, edges, q))
    count = 0
    zeros_balanced = 0
    nonzero = 0
    for freq in product(range(q), repeat=n):
        got = integer_fourier_value(xs, freq, q, klein)
        expected = predict(freq, c, leaves, q, klein)
        assert got == expected, (q, c, leaves, klein, freq, got, expected)
        if got:
            nonzero += 1
        elif (sum(freq) % q if not klein else __import__('functools').reduce(lambda a,b: a^b, freq, 0)) == 0:
            zeros_balanced += 1
        count += 1
    if c % q == 1:
        m = (c - 1) // q
        z = factorial(c) // (factorial(m+1) * factorial(m)**(q-1))
    else:
        z = 0
    rank = q**(n-1) - q**(n-c)*z
    assert nonzero == rank, (q, c, leaves, klein, nonzero, rank)
    assert zeros_balanced == q**(n-c)*z
    print('PASS', 'Klein' if klein else 'cyclic', 'q', q, 'cycle', c, 'leaves', leaves,
          'frequencies', count, 'rank', rank, 'balanced-zero', zeros_balanced)
    return count


def test_selected(q, c, freqs):
    n, edges = graph(c)
    xs = list(colorings(n, edges, q))
    for freq in freqs:
        assert integer_fourier_value(xs, freq, q, False) == predict(freq, c, (), q, False)
    print('PASS selected', 'q', q, 'cycle', c, len(freqs))

if __name__ == '__main__':
    total = 0
    for args in [
        (3, 3, ()), (3, 4, ()), (3, 4, (0,)), (3, 4, (0, 2)),
        (3, 5, ()), (4, 3, ()), (4, 5, ()), (4, 4, (0,)),
        (5, 3, ()), (5, 4, ()),
    ]:
        total += test(*args)
    total += test(4, 5, (), True)
    # q=5 length 6 is the first resonant cycle, with direct sample frequencies.
    test_selected(5, 6, [(0,1,2,3,4,0), (0,0,0,0,0,0), (1,2,3,4,0,0), (1,1,1,1,1,0)])
    print('PASS TOTAL', total, 'exhaustive frequency comparisons')
