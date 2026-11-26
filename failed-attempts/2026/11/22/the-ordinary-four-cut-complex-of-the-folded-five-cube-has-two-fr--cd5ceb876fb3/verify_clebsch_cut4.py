#!/usr/bin/env python3
"""Exact integral certificate for the folded-five-cube ordinary 4-cut complex.
This reconstructs all faces and checks unit triangular chain-boundary
certificates and the signed-incidence reduction using only Python stdlib.
"""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256

# Folded 5-cube: choose even-parity representatives of complementary
# classes of five-bit strings; quotient cube adjacency means distance 4.
labels = tuple(i for i in range(32) if i.bit_count()%2 == 0)
assert len(labels)==16
nbr = tuple(frozenset(j for j in range(16) if i!=j and
            (labels[i]^labels[j]).bit_count()==4) for i in range(16))
assert all(len(nbr[i])==5 for i in range(16))
assert all((i in nbr[j]) == (j in nbr[i]) for i in range(16) for j in range(16))
assert all(len(nbr[i]&nbr[j]) == (0 if j in nbr[i] else 2)
           for i in range(16) for j in range(i+1,16))

def connected(s):
    f=set(s);seen={s[0]};front=[s[0]]
    while front:
        i=front.pop()
        for j in nbr[i]&f:
            if j not in seen:seen.add(j);front.append(j)
    return len(seen)==len(f)

def connected_independent(s):
    # Separate transitive-closure implementation checks all 4-subsets.
    f=set(s);seen={s[0]}
    for _ in range(len(s)-1):seen.update({j for i in seen for j in nbr[i]&f})
    return len(seen)==len(f)

quad=tuple(combinations(range(16),4))
for q in quad:assert connected(q)==connected_independent(q)
disconnected=frozenset(q for q in quad if not connected(q))
connected_four=frozenset(q for q in quad if q not in disconnected)
assert (len(disconnected),len(connected_four))==(1140,680)

# Dual of the ordinary cut complex is the simplicial independence
# complex of the 4-uniform hypergraph of disconnected induced 4-sets.
# Enumerate independently all possible 5-sets and 6-sets.
five=tuple(q for q in combinations(range(16),5)
           if all(s in connected_four for s in combinations(q,4)))
six=tuple(q for q in combinations(range(16),6)
          if all(s in connected_four for s in combinations(q,4)))
assert len(five)==192 and not six

# Full 2-skeleton; the 2-cycle lattice has basis indexed by triples
# avoiding the distinguished vertex 0 (the boundaries [0,a,b,c]).
triples=tuple(combinations(range(1,16),3))
assert len(triples)==455
first=frozenset(t for t in triples if (0,)+t in connected_four)
second=frozenset(triples)-first
assert len(first)==170 and len(second)==285
nozero=tuple(sorted(f for f in connected_four if 0 not in f))

# Two rounds of exact integral unit pivots, using only original columns.
round_one={}
for f in nozero:
    s=set(combinations(f,3))&second
    if len(s)==1:round_one.setdefault(next(iter(s)),f)
assert len(round_one)==140
remaining=second-set(round_one)
assert len(remaining)==145
round_two={}
for f in nozero:
    s=set(combinations(f,3))&remaining
    if len(s)==1:round_two.setdefault(next(iter(s)),f)
assert set(round_two)==remaining

rows=tuple(sorted(first))+tuple(sorted(round_one))+tuple(sorted(round_two))
columns=(tuple((0,)+t for t in sorted(first))+
         tuple(round_one[t] for t in sorted(round_one))+
         tuple(round_two[t] for t in sorted(round_two)))
assert len(rows)==len(columns)==455
assert set(rows)==set(triples) and len(set(columns))==455
idx={t:i for i,t in enumerate(rows)}
product=1; nonzeros=0
for i,f in enumerate(columns):
    assert f in connected_four
    # In the standard cycle basis, take coefficients of triples not
    # containing 0 in the oriented tetrahedral boundary.
    coeff=({f[1:]:1} if 0 in f else
           {t:(-1)**j for j,t in enumerate(combinations(f,3))})
    assert coeff[rows[i]] in (-1,1)
    assert all(idx[t]<=i for t in coeff)
    product*=coeff[rows[i]]
    nonzeros+=len(coeff)
assert abs(product)==1

# Each 4-simplex is an induced five-cycle. Its boundary rows are
# 4-subsets, and each of the 480 participating rows has two incidences.
incidence={}
for k,f in enumerate(five):
    assert connected(f)
    assert len([1 for i in f for j in f if j in nbr[i]])==10 # C5
    for j,q in enumerate(combinations(f,4)):
        incidence.setdefault(q,[]).append((k,(-1)**j))
assert len(incidence)==480
assert all(q in connected_four and len(items)==2 for q,items in incidence.items())
assert len(connected_four-set(incidence))==200

# The dual graph of 192 facets is connected and consistently
# orientable. After changing signs of the 4-simplex basis, every row
# has entries (+1,-1), making d4 the transpose of a graph incidence
# matrix. A spanning tree yields a unimodular 191x191 minor.
adj=[[] for _ in five]
for q,items in incidence.items():
    (i,a),(j,b)=items
    assert i!=j
    fac=-a*b
    adj[i].append((j,fac))
    adj[j].append((i,fac))
orientation={0:1}; stack=deque([0])
while stack:
    i=stack.popleft()
    for j,fac in adj[i]:
        candidate=fac*orientation[i]
        if j not in orientation:
            orientation[j]=candidate;stack.append(j)
        else:assert orientation[j]==candidate
assert len(orientation)==192
assert sum(len(edges) for edges in adj)//2==480
assert Counter(orientation.values())=={1:96,-1:96}
assert all(a*orientation[i]+b*orientation[j]==0
           for (i,a),(j,b) in incidence.values())

# Integral conclusions: d3 onto Z^455, rank d4=191 with primitive
# image, ker d4=Z, ker d3 rank=680-455=225. Therefore H3=Z^34,
# H4=Z, and duality on 16 vertices yields cut H9=Z, H10=Z^34.
assert 680-455-191==34
assert -1+16-120+560-680+192==-33
witness='\n'.join(f'{i}: {rows[i]} {columns[i]}' for i in range(455))
print('graph=folded-five-cube; srg=(16,5,0,2); graph_edges=40')
print('connected_4=680; disconnected_4=1140')
print('cut_Alexander_dual_f_vector=(16,120,560,680,192); no_6faces=True')
print('d3_unimodular_pivot_rounds=(170,140,145); det_abs=1; nonzeros=%d'%nonzeros)
print('d3_witness_sha256='+sha256(witness.encode('utf-8')).hexdigest())
print('d4_rows=(480_twice,200_zero); dual_graph_edges=480; connected=True; orientable=True')
print('d4_rank=191; d4_primitive=True; H3_dual=Z^34; H4_dual=Z')
print('cut_reduced_H9=Z; cut_reduced_H10=Z^34; all_other=0')
print('PASS')
