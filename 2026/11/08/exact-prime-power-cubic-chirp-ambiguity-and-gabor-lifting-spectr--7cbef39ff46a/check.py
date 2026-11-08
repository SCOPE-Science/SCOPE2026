#!/usr/bin/env python3
"""Numerical spot checks of exact cubic-chirp ambiguity strata; no proof by enumeration."""
import numpy as np

def prediction(p,k):
    n = p**k
    arr = np.zeros((n,n),dtype=float)
    for a in range(n):
        if a == 0: t=k
        else:
            t=0; z=a
            while z % p == 0: t+=1; z//=p
        for b in range(n):
            if p!=3:
                if a==0:
                    if b==0: arr[a,b]=n
                elif b % (p**t) == 0: arr[a,b]=p**((k+t)/2)
            else:
                if t>=k-1:
                    if b==0: arr[a,b]=n
                elif b % (p**(t+1)) == 0: arr[a,b]=p**((k+t+1)/2)
    return arr

def check(p,k):
    n=p**k
    idx=np.arange(n, dtype=np.int64)
    g=np.exp(2j*np.pi * (np.power(idx,3)%n)/n)
    pred=prediction(p,k)
    raw=np.zeros((n,n),dtype=complex)
    for a in range(n):
        raw[a]=np.fft.fft(np.conjugate(g)*np.roll(g,-a))
    delta=np.max(np.abs(np.abs(raw)-pred))
    assert delta<2e-8*max(1,n), (p,k,delta)
    if p==3:
        target=(n*n+3)//4
    else:
        target=(p*n*n+1)//(p+1)
    count=np.count_nonzero(pred)
    assert count==target,(p,k,count,target)
    # Parseval/Weyl Parseval: Σ_{a,b}|A(a,b)|² = N||g||⁴=N³.
    assert abs(np.sum(pred*pred)-n**3)<max(1,1e-7*n**3)
    print(f'p={p}, k={k}, N={n}, nonzero={count}, max_modulus_error={delta:.2e}')
    if p==3 and k==2:
        # Build actual complex linear measurement matrix on all N×N matrices.
        e=np.eye(n,dtype=complex)
        lifting=[]
        for a in range(n):
            for b in range(n):
                h=np.roll(g,a)*np.exp(2j*np.pi*b*idx/n)
                lifting.append(np.outer(h,h.conj()).ravel().conj())
        lifting=np.asarray(lifting)
        sv=np.linalg.svd(lifting,compute_uv=False)
        expected=np.sort((np.sqrt(n)*pred).ravel())[::-1]
        assert np.max(np.abs(sv-expected))<2e-7
        print('N=9 full 81x81 lifted singular spectrum agrees with Weyl prediction')

if __name__=='__main__':
    for p,k in [(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,1)]:
        check(p,k)
    print('CUBIC_CHIRP_AMBIGUITY_STRATA_TESTS_OK')
