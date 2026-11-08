"""Exact finite-tree certificate for the random feasible-edge greedy matching law.

Run with Python 3 and NetworkX 3.x (requirements.txt).  No floating point
arithmetic is used in any mathematical assertion.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter, defaultdict
from math import factorial
import networkx as nx

TREE_COUNTS = {1:1, 2:1, 3:1, 4:2, 5:3, 6:6, 7:11,
               8:23, 9:47, 10:106, 11:235, 12:551, 13:1301}
COUNTS_NEGATIVE_13 = 6
WITNESS_G6 = 'Lp`?GCCO??_@?C'
WITNESS_NUMERATORS = (180, 1852, 5149, 4339)
WITNESS_DENOMINATOR = 11520

def matching_law(graph):
    """Coefficients of E[z^M] using first-feasible-edge conditioning."""
    n = len(graph)
    adj = [sum(1 << v for v in graph.neighbors(u)) for u in range(n)]

    @lru_cache(None)
    def law(vertices):
        edges = [(u,v) for u in range(n) if (vertices >> u) & 1
                 for v in range(u+1,n)
                 if ((vertices >> v) & 1) and ((adj[u] >> v) & 1)]
        if not edges:
            return (Fraction(1),)
        coefficients = [Fraction(0)] * (n//2+2)
        count = len(edges)
        for u,v in edges:
            remainder = law(vertices & ~(1 << u) & ~(1 << v))
            for j, probability in enumerate(remainder):
                coefficients[j+1] += probability / count
        while not coefficients[-1]:
            coefficients.pop()
        return tuple(coefficients)

    answer = law((1 << n)-1)
    assert sum(answer) == 1
    assert all(p >= 0 for p in answer)
    return answer

def discr_of_asc(p):
    if len(p) <= 2:
        return Fraction(1)
    if len(p) == 3:
        c, b, a = p
        return b*b - 4*a*c
    if len(p) == 4:
        d,c,b,a = p
        return b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d
    raise AssertionError('support width exceeds three')

def independent_edge_order_counts(graph):
    """Count all edge permutations, including rejected edges, by integer DP."""
    edges=list(graph.edges())
    m=len(edges)
    states={(0,0):1}  # (processed-edge bits, covered-vertex bits) -> orders
    for _ in range(m):
        next_states=defaultdict(int)
        for (processed,covered),number in states.items():
            for j,(u,v) in enumerate(edges):
                if (processed>>j)&1:
                    continue
                newcovered=covered
                if not (((covered>>u)&1) or ((covered>>v)&1)):
                    newcovered |= (1<<u)|(1<<v)
                next_states[(processed|(1<<j),newcovered)] += number
        states=next_states
    counts=defaultdict(int)
    for (_,covered),number in states.items():
        counts[covered.bit_count()//2] += number
    assert sum(counts.values()) == factorial(m)
    return counts

def main():
    distribution = Counter()
    nonreal_graphs = []
    checked = 0
    for n in range(1,14):
        k=0
        for graph in nx.nonisomorphic_trees(n):
            assert sorted(graph.nodes) == list(range(n))
            probs = matching_law(graph)
            first = next(i for i,x in enumerate(probs) if x)
            compressed = probs[first:]
            assert compressed[0] > 0
            assert all(x > 0 for x in compressed)
            distribution[(n,len(compressed)-1)] += 1
            disc = discr_of_asc(compressed)
            if disc < 0:
                assert n == 13, 'found smaller non-real-rooted distribution'
                nonreal_graphs.append(nx.to_graph6_bytes(graph, header=False).decode().strip())
            k+=1
            checked+=1
        assert k == TREE_COUNTS[n], (n,k)
        print('n=%d types=%d nonreal=%d widths=%s' % (
              n,k, len(nonreal_graphs) if n==13 else 0,
              {d:distribution[(n,d)] for d in range(4) if distribution[(n,d)]}),flush=True)
    assert len(nonreal_graphs) == COUNTS_NEGATIVE_13, nonreal_graphs
    assert sorted(nonreal_graphs) == sorted([
        'LpCPA?@?G?g??@','LpC`A?@?G?g??@','LpCa?C@?GAG??@',
        'LpD?GC@O??_@?@','LpD?GCCO??_@?C','Lp`?GCCO??_@?C'
    ]), nonreal_graphs
    T=nx.Graph()
    for j in range(3):
        hub=1+4*j
        T.add_edges_from([(0,hub),(hub,hub+1),(hub,hub+2),(hub+2,hub+3)])
    assert nx.is_isomorphic(T,nx.from_graph6_bytes(WITNESS_G6.encode()))
    assert T.number_of_nodes()==13 and nx.is_tree(T)
    assert sorted(dict(T.degree()).values()).count(3)==4
    P=matching_law(T)
    assert P[:3] == (Fraction(0),)*3
    assert P[3:] == tuple(Fraction(a,WITNESS_DENOMINATOR)
                          for a in WITNESS_NUMERATORS), P
    integral_discriminant = -12323232144
    a,b,c,d = WITNESS_NUMERATORS
    assert (c*c*b*b - 4*d*b*b*b - 4*c*c*c*a - 27*d*d*a*a
            +18*d*c*b*a)==integral_discriminant
    orders=independent_edge_order_counts(T)
    assert [orders[k] for k in range(3,7)] == [7484400,77006160,214095420,180415620]
    assert len(orders)==4
    print('PASS: %d unlabeled trees, six exceptional 13-vertex types; witness exact; 12! edge orders verified independently.'%checked)

if __name__=='__main__':
    main()
