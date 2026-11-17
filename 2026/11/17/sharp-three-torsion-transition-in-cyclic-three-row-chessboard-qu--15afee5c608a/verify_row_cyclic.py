#!/usr/bin/env python3
"""Independent exact cellular checker for three-row rook quotients.
Rebuilds all 3-row nonattacking rook faces up to three rooks, forms
free row-rotation orbit cells, verifies boundary-square zero, then
computes integral Smith invariants in a canonical cycle basis.
"""
from itertools import combinations, permutations
from math import comb
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def faces(n,k):
    # Each matching is represented by increasing columns and distinct rows.
    return [tuple(zip(rows,cols)) for cols in combinations(range(1,n+1),k)
            for rows in permutations(range(3),k)]


def shifted(face,s):
    return tuple(((row+s)%3,col) for row,col in face)


def representative(face):
    return min(shifted(face,s) for s in range(3))


def check(n):
    reps={k:sorted(set(map(representative,faces(n,k)))) for k in (1,2,3)}
    counts=[len(reps[k]) for k in (1,2,3)]
    assert counts==[n,n*(n-1),n*(n-1)*(n-2)//3]
    idx={k:{f:i for i,f in enumerate(reps[k])} for k in reps}
    D1=Matrix.zeros(counts[0],counts[1]); D2=Matrix.zeros(counts[1],counts[2])
    for d,M in ((2,D1),(3,D2)):
        for j,face in enumerate(reps[d]):
            for pos in range(d):
                sub=face[:pos]+face[pos+1:]
                M[idx[d-1][representative(sub)],j]+=(-1)**pos
    assert D1*D2==Matrix.zeros(counts[0],counts[2])
    # Independently identify each 2-edge quotient orbit with its column pair
    # and a signed row difference; form boundary coordinates in basis
    #   d_ij=e^+_ij-e^-_ij, all i<j
    #   t_ij=e^+_ij-e^+_1j+e^+_1i, 1<i<j.
    pairs=list(combinations(range(1,n+1),2))
    trigs=list(combinations(range(2,n+1),2))
    d_pos={p:i for i,p in enumerate(pairs)}
    t_pos={p:len(pairs)+i for i,p in enumerate(trigs)}
    def edge_info(f):
        (ri,i),(rj,j)=f
        return (i,j), 1 if (rj-ri)%3==1 else -1
    def coords(z):
        # input a formal signed sum of oriented edges, output its unique
        # integral coordinates in cycle space basis (d,t).
        arr=[0]*(len(pairs)+len(trigs))
        a={p:0 for p in pairs}
        for f,coeff in z:
            pair,sign=edge_info(f)
            if sign==1: a[pair]+=coeff
            else:
                a[pair]+=coeff
                arr[d_pos[pair]]-=coeff
        # The a-part is a cycle; t_ij coefficient equals a_ij for 2<=i<j.
        for p in trigs: arr[t_pos[p]]=a[p]
        # Verify reconstruction and equality over original oriented edges.
        recon={(p,s):0 for p in pairs for s in (+1,-1)}
        for p in pairs:
            v=arr[d_pos[p]]
            recon[p,+1]+=v;recon[p,-1]-=v
        for (i,j) in trigs:
            v=arr[t_pos[i,j]]
            recon[(i,j),+1]+=v
            recon[(1,j),+1]-=v
            recon[(1,i),+1]+=v
        actual={(p,s):0 for p in pairs for s in (+1,-1)}
        for f,c in z:
            p,s=edge_info(f);actual[p,s]+=c
        assert recon==actual
        return arr
    R=Matrix.zeros(len(pairs)+len(trigs),counts[2])
    for j,f in enumerate(reps[3]):
        boundary=[(f[:pos]+f[pos+1:],(-1)**pos) for pos in range(3)]
        for i,v in enumerate(coords(boundary)): R[i,j]=v
    SD=smith_normal_form(R,domain=ZZ)
    diag=[abs(int(SD[i,i])) for i in range(min(SD.rows,SD.cols)) if SD[i,i]]
    tors=[v for v in diag if v>1]
    b1=R.rows-len(diag)
    b2=R.cols-len(diag)
    exp_b1,exp_tors=(2,[]) if n in (3,4) else (0,[3])
    exp_b2={3:0,4:1}.get(n,n*(n-2)*(n-4)//3-1)
    assert (b1,tors,b2)==(exp_b1,exp_tors,exp_b2), (n,b1,tors,b2)
    # Formula for Euler characteristic of free quotient: cells by simple orbits.
    assert counts[0]-counts[1]+counts[2]==n*(n-2)*(n-4)//3
    return n,counts,b1,tors,b2

if __name__=='__main__':
    for n in range(3,9):
        print(check(n),flush=True)
    print('ROW_CYCLIC_CHESSBOARD_INTEGRAL_CHECK_PASS n=3..8')
