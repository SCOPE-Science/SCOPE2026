"""Second implementation using sets of bipartite edges, not partial permutations.
Enumerates matchings and directly tests which individual edge replacements are slides.
"""
from collections import deque
from itertools import combinations
from math import factorial
from check_formula import potential

def enumerate_matchings(n):
    edges = [(i, j) for i in range(n) for j in range(n)]
    # A direct matching census from edge subsets; no permutation generator.
    for subset in combinations(edges, n - 1):
        if len({a for a, _ in subset}) == n - 1 and len({b for _, b in subset}) == n - 1:
            yield frozenset(subset)

def row_encoding(matching, n):
    answer = [-1] * n
    for r, c in matching:
        answer[r] = c
    return tuple(answer)

def is_slide(a, b):
    removed = a - b
    added = b - a
    if len(removed) != 1 or len(added) != 1:
        return False
    (u, v), = removed
    (s, t), = added
    return u == s or v == t

def main():
    for n in range(2, 6):
        states = tuple(enumerate_matchings(n))
        assert len(states) == n * n * factorial(n - 1)
        pos = {s: i for i, s in enumerate(states)}
        adjacency = [[] for _ in states]
        for i, m in enumerate(states):
            for edge in m:
                rest = m - {edge}
                rows = {r for r, _ in rest}
                cols = {c for _, c in rest}
                for r in range(n):
                    if r in rows:
                        continue
                    for c in range(n):
                        if c in cols or (r, c) == edge:
                            continue
                        target = rest | {(r, c)}
                        if target in pos and is_slide(m, target):
                            adjacency[i].append(pos[target])
            assert len(adjacency[i]) == 2 * (n - 1)
            assert len(set(adjacency[i])) == len(adjacency[i])
        origin = frozenset((i, i) for i in range(n - 1))
        start = pos[origin]
        visited = {start: 0}
        queue = deque([start])
        while queue:
            i = queue.popleft()
            for j in adjacency[i]:
                if j not in visited:
                    visited[j] = visited[i] + 1
                    queue.append(j)
        assert len(visited) == len(states)
        for i, m in enumerate(states):
            assert visited[i] == potential(row_encoding(m, n))
        assert max(visited.values()) == 3 * n // 2 - 1
        print(f'PASS direct edge census n={n} states={len(states)} edges={sum(map(len, adjacency)) // 2} diameter={max(visited.values())}', flush=True)

if __name__ == '__main__':
    main()
