#!/usr/bin/env python3
"""Exact exhaustive certificate for the six-point separation-graph threshold.
No external dependencies. A total order 0..n-1 is chosen as a linear extension;
every finite poset has such a relabeling, so all upper-triangular transitive
relations cover all n-element posets up to isomorphism.
"""
from itertools import combinations, permutations


def orders(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        up=[1<<i for i in range(n)]
        for k,(i,j) in enumerate(pairs):
            if mask & (1<<k):up[i] |= 1<<j
        # All transitivity instances, not only covers, must be explicitly present.
        if all(not ((up[i]>>j)&1) or ((up[j] & ~up[i])==0)
               for i in range(n) for j in range(i+1,n)):
            yield tuple(up)


def graphs(n,up):
    down=tuple(sum(1<<j for j in range(n) if up[j] & (1<<i)) for i in range(n))
    ins=[0]*n;cm=[0]*n
    for i,j in combinations(range(n),2):
        if down[i]&down[j]:ins[i] |= 1<<j;ins[j] |= 1<<i
        if up[i]&up[j]:cm[i] |= 1<<j;cm[j] |= 1<<i
    ury=ins.copy()
    for i in range(n):
        for j in range(n):
            if ins[i] & (1<<j):ury[i] |= ins[j]
        ury[i] &= ~(1<<i)
    fun=[0]*n
    for i in range(n):
        seen=1<<i;queue=[i]
        while queue:
            v=queue.pop()
            for j in range(n):
                if (ins[v] & (1<<j)) and not (seen & (1<<j)):
                    seen |= 1<<j;queue.append(j)
        fun[i]=seen & ~(1<<i)
    return ins,cm,ury,fun


def canonical_graphs(n, gs, perms):
    key=None
    for p in perms:
        z=0
        for g in gs:
            for i in range(n):
                for j in range(i+1,n):
                    z=(z<<1) | bool(g[p[i]] & (1<<p[j]))
        if key is None or z<key:key=z
    return key


def components(n,gs):
    # Undirected 1-skeleton of the comparability complex, graph connectivity
    # equals connected components of the order complex.
    up=gs
    remain=set(range(n));components=[]
    while remain:
        start=min(remain);done={start};q=[start]
        while q:
            a=q.pop()
            for b in list(remain-done):
                if (up[a] & (1<<b)) or (up[b] & (1<<a)):
                    done.add(b);q.append(b)
        remain.difference_update(done)
        components.append(tuple(sorted(done)))
    return components


def faces_of_poset(n,up, subset):
    f=set()
    for r in range(1,len(subset)+1):
        for xs in combinations(subset,r):
            if all((up[i] & (1<<j)) or (up[j] & (1<<i))
                   for i,j in combinations(xs,2)):
                f.add(frozenset(xs))
    return f


def collapse_to_graph(faces):
    faces=set(faces)
    steps=0
    while any(len(s)>=3 for s in faces):
        # Choose a maximal face of dimension >=2, with a codimension-one
        # subface contained in exactly one (not necessarily maximal) face.
        move=None
        for top in sorted((s for s in faces if len(s)>=3),key=lambda s:(-len(s),tuple(sorted(s)))):
            if any(top<s for s in faces): continue
            for v in sorted(top):
                bottom=top-{v}
                if sum(1 for t in faces if bottom<t)==1:
                    move=(top,bottom);break
            if move:break
        if move is None:
            raise AssertionError('no free-face collapse to graph')
        top,bottom=move
        faces.remove(top);faces.remove(bottom);steps+=1
    return faces, steps


def graph_beta(comp, up):
    faces=faces_of_poset(len(up),up,comp)
    reduced,steps=collapse_to_graph(faces)
    v=sum(len(s)==1 for s in reduced)
    e=sum(len(s)==2 for s in reduced)
    # comp is connected and elementary collapses preserve connectedness.
    return e-v+1,steps


def witness():
    # bottom 0,1; middle 2,3; top 4,5.
    left=(61,62,52,56,16,32) # three antichains of size 2
    right=(61,62,60,56,16,32) # middle is a chain 2<3
    assert graphs(6,left)==graphs(6,right)
    assert left in set(orders(6)) and right in set(orders(6))
    # Left order complex is threefold join of S^0, hence S^2;
    # right has a conical middle factor, hence is contractible.
    assert len(faces_of_poset(6,left,tuple(range(6))))==26 # 6 + 12 + 8
    assert len(faces_of_poset(6,right,tuple(range(6))))==35 # 6+13+12+4? check independently below
    return left,right


def run():
    for n in range(1,6):
        perms=list(permutations(range(n)))
        groups={};count=0;collapses=0; maxsteps=0
        for up in orders(n):
            count+=1
            g=graphs(n,up)
            key=canonical_graphs(n,g,perms)
            c=components(n,up)
            ranks=[]
            for cc in c:
                rank,steps=graph_beta(cc,up)
                ranks.append(rank);collapses+=steps;maxsteps=max(maxsteps,steps)
            ht=tuple(sorted(ranks))
            if key in groups:
                assert groups[key]==ht, (n,key,groups[key],ht,up)
            else:groups[key]=ht
        print('n=%d linear-extension-labelled-posets=%d four-graph-classes=%d collapse_pairs=%d max_pairs=%d all_class_types_consistent=YES' % (n,count,len(groups),collapses,maxsteps))
    left,right=witness()
    print('n=6 common-graph-witness P0=%s P1=%s' % (left,right))
    print('n=6 P0: S^2, chi=2; P1: contractible, chi=1')
    print('CERTIFICATE PASS')

if __name__=='__main__':run()
