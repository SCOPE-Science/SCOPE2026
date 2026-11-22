"""Exhaustive neighbourhood simulation and binomial-fibre verification.

Uses integer bit words for the full graph and direct adjacency loops.
"""
from itertools import product
from math import comb


def graph(k, edge_set, m):
    adjacency = [[] for _ in range(k + sum(m))]
    for u, v in edge_set:
        adjacency[u].append(v)
        adjacency[v].append(u)
    c = k
    for v in range(k):
        for _ in range(m[v]):
            adjacency[v].append(c)
            adjacency[c].append(v)
            c += 1
    return adjacency


def full_step(state, adjacency):
    result = 0
    for v, neighbors in enumerate(adjacency):
        ones = sum((state >> u) & 1 for u in neighbors)
        if 2 * ones > len(neighbors) or (2 * ones == len(neighbors) and (state >> v) & 1):
            result |= 1 << v
    return result


def fibre(k, edge_set, m, a, b):
    total = 1
    for v in range(k):
        d = sum(v in e for e in edge_set)
        cross_ones = sum((a >> u) & 1 for e in edge_set if v in e for u in e if u != v)
        target = (b >> v) & 1
        p = 0
        for j in range(m[v] + 1):
            s = j + cross_ones
            output = 1 if 2*s > m[v]+d else 0 if 2*s < m[v]+d else (a >> v)&1
            if output == target:
                p += comb(m[v], j)
        total *= p
    return total


def run(k, edges, m):
    adj = graph(k, edges, m)
    n = len(adj)
    states = 1 << n
    observed = {}
    recurrent = 0
    for x in range(states):
        y = full_step(x, adj)
        z = full_step(y, adj)
        zz = full_step(z, adj)
        assert zz == y, (k, edges, m, x, y, z, zz)
        if z == x:
            recurrent += 1
        a = x & ((1 << k)-1)
        b = y & ((1 << k)-1)
        assert (y >> k) == sum(((a >> v)&1) << (sum(m[:v])+j) for v in range(k) for j in range(m[v]))
        observed[a,b] = observed.get((a,b),0)+1
    for a in range(1 << k):
        for b in range(1 << k):
            predicted = fibre(k, edges, m, a, b)
            assert observed.get((a,b),0) == predicted, (k, edges, m, a, b,observed.get((a,b),0),predicted)
            assert predicted >= 1
    assert recurrent == 1 << (2*k), (k,edges,m,recurrent)
    assert len(observed) == 1 << (2*k)
    return states


def main():
    cases=0
    checked_states=0
    for k in (1,2,3):
        possible = [(i,j) for i in range(k) for j in range(i+1,k)]
        for mask in range(1 << len(possible)):
            edges=[pair for bit,pair in enumerate(possible) if mask>>bit&1]
            degrees=[sum(v in e for e in edges) for v in range(k)]
            for padding in product((0,1),repeat=k):
                m=[degrees[v]+1+padding[v] for v in range(k)]
                checked_states+=run(k,edges,m)
                cases+=1
    for k,edges in [
            (4,[(0,1),(1,2),(2,3)]),
            (4,[(0,1),(1,2),(2,3),(3,0)]),
            (4,[(0,1),(0,2),(0,3)]),
            (4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    ]:
        m=[1+sum(v in e for e in edges) for v in range(k)]
        checked_states+=run(k,edges,m)
        cases+=1
    print(f'EXHAUSTIVE_OK cases={cases} initial_states={checked_states}')


if __name__ == '__main__':
    main()
