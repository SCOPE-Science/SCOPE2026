#!/usr/bin/env python3
"""Exact finite checks for the central Delannoy 3-adic residue theorem."""
from math import comb

N=30000
values=[1,3]
a,b=1,3
for n in range(1,N):
    c=3*(2*n+1)*b-n*a
    assert c%(n+1)==0
    a,b=b,c//(n+1)
    values.append(b)
assert len(values)==N+1
for n in range(101):
    assert values[n]==sum(comb(n,j)**2*2**j for j in range(n+1))

for k in range(1,6):
    mod=3**k
    observed={v%mod for v in values}
    wanted={r for r in range(mod) if r%3 in (0,1)}
    assert observed==wanted, (k,len(observed),len(wanted),len(wanted-observed))

# Verify the normalized seed classes, which are proved via dominant Legendre coefficients.
for a in range(1,9):
    nplus=3**(a-1)
    nminus=3**a+1
    if nplus<=N:
        assert values[nplus]%(3**(a+1)) == 3**a
    if nminus<=N:
        assert values[nminus]%(3**(a+1)) == 2*3**a

# Modular block-separation lemma: D_(a+2*3^r)=D_a*D_(2*3^(k-1)) mod 3^k
block_tests=0
for k in range(1,6):
    mod=3**k
    c=values[2*3**(k-1)]%mod
    if k>=2:
        assert c%9==7
        assert pow(c,3**(k-1),mod)==1
        if k>=3:
            assert pow(c,3**(k-2),mod)!=1
    for r in range(k,8):
        shift=2*3**r
        for low in [0,1,2,3,4,7,11,19,28,40,59,99]:
            if shift+low>N or low>=3**(r-k+1): continue
            assert values[shift+low]%mod==values[low]*c%mod,(k,r,low)
            block_tests+=1

# Algebraic witness-products exhaust the claimed residue set at each tested level.
for k in range(1,7):
    mod=3**k
    c=values[2*3**(k-1)]%mod
    products={0}
    for base in [0]+[v for a in range(1,k) for v in (3**(a-1),3**a+1)]:
        current=1
        for j in range(3**(k-1)):
            products.add(values[base]*current%mod)
            current=current*c%mod
    wanted={r for r in range(mod) if r%3 in (0,1)}
    assert products==wanted,(k,len(products),len(wanted))
print('VERIFY_OK exact_recurrence_n=0..30000 direct_binomial=101 complete_residue_levels=1..5 '
      f'block_lemmas={block_tests} signed_seed_levels=1..8 generator_levels=1..6 '
      'constructive_residue_levels=1..6')
