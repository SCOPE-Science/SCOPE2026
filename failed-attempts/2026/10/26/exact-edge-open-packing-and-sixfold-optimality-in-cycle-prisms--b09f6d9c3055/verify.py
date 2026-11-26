#!/usr/bin/env python3
"""Reproducible checks for edge-open-packing numbers of cycle prisms."""
from functools import lru_cache
from itertools import combinations

BASE = {3: '003', 4: '0023', 5: '02045',
        6: '023045', 7: '0023045', 8: '02103045',
        9: '003045023', 10: '0023045023', 11: '02045023045'}


def graph(n):
    assert n >= 3
    edges = []
    for i in range(n):
        edges.extend(((2*i, 2*i+1),
                      (2*i, 2*((i+1) % n)),
                      (2*i+1, 2*((i+1) % n)+1)))
    return edges


def conflict_graph(n):
    edges = graph(n)
    adj = {frozenset(edge) for edge in edges}
    masks = [0]*len(edges)
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges):
            if j == i: continue
            if any((frozenset((u, v)) in adj and
                    frozenset((u, v)) != frozenset((a, b)) and
                    frozenset((u, v)) != frozenset((c, d)))
                   for u in (a,b) for v in (c,d) if u != v):
                masks[i] |= 1 << j
    return masks


def witness(n):
    if n in (3,4,5): return tuple(map(int, BASE[n]))
    q, r = divmod(n, 6)
    def rotate(s):
        s = list(map(int,s))
        i = next(i for i in range(len(s)) if s[i] == 0 and s[(i+1) % len(s)] == 2)
        s = s[i:]+s[:i]
        return s[2:]+s[:2]
    return tuple(rotate(BASE[6 if r == 0 else 6+r]) + rotate(BASE[6])*(q-1))


def selected_indices(seq):
    return tuple(3*i+j for i,m in enumerate(seq) for j,bit in enumerate((1,2,4)) if m & bit)


def check_witness(n):
    indices = selected_indices(witness(n))
    graph_conf = conflict_graph(n)
    assert all((graph_conf[e] >> f) & 1 == 0 for e,f in combinations(indices,2))
    assert len(indices) == n if n % 6 == 0 else len(indices) == n-1
    return len(indices)


def exact_optimum(n):
    """Independent transfer DP: conflicts are checked in the actual n-prism."""
    conf = conflict_graph(n)
    choices = []
    for i in range(n):
        options=[]
        for mask in range(8):
            es = tuple(3*i+j for j in range(3) if mask & (1<<j))
            if all((conf[a] >> b) & 1 == 0 for a,b in combinations(es,2)):
                options.append((mask,es))
        choices.append(options)
    def cross(a,b):
        return any((conf[e] >> f) & 1 for e in a for f in b)
    best=0
    # Boundary states are fixed. Every edge-column pair with a possible
    # common edge has column distance at most two on the n-cycle.
    for _, first in choices[0]:
        for _, second in choices[1]:
            if cross(first,second): continue
            @lru_cache(None)
            def rec(i, prev, prev2):
                if i == n: return 0
                result = -100000
                for _, now in choices[i]:
                    if cross(now,prev) or cross(now,prev2): continue
                    if i >= n-2 and cross(now,first): continue
                    if i == n-1 and cross(now,second): continue
                    result=max(result, len(now)+rec(i+1,now,prev))
                return result
            best=max(best,len(first)+len(second)+rec(2,second,first))
    return best


def direct_maximizers(n):
    """Exhaustive exact independent-set count, used at six rungs."""
    conf=conflict_graph(n)
    optimum=n if n % 6 == 0 else n-1
    total=0
    for indices in combinations(range(3*n),optimum):
        if all(((conf[a] >> b)&1)==0 for a,b in combinations(indices,2)):
            total+=1
    return total


def main():
    for n in range(3, 41):
        assert exact_optimum(n) == (n if n%6 == 0 else n-1),n
    print('Exact transfer DP: 38 prism graphs, n=3..40: PASS')
    for n in range(3,201):
        check_witness(n)
    print('Constructive cyclic words: n=3..200: PASS')
    count=direct_maximizers(6)
    assert count == 6, count
    print('Exhaustive six-rung prism maximizing sets: 6: PASS')
    print('VERIFY_OK')

if __name__ == '__main__': main()
