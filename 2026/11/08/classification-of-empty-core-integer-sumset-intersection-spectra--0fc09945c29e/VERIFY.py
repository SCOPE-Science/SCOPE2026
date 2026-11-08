"""Finite arithmetic spot-checks for zero-sum length spectra of separated integer tails.

The full infinite statement is proved analytically, not by this test.
"""
from itertools import combinations_with_replacement

def construct(ds, q, count):
    D=max(ds)
    G=1
    for j in range(1,q):
        G *= (D+1)*(j+2)
    entries=[]
    for j in range(q,q+count):
        d=ds[(j-1)%len(ds)]
        entries.extend([G,-(d-1)*G])
        G *= (D+1)*(j+2)
    return entries

def in_monoid(h,ds):
    reachable=[False]*(h+1)
    reachable[0]=True
    for k in range(1,h+1):
        reachable[k]=any(k>=d and reachable[k-d] for d in ds)
    return reachable[h]

def check():
    cases=[([3],6,3,10),([3,5],6,4,10),([4,7],6,4,10),([3,4,7],6,5,8)]
    total=0
    for ds,q,count,max_h in cases:
        x=construct(ds,q,count)
        for h in range(1,max_h+1):
            zeros=0
            for indices in combinations_with_replacement(range(len(x)),h):
                if sum(x[i] for i in indices)==0:
                    zeros+=1
            expect=in_monoid(h,ds)
            assert (zeros>0)==expect,(ds,q,count,h,zeros,expect)
            total+=1
        print('FINITE_ZERO_SUM_LENGTHS_OK',ds,'q',q,'indices',count,'tested_h',max_h)
    print('VERIFY_OK', 'cases', total, 'finite_only', True, 'infinite_proof_separate', True)
if __name__=='__main__':check()
