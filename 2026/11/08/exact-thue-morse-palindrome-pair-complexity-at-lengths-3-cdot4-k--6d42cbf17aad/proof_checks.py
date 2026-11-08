#!/usr/bin/env python3
"""Finite local identities used in an all-length theorem on palindrome pairs."""
from collections import Counter
from itertools import product

B = {'0':'0110', '1':'1001'}
BAD = {('0', 1):'1110', ('1', 1):'0001',
       ('0', 2):'1010', ('1', 2):'0101',
       ('0', 3):'1000', ('1', 3):'0111'}

def spectrum(w, k=6):
    return Counter(''.join(w[(i+j)%len(w)] for j in range(k))
                   for i in range(len(w)))

def asymmetry(w, k=6):
    z=spectrum(w,k)
    return sum(abs(z[s]-z[s[::-1]]) for s in
               map(''.join, product('01',repeat=k)))//2

# The adjacent-block local table measures the 6-factor reversal
# discrepancy of a circle with one anomalous 4-block.
table={}
for key,c in BAD.items():
    table[key]=[asymmetry(B[left]+c+B[right])
                for left,right in product('01',repeat=2)]
    assert all(v>0 for v in table[key])
print('six-factor local discrepancy table', table)

# For any cyclic block string with at least four good B-blocks,
# replacing the bad block by a good block changes only six-factors
# touching the bad block; two neighbors on each side suffice. All
# 16 binary choices of these four neighbors are checked exactly.
five_block_table={}
for key,c in BAD.items():
    scores=[]
    for l2,l1,r1,r2 in product('01',repeat=4):
        scores.append(asymmetry(B[l2]+B[l1]+c+B[r1]+B[r2]))
    assert min(scores)>0
    five_block_table[key]=[min(scores), max(scores)]
print('full five-block local bounds',five_block_table)

# Every binary cyclic word has a reversal-invariant 3-factor spectrum.
# A 6-factor in its 4-uniform palindromic image reads at most three
# consecutive source symbols, proving symmetry for arbitrary lengths.
for n in range(1,10):
    for letters in product('01',repeat=n):
        x=''.join(B[c] for c in letters)
        assert asymmetry(x)==0
print('good-block six-factor spectrum checked through nine blocks')

# The only extra block phase for a cyclic B-image is offset two,
# and it occurs only when all input symbols are equal.
for n in range(2,10):
    for v in product('01',repeat=n):
        x=''.join(B[c] for c in v)
        shifts=[s for s in range(1,4)
                if all((x+x)[s+4*j:s+4*j+4] in B.values() for j in range(n))]
        assert shifts == ([2] if len(set(v))==1 else [])
print('block phase uniqueness verified')

# Independent brute-force stress test of the spliced-block lemma.
for n in range(2,11):
    for v in product('01', repeat=n+1):
        if v[0]==v[-1]: continue
        x=''.join(B[c] for c in v)
        for r in (1,2,3):
            z=x[r:r+4*n]
            assert asymmetry(z)>0
print('all misaligned unequal-endpoint windows checked through length 40')
