#!/usr/bin/env python3
"""Exact finite-field verification of the second Cartier-rank formula.

For y^(2r+1)=sum_{a=0}^{log2(r)} x^(2^a), in characteristic two,
compute Cartier on the holomorphic differential monomial basis.
Binary columns are represented as arbitrary-precision integers; the
rank computation uses exact Gaussian elimination over GF(2).
The theoretical assertion for all r=2^e, e>=2, is proved separately.
"""

def basis(r):
    top = 2*r*(r-1)-2
    return [(i,j) for j in range(2*r-2) for i in range(r)
            if (2*r+1)*i+r*j <= top]


def cterms(i,j,r):
    if i % 2 == 0 and j % 2 == 0:
        return []
    if i % 2 == 0:
        return [(i//2,(j-1)//2)]
    if j % 2 == 0:
        return [((i-1)//2,r+j//2)]
    return [((i-1)//2 + (1 << a),(j-1)//2)
            for a in range(r.bit_length()-1)]


def rank(cols):
    piv={}
    for value in cols:
        while value:
            leading = value.bit_length()-1
            if leading not in piv:
                piv[leading] = value
                break
            value ^= piv[leading]
    return len(piv)


def apply(cols, bitfield):
    result=0
    while bitfield:
        low = bitfield & -bitfield
        result ^= cols[low.bit_length()-1]
        bitfield ^= low
    return result


def verify(q):
    assert q >=8 and (q & (q-1))==0
    r=q//2
    b=basis(r)
    assert len(b)==r*(r-1), ('genus',q,len(b))
    ids={b_i:i for i,b_i in enumerate(b)}
    assert len(ids)==len(b)
    cols=[]
    for v in b:
        col=0
        for t in cterms(*v,r):
            assert t in ids, (q,v,t)
            col ^= 1 << ids[t]
        cols.append(col)
    first=rank(cols)
    assert first == 3*r*r//4-r, ('Cartier rank',q,first)
    squared=[apply(cols,c) for c in cols]
    second=rank(squared)
    expect=9*r*r//16-5*r//4
    assert second==expect, ('Cartier squared rank',q,second,expect)
    print('q=%d genus=%d rank_C=%d rank_C2=%d formula=%d verified' %
          (q,len(b),first,second,expect))

if __name__ == '__main__':
    for q in [8,16,32,64]:
        verify(q)
