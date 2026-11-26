"""Finite independent tests of limited domination in generalized Hamming graphs.
Requires Python 3 and NumPy/SciPy for the larger mixed-alphabet integer programs.
Finite tests corroborate but do not prove the unrestricted result.
"""
import itertools
import math
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def graph(qs):
    verts = list(itertools.product(*(range(q) for q in qs)))
    index = {v: k for k, v in enumerate(verts)}
    adj = []
    for v in verts:
        neigh = set()
        for i, q in enumerate(qs):
            for a in range(q):
                if a != v[i]:
                    w = list(v)
                    w[i] = a
                    neigh.add(index[tuple(w)])
        adj.append(neigh)
    return verts, adj


def direct_legal(mask, adj):
    for u, row in enumerate(adj):
        in_D = bool(mask & (1 << u))
        d_neighbors = sum(bool(mask & (1 << v)) for v in row)
        if in_D and (len(row) - d_neighbors > 1):
            return False
        if not in_D and d_neighbors == 0:
            return False
    return True


def geometric_legal(mask, verts, adj, qs):
    """Check separate geometric characterization without using domination."""
    n = len(verts)
    T = set(range(n)) - {u for u in range(n) if mask & (1 << u)}
    components = []
    while T:
        start = next(iter(T))
        seen = {start}
        stack = [start]
        while stack:
            v = stack.pop()
            for w in adj[v] & T:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        T.difference_update(seen)
        components.append(seen)
    for component in components:
        coordinate_values = [set(verts[u][i] for u in component) for i in range(len(qs))]
        # A face has each coordinate either completely free or fixed.
        for i, vals in enumerate(coordinate_values):
            if len(vals) not in (1, qs[i]):
                return False
        if math.prod(len(x) for x in coordinate_values) != len(component):
            return False
        if len(component) == n:
            return False
    for i, C in enumerate(components):
        for E in components[i+1:]:
            if min(sum(a != b for a,b in zip(verts[u],verts[v])) for u in C for v in E) < 3:
                return False
    return True


def expected_minima(verts, qs):
    qstar = min(qs)
    minimum = len(verts) - len(verts)//qstar
    masks = []
    for i,q in enumerate(qs):
        if q == qstar:
            for a in range(q):
                masks.append(sum(1 << u for u,v in enumerate(verts) if v[i] != a))
    return minimum, masks


def min_ilp(adj, forbidden, deadline=12):
    """Integer linear formulation directly from the defining constraints."""
    n = len(adj)
    row_count = 2*n+len(forbidden)
    A = lil_matrix((row_count,n), dtype=float)
    lo = np.full(row_count,-np.inf)
    hi = np.full(row_count,np.inf)
    for u,neigh in enumerate(adj):
        A[u,u] = 1  # domination x[u]+sum_neighbor x >=1
        for v in neigh: A[u,v] = 1
        lo[u] = 1
        A[n+u,u] = -len(neigh)  # if selected, at most one absent neighbor
        for v in neigh: A[n+u,v] = 1
        lo[n+u] = -1
    for k,mask in enumerate(forbidden):
        # Exclude this exact optimum when seeking another optimum.
        for u in range(n):
            if mask & (1<<u): A[2*n+k,u] = 1
        hi[2*n+k] = mask.bit_count()-1
    r=milp(c=np.ones(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),
           constraints=LinearConstraint(A.tocsr(),lo,hi),
           options={'time_limit':deadline,'mip_rel_gap':0})
    if r.status == 0:
        return ('optimal',int(round(r.fun)))
    if r.status == 2:
        return ('infeasible',None)
    return ('unresolved',None)


if __name__ == '__main__':
    small = [(2,),(3,),(2,2),(2,3),(3,3),(3,4),(2,2,2),(2,2,3),(2,3,3),(2,2,2,2)]
    large = [(3,3,3),(2,2,2,3),(3,3,4),(2,3,4),(2,4,4)]
    for qs in small:
        vertices, adj = graph(qs)
        minimum, expected = expected_minima(vertices,qs)
        valid = []
        for mask in range(1<<len(vertices)):
            by_definition = direct_legal(mask, adj)
            by_geometry = geometric_legal(mask, vertices, adj, qs)
            assert by_definition == by_geometry, ('structure',qs,mask)
            if by_definition: valid.append(mask)
        minsets = {m for m in valid if m.bit_count() == min(m.bit_count() for m in valid)}
        assert min(m.bit_count() for m in valid) == minimum
        assert minsets == set(expected)
        print('FULL',qs,'subsets',1<<len(vertices),'valid',len(valid),'min',minimum,'minsets',len(minsets))
    for qs in large:
        vertices, adj = graph(qs)
        minimum, expected = expected_minima(vertices,qs)
        assert all(direct_legal(m,adj) for m in expected)
        status, value = min_ilp(adj,[])
        assert status=='optimal' and value==minimum, ('minimum',qs,status,value)
        status2, value2 = min_ilp(adj,expected)
        assert status2=='optimal' and value2>minimum, ('rigidity',qs,status2,value2)
        print('INTEGER',qs,'order',len(vertices),'min',value,'next_nondictator',value2,'minsets',len(expected))
    print('VERIFY_OK')
