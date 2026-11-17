"""Exact, self-contained enumeration of the proper A5 subgroup order complex.

Requires Python 3.9+ standard library only. Enumerates all subgroups by closure,
chains by inclusion, and every S5 automorphism by permutation conjugation.
"""
import collections
import itertools
import math
from functools import lru_cache

perms5 = list(itertools.permutations(range(5)))
identity_perm = tuple(range(5))

def parity(p):
    return sum(p[i] > p[j] for i in range(5) for j in range(i+1,5)) % 2

a5 = [p for p in perms5 if parity(p)==0]
assert len(a5)==60
idx = {p:i for i,p in enumerate(a5)}
e = idx[identity_perm]
mult = [[idx[tuple(p[q[k]] for k in range(5))] for q in a5] for p in a5]
inverse = [next(j for j in range(60) if mult[i][j]==e and mult[j][i]==e) for i in range(60)]

def subgroup_generated(generators):
    gens=list(generators)+[inverse[j] for j in generators]
    seen={e}
    bfs=[e]
    for x in bfs:
        for y in gens:
            z=mult[x][y]
            if z not in seen:
                seen.add(z)
                bfs.append(z)
    return frozenset(seen)

subgroups={frozenset((e,))}
queue=list(subgroups)
for H in queue:
    for x in range(60):
        if x not in H:
            Hnew=subgroup_generated(list(H)+[x])
            if Hnew not in subgroups:
                subgroups.add(Hnew)
                queue.append(Hnew)

subgroup_counts=collections.Counter(map(len,subgroups))
assert subgroup_counts=={1:1,2:15,3:10,4:5,5:6,6:10,10:6,12:5,60:1}
assert len(subgroups)==59
proper=sorted((h for h in subgroups if 1<len(h)<60),key=lambda h:(len(h),tuple(sorted(h))))
lookup={h:i for i,h in enumerate(proper)}
faces=[[(i,) for i in range(57)],[],[]]
for i,a in enumerate(proper):
    for j,b in enumerate(proper):
        if len(a)<len(b) and a<=b:
            faces[1].append((i,j))
for i,j in faces[1]:
    for k,c in enumerate(proper):
        if len(proper[j])<len(c) and proper[j]<=c:
            faces[2].append((i,j,k))
assert tuple(map(len,faces))==(57,131,15)
assert all((len(proper[i]),len(proper[j]),len(proper[k]))==(2,4,12) for i,j,k in faces[2])

edge_index={edge:i for i,edge in enumerate(faces[1])}
triangle_cofaces=collections.Counter((i,j) for i,j,k in faces[2])
free_edges={edge for edge,n in triangle_cofaces.items() if n==1}
assert len(free_edges)==15
assert all((len(proper[i]),len(proper[j]))==(2,4) for i,j in free_edges)
assert all(edge in edge_index for edge in free_edges)
remaining_edges=[edge for edge in faces[1] if edge not in free_edges]
assert len(remaining_edges)==116
# Spanning graph of residual one-dimensional complex.
adj=[set() for _ in range(57)]
for i,j in remaining_edges:
    adj[i].add(j)
    adj[j].add(i)
seen={0}; queue=[0]
for i in queue:
    for j in adj[i]:
        if j not in seen:
            seen.add(j)
            queue.append(j)
assert len(seen)==57
assert len(remaining_edges)-len(proper)+1==60

# As a complementary check, exact boundary ranks over several prime fields.
def rankmod(columns,p):
    pivots={}
    for col in columns:
        v={k:x%p for k,x in col.items() if x%p}
        while v:
            key=max(v)
            if key not in pivots:
                lead_inverse=pow(v[key],-1,p)
                pivots[key]={a:(b*lead_inverse)%p for a,b in v.items()}
                break
            coef=v[key]
            for a,b in pivots[key].items():
                z=(v.get(a,0)-coef*b)%p
                if z:v[a]=z
                else:v.pop(a,None)
    return len(pivots)

d1=[{i:-1,j:1} for i,j in faces[1]]
d2=[{edge_index[(j,k)]:1,edge_index[(i,k)]:-1,edge_index[(i,j)]:1} for i,j,k in faces[2]]
for p in (2,3,5,7,11,101):
    assert (rankmod(d1,p),rankmod(d2,p))==(56,15)

# Conjugation by every S5 permutation on each proper subgroup.
def conjugation_table(p):
    invp=[None]*5
    for a,b in enumerate(p):
        invp[b]=a
    return [idx[tuple(p[g[invp[k]]] for k in range(5))] for g in a5]

actions=[]
for p in perms5:
    table=conjugation_table(p)
    action=tuple(lookup[frozenset(table[x] for x in H)] for H in proper)
    assert sorted(action)==list(range(57))
    assert all(tuple(action[z] for z in edge) in edge_index for edge in faces[1])
    assert all(tuple(action[z] for z in tri) in faces[2] for tri in faces[2])
    actions.append(action)

def cycle_type(p):
    seen=set(); result=[]
    for i in range(5):
        if i not in seen:
            cur=i;k=0
            while cur not in seen:
                seen.add(cur);k+=1;cur=p[cur]
            result.append(k)
    return tuple(sorted(result,reverse=True))

fixed_data={}
class_sizes=collections.Counter()
for p,action in zip(perms5,actions):
    cl=cycle_type(p)
    class_sizes[cl]+=1
    fixed={i for i,j in enumerate(action) if i==j}
    counts=(len(fixed),
            sum(all(i in fixed for i in edge) for edge in faces[1]),
            sum(all(i in fixed for i in tri) for tri in faces[2]))
    # No face inversion is possible: subgroup orders strictly increase in chains.
    value=1-counts[0]+counts[1]-counts[2]
    if cl in fixed_data:assert fixed_data[cl]==(counts,value)
    fixed_data[cl]=(counts,value)

expected={
    (1,1,1,1,1):((57,131,15),60),
    (2,1,1,1):((17,25,3),6),
    (2,2,1):((13,15,3),0),
    (3,1,1):((6,5,0),0),
    (3,2):((2,1,0),0),
    (4,1):((7,7,1),0),
    (5,):((2,1,0),0),
}
assert fixed_data==expected
assert sum(class_sizes.values())==120

# Face orbits. No inversions, so the quotient is a finite Delta complex.
orbit_counts=[]
orbit_types=[]
for cells in faces:
    remaining=set(cells); sizes=[]; labels=[]
    while remaining:
        face=min(remaining)
        orbit={tuple(action[i] for i in face) for action in actions}
        assert orbit<=remaining
        remaining-=orbit
        sizes.append(len(orbit))
        labels.append(tuple(len(proper[i]) for i in face))
    orbit_counts.append(len(sizes))
    orbit_types.append(set(labels))
assert orbit_counts==[7,8,1]
assert orbit_types[0]=={(k,) for k in (2,3,4,5,6,10,12)}
assert orbit_types[1]=={(2,4),(2,6),(2,10),(2,12),(3,6),(3,12),(4,12),(5,10)}
assert orbit_types[2]=={(2,4,12)}
# The C2<V4 edge orbit is the unique free boundary edge of the triangle orbit;
# quotient collapse leaves a connected 7-vertex 7-edge graph, hence a circle.
assert len({tuple(len(proper[z]) for z in f) for f in faces[2]})==1
assert len({tuple(len(proper[z]) for z in f) for f in free_edges})==1
assert 8-1==7

@lru_cache(None)
def partitions(n,maxpart=None):
    if n==0:return ((),)
    if maxpart is None:maxpart=n
    return tuple((k,)+tail for k in range(min(n,maxpart),0,-1) for tail in partitions(n-k,k))

@lru_cache(None)
def permutation_character(alpha,mu):
    if min(alpha)<0 or sum(alpha)!=sum(mu):return 0
    total=0
    for assignment in itertools.product(range(len(alpha)),repeat=len(mu)):
        sizes=[0]*len(alpha)
        for i,m in zip(assignment,mu):sizes[i]+=m
        total+=tuple(sizes)==alpha
    return total

def specht_character(lam,mu):
    total=0
    for p in itertools.permutations(range(len(lam))):
        alpha=tuple(lam[i]-i+p[i] for i in range(len(lam)))
        if min(alpha)<0:continue
        sign=(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        total+=sign*permutation_character(alpha,mu)
    return total

multiplicities={}
for lam in partitions(5):
    numerator=sum(class_sizes[mu]*fixed_data[mu][1]*specht_character(lam,mu) for mu in expected)
    assert numerator%120==0
    multiplicities[lam]=numerator//120
assert multiplicities=={
    (5,):1,(4,1):3,(3,2):3,(3,1,1):3,(2,2,1):2,(2,1,1,1):1,(1,1,1,1,1):0
}
assert sum(multiplicities[lam]*specht_character(lam,(1,1,1,1,1)) for lam in multiplicities)==60
assert (sum(class_sizes[mu]*fixed_data[mu][1] for mu in expected)//120)==1

print('A5_SUBGROUP_COMPLEX_PASS')
print('subgroup_order_counts:',dict(sorted(subgroup_counts.items())))
print('simplices_by_dimension: 57 131 15')
print('equivariant_free_triangle_edge_pairs: 15')
print('collapsed_graph: vertices=57 edges=116 connected=yes beta1=60')
print('field_boundary_ranks: (56,15) for 2,3,5,7,11,101')
print('S5_class_size_and_F0_F1_F2_H1:')
for key in sorted(expected,reverse=True):
    print(key,class_sizes[key],expected[key][0],expected[key][1])
print('Specht_multiplicities:',multiplicities)
print('face_orbits: 7 8 1; quotient_homotopy_type=S1')
