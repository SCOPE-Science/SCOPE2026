#!/usr/bin/env python3
"""Direct finite-field verification of radical-power ranks in layered incidence algebras.
Only integer prime fields are used in exhaustive tests; theorem applies to all finite fields.
"""
from itertools import product
from collections import Counter
from random import Random
from math import prod


def rank_mod(mat, q):
    a = [[x % q for x in row] for row in mat]
    if not a: return 0
    n = len(a[0]); r = 0
    for col in range(n):
        pivot = next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot] = a[pivot],a[r]
        inv = pow(a[r][col], -1, q)
        a[r] = [x*inv % q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                c = a[i][col]
                a[i] = [(x-c*y)%q for x,y in zip(a[i],a[r])]
        r += 1
        if r==len(a):break
    return r


def matmul(a,b,q):
    return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*b)] for row in a]


def q_binom(n,k,q):
    if k < 0 or k > n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    assert num%den==0
    return num//den


def n_rank(a,b,r,q):
    return q_binom(a,r,q)*prod(q**b-q**j for j in range(r))


def predicted_cover_counts(widths,q):
    counts={widths[0]:1}
    for cur,nxt in zip(widths[:-1],widths[1:]):
        tmp=Counter()
        for rank,v in counts.items():
            for s in range(min(rank,nxt)+1):
                # Given an existing product of rank r, the next cur-by-nxt factor
                # yields a uniform r-by-nxt matrix, with q^((cur-r)*nxt) lifts.
                tmp[s]+=v*q**((cur-rank)*nxt)*n_rank(rank,nxt,s,q)
        counts=dict(tmp)
    assert sum(counts.values()) == q**sum(a*b for a,b in zip(widths[:-1],widths[1:])),(widths,q,counts)
    return counts


def levels_and_entries(widths):
    levels=[[sum(widths[:i])+u for u in range(widths[i])] for i in range(len(widths))]
    edges=[(a,b,i,j) for i in range(len(widths)) for j in range(i+1,len(widths)) for a in levels[i] for b in levels[j]]
    return levels,edges


def raw_top_rank(widths,q,assign,edges):
    n=sum(widths); h=len(widths)
    a=[[0]*n for _ in range(n)]
    for (u,v,_,_),x in zip(edges,assign):a[u][v]=x
    power=a
    for _ in range(h-2):power=matmul(power,a,q)
    out=rank_mod(power,q)
    # Independently enforce that the top nonzero power has support only
    # between the first and last levels of the ordinal-sum poset.
    levels,_=levels_and_entries(widths)
    for i in range(n):
        for j in range(n):
            if i not in levels[0] or j not in levels[-1]:
                assert power[i][j]==0
    # Check nilpotence one step later directly.
    assert not any(x for row in matmul(power,a,q) for x in row)
    return out


def full_case(widths,q):
    levels,edges=levels_and_entries(widths); m=len(edges)
    expected=predicted_cover_counts(widths,q)
    far=sum(a*b for i,a in enumerate(widths) for j,b in enumerate(widths) if j>i+1)
    expected={r:v*q**far for r,v in expected.items()}
    actual=Counter()
    for vals in product(range(q),repeat=m):
        actual[raw_top_rank(widths,q,vals,edges)]+=1
    assert dict(actual)==expected,(widths,q,actual,expected)
    print('FULL',widths,'q',q,'total',q**m,'ranks',dict(sorted(actual.items())))


def cover_case(widths,q):
    levels,edges=levels_and_entries(widths)
    near=[e for e in edges if e[3]==e[2]+1]
    m=len(near);expected=predicted_cover_counts(widths,q)
    actual=Counter()
    for vals in product(range(q),repeat=m):
        actual[raw_top_rank(widths,q,vals,near)]+=1
    assert dict(actual)==expected,(widths,q,actual,expected)
    print('COVER',widths,'q',q,'total',q**m,'ranks',dict(sorted(actual.items())))


def sampled_cases(widths,q,howmany=512):
    rng=Random(20261104)
    levels,edges=levels_and_entries(widths)
    near=[e for e in edges if e[3]==e[2]+1]
    for _ in range(howmany):
        vals=[rng.randrange(q) for e in edges]
        all_rank=raw_top_rank(widths,q,vals,edges)
        cover_rank=raw_top_rank(widths,q,[v for v,e in zip(vals,edges) if e[3]==e[2]+1],near)
        assert all_rank == cover_rank
    print('SAMPLED_FAR_INDEPENDENCE',widths,'q',q,'trials',howmany)


def explicit_width_two(q,h):
    # Formula is exact using fractions, not float approximation.
    from fractions import Fraction
    c=Fraction(q*q-1,q*q)
    a=c*Fraction(q-1,q)
    L=h-1
    p2=a**L
    p1=Fraction(q+1,q)*(c**L-a**L)
    p0=1-p1-p2
    predicted=predicted_cover_counts((2,)*h,q)
    total=q**(4*L)
    assert all((total*x).denominator == 1 for x in (p0,p1,p2))
    assert [int(total*x) for x in (p0,p1,p2)]==[predicted.get(i,0) for i in range(3)]
    print('WIDTH_TWO_CLOSED',q,h,'probabilities',*[str(x) for x in (p0,p1,p2)])

if __name__=='__main__':
    for ws,q in [((1,1,1,1),2),((2,1,2),2),((2,2,2),2),((1,2,1,2),2),((1,2,1),3),((2,1,2),3)]:
        full_case(ws,q)
    for ws,q in [((2,2,2,2),2),((2,2,2),3),((2,1,2,1),3)]:cover_case(ws,q)
    for ws,q in [((2,2,2,2),2),((2,2,2,2),3),((1,3,2,2),3)]:sampled_cases(ws,q)
    for q in [2,3,5,7,11]:
        for h in range(2,12):explicit_width_two(q,h)
    print('LAYERED_INCIDENCE_RADICAL_POWER_CENSUS_PASS')
