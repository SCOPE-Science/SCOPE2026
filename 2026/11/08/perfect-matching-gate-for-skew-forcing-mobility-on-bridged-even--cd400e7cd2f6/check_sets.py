#!/usr/bin/env python3
"""Independent set-based exhaustive checks for bridged cycle families."""
from itertools import combinations, product
from collections import deque
import json

CASES = [
    ('two_4_4', (4,4), ((0,1),), True),
    ('two_4_6', (4,6), ((0,1),), True),
    ('two_6_6', (6,6), ((0,1),), True),
    ('path_four_4', (4,4,4,4), ((0,1),(1,2),(2,3)), True),
    ('path_three_4', (4,4,4), ((0,1),(1,2)), False),
    ('star_four_4', (4,4,4,4), ((0,1),(0,2),(0,3)), False),
]

def verify(case):
    name, lengths, links, has_pm = case
    nodes = [(i, j) for i, sz in enumerate(lengths) for j in range(sz)]
    links_graph = {u:set() for u in nodes}
    def edge(a,b):
        links_graph[a].add(b)
        links_graph[b].add(a)
    for i, sz in enumerate(lengths):
        for j in range(sz):edge((i,j),(i,(j+1)%sz))
    for i,j in links:edge((i,0),(j,0))
    all_nodes = frozenset(nodes)

    def succeeds(blue_initial):
        white = set(all_nodes.difference(blue_initial))
        while True:
            possible = set()
            for neighbors in links_graph.values():
                remaining = neighbors.intersection(white)
                if len(remaining) == 1:
                    possible.update(remaining)
            if not possible:
                return not white
            white.difference_update(possible)

    k = len(lengths)
    for j in range(k):
        assert not any(succeeds(x) for x in combinations(nodes,j))
    actual = {frozenset(x) for x in combinations(nodes,k) if succeeds(x)}
    predicted = {frozenset((i,j) for i,j in enumerate(c))
                 for c in product(*[range(1, n, 2) for n in lengths])}
    if has_pm:
        assert actual == predicted, (name,len(actual),len(predicted))
        jump = set()
        slide = set()
        index = {s:i for i,s in enumerate(sorted(actual,key=lambda s:sorted(s)))}
        graph = {s:set() for s in actual}
        for a in actual:
            for x in a:
                for y in all_nodes.difference(a):
                    b = (a - {x}) | {y}
                    if b in actual:
                        graph[a].add(b)
                        jump.add(frozenset((a,b)))
                        if y in links_graph[x]:slide.add(frozenset((a,b)))
        assert not slide
        reached = {next(iter(actual))}
        todo = deque(reached)
        while todo:
            x = todo.popleft()
            for y in graph[x].difference(reached):reached.add(y);todo.append(y)
        assert reached == actual
        deg_expected = sum(sz // 2 - 1 for sz in lengths)
        assert all(len(graph[x]) == deg_expected for x in actual)
        assert len(jump) == len(actual)*deg_expected//2
        # Graph distances match Hamming distances in the selected cycle positions.
        for source in actual:
            dist={source:0};todo=deque([source])
            while todo:
                x=todo.popleft()
                for y in graph[x]:
                    if y not in dist:dist[y]=dist[x]+1;todo.append(y)
            assert len(dist)==len(actual)
            for target in actual:
                expected=len([i for i in range(k) if next(v for v in source if v[0]==i)!=next(v for v in target if v[0]==i)])
                assert dist[target]==expected
    else:
        assert not actual
        jump=set();slide=set()
    return {'case':name,'n':len(nodes),'cycle_count':k,'tree_has_perfect_matching':has_pm,
            'skew_forcing_sets_below_k':0,'forcing_sets_at_k':len(actual),
            'predicted_count_if_matched':len(predicted),
            'token_exchange_edges':len(jump),'token_slide_edges':len(slide)}

if __name__=='__main__':
    print(json.dumps([verify(case) for case in CASES],sort_keys=True,indent=2))
