#!/usr/bin/env python3
"""Independent exhaustive checker for EFX orientations on labeled bicliques.

One edge per pair (i,j). A 1 bit allocates its edge to the left endpoint;
a 0 bit allocates it to the right endpoint. EFX includes the deletion of
edges that the envying agent values at zero.
"""
from itertools import product
from math import comb


def predicted(a, b):
    return (2**b - 1)**a + (2**a - 1)**b - 2**(a*b) + a + b


def direct_efx(a, b, mask):
    # Explicitly allocate each edge to an agent, then compare valuations
    # for all ordered pairs and all items in the second agent's bundle.
    bundles = [[] for _ in range(a+b)]
    for i in range(a):
        for j in range(b):
            e = (i, j)
            owner = i if mask & (1 << (i*b+j)) else a+j
            bundles[owner].append(e)
    def value(u, edges):
        if u < a:
            return sum(i == u for i,j in edges)
        return sum(j == u-a for i,j in edges)
    for u in range(a+b):
        own = value(u, bundles[u])
        for v in range(a+b):
            if u == v:
                continue
            for k in range(len(bundles[v])):
                after = bundles[v][:k]+bundles[v][k+1:]
                if own < value(u, after):
                    return False
    return True


def structural_efx(a, b, mask):
    indegree = [0]*(a+b)
    owners = {}
    for i in range(a):
        for j in range(b):
            owner = i if mask & (1 << (i*b+j)) else a+j
            owners[(i, j)] = owner
            indegree[owner] += 1
    for i in range(a):
        for j in range(b):
            if indegree[i] == 0 and indegree[a+j] != 1:
                return False
            if indegree[a+j] == 0 and indegree[i] != 1:
                return False
    return True


def run():
    instances = 0
    orientations = 0
    for a in range(1, 6):
        for b in range(1, 6):
            if a*b > 16:
                continue
            found = 0
            for mask in range(1 << (a*b)):
                direct = direct_efx(a,b,mask)
                structural = structural_efx(a,b,mask)
                assert direct == structural, (a,b,mask,direct,structural)
                found += direct
                orientations += 1
            assert found == predicted(a,b), (a,b,found,predicted(a,b))
            print(f'a={a} b={b} EFX={found} all={1<<(a*b)}')
            instances += 1
    # Exact integer formula remains symmetric in the bipartition.
    for a in range(1,100):
        for b in range(1,100):
            assert predicted(a,b) == predicted(b,a)
            assert 0 < predicted(a,b) <= 2**(a*b)
    print(f'PASS {instances} parameter instances, {orientations} fully checked orientations')

if __name__ == '__main__':
    run()
