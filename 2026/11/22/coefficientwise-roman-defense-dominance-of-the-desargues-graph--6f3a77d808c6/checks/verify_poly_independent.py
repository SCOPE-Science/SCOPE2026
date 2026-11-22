#!/usr/bin/env python3
"""Independent, standard-library Roman enumeration on explicitly specified graphs.
The two graph structures are given as adjacency triples in a numbering distinct
from generalized Petersen coordinates. An explicit permutation certifies each
isomorphism, and a 3^10 direct labeling search tests the counting mechanism.
"""
from itertools import product
from math import comb
from pathlib import Path
import json

DODECA = [
 (1,10,19),(0,2,8),(1,3,6),(2,4,19),(3,5,17),
 (4,6,15),(2,5,7),(6,8,14),(1,7,9),(8,10,13),
 (0,9,11),(10,12,18),(11,13,16),(9,12,14),(7,13,15),
 (5,14,16),(12,15,17),(4,16,18),(11,17,19),(0,3,18)]
DESARGUES = [
 (1,5,19),(0,2,16),(1,3,11),(2,4,14),(3,5,9),
 (0,4,6),(5,7,15),(6,8,18),(7,9,13),(4,8,10),
 (9,11,19),(2,10,12),(11,13,17),(8,12,14),(3,13,15),
 (6,14,16),(1,15,17),(12,16,18),(7,17,19),(0,10,18)]
MAP2 = [0,1,8,7,14,15,16,17,18,19,10,2,9,6,13,5,12,4,11,3]
MAP3 = [0,1,16,15,14,13,8,9,10,19,5,2,17,6,3,12,7,4,11,18]

def check_graph(neighbors,k,perm):
    n=len(neighbors)
    assert n==20 and sorted(perm)==list(range(n))
    assert all(len(set(t))==3 and i not in t for i,t in enumerate(neighbors))
    assert all(i in neighbors[j] for i,t in enumerate(neighbors) for j in t)
    expected=set()
    for i in range(10):
        for a,b in [(i,(i+1)%10),(i,10+i),(i+10,10+(i+k)%10)]:
            expected.add(tuple(sorted((perm[a],perm[b]))))
    edges={tuple(sorted((i,j))) for i,t in enumerate(neighbors) for j in t}
    assert edges==expected and len(edges)==30

def poly(neighbors):
    n=len(neighbors)
    N=1<<n
    masks=[sum(1<<j for j in t) for t in neighbors]
    answer=[0]*(2*n+1)
    full=N-1
    hist={}
    for B in range(N):
        dominated=B; s=B
        while s:
            bit=s & -s; s-=bit
            dominated |= masks[bit.bit_length()-1]
        ones=(full^dominated).bit_count()
        twos=B.bit_count()
        optional=n-twos-ones
        hist[twos,ones]=hist.get((twos,ones),0)+1
        base=2*twos+ones
        for j in range(optional+1):
            answer[base+j]+=comb(optional,j)
    assert sum(hist.values())==N
    return answer,hist

def brute(neighbors):
    n=len(neighbors)
    counts=[0]*(2*n+1)
    for values in product(range(3), repeat=n):
        if all(values[i] or any(values[j]==2 for j in t) for i,t in enumerate(neighbors)):
            counts[sum(values)]+=1
    return counts

# Exhaustive direct 3^10 check on independently specified Petersen graph.
pairs=[(i,j) for i in range(5) for j in range(i+1,5)]
petersen=[tuple(j for j,b in enumerate(pairs) if set(a).isdisjoint(b)) for a in pairs]
assert len(petersen)==10
assert poly(petersen)[0]==brute(petersen)
check_graph(DODECA,2,MAP2)
check_graph(DESARGUES,3,MAP3)
a,ha=poly(DODECA)
b,hb=poly(DESARGUES)
assert a[12]==20 and b[12]==340
assert (sum(a),sum(b))==(742721362,754088530)
assert all(b[i]-a[i]>0 for i in range(12,30))
assert all(a[i]==b[i] for i in list(range(12))+list(range(30,41)))
q=[80,760,3025,6748,9712,9873,7427,4233,1825,580,125,15]
expected=[0]*41
for i,qv in enumerate(q):
    for j in range(7): expected[12+i+j]+=4*qv*comb(6,j)
assert [y-x for x,y in zip(a,b)]==expected
# Independently verify every entry in the saved census certificate.
snapshot=json.loads((Path(__file__).resolve().parent.parent/'data'/'roman_census.json').read_text(encoding='utf-8'))
for key,coef,hist in [('gp_10_2',a,ha),('gp_10_3',b,hb)]:
    assert snapshot[key]['weight_coefficients']==coef
    assert snapshot[key]['support_histogram']==[[hist.get((i,j),0) for j in range(21)] for i in range(21)]
assert snapshot['positive_factor_Q_ascending']==q
print('PASS ALL PACKAGED CENSUS CERTIFICATE ENTRIES')
print('PASS EXPLICIT ISOMORPHISMS AND INDEPENDENT ADJACENCY')
print('PASS DIRECT 3^10 PETERSEN FUNCTION SEARCH')
print('PASS 2^20 SUPPORTS PER GRAPH, ALL 41 COEFFICIENTS, FACTORIZATION')
print('P',a)
print('D',b)
