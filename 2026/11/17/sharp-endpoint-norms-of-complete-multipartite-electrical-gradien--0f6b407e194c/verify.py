"""Exact independent checks for edge-gradient projections on complete multipartite graphs.

Requires sympy; run: python verify.py
"""
from fractions import Fraction
from itertools import product
from sympy import Matrix, Rational


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for k in range(minimum, n + 1):
        for other in partitions(n - k, k):
            yield (k,) + other


def predicted_edge_row(n, a, b):
    def h(s):
        return Rational(n*n-2*n-s*s+2, n*(n-s))
    return h(a)+h(b)


def exact_matrix(parts):
    n = sum(parts)
    vertex_part = [idx for idx, size in enumerate(parts) for _ in range(size)]
    edges = [(u,v) for u in range(n) for v in range(u+1,n) if vertex_part[u] != vertex_part[v]]
    B = Matrix([[int(v==w) - int(u==w) for w in range(n-1)] for u,v in edges])
    lap = B.T*B
    # Grounded Dirichlet inverse provides exactly the same edge gradients as the Laplacian pseudoinverse.
    P = B*lap.inv()*B.T
    return vertex_part, edges, P


def global_max(n):
    if n==2: return Rational(1)
    if n==3: return Rational(4,3)
    if n==4: return Rational(3,2)
    if n==5: return Rational(26,15)
    if n%2==0: return Rational(3)-Rational(8*(n-1), n*n)
    return Rational(3)-Rational(8,n+1)


count_graphs=0
count_rows=0
count_witness=0
for n in range(2,11):
    for part_sizes in partitions(n):
        if len(part_sizes)<2: continue
        vp, edges, P=exact_matrix(part_sizes)
        assert P==P.T and P*P==P
        expected = max(predicted_edge_row(n, part_sizes[vp[u]], part_sizes[vp[v]]) for u,v in edges)
        for row_idx,(u,v) in enumerate(edges):
            target=predicted_edge_row(n,part_sizes[vp[u]],part_sizes[vp[v]])
            measured=sum(abs(P[row_idx,col]) for col in range(len(edges)))
            assert measured==target,(part_sizes,u,v,measured,target)
            signs=Matrix([1 if P[row_idx,col]>0 else (-1 if P[row_idx,col]<0 else 0) for col in range(len(edges))])
            assert abs((P*signs)[row_idx])==measured
            count_rows+=1
            count_witness+=1
        assert max(sum(abs(P[row,col]) for col in range(len(edges))) for row in range(len(edges)))==expected
        assert expected <= global_max(n)
        count_graphs+=1
    print('order',n,'graphs checked')
print('EXACT_GROUNDED_LAPLACIAN_PROJECTION_GRAPHS_PASSED',count_graphs)
print('EXACT_EDGE_ROW_FORMULAS_PASSED',count_rows)
print('EXACT_SIGN_EXTREMIZERS_PASSED',count_witness)

# Independently enumerate all partitions and find all unrestricted multipartite maxima.
case_count=0
for n in range(2,19):
    winners=[]
    observed=Rational(0)
    for parts in partitions(n):
        if len(parts)<2:continue
        val=max(predicted_edge_row(n,a,b) for i,a in enumerate(parts) for b in parts[i+1:])
        if val>observed:observed=val;winners=[parts]
        elif val==observed:winners.append(parts)
    assert observed==global_max(n), (n,observed,global_max(n))
    if n==2: expected={(1,1)}
    elif n==3:expected={(1,1,1)}
    elif n==4:expected={(1,1,1,1),(1,1,2),(2,2)}
    elif n==5:expected={(1,2,2)}
    elif n==7:expected={(1,3,3),(3,4)}
    else:expected={(n//2,(n+1)//2)}
    assert set(winners)==expected, (n,winners)
    case_count+=1
print('PARTITION_EXTREMAL_CLASSIFICATION_PASSED',case_count)
print('ALL_EXACT_MULTIPARTITE_HODGE_ENDPOINT_CHECKS_PASSED')
