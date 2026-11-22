#!/usr/bin/env python3
"""Exact verification of paired-chord deletion codes for at most four chords.

Standard-library only.  Chord endpoints are ordered integers 0,...,2m-1.
The sole channel event removes both ends of one matched pair and then
renumbers surviving endpoints increasingly.
"""
from functools import lru_cache

@lru_cache(None)
def recursive_matchings(n):
    if n == 0:
        return ((),)
    out = []
    for partner in range(1, n):
        remaining = tuple(i for i in range(1, n) if i != partner)
        for smaller in recursive_matchings(n-2):
            out.append(((0, partner),) + tuple((remaining[a], remaining[b]) for a,b in smaller))
    return tuple(out)

def independent_matchings(n):
    """Separate perfect-involution recurrence on arbitrary free positions."""
    out=[]
    def walk(free, pairs):
        if not free:
            out.append(tuple(sorted(pairs)))
            return
        a=free[0]
        for j in range(1,len(free)):
            walk(free[1:j]+free[j+1:],pairs+((a,free[j]),))
    walk(tuple(range(n)),())
    return tuple(sorted(out))

def direct_shadows(m):
    n=2*len(m)
    ans=set()
    for drop in m:
        remaining=[i for i in range(n) if i not in drop]
        rank={v:j for j,v in enumerate(remaining)}
        ans.add(tuple(sorted((rank[a],rank[b]) for a,b in m if (a,b)!=drop)))
    return ans

def insertion_shadows(m):
    """An independent test: delete each pair via a partner involution.

    For the deleted positions a,b the other endpoints c are mapped to
    c - [a<c] - [b<c].
    """
    n=2*len(m)
    partner=[-1]*n
    for a,b in m:partner[a]=b;partner[b]=a
    out=set()
    for a in range(n):
        b=partner[a]
        if a>b:continue
        mapped=[]
        for c in range(n):
            d=partner[c]
            if c<d and c not in (a,b):
                mapped.append((c-int(a<c)-int(b<c), d-int(a<d)-int(b<d)))
        out.add(tuple(mapped))
    return out

def construct(m):
    sources=recursive_matchings(2*m)
    assert len(sources)==__import__('math').factorial(2*m)//(2**m*__import__('math').factorial(m))
    assert sorted(sources)==list(independent_matchings(2*m))
    outputs=list(recursive_matchings(2*m-2))
    index={x:j for j,x in enumerate(outputs)}
    masks=[]
    for s in sources:
        shadows=direct_shadows(s)
        assert shadows==insertion_shadows(s)
        assert shadows and all(t in index for t in shadows)
        masks.append(sum(1<<index[t] for t in shadows))
    return sources,outputs,masks

# For m=4, all weights are halves; arrays below store twice the weight.
# Source indices use the ordering in recursive_matchings(8).
PRIMAL_2={0:2,17:2,31:2,52:2,65:2,87:1,88:1,94:1,104:2}
DUAL_2=(2,1,1,1,0,0,1,2,1,0,1,1,1,1,2)
# One explicit 7-word correcting code in the same ordering.
WITNESS=(0,23,50,52,78,87,104)

def subset_dp(masks,output_count):
    incidence=[[] for _ in range(output_count)]
    for i,mask in enumerate(masks):
        for bit in range(output_count):
            if mask & (1<<bit):incidence[bit].append(i)
    @lru_cache(None)
    def optimal(free):
        if not free:return (0,1)
        bit=(free & -free).bit_length()-1
        best,number=optimal(free ^ (1<<bit))
        for i in incidence[bit]:
            edge=masks[i]
            if edge & free != edge:continue
            possible,count=optimal(free ^ edge)
            possible+=1
            if possible>best:
                best,number=possible,count
            elif possible==best:
                number+=count
        return best,number
    return optimal((1<<output_count)-1)

def clique_count(masks):
    """An independent exact maximal-clique enumeration on 105 source vertices."""
    n=len(masks)
    compat=[0]*n
    for i in range(n):
        for j in range(i):
            if masks[i]&masks[j]==0:
                compat[i]|=1<<j
                compat[j]|=1<<i
    max_size=0
    num_max=0
    def bk(Rsize,P,X):
        nonlocal max_size,num_max
        if not (P|X):
            if Rsize>max_size:max_size,num_max=Rsize,1
            elif Rsize==max_size:num_max+=1
            return
        if Rsize+P.bit_count()<max_size:return
        PX=P|X
        # Standard Bron--Kerbosch pivot: any vertex in P union X.
        pivot=(PX&-PX).bit_length()-1
        candidates=P & ~compat[pivot]
        while candidates:
            bit=candidates&-candidates
            v=bit.bit_length()-1
            bk(Rsize+1,P&compat[v],X&compat[v])
            P^=bit
            X|=bit
            candidates^=bit
    bk(0,(1<<n)-1,0)
    return max_size,num_max

def reversal_stats(masks,output_count, sources):
    n=2*len(sources[0])
    lookup={x:i for i,x in enumerate(sources)}
    reflection=[]
    for s in sources:
        r=tuple(sorted((n-1-b,n-1-a) for a,b in s))
        reflection.append(lookup[r])
    incidence=[[] for _ in range(output_count)]
    for i,mask in enumerate(masks):
        for b in range(output_count):
            if mask&(1<<b):incidence[b].append(i)
    @lru_cache(None)
    def maximum(free):
        if not free:return 0
        b=(free & -free).bit_length()-1
        best=maximum(free ^ (1<<b))
        for i in incidence[b]:
            if masks[i]&free==masks[i]:best=max(best,1+maximum(free ^ masks[i]))
        return best
    full=(1<<output_count)-1
    max_size=maximum(full)
    count=0; fixed=0
    def walk(free,selected):
        nonlocal count,fixed
        if len(selected)==max_size:
            count+=1
            if set(reflection[i] for i in selected)==set(selected):fixed+=1
            return
        if not free:return
        b=(free&-free).bit_length()-1
        without=free ^ (1<<b)
        if len(selected)+maximum(without)>=max_size:walk(without,selected)
        for i in incidence[b]:
            if masks[i]&free==masks[i] and len(selected)+1+maximum(free^masks[i])>=max_size:
                walk(free^masks[i],selected+(i,))
    walk(full,())
    return count,fixed,(count+fixed)//2

def run():
    import json
    from pathlib import Path
    certificate_path = Path(__file__).with_name('CERTIFICATES.json')
    with certificate_path.open(encoding='utf-8') as f:
        certificate = json.load(f)
    assert certificate['witness_source_indices'] == list(WITNESS)
    assert certificate['dual_half_units'] == list(DUAL_2)
    assert dict(certificate['primal_half_units']) == PRIMAL_2
    expected_integer=(1,1,3,7)
    expected_codebook_counts=(1,3,1,278)
    for m in range(1,5):
        src,out,masks=construct(m)
        maximum,count=subset_dp(masks,len(out))
        assert maximum==expected_integer[m-1],(m,maximum)
        assert count==expected_codebook_counts[m-1],(m,count)
        assert clique_count(masks)==(maximum,count),(m,clique_count(masks))
        print('m=%s sources=%s outputs=%s maximum=%s codebooks=%s'%(m,len(src),len(out),maximum,count))
        if m==4:
            assert certificate['witness_pairs'] == [list(map(list,src[i])) for i in WITNESS]
            assert len(set(masks))==104
            assert len(PRIMAL_2)==9 and sum(PRIMAL_2.values())==15
            assert len(DUAL_2)==15 and sum(DUAL_2)==15
            # Primal nonnegativity and every output packing constraint.
            for bit in range(len(out)):
                assert sum(w for j,w in PRIMAL_2.items() if masks[j] & (1<<bit))<=2
            # Dual covers each source's entire distinct output set.
            for mask in masks:
                assert sum(DUAL_2[b] for b in range(len(out)) if mask&(1<<b))>=2
            used=0
            for j in WITNESS:
                assert used&masks[j]==0
                used |= masks[j]
            assert len(WITNESS)==7
            total,fixed,orbits=reversal_stats(masks,len(out),src)
            assert (total,fixed,orbits)==(278,136,207)
            print('m=4 fractional=15/2; reflection_fixed=136; reflection_orbits=207')
    print('VERIFY_OK')

if __name__=='__main__':run()
