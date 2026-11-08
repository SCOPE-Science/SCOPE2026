#!/usr/bin/env python3
"""Standalone finite certificate checker for GC-balanced deletion codes."""
import itertools, json, sys, collections
from pathlib import Path
P=Path(__file__).resolve().parent
D=json.loads((P/'certificate.json').read_text(encoding='utf-8'))
A='ACGT'; C={'A':'T','T':'A','C':'G','G':'C'}
def rc(w):return ''.join(C[x] for x in w[::-1])
def deletions(w):return {w[:p]+w[p+1:] for p in range(len(w))}
words=[''.join(x) for x in itertools.product(A,repeat=4) if sum(y in 'GC' for y in x)==2]
assert len(words)==96
all_orbits=sorted({tuple(sorted({w,rc(w)})) for w in words})
assert len(all_orbits)==52 and sum(len(o)==1 for o in all_orbits)==8
orbits=[o for o in all_orbits if len(o)==2 and not (deletions(o[0])&deletions(o[1]))]
assert len(orbits)==44
assert [list(o) for o in orbits]==D['orbits']
shadow=[set().union(*(deletions(w) for w in o)) for o in orbits]
N=len(orbits); conflicts=[[False]*N for _ in range(N)]
for i in range(N):
 for j in range(i+1,N):
  conflicts[i][j]=conflicts[j][i]=bool(shadow[i]&shadow[j])
assert sum(conflicts[i][j] for i in range(N) for j in range(i+1,N))==344
cliques=D['upper_certificate_cliques']
assert len(cliques)==14
multiplicity=[0]*N
for clique in cliques:
 assert clique==sorted(set(clique)) and len(clique)>=2
 for i in clique:
  assert 0<=i<N
  multiplicity[i]+=1
 for i,j in itertools.combinations(clique,2):assert conflicts[i][j]
assert min(multiplicity)>=2
# In each conflict clique, a valid code can use at most one orbit;
# summing gives 2*|selected| <= sum_j |selected intersect clique_j| <=14.
assert collections.Counter(multiplicity)=={2:36,3:8}
witness=D['witness_orbit_indices'];assert len(witness)==7
assert all(not conflicts[i][j] for i,j in itertools.combinations(witness,2))
assert sum(len(orbits[i]) for i in witness)==14
# Exhaustive increasing-index recursion: every seven-set appears exactly once.
solutions=[]
def search(partial,candidates):
 left=7-len(partial)
 if left==0:
  solutions.append(tuple(partial));return
 if len(candidates)<left:return
 for j,i in enumerate(candidates):
  rest=[k for k in candidates[j+1:] if not conflicts[i][k]]
  if len(rest)>=left-1:search(partial+[i],rest)
search([],list(range(N)))
assert len(solutions)==20
assert [list(s) for s in sorted(solutions)]==D['all_maximal_seven_orbit_codes']
# Alphabet permutations commuting with complement and preserving GC balance,
# with optional word reversal, generate the natural symmetry group of size 16.
perms=[]
for p in itertools.permutations(A):
 m=dict(zip(A,p))
 if all(m[C[x]]==C[m[x]] for x in A) and {m['A'],m['T']} in ({'A','T'},{'C','G'}):perms.append(m)
assert len(perms)==8
idx={o:i for i,o in enumerate(orbits)}
def transform(o,p,r):return tuple(sorted(''.join(p[x] for x in (w[::-1] if r else w)) for w in o))
unclassified=set(solutions);classes=[]
while unclassified:
 z=min(unclassified)
 orbit={tuple(sorted(idx[transform(orbits[i],p,r)] for i in z)) for p in perms for r in [False,True]}
 assert orbit<=unclassified
 classes.append(orbit);unclassified-=orbit
assert sorted(map(len,classes))==[4,4,4,8]
print('CERTIFICATE_OK words=96 reverse_complement_orbits=52 admissible_pairs=44 conflict_edges=344')
print('UPPER_BOUND_OK fourteen_conflict_cliques_half_weight total_weight=7')
print('ATTAINMENT_OK fourteen_codewords')
print('CENSUS_OK exactly_20_labeled_optima four_symmetry_classes=4,4,4,8')
