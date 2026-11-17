#!/usr/bin/env python3
"""Independent finite checks of distance-forbidden graphs and signed chain Lefschetz traces.
Python 3 standard library only. All homology deductions are separately proved in RESULT.md.
"""
from functools import lru_cache

def check(m,b):
    n=2*b; a=(m-1)//2
    verts=[(x,y) for x in range(m) for y in range(n)]
    idx={v:i for i,v in enumerate(verts)}
    N=len(verts); adj=[0]*N
    for (x,y),i in idx.items():
        for dx in (-a,a):
            j=idx[((x+dx)%m,(y+b)%n)]
            adj[i]|=1<<j
        # independent metric check against ALL other vertices
        for (z,w),j in idx.items():
            dist=min((z-x)%m,(x-z)%m)+min((w-y)%n,(y-w)%n)
            assert bool((adj[i]>>j)&1)==(dist==a+b)
    assert all(v.bit_count()==2 for v in adj)
    # Exactly b components, each an induced C_(2m)
    remain=set(range(N)); comps=[]
    while remain:
        todo=[next(iter(remain))]; seen={todo[0]};remain.remove(todo[0])
        for v in todo:
            for j in range(N):
                if (adj[v]>>j)&1 and j not in seen:
                    assert j in remain
                    seen.add(j);remain.remove(j);todo.append(j)
        comps.append(seen)
    assert len(comps)==b and all(len(c)==2*m for c in comps)

    q=2*(m//3)+1; d=q-1; B=b*q-1
    eps=1 if m%6==1 else -1
    targets={'oddrot':1,'oddref':eps**b,'evenrot':(-1)**b,'evenref':(-1)**(b//2)}

    def signed_trace(kind):
        if kind=='oddrot': f=lambda x,y:((x+1)%m,y)
        elif kind=='oddref': f=lambda x,y:((-x)%m,y)
        elif kind=='evenrot':f=lambda x,y:(x,(y+1)%n)
        elif kind=='evenref':f=lambda x,y:(x,(-y)%n)
        else:raise ValueError(kind)
        perm=[idx[f(x,y)] for x,y in verts]
        orbit_masks=[]; weights=[]; seen=set()
        for i in range(N):
            if i in seen:continue
            cyc=[];k=i
            while k not in seen:
                cyc.append(k);seen.add(k);k=perm[k]
            mask=sum(1<<v for v in cyc)
            if any(adj[v]&mask for v in cyc):continue
            orbit_masks.append(mask)
            # A cycle on len(cyc) vertices has permutation sign (-1)^(len-1).
            weights.append(-1) # (-1)^len * (-1)^(len-1)
        M=len(orbit_masks); blocks=[0]*M
        for i,sm in enumerate(orbit_masks):
            near=0
            for v in range(N):
                if (sm>>v)&1:near|=adj[v]
            for j,tm in enumerate(orbit_masks):
                if near&tm:blocks[i]|=1<<j
        assert not any((blocks[i]>>i)&1 for i in range(M))
        @lru_cache(None)
        def F(mask):
            if mask==0:return 1
            v=(mask&-mask).bit_length()-1
            return F(mask &~(1<<v))-F(mask&~((1<<v)|blocks[v]))
        reduced_lefschetz=-F((1<<M)-1)
        return (-1)**B * reduced_lefschetz
    got={k:signed_trace(k) for k in targets}
    assert got==targets,(m,b,got,targets)
    return N,len(comps),B,got

if __name__=='__main__':
    cases=[(5,2),(5,3),(5,4),(7,2),(7,3),(7,4),(11,2)]
    for m,b in cases:
        N,nc,B,tr=check(m,b)
        print(f'm={m}, b={b}, vertices={N}, components={nc}, top_degree={B}, signed_traces={tr}: PASS')
    print(f'ALL {len(cases)} CASES PASS')
