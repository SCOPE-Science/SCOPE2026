import pickle, numpy as np, collections
with open("mats.pkl","rb") as f:
    D=pickle.load(f)
cells=D["cells"]; edges=D["edges"]
# Build face incidence (unsigned) for k=1..5 using boundary formula
V=11
def faces_of(k, cell):
    es,vs=cell; vs=list(vs)
    out=[]
    for i,e in enumerate(es):
        u,v=edges[e]
        rest=tuple(x for ii,x in enumerate(es) if ii!=i)
        for w in (u,v):
            lst=tuple(sorted(vs+[w]))
            out.append((rest,lst))
    return out

# map cells to ids per dim
idx=[{c:i for i,c in enumerate(cells[k])} for k in range(6)]
# coface counts: for collapse we need free faces: (k-1)-cell with exactly one coface k-cell among REMAINING cells.
# Greedy: process dimensions top-down (collapse k-cells with free (k-1)-faces first), standard.
remaining=[set(range(len(cells[k]))) for k in range(6)]
# precompute faces per cell (as ids)
faces={}
for k in range(1,6):
    fl=[]
    for j,cell in enumerate(cells[k]):
        fl.append([idx[k-1][f] for f in faces_of(k,cell)])
    faces[k]=fl

import time
t0=time.time()
pairs=[]
changed=True
# order: iterate k from 5 down to 1 repeatedly until no change
niter=0
while changed:
    changed=False; niter+=1
    for k in range(5,0,-1):
        # count cofaces among remaining
        cof=collections.Counter()
        for j in remaining[k]:
            for r in faces[k][j]:
                if r in remaining[k-1]:
                    cof[r]+=1
        # free faces: cof==1; match each free face with its unique coface (avoid double-matching coface)
        # build map face -> coface
        # for determinism, process faces sorted
        used_cof=set()
        # invert: for each coface, list faces... simpler: for each face with cof 1, find its coface
        # build coface lists
        for r in sorted(cof):
            if cof[r]!=1: continue
            # find the coface
            for j in remaining[k]:
                if j in used_cof: continue
                if r in faces[k][j]:
                    # pair (r,j)
                    remaining[k-1].discard(r); remaining[k].discard(j)
                    pairs.append((k-1,r,k,j))
                    used_cof.add(j)
                    changed=True
                    break
    print("iter",niter,"remaining",[len(s) for s in remaining],"pairs",len(pairs),flush=True)
    if niter>50: break
print("done", time.time()-t0)
print([len(s) for s in remaining])
with open("collapse_state.pkl","wb") as f:
    pickle.dump({"remaining":remaining,"pairs":pairs},f)
