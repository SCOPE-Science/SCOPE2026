#!/usr/bin/env python3
"""Independent finite enumeration of two-deletion multiplicity and run rigidity."""
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
from math import comb,log

def histories(x):
    n=len(x)
    h={}
    for i,j in combinations(range(n),2):
        y=x[:i]+x[i+1:j]+x[j+1:]
        h[y]=h.get(y,0)+1
    return h

def runinfo(x):
    rid=[]; sizes=[]
    for a,v in enumerate(x):
        if a==0 or x[a-1]!=v:sizes.append(0)
        rid.append(len(sizes)-1);sizes[-1]+=1
    return rid,sizes

def check():
    checked=0
    for q,nmax in [(2,9),(3,7),(4,6)]:
        for n in range(2,nmax+1):
            multiplicities=Counter()
            pairs=comb(n,2)
            for x in product(range(q),repeat=n):
                h=histories(x)
                rid,sizes=runinfo(x)
                for i,j in combinations(range(n),2):
                    y=x[:i]+x[i+1:j]+x[j+1:]
                    z=h[y]
                    multiplicities[z]+=1
                    if rid[j]-rid[i]>=3:
                        assert z==sizes[rid[i]]*sizes[rid[j]],(q,n,x,i,j,z)
                    checked+=1
            assert sum(multiplicities.values())==q**n*pairs
            # Conditional-entropy identity, directly averaged from exact enumerations.
            e_log=sum(v*log(k) for k,v in multiplicities.items())/(q**n*pairs)
            H_cond=log(pairs)-e_log
            # Explicit conditional output distribution: probability z / pairs.
            h_from_outputs=0.0
            for x in product(range(q),repeat=n):
                for count in histories(x).values():
                    p_out=count/pairs
                    h_from_outputs-=p_out*log(p_out)/(q**n)
            assert abs(H_cond-h_from_outputs)<1e-9,(q,n)
    print('PASS: checked',checked,'planted pairs across exhaustive small inputs')
if __name__=='__main__':check()
