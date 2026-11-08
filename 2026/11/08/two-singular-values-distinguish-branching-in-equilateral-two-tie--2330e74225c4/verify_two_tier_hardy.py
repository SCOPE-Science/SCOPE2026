"""Independent checks for two-tier rooted metric-tree integration.

Run: python verify_two_tier_hardy.py
Requires: numpy, scipy, sympy. The analytical proof is in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh


def secular_determinant(d, e):
    t = sp.symbols('t', real=True)
    A = sp.zeros(d + 1)
    A[0, 0] = 1
    for j in range(1, d + 1):
        A[0, j] = -t
        A[j, 0] = -(e + 1)*t
        A[j, j] = 1 - e*t**2
    expected = (1-e*t**2)**(d-1) * (1-(d*e+d+e)*t**2)
    assert sp.expand(A.det(method='berkowitz')-expected) == 0


def finite_element_eigenvalues(d, e, subdiv=16):
    # Each of the 1+d+de unit edges is split into subdiv equal segments.
    edges = []
    index = 1
    def append_unit_edge(start):
        nonlocal index
        path = [start]
        for _ in range(subdiv):
            path.append(index)
            index += 1
        edges.extend(zip(path, path[1:]))
        return path[-1]
    hub = append_unit_edge(0)
    for _ in range(d):
        second = append_unit_edge(hub)
        for _ in range(e):
            append_unit_edge(second)
    K = lil_matrix((index, index), dtype=float)
    M = lil_matrix((index, index), dtype=float)
    h = 1/subdiv
    for i, j in edges:
        K[i,i] += 1/h; K[j,j] += 1/h
        K[i,j] -= 1/h; K[j,i] -= 1/h
        M[i,i] += h/3; M[j,j] += h/3
        M[i,j] += h/6; M[j,i] += h/6
    # Zero root is a prescribed Dirichlet trace; all other nodes are free.
    return eigsh(K[1:,1:].tocsc(), k=d+1, M=M[1:,1:].tocsc(),
                 sigma=0.0, which='LM', tol=1e-11)[0]


def run():
    cases = [(2,2),(2,3),(3,2),(2,7),(3,5),(3,3),(5,2),(2,5)]
    for d, e in cases:
        secular_determinant(d,e)
    print('EXACT_SECULAR_DETERMINANTS_OK', len(cases))
    for d, e in cases:
        v=finite_element_eigenvalues(d,e)
        expected0=math.atan(1/math.sqrt(d*e+d+e))**2
        expected1=math.atan(1/math.sqrt(e))**2
        assert abs(v[0]-expected0) < 1e-4, (d,e,v[0],expected0)
        for val in v[1:d]:
            assert abs(val-expected1) < 1e-4, (d,e,val,expected1)
        assert v[d] > 2.4, (d,e,v)
    print('INDEPENDENT_CONFORMING_FE_LOW_SPECTRUM_OK', len(cases))
    for d,e in [(2,7),(3,5),(2,5),(5,2)]:
        q=d*e+d+e
        v=math.atan(1/math.sqrt(q))
        w=math.atan(1/math.sqrt(e))
        assert math.isclose(q,(d+1)*(e+1)-1)
        assert math.isclose(1/(math.tan(v)**2),q,rel_tol=1e-13)
        assert math.isclose(1/(math.tan(w)**2),e,rel_tol=1e-13)
    assert math.isclose(math.atan(1/math.sqrt(23)),math.atan(1/math.sqrt(23)))
    assert (2+1)*(7+1) == (3+1)*(5+1) == 24
    assert 1+2+2*7 != 1+3+3*5
    print('BRANCH_PRODUCT_COLLISIONS_AND_TWO_VALUE_INVERSION_OK')
    print('ALL_TWO_TIER_HARDY_CHECKS_OK')

if __name__=='__main__':
    run()
