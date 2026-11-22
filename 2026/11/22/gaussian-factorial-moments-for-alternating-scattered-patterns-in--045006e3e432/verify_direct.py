#!/usr/bin/env python3
"""Independent exhaustive check of fixed-content, fixed-ab and gap-count spectra."""
from itertools import combinations
from collections import Counter
from math import comb

def contains(seq, pat):
    p=0
    for c in seq:
        if p<len(pat) and c==pat[p]: p+=1
    return p==len(pat)

def modeled(A,B):
    ans=Counter()
    def visit(gaps,remaining):
        i=len(gaps)
        if i==A:
            gaps=gaps+(remaining,)
            C=sum(j*g for j,g in enumerate(gaps))
            h=sum(g>0 for g in gaps[1:A])
            ans[C,h]+=1
            return
        for g in range(remaining+1):visit(gaps+(g,),remaining-g)
    visit((),B)
    return ans

def verify():
    tested=0
    for n in range(0,13):
        for A in range(n+1):
            B=n-A
            counts=Counter()
            for ones in combinations(range(n),A):
                x=['b']*n
                for i in ones:x[i]='a'
                C=sum(x[i]=='a' and x[j]=='b' for i in range(n) for j in range(i+1,n))
                if A:
                    gaps=[0]*(A+1)
                    past_a=0
                    for z in x:
                        if z=='a':past_a+=1
                        else:gaps[past_a]+=1
                    h=sum(v>0 for v in gaps[1:A])
                else:h=0
                counts[C,h]+=1
                for k in range(1,A+2):
                    expected=(h>=k)
                    pat=['a','b']*k+['a']
                    assert contains(x,pat)==expected,(x,k,h)
                tested+=1
            assert counts==modeled(A,B),(A,B,counts,modeled(A,B))
            assert sum(counts.values())==comb(n,A)
            for h in (range(min(A-1,B)+1) if A else [0]):
                observed=sum(v for (c,r),v in counts.items() if r==h)
                expected=(comb(A-1,h)*comb(B+1,h+1) if A else 1)
                assert observed==expected,(A,B,h,observed,expected)
    print('PASS: all binary words of length <=12, 8191 words; pattern equivalence and bivariate spectrum')
if __name__=='__main__': verify()
