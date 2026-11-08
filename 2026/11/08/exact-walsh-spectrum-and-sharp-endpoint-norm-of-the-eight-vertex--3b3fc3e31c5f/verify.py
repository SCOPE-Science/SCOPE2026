#!/usr/bin/env python3
"""Exact, standard-library Walsh certificate for the K8 perfect-matching spectrum."""
from array import array
from collections import Counter
from itertools import combinations
from fractions import Fraction

EXPECTED = {
    1:403200,3:259280,5:256032,7:289680,9:221340,
    11:175560,13:146160,15:122976,17:90720,19:33600,
    21:23800,23:25200,25:15750,27:16800,29:5040,
    33:6720,39:3430,41:210,43:840,45:336,
    57:420,75:56,105:2
}

def pairings(vertices):
    v=tuple(vertices)
    if not v:
        yield ()
    else:
        for j in range(1,len(v)):
            for tail in pairings(v[1:j]+v[j+1:]):
                yield ((v[0],v[j]),)+tail

def main():
    e={edge:i for i,edge in enumerate(combinations(range(1,8),2))}
    indices=[]
    for matching in pairings(range(8)):
        mask=0
        for a,b in matching:
            if a!=0:mask |= 1 << e[(a,b)]
        indices.append(mask)
    assert len(indices)==len(set(indices))==105
    n=1<<21
    a=array('i',[0])*n
    for i in indices:a[i]=1
    stride=1
    while stride<n:
        jump=stride*2
        for start in range(0,n,jump):
            for i in range(start,start+stride):
                x=a[i];y=a[i+stride]
                a[i]=x+y; a[i+stride]=x-y
        stride=jump
    hist=Counter(abs(v) for v in a)
    assert hist==EXPECTED,(hist,EXPECTED)
    assert sum(hist.values())==n
    second=sum(k*k*c for k,c in hist.items())
    fourth=sum(k**4*c for k,c in hist.items())
    assert second==105*n
    # A second fourth-moment calculation from pairwise matching XOR differences.
    differences=Counter(a^b for a in indices for b in indices)
    fourth_independent=n*sum(c*c for c in differences.values())
    assert fourth==fourth_independent==40425*n
    abs_sum=sum(k*c for k,c in hist.items())
    assert abs_sum==16854180
    endpoint=Fraction(abs_sum,n)
    assert endpoint==Fraction(4213545,524288)
    # Vertex switching creates 2^7 configurations for each star-normalized mask.
    assert n*128==1<<28
    print('ABSOLUTE_SPECTRUM',sorted(hist.items()))
    print('SPECTRAL_MOMENTS', second, fourth)
    print('SHARP_ENDPOINT_NORM', endpoint)
    print('K8_MATCHING_WALSH_CERTIFICATE_PASS')

if __name__=='__main__':main()
