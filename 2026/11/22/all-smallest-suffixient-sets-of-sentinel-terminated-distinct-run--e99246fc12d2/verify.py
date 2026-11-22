#!/usr/bin/env python3
"""Finite independent checks of exact suffixient-set theorem.
Brute-force substring/right-context enumeration is independent of symbolic proof.
"""
from collections import defaultdict
from itertools import product
from math import prod


def brute_sre(t):
    follows=defaultdict(set)
    ends=defaultdict(list)
    follows['']=set(t)
    n=len(t)
    for i in range(n):
        for j in range(i+1,n+1):
            v=t[i:j]
            ends[v].append(j-1)
            if j<n:
                follows[v].add(t[j])
    exts={(u,x) for u,fs in follows.items() if len(fs)>=2 for x in fs}
    sre={e for e in exts if not any(v!=e[0] and x==e[1] and v.endswith(e[0]) for v,x in exts)}
    return sre,ends,exts


def expected_sre(rs,k):
    q=len(rs)
    p=''.join(str(i)*rs[i] for i in range(q))
    out={(str(i)*(rs[i]-1),str(i)) for i in range(q)}
    out|={(str(i)*(rs[i]-1),str(i+1)) for i in range(q-1)}
    out|={(p*(k-1),'0'),(p*(k-1),'$')}
    return out


def validate(rs,k):
    q=len(rs)
    p=''.join(str(i)*rs[i] for i in range(q))
    t=p*k+'$'
    sre,ends,exts=brute_sre(t)
    exp=expected_sre(rs,k)
    assert sre==exp,(rs,k,'SRE difference',sre^exp)
    assert len(sre)==2*q+1
    ec=[len(ends[u+x]) for (u,x) in sre]
    assert sorted(ec)==[1,1]+[k]*(2*q-1),(rs,k,ec)
    position_sets=[set(ends[u+x]) for u,x in sre]
    for i,a in enumerate(position_sets):
        for b in position_sets[i+1:]:
            assert a.isdisjoint(b),(rs,k,'overlap',a&b)
    assert prod(ec)==k**(2*q-1)
    # Additionally, a single arbitrary selected occurrence for each SRE covers all extensions.
    selection={next(iter(a)) for a in position_sets}
    assert all(any(t[:z+1].endswith(u+x) for z in selection) for u,x in exts)
    return len(exts)


def main():
    count=0; total_exts=0
    for q in range(2,5):
        for rs in product([2,3,4],repeat=q):
            for k in [2,3]:
                total_exts+=validate(rs,k);count+=1
    for q in [5,6]:
        for rs in [(2,)*q,(3,)*q,tuple(2+i%2 for i in range(q))]:
            for k in [2,3]:
                total_exts+=validate(rs,k);count+=1
    # Test ALL minimum-sized position sets directly, without SRE endpoint products.
    import itertools
    for rs,k in [((2,2),2),((2,2),3),((2,2,2),2),((2,2,2,2),2)]:
        t=''.join(str(i)*r for i,r in enumerate(rs))*k+'$'
        sre,ends,exts=brute_sre(t)
        count_min=0
        for subset in itertools.combinations(range(len(t)),2*len(rs)+1):
            positions=set(subset)
            if all(any(t[:z+1].endswith(u+x) for z in positions) for u,x in exts):
                count_min+=1
        assert count_min==k**(2*len(rs)-1),(rs,k,count_min)
        print('PASS: direct minimum-set enumeration q={}, k={}, count={}'.format(len(rs),k,count_min))
    print('PASS: {} independently enumerated parameter instances and {} right extensions'.format(count,total_exts))
    print('PASS: exact SRE lists, k-fold occurrences, pairwise-disjoint occurrence endpoint sets, and coverage')

if __name__=='__main__':main()
