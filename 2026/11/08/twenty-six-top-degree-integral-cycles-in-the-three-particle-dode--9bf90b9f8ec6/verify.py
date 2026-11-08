#!/usr/bin/env python3
"""Exact integral degree-three reduced graph-configuration chain calculation.

No external Python packages. The edge and half-edge conventions are defined here.
"""
import hashlib
import itertools
import json
from collections import defaultdict

N=10
vertices=tuple(range(2*N))
def edge(a,b): return tuple(sorted((a,b)))
E=tuple(sorted(set([edge(i,(i+1)%N) for i in range(N)] +
                   [edge(i,N+i) for i in range(N)] +
                   [edge(N+i,N+(i+2)%N) for i in range(N)])))
assert len(E)==30
nbr={v:sorted([b if a==v else a for a,b in E if a==v or b==v]) for v in vertices}
assert all(len(nbr[v])==3 for v in vertices)
edge_id={e:k for k,e in enumerate(E)}

# C3: three degree-one half-edge differences, each using a distinct vertex.
# C2: two such differences at distinct vertices and one edge generator.
pairs=tuple(itertools.combinations(vertices,2))
pair_index={p:i for i,p in enumerate(pairs)}
def rindex(x,y,a,b,e):
    return (pair_index[(x,y)]*4+(a-1)*2+(b-1))*len(E)+e
assert len(pairs)*4*len(E)==22800
cols=[]
for vtx in itertools.combinations(vertices,3):
    for choices in itertools.product((1,2),repeat=3):
        acc=defaultdict(int)
        for j,(v,c) in enumerate(zip(vtx,choices)):
            other=[(vtx[k],choices[k]) for k in range(3) if k!=j]
            (x,a),(y,b)=other
            for plus,neigh in ((1,nbr[v][c]),(-1,nbr[v][0])):
                ei=edge_id[edge(v,neigh)]
                acc[rindex(x,y,a,b,ei)]+=((1 if j%2==0 else -1)*plus)
        col={k:v for k,v in acc.items() if v}
        assert len(col)==6 and set(map(abs,col.values()))=={1}
        cols.append(col)
assert len(cols)==9120

# A unit-pivot (unimodular) column-reduction, recording precise integer
# kernel witnesses.  Unit pivots give a saturation certificate, not only rank.
piv={}; piv_rep={}; dependencies=[]; pivots_created=0
for index,initial_col in enumerate(cols):
    col=dict(initial_col)
    rep={index:1}
    while col:
        row=max(col)
        c=col[row]
        if row not in piv:
            assert c in (-1,1), ('nonunit pivot',index,row,c)
            if c==-1:
                col={r:-z for r,z in col.items()}
                rep={j:-z for j,z in rep.items()}
            piv[row]=col
            piv_rep[row]=rep
            pivots_created+=1
            break
        base=piv[row]
        for r,z in base.items():
            new=col.get(r,0)-c*z
            if new:col[r]=new
            else:col.pop(r,None)
        for j,z in piv_rep[row].items():
            new=rep.get(j,0)-c*z
            if new:rep[j]=new
            else:rep.pop(j,None)
    else:
        # Reconstruct the entire integer chain boundary for each witness.
        assert rep.get(index)==1
        image=defaultdict(int)
        for j,coefficient in rep.items():
            for r,z in cols[j].items():image[r]+=coefficient*z
        assert not any(image.values())
        dependencies.append((index,rep))
assert pivots_created==9094 and len(dependencies)==26
# The zero residuals are independent: each kernel vector has coefficient 1
# in a new nonpivot column and only earlier columns elsewhere.
nonpivot=[i for i,_ in dependencies]
assert all(all((j==i or j<i) for j in rep) and i not in set(nonpivot[:t])
           for t,(i,rep) in enumerate(dependencies))

# Independent characteristic-two row reduction, not using integral pivots.
basis={}; mod2_rank=0
for col in cols:
    vec=0
    for k,v in col.items():
        if v%2:vec ^=1<<k
    while vec:
        lead=vec.bit_length()-1
        if lead not in basis:
            basis[lead]=vec;mod2_rank+=1
            break
        vec ^= basis[lead]
assert mod2_rank==9094

# Recompute the boundary-square on all basis elements of C3 algebraically.
# For each triple of distinct vertices, antisymmetrization of commuting
# edge replacements makes each double-differential coefficient cancel.
def boundary_squared_zero_on_c3():
    # Verified by pairwise products of local edge differences (d_v d_w =
    # -d_w d_v in the ordered tensor complex), including shared graph edges.
    for vtx in itertools.combinations(vertices,3):
        for choices in itertools.product((1,2),repeat=3):
            terms=defaultdict(int)
            for j in range(3):
                for k in range(3):
                    if j==k:continue
                    left=[t for t in range(3) if t!=j]
                    pos=left.index(k)
                    sign=((-1)**(j+pos))
                    for sj,nj in ((1,nbr[vtx[j]][choices[j]]),(-1,nbr[vtx[j]][0])):
                        for sk,nk in ((1,nbr[vtx[k]][choices[k]]),(-1,nbr[vtx[k]][0])):
                            l=[t for t in range(3) if t!=j and t!=k][0]
                            e1=edge_id[edge(vtx[j],nj)]
                            e2=edge_id[edge(vtx[k],nk)]
                            # Symmetric degree-zero edge factors commute.
                            terms[(vtx[l],choices[l],tuple(sorted((e1,e2))))]+=sign*sj*sk
            if any(terms.values()):return False
    return True
assert boundary_squared_zero_on_c3()

serial=json.dumps([(j,sorted(rep.items())) for j,rep in dependencies],separators=(',',':'))
hash_cycles=hashlib.sha256(serial.encode('ascii')).hexdigest()
print('GRAPH GP(10,2) V=20 E=30 DEGREE=3')
print('REDUCED_CHAINS C3=9120 C2=22800 C4=0')
print('BOUNDARY_SQUARED_ZERO=true')
print('INTEGRAL_UNIT_PIVOTS=9094 KERNEL_WITNESSES=26')
print('INDEPENDENT_GF2_RANK=9094')
print('KERNEL_WITNESS_SHA256='+hash_cycles)
print('CONCLUSION H3(B3(dodecahedral);Z)=Z^26')
print('ALL_CHECKS_PASS')
