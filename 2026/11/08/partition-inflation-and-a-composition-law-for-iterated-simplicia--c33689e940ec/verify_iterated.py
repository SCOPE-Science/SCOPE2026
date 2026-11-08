"""Independent finite checks for iterated simplicial r-tupling.

Run: python verify_iterated.py
Only Python standard library is required.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb, factorial


def parts_of_size(s, r):
    """Unordered partitions of the labeled set s into r-blocks."""
    s = frozenset(s)
    if not s:
        yield frozenset()
        return
    a = min(s)
    for extra in combinations(sorted(s - {a}), r - 1):
        block = frozenset((a, *extra))
        for rest in parts_of_size(s - block, r):
            yield frozenset((block, *rest))


def face_set_from_facets(facets):
    fs = {frozenset()}
    for facet in facets:
        for size in range(1, len(facet) + 1):
            fs.update(map(frozenset, combinations(sorted(facet), size)))
    return fs


def direct_iterated(faces, r, s):
    """Return vertices of D_r(D_s X) and its 1-skeleton, from the two definitions."""
    sblocks = sorted((f for f in faces if len(f) == s), key=lambda f:tuple(sorted(f)))
    midfaces = set()
    for k in range(1, len(sblocks) + 1):
        if k * s > max(map(len, faces)):
            break
        for bs in combinations(sblocks, k):
            if len(frozenset().union(*bs)) == k*s and frozenset().union(*bs) in faces:
                midfaces.add(frozenset(bs))
    iter_vertices = sorted((f for f in midfaces if len(f) == r),
                           key=lambda f:tuple(sorted(map(lambda b:tuple(sorted(b)), f))))
    verts = {f: frozenset().union(*f) for f in iter_vertices}
    graph_edges = set()
    if 2*r*s <= max(map(len, faces)):
        for i,j in combinations(range(len(iter_vertices)), 2):
            v,w=iter_vertices[i],iter_vertices[j]
            if len(v|w)==2*r and v|w in midfaces:
                graph_edges.add(frozenset((i,j)))
    return list(verts.values()), graph_edges


def check(n, facets, r, s):
    faces = face_set_from_facets(facets)
    unions, actual_edges = direct_iterated(faces, r, s)
    base = [f for f in faces if len(f) == r*s]
    copies = factorial(r*s)//(factorial(r)*factorial(s)**r)
    counts = Counter(unions)
    assert set(counts)==set(base) and set(counts.values())=={copies}, (n,r,s,counts)
    expected_edges = {frozenset((i,j)) for i,j in combinations(range(len(unions)),2)
                      if unions[i].isdisjoint(unions[j]) and unions[i]|unions[j] in faces}
    assert expected_edges == actual_edges, (n,r,s,len(expected_edges),len(actual_edges))
    return len(base), len(unions), len(actual_edges)


def ncomponents(num, edges):
    adj=[set() for _ in range(num)]
    for e in edges:
        i,j=tuple(e);adj[i].add(j);adj[j].add(i)
    seen=set(); components=[]
    for u in range(num):
        if u in seen: continue
        q=deque([u]);seen.add(u);nodes=[]
        while q:
            a=q.popleft();nodes.append(a)
            for v in adj[a]-seen: seen.add(v);q.append(v)
        components.append(nodes)
    return components


def main():
    for n in range(4,10):
        t=check(n,[range(n)],2,2)
        print(f'simplex_n={n} r=2 s=2 base_vertices={t[0]} iter_vertices={t[1]} iter_edges={t[2]}')
    for n in range(6,10):
        for r,s in ((2,3),(3,2)):
            b,v,e=check(n,[range(n)],r,s)
            print(f'simplex_n={n} r={r} s={s} base_vertices={b} iter_vertices={v} iter_edges={e}')
    t=check(8,[range(6),range(2,8)],2,2)
    print('two_facets_size_6_intersect_4',t)
    assert t == (29,87,0)
    faces=face_set_from_facets([range(9)])
    unions,edges=direct_iterated(faces,2,2)
    cs=ncomponents(len(unions),edges)
    assert len(cs)==1 and len(unions)==378 and len(edges)==2835
    beta=len(edges)-len(unions)+1
    assert beta==2458
    print(f'connected_n9 V={len(unions)} E={len(edges)} beta1_integral={beta}')
    assert check(6,[range(6)],2,3)==(1,10,0)
    assert check(6,[range(6)],3,2)==(1,15,0)
    print('ALL_ITERATION_CHECKS_OK')

if __name__=='__main__':main()
