#!/usr/bin/env python3
"""Numerical low-dimensional corroboration of the stated Hansen-radius identity.

The general theorem is proved analytically; these tests sample finite graphs and
compare two independently constructed halfspace systems.
Requires NumPy and SciPy.  No external data or services.
"""
from itertools import combinations
import numpy as np
from scipy.spatial import HalfspaceIntersection


def cliques(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    ans = [()]
    for s in range(1, n+1):
        for S in combinations(range(n), s):
            if all(tuple(sorted(e)) in E for e in combinations(S, 2)):
                ans.append(S)
    return ans


def verify(n, edges, label):
    # H is the complementary graph of G. Cliques of H are stable sets of G.
    C = cliques(n, edges)
    A = [(-np.eye(n)[i]).tolist() for i in range(n)]
    b = [0.0]*n
    for S in C[1:]:
        v = np.zeros(n); v[list(S)] = 1.0
        A.append(v.tolist()); b.append(1.0)
    A = np.array(A); b = np.array(b)
    Qhalf = np.column_stack((A, -b))
    p0 = np.full(n, 1/(4*n))
    qverts = HalfspaceIntersection(Qhalf, p0, qhull_options='Qx').intersections
    M = max(float(np.dot(p,p)) for p in qverts)
    # Separate construction of the full Hansen polar from all signed stable-set vertices.
    V=[]
    for S in C:
        v=np.zeros(n+1);v[0]=1
        v[1+np.array(S,dtype=int)] = 1
        V.extend([v,-v])
    Hhalf = np.column_stack((np.array(V), -np.ones(len(V))))
    rverts = HalfspaceIntersection(Hhalf, np.zeros(n+1), qhull_options='Qx').intersections
    R2 = max(float(np.dot(z,z)) for z in rverts)
    assert abs(R2-(1+4*M)) < 5e-7, (label,R2,M)
    far=[z for z in rverts if abs(np.dot(z,z)-R2)<1e-7]
    assert all(abs(abs(z[0])-1)<1e-6 for z in far),label
    print(f'{label}: n={n} cliques={len(C)} Q_vertices={len(qverts)} '
          f'polar_vertices={len(rverts)} maxQnorm2={M:.9g} maxPolarNorm2={R2:.9g} '
          f'inradius={1/np.sqrt(R2):.10g} far={len(far)}')


if __name__=='__main__':
    for n,E,label in [
        (2,[], 'empty2'),
        (3,list(combinations(range(3),2)),'complete3'),
        (4,[(i,i+1) for i in range(3)],'path4'),
        (4,[(0,i) for i in range(1,4)],'star4'),
        (5,[(i,(i+1)%5) for i in range(5)],'cycle5'),
        (5,[(i,i+1) for i in range(4)],'path5'),
    ]:
        verify(n,E,label)
    print('HANSEN_FRACTIONAL_ANTIBLOCKER_CHECKS_PASSED')

# Independently sourced 35-vertex Ramsey(3,9) graph in graph6 format.
# Data: B. D. McKay, https://users.cecs.anu.edu.au/~bdm/data/r39_35.g6
# Its existence/uniqueness is discussed by Goedgebeur and Radziszowski (2013).
RAMSEY35 = 'bsaCCA?O?O_aC??`c@O@b?RcHQ?DcA@H?PC_@QO@@Q?DA@MP?RgKADoH?aR?KCbOC_JE?xO@AALC@AJPG?__V?_K@ROO_A@dOG@?_'


def decode_graph6(s):
    n = ord(s[0]) - 63
    assert 1 <= n <= 62
    bits = []
    for ch in s[1:]:
        k = ord(ch)-63
        assert 0 <= k < 64
        bits.extend((k >> j)&1 for j in range(5,-1,-1))
    assert len(bits) >= n*(n-1)//2
    adj = [0]*n
    b = 0
    for j in range(1,n):
        for i in range(j):
            if bits[b]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            b += 1
    return adj


def ramsey35_check():
    adj=decode_graph6(RAMSEY35)
    n=len(adj)
    assert n==35
    assert sum(x.bit_count() for x in adj)//2==140
    assert all(((adj[i]&adj[j]).bit_count()==0) for i in range(n)
               for j in range(i+1,n) if (adj[i]>>j)&1)
    # Maximal cliques of the complement are independent sets of the source.
    allmask=(1<<n)-1
    comp=[allmask ^(1<<i) ^ adj[i] for i in range(n)]
    best=0; maximal_count=0
    def bronk(k,P,X):
        nonlocal best,maximal_count
        if not P and not X:
            maximal_count += 1
            best=max(best,k)
            return
        ux=P|X
        pivot=max((i for i in range(n) if ux>>i&1),
                  key=lambda i:(P&comp[i]).bit_count(), default=0)
        todo=P&~comp[pivot]
        while todo:
            bit=todo & -todo
            v=bit.bit_length()-1
            bronk(k+1,P&comp[v],X&comp[v])
            P &= ~bit
            X |= bit
            todo &= ~bit
    bronk(0,allmask,0)
    assert best==8
    print(f'RAMSEY35_EXACT_CHECK_PASSED vertices={n} edges=140 '
          f'triangles=0 independence={best} maximal_independent_sets={maximal_count}')


if __name__=='__main__':
    ramsey35_check()
