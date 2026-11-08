#!/usr/bin/env python3
"""Brute-force check of maximal 2-plex classification in Hamming graphs.
Uses only the standard library. The structural generator is independent of the
subset-search predicate; it enumerates distant pairs, complete coordinate lines,
and axis-aligned rectangles.
"""
import itertools
import collections
from math import comb,prod


def check(dims,exhaustive=True):
    assert len(dims)>=2 and min(dims)>=2
    vs=list(itertools.product(*(range(x) for x in dims)))
    N=len(vs)
    dist=[[sum(a!=b for a,b in zip(v,w)) for w in vs] for v in vs]
    nonadj=[sum((1<<j) for j in range(N) if i!=j and dist[i][j]!=1) for i in range(N)]
    def two_plex(mask):
        x=mask
        while x:
            b=x&-x; x-=b
            i=b.bit_length()-1
            if (mask & nonadj[i]).bit_count()>1:return False
        return True
    def maximal(mask):
        if not two_plex(mask): return False
        for i in range(N):
            if not mask>>i&1 and two_plex(mask|(1<<i)):return False
        return True
    generated=set()
    for i in range(N):
        for j in range(i+1,N):
            if dist[i][j]>=3: generated.add((1<<i)|(1<<j))
    for axis in range(len(dims)):
        if dims[axis]>=3:
            for fixed in itertools.product(*(range(dims[j]) for j in range(len(dims)) if j!=axis)):
                tup=iter(fixed); core=[next(tup) if j!=axis else None for j in range(len(dims))]
                target=[idx for idx,v in enumerate(vs) if all(v[j]==core[j] for j in range(len(dims)) if j!=axis)]
                generated.add(sum(1<<i for i in target))
    for a,b in itertools.combinations(range(len(dims)),2):
        for x1,x2 in itertools.combinations(range(dims[a]),2):
            for y1,y2 in itertools.combinations(range(dims[b]),2):
                for fixed in itertools.product(*(range(dims[j]) for j in range(len(dims)) if j not in (a,b))):
                    it=iter(fixed); core=[next(it) if j not in(a,b) else None for j in range(len(dims))]
                    target=[idx for idx,v in enumerate(vs) if v[a] in (x1,x2) and v[b] in (y1,y2) and all(v[j]==core[j] for j in range(len(dims)) if j not in(a,b))]
                    assert len(target)==4
                    generated.add(sum(1<<i for i in target))
    pair_coefficient=N*sum(prod(dims[i]-1 for i in J) for s in range(3,len(dims)+1) for J in itertools.combinations(range(len(dims)),s))//2
    line_coefs=collections.Counter({})
    for i,x in enumerate(dims):
        if x>=3: line_coefs[x]+=N//x
    square_coefficient=sum(N//(dims[a]*dims[b])*comb(dims[a],2)*comb(dims[b],2) for a,b in itertools.combinations(range(len(dims)),2))
    expect=collections.Counter({2:pair_coefficient,4:square_coefficient})
    expect.update({})
    for k,num in line_coefs.items():expect[k]+=num
    actual=collections.Counter(x.bit_count() for x in generated)
    assert actual==+expect,(dims,actual,+expect)
    for mask in generated:assert maximal(mask),(dims,'predicted not maximal',mask)
    all_coeff=collections.Counter({0:1,1:N,2:comb(N,2),3:4*square_coefficient,4:square_coefficient})
    for i,dim in enumerate(dims):
        for r in range(3,dim+1):
            all_coeff[r]+=(N//dim)*comb(dim,r)
    subsets=0
    if exhaustive:
        observed_all=collections.Counter({0:1})
        for mask in range(1,1<<N):
            subsets+=1
            if two_plex(mask):observed_all[mask.bit_count()]+=1
            if maximal(mask):assert mask in generated,(dims,'unpredicted maximal',mask)
        assert observed_all==+all_coeff,(dims,observed_all,+all_coeff)
    return N,subsets,len(generated),dict(actual),dict(+all_coeff)


def main():
    cases=[(2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(2,2,2),(2,2,3),(2,2,4),(2,3,3),(2,2,2,2),(2,3,4),(3,3,3),(2,2,2,3)]
    total=total_s=total_m=0
    for dims in cases:
        exhaustive=prod(dims)<=18
        n,s,m,count,all_coeff=check(dims,exhaustive)
        total+=1;total_s+=s;total_m+=m
        print('case',dims,'N',n,'exhaustive',exhaustive,'subsets',s,'maximal',m,'maximal_polynomial',count,'all_plex_polynomial',all_coeff)
    print(f'VERIFY_OK instances={total} tested_subsets={total_s} generated_maximal={total_m} exact_families=PASS all_and_maximal_polynomials=PASS')
if __name__=='__main__':main()
