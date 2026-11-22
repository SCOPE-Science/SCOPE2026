#!/usr/bin/env python3
"""Exact finite verification for a two-gateway rooted-tree containment theorem.

Uses only Python's standard library.  Run: python3 check_gate_reversals.py
All exclusion decisions are integer algebra, not numerical root sampling.
"""
from collections import deque
from math import comb
from fractions import Fraction


def compositions(n):
    """Generate every ordered positive-integer composition of n once."""
    if n == 0:
        yield ()
        return
    for mask in range(1 << (n - 1)):
        parts = []
        size = 1
        for j in range(n - 1):
            if mask & (1 << j):
                parts.append(size)
                size = 1
            else:
                size += 1
        parts.append(size)
        yield tuple(parts)


def compositions_recursive(n):
    """Second, structurally different generator, used for cross-checking."""
    if n == 0:
        yield ()
    else:
        for first in range(1, n + 1):
            for remainder in compositions_recursive(n - first):
                yield (first,) + remainder


def profiles(branch_vertices):
    """Width vector at successive positive distances from a fixed source."""
    return [(1,) + comp for comp in compositions(branch_vertices - 1)]


def polynomial_difference(left, right):
    """Difference of depth polynomials with their common gateway p removed."""
    coeff = [(left[k] if k < len(left) else 0)
             - (right[k] if k < len(right) else 0)
             for k in range(max(len(left), len(right)))]
    while coeff and coeff[-1] == 0:
        coeff.pop()
    while coeff and coeff[0] == 0:
        coeff.pop(0)
    return coeff


def variation_bound_unit_interval(c):
    """Descartes bound after x=t/(1+t), using only integer coefficients."""
    if not c:
        return 0
    d = len(c) - 1
    transformed = [sum(c[i] * comb(d-i, j-i) for i in range(j+1))
                   for j in range(d+1)]
    signs = [1 if z > 0 else -1 for z in transformed if z]
    return sum(signs[i] != signs[i-1] for i in range(1, len(signs)))


def integral_scaled_evaluation(c, num, den):
    """Exactly den**degree times a polynomial's value at num/den."""
    d = len(c) - 1
    return sum(v * num**j * den**(d-j) for j, v in enumerate(c))


def graph_depth_profiles(edges):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
    depth = {0: 0}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj.get(u, ()):
            assert v not in depth
            depth[v] = depth[u] + 1
            q.append(v)
    assert len(depth) == len(edges) + 1
    first, second = {}, {}
    for root, result in ((1, first), (7, second)):
        q = deque([root])
        while q:
            u = q.popleft()
            result[depth[u]] = result.get(depth[u], 0) + 1
            q.extend(adj.get(u, ()))
    return (tuple(first.get(k, 0) for k in range(1, max(first)+1)),
            tuple(second.get(k, 0) for k in range(1, max(second)+1)))


EXPECTED = {3: 0, 4: 1, 5: 2, 6: 6, 7: 13, 8: 32,
            9: 70, 10: 160, 11: 348, 12: 768, 13: 1656}
profiles_by_size = {m: profiles(m) for m in range(1, 14)}
for m in range(1, 13):
    assert set(compositions(m)) == set(compositions_recursive(m))
    assert len(profiles_by_size[m]) == (1 if m == 1 else 2**(m - 2))

checked = 0
for total_vertices in range(3, 14):
    branch_total = total_vertices - 1
    count = 0
    for left_size in range(1, branch_total):
        right_size = branch_total - left_size
        for left in profiles_by_size[left_size]:
            for right in profiles_by_size[right_size]:
                if left >= right:
                    continue  # Each unordered pair of distinct profiles once.
                count += 1
                c = polynomial_difference(left, right)
                assert variation_bound_unit_interval(c) <= 1, (left, right, c)
    assert count == EXPECTED[total_vertices], (total_vertices, count)
    checked += count
assert checked == 3056

# Independently obtain witness branch widths from an explicit 14-vertex graph.
witness_edges = [(0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (0, 7), (7, 8), (7, 9), (8, 10), (10, 11),
                 (11, 12), (11, 13)]
a, b = graph_depth_profiles(witness_edges)
assert a == (1, 1, 4) and b == (1, 2, 1, 1, 2)
assert len(witness_edges) + 1 == 14
c = polynomial_difference(a, b)
assert c == [-1, 3, -1, -2]
# The full difference is -p^2*(2p-1)*(p^2+p-1).
# This list is the quotient by p^2, in increasing-power order.
assert c == [-1, 3, -1, -2]
assert variation_bound_unit_interval(c) == 2
assert integral_scaled_evaluation(c, 1, 4) < 0
assert integral_scaled_evaluation(c, 11, 20) > 0
assert integral_scaled_evaluation(c, 3, 4) < 0
# Independent full 2**13 edge-state calculation at rational probabilities.
# This corroborates both gateway-benefit formulas without using path sums.
def infected_count(mask, closed_gateway=None):
    adjacency = {}
    for j, (u, v) in enumerate(witness_edges):
        if j != closed_gateway and (mask & (1 << j)):
            adjacency.setdefault(u, []).append(v)
    seen, queue = {0}, deque([0])
    while queue:
        for v in adjacency.get(queue.popleft(), ()):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen)

for transmission in (Fraction(1, 4), Fraction(11, 20), Fraction(3, 4)):
    expected = [Fraction(0), Fraction(0), Fraction(0)]
    for mask in range(1 << len(witness_edges)):
        k = mask.bit_count()
        probability = transmission**k * (1-transmission)**(len(witness_edges)-k)
        expected[0] += probability * infected_count(mask)
        expected[1] += probability * infected_count(mask, 0)
        expected[2] += probability * infected_count(mask, 6)
    ga = transmission + transmission**2 + 4*transmission**3
    gb = transmission + 2*transmission**2 + transmission**3 + transmission**4 + 2*transmission**5
    assert expected[0]-expected[1] == ga
    assert expected[0]-expected[2] == gb

print('NO_TWO_REVERSALS_ON_AT_MOST_13_VERTICES', checked)
print('WITNESS_SIZE', len(witness_edges) + 1)
print('VERIFY_OK')
