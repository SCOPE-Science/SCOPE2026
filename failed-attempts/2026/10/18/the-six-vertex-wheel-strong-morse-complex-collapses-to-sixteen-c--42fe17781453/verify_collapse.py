"""Exhaustive finite check for the strong matching complex of the six-vertex wheel.

All dependencies are Python standard-library modules. Vertices of the complex
are ordered pairs (u,v) encoding the matching (u,{u,v}) with u later than v.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
RIM = tuple(range(5))
VERTICES = tuple(range(6))
HUB = 5
NEIGHBORS = {i: {(i-1)%5, (i+1)%5, HUB} for i in RIM}
NEIGHBORS[HUB] = set(RIM)


def facets_generated_by_filtrations():
    generating = set()
    for order in itertools.permutations(VERTICES):
        earlier = set()
        oriented_pairs = []
        for vertex in order:
            lower = NEIGHBORS[vertex].intersection(earlier)
            # In a one-dimensional complex, the descending link is a cone
            # precisely when it consists of one vertex.
            if len(lower) == 1:
                oriented_pairs.append((vertex, next(iter(lower))))
            earlier.add(vertex)
        generating.add(frozenset(oriented_pairs))
    return generating


def downclosure(facets):
    faces = {frozenset()}
    for facet in facets:
        for k in range(1, len(facet)+1):
            for subset in itertools.combinations(facet, k):
                faces.add(frozenset(subset))
    return faces


def serialize_face(face):
    return sorted([f'{u}>{v}' for u,v in face])


def parse_face(strings):
    return frozenset(tuple(int(y) for y in s.split('>')) for s in strings)


def main():
    raw_facets = facets_generated_by_filtrations()
    facets = {f for f in raw_facets if not any(f < g for g in raw_facets)}
    faces = downclosure(raw_facets)
    dim_count = Counter(len(f)-1 for f in faces if f)
    assert dict(sorted(dim_count.items())) == {0:20,1:55,2:20}
    assert Counter(len(f) for f in facets) == {2:25,3:20}
    assert len(faces) == 96

    cert = json.loads((BASE / 'collapse_certificate.json').read_text(encoding='utf-8'))
    assert cert['graph']['rim_vertices'] == list(RIM)
    assert cert['graph']['hub_vertex'] == HUB
    assert len(cert['pairs']) == 20
    current = set(faces)
    for i, pair in enumerate(cert['pairs']):
        edge, triangle = parse_face(pair['free_edge']), parse_face(pair['triangle'])
        assert len(edge)==2 and len(triangle)==3 and edge < triangle
        assert edge in current and triangle in current
        maximal_cofaces = [t for t in current if edge < t]
        assert maximal_cofaces == [triangle], (i, maximal_cofaces)
        current.remove(edge)
        current.remove(triangle)
        for sigma in current:
            assert all(frozenset(s) in current for k in range(len(sigma))
                       for s in itertools.combinations(sigma,k))

    assert all(len(face) < 3 for face in current)
    v = {next(iter(face)) for face in current if len(face)==1}
    e = [face for face in current if len(face)==2]
    assert len(v)==20 and len(e)==35
    visited = {next(iter(v))}
    while True:
        nxt = visited | {w for face in e if len(face & visited)>0 for w in face}
        if nxt==visited: break
        visited=nxt
    assert visited == v
    b1=len(e)-len(v)+1
    assert b1==16
    print('all 720 vertex filtrations examined')
    print(f'generating maximal faces: {len(facets)}, sizes {dict(Counter(map(len,facets)))}')
    print(f'face counts: {dict(sorted(dim_count.items()))}, including empty: {len(faces)}')
    print('elementary collapses: 20 free-edge/triangle pairs, each checked against current faces')
    print(f'final connected graph: {len(v)} vertices, {len(e)} edges, cycle rank {b1}')
    print('homotopy type: wedge of 16 circles')


if __name__=='__main__':main()
