"""Exact finite collapse and barcode checks for 3- and 5-edge theta arms.

Run in the directory containing verify_mixed_theta.py:
    python3 verify_five_arm.py
"""
from itertools import combinations
from verify_mixed_theta import theta, paths_dists, rips_faces, remove_pair, bettis_mod2


def verify(p,q):
    V,E=theta(p,[5]*q)
    D=paths_dists(V,E)
    assert max(max(row.values()) for row in D.values())<=5
    K=rips_faces(V,D,3)
    initial=len(K)
    # Old short arms have identical closed neighborhoods in the graph cube.
    for side in (1,2):
        rep=f's0_{side}'
        for j in range(1,p):
            x=f's{j}_{side}'
            verts={v for v in V if (v,) in K}
            assert {w for w in verts if D[x][w]<=3}=={w for w in verts if D[rep][w]<=3}
            lows=[face for face in K if x in face and rep not in face]
            for low in sorted(lows,key=lambda face:-len(face)):
                remove_pair(K,low,low+(rep,))
    remaining={v for v in V if (v,) in K}
    core={'u','v','s0_1','s0_2'}
    assert len(remaining)==4+4*q
    target=set()
    for j in range(q):
        arm=set(f'l{j}_{k}' for k in range(1,5))
        C=rips_faces(core|arm,D,3)
        target |= C
        nonedges=[(a,b) for a,b in combinations(sorted(core|arm),2) if D[a][b]>3]
        assert len(nonedges)==4 and len(set(sum(([a,b] for a,b in nonedges),[])))==8
    # Every face outside target uses multiple long arms; every such face
    # lies on exactly one of the two short-endpoint cones.
    outer=K-target
    lowers=[]
    for face in outer:
        if 'u' in face or 'v' in face:continue
        long_indices={int(z.split('_')[0][1:]) for z in face if z.startswith('l')}
        assert len(long_indices)>=2
        new=[int(z.split('_')[1]) for z in face if z.startswith('l')]
        near_u=all(k<=2 for k in new)
        near_v=all(k>=3 for k in new)
        assert near_u != near_v
        apex='u' if near_u else 'v'
        assert tuple(sorted(face+(apex,))) in outer
        lowers.append((face,apex))
    # Every outside face belongs to exactly one pair.
    covered=set()
    for face,apex in lowers:
        a=tuple(sorted(face));b=tuple(sorted(face+(apex,)))
        assert not (a in covered or b in covered)
        covered.add(a);covered.add(b)
    assert covered==outer
    for low,apex in sorted(lowers,key=lambda item:-len(item[0])):
        remove_pair(K,low,low+(apex,))
    assert K==target
    assert len(target)==65*q+15  # 80 for q=1; each extra arm adds 65 faces.
    B=bettis_mod2(rips_faces(V,D,3))
    assert B.get(0)==1 and B.get(3)==q and all(v==0 for k,v in B.items() if k not in (0,3))
    # Radius four has a universal short-arm vertex.
    assert all(D['s0_1'][w]<=4 for w in V)
    return initial,len(outer),B[3]


def main():
    cases=0;removed=0
    for p in range(2,5):
        for q in range(1,4):
            initial,outer,b3=verify(p,q)
            cases+=1;removed+=outer
            print(f'p={p},q={q},faces={initial},cross_arm_faces={outer},beta3={b3}')
    print('MIXED_THETA_RADIUS3_EXACT_COLLAPSE_OK',cases,'cases;',removed,'external faces')


if __name__=='__main__':main()
