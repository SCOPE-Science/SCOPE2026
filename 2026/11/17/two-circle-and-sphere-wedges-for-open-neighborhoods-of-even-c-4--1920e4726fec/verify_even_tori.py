#!/usr/bin/env python3
"""Exact finite checks for open neighborhood complexes of C4 x Cn.

No third-party packages. Universal assertions are proved in RESULT.md, not by
extrapolating these finite tests.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def simplices(n):
    faces = set()
    facets = []
    for r in range(4):
        for c in range(n):
            t = tuple(sorted((n * ((r-1) % 4) + c,
                              n * ((r+1) % 4) + c,
                              n*r + (c-1) % n,
                              n*r + (c+1) % n)))
            assert len(set(t)) == 4
            facets.append(t)
            for k in range(1, 5):
                faces.update(combinations(t, k))
    assert len(set(facets)) == 4*n
    return faces


def matching(n, faces):
    fibers = defaultdict(set)
    for f in faces:
        fibers[tuple(x for x in f if x >= n)].add(f)
    paired, pairs = set(), []

    def add(low, high):
        assert low in faces and high in faces
        assert len(high) == len(low)+1 and set(low).issubset(high)
        assert low not in paired and high not in paired
        paired.update((low,high))
        pairs.append((low, high))

    for F, fiber in fibers.items():
        if F:
            row0 = sorted({x for f in fiber for x in f if x < n})
            if row0:
                v = row0[0]
                # Verify entire row-zero extension fiber is a simplex.
                assert len(fiber) == 2**len(row0)
                for f in sorted(fiber):
                    if v not in f:
                        high = tuple(sorted((*f,v)))
                        assert high in fiber
                        add(f,high)
        else:
            unseen = set(range(n))
            while unseen:
                root = min(unseen)
                cycle = []
                current = root
                while current not in cycle:
                    cycle.append(current)
                    unseen.remove(current)
                    current = (current + 2) % n
                assert current == root
                for a,b in zip(cycle,cycle[1:]):
                    add((b,),tuple(sorted((a,b))))

    for c in range(n):
        edge = tuple(sorted((2*n+(c-1)%n, 2*n+(c+1)%n)))
        plus = tuple(sorted((*edge, n+c)))
        minus = tuple(sorted((*edge, 3*n+c)))
        tet = tuple(sorted((*edge,n+c,3*n+c)))
        add(edge,plus)
        add(minus,tet)

    critical = faces - paired
    assert Counter(map(len,critical)) == Counter({1:2,2:2,3:2*n})
    return pairs,critical


def no_gradient_cycles(faces,pairs):
    upwards = dict(pairs)
    out = defaultdict(list)
    indegree = {f:0 for f in faces}
    for high in faces:
        for j in range(len(high)):
            low = high[:j] + high[j+1:]
            if len(low) == 0:
                continue
            if upwards.get(low) == high:
                source,target=low,high
            else:
                source,target=high,low
            out[source].append(target)
            indegree[target] += 1
    q=deque(f for f in faces if indegree[f] == 0)
    visited=0
    while q:
        f=q.popleft()
        visited += 1
        for g in out[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    assert visited == len(faces)


def homology_mod2(n,faces):
    by_size={k:sorted(f for f in faces if len(f)==k) for k in range(1,5)}
    def rank(d):
        # rank of boundary C_d -> C_(d-1), with d>=1
        lower=by_size[d]
        upper=by_size[d+1]
        idx={f:i for i,f in enumerate(lower)}
        pivots={}
        for t in upper:
            row=0
            for g in combinations(t,d):
                row ^= 1<<idx[g]
            while row:
                i=row.bit_length()-1
                if i in pivots:
                    row ^= pivots[i]
                else:
                    pivots[i]=row
                    break
        return len(pivots)
    ranks={0:0,1:rank(1),2:rank(2),3:rank(3),4:0}
    betti=[len(by_size[k+1])-ranks[k]-ranks[k+1] for k in range(4)]
    betti[0] -= 1  # reduced H0
    assert betti == [1,2,2*n,0], (n,betti)


def winding(n,faces):
    def lift(a,b):
        delta=(b%n-a%n)%n
        if delta > n//2: delta-=n
        # A possible half-circle jump is never an edge in this complex.
        assert abs(delta) <= 2
        return delta
    for f in faces:
        if len(f)==3:
            x,y,z=f
            assert lift(x,y)+lift(y,z)+lift(z,x)==0
    # There are two step-2 row-zero cycles, each has winding exactly n.
    for root in (0,1):
        cur=root
        total=0
        for _ in range(n//2):
            nxt=(cur+2)%n
            total+=lift(cur,nxt)
            cur=nxt
        assert cur==root and total==n


def main():
    for n in range(6,21,2):
        faces=simplices(n)
        pairs,critical=matching(n,faces)
        no_gradient_cycles(faces,pairs)
        winding(n,faces)
        if n<=12: homology_mod2(n,faces)
        print(f'n={n} simplices={len(faces)} pairs={len(pairs)} critical_0=2 critical_1=2 critical_2={2*n} acyclic=YES winding=YES mod2={"YES" if n<=12 else "not_checked"}')
    print('VERIFY_OK 8 even cycle lengths, exact matchings and integer cocycle checks')


if __name__=='__main__':
    main()
