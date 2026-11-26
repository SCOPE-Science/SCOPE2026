"""Standalone finite checks for the seven-gon diagonal complex and its dihedral quotient.
Requires only Python 3; exhaustive over all faces, flags and 14 polygon isometries.
The homeomorphism theorem also uses established secondary-polytope and
three-manifold theorems, proved separately in RESULT.md, not this finite code.
"""
from itertools import combinations
from collections import Counter

n=7
verts=range(n)
diagonals=[(a,b) for a,b in combinations(verts,2) if b-a not in (1,n-1)]
diag_id={p:i for i,p in enumerate(diagonals)}

def cross(ab,cd):
    a,b=ab;c,d=cd
    return len({a,b,c,d})==4 and ((a<c<b)!=(a<d<b)) and ((c<a<d)!=(c<b<d))

faces=[]
for k in range(1,5):
    for f in combinations(range(len(diagonals)),k):
        if all(not cross(diagonals[i],diagonals[j]) for i,j in combinations(f,2)):
            faces.append(frozenset(f))
assert len(diagonals)==14
assert Counter(map(len,faces))=={1:14,2:56,3:84,4:42}
face_id={face:i for i,face in enumerate(faces)}

def action(s,t):
    p=[]
    for a,b in diagonals:
        p.append(diag_id[tuple(sorted(((s*a+t)%n,(s*b+t)%n)))])
    return [face_id[frozenset(p[j] for j in f)] for f in faces]

actions={(s,t):action(s,t) for s in (1,-1) for t in range(n)}
assert len({tuple(a) for a in actions.values()})==14
for t in range(1,n):
    assert all(actions[(1,t)][i]!=i for i in range(len(faces)))

# All strict chains in the face poset: barycentric simplices of each dimension.
chains={0:[(i,) for i in range(len(faces))]}
for d in range(1,4):
    chains[d]=[ch+(j,) for ch in chains[d-1]
               for j,f in enumerate(faces)
               if faces[ch[-1]]<f]
assert [len(chains[i]) for i in range(4)]==[196,1204,2016,1008]

orbits=[];orbit_id=[]
for d in range(4):
    mp={}; reps=[]
    for chain in chains[d]:
        if chain in mp:continue
        k=len(reps);reps.append(chain)
        for a in actions.values():
            mp[tuple(a[i] for i in chain)]=k
    assert len(mp)==len(chains[d])
    orbits.append(reps);orbit_id.append(mp)
assert [len(x) for x in orbits]==[19,91,144,72]

boundaries=[]
for d in range(1,4):
    cols=[]
    for ch in orbits[d]:
        c=Counter()
        for i in range(d+1):
            c[orbit_id[d-1][ch[:i]+ch[i+1:]]]+=(-1)**i
        cols.append({i:x for i,x in c.items() if x})
    boundaries.append(cols)

for d in (1,2):
    for col in boundaries[d]:
        accum=Counter()
        for i,v in col.items():
            for j,w in boundaries[d-1][i].items():accum[j]+=v*w
        assert not any(accum.values()), ('boundary square',d)

def rank_mod(columns,p):
    pivots={}
    for col in columns:
        v={i:c%p for i,c in col.items() if c%p}
        while v:
            k=min(v)
            if k not in pivots:
                inv=pow(v[k],-1,p)
                pivots[k]={i:c*inv%p for i,c in v.items() if c%p}
                break
            factor=v[k]
            for i,c in pivots[k].items():
                x=(v.get(i,0)-factor*c)%p
                if x:v[i]=x
                else:v.pop(i,None)
    return len(pivots)
for p in (2,3,5,7,11,101,1009):
    assert [rank_mod(b,p) for b in boundaries]==[18,73,71]

# Every reflection-fixed barycentric subcomplex is a 10-vertex 10-edge cycle.
for t in range(n):
    a=actions[(-1,t)]
    fix={i for i in range(len(faces)) if a[i]==i}
    assert len(fix)==10
    edges={(i,j) for i in fix for j in fix if faces[i]<faces[j]}
    degrees=Counter()
    for i,j in edges:degrees[i]+=1;degrees[j]+=1
    assert len(edges)==10 and set(degrees)==fix and set(degrees.values())=={2}
    seen={next(iter(fix))}
    while True:
        more={i for i,j in edges if j in seen}|{j for i,j in edges if i in seen}
        if more<=seen:break
        seen|=more
    assert seen==fix
    assert not any(faces[i]<faces[j]<faces[k] for i in fix for j in fix for k in fix)

print('HEPTAGON_DIHEDRAL_ORBIT_OK; noncrossing faces 196; flag orbits 19,91,144,72; reflection fixed circles 7; modular ranks 18,73,71')
