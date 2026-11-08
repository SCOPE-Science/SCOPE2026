#!/usr/bin/env python3
"""Exact finite-field and Fano-plane restrictions for quartics in characteristic two."""
from itertools import product
from collections import Counter

def gf8_mul(a,b):
    z=0
    while b:
        if b&1: z^=a
        b>>=1;a<<=1
        if a&8:a^=0b1011
    return z

def admissible(a,b,c,d,e,f):
    return all([a,b,c,a^b^d,b^c^e,a^c^f,(a^b^c^d^e^f)!=1])

# The full list of seven lines (over F2) and their cross coefficients.
# In order: x=0, y=0, z=0, x+y=0, y+z=0, x+z=0, x+y+z=0.
forms = ((0,1,0),(0,0,1),(1,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1))
# A form is applied to the vector (d,e,f).
byrank=Counter()
for d,e,f in product(range(8),repeat=3):
    h=sum(not (gf8_mul(aa,d)^gf8_mul(bb,e)^gf8_mul(cc,f)) for aa,bb,cc in forms)
    image={0,d,e,f,d^e,d^f,e^f,d^e^f}
    rank={1:0,2:1,4:2,8:3}[len(image)]
    assert h==(1<<(3-rank))-1
    byrank[rank]+=1
print('mixed_coefficients_rank_counts_GF8',dict(sorted(byrank.items())))
assert dict(byrank)=={0:1,1:49,2:294,3:168}

witnesses={}
for d,e,f in product(range(8),repeat=3):
    image={0,d,e,f,d^e,d^f,d^e,d^f,e^f,d^e^f}
    rank={1:0,2:1,4:2,8:3}[len(image)]
    if rank in witnesses:continue
    for a,b,c in product(range(1,8),repeat=3):
        if admissible(a,b,c,d,e,f):
            witnesses[rank]=(a,b,c,d,e,f)
            break
for rank in range(4):
    a,b,c,d,e,f=witnesses[rank]
    assert admissible(a,b,c,d,e,f)
    hh=[i for i,(aa,bb,cc) in enumerate(forms) if not (gf8_mul(aa,d)^gf8_mul(bb,e)^gf8_mul(cc,f))]
    assert len(hh)==(1<<(3-rank))-1
    if len(hh)==3:
        # The three bitangent coefficient vectors add to zero.
        bit_lines=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1),(1,1,1)]
        assert tuple(bit_lines[hh[0]][j]^bit_lines[hh[1]][j]^bit_lines[hh[2]][j] for j in range(3))==(0,0,0)
    print('rank',rank,'number_of_hyperflexes',len(hh),'witness_GF8',witnesses[rank],'hyperflex_line_indices',hh)
print('ALL_CHECKS_PASSED')
