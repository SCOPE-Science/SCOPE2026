"""Corrected BFS: column-wise minimal right ideals -> subideals -> classes -> Brandt matrices."""
from itertools import product
import numpy as np, sys, json
sys.path.insert(0,'output/artifacts')
from hnf import hnf_full_rank
from brandt_main import RM, GENS_O, theta_fp
from brandt_step import matrix_units, coords_map

def tom(c): return np.array(c).reshape(2,2)
def subideals_O(l):
    units = matrix_units(l); coords = coords_map(units,l)
    Gm = {g: tom(coords(g))%l for g in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]}
    seen=set(); lines=[]
    for u,v in product(range(l),repeat=2):
        if (u,v)==(0,0): continue
        key=tuple(sorted([((s*u)%l,(s*v)%l) for s in range(l)]))
        if key in seen: continue
        seen.add(key); lines.append((u,v))
    assert len(lines)==l+1
    out=[]
    for (u,v) in lines:
        R=set(((s*u)%l,(t*u)%l,(s*v)%l,(t*v)%l) for s in range(l) for t in range(l))
        assert len(R)==l**2
        # sanity right ideal
        for C in R:
            for g in [(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
                assert tuple(int(x)%l for x in (tom(C)@Gm[g]%l).ravel()) in R
        JL=[a for a in product(range(l),repeat=4) if coords(a) in R]
        assert len(JL)==l**2
        JO=[(a[0]%l,(a[1]-a[3])%l,a[2]%l,(2*a[3])%l) for a in JL]
        rows=[list(r) for r in JO]+[[l if i==j else 0 for j in range(4)] for i in range(4)]
        B,d=hnf_full_rank(rows)
        assert d==l**2,(l,d)
        Bm=np.array(B,dtype=float); Bi=np.linalg.inv(Bm)
        for g in set(GENS_O):
            for row in B:
                c=(np.array(row)@np.array(RM[g]))@Bi
                assert np.allclose(c,np.round(c)),(l,(u,v),g)
        out.append(B)
    return out

if __name__=="__main__":
    allJ={}
    for l in [3,5,7,11,13]:
        Js=subideals_O(l)
        allJ[str(l)]=Js
        print(f"l={l}: {len(Js)} ideals VERIFIED right-O-stable", flush=True)
        for B in Js:
            fp,n=theta_fp(np.array(B))
            print("   fp[:8]=",fp[:8],flush=True)
    json.dump(allJ, open("/tmp/subideals_O.json","w"))
