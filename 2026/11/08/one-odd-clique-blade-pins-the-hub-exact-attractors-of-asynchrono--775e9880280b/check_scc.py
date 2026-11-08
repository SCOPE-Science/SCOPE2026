#!/usr/bin/env python3
"""Exhaustive communicating-class test of an asynchronous two-color process.
Requires only Python 3 standard library.
"""
from itertools import product
from collections import Counter
from math import comb


def graph(rs):
    nv = 1 + sum(rs)
    nb = [set() for _ in range(nv)]
    j = 1
    for r in rs:
        vertices = [0] + list(range(j, j+r))
        for i in vertices:
            nb[i].update(x for x in vertices if x != i)
        j += r
    return [sorted(x) for x in nb]


def edges_for_state(s, nb):
    for v, neigh in enumerate(nb):
        count = sum(((s >> u) & 1) == ((s >> v) & 1)
                    for u in neigh) + 1
        if 2*count > len(neigh)+1:
            yield s ^ (1 << v)


def tarjan(graph_rows):
    order, low, stack, instack, comps = {}, {}, [], set(), []
    def visit(u):
        order[u] = low[u] = len(order)
        stack.append(u); instack.add(u)
        for v in graph_rows[u]:
            if v not in order:
                visit(v); low[u] = min(low[u], low[v])
            elif v in instack:
                low[u] = min(low[u], order[v])
        if low[u] == order[u]:
            comp = set()
            while True:
                w = stack.pop(); instack.remove(w); comp.add(w)
                if w == u: break
            comps.append(comp)
    for s in range(len(graph_rows)):
        if s not in order: visit(s)
    return comps


def predicted(rs):
    odd = [r for r in rs if r % 2]
    even = [r for r in rs if not r % 2]
    sizes = [comb(2*(r//2)+1, r//2) for r in rs]
    nrec = 2
    for x in sizes: nrec *= x
    if odd:
        classes = 2
        for r in odd: classes *= comb(r, r//2)
        cls_size = 1
        for r in even: cls_size *= comb(r+1, r//2)
    else:
        classes = 1
        cls_size = nrec
    return classes, cls_size, nrec


def run_case(rs):
    nb = graph(rs); n = len(nb)
    rows = [set(edges_for_state(s, nb)) for s in range(1<<n)]
    components = tarjan(rows)
    label = {s:i for i,c in enumerate(components) for s in c}
    rec = [c for i,c in enumerate(components) if all(
        label[t] == i for s in c for t in rows[s])]
    expected = predicted(rs)
    actual = (len(rec), min(map(len,rec)),sum(map(len,rec)))
    assert len({len(c) for c in rec}) == 1
    assert actual == expected, (rs,actual,expected)
    edges = [(i,j) for i in range(n) for j in nb[i] if i<j]
    def cut(s): return sum(((s>>a)^(s>>b))&1 for a,b in edges)
    maxcut=sum((r+1)**2//4 for r in rs) # floor((r+1)^2/4)
    assert all(cut(s) == maxcut for c in rec for s in c),rs
    # Every maximum-cut configuration is recurrent, and no others are.
    assert {s for s in range(1<<n) if cut(s)==maxcut} == set().union(*rec),rs
    return len(rows),len(rec)


def main():
    cases = []
    for m in range(1,4):
        for rs in product(range(1,6),repeat=m):
            if sum(rs)<=8: cases.append(rs)
    for rs in [(2,2,2,3),(2,3,4),(4,5),(5,5),(2,2,2,2),
               (3,3,3),(4,4),(3,4,2),(2,4,4)]:
        if rs not in cases: cases.append(rs)
    nstates=0
    for rs in cases:
        tested,_ = run_case(rs); nstates += tested
    print('PASS SCC, exact class size and count, and maximum-cut equality')
    print('cases:',len(cases),'labelled configurations:',nstates)
    print('examples:',[(rs,predicted(rs)) for rs in [(2,2,2),(2,3,2),(4,4),(4,5),(2,2,2,3)]])

if __name__=='__main__':main()
