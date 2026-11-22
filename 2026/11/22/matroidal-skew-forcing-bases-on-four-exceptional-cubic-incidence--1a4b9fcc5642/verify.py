#!/usr/bin/env python3
"""Exact verification of skew forcing on four finite cubic incidence graphs.
Python 3 standard library only. Run: python3 verify.py
"""
from itertools import combinations
from collections import Counter, deque


def graph(name):
    if name == 'Heawood':
        return 14, [(i, 7+j) for i in range(7) for j in range(7)
                    if (j-i) % 7 in (0, 1, 3)]
    if name == 'Mobius-Kantor':
        return 16, ([(i, (i+1) % 8) for i in range(8)]
                    + [(8+i, 8+(i+3) % 8) for i in range(8)]
                    + [(i, i+8) for i in range(8)])
    if name == 'Pappus':
        p = list((x, y) for x in range(3) for y in range(3))
        return 18, [(i, 9+3*k+c) for i, (x, y) in enumerate(p)
                    for k in range(3) for c in range(3)
                    if (x, y, (y-x) % 3)[k] == c]
    if name == 'Desargues':
        p = list(combinations(range(5), 2))
        t = list(combinations(range(5), 3))
        return 20, [(i, 10+j) for i, pair in enumerate(p)
                    for j, tri in enumerate(t) if set(pair).issubset(tri)]
    raise ValueError(name)


def bicolor(n, edges):
    adj = [set() for _ in range(n)]
    for i,j in edges:
        assert i != j
        adj[i].add(j); adj[j].add(i)
    assert len(edges) == 3*n//2 and all(len(z)==3 for z in adj)
    col = [-1]*n; col[0] = 0;todo = deque([0])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if col[v] < 0: col[v] = 1-col[u];todo.append(v)
            assert col[u] != col[v]
    assert -1 not in col
    a = [i for i in range(n) if col[i] == 0]
    b = [i for i in range(n) if col[i] == 1]
    assert len(a) == len(b) == n//2
    return adj, a, b


def shore_sets(adj, shore):
    m = len(shore);index = {u:i for i,u in enumerate(shore)}
    blocks = [sum(1<<index[v] for v in adj[u]) for u in range(len(adj)) if u not in index]
    full = (1<<m)-1
    def succeeds(seed):
        blue = seed
        while True:
            white = full ^ blue
            newly = 0
            for b in blocks:
                white_nb = b & white
                if white_nb != 0 and white_nb & (white_nb - 1) == 0:
                    newly |= white_nb
            if not newly: return blue == full
            blue |= newly
    feasible = [x for x in range(full+1) if succeeds(x)]
    poly = Counter(x.bit_count() for x in feasible)
    k = min(poly)
    bases = [x for x in feasible if x.bit_count()==k]
    return poly, k, bases, succeeds, blocks


def exchange_summary(bases):
    node = set(bases); ne = len(bases);links = {s:set() for s in bases}
    for x in bases:
        for y in bases:
            if x != y and (x ^ y).bit_count() == 2:
                links[x].add(y)
    edge_count = sum(map(len, links.values()))//2
    degrees = Counter(map(len, links.values()))
    ecc = Counter()
    for src in bases:
        dist = {src:0};pending=deque([src])
        while pending:
            u = pending.popleft()
            for v in links[u]:
                if v not in dist:
                    dist[v] = dist[u]+1;pending.append(v)
        assert len(dist)==ne
        # Every graph is a matroid basis graph precisely when exchanges realize
        # the Hamming lower bound, which we check for every pair.
        assert all(d == (src ^ v).bit_count()//2 for v,d in dist.items())
        ecc[max(dist.values())]+=1
    return edge_count, dict(sorted(degrees.items())), dict(sorted(ecc.items()))

EXPECTED = {
 'Heawood': ({3:28,4:35,5:21,6:7,7:1}, 3, 28, 126, {9:28}, {3:28}),
 'Mobius-Kantor': ({3:48,4:70,5:56,6:28,7:8,8:1},3,48,300,{12:24,13:24},{3:48}),
 'Pappus': ({3:72,4:126,5:126,6:84,7:36,8:9,9:1},3,72,540,{15:72},{3:72}),
 'Desargues': ({4:125,5:222,6:205,7:120,8:45,9:10,10:1},4,125,930,{12:5,14:60,16:60},{3:5,4:120}),
}


def triple_system(name, shore, feasible, blocks):
    if name == 'Desargues': return
    m=len(shore);bad = {s for s in range(1<<m) if s.bit_count()==3 and not feasible(s)}
    assert len(bad)=={'Heawood':7,'Mobius-Kantor':8,'Pappus':12}[name]
    pair_freq=Counter()
    for mask in bad:
        vertices=[i for i in range(m) if mask>>i&1]
        for u,v in combinations(vertices,2):pair_freq[u,v]+=1
    assert all(v==1 for v in pair_freq.values())
    if name in ('Heawood','Mobius-Kantor'):
        assert bad == set(blocks)
    if name == 'Pappus':
        assert len(pair_freq)==36
        if set(shore)==set(range(9)):
            pts=list((x,y) for x in range(3) for y in range(3))
            affine={sum(1<<i for i,(x,y) in enumerate(pts)
                        if (x,y,(y-x)%3,(y+x)%3)[j] == c)
                    for j in range(4) for c in range(3)}
            assert bad == affine
            assert len(bad-set(blocks))==3
        else:
            # Explicit bijection to the same AG(2,3) triple system.
            # Order here is the line labels (x=0..2,y=0..2,y-x=0..2).
            assert shore == list(range(9,18))
            p=[0,1,2,3,5,4,6,7,8]
            pts=list((x,y) for x in range(3) for y in range(3))
            affine={sum(1<<i for i,(x,y) in enumerate(pts)
                        if (x,y,(y-x)%3,(y+x)%3)[j] == c)
                    for j in range(4) for c in range(3)}
            assert {sum(1<<p[i] for i in range(9) if mask>>i&1) for mask in bad} == affine


def desargues_tree_check(shore, succeeds):
    m=10
    assert len(shore)==m
    # 2-subset side or, via complementing the 3-subset side, its dual.
    for seed in range(1<<m):
        parent=list(range(5))
        def find(v):
            while parent[v]!=v:v=parent[v]
            return v
        pairs=list(combinations(range(5),2))
        for i,(u,v) in enumerate(pairs):
            if seed>>i&1: parent[find(u)] = find(v)
        assert succeeds(seed) == (len({find(i) for i in range(5)})==1)


def run():
    for name in EXPECTED:
        n, edges=graph(name)
        adj, a,b = bicolor(n,edges)
        left=shore_sets(adj,a); right=shore_sets(adj,b)
        exp,k,c,exed,degrees,ecc=EXPECTED[name]
        assert left[0] == right[0] == exp
        assert left[1] == right[1] == k
        assert len(left[2]) == len(right[2]) == c
        for side, v in [(a,left),(b,right)]:
            assert exchange_summary(v[2]) == (exed,degrees,ecc)
            triple_system(name,side,v[3],v[4])
        if name == 'Desargues':
            for side,v in [(a,left),(b,right)]:
                # For the 3-subset shore, reorder its indices by complement.
                if min(side) == 10:
                    p2=list(combinations(range(5),2))
                    p3=list(combinations(range(5),3))
                    dual_idx=[p2.index(tuple(i for i in range(5) if i not in t)) for t in p3]
                    def comp_suc(mask, old=v[3]):
                        recoded=sum(1<<i for i,j in enumerate(dual_idx) if mask>>j&1)
                        return old(recoded)
                    desargues_tree_check(side,comp_suc)
                else: desargues_tree_check(side,v[3])
        full_count=c*c
        full_edges=2*c*exed
        full_ecc=Counter()
        for i in ecc:
            for j in ecc: full_ecc[i+j] += ecc[i]*ecc[j]
        # No slides: all minima have k initially black vertices in each shore.
        # Every source edge crosses shores, hence every slide changes this balance.
        print(name, 'one-side poly',sorted(exp.items()),'minimum',2*k,
              'optima',full_count,'jump edges',full_edges,'jump ecc',dict(sorted(full_ecc.items())),
              'slides',0)
    print('ALL CHECKS PASSED')
if __name__=='__main__': run()
