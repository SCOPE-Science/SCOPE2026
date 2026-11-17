#!/usr/bin/env python3
"""Exact finite-state certificate for Life's 3-row periodic-two theorem.
Python 3 standard library only; use: python3 transfer_certificate.py.
"""
from collections import Counter, defaultdict

WIDTH = 3
COLORS = 1 << (2 * WIDTH)
NODES = COLORS * COLORS

def bit(column, row, phase):
    return (column >> (row + WIDTH * phase)) & 1

def life_ok(a, b, c, phase):
    for row in range(WIDTH):
        nb = (bit(b, (row + 1) % WIDTH, phase)
              + bit(b, (row + 2) % WIDTH, phase)
              + sum(bit(a, r, phase) for r in range(WIDTH))
              + sum(bit(c, r, phase) for r in range(WIDTH)))
        old = bit(b, row, phase)
        new = (nb == 3 or (old == 1 and nb == 2))
        if new != bool(bit(b, row, 1-phase)):
            return False
    return True

def adjacency():
    out = [[] for _ in range(NODES)]
    rev = [[] for _ in range(NODES)]
    for a in range(COLORS):
        for b in range(COLORS):
            u = a * COLORS + b
            for c in range(COLORS):
                if life_ok(a,b,c,0) and life_ok(a,b,c,1):
                    v = b * COLORS + c
                    out[u].append(v)
                    rev[v].append(u)
    return out, rev

def kosaraju(out, rev):
    used = bytearray(NODES)
    order = []
    for root in range(NODES):
        if used[root]: continue
        used[root] = 1
        stack = [(root,0)]
        while stack:
            node,i = stack[-1]
            if i < len(out[node]):
                v = out[node][i]
                stack[-1] = (node,i+1)
                if not used[v]:
                    used[v] = 1
                    stack.append((v,0))
            else:
                order.append(node)
                stack.pop()
    used = bytearray(NODES)
    comp = []
    for root in reversed(order):
        if used[root]: continue
        used[root] = 1
        queue = [root]
        for u in queue:
            for v in rev[u]:
                if not used[v]:
                    used[v] = 1
                    queue.append(v)
        comp.append(set(queue))
    return comp

def diagonal_column(c):
    return c & 7 == (c >> 3)

def main():
    out, rev = adjacency()
    total_edges = sum(map(len,out))
    assert total_edges == 6140, total_edges
    components = kosaraju(out, rev)
    cyclic = [c for c in components if len(c)>1 or any(u in out[u] for u in c)]
    cyclic.sort(key=lambda c:-len(c))
    sizes = [(len(c),sum(sum(v in c for v in out[u]) for u in c)) for c in cyclic]
    assert sizes == [(30,75),(27,81),(4,4)],sizes
    for c in cyclic[:2]:
        assert all(diagonal_column(u//COLORS) and diagonal_column(u%COLORS) for u in c)
    four = cyclic[2]
    assert four == {455,504,3591,3640},four
    four_out = {u: set(out[u]) & four for u in four}
    assert four_out == {455:{504},504:{3640},3640:{3591},3591:{455}},four_out
    assert all(not(diagonal_column(u//COLORS) and diagonal_column(u%COLORS)) for u in four)
    # Every closed walk is entirely inside a cyclic strongly connected component.
    # 30 and 27 are phase-diagonal. The remaining component is one directed 4-cycle.
    print('nodes:',NODES)
    print('local edges:',total_edges)
    print('strong components:',len(components))
    print('cyclic components (vertices, internal edges):',sizes)
    print('non-diagonal cyclic vertices:',sorted(four))
    print('non-diagonal cyclic edges:',[(u,next(iter(four_out[u]))) for u in sorted(four)])
    print('nonfixed cyclic configurations: 4 when 4 divides n, otherwise 0 (n>=3)')
    print('primitive temporal two-orbits: 2 when 4 divides n, otherwise 0')
    print('PASS')
if __name__ == '__main__':
    main()
