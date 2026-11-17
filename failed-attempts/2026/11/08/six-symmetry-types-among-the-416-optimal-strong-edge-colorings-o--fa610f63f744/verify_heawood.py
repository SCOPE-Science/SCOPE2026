#!/usr/bin/env python3
"""Exact-cover enumeration and full projective-duality orbit check.
All graph objects and automorphisms are constructed explicitly.
"""
from itertools import combinations, product
from collections import Counter
import json, hashlib

P = tuple(range(1,8))
L = sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(P,2)})
assert len(L)==7
Lidx = {line:i for i,line in enumerate(L)}
E = [(p,j) for j,line in enumerate(L) for p in line]
lookup = {edge:i for i,edge in enumerate(E)}
assert len(E)==21

def independent(e,f):
    p,j = E[e]; q,k = E[f]
    return p!=q and j!=k and p not in L[k] and q not in L[j]

# All induced matching candidates. A direct check proves there are no size-four ones.
M = [sum(1<<i for i in c) for c in combinations(range(21),3)
     if all(independent(*pair) for pair in combinations(c,2))]
assert len(M)==84
assert not any(all(independent(*pair) for pair in combinations(c,2))
               for c in combinations(range(21),4))
by_edge = [[j for j,m in enumerate(M) if (m>>i)&1] for i in range(21)]
assert [len(s) for s in by_edge] == [12]*21
full = (1<<21)-1
found=set()
nodes=0

def solve(rem,chosen):
    global nodes
    nodes+=1
    if not rem:
        found.add(tuple(sorted(chosen)))
        return
    choices = None
    for e in range(21):
        if rem&(1<<e):
            avail = [j for j in by_edge[e] if M[j]&rem==M[j]]
            if not avail: return
            if choices is None or len(avail)<len(choices): choices=avail
    for j in choices: solve(rem^M[j], chosen+(j,))
solve(full,())
assert len(found)==416

# All 168 invertible binary-linear maps on F_2^3 and their 168 dualities.
def linear(a,b,c):
    return {p:((a if p&1 else 0)^(b if p&2 else 0)^(c if p&4 else 0)) for p in P}
def dot(a,b): return (a&b).bit_count()%2
normal = {j:next(p for p in P if all(dot(p,q)==0 for q in line))
          for j,line in enumerate(L)}
line_for_normal = {p:j for j,p in normal.items()}
autos=[]
for a,b,c in product(P,repeat=3):
    f=linear(a,b,c)
    if len(set(f.values()))!=7: continue
    line_perm={j:Lidx[tuple(sorted(f[p] for p in line))] for j,line in enumerate(L)}
    keep=tuple(lookup[(f[p],line_perm[j])] for p,j in E)
    swap=tuple(lookup[(normal[line_perm[j]],line_for_normal[f[p]])] for p,j in E)
    autos.extend((keep,swap))
assert len(set(autos))==336
Midx={m:i for i,m in enumerate(M)}
trans=[]
for auto in autos:
    assert len(set(auto))==21
    assert all(independent(i,j)==independent(auto[i],auto[j]) for i,j in combinations(range(21),2))
    trans.append(tuple(Midx[sum(1<<auto[i] for i in range(21) if m>>i&1)] for m in M))
seen=set(); orbits=[]
for s in sorted(found):
    if s in seen: continue
    orbit={tuple(sorted(t[j] for j in s)) for t in trans}
    assert orbit<=found
    orbits.append((len(orbit), min(orbit)))
    seen.update(orbit)
assert len(seen)==416
assert Counter(z for z,_ in orbits)==Counter({112:3,56:1,16:1,8:1})
# An independent direct Burnside count from fixed solutions also checks the orbit calculation.
fix=[sum(tuple(sorted(t[j] for j in s))==s for s in found) for t in trans]
assert sum(fix)//336 == 6 and sum(fix)%336==0

out={
    'graph':'Heawood incidence graph of nonzero F_2^3 and its 2-spaces',
    'points':list(P), 'lines':[list(x) for x in L], 'incidence_edges':E,
    'induced_triples':len(M), 'induced_triples_at_each_edge':[len(x) for x in by_edge],
    'four_edge_induced_matchings':0, 'exact_cover_search_nodes':nodes,
    'unlabeled_color_partitions':len(found), 'full_automorphisms':len(autos),
    'orbit_sizes':sorted(z for z,_ in orbits),
    'orbit_representatives':[
        [[E[i] for i in range(21) if M[j]>>i&1] for j in rep]
        for _,rep in sorted(orbits)],
    'burnside_fixed_sum':sum(fix),
    'color_partition_certificate_sha256':hashlib.sha256(
      ('\n'.join(','.join(str(M[j]) for j in s) for s in sorted(found))+'\n').encode()).hexdigest()
}
print(json.dumps(out,indent=2))
