#!/usr/bin/env python3
"""Reproducibility checks for the weight-two deletion-code theorem.

Requires Python 3.10+ standard library only. Run: python3 verify.py
"""
from itertools import combinations


def deletion_set(word):
    return {word[:k] + word[k+1:] for k in range(len(word))}


def construct(n):
    assert n >= 2
    pairs = [(i, i+1) for i in range(0,n-1,2)]
    pairs += [(4*k+1, 4*k+4) for k in range((n-1)//4)]
    return pairs


def word(n,pair):
    i,j=pair
    return ''.join('1' if t==i or t==j else '0' for t in range(n))


def optimum(n):
    return (3*n-2)//4


def maximum_independent_set(n):
    pairs=list(combinations(range(n),2))
    sh=[deletion_set(word(n,p)) for p in pairs]
    m=len(pairs); allbits=(1<<m)-1
    compatible=[0]*m
    for i in range(m):
        for j in range(m):
            if i!=j and sh[i].isdisjoint(sh[j]):
                compatible[i]|=1<<j
    best=0

    def bound_coloring(p):
        order=[]; col=[]; c=0; rest=p
        while rest:
            c+=1; candidates=rest
            while candidates:
                bit=candidates & -candidates; v=bit.bit_length()-1
                order.append(v); col.append(c)
                rest &= ~bit
                candidates &= ~(bit|compatible[v])
        return order,col

    def expand(p,size):
        nonlocal best
        if not p:
            if size>best:best=size
            return
        order, cols=bound_coloring(p)
        for z in range(len(order)-1,-1,-1):
            if size+cols[z]<=best:return
            v=order[z]
            expand(p & compatible[v],size+1)
            p &= ~(1<<v)
    expand(allbits,0)
    return best


def main():
    max_constructor=120
    for n in range(2,max_constructor+1):
        pairs=construct(n)
        assert len(pairs)==optimum(n),(n,'count')
        seen={}
        for pair in pairs:
            s=deletion_set(word(n,pair))
            for output in s:
                assert output not in seen,(n,pair,seen.get(output),output)
                seen[output]=pair
    values=[]
    for n in range(2,13):
        val=maximum_independent_set(n)
        assert val==optimum(n),(n,val,optimum(n))
        values.append(val)
    print('VERIFY_OK construction_lengths=2..120 exact_maximum_lengths=2..12')
    print('exact_maxima_n2_to_n12='+','.join(map(str,values)))

if __name__=='__main__': main()
