"""Standalone exact construction checks for delayed unary modular languages.
Pure Python 3; no external dependencies.  Mathematical lower bounds are proved
in RESULT.md and are not inferred from finite testing.
"""
from collections import deque


def construct(n, t):
    assert n >= 2 and t >= 1
    even = n % 2 == 0
    N = t * n if even else (t + 1) * n
    delta = {j: j+1 for j in range(N)}
    cycle_length = n if even else 2*n
    delta[N] = N-cycle_length+1
    finals = {N} if even else {t*n, (t+1)*n}
    return N+1, delta, finals


def check_one(n, t):
    size, delta, finals = construct(n,t)
    target = t*n+1 if n%2==0 else (t+1)*n+1
    assert size == target
    assert set(delta) == set(range(size))
    assert all(0 <= x < size for x in delta.values())
    # Every transition changes color; no loops are permitted.
    assert all((i-j)%2 == 1 for i,j in delta.items())
    # Undirected transition graph is a path with at most one extra edge.
    edges = {tuple(sorted((i,j))) for i,j in delta.items()}
    assert len(edges) <= size
    adj = [set() for _ in range(size)]
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
    q = deque([0]); seen={0}
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in seen: seen.add(w); q.append(w)
    assert len(seen) == size
    # A connected graph with at most one simple cycle is a cactus.
    assert len(edges) in {size-1, size}
    state=0
    for k in range((t+9)*n+1):
        assert (state in finals) == (k%n == 0 and k//n >= t), (n,t,k,state)
        state=delta[state]
    return size


def main():
    samples=0
    for n in range(2,35):
        for t in range(1,19):
            check_one(n,t)
            samples+=1
    for n,t in [(2,1),(3,1),(4,2),(5,3),(9,7),(11,20)]:
        check_one(n,t)
    print(f"PASS: {samples+6} independently replayed deterministic witness constructions")
    print('Scope: exact language membership, state counts, bipartiteness, and cactus structure.')
    print('The infinite lower bound relies on the separate simple-run proof.')

if __name__ == '__main__':
    main()
