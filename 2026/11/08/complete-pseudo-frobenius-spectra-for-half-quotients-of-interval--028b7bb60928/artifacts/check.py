#!/usr/bin/env python3
"""Exact checks for pseudo-Frobenius spectra of half-quotients of interval semigroups.

Uses two separately implemented paths: shortest residue graph for proposed
quotient generators, and direct coin reachability for the original semigroup.
No symbolic infinite theorem is claimed by finite checks.
"""
import heapq


def result(a,k):
    assert a%2==1 and 3<=k<=a-2
    r=(a-1)//2
    T=(a-3)//k
    blocks=[list(range(t*(a+k)//2+1, ((t+1)*a-1)//2+1)) for t in range(T+1)]
    gaps=[x for block in blocks for x in block]
    F=((T+1)*a-1)//2
    assert gaps[-1]==F
    pf=blocks[-1][:]
    if T>=1:
        if T%2: pf.append(blocks[-2][-1])
        elif k%2==0: pf.append(blocks[-2][0])
    pf.sort()
    genus=sum(r-(k*t+1)//2 for t in range(T+1))
    assert genus==len(gaps)
    return F, genus, gaps, pf


def apery_gaps(a,k):
    m=(a+1)//2
    h=(k-1)//2
    generators=list(range(m,m+h+1))+[a]+([a+k] if k%2==0 else [])
    dist=[10**40]*m
    dist[0]=0
    heap=[(0,0)]
    while heap:
        v,x=heapq.heappop(heap)
        if v!=dist[x]:continue
        for s in generators:
            nx=(x+s)%m
            nv=v+s
            if nv<dist[nx]:
                dist[nx]=nv
                heapq.heappush(heap,(nv,nx))
    F=max(dist)-m
    gaps=[n for n in range(F+1) if n<dist[n%m]]
    pf=[x for x in gaps if all(x+g>=dist[(x+g)%m] for g in generators)]
    return F,gaps,pf


def direct_coin_gaps(a,k,cutoff):
    # Independent dynamic program in the original semigroup.
    reach=bytearray(2*cutoff+1)
    reach[0]=1
    for n in range(1,len(reach)):
        reach[n]=int(any(n>=g and reach[n-g] for g in range(a,a+k+1)))
    return [n for n in range(cutoff+1) if not reach[2*n]]


def main():
    count=0
    pf_count=0
    for a in range(5,152,2):
        for k in range(3,a-1):
            F,g,gaps,pf=result(a,k)
            F2,gaps2,pf2=apery_gaps(a,k)
            assert (F,gaps,pf)==(F2,gaps2,pf2), (a,k,F,F2,pf,pf2)
            count+=1
            pf_count+=len(pf)
    examples=[(11,3),(13,3),(21,4),(21,5),(25,4),(29,7),(49,11),(101,17)]
    for a,k in examples:
        F,g,gaps,pf=result(a,k)
        assert direct_coin_gaps(a,k,F+max(a,k)+3)==gaps, (a,k)
        print(f'example a={a} k={k}: F={F} genus={g} type={len(pf)} PF={pf}')
    print(f'APERY_AND_PF_MATCH cases={count} pseudo_frobenius_occurrences={pf_count}')
    print(f'ORIGINAL_GENERATOR_DP_MATCH cases={len(examples)}')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
