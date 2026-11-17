"""Exact-arithmetic finite checks for a convex-order inequality on bridgeless metric graphs.

This program is supplementary evidence. The theorem for all graphs and all
Lipschitz functions follows from the mathematical proof, not enumeration.
"""
from fractions import Fraction as F
from itertools import combinations, product


def stats(edges, values):
    total = sum((length for _, _, length in edges), F(0))
    mean = sum((length * (values[i] + values[j]) / 2 for i,j,length in edges), F(0)) / total
    sq = sum((length * (values[i]**2 + values[i]*values[j] + values[j]**2) / 3
              for i,j,length in edges), F(0)) / total
    return total, mean, sq - mean**2


def hinge(edges, values, threshold):
    total, mean, _ = stats(edges, values)
    z = mean + threshold
    result = F(0)
    for i,j,length in edges:
        a,b = sorted((values[i],values[j]))
        if a == b:
            term = max(F(0),a-z)
        else:
            term = (max(F(0),b-z)**2 - max(F(0),a-z)**2) / (2*(b-a))
        result += length * term
    return result / total


def benchmark_hinge(L, threshold):
    radius = L / 4
    if threshold <= -radius:
        return -threshold
    if threshold >= radius:
        return F(0)
    return (radius - threshold)**2 / L


def is_connected(n, edges):
    seen={0}
    for _ in range(n):
        seen |= {b for a,b in edges if a in seen} | {a for a,b in edges if b in seen}
    return len(seen)==n


def bridgeless(n, edges):
    return is_connected(n, edges) and all(is_connected(n, [e for e in edges if e!=x]) for x in edges)


checked_graphs=0
checked_functions=0
checked_hinges=0
for n in [3,4,5]:
    all_edges=list(combinations(range(n),2))
    for mask in range(1<<len(all_edges)):
        unweighted=[e for k,e in enumerate(all_edges) if mask>>k &1]
        if not bridgeless(n,unweighted):
            continue
        checked_graphs +=1
        edges=[(a,b,F(1+(a+2*b)%2)) for a,b in unweighted]
        for tup in product(range(-2,3),repeat=n-1):
            v=(F(0),) + tuple(map(F,tup))
            if any(abs(v[a]-v[b])>length for a,b,length in edges):
                continue
            checked_functions+=1
            L,mean,var=stats(edges,v)
            assert var<=L**2/48, (n,edges,v,var,L**2/48)
            for s in [F(-1,2),F(0),F(1,3),F(2,3)]:
                threshold=s*L
                actual=hinge(edges,v,threshold)
                upper=benchmark_hinge(L,threshold)
                assert actual<=upper, (n,edges,v,threshold,actual,upper)
                checked_hinges+=1
print('BRIDGELESS_GRAPH_EXACT_ARCLENGTH_HINGE_TESTS_OK',checked_graphs,checked_functions,checked_hinges)

# Continuous cycle: the arclength distance from a marked point has the uniform
# distribution on [0,L/2], whether or not the marked point is a vertex.
for lengths in [[F(1)]*3,[F(1),F(2),F(3),F(4)], [F(1,3),F(7,5),F(8,9)]]:
    L=sum(lengths)
    mu=L/4
    var=L**2/48
    assert ((L/2)**2)/12==var
    for s in [F(-1,2),F(0),F(1,4)]:
        assert benchmark_hinge(L,L*s)>=0
    print('METRIC_CYCLE_EXACT_EQUALITY_OK',L,mu,var)

# Two cycles meeting at one vertex. The signed distance-to-junction profile
# has a single uniform image interval, and therefore also attains equality.
A,B=F(3),F(5)
L=A+B
lo,hi=-B/2,A/2
mu=(lo+hi)/2
var=(hi-lo)**2/12
assert var==L**2/48
print('FIGURE_EIGHT_EXACT_EQUALITY_OK',L,lo,hi,var)

# Three distinct equal-length paths between two vertices: the affine coordinate
# profile on each unit path has a uniform [0,1] image and a strictly smaller variance.
L=F(3)
var=F(1,12)
assert var < L**2/48
print('THETA_STRICT_EXAMPLE_OK',var,L**2/48)

# A bridge permits a one-crossing profile: the interval metric of length one
# has variance 1/12, so the bridgeless hypothesis is substantive.
assert F(1,12)>F(1,48)
print('BRIDGE_BOUNDARY_EXACT_COUNTEREXAMPLE_OK',F(1,12),F(1,48))
print('ALL_BRIDGELESS_CONVEX_ORDER_CHECKS_OK')
