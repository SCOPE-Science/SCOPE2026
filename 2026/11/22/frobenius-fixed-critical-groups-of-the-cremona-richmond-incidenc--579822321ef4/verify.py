#!/usr/bin/env python3
"""Exact Smith checks for the geometric Cremona-Richmond incidence graph.

Requires Python 3 and SymPy. No external files, network, or numerical tolerances.
"""
from itertools import combinations, permutations
from collections import Counter
import json
from sympy import Matrix, eye, diag, prod, factorint, symbols
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ


def sorted_pairs(parts):
    return tuple(sorted(tuple(sorted(pair)) for pair in parts))


def one_factors(unused):
    if not unused:
        yield ()
        return
    a = unused[0]
    for j in range(1, len(unused)):
        b = unused[j]
        for smaller in one_factors(unused[1:j] + unused[j + 1:]):
            yield sorted_pairs(((a, b),) + smaller)


DUADS = list(combinations(range(6), 2))
SYNTHEMES = sorted(set(one_factors(tuple(range(6)))))
assert len(DUADS) == len(SYNTHEMES) == 15
DINDEX = {d: i for i, d in enumerate(DUADS)}
SINDEX = {s: i + 15 for i, s in enumerate(SYNTHEMES)}
B = Matrix(15, 15, lambda i, j: int(DUADS[i] in SYNTHEMES[j]))
L = diag(*([3] * 30))
for i in range(15):
    for j in range(15):
        if B[i,j]:
            L[i,15+j] = L[15+j,i] = -1
assert all(sum(B[i, j] for j in range(15)) == 3 for i in range(15))
assert all(sum(B[i, j] for i in range(15)) == 3 for j in range(15))
assert (B * B.T).eigenvals() == {9:1,4:9,0:5}
assert L*Matrix.ones(30,1) == Matrix.zeros(30,1)


def perm_vertices(p):
    return ([DINDEX[tuple(sorted(p[x] for x in d))] for d in DUADS]
            + [SINDEX[sorted_pairs(tuple(tuple(p[x] for x in e) for e in syntheme))]
               for syntheme in SYNTHEMES])


def cycle_type(p):
    found = set()
    lengths=[]
    for start in range(6):
        if start not in found:
            j=start
            length=0
            while j not in found:
                found.add(j)
                length+=1
                j=p[j]
            lengths.append(length)
    return tuple(sorted(lengths,reverse=True))


def snf_invariants(A):
    D=smith_normal_form(A, domain=ZZ)
    values=[abs(int(D[i,i])) for i in range(min(D.shape))]
    assert all(t>0 for t in values)
    assert all(b%a==0 for a,b in zip(values,values[1:]))
    return tuple(v for v in values if v>1)


def quotient_matrix(p, root):
    order=perm_vertices(p)
    names=[i for i in range(30) if i!=root]
    Q=L.extract(names,names)
    R=Matrix(29,29, lambda i,j: int(names[i]==order[names[j]]) - int(names[i]==order[root]))
    T=Matrix(29,29, lambda i,j: int(names[i]==order[names[j]]) - int(order[names[j]]==root))
    assert R*Q == Q*T
    return Q.row_join(R-eye(29))


def invariants(p,root=29):
    A=quotient_matrix(p,root)
    # Two exact integer-lattice routes, including independent HNF pre-reduction.
    a=snf_invariants(A)
    H=hermite_normal_form(A)
    assert H.shape == (29,29)
    b=snf_invariants(H)
    assert a == b
    return a


# The zero-eigenvalue and nonzero Laplacian spectrum determine the tree count.
base=snf_invariants(L.extract(list(range(29)),list(range(29))))
assert base == (3,) + (15,)*7 + (45,)
assert prod(base)==3**10 * 5**8
assert (6*3**10*5**9)//30 == prod(base)

representatives={}
allperms=list(permutations(range(6)))
assert len(allperms)==720
for p in allperms:
    t=cycle_type(p)
    representatives.setdefault(t,p)
    vertex_order=perm_vertices(p)
    assert sorted(vertex_order)==list(range(30))
    # Verify actual equivariance of every graph edge under all 720 label permutations.
    for i in range(30):
        for j in range(i+1,30):
            assert L[i,j]==L[vertex_order[i],vertex_order[j]]
assert len(representatives)==11
records=[]
for t,p in sorted(representatives.items(),reverse=True):
    invari=invariants(p,29)
    assert invari==invariants(p,0)
    records.append({'cycle_type': list(t),'invariant_factors':list(invari),
                    'order': int(prod(invari)),'fixed_geometric_vertices':sum(i==j for i,j in enumerate(perm_vertices(p)))})
assert next(r for r in records if r['cycle_type']==[5,1])['fixed_geometric_vertices']==0
assert next(r for r in records if r['cycle_type']==[5,1])['invariant_factors']==[5,45]
assert next(r for r in records if r['cycle_type']==[6])['invariant_factors']==[3,15]
print(json.dumps({'ordinary_critical_group':list(base), 'spanning_trees':int(prod(base)),
                  'classes':records},ensure_ascii=False,indent=2))
print('IGUSA_CREMONA_RICHMOND_FIXED_CRITICAL_GROUP_VERIFIED_OK')
