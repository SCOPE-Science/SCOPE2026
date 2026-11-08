"""Exhaustive labelled-state checks for minority dynamics on complete split graphs.

Usage: python3 artifacts/check_attractors.py
Uses only the Python standard library.
"""
import math
import sys

sys.setrecursionlimit(100000)


def pred(a, b):
    n = a + b
    if b >= a:
        return [1, 1]
    if n % 2 == 0:
        return [1] * (2 * math.comb(a, (a - b) // 2))
    if b == 1:
        return [2 * math.comb(a + 1, a // 2)]
    return [math.comb(a + 1, (a - b + 1) // 2)] * 2


def neighborhoods(a, b):
    n = a + b
    return [tuple(w for w in range(n) if w != v and (v < a or w < a))
            for v in range(n)]


def update(mask, v, nei):
    opposite = sum(((mask >> w) ^ (mask >> v)) & 1 for w in nei[v])
    return mask ^ (1 << v) if opposite * 2 <= len(nei[v]) else mask


def cut(mask, nei):
    return sum((((mask >> v) ^ (mask >> w)) & 1)
               for v in range(len(nei)) for w in nei[v] if w > v)


def components(succ):
    index = 0
    indices = {}
    low = {}
    stack = []
    onstack = set()
    comps = []

    def visit(v):
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in succ[v]:
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = set()
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.add(w)
                if w == v:
                    break
            comps.append(comp)

    for v in range(len(succ)):
        if v not in indices:
            visit(v)
    return comps


def run():
    instances = 0
    states = 0
    total_recurrent = 0
    for a in range(2, 9):
        for b in range(1, 9):
            if a + b > 12:
                continue
            n = a + b
            nei = neighborhoods(a, b)
            successors = [set(update(s, v, nei) for v in range(n))
                          for s in range(1 << n)]
            recurrent = [c for c in components(successors)
                         if all(w in c for s in c for w in successors[s])]
            observed_sizes = sorted(len(c) for c in recurrent)
            expected_sizes = sorted(pred(a, b))
            assert observed_sizes == expected_sizes, (a, b, observed_sizes, expected_sizes)
            maximum_cut = max(cut(s, nei) for s in range(1 << n))
            all_maxima = {s for s in range(1 << n) if cut(s, nei) == maximum_cut}
            all_recurrent = set().union(*recurrent)
            assert all_recurrent == all_maxima, (a, b, all_recurrent ^ all_maxima)
            expected_maxcut = a * b if b >= a else (n * n) // 4
            assert maximum_cut == expected_maxcut, (a, b, maximum_cut, expected_maxcut)
            instances += 1
            states += 1 << n
            total_recurrent += len(all_recurrent)
    print('ATTRACTOR_CHECK_OK')
    print('instances', instances)
    print('labelled_state_examinations', states)
    print('recurrent_configurations_across_instances', total_recurrent)
    print('all recurrent sets equal the maximum-cut sets; class sizes agree')

if __name__ == '__main__':
    run()
