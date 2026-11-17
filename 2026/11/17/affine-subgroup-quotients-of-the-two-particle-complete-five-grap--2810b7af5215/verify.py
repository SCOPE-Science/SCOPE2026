#!/usr/bin/env python3
"""Exact finite-cell verification of affine-subgroup quotients of D_2(K_5).

Uses only Python's standard library; it enumerates cubical cells, strict
face chains, permutation orbits, quotient links, and orientation constraints.
"""
from itertools import combinations
from collections import Counter, defaultdict
import json

V = range(5)
GRAPH_EDGES = tuple(combinations(V, 2))


def cell(dim, supports):
    return dim, tuple(sorted(supports))

C = [[], [], []]
C[0] = [cell(0, ((0, a), (0, b))) for a, b in combinations(V, 2)]
C[1] = [cell(1, ((0, v), (1, a, b))) for v in V
        for a, b in GRAPH_EDGES if v not in (a, b)]
C[2] = [cell(2, ((1, *e), (1, *f))) for e, f in combinations(GRAPH_EDGES, 2)
        if set(e).isdisjoint(f)]
assert [len(x) for x in C] == [10, 30, 15]


def contained(face, coface):
    if face[0] >= coface[0]:
        return False
    u, v = face[1], coface[1]
    for swap in ((0, 1), (1, 0)):
        valid = True
        for i in (0, 1):
            x, y = u[i], v[swap[i]]
            if x == y:
                continue
            if not (x[0] == 0 and y[0] == 1 and x[1] in y[1:]):
                valid = False
                break
        if valid:
            return True
    return False


ALL = sum(C, [])
FLAGS = [[], [], []]
FLAGS[0] = [(x,) for x in ALL]
FLAGS[1] = [(x, y) for x in ALL for y in ALL if contained(x, y)]
FLAGS[2] = [(x, y, z) for x in C[0] for y in C[1] for z in C[2]
            if contained(x, y) and contained(y, z)]
assert [len(x) for x in FLAGS] == [55, 180, 120]


def act_cell(x, p):
    return cell(x[0], [(0, p[z[1]]) if z[0] == 0 else
           (1, *sorted((p[z[1]], p[z[2]]))) for z in x[1]])


def act_flag(x, p):
    return tuple(act_cell(c, p) for c in x)


def generated(gens):
    identity = tuple(range(5))
    group, queue = {identity}, [identity]
    while queue:
        p = queue.pop()
        for q in gens:
            r = tuple(p[q[i]] for i in V)
            if r not in group:
                group.add(r)
                queue.append(r)
    return tuple(sorted(group))


def affine(a, b):
    return tuple((a * i + b) % 5 for i in V)


def orbits(elements, group):
    index = {}
    representatives = []
    for x in elements:
        if x not in index:
            i = len(representatives)
            representatives.append(x)
            for y in (act_flag(x, p) for p in group):
                index[y] = i
    assert len(index) == len(elements)
    # Independent Burnside count, not relying on the orbit representatives.
    fixed = sum(sum(act_flag(x, p) == x for x in elements) for p in group)
    assert fixed % len(group) == 0
    assert fixed // len(group) == len(representatives)
    return representatives, index


def analyze(group):
    R = []; I = []
    for faces in FLAGS:
        rep, ind = orbits(faces, group)
        R.append(rep); I.append(ind)
    counts = tuple(map(len, R))
    triangles_at_edge = defaultdict(list)
    oriented_triangles_at_edge = defaultdict(list)
    for tri_index, tri in enumerate(R[2]):
        for k in range(3):
            edge_index = I[1][tri[:k] + tri[k+1:]]
            triangles_at_edge[edge_index].append(tri_index)
            oriented_triangles_at_edge[edge_index].append((tri_index, (-1)**k))
    incidences = Counter(len(triangles_at_edge[i]) for i in range(counts[1]))
    assert set(incidences) <= {1, 2} and sum(incidences.values()) == counts[1]
    boundary_edges = [i for i in range(counts[1]) if len(triangles_at_edge[i]) == 1]

    # Every vertex link must be exactly a connected circle or interval.
    link_types = Counter()
    for v in range(counts[0]):
        incident = [i for i, e in enumerate(R[1]) if I[0][(e[0],)] == v
                    or I[0][(e[1],)] == v]
        adjacent = defaultdict(list)
        for tri in R[2]:
            if v not in [I[0][(c,)] for c in tri]:
                continue
            eids = [I[1][(a,b)] for a,b in combinations(tri, 2)
                    if v in (I[0][(a,)], I[0][(b,)])]
            assert len(eids) == 2
            a,b = eids
            adjacent[a].append(b); adjacent[b].append(a)
        assert set(adjacent) == set(incident) and incident
        seen, stack = set(), [incident[0]]
        while stack:
            z = stack.pop()
            if z in seen: continue
            seen.add(z);stack.extend(adjacent[z])
        assert len(seen) == len(incident), ('disconnected link', v)
        degrees = Counter(len(adjacent[z]) for z in incident)
        if degrees == {2: len(incident)}:
            link_types['circle'] += 1
        else:
            assert degrees[1] == 2 and sum(degrees.values()) == len(incident)
            assert set(degrees) <= {1,2}
            link_types['interval'] += 1

    # Each boundary component is a circle, allowing parallel edges.
    boundary_incident = defaultdict(list)
    for j in boundary_edges:
        a, b = (I[0][(x,)] for x in R[1][j])
        boundary_incident[a].append(j)
        boundary_incident[b].append(j)
    assert all(len(z) == 2 for z in boundary_incident.values())
    bcount, unseen = 0, set(boundary_incident)
    while unseen:
        bcount += 1
        start = next(iter(unseen)); queue = [start]
        while queue:
            u = queue.pop()
            if u not in unseen: continue
            unseen.remove(u)
            for eid in boundary_incident[u]:
                for x in R[1][eid]:
                    w = I[0][(x,)]
                    if w in unseen: queue.append(w)
    assert link_types['interval'] == len(boundary_incident)

    # Orientability: propagate signs of 2-cells so interior edge
    # incidences of the oriented surface cancel in pairs.
    graph = defaultdict(list)
    for pair in oriented_triangles_at_edge.values():
        if len(pair) == 2:
            (u, a), (v, b) = pair
            graph[u].append((v, -a*b))
            graph[v].append((u, -a*b))
    signs, orientable = {}, True
    for first in range(counts[2]):
        if first in signs: continue
        signs[first] = 1; stack = [first]
        while stack:
            u = stack.pop()
            for v, parity in graph[u]:
                desired = signs[u]*parity
                if v in signs:
                    if signs[v] != desired: orientable = False
                else:
                    signs[v] = desired; stack.append(v)

    chi = counts[0] - counts[1] + counts[2]
    if orientable:
        assert (2 - bcount - chi) % 2 == 0
        genus = (2 - bcount - chi)//2
        label = ('sphere' if bcount == 0 and genus == 0 else
                 'closed orientable genus '+str(genus) if bcount == 0 else
                 'disk' if genus == 0 and bcount == 1 else
                 'orientable genus '+str(genus)+' with '+str(bcount)+' boundary circles')
    else:
        genus = 2 - bcount - chi
        assert genus >= 1
        label = ('closed nonorientable genus '+str(genus) if bcount == 0 else
                 'Moebius band' if genus == 1 and bcount == 1 else
                 'once-punctured Klein bottle' if genus == 2 and bcount == 1 else
                 'nonorientable genus '+str(genus)+' with '+str(bcount)+' boundary circles')
    return {'order':len(group),'flags':list(counts),'Euler_characteristic':chi,
            'boundary_components':bcount,'boundary_edges':len(boundary_edges),
            'orientable':orientable,'genus':genus,'homeomorphism_type':label,
            'link_types':dict(link_types),'edge_incidence':dict(sorted(incidences.items()))}


def run():
    groups = {'identity':generated([affine(1, 0)]),
              'C2':generated([affine(4, 0)]),
              'C4':generated([affine(2, 0)]),
              'C5':generated([affine(1, 1)]),
              'D5':generated([affine(1, 1), affine(4, 0)]),
              'F20':generated([affine(1, 1), affine(2, 0)])}
    expected = {
      'identity': (1,[55,180,120],-5,0,False,7),
      'C2':       (2,[31,92,60],-1,1,False,2),
      'C4':       (4,[16,46,30],0,1,False,1),
      'C5':       (5,[11,36,24],-1,0,False,3),
      'D5':       (10,[9,20,12],1,1,True,0),
      'F20':      (20,[5,10,6],1,1,True,0)}
    # All subgroups of the affine group: closures of ordered generator pairs.
    affine_group = groups['F20']
    def compose(p,q):
        return tuple(p[q[i]] for i in V)
    def subgroup_from_pair(p,q):
        identity = tuple(V)
        out, queue = {identity}, [identity]
        while queue:
            x = queue.pop()
            for y in (p,q):
                z=compose(x,y)
                if z not in out:
                    out.add(z); queue.append(z)
        return frozenset(out)
    all_subgroups = {subgroup_from_pair(p,q) for p in affine_group
                     for q in affine_group}
    assert len(all_subgroups) == 14
    classes = []
    remaining = set(all_subgroups)
    while remaining:
        H = next(iter(remaining))
        conjugates = set()
        for g in affine_group:
            inverse = tuple(g.index(i) for i in V)
            conjugates.add(frozenset(compose(compose(g,h),inverse) for h in H))
        assert conjugates <= remaining
        classes.append((len(H),len(conjugates)))
        remaining -= conjugates
    assert sorted(classes) == sorted([(1,1),(2,5),(4,5),(5,1),(10,1),(20,1)])

    results = {}
    for name, group in groups.items():
        result = analyze(group)
        values = (result['order'],result['flags'],result['Euler_characteristic'],
                  result['boundary_components'],result['orientable'],result['genus'])
        assert values == expected[name], (name,values)
        results[name] = result
    print(json.dumps(results,sort_keys=True,indent=2))
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
