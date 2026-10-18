#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque
from functools import lru_cache

# The closed tetrahedron Delta^3: nonempty faces are bitmasks on four vertices.
base_cells=list(range(1,16))
base_index={m:i for i,m in enumerate(base_cells)}
primitive=[]
for a in base_cells:
    for b in base_cells:
        if a.bit_count()+1==b.bit_count() and (a&b)==a:
            primitive.append((a,b))
primitive.sort(key=lambda x:(x[0].bit_count(),x[0],x[1]))
assert len(primitive)==28
prim_index={e:i for i,e in enumerate(primitive)}
used=[]
for a,b in primitive:
    used.append((1<<base_index[a])|(1<<base_index[b]))

def acyclic_selected(indices):
    bydim={}
    for i in indices:
        a,b=primitive[i]
        d=a.bit_count()-1
        g=bydim.setdefault(d,{})
        g.setdefault(a,[])
        for v in range(4):
            if (b>>v)&1:
                f=b&~(1<<v)
                if f and f!=a and f.bit_count()==a.bit_count():
                    g[a].append(f)
    for g in bydim.values():
        state={}
        def dfs(x):
            state[x]=1
            for y in g.get(x,[]):
                if state.get(y)==1:
                    return False
                if state.get(y,0)==0 and not dfs(y):
                    return False
            state[x]=2
            return True
        for x in list(g):
            if state.get(x,0)==0 and not dfs(x):
                return False
    return True

faces=[]
def rec(i,used_cells,mask,indices):
    if i==len(primitive):
        if mask:
            faces.append(mask)
        return
    rec(i+1,used_cells,mask,indices)
    if not (used_cells & used[i]):
        ni=indices+[i]
        if acyclic_selected(ni):
            rec(i+1,used_cells|used[i],mask|(1<<i),ni)
rec(0,0,0,[])
face_vector=Counter(m.bit_count()-1 for m in faces)
expected_f={0:28,1:300,2:1544,3:3932,4:4632,5:2128,6:256}
assert dict(face_vector)==expected_f
assert len(faces)==12820

# Deterministic element matching on the face poset of M(Delta^3).
unmatched=set(faces)
pairs=[]
for p in range(28):
    bit=1<<p
    lows=[m for m in unmatched if not (m&bit) and (m|bit) in unmatched]
    for lo in sorted(lows):
        up=lo|bit
        if lo in unmatched and up in unmatched:
            unmatched.remove(lo); unmatched.remove(up); pairs.append((lo,up,p))
critical=Counter(m.bit_count()-1 for m in unmatched)
assert dict(critical)=={0:1,3:2,4:101}
assert len(pairs)==6358

# Verify the matching on every Hasse cover and prove acyclicity by topological sort.
face_index={m:i for i,m in enumerate(faces)}
matched={(lo,up) for lo,up,_ in pairs}
adj=[[] for _ in faces]
indeg=[0]*len(faces)
hasse=0
for up in faces:
    for p in range(28):
        if (up>>p)&1:
            lo=up&~(1<<p)
            if lo==0 or lo not in face_index:
                continue
            hasse+=1
            a,b=(up,lo) if (lo,up) in matched else (lo,up)
            ia,ib=face_index[a],face_index[b]
            adj[ia].append(ib); indeg[ib]+=1
q=deque(i for i,d in enumerate(indeg) if d==0)
seen=0
while q:
    i=q.popleft(); seen+=1
    for j in adj[i]:
        indeg[j]-=1
        if indeg[j]==0: q.append(j)
assert seen==len(faces)

# Exact signed Morse boundary d_4:C_4^Morse -> C_3^Morse.
crit3=sorted(m for m in unmatched if m.bit_count()-1==3)
crit4=sorted(m for m in unmatched if m.bit_count()-1==4)
lower_to_upper={lo:up for lo,up,_ in pairs}
upper_to_lower={up:lo for lo,up,_ in pairs}
crit3set=set(crit3)

def boundary_facets(up):
    inds=[i for i in range(28) if (up>>i)&1]
    return [(up&~(1<<i), -1 if pos%2 else 1) for pos,i in enumerate(inds)]

def incidence(up,lo):
    diff=up^lo
    i=diff.bit_length()-1
    inds=[j for j in range(28) if (up>>j)&1]
    return -1 if inds.index(i)%2 else 1

@lru_cache(None)
def expand3(cell):
    if cell in crit3set:
        return {cell:1}
    if cell not in lower_to_upper:
        assert cell in upper_to_lower
        return {}
    up=lower_to_upper[cell]
    a=incidence(up,cell)
    out={}
    for other,b in boundary_facets(up):
        if other==cell: continue
        coef=-a*b
        for c,v in expand3(other).items():
            out[c]=out.get(c,0)+coef*v
    return {c:v for c,v in out.items() if v}

columns=[]
for c4 in crit4:
    v={}
    for f,s in boundary_facets(c4):
        for c,a in expand3(f).items():
            v[c]=v.get(c,0)+s*a
    columns.append([v.get(r,0) for r in crit3])
assert len(columns)==101 and all(len(c)==2 for c in columns)
assert max(abs(x) for c in columns for x in c)<=1
unit_minor=None
for i in range(101):
    for j in range(i+1,101):
        det=columns[i][0]*columns[j][1]-columns[j][0]*columns[i][1]
        if abs(det)==1:
            unit_minor=(i,j,det)
            break
    if unit_minor: break
assert unit_minor is not None
# The unit 2x2 minor proves Smith invariants (1,1); hence H_4=Z^99 and no H_3.

# Natural S4 action on tetrahedron vertices and hence on primitive gradients.
def perm_mask(mask,p):
    out=0
    for i in range(4):
        if (mask>>i)&1: out |= 1<<p[i]
    return out

def induced_primitive_perm(p):
    return {i:prim_index[(perm_mask(a,p),perm_mask(b,p))] for i,(a,b) in enumerate(primitive)}

def parity(seq):
    inv=0
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            inv += seq[i]>seq[j]
    return -1 if inv%2 else 1

def chain_traces(p):
    pm=induced_primitive_perm(p)
    tr=Counter()
    for f in faces:
        inds=[i for i in range(28) if (f>>i)&1]
        imgs=[pm[i] for i in inds]
        if set(imgs)==set(inds):
            pos={v:k for k,v in enumerate(inds)}
            tr[f.bit_count()-1]+=parity([pos[x] for x in imgs])
    return [tr[d] for d in range(7)]

classes=[
    ('1^4',(0,1,2,3),1),
    ('2,1^2',(1,0,2,3),6),
    ('2^2',(1,0,3,2),3),
    ('3,1',(1,2,0,3),8),
    ('4',(1,2,3,0),6),
]
character=[]
trace_table={}
for name,p,size in classes:
    tr=chain_traces(p)
    trace_table[name]=tr
    lefschetz=sum(((-1)**d)*tr[d] for d in range(7))
    # H_0 is the trivial representation and all reduced homology is H_4=Z^99.
    character.append(lefschetz-1)
assert character==[99,1,-1,0,-1]

# Decompose against the irreducible rational character table of S4.
irreps={
    '(4)':[1,1,1,1,1],
    '(3,1)':[3,1,-1,0,-1],
    '(2,2)':[2,0,2,-1,0],
    '(2,1,1)':[3,-1,-1,0,1],
    '(1,1,1,1)':[1,-1,1,1,-1],
}
sizes=[1,6,3,8,6]
mult={}
for label,ch in irreps.items():
    n=sum(s*a*b for s,a,b in zip(sizes,character,ch))
    assert n%24==0
    mult[label]=n//24
assert mult=={'(4)':4,'(3,1)':13,'(2,2)':8,'(2,1,1)':12,'(1,1,1,1)':4}
assert sum(mult[k]*irreps[k][0] for k in mult)==99

print('TETRA_S4_VERIFY_OK')
print('face_vector', [expected_f[d] for d in range(7)])
print('hasse_covers',hasse)
print('critical_vector',[critical.get(d,0) for d in range(7)])
print('unit_minor',unit_minor)
print('chain_traces',trace_table)
print('H4_character',character)
print('decomposition',mult)
