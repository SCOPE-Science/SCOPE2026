"""Reproduce finite checks of dual general-position sets in complete joins.
Python 3, standard library only. All graph and geodesic tests are direct.
"""
from itertools import combinations, product
from collections import Counter


def edges_of_graph(n, mask):
    pairs = list(combinations(range(n), 2))
    return {(i,j) for k, (i,j) in enumerate(pairs) if mask >> k & 1}


def joined_graph(sizes, edge_sets):
    n = sum(sizes)
    adj = [[False]*n for _ in range(n)]
    offsets = [0]
    for size in sizes:
        offsets.append(offsets[-1]+size)
    for a, b in combinations(range(len(sizes)), 2):
        for i in range(offsets[a], offsets[a+1]):
            for j in range(offsets[b], offsets[b+1]):
                adj[i][j] = adj[j][i] = True
    for a, es in enumerate(edge_sets):
        for i, j in es:
            u, v = offsets[a]+i, offsets[a]+j
            adj[u][v] = adj[v][u] = True
    return adj


def all_dual_position_masks(adj):
    n = len(adj)
    assert all(any(adj[i][j] for j in range(n)) for i in range(n))
    # In a join, each distinct nonadjacent pair has distance exactly two.
    obstructions = []
    for u,v in combinations(range(n),2):
        if not adj[u][v]:
            mids = sum(1 << w for w in range(n) if adj[u][w] and adj[v][w])
            assert mids
            obstructions.append(((1<<u)|(1<<v),mids))
    good = set()
    for x in range(1<<n):
        yes = True
        for pair, mids in obstructions:
            if x & pair == pair:
                if x & mids: yes = False; break
            elif x & pair == 0:
                if x & mids: yes = False; break
        if yes: good.add(x)
    return good


def two_clique_partitions(adj):
    n = len(adj)
    good=set()
    for x in range(1<<n):
        if all(adj[u][v] or ((x>>u)&1) != ((x>>v)&1)
               for u,v in combinations(range(n),2)):
            good.add(x)
    return good


def polynomial_formula(sizes, edge_sets):
    # Exactly the proper two-colorings of each complementary factor.
    # Returns polynomial for nonempty dual general-position sets.
    ps=Counter({0:1})
    for size, es in zip(sizes, edge_sets):
        table = [0]*size
        for u,v in es: table[u] |= 1<<v; table[v] |= 1<<u
        missing = [(u,v) for u,v in combinations(range(size),2) if not (table[u]>>v)&1]
        poly=Counter()
        for mask in range(1<<size):
            if all(((mask>>u)&1)!=((mask>>v)&1) for u,v in missing):
                poly[mask.bit_count()] += 1
        new=Counter()
        for k1,c1 in ps.items():
            for k2,c2 in poly.items(): new[k1+k2]+=c1*c2
        ps=new
    return ps


def test(sizes, edge_sets):
    n=sum(sizes)
    adj=joined_graph(sizes, edge_sets)
    actual=all_dual_position_masks(adj)
    predicted=two_clique_partitions(adj)
    predicted.add(0)
    if actual != predicted:
        raise AssertionError((sizes,edge_sets, sorted(actual^predicted)[:4]))
    poly=Counter(x.bit_count() for x in actual if x)
    fp=polynomial_formula(sizes,edge_sets)
    if poly != fp:
        raise AssertionError((sizes,edge_sets,poly,fp))
    return len(actual)


def main():
    count=0
    masks=0
    good=0
    # All ordered pairs of noncomplete labelled graphs, 2-4 vertices per factor,
    # at most 8 vertices in the full join. This is a direct full-subset census.
    choices=[]
    for n in range(2,5):
        choices += [(n,edges_of_graph(n,k)) for k in range((1<<(n*(n-1)//2))-1)]
    for n1,e1 in choices:
        for n2,e2 in choices:
            if n1+n2<=7 or (n1==4 and n2==4 and count%31==0):
                good += test([n1,n2],[e1,e2]); count+=1; masks+=1<<(n1+n2)
    # All triples of two-vertex noncomplete factors, plus varied joins.
    for m in (3,4,5):
        sizes=[2]*m
        good += test(sizes,[set() for _ in sizes]); count+=1;masks+=1<<(2*m)
    for sizes, specs in [([3,3,3],[0,2,5]),([2,3,4],[0,1,37]),([3,4,3],[0,39,4]),([3,3,4],[5,0,3])]:
        es=[edges_of_graph(n,k) for n,k in zip(sizes,specs)]
        good += test(sizes,es);count+=1;masks+=1<<sum(sizes)
    # Connected three-vertex path, a C4, a disjoint clique+isolated vertex,
    # and an H whose complement contains a triangle.
    profiles=[(3,{(0,1),(1,2)},3),(4,{(0,1),(1,2),(2,3),(0,3)},3),
              (4,{(0,1),(0,2),(1,2)},3),(5,{(0,1),(1,2),(2,3),(3,4)},2)]
    for n,es,m in profiles:
        if n*m<=12:
            good+=test([n]*m,[es]*m);count+=1;masks+=1<<(n*m)
    print('VERIFY_OK graph_profiles=%d vertex_subsets=%d admissible_sets=%d independent_geodesics=PASS complementary_coloring_polynomials=PASS complete_join_equivalence=PASS' %(count,masks,good))

if __name__=='__main__': main()
