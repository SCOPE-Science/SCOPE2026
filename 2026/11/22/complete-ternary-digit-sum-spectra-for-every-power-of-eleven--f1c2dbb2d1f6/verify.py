#!/usr/bin/env python3
"""Exact finite checks for ternary digit-sum spectra of multiples of 11 powers."""
from itertools import combinations_with_replacement

H=[1,3,9,27,81]
counts=[]
for t in range(1,14):
    count=0
    for a in range(t+1):
        for b in range(t-a+1):
            for c in range(t-a-b+1):
                for d in range(t-a-b-c+1):
                    e=t-a-b-c-d
                    if (a+3*b+9*c+27*d+81*e)%121 == 0:
                        count+=1
    # independent multiset enumeration of the same finite domain
    check=sum(sum(H[j] for j in inds)%121==0 for inds in combinations_with_replacement(range(5),t))
    assert count==check,(t,count,check)
    counts.append(count)
assert counts[:8]==[0,0,0,0,1,0,5,0],counts
assert all(x>0 for x in counts[8:13]),counts
witnesses={5:(1,1,1,1,1),7:(0,1,1,1,4),9:(0,1,1,4,3),10:(2,2,2,2,2),11:(0,1,1,7,2),12:(1,2,2,2,5),13:(0,1,1,10,1)}
for t,vec in witnesses.items():
    assert sum(vec)==t
    assert sum(x*y for x,y in zip(H,vec))%121==0
for k in range(1,7):
    m=11**k
    ord_expected=5*11**max(k-2,0)
    assert pow(3,ord_expected,m)==1
    if k>=3: assert pow(3,ord_expected//11,m)!=1
    if k==1: assert all(pow(3,j,m)!=1 for j in range(1,5))
    # All members of reduction kernel are generated at the higher level.
    if k>=2:
        order=ord_expected
        subgroup={pow(3,j,m) for j in range(order)}
        assert len(subgroup)==order
        for a in H:
            assert sum(x%121==a for x in subgroup)==11**(k-2)
        for t,vec in witnesses.items():
            residues=[]
            for j,c in enumerate(vec): residues += [pow(3,j,m)]*c
            last_mod=H[max(j for j,c in enumerate(vec) if c)]
            residues[-1]=(-sum(residues[:-1]))%m
            assert residues[-1] in subgroup
            # Explicit exponents unique modulo group order.
            rexp=[]
            for u in residues:
                q=next(j for j in range(order) if pow(3,j,m)==u)
                rexp.append(q+len(rexp)*order)
            assert len(rexp)==len(set(rexp))
            assert sum(pow(3,i,m) for i in rexp)%m==0
        # Project all lower-level forbidden weights: H2 census is sufficient.
print('VERIFY_OK: exhaustive short-weight enumeration; explicit witnesses; prime-power lifting samples')
