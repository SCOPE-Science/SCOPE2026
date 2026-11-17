#!/usr/bin/env python3
"""Exact finite color-cell checks for cyclic quotients of complete-graph Hom complexes.
The small integer Smith calculation uses SymPy, as declared in requirements.txt.
"""
from itertools import product
from collections import defaultdict,Counter
from math import comb

def rotate_mask(mask,shift,p):
    return ((mask << shift) | (mask >> (p-shift))) & ((1<<p)-1) if shift else mask

def rotate_cell(cell,s,p):
    return tuple(rotate_mask(mask,s,p) for mask in cell)

def all_cells(m,p):
    # Assignment label 0 means unused target color; 1,...,m mean its source coordinate.
    buckets=defaultdict(list)
    for a in product(range(m+1), repeat=p):
        counts=Counter(a)
        if any(counts[i]==0 for i in range(1,m+1)): continue
        masks=[0]*m
        for x,c in enumerate(a):
            if c:masks[c-1]|=1<<x
        cell=tuple(masks)
        dimension=sum(x.bit_count()-1 for x in cell)
        buckets[dimension].append(cell)
    return buckets

def canonical(cell,p):
    return min(rotate_cell(cell,s,p) for s in range(p))

def sortmask(mask,p):
    return [i for i in range(p) if (mask>>i)&1]

def orientation_sign(old,shift,p):
    # signs from sorting each rotated coordinate simplex
    sign=1
    for mask in old:
        arr=[(i+shift)%p for i in sortmask(mask,p)]
        inversions=sum(1 for i,x in enumerate(arr) for y in arr[i+1:] if x>y)
        if inversions%2:sign=-sign
    return sign

def canonical_with_sign(face,p):
    # Map a face to the orientation of its canonical representative.
    rep=canonical(face,p)
    shifts=[s for s in range(p) if rotate_cell(face,s,p)==rep]
    assert len(shifts)==1  # free on all cells
    return rep,orientation_sign(face,shifts[0],p)

def calculate(m,p):
    buckets=all_cells(m,p)
    reps={d: sorted({canonical(c,p) for c in v}) for d,v in buckets.items()}
    for d,v in buckets.items():
        assert len(v)==p*len(reps[d]),'nonfree cell orbit'
    dims=sorted(reps)
    assert dims==list(range(p-m+1))
    chi=sum((-1)**d*len(reps[d]) for d in dims)
    chi_formula=sum((-1)**j*comb(m,j)*(1-j)**p for j in range(m+1))
    assert chi*p==chi_formula
    beta=(-1)**(p-m)*(chi_formula-1)
    top=(-1)**(p-m)*(chi-1)
    assert top==(beta+(-1)**(p-m)*(1-p))//p
    idmap={d:{c:i for i,c in enumerate(reps[d])} for d in dims}
    boundaries={}
    for d in dims[1:]:
        columns=[]
        for cell in reps[d]:
            col=defaultdict(int)
            offset=0
            for i,mask in enumerate(cell):
                colors=sortmask(mask,p)
                if len(colors)>1:
                    for j,k in enumerate(colors):
                        new=list(cell);new[i]=mask^(1<<k)
                        f,sg=canonical_with_sign(tuple(new),p)
                        col[idmap[d-1][f]]+=((-1)**(offset+j))*sg
                offset+=len(colors)-1
            columns.append({i:v for i,v in col.items() if v})
        boundaries[d]=columns
    # All integral chain compositions, no modular shortcuts.
    for d in dims[2:]:
        lower=boundaries[d-1]
        for col in boundaries[d]:
            out=defaultdict(int)
            for j,v in col.items():
                for k,w in lower[j].items():out[k]+=v*w
            assert all(v==0 for v in out.values()), 'boundary squared nonzero'
    # Sparse exact finite-field ranks.
    def modrank(columns,q):
        pivots={}
        for col in columns:
            c={i:v%q for i,v in col.items() if v%q}
            while c:
                k=min(c)
                if k not in pivots:
                    factor=pow(c[k],-1,q)
                    pivots[k]={i:(v*factor)%q for i,v in c.items()}
                    break
                alpha=c[k]
                for j,v in pivots[k].items():
                    c[j]=(c.get(j,0)-alpha*v)%q
                    if c[j]==0:del c[j]
        return len(pivots)
    ranks_q={q:{d:modrank(boundaries[d],q) for d in boundaries} for q in [p,1000003]}
    betti={q: [len(reps[d])-ranks_q[q].get(d,0)-ranks_q[q].get(d+1,0) for d in dims] for q in ranks_q}
    assert betti[1000003]==[1]+[0]*(p-m-1)+[top]
    assert betti[p]==[1]+[1]*(p-m-1)+[top+1]
    smith=None
    if p==5 and m==3:
        from sympy import SparseMatrix, ZZ
        from sympy.matrices.normalforms import smith_normal_form
        smith={}
        for d,cols in boundaries.items():
            matrix=SparseMatrix(len(reps[d-1]),len(cols),{(i,j):v for j,col in enumerate(cols) for i,v in col.items()})
            diag=smith_normal_form(matrix,domain=ZZ)
            entries=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]!=0]
            smith[d]=dict(rank=len(entries),nonunit=[v for v in entries if v!=1])
        assert smith[2]['nonunit']==[5]
    print(f'(m,p)=({m},{p}) cells={[(d,len(buckets[d])) for d in dims]} orbit_cells={[(d,len(reps[d])) for d in dims]}')
    print(f'chi_X={chi_formula}, chi_Y={chi}, beta_X={beta}, top_rank_Y={top}')
    print(f'ranks(F_{p})={ranks_q[p]}; betti(F_{p})={betti[p]}')
    print(f'ranks(F_1000003)={ranks_q[1000003]}; betti(F_1000003)={betti[1000003]}')
    if smith:print('integral Smith boundary invariants:',smith)

if __name__=='__main__':
    calculate(3,5)
    calculate(3,7)
    print('VERIFY_OK')
