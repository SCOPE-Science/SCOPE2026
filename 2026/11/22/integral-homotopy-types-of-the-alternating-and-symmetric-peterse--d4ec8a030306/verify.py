#!/usr/bin/env python3
"""Exact finite CW / fundamental-group certificate for Petersen matching orbit spaces.

Run with: python3 petersen_orbit_verifier.py
Uses the Python standard library. Every simplex, group element, quotient flag,
free-face cancellation, and two-cell attaching word is generated afresh.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict


def reduce_word(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result


def invert_word(word):
    return [-x for x in reversed(word)]


def edge_and_face_data():
    vertices = list(combinations(range(5), 2))
    vertex_id = {v: i for i, v in enumerate(vertices)}
    edges = [(a, b) for a in range(10) for b in range(a + 1, 10)
             if set(vertices[a]).isdisjoint(vertices[b])]
    assert len(edges) == 15
    edge_id = {e: i for i, e in enumerate(edges)}
    matchings = [f for k in range(1, 6) for f in combinations(range(15), k)
                 if len(set(t for e in f for t in edges[e])) == 2 * k]
    assert tuple(Counter(map(len, matchings))[k] for k in range(1, 6)) == (15, 75, 145, 90, 6)
    face_id = {f: i for i, f in enumerate(matchings)}
    groups = {}
    for p in permutations(range(5)):
        vertex_action = [vertex_id[tuple(sorted(p[t] for t in v))] for v in vertices]
        edge_action = [edge_id[tuple(sorted((vertex_action[a], vertex_action[b])))]
                       for a, b in edges]
        faces_action = tuple(face_id[tuple(sorted(edge_action[e] for e in f))]
                             for f in matchings)
        inversion_count = sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5))
        groups[p] = (faces_action, inversion_count % 2)
    assert len(groups) == 120
    return matchings, groups


def flags_of_faces(faces):
    flags = [(i,) for i in range(len(faces))]
    for d in range(1, 5):
        additions = []
        for chain in flags:
            if len(chain) != d:
                continue
            last = set(faces[chain[-1]])
            for k, higher in enumerate(faces):
                if len(higher) > len(last) and last.issubset(higher):
                    additions.append(chain + (k,))
        flags.extend(additions)
    assert len(flags) == 12121
    assert tuple(Counter(map(len, flags))[d] for d in range(1, 6)) == (331, 2460, 5010, 3600, 720)
    return flags


def quotient(flags, face_actions):
    seen = {}
    reps = []
    for flag in flags:
        if flag in seen:
            continue
        k = len(reps)
        for action in face_actions:
            transformed = tuple(action[j] for j in flag)
            if transformed in seen:
                assert seen[transformed] == k
            else:
                seen[transformed] = k
        reps.append(flag)
    assert len(seen) == len(flags)
    bdry = []
    cofaces = [set() for _ in reps]
    for i, flag in enumerate(reps):
        d = {}
        for j in range(len(flag)):
            if len(flag) == 1:
                continue
            sub = flag[:j] + flag[j+1:]
            face = seen[sub]
            assert face not in d, 'rank-separated flags must have distinct boundary facets'
            d[face] = (-1) ** j
        bdry.append(d)
        for f in d:
            cofaces[f].add(i)
    return reps, seen, bdry, cofaces


def free_face_collapse(reps, bdry, cofaces):
    live = set(range(len(reps)))
    pairs = []
    while True:
        pair = None
        for i in sorted(live):
            higher = cofaces[i].intersection(live)
            if len(higher) != 1:
                continue
            j = next(iter(higher))
            if i not in bdry[j] or len(reps[j]) != len(reps[i]) + 1:
                continue
            pair = (i, j)
            break
        if pair is None:
            break
        i, j = pair
        assert cofaces[i].intersection(live) == {j}
        assert not cofaces[j].intersection(live), "free coface must be maximal"
        assert bdry[j][i] in (-1, 1)
        live.remove(i)
        live.remove(j)
        pairs.append(pair)
    return live, pairs


def attaching_words(reps, seen, live):
    vertices = sorted(i for i in live if len(reps[i]) == 1)
    edges = sorted(i for i in live if len(reps[i]) == 2)
    triangles = sorted(i for i in live if len(reps[i]) == 3)
    assert (len(vertices), len(edges), len(triangles)) == (8, 18, 12)
    assert all(len(reps[i]) <= 3 for i in live)

    endpoints = {e: (seen[(reps[e][0],)], seen[(reps[e][1],)]) for e in edges}
    parents = {v:v for v in vertices}
    def find(x):
        while parents[x] != x:
            x = parents[x]
        return x
    tree = set()
    for e in edges:
        a, b = endpoints[e]
        if find(a) != find(b):
            parents[find(a)] = find(b)
            tree.add(e)
    assert len(tree) == len(vertices) - 1
    generators = {e:k+1 for k,e in enumerate(e for e in edges if e not in tree)}
    assert len(generators) == 11
    words = []
    for t in triangles:
        a,b,c = reps[t]
        # The oriented 2-simplex has attaching path a->b->c->a.
        ordered = [(seen[(a,b)], 1), (seen[(b,c)],1), (seen[(a,c)],-1)]
        assert all(e in edges for e,_ in ordered)
        words.append(reduce_word([sgn*generators[e] for e,sgn in ordered if e in generators]))
    return generators, words


def elementary_presentation_cancellations(gens, words):
    # A relator containing generator x exactly once permits a homotopy-preserving
    # cellular 1/2 cancellation after sliding its incident two-cell.
    words = [list(w) for w in words]
    active_gens = set(gens.values())
    transcript = []
    while active_gens:
        options=[]
        for i, w in enumerate(words):
            for g in active_gens:
                if sum(abs(x)==g for x in w)==1:
                    options.append((len(w),g,i))
        if not options:
            raise AssertionError('Could not eliminate all 1-cell generators')
        _,g,i=min(options)
        w = words.pop(i)
        k = next(k for k, x in enumerate(w) if abs(x)==g)
        u,v = w[:k],w[k+1:]
        replacement = reduce_word(invert_word(u)+invert_word(v)) if w[k]>0 else reduce_word(v+u)
        assert all(abs(x)!=g for x in replacement)
        updated=[]
        for other in words:
            new=[]
            for x in other:
                if x==g: new.extend(replacement)
                elif x==-g: new.extend(invert_word(replacement))
                else: new.append(x)
            updated.append(reduce_word(new))
        words=updated
        active_gens.remove(g)
        transcript.append((g,len(w),len(replacement)))
    assert len(transcript)==11
    assert len(words)==1 and words[0]==[]
    return transcript


def main():
    faces, groups = edge_and_face_data()
    flags = flags_of_faces(faces)
    for name, actions, target_cells, target_collapses in (
        ('S5', [fa for fa,parity in groups.values()], (10,32,47,30,6),62),
        ('A5', [fa for fa,parity in groups.values() if parity==0],(14,58,94,60,12),100)):
        reps, seen, bdry, cofaces = quotient(flags, actions)
        counts = tuple(Counter(map(len,reps))[k] for k in range(1,6))
        assert counts == target_cells, (name,counts)
        live, pairs=free_face_collapse(reps,bdry,cofaces)
        assert len(pairs)==target_collapses, (name,len(pairs))
        counts_after=tuple(Counter(len(reps[i]) for i in live)[k] for k in range(1,6))
        if name=='S5':
            assert counts_after==(1,0,0,0,0)
            print('S5: 125 quotient flags; 62 elementary collapses; final point')
        else:
            assert counts_after==(8,18,12,0,0)
            generators,words=attaching_words(reps,seen,live)
            transcript=elementary_presentation_cancellations(generators,words)
            assert len(transcript)==11
            print('A5: 238 quotient flags; 100 elementary collapses')
            print('A5: 8 vertices, 18 edges, 12 faces; 7 tree edges contracted')
            print('A5: 11 elementary 1/2 cancellations; 1 remaining spherical 2-cell')
    print('PETERSEN_ORBIT_HOMOTOPY_OK')

if __name__=='__main__':
    main()
