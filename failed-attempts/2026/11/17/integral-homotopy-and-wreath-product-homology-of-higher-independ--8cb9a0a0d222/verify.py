#!/usr/bin/env python3
"""Exact finite checks of higher-independence complexes of windmill graphs.

The infinite-family statements have independent mathematical proofs; this
script checks complete small instances and sample/full symmetry characters.
Python 3 standard library only.
"""
from itertools import product, permutations
from math import comb


def faces_and_sizes(n,q,r):
    N=n*q
    dims={}
    masks=[]
    for mask in range(1 << (N+1)):
        center=(mask>>N)&1
        leaf_mask=mask & ((1<<N)-1)
        if center:
            valid=leaf_mask.bit_count() <= r-1
        else:
            valid=all(((leaf_mask>>(i*q)) & ((1<<q)-1)).bit_count() <= r
                      for i in range(n))
        if valid:
            masks.append(mask)
            d=mask.bit_count()-1
            dims.setdefault(d,[]).append(mask)
    return masks,dims


def graph_membership_check(n,q,r,faces):
    # Independently test all 2^(nq+1) subsets using graph adjacency/BFS,
    # rather than the blade-cardinality characterization.
    N=n*q
    adj=[]
    for v in range(N+1):
        if v==N:
            adj.append(set(range(N)))
        else:
            adj.append(({N}|{w for w in range((v//q)*q,((v//q)+1)*q) if w!=v}))
    reference=set(faces)
    for mask in range(1<<(N+1)):
        remaining={j for j in range(N+1) if mask>>j&1}
        ok=True
        while remaining:
            start=next(iter(remaining));stack=[start];remaining.remove(start)
            count=0
            while stack:
                v=stack.pop();count+=1
                neighbors=adj[v]&remaining
                remaining.difference_update(neighbors);stack.extend(neighbors)
            if count>r:ok=False
        assert (mask in reference)==ok,(n,q,r,mask)
    return 1<<(N+1)


def mod2_rank(columns):
    pivots={}
    for col in columns:
        v=col
        while v:
            i=v.bit_length()-1
            if i in pivots:
                v ^= pivots[i]
            else:
                pivots[i]=v
                break
    return len(pivots)


def homology_mod2(dims):
    dmax=max(dims)
    ranks={}
    # The reduced boundary in dimension 0 maps every vertex to the empty simplex.
    for d in range(0,dmax+1):
        rows={mask:i for i,mask in enumerate(dims.get(d-1,[]))}
        cols=[]
        for mask in dims.get(d,[]):
            v=0
            m=mask
            while m:
                b=m & (-m)
                v ^= 1<<rows[mask^b]
                m-=b
            cols.append(v)
        ranks[d]=mod2_rank(cols)
    bettis={}
    for d in range(0,dmax+1):
        k=len(dims.get(d,[]))-ranks[d]-ranks.get(d+1,0)
        if k: bettis[d]=k
    return bettis


def exterior_aug_character(p,k):
    """Trace of ∧^k(ker(sum: Q^n→Q)) for a permutation p."""
    N=len(p)
    assert sorted(p)==list(range(N))
    visited=set(); coef=[1]+[0]*N
    for s in range(N):
        if s in visited:continue
        x=s;l=0
        while x not in visited:
            visited.add(x);l+=1;x=p[x]
        # factor 1-(-t)^l = 1+(-1)^(l+1)t^l
        f=(-1)**(l+1)
        for j in range(N-l,-1,-1):
            coef[j+l]+=f*coef[j]
    out=[0]*(N)
    for j in range(N):
        out[j]=coef[j]-(out[j-1] if j>0 else 0)
    return out[k] if 0<=k<N else 0


def top_character(p,n,q,r):
    # p maps q-element blocks to q-element blocks.
    block_next=[]
    for i in range(n):
        b=p[i*q]//q
        assert all(p[i*q+a]//q==b for a in range(q))
        block_next.append(b)
    visited=set(); ans=1
    for start in range(n):
        if start in visited:continue
        cyc=[];a=start
        while a not in visited:
            visited.add(a);cyc.append(a);a=block_next[a]
        d=len(cyc)
        internal=[]
        for a in range(q):
            x=start*q+a
            for _ in range(d):x=p[x]
            assert x//q==start
            internal.append(x%q)
        ans *= ((-1)**(r*(d-1)))*exterior_aug_character(internal,r)
    return ans


def sign_restriction(mask,p):
    chosen=[i for i in range(len(p)) if mask>>i &1]
    images=[p[i] for i in chosen]
    assert set(chosen)==set(images)
    inversions=sum(images[i]>images[j] for i in range(len(images))
                   for j in range(i+1,len(images)))
    return -1 if inversions%2 else 1


def reduced_lefschetz(masks,p):
    res=0
    for mask in masks:
        if all(((mask>>i)&1)==((mask>>p[i])&1) for i in range(len(p))):
            res += (-1 if mask.bit_count()%2==0 else 1)*sign_restriction(mask,p)
    return res


def sample_actions(n,q,full=False):
    bperms=list(permutations(range(n)))
    iperms=list(permutations(range(q)))
    group_size=len(bperms)*len(iperms)**n
    if full:
        iterator=product(bperms,product(iperms,repeat=n))
    else:
        # Deterministic sample containing identity, several swaps and mixed cycles
        tests=[]
        for idx in range(56):
            bp=bperms[(idx*37)%len(bperms)]
            pp=[iperms[((idx+3*i)*11+i*5)%len(iperms)] for i in range(n)]
            tests.append((bp,pp))
        tests.insert(0,(tuple(range(n)),[tuple(range(q))]*n))
        iterator=tests
    for bp,pp in iterator:
        p=[0]*(n*q)
        for i in range(n):
            for a in range(q):p[i*q+a]=bp[i]*q+pp[i][a]
        yield p+[n*q]


def check_case(n,q,r,full=False):
    N=n*q
    masks,dims=faces_and_sizes(n,q,r)
    checked=graph_membership_check(n,q,r,masks)
    got=homology_mod2(dims)
    want={r-1:comb(N-1,r-1)}
    if r<q:
        want[n*r-1]=comb(q-1,r)**n
    assert got==want, (n,q,r,got,want)
    tests=0
    for p in sample_actions(n,q,full):
        low=exterior_aug_character(p[:N],r-1)
        high=top_character(p[:N],n,q,r) if r<q else 0
        predicted=(-1)**(r-1)*low + ((-1)**(n*r-1))*high
        actual=reduced_lefschetz(masks,p)
        assert actual==predicted,(n,q,r,p,actual,predicted)
        tests+=1
    print(f'n={n}, q={q}, r={r}: faces={len(masks)}, all_subsets={checked}, mod2={got}, action_checks={tests}, PASSED')
    return len(masks),tests


def verify_full_invariant_averages(n,q,r):
    # Exact rational invariant dimensions are averages of integral characters.
    N=n*q
    sl=0;sh=0;count=0
    for p in sample_actions(n,q,True):
        sl += exterior_aug_character(p[:N],r-1)
        if r<q: sh += top_character(p[:N],n,q,r)
        count+=1
    assert sl==0 and sh==0,(n,q,r,sl,sh)
    print(f'n={n}, q={q}, r={r}: full_group_elements={count}, '
          'low_high_invariant_character_sums=(0,0), PASSED')
    return count


def main():
    configs=[(2,3,2,True),(2,4,2,False),(2,4,3,False),
             (3,3,2,False),(2,5,3,False),(2,5,4,False),
             (2,3,3,False),(2,3,5,False),(3,3,4,False)]
    counts=[check_case(*x) for x in configs]
    print('TOTAL_CASES',len(configs),'TOTAL_FACES',sum(x[0] for x in counts),
          'TOTAL_ACTION_CHECKS',sum(x[1] for x in counts))
    sym=sum(verify_full_invariant_averages(*x) for x in [(2,3,2),(2,4,3),(3,3,2)])
    print('TOTAL_FULL_GROUP_CHARACTER_TESTS',sym)
    print('WINDMILL_HIGHER_INDEPENDENCE_FINITE_CHECKS_PASS')

if __name__=='__main__': main()
