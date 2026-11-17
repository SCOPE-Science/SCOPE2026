"""Reproduce exact tree-zonotope dihedral-angle calculations.
Run: python check_tree_angles.py
Only the Python standard library is required.
"""
from fractions import Fraction
from itertools import combinations, product
from random import Random


def edges_from_prufer(seq):
    n = len(seq) + 2
    degrees = [1] * n
    for x in seq:
        degrees[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if degrees[i] == 1)
        edges.append((leaf, x))
        degrees[leaf] -= 1
        degrees[x] -= 1
    u, v = [i for i in range(n) if degrees[i] == 1]
    edges.append((u, v))
    return edges


def components(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    unseen = set(range(n))
    result = []
    while unseen:
        start = min(unseen)
        queue = [start]
        unseen.remove(start)
        for u in queue:
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    queue.append(v)
        result.append(set(queue))
    return result


def cut_triples(n, edges):
    for i, j in combinations(range(n-1), 2):
        remain = [edge for k,edge in enumerate(edges) if k not in (i,j)]
        parts = components(n, remain)
        assert len(parts) == 3
        e, f = edges[i], edges[j]
        unique_e = next(P for P in parts if len(P.intersection(e)) == 1 and P.isdisjoint(f))
        unique_f = next(P for P in parts if len(P.intersection(f)) == 1 and P.isdisjoint(e))
        middle = next(P for P in parts if P is not unique_e and P is not unique_f)
        yield (i,j), (len(unique_e),len(middle),len(unique_f)), (unique_e,unique_f)


def predicted_rho2(a, b, c):
    return Fraction(a*c, (a+b)*(b+c))


def normals_rho2(n, A, C):
    # Direct exact dot products of the true zero-sum facet normals.
    x = [Fraction(int(i in A), 1)-Fraction(len(A), n) for i in range(n)]
    y = [Fraction(int(i in C), 1)-Fraction(len(C), n) for i in range(n)]
    dot = sum(u*v for u,v in zip(x,y))
    nx = sum(u*u for u in x)
    ny = sum(v*v for v in y)
    return dot*dot/(nx*ny)


def bounds(n):
    a=(n-1)//2
    c=(n-1)-a
    return Fraction(1,(n-1)**2), Fraction(a*c,(a+1)*(c+1))


def test_tree(n, edges):
    low, high = bounds(n)
    best=Fraction(0)
    for (i,j),(a,b,c),(A,C) in cut_triples(n,edges):
        rho=predicted_rho2(a,b,c)
        assert rho==normals_rho2(n,A,C), (n,edges,i,j)
        for k,(u,v) in enumerate(edges):
            da=int(u in A)-int(v in A)
            dc=int(u in C)-int(v in C)
            assert abs(da)==int(k==i) and abs(dc)==int(k==j), (n,edges,i,j,k)
        assert low<=rho<=high, (n,edges,a,b,c)
        if rho>best: best=rho
    # Exact characterization of both universal equalities.
    expected_min = any(len([w for w in edges if v in w]) == 2 and
                       sorted([len(P) for P in components(n,[w for w in edges if v not in w]) if v not in P])
                       == [(n-1)//2,n-1-(n-1)//2] for v in range(n))
    expected_max = max(sum(v in w for w in edges) for v in range(n))==n-1
    assert (best==high)==expected_min, (n,edges,best,high)
    assert (best==low)==expected_max, (n,edges,best,low)
    return best


def main():
    count=0
    star_count=0
    balanced_count=0
    for n in range(3,7):
        for code in product(range(n), repeat=n-2):
            edges=edges_from_prufer(code)
            v=test_tree(n,edges)
            count+=1
            star_count+= (v == bounds(n)[0])
            balanced_count+=(v == bounds(n)[1])
    rng=Random(1729)
    for n in (7,8,12,20,50):
        for _ in range(12):
            test_tree(n,edges_from_prufer(tuple(rng.randrange(n) for __ in range(n-2))))
    print('TREE_ZONOTOPE_DIHEDRAL_PASS exact_labelled_trees=%d star_cases=%d balanced_degree2_cases=%d sampled_large_trees=60' % (count,star_count,balanced_count))

if __name__=='__main__':
    main()
