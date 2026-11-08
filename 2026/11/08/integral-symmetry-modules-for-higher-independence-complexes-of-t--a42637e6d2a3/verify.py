#!/usr/bin/env python3
"""Independent signed Lefschetz tests of natural automorphism actions on
higher-independence complexes of two-ended subdivided double stars.

The verification is finite. The all-parameter theorem uses exact equivariant
Mayer--Vietoris sequences and augmented simplex chains, not extrapolation.
"""
from itertools import permutations, product
from math import comb


def sign_perm(v):
    inv = sum(v[i] > v[j] for i in range(len(v)) for j in range(i+1,len(v)))
    return -1 if inv % 2 else 1


def face(mask,r,edges,n):
    remaining = {v for v in range(n) if mask & (1<<v)}
    while remaining:
        x = remaining.pop(); stack=[x]; size=1
        while stack:
            u=stack.pop()
            for v,w in edges:
                t = w if u==v else v if u==w else -1
                if t in remaining:
                    remaining.remove(t);stack.append(t);size+=1
        if size>r:return False
    return True


def chars_wedge_augmentation(mapping):
    # mapping is permutation in 0..len-1; output traces on exterior powers
    seen=set(); polynomial=[1]
    for i in range(len(mapping)):
        if i in seen:continue
        j=i; ell=0
        while j not in seen:
            seen.add(j);ell+=1;j=mapping[j]
        nxt=[0]*(len(polynomial)+ell)
        for k,c in enumerate(polynomial):
            nxt[k]+=c
            nxt[k+ell]-=(-1)**ell*c
        polynomial=nxt
    out=[]
    for k in range(len(mapping)):
        out.append(polynomial[k]-(out[k-1] if k else 0))
    assert polynomial[-1]==out[-1]
    return out


def perms(a,b):
    A=tuple(range(3,3+a)); B=tuple(range(3+a,3+a+b))
    for p in permutations(A):
        for q in permutations(B):
            yield (0,1,2,*p,*q),False
    if a==b:
        for p in permutations(B):
            for q in permutations(A):
                yield (2,1,0,*p,*q),True


def lefschetz(faces,g):
    output=-1   # empty augmented face
    for vertices in faces:
        images=[g[i] for i in vertices]
        if set(images)==set(vertices):
            output+=(-1)**(len(vertices)-1)*sign_perm(images)
    return output


def predicted_trace(a,b,r,g,swap):
    m=a+b
    # Lower summand in reduced H_(r-1): det(hub two-space) * exterior^(r-3) U(A+B)
    leaf_map=[g[3+i]-3 for i in range(m)]
    char_leaf=chars_wedge_augmentation(leaf_map)
    low=( (-1 if swap else 1)*char_leaf[r-3] ) if 3<=r<=m+2 else 0
    # Upper summand in reduced H_(2r-1): tensor of local exterior powers,
    # with a (-1)^r interchange sign for the two star factors.
    if r>min(a,b): high=0
    elif not swap:
        ca=chars_wedge_augmentation([g[3+i]-3 for i in range(a)])
        cb=chars_wedge_augmentation([g[3+a+i]-(3+a) for i in range(b)])
        high=ca[r-1]*cb[r-1]
    else:
        # trace of signed factor swap = (-1)^r times trace of composition
        a_sq=[g[g[3+i]]-3 for i in range(a)]
        high=(-1)**r*chars_wedge_augmentation(a_sq)[r-1]
    return low,high


def gf2_boundary_rank(faces_by_dim,degree):
    """Column elimination over F2 in the full augmented simplicial complex."""
    source=faces_by_dim.get(degree,[])
    if not source:return 0
    if degree==0: return 1
    prior={tuple(face):i for i,face in enumerate(faces_by_dim.get(degree-1,[]))}
    pivots={}
    for face in source:
        column=0
        for i in range(len(face)):
            sub=face[:i]+face[i+1:]
            column^=1<<prior[sub]
        while column:
            v=column.bit_length()-1
            if v in pivots:column^=pivots[v]
            else:
                pivots[v]=column
                break
    return len(pivots)


def check_modtwo_ranks(simplices,a,b,r):
    by_dim={}
    for f in simplices:
        by_dim.setdefault(len(f)-1,[]).append(f)
    if not by_dim:return 0
    top=max(by_dim)
    boundary={d:gf2_boundary_rank(by_dim,d) for d in range(top+1)}
    for d in range(top+1):
        actual=len(by_dim.get(d,[]))-boundary.get(d,0)-boundary.get(d+1,0)
        expected=(comb(a+b-1,r-3) if 3<=r<=a+b+2 and d==r-1 else 0)
        expected+=(comb(a-1,r-1)*comb(b-1,r-1) if 1<=r<=min(a,b) and d==2*r-1 else 0)
        assert actual==expected,(a,b,r,d,actual,expected)
    return 1


def main():
    checks=0; nonidentity=0; rank_checks=0; group_orders={}
    for a,b in product(range(1,4),repeat=2):
        n=a+b+3
        E=[(0,1),(1,2)]+[(0,i) for i in range(3,3+a)]+[(2,i) for i in range(3+a,n)]
        auts=list(perms(a,b));group_orders[(a,b)]=len(auts)
        for r in range(1,n+2):
            simplices=[tuple(i for i in range(n) if mask&(1<<i))
                       for mask in range(1,1<<n) if face(mask,r,E,n)]
            rank_checks+=check_modtwo_ranks(simplices,a,b,r)
            for g,swap in auts:
                lo,hi=predicted_trace(a,b,r,g,swap)
                expected=(-1)**(r-1)*lo-hi
                got=lefschetz(simplices,g)
                assert got==expected,(a,b,r,g,got,expected,lo,hi)
                checks+=1
                nonidentity+=int(g!=tuple(range(n)))
    print('AUTOMORPHISM_GROUP_ORDERS',group_orders)
    print('SIGNED_REDUCED_LEFSCHETZ_EQUALITIES',checks)
    print('NONIDENTITY_CASES',nonidentity)
    print('EXACT_MOD_TWO_BETTI_PROFILES',rank_checks)
    print('D_2_2_HUB_SWAP_R1_H1_TRACE',predicted_trace(2,2,1,(2,1,0,5,6,3,4),True)[1])
    print('D_2_2_HUB_SWAP_R3_LOWER_TRACE',predicted_trace(2,2,3,(2,1,0,5,6,3,4),True)[0])
    print('ALL_VERIFY_OK')

if __name__=='__main__':
    main()
