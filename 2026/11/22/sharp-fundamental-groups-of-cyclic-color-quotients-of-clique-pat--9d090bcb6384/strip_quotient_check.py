#!/usr/bin/env python3
"""Exact low-dimensional quotient homology checks for the independence
complex of the clique-column strip P_m Cartesian K_q, modulo cyclic
permutation of its q colors. This is a finite checker, not the infinite proof.
"""
from collections import defaultdict,deque
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form

def independent_faces(m,q):
    by_dim=defaultdict(list)
    def visit(column,last,color_list):
        if column==m:
            if color_list:by_dim[len(color_list)-1].append(tuple(sorted(color_list)))
            return
        visit(column+1,-1,color_list)
        for color in range(q):
            if color!=last:
                visit(column+1,color,color_list+[q*column+color])
    visit(0,-1,[])
    return {k:sorted(v) for k,v in by_dim.items()}

def cyclic(face,r,q):return tuple(sorted(q*(v//q)+(v%q+r)%q for v in face))

def sign_of_order(items,sorted_items):
    perm=[sorted_items.index(v) for v in items]
    inv=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
    return -1 if inv%2 else 1

def quotient_chains(m,q):
    ff=independent_faces(m,q)
    assert all(cyclic(f,r,q)!=f for faces in ff.values() for f in faces for r in range(1,q))
    reps={k:sorted({min(cyclic(f,r,q) for r in range(q)) for f in faces}) for k,faces in ff.items()}
    index={k:{f:i for i,f in enumerate(faces)} for k,faces in reps.items()}
    lookup={}
    for k,faces in ff.items():
        for f in faces:
            canon=min(cyclic(f,r,q) for r in range(q))
            lookup[f]=(canon,next(r for r in range(q) if cyclic(canon,r,q)==f))
    boundaries={}
    for k in sorted(reps):
        if k==0:continue
        b=Matrix.zeros(len(reps[k-1]),len(reps[k]))
        for j,face in enumerate(reps[k]):
            for i in range(k+1):
                sub=face[:i]+face[i+1:]
                canon,r=lookup[sub]
                moved=[q*(v//q)+(v%q+r)%q for v in canon]
                b[index[k-1][canon],j]+=(-1)**i*sign_of_order(moved,list(sub))
        boundaries[k]=b
    for k in range(2,max(reps)+1):
        assert boundaries[k-1]*boundaries[k]==Matrix.zeros(boundaries[k-1].rows,boundaries[k].cols)
    return reps,boundaries

def H1(m,q):
    reps,bounds=quotient_chains(m,q)
    v=len(reps[0]);e=len(reps.get(1,[]))
    b1=bounds.get(1,Matrix.zeros(v,0));b2=bounds.get(2,Matrix.zeros(e,0))
    adj=defaultdict(list)
    for j in range(e):
        ends=[i for i in range(v) if b1[i,j]]
        assert len(ends)==2
        x,y=ends;adj[x].append((y,j));adj[y].append((x,j))
    seen={0};queue=deque([0]);tree=set()
    while queue:
        s=queue.popleft()
        for t,j in adj[s]:
            if t not in seen:seen.add(t);queue.append(t);tree.add(j)
    assert len(seen)==v
    non_tree=[j for j in range(e) if j not in tree]
    relations=b2[non_tree,:]
    D=smith_normal_form(relations,domain=ZZ)
    diagonal=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]]
    return dict(q=q,m=m,cell_counts=[len(reps.get(d,[])) for d in range(m)],H1_free_rank=len(non_tree)-len(diagonal),H1_torsion=[z for z in diagonal if z>1])

if __name__=='__main__':
    for q,m in [(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(5,2),(5,3),(5,4)]:
        print(H1(m,q),flush=True)
