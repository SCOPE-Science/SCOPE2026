"""Independent exact template enumeration in the Fano-triple Coxeter model.

Python 3 standard library only. This builds a graph by deleting the seven
Fano-plane lines from the 35 triples, then joining disjoint triples.
It does not call the cyclic-model enumerator or use its pruning routine.
"""
import itertools
from collections import Counter

lines = {frozenset((i, (i+1)%7, (i+3)%7)) for i in range(7)}
triples = [frozenset(t) for t in itertools.combinations(range(7), 3)
           if frozenset(t) not in lines]
assert len(triples) == 28
neighbors = [tuple(j for j in range(28) if j != i and
                   not (triples[i] & triples[j])) for i in range(28)]
assert all(len(x) == 3 for x in neighbors)
assert sum(map(len, neighbors)) == 84

# A fixed explicit isomorphism to the seven-claw labeling, verified edge by edge.
phi = [0, 19, 21, 22, 7, 16, 11, 27, 4, 18, 9, 13, 10, 12,
       26, 6, 1, 17, 24, 5, 15, 25, 8, 2, 3, 14, 23, 20]
assert sorted(phi) == list(range(28))
cyclic_edges = set()
for i in range(7):
    for j, step in enumerate((1, 2, 4)):
        u = 7 + 7*j + i
        for x,y in ((i,u),(u,7+7*j+(i+step)%7)):
            cyclic_edges.add(frozenset((phi[x],phi[y])))
fano_edges = {frozenset((i,j)) for i in range(28) for j in neighbors[i]}
assert cyclic_edges == fano_edges and len(fano_edges) == 42

constraints = [(i, *neighbors[i]) for i in range(28)]
templates = []
for c in range(4):
    other = [j for j in range(4) if j != c]
    templates.extend((c,d,d,d) for d in other)
    templates.extend((c,*p) for p in itertools.permutations(other))
assert len(templates) == 36
solutions = []
node_count = 0

def search(colours, processed):
    global node_count
    node_count += 1
    if len(processed) == 28:
        assert all(colours[i] != colours[j] for i in range(28) for j in neighbors[i])
        assert all(len({colours[j] for j in neighbors[i]}) in (1,3)
                   for i in range(28))
        solutions.append(tuple(colours))
        return
    # Branch over a whole valid closed star instead of individual vertex colours.
    chosen = None
    choices = None
    for q,vertices in enumerate(constraints):
        if q in processed:
            continue
        candidates = [p for p in templates
                      if all(colours[v] in (-1,p[j]) for j,v in enumerate(vertices))]
        if not candidates:
            return
        if choices is None or len(candidates) < len(choices):
            chosen, choices = q, candidates
        if len(candidates) == 1:
            break
    vertices = constraints[chosen]
    for p in choices:
        new = colours[:]
        for j,v in enumerate(vertices):
            new[v] = p[j]
        search(new, processed | {chosen})

start = [-1]*28
start[0] = 0
search(start, set())
assert len(solutions) == 84
assert Counter(tuple(sorted(Counter(x).values())) for x in solutions) == {(4,8,8,8):84}

def partition(x):
    return tuple(sorted(tuple(i for i,c in enumerate(x) if c == j) for j in range(4)))
partitions = {partition(x) for x in solutions}
assert len(partitions) == 14
print('Fano-triple isomorphism=verified')
print('local-template enumeration root-fixed=84 search_nodes='+str(node_count))
print('named_four_colours=336 unlabeled_partitions=14')
print('all_class_sizes=4,8,8,8')
