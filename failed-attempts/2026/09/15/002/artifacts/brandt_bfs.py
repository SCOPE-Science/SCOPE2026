"""BFS: subideals of norm l from each class + fingerprint identification → class number + Brandt matrices."""
from fractions import Fraction
from itertools import product
import numpy as np, json, sys
sys.path.insert(0,'output/artifacts')
from hnf import hnf_full_rank
from brandt_main import rmulO, RM, GENS_O, OBAS, theta_fp, toL, toO, mulL

def mulm_factory(l):
    def mulm(a,b):
        a0,a1,a2,a3=a; b0,b1,b2,b3=b
        return ((a0*b0-2*a1*b1-109*a2*b2-218*a3*b3)%l,(a0*b1+a1*b0+109*a2*b3-109*a3*b2)%l,
                (a0*b2+a2*b0-2*a1*b3+2*a3*b1)%l,(a0*b3+a3*b0+a1*b2-a2*b1)%l)
    return mulm

def norm_l_subideals_of_O(l):
    """HNF bases (O-coords) of all right subideals J⊂O with [O:J]=l^2 (odd l)."""
    from brandt_step import matrix_units, coords_map
    units = matrix_units(l); coords = coords_map(units,l)
    seen=set(); lines=[]
    for u,v in product(range(l),repeat=2):
        if (u,v)==(0,0): continue
        key=tuple(sorted([((s*u)%l,(s*v)%l) for s in range(l)]))
        if key in seen: continue
        seen.add(key); lines.append((u,v))
    assert len(lines)==l+1
    out=[]
    for (u,v) in lines:
        R=set((s*u%l,s*v%l,t*u%l,t*v%l) for s in range(l) for t in range(l))
        JL=[a for a in product(range(l),repeat=4) if coords(a) in R]
        assert len(JL)==l**2
        # convert L-coords mod l → O-coords: c=(x0,x1-x3,x2,2x3) mod l
        JO=[(a[0]%l,(a[1]-a[3])%l,a[2]%l,(2*a[3])%l) for a in JL]
        rows=list(JO)+[(l if i==j else 0) for i in range(4) for j in range(4)]
        rows=[tuple(rows[4*i:4*i+4]) for i in range(len(rows)//4)]
        B,d=hnf_full_rank(rows)
        assert d==l**2,(l,d)
        # right-O-stability check
        Bm=np.array(B)
        for g in set(GENS_O):
            R=np.array(RM[g])
            for row in B:
                w=tuple(int(x) for x in (np.array(row)@R))
                # w in lattice? solve
                c=np.array(w,dtype=float)@np.linalg.inv(np.array(B,dtype=float))
                assert np.allclose(c,np.round(c)), (l,(u,v),g,row,c)
        out.append(B)
    return out

if __name__=="__main__":
    for l in [3,5]:
        Js=norm_l_subideals_of_O(l)
        print(f"l={l}: {len(Js)} ideals", flush=True)
        for B in Js:
            fp,n=theta_fp(np.array(B))
            print("  N=",n,"fp[:10]=",fp[:10],flush=True)
