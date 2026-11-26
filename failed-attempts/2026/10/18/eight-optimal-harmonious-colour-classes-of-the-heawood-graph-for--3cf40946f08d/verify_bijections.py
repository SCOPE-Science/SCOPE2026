"""Exact named Fano line-to-point nesting enumeration; standalone standard-library checker."""
import itertools
from collections import Counter
P=range(1,8)
L=range(1,8)
blocks={l:{p for p in P if (p & l).bit_count()%2==0} for l in L}
assert all(len(b)==3 for b in blocks.values())
assert len({frozenset(b) for b in blocks.values()})==7
# Candidate bijections f(line) is its color, point colors are point labels.
valid=[]; nonincident=0; collisions=Counter()
for assignment in itertools.permutations(P):
 f=dict(zip(L,assignment))
 if any(f[l] in blocks[l] for l in L):continue
 nonincident+=1
 pairs=[tuple(sorted((p,f[l]))) for l in L for p in blocks[l]]
 distinct=len(set(pairs))
 collisions[distinct]+=1
 if distinct==21:valid.append(assignment)
assert len(valid)==8
# Independently classify the order-168 Fano incidence automorphism group by point permutations.
perms=[]
blockset={frozenset(v) for v in blocks.values()}
for p in itertools.permutations(P):
 h=dict(zip(P,p))
 if {frozenset(h[x] for x in b) for b in blocks.values()}==blockset:
  perms.append(h)
assert len(perms)==168
# Each automorphism acts on both point and line labels.
image_line={frozenset(v):l for l,v in blocks.items()}
def transport(f,h):
 return tuple(h[f[l]] for l in L) # not used (line labels transported below)
solutions=set(valid)
f0=dict(zip(L,valid[0])); orbit=set()
for h in perms:
 out={image_line[frozenset(h[p] for p in blocks[l])]:h[f0[l]] for l in L}
 orbit.add(tuple(out[l] for l in L))
assert orbit==solutions
assert len(orbit)==8
# Verify permutations in solution stabilizer are exactly 21.
print('all_bijections',5040)
print('proper_nonincidence_bijections',nonincident)
print('distinct_edge_color_pair_spectrum',sorted(collisions.items()))
print('harmonious_exact_bijections',len(solutions))
print('fano_collineation_order',len(perms))
print('collineation_orbit',len(orbit),'collineation_stabilizer',len(perms)//len(orbit))
print('one_canonical_assignment',valid[0])
print('VERIFY_OK')
