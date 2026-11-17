#!/usr/bin/env python3
"""Exhaustive finite checks for robust clique complexes of rooted biclique bouquets."""
from collections import deque
from itertools import combinations
from math import prod


def graph(widths):
    """Return adjacency masks, central vertex, b vertices, and lists of leaves."""
    n = 1 + len(widths) + sum(widths)
    nbr = [0] * n
    center = 0
    b = list(range(1, len(widths)+1))
    leaves = []
    u = len(widths)+1
    for i,t in enumerate(widths):
        block = list(range(u,u+t)); u += t
        leaves.append(block)
        for x in block:
            for y in (center, b[i]):
                nbr[x] |= (1<<y)
                nbr[y] |= (1<<x)
    return nbr, b, leaves


def independent_numbers(adj):
    """Independent exact recurrence using graph adjacency, no petal formula."""
    n = len(adj)
    a = [0] * (1<<n)
    for s in range(1,1<<n):
        v = (s&-s).bit_length()-1
        a[s] = max(a[s^(1<<v)], 1 + a[s&~((1<<v)|adj[v])])
    return a


def matching(faces, b, leaves):
    rem = set(faces)
    pairs = []
    for v in [0]+[block[0] for block in leaves]:
        bit = 1<<v
        lower = [s for s in rem if not (s&bit) and (s|bit) in rem]
        for s in lower:
            rem.remove(s)
            rem.remove(s|bit)
            pairs.append((s,s|bit))
    return rem,pairs


def verify_acyclic(faces, pairs):
    """Kahn topological sort of the entire oriented Hasse diagram."""
    mate={lower:upper for lower,upper in pairs}
    indeg={s:0 for s in faces}
    # Orient unmatched incidence from coface to face, matched incidence in reverse.
    for s in faces:
        bits=s
        while bits:
            bit=bits&-bits; bits-=bit
            t=s^bit
            if mate.get(t)==s:
                indeg[s]+=1
            else:
                indeg[t]+=1
    q=deque(v for v,d in indeg.items() if d==0)
    count=0
    while q:
        s=q.popleft();count+=1
        upper=mate.get(s)
        if upper is not None:
            indeg[upper]-=1
            if indeg[upper]==0:q.append(upper)
        bits=s
        while bits:
            bit=bits&-bits;bits-=bit
            t=s^bit
            if mate.get(t)==s:continue
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert count==len(faces), ('cycle',count,len(faces))


def expected_critical(widths,k,b,leaves):
    if k-1>len(b):return set()
    result=set()
    for I in combinations(range(len(b)), k-1):
        possibilities=[block[1:] for i,block in enumerate(leaves) if i in I]
        import itertools
        for xs in itertools.product(*possibilities):
            mask=0
            for i in I:mask |= 1<<b[i]
            for x in xs:mask |= 1<<x
            result.add(mask)
    return result


def run(widths,k):
    adj,b,leaves=graph(widths)
    assert len(adj)<=18
    a=independent_numbers(adj)
    n=len(adj)
    for s in range(1<<n):
        count=0; eps=0
        for i,block in enumerate(leaves):
            v=sum(bool(s>>x&1) for x in block)
            e=int(bool(s>>b[i]&1)); eps+=e
            count+=max(v,e)
        theory=max(count,1+eps) if s&1 else count
        assert a[s]==theory,('independent number',widths,k,s,a[s],theory)
    faces={s for s in range(1<<n) if a[s]<k}
    critical,pairs=matching(faces,b,leaves)
    predicted=expected_critical(widths,k,b,leaves)
    assert critical==predicted, ('critical mismatch',widths,k,critical^predicted)
    assert len(critical)==sum(prod(widths[i]-1 for i in I) for I in combinations(range(len(widths)),k-1))
    assert all(s.bit_count()==2*(k-1) for s in critical)
    assert 2*len(pairs)+len(critical)==len(faces)
    verify_acyclic(faces,pairs)
    print(f'widths={widths}; k={k}; vertices={n}; faces={len(faces)}; pairs={len(pairs)}; critical={len(critical)}; dimension={2*k-3}; acyclic=YES')


if __name__=='__main__':
    cases = [
        ((2,),2), ((4,),2), ((5,),3),
        ((2,2),2), ((2,2),3), ((2,3),2), ((2,3),3), ((2,3),4),
        ((2,2,2),2), ((2,2,2),3), ((2,2,2),4),
        ((2,3,4),2), ((2,3,4),3), ((2,3,4),4), ((2,3,4),5),
        ((2,2,2,2),3), ((2,2,2,2),4), ((2,2,3,3),3), ((2,2,3,3),4),
        ((2,2,2,2,2),4), ((2,2,2,2,2),5),
    ]
    for w,k in cases:run(w,k)
    print('ROBUST_BICLIQUE_BOUQUET_ALL_EXACT_TESTS_PASS')

# Integral module formula, checked against signed Lefschetz traces.
def predicted_trace(widths, k, b, leaves, permutation):
    import itertools
    m=len(widths)
    sigma=[b.index(permutation[x]) for x in b]
    total=0
    for I_tuple in combinations(range(m), k-1):
        I=set(I_tuple)
        if {sigma[i] for i in I}!=I: continue
        unseen=set(I)
        term=1
        while unseen:
            i=min(unseen)
            cyc=[]; j=i
            while j not in cyc:
                cyc.append(j); unseen.remove(j); j=sigma[j]
            assert j==i
            fixed=0
            for leaf in leaves[i]:
                x=leaf
                for _ in cyc:x=permutation[x]
                fixed += (x==leaf)
            term *= fixed-1
        total+=term
    return total


def lefschetz_trace(widths,k,permutation):
    adj,b,leaves=graph(widths)
    alphas=independent_numbers(adj)
    value=0
    for s,alpha in enumerate(alphas):
        if alpha>=k:continue
        support=[v for v in range(len(adj)) if s>>v&1]
        images=[permutation[v] for v in support]
        if sorted(images)!=support:continue
        inversions=sum(images[x]>images[y] for x in range(len(images)) for y in range(x+1,len(images)))
        value+=(-1)**(len(support)-1+inversions)
    return value*(-1)**(2*k-3)


def trace_checks():
    for w,k in [((2,2),3),((3,3),3),((2,2,2),3),((2,2,2),4),((2,3,4),3),((2,3,4),4),((2,2,3,3),4)]:
        _,b,leaf=graph(w)
        n=1+len(b)+sum(w)
        perms=[]
        p=list(range(n));perms.append(('identity',p))
        p=list(range(n));p[leaf[0][0]],p[leaf[0][1]]=p[leaf[0][1]],p[leaf[0][0]]
        perms.append(('leaf_transposition',p))
        if w[0]==w[1]:
            p=list(range(n));p[b[0]],p[b[1]]=p[b[1]],p[b[0]]
            for u,v in zip(leaf[0],leaf[1]):p[u],p[v]=p[v],p[u]
            perms.append(('block_transposition',p))
            q=p.copy();q[leaf[0][0]],q[leaf[0][1]]=q[leaf[0][1]],q[leaf[0][0]]
            # q might not be automorphism if the leaf cycle mapping isn't bijective? It is.
            perms.append(('block_and_leaf',q))
        for label,p in perms:
            pred=predicted_trace(w,k,b,leaf,p)
            actual=lefschetz_trace(w,k,p)
            assert pred==actual, (w,k,label,pred,actual)
            print('character',w,k,label,pred,'LEFSCHETZ_MATCH')

if __name__=='__main__':
    trace_checks()
    print('EQUIVARIANT_HOMOLOGY_CHARACTER_TESTS_PASS')
