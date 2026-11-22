#!/usr/bin/env python3
"""Reproducible exact checks for shortest acyclic-orientation flip sequences on K_{2,n}.

Three independent mechanisms are compared: formal-series recurrence, monotone bitset
DP, and full undirected breadth-first search (the latter allows all legal reversals).
"""
from collections import deque
from math import factorial


def acyclic(mask, n):
    forward = reverse = False
    for i in range(n):
        bits = (mask >> (2 * i)) & 3
        forward |= (bits == 1)
        reverse |= (bits == 2)
    return not (forward and reverse)


def recurrence(nmax):
    s = [factorial(2 * k) // (2**k * factorial(k)) for k in range(nmax + 1)]
    f = [1]
    for n in range(1, nmax + 1):
        # F = S / (2-S) = S + (S-1) F
        f.append(s[n] + sum(s[k] * f[n-k] for k in range(1, n+1)))
    return [factorial(n)*f[n] for n in range(nmax+1)]


def monotone_count(n):
    last = (1 << (2*n)) - 1
    ways = [0] * (last + 1)
    ways[0] = 1
    for mask in range(last + 1):
        if not ways[mask]:
            continue
        for bit in range(2*n):
            if not ((mask >> bit) & 1):
                nxt = mask | (1 << bit)
                if acyclic(nxt, n):
                    ways[nxt] += ways[mask]
    return ways[last]


def full_flip_bfs(n):
    last = (1 << (2*n)) - 1
    legal = {mask for mask in range(last+1) if acyclic(mask,n)}
    dist = {0:0}
    count = {0:1}
    queue = deque([0])
    while queue:
        mask = queue.popleft()
        for bit in range(2*n):
            nxt = mask ^ (1<<bit)    # ordinary swaps in either orientation, no monotonicity
            if nxt not in legal:
                continue
            if nxt not in dist:
                dist[nxt] = dist[mask] + 1
                count[nxt] = 0
                queue.append(nxt)
            if dist[nxt] == dist[mask]+1:
                count[nxt] += count[mask]
    assert len(dist) == len(legal), (n,len(dist),len(legal))
    return dist[last], count[last], len(legal)


def main():
    target = recurrence(8)
    print('n  series  independent_monotone_DP  legal_vertices  legal_edges  full_graph_BFS')
    for n in range(1,9):
        independent = monotone_count(n)
        legal_n = sum(acyclic(mask,n) for mask in range(1<<(2*n)))
        edges = sum(acyclic(mask,n) and acyclic(mask^(1<<bit),n)
                    for mask in range(1<<(2*n)) for bit in range(2*n)) // 2
        assert legal_n == 2*3**n - 2**n
        assert edges == 4*n*3**(n-1)
        assert independent == target[n]
        bfs_result = '-'
        if n <= 7:
            distance, count, visited = full_flip_bfs(n)
            assert distance == 2*n and count == target[n] and visited == legal_n
            bfs_result = f'distance={distance}, paths={count}'
        print(f'{n}  {target[n]}  {independent}  {legal_n}  {edges}  {bfs_result}')
    print('ALL INDEPENDENT CHECKS PASS')


if __name__ == '__main__':
    main()
