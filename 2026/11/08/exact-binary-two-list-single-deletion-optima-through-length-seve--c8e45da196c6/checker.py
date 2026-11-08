#!/usr/bin/env python3
"""Exact, standard-library verification of short binary list-two deletion codes."""
import json
from pathlib import Path


def incidence(n):
    count = 1 << n
    matrix = [[0] * count for _ in range(1 << (n-1))]
    for j in range(count):
        word = format(j, f'0{n}b')
        for k in range(n):
            y = int(word[:k] + word[k + 1:], 2)
            matrix[y][j] = 1
    return matrix


def check_instance(entry, scale, capacity=2):
    n = entry['n']
    N, M = 1 << n, 1 << (n - 1)
    A = incidence(n)
    code = entry['code_indices']
    assert len(code) == entry['optimum']
    assert len(set(code)) == len(code)
    assert all(type(j) is int and 0 <= j < N for j in code)
    assert all(sum(A[i][j] for j in code) <= capacity for i in range(M))
    vt = [0] * (n + 1)
    for j in range(N):
        word = format(j, f'0{n}b')
        s = sum((i + 1) * int(c) for i, c in enumerate(word)) % (n + 1)
        vt[s] += 1
    if 'vt_class_sizes' in entry:
        assert vt == entry['vt_class_sizes']
    target = len(code) + 1
    nodes, leaves = [0], [0]

    def recurse(node, excluded, included):
        nodes[0] += 1
        assert not (excluded & included)
        remaining = set(range(N)) - excluded - included
        capacities = [capacity - sum(A[i][j] for j in included) for i in range(M)]
        if 'branch' in node:
            j = node['branch']
            assert type(j) is int and j in remaining
            assert set(node) == {'branch', 'one', 'zero'}
            recurse(node['one'], excluded, included | {j})
            recurse(node['zero'], excluded | {j}, included)
            return
        leaves[0] += 1
        if 'conflict' in node:
            assert set(node) == {'conflict'}
            k = node['conflict']
            assert type(k) is int and 0 <= k < M and capacities[k] < 0
            return
        if 'count' in node:
            assert set(node) == {'count'} and node['count'] is True
            assert len(included) + len(remaining) < target
            return
        assert set(node) == {'dual'} and min(capacities) >= 0
        payload = node['dual']
        assert set(payload) == {'a', 'b'}
        alpha = [0] * M
        beta = [0] * N
        for i, value in payload['a']:
            assert type(i) is int and 0 <= i < M and alpha[i] == 0
            assert type(value) is int and value > 0
            alpha[i] = value
        for j, value in payload['b']:
            assert type(j) is int and j in remaining and beta[j] == 0
            assert type(value) is int and value > 0
            beta[j] = value
        # This is the exact dual feasibility inequality, checked for EVERY remaining word.
        for j in remaining:
            assert sum(alpha[i] for i in range(M) if A[i][j]) + beta[j] >= scale
        # In every branch, no integral completion can reach 'target'.
        cost = len(included) * scale + sum(capacities[i] * alpha[i] for i in range(M)) + sum(beta)
        assert cost < target * scale, (n, cost, target * scale)

    recurse(entry['upper_tree'], set(), set())
    return n, len(code), nodes[0], leaves[0], sorted(vt)[-2:]


def main():
    root = Path(__file__).resolve().parent
    data = json.loads((root / 'certificate.json').read_text(encoding='utf-8'))
    assert data['schema_version'] == 1
    assert data['model'] == 'binary exact-one-deletion list-size-two'
    scale = data['scale']
    assert type(scale) is int and scale > 0
    assert [v['n'] for v in data['instances']] == list(range(2, 8))
    assert [v['optimum'] for v in data['instances']] == [3, 4, 7, 12, 19, 33]
    for entry in data['instances']:
        n, size, nodes, leaves, two = check_instance(entry, scale)
        print(f'n={n}: optimum={size}, upper-proof nodes={nodes}, leaves={leaves}, best-two-VT={sum(two)}')
    unique = data['unique_n7']
    assert (unique['n'], unique['capacity'], unique['optimum']) == (7, 1, 16)
    n, size, nodes, leaves, _ = check_instance(unique, scale, capacity=1)
    assert (nodes, leaves) == (25, 13)
    print(f'n={n}: unique-correction optimum={size}, upper-proof nodes={nodes}, leaves={leaves}')
    print('VERIFY_OK: all codewords, all dual inequalities, all exhaustive proof branches')

if __name__ == '__main__':
    main()
