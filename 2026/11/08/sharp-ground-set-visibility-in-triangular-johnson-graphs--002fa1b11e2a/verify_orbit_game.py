"""Exact finite k-pebble orbit refinement for triangular graphs J(n,2).

Reproducible with Python 3 standard library. It enumerates all orbits of
ordered k-tuples of graph vertices under ground-set permutations, then
computes the greatest back-and-forth equivalence by finite refinement.
"""
from itertools import combinations, product
from functools import lru_cache

@lru_cache(None)
def canonical(edges):
    if not edges:
        return ()
    codes = []
    for swaps in product((0, 1), repeat=len(edges)):
        labels = {}
        next_label = 0
        pairs = []
        for (a, b), sw in zip(edges, swaps):
            u, v = (b, a) if sw else (a, b)
            pair = []
            for x in (u, v):
                if x not in labels:
                    labels[x] = next_label
                    next_label += 1
                pair.append(labels[x])
            pairs.append(tuple(sorted(pair)))
        codes.append(tuple(pairs))
    return min(codes)

@lru_cache(None)
def tuple_orbits(n, k):
    states = {()}
    for _ in range(k):
        output = set()
        for state in states:
            t = len({v for pair in state for v in pair})
            for a, b in combinations(range(t + 2), 2):
                if t + (a >= t) + (b >= t) <= n:
                    output.add(canonical(state + ((a, b),)))
        states = output
    return frozenset(states)

@lru_cache(None)
def successors(state, n, coordinate):
    others = canonical(state[:coordinate] + state[coordinate + 1:])
    t = len({v for pair in others for v in pair})
    result = set()
    for a, b in combinations(range(t + 2), 2):
        if t + (a >= t) + (b >= t) <= n:
            new_state = others[:coordinate] + ((a, b),) + others[coordinate:]
            result.add(canonical(new_state))
    return frozenset(result)

def atomic_diagram(state):
    return tuple(
        2 if state[i] == state[j] else int(bool(set(state[i]) & set(state[j])))
        for i in range(len(state))
        for j in range(i + 1, len(state))
    )

def normalize(signatures):
    codebook = {code: i for i, code in enumerate(sorted(set(signatures.values())))}
    return {state: codebook[code] for state, code in signatures.items()}

def check_width(k, ns):
    all_states = [(n, state) for n in ns for state in tuple_orbits(n, k)]
    colors = normalize({item: atomic_diagram(item[1]) for item in all_states})
    rounds = 0
    while True:
        new_colors = normalize({
            (n, state): (
                colors[n, state],
                tuple(tuple(sorted({colors[n, s] for s in successors(state, n, i)}))
                      for i in range(k)),
            ) for (n, state) in all_states
        })
        rounds += 1
        if new_colors == colors:
            break
        colors = new_colors
        if rounds > 100:
            raise AssertionError('refinement did not stabilize')
    checks = 0
    by_n = {n: {colors[n, state] for state in tuple_orbits(n, k)} for n in ns}
    for a, b in combinations(ns, 2):
        same_theory = by_n[a] == by_n[b]
        expected = min(a, 2*k) == min(b, 2*k)
        assert same_theory == expected, (k, a, b, same_theory, expected)
        checks += 1
    print(f'k={k}: {len(all_states)} orbit positions, {rounds} refinement rounds, '
          f'{checks} distinct-order comparisons, zero discrepancies')
    print('  orbits by order: '+', '.join(f'{n}:{len(tuple_orbits(n,k))}' for n in ns))
    return checks

if __name__ == '__main__':
    total = 0
    total += check_width(2, tuple(range(3, 9)))
    total += check_width(3, tuple(range(3, 9)))
    total += check_width(4, tuple(range(4, 10)))
    print(f'PASS: {total} complete cross-order orbit-game comparisons.')
