"""Checks for the unicyclic graphical-zonotope third-intrinsic-volume theorem.

Python 3 standard library only. Analytic inequalities are proved in RESULT.md;
finite enumeration is an independent cross-check, not an infinite proof.
"""
from itertools import combinations
from math import comb, factorial, sqrt
from random import Random

A = 2 * sqrt(2) - sqrt(6)
B = 2 + 4 * sqrt(2) - 3 * sqrt(6)
C = 2 * sqrt(6) - 2 - 2 * sqrt(2)
D = 3 * sqrt(6) - 4 * sqrt(2)


def components_count(n, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for u, v in edges:
        a, b = root(u), root(v)
        if a != b:
            parent[a] = b
    return len({root(i) for i in range(n)})


def combinatorial_profile(n, edges):
    degree = [0] * n
    E = set(edges)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    W = sum(comb(x, 2) for x in degree if x >= 2)
    S = sum(comb(x, 3) for x in degree if x >= 3)
    T = sum(int((i, j) in E and (i, k) in E and (j, k) in E)
            for i, j, k in combinations(range(n), 3))
    P = sum((degree[u] - 1) * (degree[v] - 1) for u, v in edges) - 3*T
    return W, S, T, P, degree


def third_edge_types(edges):
    # Number of distinct vertices of a three-edge subgraph identifies its type.
    counts = {3: 0, 4: 0, 5: 0, 6: 0}
    for e, f, g in combinations(edges, 3):
        counts[len({*e, *f, *g})] += 1
    return counts


def determinant_of_gram_3(e, f, g):
    vectors=[]
    n=max(*e,*f,*g)+1
    for u,v in (e,f,g):
        w=[0]*n
        w[u]=1; w[v]=-1
        vectors.append(w)
    x=sum(a*b for a,b in zip(vectors[0],vectors[1]))
    y=sum(a*b for a,b in zip(vectors[0],vectors[2]))
    z=sum(a*b for a,b in zip(vectors[1],vectors[2]))
    return 8 + 2*x*y*z - 2*(x*x+y*y+z*z)


def cycle_value(n):
    # Formula counts three-edge matchings, separated wedges and three-paths.
    return (2*sqrt(2)*(comb(n,3)-n*(n-3))
            +sqrt(6)*n*(n-4)+2*n)


def runner_gap(n):
    return A*(n-2)+C-B


def volume_from_types(k):
    return 2*k[4]+sqrt(6)*k[5]+2*sqrt(2)*k[6]


def check_one(n, edges, do_gram):
    W,S,T,P,degree = combinatorial_profile(n,edges)
    k=third_edge_types(edges)
    assert sum(k.values()) == comb(n,3)
    assert k[3]==T and k[4]==P+S
    assert k[5]+2*P+3*S+3*T == W*(n-2)
    assert W-n==sum(comb(x-1,2) for x in degree if x>=3)
    assert 3*S <= (n-1)*(W-n)
    z=volume_from_types(k)
    z2=2*sqrt(2)*comb(n,3)-A*(n-2)*W-C*P+B*S-D*T
    assert abs(z-z2)<1e-7*max(1,abs(z))
    assert z <= cycle_value(n)+1e-8
    if W==n:
        assert all(d==2 for d in degree)
        assert abs(z-cycle_value(n))<1e-8
    elif n>=5:
        assert z <= cycle_value(n)-runner_gap(n)+1e-8
    if do_gram:
        for three in combinations(edges,3):
            determinant=determinant_of_gram_3(*three)
            distinct=len(set().union(*map(set,three)))
            assert determinant=={3:0,4:4,5:6,6:8}[distinct]
    return W,S,T,P,z


def exhaustive():
    total=0
    for n in range(4,8):
        all_edges=list(combinations(range(n),2))
        cycle_count=runner_count=connected_count=0
        for idx in combinations(range(len(all_edges)),n):
            ed=[all_edges[i] for i in idx]
            if components_count(n,ed)!=1: continue
            connected_count+=1
            W,S,T,P,z=check_one(n,ed,do_gram=(n<=6))
            if W==n:
                cycle_count+=1
            elif n>=5 and abs(z-cycle_value(n)+runner_gap(n))<1e-8:
                runner_count+=1
                assert W==n+1 and S==1 and T==0 and P==n+1
        assert cycle_count==factorial(n-1)//2
        if n>=5:
            assert runner_count==factorial(n)//2
        total+=connected_count
        print('exhaustive_n=%d connected=%d cycle_labelings=%d runner_labelings=%d' %
              (n,connected_count,cycle_count,runner_count))
    return total


def randomized():
    rng=Random(8041)
    total=0
    for n in range(8,21):
        for _ in range(100):
            # Random tree by building a connected graph, then one extra edge.
            edges=[]
            for j in range(1,n):
                i=rng.randrange(j)
                edges.append(tuple(sorted((i,j))))
            present=set(edges)
            while True:
                a,b=rng.sample(range(n),2)
                extra=tuple(sorted((a,b)))
                if extra not in present:break
            edges.append(extra)
            check_one(n,edges,do_gram=False)
            total+=1
    return total


if __name__=='__main__':
    assert A>0 and B>0 and C>0 and D>2*C
    assert 8+10*sqrt(2)-9*sqrt(6)>0
    assert A*3-C*4/3>0
    exact_graphs=exhaustive()
    random_graphs=randomized()
    print('UNICYCLIC_THIRD_INTRINSIC_CHECKS_PASSED exhaustive_graphs=%d random_graphs=%d' %(exact_graphs,random_graphs))
