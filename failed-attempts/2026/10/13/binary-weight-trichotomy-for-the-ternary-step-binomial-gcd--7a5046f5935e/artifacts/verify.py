#!/usr/bin/env python3
"""Exact finite transcription checks for a symbolic binary-weight theorem."""
from math import comb, gcd
from collections import Counter

def binary_weight(t):
    assert t>0
    return t.bit_count()

def predicted(n):
    assert n>=2
    w=binary_weight(3*n)
    assert w>=2
    return 2 if w==2 else (1 if w==3 else 0)

def count_2_valuation(x):
    assert x>0
    v=0
    while x%2==0:
        v+=1
        x//=2
    return v

def independent_binomial_gcd(n):
    g=0
    for k in range(1,n):
        g=gcd(g,comb(3*n,3*k))
    return count_2_valuation(g)

def min_binary_weight_formula(n):
    N=3*n
    return min(binary_weight(3*k)+binary_weight(N-3*k)-binary_weight(N)
               for k in range(1,n))

def constructed_witness(n):
    N=3*n
    bit_positions=[i for i in range(N.bit_length()) if (N>>i)&1]
    w=len(bit_positions)
    if w==2:
        i,j=bit_positions
        assert (j-i)%2==1
        if j-i==1:
            assert i>=1
            t=3*(1<<(i-1))
        else:
            assert j-i>=3
            t=(1<<i)+(1<<(j-2))
        expected=2
    elif w==3:
        i,j,k=bit_positions
        assert i%2==j%2==k%2
        t=(1<<i)+(1<<(j-1))
        expected=1
    else:
        even=[i for i in bit_positions if i%2==0]
        odd=[i for i in bit_positions if i%2==1]
        if even and odd:
            t=(1<<even[0])+(1<<odd[0])
        else:
            t=sum(1<<i for i in bit_positions[:3])
        expected=0
    assert 0<t<N and t%3==0
    s=N-t
    assert s>0 and s%3==0
    val=binary_weight(t)+binary_weight(s)-binary_weight(N)
    assert val==expected,(n,t,s,val,expected)
    return t,val

counts=Counter()
for n in range(2,1001):
    p=predicted(n)
    assert min_binary_weight_formula(n)==p,n
    t,w=constructed_witness(n)
    assert w==p,n
    if n<=200:
        assert independent_binomial_gcd(n)==p,n
    counts[p]+=1

assert counts=={0:925,1:40,2:34},counts
assert [predicted(n) for n in [2,5,7,8,91]]==[2,0,1,2,1]
print('VERIFY_OK all_n=2..1000 direct_gcd_n=2..200 '
      'symbolic_witnesses=999 binary_minima=999 counts_0_1_2=925,40,34 '
      'examples_2_5_7_8_91=2,0,1,2,1')
