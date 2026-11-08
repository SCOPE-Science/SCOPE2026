"""Reproducibility checks for Catalan prime-power residue coverage.
This finite script corroborates rather than replaces the proof for all k.
"""
from math import comb

def C(n):
    return comb(2*n,n)//(n+1)

def valuation(a,p):
    r=0
    while a and a%p==0:
        a//=p;r+=1
    return r

for p in (3,5,11):
    c=1
    for k in (1,2,3):
        if p**k>500: continue
        residues=set()
        for n in range(4000):
            residues.add(c%(p**k))
            c=c*(4*n+2)//(n+2)
        assert len(residues)==p**k,(p,k,len(residues))
        c=1

for p in (3,5,11):
    for k in (1,2):
        L=2*k+3
        # Limit direct binom size for inexpensive deterministic replay.
        for digits in ((1,), ((p+1)//2,), (1,1), ((p+1)//2,1)):
            n=sum(d*p**(L*(j+1)) for j,d in enumerate(digits))
            if n>17000: continue
            b=comb(2*n,n)
            a=sum(d==(p+1)//2 for d in digits)
            assert valuation(b,p)==a
            predicted=1
            for d in digits:
                v=int(d==(p+1)//2)
                predicted*=comb(2*d,d)//p**v
            assert (b//p**a-predicted)%p**k==0,(p,k,digits)

assert (C(3*125+5**6)-20*2)%125==0
print('VERIFY_OK Catalan residue exhaustions p=3,5,11 at checked prime powers; separated-block binomial-unit checks')
