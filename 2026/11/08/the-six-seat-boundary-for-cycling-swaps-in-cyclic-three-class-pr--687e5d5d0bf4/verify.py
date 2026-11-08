"""Exact finite enumeration for cyclic three-type binary seating dynamics.
Run: python3 verify.py. Requires Python standard library only.
"""
from itertools import product
from collections import Counter


def utility(word, position):
    n = len(word)
    preferred = (word[position] + 1) % 3
    return int(word[(position - 1) % n] == preferred) + int(word[(position + 1) % n] == preferred)


def exchanges(word):
    n = len(word)
    old = tuple(utility(word, p) for p in range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if word[i] == word[j]:
                continue
            after = list(word)
            after[i], after[j] = after[j], after[i]
            after = tuple(after)
            # Old occupant of position j is now at position i, and conversely.
            if utility(after, i) > old[j] and utility(after, j) > old[i]:
                yield after, (i, j)


def components(adjacency):
    """Tarjan's strongly connected components algorithm."""
    order = {}
    low = {}
    stack = []
    on_stack = set()
    scc = []
    def visit(v):
        order[v] = low[v] = len(order)
        stack.append(v)
        on_stack.add(v)
        for w in adjacency[v]:
            if w not in order:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], order[w])
        if low[v] == order[v]:
            comp = set()
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.add(w)
                if w == v:
                    break
            scc.append(comp)
    for v in adjacency:
        if v not in order:
            visit(v)
    return scc


def welfare(word):
    n = len(word)
    return sum(word[i] != word[(i+1) % n] for i in range(n))


def orbit(v):
    n = len(v)
    out = set()
    for k in range(n):
        shifted = v[k:] + v[:k]
        for reversal in (False, True):
            oriented = shifted[::-1] if reversal else shifted
            for t in range(3):
                out.add(tuple((x+t) % 3 for x in oriented))
    return out


def check():
    summary = {}
    for n in range(3, 7):
        vertices = list(product(range(3), repeat=n))
        assert len(vertices) == 3**n
        edges = {v: [w for w, ij in exchanges(v)] for v in vertices}
        comps = [s for s in components(edges) if len(s) > 1]
        summary[n] = (len(vertices), sum(len(edges[v]) for v in vertices), len(comps), sorted(map(len, comps)))
        if n <= 5:
            assert not comps, (n, comps)
        else:
            assert len(comps) == 6
            assert all(len(c) == 6 for c in comps)
            cyclic_vertices = set().union(*comps)
            assert len(cyclic_vertices) == 36
            assert cyclic_vertices == orbit((0, 0, 1, 2, 1, 2))
            assert all(tuple(v.count(k) for k in range(3)) == (2, 2, 2) for v in cyclic_vertices)
            assert all(welfare(v) == 5 for v in cyclic_vertices)
            assert all(sum(1 for w in edges[v] if w in c) == 1 for c in comps for v in c)
            # Each six-state nontrivial component consists of exactly six directed edges.
            assert sum(sum(w in c for w in edges[v]) for c in comps for v in c) == 36
            assert welfare((0,1,2,0,1,2)) == 6
            assert not list(exchanges((0,1,2,0,1,2)))
    assert summary[3] == (27, 0, 0, [])
    # In particular any path of strict swaps on n<=5 must terminate.
    a = (2,2,0,1,0,1)
    moves = ((0,3),(2,5),(1,4),(0,3),(2,5),(1,4))
    states = [a]
    gains=[]
    for i,j in moves:
        before=states[-1]
        assert before[i] != before[j]
        nxt=list(before);nxt[i],nxt[j]=nxt[j],nxt[i];nxt=tuple(nxt)
        gi=(utility(nxt,i)-utility(before,j), utility(nxt,j)-utility(before,i))
        assert gi[0]>0 and gi[1]>0
        gains.append(gi)
        states.append(nxt)
    assert len(set(states[:-1])) == 6 and states[-1] == a
    assert all(welfare(s)==5 for s in states)
    print('SMALL_N',summary)
    print('SIX_SWAP_CYCLE',states)
    print('STRICT_GAINS',gains)
    print('VERIFIED: 3^n exhaustive states for 3<=n<=6, exact SCC structure and explicit cycle')

if __name__ == '__main__':
    check()
