import pickle, itertools, numpy as np, collections, time, random
# Build sparse ordered d2 (remaining): rows=ord1 (56040), cols=ord2 (31920), 4 nnz/col.
# First enumerate ord2 lifts, index ord1.
with open("mats.pkl","rb") as f:
    D=pickle.load(f)
cells=D["cells"]; edges=D["edges"]
V=11; E=len(edges); n=5
with open("collapse_state.pkl","rb") as f:
    S=pickle.load(f)
remaining=S["remaining"]
rem1=set(remaining[1]); rem2=set(remaining[2]); rem0=set(remaining[0])

# index remaining unordered
# Build ord1 index
t0=time.time()
ord1=[]
for j in rem1:
    es,vs=cells[1][j]
    e=es[0]
    for l in range(n):
        for rest in itertools.permutations(vs):
            code=[""]*n
            code[l]=("e",e)
            ri=0
            for m in range(n):
                if m==l: continue
                code[m]=("v",rest[ri]); ri+=1
            ord1.append(tuple(code))
o1id={c:i for i,c in enumerate(ord1)}
print("ord1 done",len(ord1),time.time()-t0,flush=True)
# Build ord2 columns as list of (rows, vals)
cols_row=[]; cols_val=[]
ncols=0
for j in rem2:
    es,vs=cells[2][j]
    e0,e1=es
    # ordered lifts: choose 2 distinct particles for edges (P(5,2)=20), assign which edge to which (2 ways -> included in P? choose ordered: l0->e_a... enumerate: assignment of the 2 edges to 2 distinct particles: P(5,2)*... let's enumerate: pick ordered pair (l_a,l_b) distinct + which edge goes to l_a (2 choices), rest permute over vs (6 ways). total 20*2*6=240? That's wrong: should be 120. Mistake: unordered cell has 2 DISTINGUISHED edges e0,e1 (sorted). Ordered lift: bijection from {e0,e1} to 2 of 5 particles: P(5,2)=20, remaining 3 particles to 3 vertices: 6. total 120. So: choose ordered distinct (l0,l1) with l0 gets e0, l1 gets e1: 20 ways. No extra factor 2.
    for l0 in range(n):
        for l1 in range(n):
            if l1==l0: continue
            for rest in itertools.permutations(vs):
                code=[""]*n
                code[l0]=("e",e0); code[l1]=("e",e1)
                ri=0
                for m in range(n):
                    if m==l0 or m==l1: continue
                    code[m]=("v",rest[ri]); ri+=1
                co=tuple(code)
                # faces: edge-particles in label order: sorted([l0,l1]); t=0 -> first, t=1 -> second
                labs=sorted([l0,l1])
                rows=[]; vals=[]
                for t,l in enumerate(labs):
                    ee=e0 if l==l0 else e1
                    u,v=edges[ee]
                    s=(-1)**t
                    for sgn,w in ((1,u),(-1,v)):
                        fc=list(co); fc[l]=("v",w)
                        fc=tuple(fc)
                        r=o1id.get(fc)
                        if r is None:
                            raise RuntimeError("face not in remaining ord1 -- subcomplex lift fails")
                        rows.append(r); vals.append(s*sgn)
                cols_row.append(rows); cols_val.append(vals)
                ncols+=1
print("ord2 cols",ncols,time.time()-t0,flush=True)
# quick check: all faces found => lifted remaining IS a subcomplex upstairs. 
with open("ord_d2.pkl","wb") as f:
    pickle.dump({"rows":cols_row,"vals":cols_val,"nrows":len(ord1),"ncols":ncols},f)
print("saved")
