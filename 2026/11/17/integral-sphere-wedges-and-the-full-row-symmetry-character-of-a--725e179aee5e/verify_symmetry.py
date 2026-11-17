#!/usr/bin/env python3
"""Signed-orbit chain computation of the S3 homology character.
Requires verify_chessboard.py (same directory). Standard library only.
"""
from verify_chessboard import enumerate_faces,lower_faces
from collections import defaultdict
from time import monotonic
F=enumerate_faces()

def action(face,permutation):
    xs=[i for i in range(28) if face>>i&1]
    ys=[4*(i//4)+permutation[i%4] for i in xs]
    inversions=sum(ys[i]>ys[j] for i in range(len(ys)) for j in range(i+1,len(ys)))
    return sum(1<<y for y in ys),(-1 if inversions%2 else 1)

def oriented_orbits(permutation,order):
    unseen=set(F)
    orbits=defaultdict(list)
    while unseen:
        root=min(unseen)
        current=root;sign=1;orbit=[]
        for t in range(order):
            assert current in unseen
            unseen.remove(current)
            orbit.append((current,sign))
            current,step_sign=action(current,permutation)
            sign*=step_sign
            if current==root:break
        assert current==root
        # If the stabilizer reverses orientation, invariant chains vanish on this orbit.
        if sign==1:
            orbits[root.bit_count()-1].append((root,orbit))
    return orbits

def matrices(orbits):
    result={}
    for k in range(7):
        reps={r:i for i,(r,_) in enumerate(orbits[k-1])}
        columns=[]
        for _,orbit in orbits[k]:
            col=defaultdict(int)
            for face,sign in orbit:
                for lower,coeff in lower_faces(face):
                    if lower in reps:col[reps[lower]]+=sign*coeff
            columns.append({j:c for j,c in col.items() if c})
        result[k]=columns
    return result

def rank_mod_prime(columns,p):
    pivots={}
    for col in columns:
        v={i:a%p for i,a in col.items() if a%p}
        while v:
            r=min(v)
            if r not in pivots:
                scale=pow(v[r],-1,p)
                pivots[r]={i:(a*scale)%p for i,a in v.items()}
                break
            a=v[r]
            for i,b in pivots[r].items():
                q=(v.get(i,0)-a*b)%p
                if q:v[i]=q
                else:v.pop(i,None)
    return len(pivots)

def compute_for_order(per,order,prime):
    orbits=oriented_orbits(per,order)
    mats=matrices(orbits)
    # Signed-orbit boundaries form a chain complex over the integers.
    for k in range(1,7):
        for col in mats[k].values() if isinstance(mats[k],dict) else mats[k]:
            comp=defaultdict(int)
            for i,a in col.items():
                for j,b in mats[k-1][i].items():comp[j]+=a*b
            assert not any(comp.values()),f'invariant d^2 fails: degree {k}'
    ranks={k:rank_mod_prime(mats[k],prime) for k in range(7)}
    betti={k:len(orbits[k])-ranks[k]-ranks.get(k+1,0) for k in range(7)}
    assert all(betti[k]==0 for k in [0,1,2,3,6])
    return {k:len(orbits[k]) for k in [-1,0,1,2,3,4,5,6]},ranks,betti

def main():
    for order,per in [(2,(0,2,1,3)),(3,(0,2,3,1))]:
        outputs=[]
        for prime in [1000003,1000033]:
            sizes,ranks,betti=compute_for_order(per,order,prime)
            outputs.append(betti)
            print(f'order={order} prime={prime} invariant_chain_dimensions={sizes}')
            print(f'order={order} prime={prime} invariant_boundary_ranks={ranks} invariant_homology={betti}')
        assert outputs[0]==outputs[1]
        expected=(49,8) if order==2 else (35,22)
        assert (outputs[0][4],outputs[0][5])==expected
    print('S3 rational homology character: H4=(63,35,21); H5=(36,-20,15)')
    print('S3 decomposition: H4=35 trivial + 14 standard; H5=1 trivial + 21 sign + 7 standard')
    print('symmetry verification: PASS')
if __name__=='__main__':main()
