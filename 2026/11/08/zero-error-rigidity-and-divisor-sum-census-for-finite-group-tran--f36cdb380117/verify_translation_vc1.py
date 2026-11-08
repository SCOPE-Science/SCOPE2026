#!/usr/bin/env python3
"""Independent finite checks for low-VC translation families over cyclic groups."""
from itertools import combinations

def count_divisor_sum(n):
    return sum(d for d in range(1,n+1) if n%d == 0)

def coset_form(A,n):
    G=set(range(n))
    if not A or A==G:
        return True
    for index in range(2,n+1):
        if n%index:
            continue
        for residue in range(index):
            C={i for i in G if i%index==residue}
            if A==C or A==G-C:
                return True
    return False

def translates(A,n):
    return [frozenset((x+t)%n for x in A) for t in range(n)]

def directly_shattered_pairs(A,n):
    C=translates(A,n)
    return {frozenset((x,y)) for x,y in combinations(range(n),2)
            if len({frozenset(H.intersection((x,y))) for H in C})==4}

def autocorr_pairs(A,n):
    G=set(range(n)); B=G-A
    periods={d for d in G if {(x+d)%n for x in A}==A}
    distances={d for d in range(1,n)
               if d not in periods
               and any((x+d)%n in A for x in A)
               and any((x+d)%n in B for x in B)}
    return len(distances)*n//2

def check_elementary_abelian():
    for dimension in (2,3):
        G=list(range(1<<dimension)); n=len(G)
        plus=lambda x,y:x^y
        subgroups=[]
        for mask in range(1,1<<n):
            H={x for x in G if mask>>x&1}
            if 0 not in H or any((a^b) not in H for a in H for b in H):
                continue
            subgroups.append(H)
        def predicted(A):
            if not A or len(A)==n:return True
            for H in subgroups:
                if len(H)==n:continue
                for t in G:
                    C={t^h for h in H}
                    if A==C or A==set(G)-C:
                        return True
            return False
        matched=0
        for mask in range(1<<n):
            A={i for i in G if mask>>i&1}
            orbit=[{x^t for x in A} for t in G]
            shattered=any(len({tuple(sorted(H.intersection({i,j}))) for H in orbit})==4
                          for i,j in combinations(G,2))
            assert (not shattered)==predicted(A),(dimension,mask)
            matched+=1
        print(f'elementary_abelian_rank={dimension} masks={matched} PASS')

def main():
    checks=0
    for n in range(1,14):
        passing=0
        for mask in range(1<<n):
            A={j for j in range(n) if mask>>j&1}
            expected=coset_form(A,n)
            from_autocorr=(autocorr_pairs(A,n)==0)
            assert expected==from_autocorr,(n,mask,'classification')
            if n<=10:
                direct=directly_shattered_pairs(A,n)
                assert len(direct)==autocorr_pairs(A,n),(n,mask,'pair profile')
                assert (not direct)==expected,(n,mask,'direct traces')
            passing += expected
            checks+=1
        predicted=2*count_divisor_sum(n)-2*(n%2==0)
        assert passing==predicted,(n,passing,predicted)
        print(f'n={n:2d} classified={passing:3d} predicted={predicted:3d}')
    check_elementary_abelian()
    print(f'ALL_LOW_VC_TRANSLATION_CHECKS_PASS masks={checks} n=1..13 direct_n=1..10')

if __name__=='__main__':
    main()
