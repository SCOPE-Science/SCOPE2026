#!/usr/bin/env python3
"""Exact finite tests of the full second Fourier level on symmetric groups.
Run: python3 verify.py (Python 3, standard library).
"""
from itertools import permutations
from math import factorial, comb, exp
from fractions import Fraction


def cycle_counts(pi):
    n=len(pi)
    seen=[False]*n
    a=b=0
    for i in range(n):
        if seen[i]:
            continue
        j=i;length=0
        while not seen[j]:
            seen[j]=True
            j=pi[j]
            length+=1
        a+=(length==1)
        b+=(length==2)
    return a,b


def derangements(m):
    d=[0]*(m+1);d[0]=1
    for r in range(1,m+1):
        d[r]=(r-1)*(d[r-1]+(d[r-2] if r>=2 else 0))
    return d


def run():
    ds=derangements(60)
    for m in range(61):
        assert ds[m] == sum((-1)**j*comb(m,j)*factorial(m-j) for j in range(m+1))
    for n in range(4,10):
        dA=n*(n-3)//2
        dB=(n-1)*(n-2)//2
        signed=abs_total=neg=pos=0
        for pi in permutations(range(n)):
            f,t=cycle_counts(pi)
            a=comb(f,2)+t-f
            # binom(f-1,2) equals (f-1)(f-2)/2 also for f=0.
            b=(f-1)*(f-2)//2-t
            u=dA*a+dB*b
            assert u==(dA*(f*(f-3)//2)+dB*((f-1)*(f-2)//2)-t)
            assert (u<0)==(f in (1,2))
            if u<0: assert u==-dA-t
            signed+=u
            abs_total+=abs(u)
            neg+=(u<0)
            pos+=(u>0)
        formula=2*dA*(Fraction(ds[n-1],factorial(n-1))+Fraction(ds[n-2],2*factorial(n-2)))
        formula+=Fraction(ds[n-3],factorial(n-3))+Fraction(ds[n-4],2*factorial(n-4))
        assert signed==0
        assert Fraction(abs_total,factorial(n))==formula,(n,abs_total,formula)
        assert neg==n*ds[n-1]+comb(n,2)*ds[n-2]
        print('n=%d degree=%d exact_norm=%s negative=%d positive=%d'%(n,dA+dB,formula,neg,pos))
    for n in (10,12,20,40,60):
        a=2*(n*(n-3)//2)*(Fraction(ds[n-1],factorial(n-1))+Fraction(ds[n-2],2*factorial(n-2)))
        a+=Fraction(ds[n-3],factorial(n-3))+Fraction(ds[n-4],2*factorial(n-4))
        print('n=%d normalized=%.13f limit=%.13f'%(n,float(a/(n*n-3*n+1)),3/(2*exp(1))))
    print('VERIFY_OK exact_all_permutations_n4_to9 full_second_level_n4_to60')

if __name__=='__main__': run()
