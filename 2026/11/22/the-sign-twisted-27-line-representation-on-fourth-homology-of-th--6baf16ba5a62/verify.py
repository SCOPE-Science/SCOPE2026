"""Exact finite verification of Weyl action on cubic-surface skew-line homology.

Python 3 standard library only.  No random choices or external packages.
"""
from itertools import combinations
from collections import deque, Counter

# Divisor (a,b_0,...,b_5) represents aH - sum b_i E_i.
lines = []
for i in range(6):
    x=[0]*7; x[i+1]=-1; lines.append(tuple(x))
for i,j in combinations(range(6),2):
    lines.append((1,)+tuple(int(k in (i,j)) for k in range(6)))
for i in range(6):
    lines.append((2,)+tuple(int(k != i) for k in range(6)))
assert len(lines)==len(set(lines))==27

def intersection(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

skew = [[intersection(lines[i],lines[j])==0 for j in range(27)] for i in range(27)]
assert all(sum(skew[i][j] for j in range(27))==16 for i in range(27))
assert sum(skew[i][j] for i in range(27) for j in range(27))//2==216

# Index 0 is the empty face, index d+1 consists of oriented d-simplices.
faces=[[()],[(i,) for i in range(27)]]
for k in range(2,7):
    faces.append([f+(j,) for f in faces[-1] for j in range(f[-1]+1,27)
                  if all(skew[v][j] for v in f)])
assert list(map(len,faces))==[1,27,216,720,1080,648,72]
assert sum(map(len, faces))==2764

def augmented_boundary_rank_mod_two(i):
    rows={f:j for j,f in enumerate(faces[i-1])}
    basis={}
    for simplex in faces[i]:
        v=0
        for j in range(i):
            v ^= 1<<rows[simplex[:j]+simplex[j+1:]]
        while v:
            pivot=v.bit_length()-1
            if pivot not in basis:
                basis[pivot]=v
                break
            v ^= basis[pivot]
    return len(basis)

ranks=[augmented_boundary_rank_mod_two(i) for i in range(1,7)]
assert ranks==[1,26,190,530,550,72]
# The mod-2 ranks saturate dim C_i in every degree other than degree 4,
# and all ranks over Q are at least the corresponding mod-2 ranks.
# This forces all Q-ranks to be exactly the six displayed ranks.
assert ranks[0]+ranks[1]==27
assert ranks[1]+ranks[2]==216
assert ranks[2]+ranks[3]==720
assert ranks[3]+ranks[4]==1080
assert ranks[5]==72
assert 648-ranks[4]-ranks[5]==26

index={line:i for i,line in enumerate(lines)}
identity=tuple(range(27))
def permute_coordinates(i,j):
    result=[]
    for line in lines:
        x=list(line)
        x[i+1],x[j+1]=x[j+1],x[i+1]
        result.append(index[tuple(x)])
    return tuple(result)

def reflect(root):
    assert intersection(root,root)==-2
    return tuple(index[tuple(x+intersection(line,root)*r
                             for x,r in zip(line,root))] for line in lines)

def compose(a,b):
    return tuple(a[b[i]] for i in range(27))

generators=[permute_coordinates(i,i+1) for i in range(5)]
generators.append(reflect((1,1,1,1,0,0,0)))
assert all(compose(s,s)==identity for s in generators)
for s in generators:
    for i in range(27):
        for j in range(27):
            assert skew[i][j]==skew[s[i]][s[j]]

# The parity of a word in the six simple root reflections equals its
# determinant on the rank-six root representation. Check consistency.
det_parity={identity:0}
queue=deque([identity])
while queue:
    g=queue.popleft()
    for s in generators:
        h=compose(g,s)
        if h not in det_parity:
            det_parity[h]=det_parity[g]^1
            queue.append(h)
        else:
            assert det_parity[h]==(det_parity[g]^1)
assert len(det_parity)==51840

def permutation_sign(v):
    return -1 if sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))%2 else 1

def chain_traces(g):
    traces=[]
    for layer in faces[1:]:
        result=0
        for simplex in layer:
            im=[g[i] for i in simplex]
            if set(im)==set(simplex):
                positions={x:j for j,x in enumerate(simplex)}
                result+=permutation_sign([positions[x] for x in im])
        traces.append(result)
    return traces

def cycle_profile(g):
    seen=set(); c=[]
    for i in range(27):
        if i in seen: continue
        j=i; n=0
        while j not in seen:
            seen.add(j); n+=1; j=g[j]
        c.append(n)
    return tuple(sorted(Counter(c).items()))

# Exhaust the conjugacy classes through conjugation by generating reflections.
remaining=set(det_parity)
rows=[]
while remaining:
    rep=next(iter(remaining))
    seen={rep}; queue=deque([rep])
    while queue:
        g=queue.popleft()
        for s in generators:
            h=compose(s,compose(g,s))
            if h not in seen:
                seen.add(h);queue.append(h)
    assert seen<=remaining
    remaining.difference_update(seen)
    trace=chain_traces(rep)
    # Reduced Lefschetz number: the empty augmented face contributes -1.
    top_trace=-1+sum((-1)**d * t for d,t in enumerate(trace))
    fix=sum(i==rep[i] for i in range(27))
    target=(-1 if det_parity[rep] else 1)*(fix-1)
    assert top_trace==target, (len(seen),fix,top_trace,target)
    rows.append((len(seen),det_parity[rep],fix,cycle_profile(rep),top_trace))
assert len(rows)==25
assert sum(x[0] for x in rows)==51840
assert (1,0,27,((1,27),),26) in rows
assert (36,1,15,((1,15),(2,6)),-14) in rows
assert (240,0,9,((1,9),(3,6)),8) in rows

for size, parity, fixed, cycles, top in sorted(rows, reverse=True):
    cyc=''.join('%s^%s_'%(length,multiplicity) for length,multiplicity in cycles).rstrip('_')
    print('class_size=%d det=%+d fixed_lines=%d line_cycles=%s homology_trace=%d'%
          (size,-1 if parity else 1,fixed,cyc,top))
print('SCHLAFLI_WEYL_HOMOLOGY_CHARACTER_VERIFIED_OK')
