"""Exact integral degree-one cubical checks for small incidence relations.

The output reports the invariant factors of the first normalized cubical
homology from the complete 0,1,2-cube chain groups. This is a finite
verification, not a substitute for the all-hypergraph proof.
"""
from itertools import combinations, product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def first_cubical_h1(vertex_count, hyperedges):
    """Integral H1 via direct normalized Box cubes of dimensions <=2.

    A constant cube direction is omitted; reversing a 1-cube remains a
    separate generator until its relation is supplied by 2-cubes.
    """
    hyp = [frozenset(e) for e in hyperedges]
    V = range(vertex_count)
    if not all(any(v in e for e in hyp) for v in V):
        raise ValueError('All vertices must be supported')
    adj = set()
    for e in hyp:
        adj.update(frozenset(pair) for pair in combinations(e,2))
    undirected = sorted((tuple(sorted(e)) for e in adj))
    index = {e: i for i,e in enumerate(undirected)}
    m = len(undirected)
    parent = list(V)
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    forest = set()
    for u,v in undirected:
        if root(u) != root(v):
            parent[root(u)] = root(v)
            forest.add((u,v))
    chords = [e for e in undirected if e not in forest]
    chord_idx = {e:i for i,e in enumerate(chords)}
    cycle_rank = len(chords)
    relation_set = set()

    def arc(tail,head):
        if tail==head: return None
        e = tuple(sorted((tail,head)))
        if e not in index: raise ValueError('invalid edge')
        return e, 1 if tail<head else -1

    # Directed 2-cube faces, with order (00,10,01,11).
    for a,b,c,d in product(V, repeat=4):
        if not ((a!=b or c!=d) and (a!=c or b!=d)):
            continue
        if any(x!=y and frozenset((x,y)) not in adj for x,y in ((a,b),(a,c),(b,d),(c,d))):
            continue
        # Boundary = (a,b)+(b,d)-(a,c)-(c,d).
        forward = [0]*m
        backward = [0]*m
        for s,t,sgn in ((a,b,1),(b,d,1),(a,c,-1),(c,d,-1)):
            w=arc(s,t)
            if w is None: continue
            e,orientation=w
            if orientation==1: forward[index[e]] += sgn
            else: backward[index[e]] += sgn
        z=[forward[i]-backward[i] for i in range(m)]
        if any(sum((z[index[e]] * (1 if v==e[1] else -1) for e in undirected if v in e),0)
               for v in V):
            raise AssertionError('2-cube boundary not a cycle')
        row = tuple(z[index[e]] for e in chords) + tuple(backward)
        if any(row): relation_set.add(row)

    k = cycle_rank + m
    if k == 0: return (0,())
    rows = list(relation_set)
    mat = Matrix(rows).T if rows else Matrix.zeros(k,0)
    D = smith_normal_form(mat, domain=ZZ)
    diagonal = [abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i] != 0]
    torsion = tuple(d for d in diagonal if d>1)
    return (k-len(diagonal),torsion)


def incidence_dual(n,hyperedges):
    return len(hyperedges), [tuple(i for i,e in enumerate(hyperedges) if v in e) for v in range(n)]


def case(name,n,hyperedges,expected=None):
    a=first_cubical_h1(n,hyperedges)
    dn,de=incidence_dual(n,hyperedges)
    b=first_cubical_h1(dn,de)
    assert a==b,(name,a,b)
    if expected is not None: assert a==expected,(name,a,expected)
    print(name, 'vertices',n,'hyperedges',len(hyperedges),'H1_Z',a)


def main():
    case('single edge',3,[(0,1,2)],(0,()))
    case('loose 5-cycle',10,[(i,(i+1)%5,5+i) for i in range(5)],(1,()))
    case('loose 4-cycle',8,[(i,(i+1)%4,4+i) for i in range(4)],(0,()))
    case('five-cycle graph',5,[(i,(i+1)%5) for i in range(5)],(1,()))
    case('unequal incidence degrees',6,[(0,1,2),(1,2,3),(0,3,4),(2,4,5),(0,5)],None)
    case('Fano triples',7,[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)],None)
    print('DUAL_BOX_H1_INTEGRAL_FINITE_CHECK_PASS')

if __name__ == '__main__':
    main()
