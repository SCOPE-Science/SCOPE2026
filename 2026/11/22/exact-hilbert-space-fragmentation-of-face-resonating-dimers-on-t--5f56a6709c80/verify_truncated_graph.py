#!/usr/bin/env python3
"""Independent actual truncated-polyhedron dimer enumeration and face-flip test.
Uses only the Python standard library. Vertex identities are directed base edges.
"""
from functools import lru_cache
from collections import Counter


def data(n):
    base = 2 * n
    edges = set()
    for i in range(n):
        for a, b in ((i, (i + 1) % n),
                     (n + i, n + (i + 1) % n), (i, n + i)):
            edges.add(tuple(sorted((a, b))))
    nbr = {i: [] for i in range(base)}
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    assert all(len(x) == 3 for x in nbr.values())
    darts = sorted((v, w) for v in nbr for w in nbr[v])
    did = {d: i for i, d in enumerate(darts)}
    all_edges = set()
    for v in nbr:
        for i, u in enumerate(sorted(nbr[v])):
            for w in sorted(nbr[v])[i + 1:]:
                all_edges.add(tuple(sorted((did[v, u], did[v, w]))))
    for u, v in edges:
        all_edges.add(tuple(sorted((did[u, v], did[v, u]))))
    full_faces = [list(range(n)), list(range(n, base))]
    for i in range(n):
        full_faces.append([i, (i + 1) % n, n + (i + 1) % n, n + i])
    cycles = []
    for face in full_faces:
        cyc = []
        for i, v in enumerate(face):
            cyc.extend((did[v, face[(i - 1) % len(face)]],
                        did[v, face[(i + 1) % len(face)]]))
        cyc_edges = frozenset(tuple(sorted((cyc[i], cyc[(i + 1) % len(cyc)])))
                              for i in range(len(cyc)))
        assert len(cyc_edges) == 2 * len(face)
        assert cyc_edges <= all_edges
        cycles.append(cyc_edges)
    assert len(darts) == 6 * n
    assert len(all_edges) == 9 * n
    return nbr, darts, did, edges, all_edges, cycles


def matchings(n, all_edges):
    adj = {v: set() for v in range(6*n)}
    for i, (u,v) in enumerate(sorted(all_edges)):
        adj[u].add((v,i));adj[v].add((u,i))
    @lru_cache(None)
    def generate(mask):
        if not mask:
            return ((),)
        u = (mask & -mask).bit_length()-1
        ans=[]
        for v,eid in adj[u]:
            if mask>>v & 1:
                for rest in generate(mask^(1<<u)^(1<<v)):
                    ans.append(tuple(sorted((eid,)+rest)))
        return tuple(ans)
    return generate((1<<(6*n))-1), sorted(all_edges)


def main():
    for n in range(3, 8):
        nbr, darts, did, E, TE, faces = data(n)
        matching_indices, sorted_edges = matchings(n, TE)
        actual = [frozenset(sorted_edges[i] for i in M) for M in matching_indices]
        assert len(actual) == 2 ** (n + 1)
        idx = {M:i for i,M in enumerate(actual)}
        transitions = [set() for _ in actual]
        for i,M in enumerate(actual):
            for F in faces:
                contained = M & F
                if len(contained) == len(F)//2:
                    # Alternation: all selected face edges form a perfect matching of this face.
                    covered = set()
                    for a,b in contained:
                        covered.add(a);covered.add(b)
                    if len(covered)==len(F):
                        new=frozenset(M ^ F)
                        assert new in idx, (n, i)
                        transitions[i].add(idx[new])
        assert all(i in transitions[j] for i in range(len(actual)) for j in transitions[i])
        cores = [set() for _ in actual]
        comps=[]
        undone=set(range(len(actual)))
        while undone:
            s=undone.pop();stack=[s];C={s}
            while stack:
                for t in transitions[stack.pop()]:
                    if t in undone:undone.remove(t);C.add(t);stack.append(t)
            comps.append(C)
        # Independent of explicit face-flip formula: graph on actual truncated-polyhedron vertices.
        assert len(comps) == (10,23,46,90,176)[n-3]
        assert max(map(len, comps)) == (7,10,14,21,32)[n-3]
        print('n=%d physical_vertices=%d dimer_coverings=%d physical_faces=%d '%
              (n,6*n,len(actual),len(faces))+
              'flip_edges=%d components=%d max=%d frozen=%d'%
              (sum(map(len, transitions))//2,len(comps),max(map(len,comps)),
               sum(not a for a in transitions)))
    print('PASS: direct matching enumeration in the genuine 6n-vertex polyhedral graph')


if __name__=='__main__':main()
