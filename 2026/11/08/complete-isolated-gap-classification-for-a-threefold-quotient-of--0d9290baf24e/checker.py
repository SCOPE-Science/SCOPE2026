"""Exact independent finite checks of a three-generator semigroup identity.

Run: python3 checker.py
No nonstandard dependencies.
"""
from heapq import heappop, heappush


def apery_by_shortest_paths(k):
    m = 2 * k + 1
    generators = (m, 3 * k + 1, 3 * k + 2)
    distances = [None] * m
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        value, residue = heappop(queue)
        if value != distances[residue]:
            continue
        for generator in generators:
            new_value = value + generator
            new_residue = new_value % m
            old = distances[new_residue]
            if old is None or new_value < old:
                distances[new_residue] = new_value
                heappush(queue, (new_value, new_residue))
    return distances


def isolated_via_paths(k):
    m = 2 * k + 1
    distances = apery_by_shortest_paths(k)
    top = max(distances)
    membership = [n >= distances[n % m] for n in range(top + 2)]
    return [n for n in range(1, top) if not membership[n]
            and membership[n - 1] and membership[n + 1]]


def theoretical_apery(k):
    m = 2 * k + 1
    u, v = 3 * k + 1, 3 * k + 2
    entries = [None] * m
    for t in range(k + 1):
        entries[(t * u) % m] = t * u
    for t in range(1, k + 1):
        entries[(t * v) % m] = t * v
    assert all(x is not None for x in entries)
    return entries


def quotient_membership_by_original_coins(a, limit):
    # Independent enumeration of x*a+y*(a+1) in the needed range.
    present = [False] * (limit + 1)
    for x in range((3 * limit) // a + 1):
        for y in range((3 * limit - x * a) // (a + 1) + 1):
            number = x * a + y * (a + 1)
            if number % 3 == 0:
                present[number // 3] = True
    return present


number_of_apery_checks = 0
number_of_isolated_checks = 0
for k in range(2, 121):
    m = 2 * k + 1
    assert apery_by_shortest_paths(k) == theoretical_apery(k), k
    number_of_apery_checks += 1
    predicted = [3 * k * k - 2 * k - 2,
                 3 * k * k - k - 1,
                 3 * k * k - 1]
    assert isolated_via_paths(k) == predicted, k
    number_of_isolated_checks += 1

number_of_quotient_checks = 0
for k in range(2, 25):
    a = 3 * k + 1
    m = 2 * k + 1
    bound = 3 * k * k + 15
    by_original_coins = quotient_membership_by_original_coins(a, bound)
    distances = apery_by_shortest_paths(k)
    assert all(by_original_coins[n] == (n >= distances[n % m])
               for n in range(bound + 1)), k
    number_of_quotient_checks += 1

assert isolated_via_paths(1) == []
print('Independent Apéry shortest-path cases:', number_of_apery_checks)
print('Exact isolated-gap enumeration cases:', number_of_isolated_checks)
print('Direct quotient representation cases:', number_of_quotient_checks)
print('Boundary k=1 checked (no isolated gaps)')
print('All tests passed.')
