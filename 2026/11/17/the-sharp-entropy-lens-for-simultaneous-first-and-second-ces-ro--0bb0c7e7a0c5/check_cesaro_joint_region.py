"""Exact finite tests of the two-Cesaro joint-region bounds.

Run: python check_cesaro_joint_region.py
These tests corroborate but do not replace the unrestricted proof.
"""
from fractions import Fraction as F
from math import log, isclose


def harmonics(n):
    h=[F(0)]*(n+1)
    for j in range(1,n+1):h[j]=h[j-1]+F(1,j)
    return h


def extrema(n,k,h):
    if k==0:return F(0),F(0)
    if k==n:return F(1),F(1)
    return (F(k,n)-F(n-k,n)*(h[n]-h[n-k]),
            F(k,n)*(1+h[n]-h[k]))


def U(u):return 0.0 if u==0 else u*(1-log(u))
def L(u):return 1.0 if u==1 else (0.0 if u==0 else u+(1-u)*log(1-u))


def check():
    total=0
    for n in range(1,16):
        h=harmonics(n)
        w=[(h[n]-h[j-1])/n for j in range(1,n+1)]
        assert sum(w,F(0))==1
        assert all(w[i]>w[i+1] for i in range(n-1))
        lower_upper=[extrema(n,k,h) for k in range(n+1)]
        # Enumerate all binary inputs with a single update per Gray-code step.
        prev=0;v=F(0)
        for i in range(1<<n):
            bits=i^(i>>1)
            if i:
                j=(bits^prev).bit_length()-1
                v+=w[j] if bits>>j&1 else -w[j]
            k=bits.bit_count();lo,up=lower_upper[k]
            assert lo<=v<=up,(n,bits,k,v,lo,up)
            if bits==(1<<k)-1:assert v==up
            if bits==((1<<k)-1)<<(n-k):assert v==lo
            prev=bits; total+=1
        for k,(lo,up) in enumerate(lower_upper):
            u=k/n
            assert L(u)<=float(lo)+1e-13
            assert float(up)<=U(u)+1e-13
            assert 0<=U(u)-float(up)<=1/n+1e-12
            assert 0<=float(lo)-L(u)<=1/n+1e-12
            entropy= -u*log(u)-(1-u)*log(1-u) if 0<u<1 else 0
            assert abs(float(up-lo)-entropy)<=2/n+1e-12
    print('EXACT_ALL_BINARY_WORDS_N1_TO_N15_PASSED',total)
    for n in (100,1000,5000):
        h=harmonics(n)
        prefix=[F(0)]*(n+1)
        for j in range(1,n+1):prefix[j]=prefix[j-1]+(h[n]-h[j-1])/n
        for a,u in ((0,0.1),(0.2,0.4),(0.6,0.1),(0.1,0.8)):
            start=round(a*n);end=min(n,round((a+u)*n))
            v=prefix[end]-prefix[start]
            integral=U(end/n)-U(start/n)
            assert abs(float(v)-integral)<=2/n+1e-12
        for m in (0,1,2,7):
            first=prefix[m]
            bound=(m/n)*(1+log(n/max(m,1))) if m else 0
            assert float(first)<=bound+1e-12
    print('CONTIGUOUS_BLOCK_AND_PREFIX_ESTIMATES_PASSED')
    assert isclose(U(.5)-L(.5),log(2),rel_tol=1e-14)
    print('ENTROPY_WIDTH_IDENTITY_PASSED')

if __name__=='__main__':check()
