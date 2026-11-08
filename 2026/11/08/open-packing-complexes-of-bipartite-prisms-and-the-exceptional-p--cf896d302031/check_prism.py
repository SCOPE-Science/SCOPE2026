"""Reproducible finite checks for open-packing prism factorization.
Run: python3 check_prism.py
Uses only the Python standard library.
"""
from collections import Counter
from itertools import combinations
from math import comb


def edge_set_graph(n, bitmask):
    edges = list(combinations(range(n), 2))
    return [e for k, e in enumerate(edges) if (bitmask >> k) & 1]


def graph_adjacency(n, edges):
    A = [set() for _ in range(n)]
    for u, v in edges:
        A[u].add(v)
        A[v].add(u)
    return A


def bipartition(A):
    n = len(A)
    colors = [-1] * n
    for root in range(n):
        if colors[root] != -1: continue
        colors[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for v in A[u]:
                if colors[v] == -1:
                    colors[v] = 1-colors[u]
                    stack.append(v)
                elif colors[v] == colors[u]:
                    return None
    return colors


def square_adjacency(A):
    n = len(A)
    return [{v for v in range(n) if v != u and (
             v in A[u] or bool(A[u] & A[v]))} for u in range(n)]


def prism_adjacency(A):
    n = len(A)
    B = [set() for _ in range(2*n)]
    for u in range(n):
        B[u].add(u+n)
        B[u+n].add(u)
        for v in A[u]:
            B[u].add(v)
            B[u+n].add(v+n)
    return B


def two_step(A):
    n = len(A)
    return [{v for v in range(n) if v != u and bool(A[u] & A[v])}
            for u in range(n)]


def poly_ind_sets(A):
    n = len(A)
    C = Counter()
    for mask in range(1 << n):
        vs = [i for i in range(n) if (mask >> i)&1]
        if all(v not in A[u] for u,v in combinations(vs,2)):
            C[len(vs)]+=1
    return C


def convolution(C, D):
    R = Counter()
    for i,a in C.items():
        for j,b in D.items(): R[i+j]+=a*b
    return R


def check_one(A, exhaustive=True):
    color = bipartition(A)
    if color is None: return False
    n = len(A)
    conflict = two_step(prism_adjacency(A))
    square = square_adjacency(A)
    # The permutation (u,layer) -> (u,layer XOR color(u))
    # makes two separate copies of the square graph.
    relabel = [u+n*(layer^color[u]) for layer in range(2) for u in range(n)]
    assert sorted(relabel) == list(range(2*n))
    for v in range(2*n):
        for w in range(v+1,2*n):
            a,b = v%n,w%n
            expected = v//n==w//n and b in square[a]
            assert (relabel[w] in conflict[relabel[v]]) == expected, (n,A,v,w)
    if exhaustive:
        C = poly_ind_sets(square)
        D = poly_ind_sets(conflict)
        assert D==convolution(C,C), (n,A,C,D)
    return True


def maximal_ind_poly(A):
    n=len(A)
    C=Counter()
    for mask in range(1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        if any(v in A[u] for u,v in combinations(sorted(S),2)):
            continue
        if any(all(s not in A[v] for s in S) for v in range(n) if v not in S):
            continue
        C[len(S)]+=1
    return C


def max_path_formula(n):
    C=Counter()
    # Each maximal set has a left offset 0..2, right offset 0..2,
    # and successive inter-vertex spacings in {3,4,5}.
    def visit(total, k):
        if total==n:
            C[k]+=1
        if total>=n: return
        for gap in (3,4,5):
            visit(total+gap,k+1)
    for a in range(3):
        for b in range(3):
            # End-offset b; first vertex at a+1.
            visit(a+b+1,1)
    return C


def check_path_explicit(n):
    A=graph_adjacency(n,[(i,i+1) for i in range(n-1)])
    assert check_one(A,exhaustive=n<=7)
    C=poly_ind_sets(square_adjacency(A))
    formula=Counter({k:comb(n-2*k+2,k) for k in range((n+2)//3+1) if n-2*k+2>=k})
    assert C==formula,(n,C,formula)
    M=maximal_ind_poly(square_adjacency(A))
    assert M==max_path_formula(n),(n,M,max_path_formula(n))
    wanted=set(range((n+4)//5,(n+2)//3+1))
    assert set(M)==wanted,(n,M,wanted)
    # The two-factor maximal open-packing polynomial is M squared.
    if n<=7:
        assert maximal_ind_poly(two_step(prism_adjacency(A))) == convolution(M,M)


def main():
    bipartite_checked=0
    all_graphs_checked=0
    for n in range(1,6):
        for m in range(1<<(n*(n-1)//2)):
            A=graph_adjacency(n,edge_set_graph(n,m))
            all_graphs_checked+=1
            if check_one(A): bipartite_checked+=1
    for n in range(1,13): check_path_explicit(n)
    # Odd cycle C_5 violates the asserted two-copy decomposition.
    A=graph_adjacency(5,[(i,(i+1)%5) for i in range(5)])
    assert bipartition(A) is None
    # The conflict graph of the prism is connected for odd cycle.
    H=two_step(prism_adjacency(A))
    seen={0}; queue=[0]
    while queue:
        for v in H[queue.pop()]:
            if v not in seen: seen.add(v); queue.append(v)
    assert len(seen)==10
    print('VERIFY_OK all_labeled_graphs_n1to5=%d bipartite_cases=%d identity_and_polynomials=PASS path_all_and_maximal_n1to12=PASS odd_cycle_boundary=PASS' % (all_graphs_checked,bipartite_checked))

if __name__=='__main__': main()
