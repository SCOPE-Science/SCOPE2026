#!/usr/bin/env python3
"""Exact/independent checks of first-order jamming-time kinetics on crown graphs.
Standard library only. Run: python3 verify_kinetics.py
"""
from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def rate_mean(m,k):
    assert 1 <= m and 0 <= k <= m
    if m==1:
        return Fraction(1-k)
    denom=m*m-k
    acc=Fraction(1,denom)
    if k>=2:
        acc+=Fraction(k*(k-1),denom)*rate_mean(m-1,k-2)
    if 0<k<m:
        acc+=Fraction(2*k*(m-k),denom)*rate_mean(m-1,k-1)
    if k<m:
        acc+=Fraction((m-k)**2,denom)*rate_mean(m-1,k)
    return acc

@lru_cache(None)
def rate_laplace(m,k,s):
    if m==1:
        return Fraction(1,1+s) if k==0 else Fraction(1)
    denom=m*m-k
    acc=Fraction(0)
    if k>=2:
        acc+=k*(k-1)*rate_laplace(m-1,k-2,s)
    if 0<k<m:
        acc+=2*k*(m-k)*rate_laplace(m-1,k-1,s)
    if k<m:
        acc+=(m-k)**2*rate_laplace(m-1,k,s)
    return acc/Fraction(denom+s)

@lru_cache(None)
def labelled(A,B,n,s):
    # The independent recursion uses the actual labelled vertex sets.
    allowed=[(i,j) for i in range(n) if A&(1<<i)
                              for j in range(n) if B&(1<<j) and i!=j]
    if not allowed:
        return Fraction(0),Fraction(1)
    R=len(allowed)
    children=[labelled(A^(1<<i), B^(1<<j),n,s) for i,j in allowed]
    mean=Fraction(1,R)+sum((t[0] for t in children),Fraction(0))/R
    transform=sum((t[1] for t in children),Fraction(0))/Fraction(R+s)
    return mean,transform

def check():
    print('Exact labelled-state / reduced-state agreement:')
    for n in range(2,8):
        A=B=(1<<n)-1
        for s in [Fraction(1,2),Fraction(2)]:
            independent_mean, independent_L=labelled(A,B,n,s)
            assert rate_mean(n,n)==independent_mean,(n,'mean')
            assert rate_laplace(n,n,s)==independent_L,(n,'Laplace',s)
        h=sum((Fraction(1,j*j) for j in range(1,n+1)),Fraction(0))
        print(n,'mean=',str(rate_mean(n,n))[:70], 'baseline=',str(h)[:55])
    assert rate_mean(3,3)==Fraction(7,6)
    assert rate_mean(4,4)==Fraction(115,84)
    assert rate_mean(5,5)==Fraction(7573,5460)
    # Numerically test the first-order kinetic correction, independently of the exact rational recursion.
    prev=[1.,0.]
    h=1.
    for m in range(2,2001):
        cur=[]
        for k in range(m+1):
            d=m*m-k
            v=1/d
            if k>=2:v+=k*(k-1)*prev[k-2]/d
            if k<m and k>0:v+=2*k*(m-k)*prev[k-1]/d
            if k<m:v+=(m-k)**2*prev[k]/d
            cur.append(v)
        prev=cur
        h+=1/(m*m)
        if m in [20,50,100,200,500,1000,2000]:
            print(m,'n*(E[T]-H_n^(2))=',round(m*(prev[m]-h),12))
    assert abs(2000*(prev[2000]-h)+1)<0.02
    print('All verification checks passed')

if __name__=='__main__':
    check()
