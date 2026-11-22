#!/usr/bin/env python3
"""Exact standalone finite checks for regular-overpartition mex moment laws."""
from math import pi,sqrt,gamma,exp

def overpart_counts(ell,N):
    # Product over admissible j of (1+q^j)/(1-q^j)
    P=[0]*(N+1)
    P[0]=1
    for j in range(1,N+1):
        if j%ell==0:continue
        # multiply (1-q^j)^-1, then 1+q^j
        for n in range(j,N+1):P[n]+=P[n-j]
        for n in range(N,j-1,-1):P[n]+=P[n-j]
    return P

def mex_moments(ell,N,s):
    P=overpart_counts(ell,N)
    J=[]
    for j in range(1,N+3):
        if j%ell:J.append(j)
    H=[0]*(N+1);H[0]=1
    total=0
    for j in range(len(J)-1):
        total+=J[j]
        if total>N:break
        H[total]+=J[j+1]**s-J[j]**s
    F=[sum(P[n-k]*H[k] for k in range(n+1)) for n in range(N+1)]
    return P,F,H

def brute(ell,n):
    ans=[0,0,0]
    ad=[j for j in range(1,n+ell+3) if j%ell]
    def rec(i,rem,present):
        if i==len(ad) or ad[i]>rem:
            if rem: return
            m=next(j for j in ad if j not in present)
            ans[0]+=1;ans[1]+=m;ans[2]+=m*m
            return
        j=ad[i]
        rec(i+1,rem,present)
        for k in range(1,rem//j+1):
            # no overline, k nonoverlined copies
            rec(i+1,rem-k*j,present+(j,))
            # one overline and k-1 nonoverlined, with k>=1
            rec(i+1,rem-k*j,present+((j,) if k>1 else ()))
    rec(0,n,())
    return tuple(ans)

def main():
    tests=0
    for ell in range(2,9):
        N=500
        P,F1,H1=mex_moments(ell,N,1)
        _,F2,H2=mex_moments(ell,N,2)
        for n in range(0,16):
            b=brute(ell,n)
            assert (P[n],F1[n],F2[n])==b,(ell,n,(P[n],F1[n],F2[n]),b)
            tests+=1
        assert all(F1[n]>=F1[n-1] and F2[n]>=F2[n-1] for n in range(1,N+1))
        c=ell/(ell-1)
        a=pi/(4*c**1.5)
        # normalized mean and second moment converge slowly but must be plausibly near limit
        for n in (200,500):
            mean=F1[n]/P[n]/n**.25
            second=F2[n]/P[n]/n**.5
            predmean=gamma(1.5)/a**.5
            predsecond=1/a
            assert .70*predmean<mean<1.25*predmean,(ell,n,mean,predmean)
            assert .60*predsecond<second<1.40*predsecond,(ell,n,second,predsecond)
            tests+=1
        print(f'ell={ell} n=500 mean/n^.25={mean:.5f} target={predmean:.5f} E[M^2]/sqrt(n)={second:.5f} target={predsecond:.5f}')
    print('MEX_REGULAR_OVERPARTITIONS_FINITE_OK',tests,'exact brute and asymptotic spot checks')

if __name__=='__main__':main()
