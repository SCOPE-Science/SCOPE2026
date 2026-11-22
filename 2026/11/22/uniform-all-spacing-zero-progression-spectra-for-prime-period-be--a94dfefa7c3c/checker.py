"""Exact finite cross-checks for Bell-zero progression theorem.
Uses elementary integer recurrences; proof for all indices is in RESULT.md.
"""
from math import comb

def direct_bell_mod(p, count):
    B=[1]
    for n in range(count-1):
        B.append(sum(comb(n,k)*B[k] for k in range(n+1))%p)
    return B

def touchard_bell_mod(p,N):
    B=direct_bell_mod(p,p)
    for n in range(max(N+p, 32+p)):
        B.append((B[n+1]+B[n])%p)
    return B

def certify(p,all_steps):
    N=(p**p-1)//(p-1)
    B=touchard_bell_mod(p,N)
    assert B[:30]==direct_bell_mod(p,30)
    assert all(B[n+N]==B[n] for n in range(p))
    assert all(any(B[n+d]!=B[n] for n in range(p))
               for d in range(1,N) if N%d==0)
    expected=[(p**(p-ell)-1)//(p-1) for ell in range(1,p+1)]
    Z=[i for i,b in enumerate(B[:N]) if b==0]
    assert len(Z)==expected[0]
    checkh=range(1,N) if all_steps else [1,2,3,4,11,71,101,390,780]
    cases=0
    for h in checkh:
        h%=N
        if h==0: continue
        candidates=Z
        for ell in range(1,p+1):
            if ell>1:
                j=ell-1
                candidates=[n for n in candidates if B[(n+j*h)%N]==0]
            assert len(candidates)==expected[ell-1], (p,N,h,ell,len(candidates),expected[ell-1])
            cases+=1
    if p==5:
        starts=[i for i in Z if all(B[(i+j)%N]==0 for j in range(1,4))]
        assert starts==[587],starts
    print(f'p={p} N={N} steps={len(checkh)} exact AP comparisons={cases} counts={expected}, verified direct prefix and full periodicity')

if __name__=='__main__':
    certify(2,True)
    certify(3,True)
    certify(5,True)
