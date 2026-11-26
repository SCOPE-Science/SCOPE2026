#!/usr/bin/env python3
"""Exact finite checks for the joint edge/midpoint-coverage law in iid uniform interval graphs."""
import itertools
from collections import defaultdict
from fractions import Fraction as F
from math import factorial, comb


def exact(n):
    m=2*n
    sums=defaultdict(F)
    for perm in itertools.permutations(range(m)):
        pos=[0]*m
        for i,v in enumerate(perm):pos[v]=i
        pairs=[(min(pos[2*j],pos[2*j+1]),max(pos[2*j],pos[2*j+1])) for j in range(n)]
        e=sum(not (pairs[i][1]<pairs[j][0] or pairs[j][1]<pairs[i][0]) for i in range(n) for j in range(i+1,n))
        omega=max(sum(a<r<=b for a,b in pairs) for r in range(m+1))
        largest_clique=0
        for mask in range(1<<n):
            vertices=[i for i in range(n) if (mask>>i)&1]
            if all(not (pairs[i][1]<pairs[j][0] or pairs[j][1]<pairs[i][0])
                   for ii,i in enumerate(vertices) for j in vertices[ii+1:]):
                largest_clique=max(largest_clique,len(vertices))
        assert omega==largest_clique, (n,perm,omega,largest_clique)
        sums['E']+=F(e)
        sums['E2']+=F(e*e)
        for r in range(m+1):
            z=sum(a<r<=b for a,b in pairs)
            wt=F(comb(m,r), 2**m)
            sums['C']+=z*wt
            sums['C2']+=z*z*wt
            sums['CE']+=z*e*wt
    for k in sums:sums[k]/=factorial(m)
    me=F(n*(n-1),3)
    ve=F(n*(n-1),9)+F(2*n*(n-1)*(n-2),45)
    assert sums['E']==me,(n,'mean_E',sums['E'],me)
    assert sums['E2']-sums['E']**2==ve,(n,'var_E',sums['E2']-sums['E']**2,ve)
    assert sums['C']==F(n,2),(n,'mean_C',sums['C'])
    assert sums['C2']-sums['C']**2==F(n,4),(n,'var_C',sums['C2']-sums['C']**2)
    assert sums['CE']-sums['C']*sums['E']==F(n*(n-1),12),(n,'cov',sums['CE']-sums['C']*sums['E'])
    return n,dict(sums)

if __name__=='__main__':
    for n in (2,3,4):
        nn,res=exact(n)
        print(f'n={nn}, permutations={factorial(2*nn)}, exact identities=5, E_edge={res["E"]}, Var_edge={res["E2"]-res["E"]**2}, Cov(midpoint, edge)={res["CE"]-res["C"]*res["E"]}')
    print('PASS: 15 exact moment identities; 41064 orderings with clique/coverage agreement')
