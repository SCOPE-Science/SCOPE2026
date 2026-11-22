"""Finite exact checks of a site-percolation component-covariance identity.
Run with: python verification/check.py
This tests finite cases only; the universal sign and limit are proved analytically.
"""
from fractions import Fraction
from itertools import product
from math import comb


def formulas(a,b,p):
    q=1-p
    n=a+b
    f=(1-q**a)*(1-q**b)+a*p*q**b+b*p*q**a
    u=Fraction(b*(a+1),n)
    v=Fraction(a*(b+1),n)
    h=1-u*p+q**(b-a)*(1-v*p)-q**b
    covariance=n*p*q**a*h
    return f,covariance,h


def exact(a,b,p):
    n=a+b
    ec=ek=ekc=Fraction(0)
    for mask in product((0,1),repeat=n):
        k=sum(mask)
        left=sum(mask[:a]);right=sum(mask[a:])
        c=(1 if left and right else 0)+(left if right==0 else 0)+(right if left==0 else 0)
        probability=p**k*(1-p)**(n-k)
        ec+=c*probability
        ek+=k*probability
        ekc+=k*c*probability
    return ec,ekc-ek*ec


def main():
    count=0
    for a in range(1,5):
        for b in range(a,6):
            for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
                f,cov,h=formulas(a,b,p)
                ec,ecov=exact(a,b,p)
                assert ec==f, (a,b,p,'expectation')
                assert ecov==cov,(a,b,p,'covariance')
                count+=2
    for a in range(1,16):
        for b in range(a,22):
            h0=formulas(a,b,Fraction(0))[2]
            h1=formulas(a,b,Fraction(1))[2]
            assert h0==1
            assert h1==((1-a) if a==b else -Fraction(a*(b-1),a+b)),(a,b,h1)
            count+=2
            if b>1:
                samples=[formulas(a,b,Fraction(j,128))[2] for j in range(129)]
                assert all(x>y for x,y in zip(samples,samples[1:])),(a,b)
                count+=1
    print('PASS:',count,'exact rational equalities/inequalities; finite checks are not infinite proofs')

if __name__=='__main__':main()
