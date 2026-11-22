#!/usr/bin/env python3
"""Independent finite-diagram checks for the tetrahedron-free pair-extension formula.
No external packages or network access required.
"""
import itertools
import math
from fractions import Fraction


def links_valid(mask,pairs,edges):
    pos={p:i for i,p in enumerate(pairs)}
    return all(not all((mask>>pos[p])&1 for p in itertools.combinations(e,2)) for e in edges)


def count_direct(n,edges):
    pairs=list(itertools.combinations(range(n),2))
    valid=[m for m in range(1<<len(pairs)) if links_valid(m,pairs,edges)]
    total=0
    by_size=[0]*(n+1)
    for S_bits in range(1<<n):
        pair_mask=sum(1<<i for i,(a,b) in enumerate(pairs) if (S_bits>>a)&1 and (S_bits>>b)&1)
        count=sum(1 for x in valid for y in valid if not (x&y&pair_mask))
        total+=count
        by_size[S_bits.bit_count()]+=count
    return total,by_size


def core_counts(k,edges):
    pairs=list(itertools.combinations(range(k),2))
    good=[m for m in range(1<<len(pairs)) if links_valid(m,pairs,edges)]
    out={}
    for S in range(1<<k):
        active=sum(1<<i for i,(a,b) in enumerate(pairs) if (S>>a)&1 and (S>>b)&1)
        out[S]=sum(1 for x in good for y in good if not (x&y&active))
    return out,len(good)


def count_formula(n,k,B):
    N=math.comb(n,2)
    K=math.comb(k,2)
    ans=0
    for T,bt in B.items():
        t=T.bit_count()
        for v in range(n-k+1):
            w=math.comb(t+v,2)-math.comb(t,2)
            ans+=bt*math.comb(n-k,v)*4**(N-K-w)*3**w
    return ans


def baseline(n):
    N=math.comb(n,2)
    return sum(math.comb(n,s)*3**math.comb(s,2)*4**(N-math.comb(s,2)) for s in range(n+1))


def correction(k,edges,good_count):
    pairs=list(itertools.combinations(range(k),2))
    pos={p:i for i,p in enumerate(pairs)}
    valid=[m for m in range(1<<len(pairs)) if links_valid(m,pairs,edges)]
    u=Fraction(good_count,1<<len(pairs))
    coeff=Fraction(0)
    pieces={}
    for p,idx in pos.items():
        g0=sum(1 for v in valid if not ((v>>idx)&1))
        g1=len(valid)-g0
        a=Fraction(g0,1<<(len(pairs)-1))
        b=Fraction(g1,1<<(len(pairs)-1))
        delta=(a-b)*(a+3*b)/12
        coeff+=delta
        pieces[p]=delta
    return u,coeff,pieces


def main():
    cases=[('single_triple',3,[(0,1,2)]),
           ('two_overlapping_triples',4,[(0,1,2),(0,1,3)]),
           ('three_triples',4,[(0,1,2),(0,1,3),(0,2,3)]),
           ('no_triples',4,[])]
    tested=0
    for name,k,edges in cases:
        B,good=core_counts(k,edges)
        f,c,pieces=correction(k,edges,good)
        assert B[0]==good*good
        assert (c>0)==bool(edges)
        assert all(x>=0 for x in pieces.values())
        for n in range(k,21):
            exact=count_formula(n,k,B)
            assert exact>=f*f*baseline(n)
            if edges: assert exact>f*f*baseline(n)
            if n>=max(3,k):
                z=baseline(n)
                N=math.comb(n,2)
                weights=[math.comb(n,j)*3**math.comb(j,2)*4**(N-math.comb(j,2)) for j in range(n+1)]
                pi2=Fraction(sum(weights[j]*j*(j-1) for j in range(n+1)),z*n*(n-1))
                pi3=Fraction(sum(weights[j]*j*(j-1)*(j-2) for j in range(n+1)),z*n*(n-1)*(n-2))
                residue=abs(Fraction(exact,z)-f*f-c*pi2)
                bound=(math.comb(k,2)*max(k-2,0)+math.comb(k,3))*pi3
                assert residue<=bound,(name,n,residue,bound)
            if n<=4:
                brute,by_size=count_direct(n,edges)
                assert exact==brute,(name,n,exact,brute)
                tested+=1
        print(name,'unary_valid',good,'f',f,'positive_coefficient',c,'pair_terms',pieces)
    for n in range(0,5):
        direct,_=count_direct(n,[])
        assert direct==baseline(n)
        tested+=1
    print('BRUTE_FORCE_CASES',tested)
    print('EXACT_FORMULA_AND_STRICT_INEQUALITY_OK')
    print('THIRD_MOMENT_REMAINDER_BOUND_OK')

if __name__=='__main__': main()
