#!/usr/bin/env python3
"""Independent finite checks of the three-window k-full occupancy formulas.
The mathematical argument establishes the limiting distribution; this script checks
arithmetic enumeration, local rotation cells, and the finite exceptional factor.
"""
from math import isqrt, log
from itertools import product

def least_prime_factors(m):
    s=list(range(m+1))
    for p in range(2,isqrt(m)+1):
        if s[p]==p:
            for j in range(p*p,m+1,p):
                if s[j]==j:s[j]=p
    return s

def factor_exponents(n,spf):
    factors=[]
    while n>1:
        p=spf[n];e=0
        while n%p==0:n//=p;e+=1
        factors.append((p,e))
    return factors

def brute_counts(k,N):
    M=(N+3)**k
    spf=least_prime_factors(M)
    pref=[0]*(M+1)
    cnt=0
    for m in range(2,M+1):
        q=m;valid=True
        while q>1:
            p=spf[q];e=0
            while q%p==0:q//=p;e+=1
            if e<k:valid=False;break
        if valid: cnt+=1
        pref[m]=cnt
    return [tuple(pref[(n+j+1)**k-1]-pref[(n+j)**k] for j in range(3)) for n in range(1,N+1)]

def decomposition_counts(k,N):
    # enumerate all k-th-power-free coefficient radicals explicitly as assignments
    # each prime is assigned to at most one exponent k+j
    M=(N+3)**k
    # generate k-full integers using factors of small a and b_j via direct trial to avoid relying on brute sieve
    # primitive coefficients c are kth-power-free exponents in k+1,...,2k-1
    cap=N+3
    bases=[]
    def add(c,small_prime_limit):
        if c> M:return
        if c>1: bases.append(c)
        # p with p>small_prime_limit, choose a nonzero j mod k
        for p in range(small_prime_limit+1,cap+1):
            if p>3 and any(p%d==0 for d in range(2,isqrt(p)+1)):continue
            if p==2 or p==3 or all(p%d for d in range(2,isqrt(p)+1)):
                v=p**(k+1)
                if c*v>M:break
                for j in range(1,k):
                    z=c*p**(k+j)
                    if z>M: break
                    add(z,p)
    # huge cap gives recursion many; only k<=3 and cap small to stay bounded
    add(1,1)
    event=[0]*(N+4)
    for c in bases:
        a=1
        while (a**k)*c<M:
            m=(a**k)*c
            # exact integer kth-root floor of m: since m<cap^k, binary search
            lo,hi=0,cap
            while lo+1<hi:
                mid=(lo+hi)//2
                if mid**k<m:lo=mid
                else:hi=mid
            if lo>=1 and lo<=N+2: event[lo]+=1
            a+=1
    return [tuple(event[n+j] for j in range(3)) for n in range(1,N+1)],len(bases)

def local_check(k):
    exceptions=[2**(1+j/k) for j in range(1,k) if 2**(1+j/k)<3]
    for lam in exceptions+[3.5,5.2]:
        p=1/lam;q=max(0,3*p-1)
        probs={(0,0,0):max(0,1-3*p), (1,0,0):p-q,(0,1,0):p,(0,0,1):p-q,(1,0,1):q}
        assert abs(sum(probs.values())-1)<1e-12
        # Approximate orbit by grid of uniform initial phases.
        samples=100000
        counts={x:0 for x in probs}
        for i in range(samples):
            t=(i+.5)/samples
            word=tuple(int((t+j*p)%1>1-p) for j in range(3))
            assert word in counts, (k,lam,word)
            counts[word]+=1
        assert all(abs(counts[w]/samples-v)<3e-5 for w,v in probs.items()),(k,lam,counts,probs)
    return len(exceptions)

def main():
    for k,N in [(2,125),(3,48)]:
        a=brute_counts(k,N)
        b,count=decomposition_counts(k,N)
        assert a==b,[(n,a[n-1],b[n-1]) for n in range(1,N+1) if a[n-1]!=b[n-1]][:5]
        print('k',k,'N',N,'matching arithmetic triples',N,'primitive coefficients',count)
    for k in (2,3,4,5,8,12):
        print('k',k,'local factors verified',local_check(k),'exceptional lambda < 3')
    C=(.5-log(1.5))/log(2)
    for k in (32,128,512,2048):
        qsum=sum(max(0,3/(2**(1+j/k))-1) for j in range(1,k))
        assert abs(qsum/k-C)<2/k
        print('large-k',k,'gap',round(qsum,8),'gap/k',round(qsum/k,8),'limit',round(C,8))
    print('PASS all standalone checks')
if __name__=='__main__': main()
