#!/usr/bin/env python3
"""Independent mod-two chain ranks for Morse matchings of the tetrahedron."""
from collections import Counter
from itertools import combinations
F=range(1,16)
E=[(a,b) for a in F for b in F if a&b==a and b.bit_count()==a.bit_count()+1]
face_pos={f:i for i,f in enumerate(F)}
end=[(1<<face_pos[a])|(1<<face_pos[b]) for a,b in E]

def valid(indices):
    used=0
    for i in indices:
        if used&end[i]:return False
        used|=end[i]
    matched=set(indices);out=[[] for f in F];indeg=[0]*15
    for i,(a,b) in enumerate(E):
        u,v=(b,a) if i in matched else (a,b)
        x,y=face_pos[u],face_pos[v]
        out[x].append(y);indeg[y]+=1
    ready=[i for i in range(15) if indeg[i]==0];k=0
    while ready:
        u=ready.pop();k+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:ready.append(v)
    return k==15

faces={k:[] for k in range(7)}
def rec(j,used,ss):
    if j==len(E):
        if ss and valid(ss):faces[len(ss)-1].append(tuple(ss))
        return
    rec(j+1,used,ss)
    if used&end[j]==0:
        rec(j+1,used|end[j],ss+(j,))
rec(0,0,())
print('f-vector',tuple(len(faces[d]) for d in range(7)))
ranks={0:0}
for d in range(1,7):
    low={s:i for i,s in enumerate(faces[d-1])}
    basis={}
    for s in faces[d]:
        col=0
        for sub in combinations(s,len(s)-1):col ^= 1<<low[sub]
        while col:
            k=col.bit_length()-1
            if k in basis:col ^= basis[k]
            else:
                basis[k]=col;break
    ranks[d]=len(basis)
    print('boundary rank',d,ranks[d])
betti={d:len(faces[d])-ranks[d]-ranks.get(d+1,0) for d in range(7)}
# zero chain boundary rank 0=1 for unreduced H_0, no need for reduced others
betti0=betti[0]
print('betti_ordinary',betti)
assert betti=={0:1,1:0,2:0,3:0,4:99,5:0,6:0}
print('MOD2_BOUNDARY_CHECKS_OK')
