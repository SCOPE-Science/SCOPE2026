#!/usr/bin/env python3
"""Exact finite consistency checks for an affine-plane incidence control theorem."""
from math import isqrt

def rank_mod(rows, p=1000003):
    a = [list(map(lambda z:z % p, r)) for r in rows]
    if not a: return 0
    m,n=len(a),len(a[0]); i=0
    for j in range(n):
        k=next((k for k in range(i,m) if a[k][j]),None)
        if k is None: continue
        a[i],a[k]=a[k],a[i]
        v=pow(a[i][j],-1,p)
        a[i]=[(x*v)%p for x in a[i]]
        for k in range(m):
            if k!=i and a[k][j]:
                c=a[k][j]
                a[k]=[(a[k][l]-c*a[i][l])%p for l in range(n)]
        i+=1
        if i==m: break
    return i

def verify(q):
    assert q in (2,3,5,7,11)
    pts=[(x,y) for x in range(q) for y in range(q)]
    pi={P:i for i,P in enumerate(pts)}
    # Each line is determined by its parallel class and intercept.
    # Direction labels 0..q-1 are slopes; q is vertical.
    lines=[]
    for d in range(q+1):
        for b in range(q):
            line=tuple(pi[(x,(d*x+b)%q)] for x in range(q)) if d<q else tuple(pi[(b,y)] for y in range(q))
            lines.append((d,b,line))
    assert len(set(tuple(sorted(L)) for _,_,L in lines))==q*(q+1)
    v=q*q; w=q*(q+1)
    M=[[int(i in line) for _,_,line in lines] for i in range(v)]
    # Exact incidence Gram identity.
    for i in range(v):
        for j in range(v):
            s=sum(M[i][k]*M[j][k] for k in range(w))
            assert s==1+q*int(i==j)
    P=(0,1); selected_lines=[]
    for k,(d,b,line) in enumerate(lines):
        if d!=0 and pi[P] in line:
            selected_lines.append(k)
    assert len(selected_lines)==q
    assert {lines[k][0] for k in selected_lines}==set(range(1,q+1))
    omitted={i for i,(x,y) in enumerate(pts) if y==0}|{pi[P]}
    assert len(omitted)==q+1
    selected_points=[i for i in range(v) if i not in omitted]
    assert len(selected_points)==v-q-1
    # The following square matrix acts on the point-component x of either
    # nontrivial Laplacian eigenspace. It contains measurement constraints
    # at selected points, q chosen lines, and orthogonality to constants.
    constraints=[]
    for i in selected_points:
        row=[0]*v;row[i]=1;constraints.append(row)
    constraints += [[M[i][k] for i in range(v)] for k in selected_lines]
    constraints.append([1]*v)
    assert len(constraints)==v
    assert rank_mod(constraints)==v
    # Parallel-class kernel of the point-line incidence matrix: any class
    # difference maps to zero. The chosen lines sample q different classes.
    differences=[]
    for d in range(q):
        vec=[int(d0==d)-int(d0==q) for d0,b,line in lines]
        differences.append(vec)
        assert all(sum(M[i][j]*vec[j] for j in range(w))==0 for i in range(v))
    selected_kernel=[[vec[j] for vec in differences] for j in selected_lines]
    assert rank_mod(selected_kernel)==q
    # A PBH-optimal placement can be a stalled non-zero-forcing set.
    black_points=set(selected_points); black_lines=set(selected_lines)
    for i in black_points:
        white_neighbor_count=sum(M[i][j] and j not in black_lines for j in range(w))
        assert white_neighbor_count != 1
    for j in black_lines:
        white_neighbor_count=sum(M[i][j] and i not in black_points for i in range(v))
        assert white_neighbor_count==2
    print('ZERO_FORCING_STALLED q=%d' % q)
    print('q=%d points=%d lines=%d actuators=%d Gram_OK nontrivial_rank=%d line_kernel_rank=%d' %
          (q,v,w,len(selected_points)+len(selected_lines),v,q))

if __name__=='__main__':
    for q in (2,3,5,7,11): verify(q)
    print('VERIFY_OK')
