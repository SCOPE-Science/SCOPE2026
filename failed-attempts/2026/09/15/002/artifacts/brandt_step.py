"""Stepwise Brandt computation with checkpoints saved to JSON."""
from fractions import Fraction
from itertools import product
import numpy as np, json
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form as hnf

def mulm_factory(l):
    def mulm(a,b):
        a0,a1,a2,a3=a; b0,b1,b2,b3=b
        return (
          (a0*b0-2*a1*b1-109*a2*b2-218*a3*b3)%l,
          (a0*b1+a1*b0+109*a2*b3-109*a3*b2)%l,
          (a0*b2+a2*b0-2*a1*b3+2*a3*b1)%l,
          (a0*b3+a3*b0+a1*b2-a2*b1)%l)
    return mulm

def matrix_units(l):
    mulm = mulm_factory(l)
    def iszero(a): return all(v==0 for v in a)
    one=(1,0,0,0)
    prop=[a for a in product(range(l),repeat=4) if mulm(a,a)==a and not iszero(a) and a!=one]
    e=prop[0]
    e12=[a for a in product(range(l),repeat=4) if mulm(e,a)==a and iszero(mulm(a,e)) and not iszero(a)]
    e21=[a for a in product(range(l),repeat=4) if mulm(a,e)==a and iszero(mulm(e,a)) and not iszero(a)]
    x=e12[0]
    for y in e21:
        if mulm(x,y)==e: break
    return [e,x,y,mulm(y,x)]

def coords_map(units,l):
    M=np.array([[u[i] for u in units] for i in range(4)], dtype=int)%l
    def coords(a):
        rhs=np.array(a,dtype=int)%l
        Ab=np.concatenate([M,np.eye(4,dtype=int)],axis=1)%l
        for col in range(4):
            piv=next(row for row in range(col,4) if Ab[row,col]%l!=0)
            Ab[[col,piv]]=Ab[[piv,col]]
            Ab[col]=(Ab[col]*pow(int(Ab[col,col]),-1,l))%l
            for row in range(4):
                if row!=col and Ab[row,col]%l!=0:
                    Ab[row]=(Ab[row]-Ab[row,col]*Ab[col])%l
        return tuple(int(v)%l for v in (Ab[:,4:8]@rhs%l))
    return coords

def subideals_norm_l(l):
    """Right subideals J of O (as L-submodules, valid for odd l) with [O:J]=l^2. Returns HNF bases."""
    units = matrix_units(l)
    coords = coords_map(units,l)
    # verify on basis
    for a in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
        c=coords(a)
        r=np.sum([v*np.array(u) for v,u in zip(c,units)],axis=0)%l
        assert tuple(int(x)%l for x in r)==a
    lines=[]
    seen=set()
    for u,v in product(range(l),repeat=2):
        if (u,v)==(0,0): continue
        key=tuple(sorted([( (s*u)%l,(s*v)%l) for s in range(l)]))
        if key in seen: continue
        seen.add(key); lines.append((u,v))
    assert len(lines)==l+1, (l,len(lines))
    out=[]
    for (u,v) in lines:
        R=set()
        for s in range(l):
            for t in range(l):
                R.add((s*u%l,s*v%l,t*u%l,t*v%l))
        J=[a for a in product(range(l),repeat=4) if coords(a) in R]
        assert len(J)==l**2
        rows=list(J)+[(l if i==j else 0) for i in range(4) for j in range(4)]
        rows=[tuple(rows[4*i:4*i+4]) for i in range(len(rows)//4)]
        H=np.array(hnf(Matrix(rows)).tolist(),dtype=int)
        H=H[~np.all(H==0,axis=1)]
        out.append(H.tolist())
    return out

if __name__=="__main__":
    for l in [3,5]:
        Js = subideals_norm_l(l)
        print(f"l={l}: {len(Js)} subideals", flush=True)
        for J in Js: print("  ", J, flush=True)
        json.dump(Js, open(f"/tmp/subideals_{l}.json","w"))
