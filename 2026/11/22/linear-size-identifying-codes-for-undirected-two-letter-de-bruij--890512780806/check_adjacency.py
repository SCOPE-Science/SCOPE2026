"""Second formulation: build the undirected overlap graph, then read closed balls."""
from check_bounds import construction


def independent_check(q, chosen):
    vertex = [(a, b) for a in range(q) for b in range(q)]
    adjacent = {v: {v} for v in vertex}
    for a in range(q):
        for b in range(q):
            for c in range(q):
                u, v = (a, b), (b, c)
                adjacent[u].add(v)
                adjacent[v].add(u)
    chosen = set(chosen)
    observed = {tuple(sorted(adjacent[v] & chosen)) for v in vertex}
    return len(observed) == q * q and all(adjacent[v] & chosen for v in vertex)


if __name__ == '__main__':
    for q in range(3, 101):
        assert independent_check(q, construction(q)), q
    print('Graph-adjacency verification of construction q=3,...,100: PASS')
