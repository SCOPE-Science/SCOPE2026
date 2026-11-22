"""Independent finite tests for the punctured rectangular-mesh route theorem.

Run: python3 VERIFY.py
Uses Python standard library only. Exhaustive ranges are explicitly finite.
"""
from collections import deque
from itertools import combinations
from math import comb


def paths(a, b):
    for epos in combinations(range(a + b), a):
        es = set(epos)
        yield ''.join('E' if p in es else 'N' for p in range(a+b))


def trace(word):
    x = y = 0
    out = [(x, y)]
    for step in word:
        if step == 'E': x += 1
        else: y += 1
        out.append((x, y))
    return tuple(out)


def profile(word):
    x = 0
    result = []
    for step in word:
        if step == 'E': x += 1
        else: result.append(x)
    return tuple(result)


def component(word, i, j):
    # No admissible word meets (i,j); the layer i+j is its exact separator.
    x, y = trace(word)[i+j]
    assert y == i+j-x and x != i
    return 'above' if x < i else 'below'


def formulas(a,b,i,j):
    na = sum(comb(x+j,j)*comb(a-x+b-j-1,a-x) for x in range(i))
    nb = sum(comb(i+y,i)*comb(a-i-1+b-y,b-y) for y in range(j))
    da = a*(b-j-1)+(i-1)*(j+1)
    db = a*b-(i+1)*(b-j+1)
    through = comb(i+j,i)*comb(a+b-i-j,a-i)
    assert na + nb == comb(a+b,a)-through
    return {'above':(na,da),'below':(nb,db)}


def verify_case(a,b,i,j,full_distances=True):
    universe = set(paths(a,b))
    allowed = {w for w in universe if (i,j) not in trace(w)}
    adj = {}
    for w in allowed:
        adj[w] = set()
        for p in range(a+b-1):
            if w[p] == w[p+1]: continue
            candidate = w[:p]+w[p+1]+w[p]+w[p+2:]
            if candidate in allowed:
                # Check adjacency of geometric paths, not just move strings.
                assert sum(u!=v for u,v in zip(trace(w),trace(candidate)))==1
                adj[w].add(candidate)
    cats = {'above':set(),'below':set()}
    for w in allowed: cats[component(w,i,j)].add(w)
    expected = formulas(a,b,i,j)
    pairs = 0
    for side, ss in cats.items():
        assert len(ss) == expected[side][0], (a,b,i,j,side,'count')
        for w in ss:
            assert set(adj[w]) <= ss, (a,b,i,j,side,'cross edge')
        root = next(iter(ss))
        q = deque([root]); seen={root}
        while q:
            p=q.popleft()
            for t in adj[p]:
                if t not in seen: seen.add(t);q.append(t)
        assert seen == ss, (a,b,i,j,side,'connectivity')
        profiles = {w:profile(w) for w in ss}
        diam = 0
        if full_distances:
            for w in ss:
                q = deque([w]); dist={w:0}
                while q:
                    u=q.popleft()
                    for v in adj[u]:
                        if v not in dist:dist[v]=dist[u]+1;q.append(v)
                assert len(dist)==len(ss)
                for v, d in dist.items():
                    l1=sum(abs(x-y) for x,y in zip(profiles[w],profiles[v]))
                    assert d==l1,(a,b,i,j,side,w,v,d,l1)
                    diam=max(diam,d)
                    pairs+=1
        else:
            for w in ss:
                for v in ss:
                    diam=max(diam,sum(abs(x-y) for x,y in zip(profiles[w],profiles[v])))
        assert diam == expected[side][1], (a,b,i,j,side,'diam',diam)
        if a<=4 and b<=4:
            # Independent median condition: in-graph L1-median exists, unique.
            chosen=sorted(ss)[:min(8,len(ss))]
            memo={profile(w):w for w in ss}
            for p in chosen:
                for q in chosen:
                    for r in chosen:
                        med=tuple(sorted((x,y,z))[1] for x,y,z in zip(profiles[p],profiles[q],profiles[r]))
                        assert med in memo, (a,b,i,j,'median')
    return pairs


def main():
    cases=0; pairs=0
    for a in range(2,6):
        for b in range(2,6):
            for i in range(1,a):
                for j in range(1,b):
                    pairs+=verify_case(a,b,i,j,True)
                    cases+=1
    for a in range(6,9):
        for b in range(2,5):
            for i in range(1,a):
                for j in range(1,b):
                    verify_case(a,b,i,j,False)
                    cases+=1
    print('PASS',cases,'punctured rectangular meshes;',pairs,'ordered pair BFS distance comparisons')

if __name__=='__main__':
    main()
