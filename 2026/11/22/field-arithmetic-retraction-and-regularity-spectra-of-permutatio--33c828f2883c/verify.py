"""Finite-model checks for regular and idempotent endomorphism spectra of permutation evolution algebras.

Standalone Python 3, no third-party dependencies. All counts are literal finite-field enumerations.
"""
from itertools import product
from math import comb, gcd

class Field:
    def __init__(self, q):
        assert q in (2,3,4)
        self.q = q
    def mul(self, x, y):
        if self.q != 4: return (x*y) % self.q
        # GF(4)=GF(2)[a]/(a^2+a+1), elements 0,1,a,1+a
        p=0
        if x&1:
            p ^= y
        if x&2:
            p ^= y<<1
        if p&8: p ^= (7<<1)
        if p&4: p ^= 7
        return p&3
    def pow(self,x,n):
        a=1
        while n:
            if n&1: a=self.mul(a,x)
            x=self.mul(x,x);n//=2
        return a

def endos(lengths,q):
    F=Field(q)
    off=[];cum=0
    for n in lengths:off.append(cum);cum+=n
    local=[]
    for j,n in enumerate(lengths):
        opts=[tuple([(-1,0)]*n)]
        for i,m in enumerate(lengths):
            if n%m:continue
            for shift in range(m):
                for lam in range(1,q):
                    if F.pow(lam,2**n-1)!=1: continue
                    opts.append(tuple((off[i]+((b-shift)%m), F.pow(lam,2**((b-shift)%n))) for b in range(n)))
        local.append(opts)
    for parts in product(*local):
        yield tuple(x for part in parts for x in part)

def compose(A,B,F):
    return tuple((-1,0) if i<0 or B[i][0]<0 else (B[i][0],F.mul(a,B[i][1])) for i,a in A)

def ranks(lst):
    return len({i for i,v in lst if i>=0})

def predictions(lengths,q):
    from collections import Counter
    c=Counter(lengths); Ns=sorted(c)
    gamma={n:gcd(q-1,2**n-1) for n in Ns}
    idem={};regular={}
    for rvec in product(*(range(c[n]+1) for n in Ns)):
        r=dict(zip(Ns,rvec));dim=sum(n*r[n] for n in Ns)
        # Fixed image cycles are identities for retractions; regular maps need
        # a same-length witness for every selected image cycle.
        idemcnt=1
        regcnt=1
        for n in Ns:
            idemfactor=1+gamma[n]*sum(m*r[m] for m in Ns if n%m==0)
            idemcnt*=comb(c[n],r[n])*idemfactor**(c[n]-r[n])
            base=1+gamma[n]*sum(m*r[m] for m in Ns if m<n and n%m==0)
            inclusion=sum((-1)**a*comb(r[n],a)*(base+n*gamma[n]*(r[n]-a))**c[n] for a in range(r[n]+1))
            regcnt*=comb(c[n],r[n])*inclusion
        idem[dim]=idem.get(dim,0)+idemcnt
        regular[dim]=regular.get(dim,0)+regcnt
    return idem,regular

def check(lengths,q):
    F=Field(q)
    maps=list(endos(lengths,q)); histI={};histR={}
    for A in maps:
        k=ranks(A)
        if compose(A,A,F)==A: histI[k]=histI.get(k,0)+1
        if any(compose(compose(A,B,F),A,F)==A for B in maps):histR[k]=histR.get(k,0)+1
    predI,predR=predictions(lengths,q)
    assert histI==predI,(lengths,q,'idem',histI,predI)
    assert histR==predR,(lengths,q,'reg',histR,predR)
    fullreg=(sum(histR.values())==len(maps))
    antichain=not any(a!=b and b%a==0 for a in lengths for b in lengths)
    assert fullreg==antichain,(lengths,q,'criterion',fullreg,antichain)
    print('OK',lengths,q,'endomorphisms',len(maps),'idempotents',sorted(histI.items()),'regular',sorted(histR.items()))

if __name__=='__main__':
    for q,lengths in [(2,[1]),(2,[1,1]),(2,[1,2]),(2,[2,2]),(2,[1,2,2]),(2,[1,3]),(2,[2,4]),(2,[1,2,3]),(3,[1,2]),(3,[2,2]),(4,[1,2]),(4,[2,2]),(4,[1,2,2])]:
        check(lengths,q)
    print('CHECK_OK 13 exhaustive configurations')
