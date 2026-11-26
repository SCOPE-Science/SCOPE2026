#!/usr/bin/env python3
"""Independent exhaustive finite checks for multi-burst deletion diversity."""
from collections import Counter
from itertools import product, combinations
from math import comb

def diversity(word, b):
    n = len(word)
    return len({word[:i] + word[i+b:] for i in range(n-b+1)})

def main():
    cases=0
    for q in (2,3):
        for n in range(3,8):
            lengths = list(range(1,n))
            hist = {b:Counter() for b in lengths}
            pair = {bc:0 for bc in combinations(lengths,2)}
            tri = {abc:0 for abc in combinations(lengths,3)}
            samples=q**n
            for word in product(range(q),repeat=n):
                ds = {}
                ws = {}
                for b in lengths:
                    d=diversity(word,b)
                    prediction=1+sum(word[i]!=word[i+b] for i in range(n-b))
                    assert d==prediction, (q,n,b,word,d,prediction)
                    ds[b]=d-1
                    ws[b]=q*ds[b]-(n-b)*(q-1)
                    hist[b][ds[b]]+=1
                for bc in pair: pair[bc]+=ws[bc[0]]*ws[bc[1]]
                for abc in tri: tri[abc]+=ws[abc[0]]*ws[abc[1]]*ws[abc[2]]
            for b in lengths:
                expected={j: comb(n-b,j)*(q-1)**j*q**b for j in range(n-b+1)}
                assert hist[b]==expected,('hist',q,n,b,hist[b],expected)
            for bc,value in pair.items(): assert value==0, ('cov',q,n,bc,value)
            for abc,value in tri.items():
                a,b,c=abc
                expected=(-2*(n-c)*(q-1)*samples) if a+b==c else 0
                assert value==expected, ('third',q,n,abc,value,expected)
            cases+=1
            print(f'OK q={q} n={n} words={samples} pairs={len(pair)} triples={len(tri)}')
    print('VERIFY_OK',cases,'complete parameter sets')

if __name__=='__main__':main()
