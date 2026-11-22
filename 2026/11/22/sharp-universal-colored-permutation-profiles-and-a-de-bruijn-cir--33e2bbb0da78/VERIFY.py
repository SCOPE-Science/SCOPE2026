#!/usr/bin/env python3
"""Independent finite checks for universal one-point orbit profiles of colored permutations.
No external dependencies. Run: python3 verify_colored_permutation.py
"""
from itertools import product, permutations
from collections import Counter
from math import factorial, gcd


def necklace_rep(word):
    return min(tuple(word[i:])+tuple(word[:i]) for i in range(len(word)))


def necklaces(q, c):
    return {necklace_rep(x) for x in product(range(q), repeat=c)}


def necklace_count_formula(q, c):
    return sum(q ** gcd(i,c) for i in range(c)) // c


def debruijn_data(q,d):
    verts=list(product(range(q), repeat=d))
    arcs=list(product(range(q), repeat=d+1))
    incoming={v:[] for v in verts}
    outgoing={v:[] for v in verts}
    for j,a in enumerate(arcs):
        outgoing[a[:-1]].append(j)
        incoming[a[1:]].append(j)
    return verts, arcs, incoming, outgoing


def count_transition_systems(q,d):
    verts,arcs,inc,out=debruijn_data(q,d)
    local=[list(permutations(out[v])) for v in verts]
    hist=Counter();passing=0
    for permset in product(*local):
        next_arc=[-1]*len(arcs)
        for v,arr in zip(verts,permset):
            for a,b in zip(inc[v],arr):
                next_arc[a]=b
        seen=set(); lengths=[]
        for i in range(len(arcs)):
            if i in seen:continue
            j=i; length=0
            while j not in seen:
                seen.add(j);length+=1;j=next_arc[j]
            assert j==i
            lengths.append(length)
        if min(lengths)>d:
            passing+=1
            hist[tuple(sorted(lengths))]+=1
    return passing,hist


def short_cycles(q,d):
    _,arcs,inc,out=debruijn_data(q,d)
    aid={a:i for i,a in enumerate(arcs)}
    result=[]
    for c in range(1,d+1):
        for w in sorted(necklaces(q,c)):
            # The primitive period must be precisely c.
            if any(c%p==0 and w==w[:p]*(c//p) for p in range(1,c)):
                continue
            edges=[]
            for k in range(c):
                segment=tuple(w[(k+j)%c] for j in range(d+1))
                edges.append(aid[segment])
            assert len(edges)==len(set(edges))
            result.append(tuple(edges))
    return result


def count_via_inclusion_exclusion(q,d):
    verts,arcs,inc,out=debruijn_data(q,d)
    vindex={v:i for i,v in enumerate(verts)}
    allcycles=short_cycles(q,d)
    affected=[]
    for cy in allcycles:
        counts=Counter(vindex[arcs[e][1:]] for e in cy)
        affected.append(counts)
    total=0
    def visit(j, used, counts, sign):
        nonlocal total
        if j==len(allcycles):
            weight=sign
            for n in counts:weight*=factorial(q-n)
            total+=weight
            return
        visit(j+1,used,counts,sign)
        cy=allcycles[j]
        if not any(e in used for e in cy):
            nextcounts=counts[:]
            for v,num in affected[j].items():nextcounts[v]+=num
            assert all(k<=q for k in nextcounts)
            visit(j+1, used | set(cy), nextcounts, -sign)
    visit(0,set(),[0]*len(verts),1)
    return total,len(allcycles)


def one_type(perm,col,x,d):
    seq=[x]
    for i in range(d):seq.append(perm[seq[-1]])
    return (tuple(col[y] for y in seq), tuple(int(seq[i]==seq[j]) for i in range(d+1) for j in range(i+1,d+1)))


def brute_minimal_q2_d1():
    q=2;d=1
    universe={(w,eq) for w in product(range(q),repeat=2) for eq in [(0,)]}
    universe|={( (z,z),(1,)) for z in range(q)}
    assert len(universe)==6
    for n in range(1,7):
        winners=0
        for perm in permutations(range(n)):
            for col in product(range(q),repeat=n):
                types={one_type(perm,col,x,d) for x in range(n)}
                if types==universe:winners+=1
        if n<6:assert winners==0,(n,winners)
        else:assert winners>0
    return winners


def direct_isomorphism_census_q2_d2():
    # Enumerate arbitrary multisets of long colored cycles without using a
    # de Bruijn transition matching; all possible partitions of 8 into parts >=3.
    target=set(product(range(2),repeat=3))
    words={n: sorted(necklaces(2,n)) for n in (3,4,5,8)}
    def windows(w):
        n=len(w)
        return {tuple(w[(i+j)%n] for j in range(3)) for i in range(n)}
    survivors=[]
    for w in words[8]:
        if windows(w)==target:survivors.append((w,))
    for a in words[3]:
        for b in words[5]:
            if windows(a) | windows(b)==target:survivors.append((a,b))
    for i,a in enumerate(words[4]):
        for b in words[4][i:]:
            if windows(a) | windows(b)==target:survivors.append((a,b))
    assert len(survivors)==3, survivors
    return survivors


def main():
    checks=0
    for q in (2,3,4):
        for c in range(1,7):
            assert len(necklaces(q,c))==necklace_count_formula(q,c)
            checks+=1
    expected={(2,1):1,(2,2):3,(2,3):40,(2,4):7749,(3,1):64}
    for (q,d),value in expected.items():
        via_matching,hist=count_transition_systems(q,d)
        via_ie,short_n=count_via_inclusion_exclusion(q,d)
        assert via_matching==via_ie==value,(q,d,via_matching,via_ie,value)
        # At least one optimal realization has one long de Bruijn cycle.
        assert any(k==(q**(d+1),) for k in hist)
        checks+=1
        m=q**(d+1)+sum(c*necklace_count_formula(q,c) for c in range(1,d+1))
        t=q**(d+1)+sum(q**c for c in range(1,d+1))
        print(f'q={q} d={d}: min={m} types={t} extremal_isotypes={value} short_cycles={short_n}')
    assert brute_minimal_q2_d1()>0
    assert len(direct_isomorphism_census_q2_d2())==3
    checks+=2
    print('VERIFY_OK',checks)


if __name__=='__main__':main()
