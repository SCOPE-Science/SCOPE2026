#!/usr/bin/env python3
"""Independent finite-chain tests of the weighted-simplex persistence formula.
No external packages are required. Ordinary integral simplicial boundaries
are used; this is NOT weighted homology with a modified boundary.
"""
import itertools
from collections import Counter


def wt(mask, weights):
    return sum(w for i, w in enumerate(weights) if (mask >> i) & 1)


def faces(mask, m):
    return [mask ^ (1 << i) for i in range(m) if mask & (1 << i)]


def barcode_mod2(weights):
    m=len(weights)
    masks=sorted(range(1<<m), key=lambda s:(wt(s,weights),s.bit_count(),s))
    index={s:i for i,s in enumerate(masks)}
    reduced={}
    pairs=[]
    unpaired=set()
    for j,s in enumerate(masks):
        col={index[f] for f in faces(s,m)}
        while col:
            p=max(col)
            if p in reduced:
                col.symmetric_difference_update(reduced[p])
            else:
                reduced[p]=col
                pairs.append((masks[p],s))
                break
        if not col:
            unpaired.add(s)
    assert {s for s,_ in pairs}==unpaired, (weights,'unmatched zero columns')
    return Counter((s.bit_count()-1,wt(s,weights),wt(t,weights)) for s,t in pairs if wt(s,weights)<wt(t,weights))


def expected(weights):
    v=weights[0]
    return Counter((s.bit_count()-1,wt(s,weights),wt(s,weights)+v)
            for s in range(1<<len(weights)) if not (s&1))


def oriented_boundary(mask, m):
    indices=[i for i in range(m) if mask>>i&1]
    return {mask^(1<<i):(-1 if j%2 else 1) for j,i in enumerate(indices)}


def z_cycle(S, weights):
    return oriented_boundary(S|1,len(weights))


def check_chain(weights):
    m=len(weights)
    for S in range(1<<m):
        if S&1:continue
        z=z_cycle(S,weights)
        assert z.get(S)==1
        assert all(wt(T,weights)<=wt(S,weights) for T in z)
        dz={}
        for T,cf in z.items():
            for U,c in oriented_boundary(T,m).items():
                dz[U]=dz.get(U,0)+cf*c
        assert all(c==0 for c in dz.values())
        # Every z[S] is a unit-triangular replacement for a simplex S.
    return 1<< (m-1)


def sign_order(original, transformed):
    return (-1)**sum(transformed[i]>transformed[j] for i in range(len(transformed)) for j in range(i+1,len(transformed)))


def check_equivariance(weights):
    m=len(weights)
    if weights.count(min(weights))!=1: return 0
    grouped={}
    for i,w in enumerate(weights): grouped.setdefault(w,[]).append(i)
    perms=[]
    for swaps in itertools.product(*(list(itertools.permutations(gr)) for gr in grouped.values())):
        v=list(range(m))
        for gr,im in zip(grouped.values(),swaps):
            for i,j in zip(gr,im):v[i]=j
        perms.append(v)
    for p in perms:
        for S in range(1<<m):
            if S&1:continue
            old=[i for i in range(m) if S>>i&1]
            mapped=[p[i] for i in old]
            newmask=sum(1<<i for i in mapped)
            sgn=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
            zs=z_cycle(S,weights)
            actual={}
            for face,cf in zs.items():
                inds=[i for i in range(m) if face>>i&1]
                permuted=[p[i] for i in inds]
                qmask=sum(1<<i for i in permuted)
                qsgn=(-1)**sum(permuted[i]>permuted[j] for i in range(len(permuted)) for j in range(i+1,len(permuted)))
                actual[qmask]=cf*qsgn
            target={k:v*sgn for k,v in z_cycle(newmask,weights).items()}
            assert actual==target,(weights,p,S,actual,target)
    return len(perms)


def run():
    count=0; faces_count=0; perm_count=0
    for m in range(2,7):
        for weights in itertools.combinations_with_replacement((1,2,3,4),m):
            got=barcode_mod2(weights)
            want=expected(weights)
            assert got==want,(weights,got,want)
            faces_count+=check_chain(weights)
            if m<=5:perm_count+=check_equivariance(weights)
            count+=1
    print('WEIGHTED_MATROID_FIXED_PERSISTENCE_PASS',f'weight_profiles={count}',f'cycle_checks={faces_count}',f'normalizer_permutation_checks={perm_count}')
    for weights in ((1,3,3),(2,2,2),(1,2,2,3,3)):
        bc=expected(weights)
        print('weights='+str(weights),'nonempty_bars='+str(sorted((a,b,c) for (a,b,c),k in bc.items() if a>=0 for _ in range(k))))
if __name__=='__main__':run()
