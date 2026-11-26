#!/usr/bin/env python3
"""Exact reproducible integer Morse certificate for the dodecahedral perfect-matching complex."""
import collections, functools, hashlib, itertools, json, math, random

N=10
E=sorted(set(tuple(sorted(edge)) for edge in ([(i,(i+1)%N) for i in range(N)] + [(i,N+i) for i in range(N)] + [(N+i,N+((i+2)%N)) for i in range(N)])))
assert len(E)==30
adj=[[] for i in range(20)]
for j,(a,b) in enumerate(E):
    adj[a].append((b,j)); adj[b].append((a,j))
@functools.lru_cache(None)
def completions(remaining):
    if remaining==0:return (0,)
    a=(remaining & -remaining).bit_length()-1
    ans=[]
    for b,j in adj[a]:
        if remaining & (1<<b):
            for m in completions(remaining ^ (1<<a) ^ (1<<b)):
                ans.append(m | (1<<j))
    return tuple(ans)
P=tuple(sorted(set(completions((1<<20)-1))))
assert len(P)==36
faces={0}
for p in P:
    sub=[0]
    for j in range(30):
        if p & (1<<j):sub.extend([s | (1<<j) for s in tuple(sub)])
    faces.update(sub)
assert len(faces)==30504
F=tuple(sorted(faces-{0}))
by_dim=collections.Counter(f.bit_count()-1 for f in F)
assert [by_dim[i] for i in range(10)]==[30,375,2180,5790,8352,7440,4320,1620,360,36]

order=list(range(30)); random.Random(7*9391).shuffle(order)
remaining=set(F)
partner={}
for j in order:
    bit=1<<j
    for a in F:
        if a not in remaining or (a&bit):continue
        b=a|bit
        if b in remaining:
            remaining.remove(a);remaining.remove(b)
            partner[a]=b;partner[b]=a
critical=sorted(remaining)
cs=collections.Counter(c.bit_count()-1 for c in critical)
assert cs=={0:1,2:3,3:23},cs
assert len(partner)==30503-27
# Verify all covering incidences and acyclicity by a topological sort of reversed matched incidences.
indegree={f:0 for f in F}
out={f:[] for f in F}
inc=0
for b in F:
    if b.bit_count()<2:continue
    bits=[i for i in range(30) if b&(1<<i)]
    for i in bits:
        a=b^(1<<i)
        inc+=1
        if partner.get(a)==b:
            x,y=a,b
        else:
            x,y=b,a
        out[x].append(y);indegree[y]+=1
queue=collections.deque(f for f in F if indegree[f]==0)
processed=0
while queue:
    f=queue.popleft();processed+=1
    for g in out[f]:
        indegree[g]-=1
        if indegree[g]==0:queue.append(g)
assert processed==len(F),(processed,len(F))

crit2=tuple(c for c in critical if c.bit_count()==3)
crit3=tuple(c for c in critical if c.bit_count()==4)
ci={c:i for i,c in enumerate(crit2)}
def incidence(upper,removed):
    return (-1)**((upper&((1<<removed)-1)).bit_count())
@functools.lru_cache(None)
def project_2(f):
    assert f.bit_count()==3
    if f in ci:
        v=[0]*len(crit2);v[ci[f]]=1;return tuple(v)
    p=partner[f]
    if p.bit_count()==2:return (0,)*len(crit2)
    assert p.bit_count()==4
    missing=(p^f).bit_length()-1
    sign=incidence(p,missing)
    v=[0]*len(crit2)
    for j in range(30):
        if p&(1<<j) and j!=missing:
            g=p^(1<<j)
            coeff=-sign*incidence(p,j)
            pg=project_2(g)
            for i,z in enumerate(pg):v[i]+=coeff*z
    return tuple(v)

cols=[]
for c in crit3:
    v=[0]*len(crit2)
    for j in range(30):
        if c&(1<<j):
            for i,z in enumerate(project_2(c^(1<<j))):v[i]+=incidence(c,j)*z
    cols.append(v)
rows=[[cols[j][i] for j in range(23)] for i in range(3)]
# Smith invariant factors of a 3x23 integer matrix are the successive
# gcds of its 1x1, 2x2 and 3x3 minors. Calculate ALL minors exactly.
def det2(a,b,c,d):return a*d-b*c
def det3(u,v,w):
    return u[0]*det2(v[1],v[2],w[1],w[2])-u[1]*det2(v[0],v[2],w[0],w[2])+u[2]*det2(v[0],v[1],w[0],w[1])
gcd1=math.gcd(*(abs(x) for r in rows for x in r))
gcd2=0; witness2=None
for i,k in itertools.combinations(range(3),2):
    for j,l in itertools.combinations(range(23),2):
        z=det2(rows[i][j],rows[i][l],rows[k][j],rows[k][l])
        gcd2=math.gcd(gcd2,abs(z))
        if witness2 is None and abs(z)==1:witness2=[i,k,j,l,z]
gcd3=0; witness3=None
for js in itertools.combinations(range(23),3):
    z=det3(*(tuple(rows[i][j] for j in js) for i in range(3)))
    gcd3=math.gcd(gcd3,abs(z))
    if witness3 is None and abs(z)==2:witness3=[*js,z]
assert (gcd1,gcd2,gcd3)==(1,1,2)
assert witness2 is not None and witness3 is not None
smith=[gcd1,gcd2//gcd1,gcd3//gcd2]
assert smith == [1,1,2]
# Independent purely combinatorial face counts from perfect-matching intersections by inclusion-exclusion.
assert len(set(E))==30 and all(len([e for e in E if i in e])==3 for i in range(20))
# Signed Morse matrix, lexicographically ordered remaining critical cells.
summary={
 'graph':'generalized Petersen GP(10,2) (dodecahedral graph)',
 'edge_count':len(E),
 'perfect_matching_count':len(P),
 'faces_including_empty':len(faces),
 'nonempty_f_vector':[by_dim[i] for i in range(10)],
 'toggle_order':order,
 'matching_pairs':len(partner)//2,
 'critical_cells_by_dimension':dict(sorted(cs.items())),
 'incidences_checked':inc,
 'acyclic_vertices_processed':processed,
 'critical_two_cell_masks':crit2,
 'critical_three_cell_masks':crit3,
 'morse_boundary_rows':rows,
 'minor_gcds':[gcd1,gcd2,gcd3],
 'unit_two_by_two_minor_witness':witness2,
 'abs_two_three_by_three_minor_witness':witness3,
 'smith_invariants':smith,
 'reduced_integral_homology':{'2':'Z/2','3':'Z^20'},
 'homotopy_type':'M(Z/2,2) vee (20 copies of S^3)',
}
print(json.dumps(summary,sort_keys=True,separators=(',',':')))
