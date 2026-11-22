#!/usr/bin/env python3
"""Exact rational checks for iid sliding order-statistic identity-change statistics.
All calculations use integer counts or fractions; no simulation is used as proof.
"""
from itertools import permutations
from fractions import Fraction as Q
from math import comb, factorial

def polynomial_beta_cdf(k, j):
    # F_Beta(j,k+1-j)(u)=sum_{a=j}^k binom(k,a) u^a (1-u)^(k-a)
    p = [Q(0)] * (k+1)
    for a in range(j,k+1):
        for t in range(k-a+1):
            p[a+t] += Q(comb(k,a)*comb(k-a,t)*(-1)**t)
    return p

def lag_k_cov(k, j):
    p = polynomial_beta_cdf(k,j)
    m1 = sum(c/Q(i+1) for i,c in enumerate(p))
    m2 = sum(p[i]*p[h]/Q(i+h+1) for i in range(len(p)) for h in range(len(p)))
    return Q((k+1-2*j)**2,k*k) * (m2-m1*m1)

def theor(k,j):
    z=j*(k+1-j)
    a=k*(k+1)-2*z
    q=Q(a,k*(k+1))
    joint=Q(a*(a-2),k*(k-1)*(k+1)*(k+2))
    cov=joint-q*q
    compact=-Q(4*z*a,k*k*(k-1)*(k+1)**2*(k+2))
    assert cov == compact
    return q,joint,cov,lag_k_cov(k,j)

def enumerated(k,j,d):
    n=k+2 if d==1 else 2*k+1
    s0=s1=joint=0
    N=factorial(n)
    for arr in permutations(range(n)):
        w0=sorted(arr[:k])[j-1]
        w1=sorted(arr[1:k+1])[j-1]
        wd=sorted(arr[d:d+k])[j-1]
        we=sorted(arr[d+1:d+k+1])[j-1]
        x=w0==w1
        y=wd==we
        s0+=x; s1+=y; joint+=(x and y)
    q0=Q(s0,N);q1=Q(s1,N); P=Q(joint,N)
    return q0, q1, P, P-q0*q1

def main():
    checks=0
    for k in range(2,22):
        for j in range(1,k+1):
            q,adj,c1,ck=theor(k,j)
            assert 0<q<1 and c1<0; checks+=2
            assert (ck==0)==(2*j==k+1);checks+=1
            assert 0 <= ck and ck < Q(1,4);checks+=1
            assert polynomial_beta_cdf(k,j)[0]==0;checks+=1
        zs={j:j*(k+1-j) for j in range(1,k+1)}
        maximum=max(-theor(k,j)[2] for j in zs)
        optimum={j for j in zs if -theor(k,j)[2]==maximum}
        target=Q(k*(k+1),4)
        optimum2={j for j in zs if abs(zs[j]-target)==min(abs(z-target) for z in zs.values())}
        assert optimum==optimum2;checks+=1
    for k in range(2,7):
        for j in range(1,k+1):
            q,adj,c1,ck=theor(k,j)
            a,b,pr,cv=enumerated(k,j,1)
            assert a==q and b==q and pr==adj and cv==c1; checks+=4
    for k in range(2,5):
        for j in range(1,k+1):
            q,adj,c1,ck=theor(k,j)
            a,b,pr,cv=enumerated(k,j,k)
            assert a==q and b==q and cv==ck;checks+=3
    for k in range(3,21,2):
        assert theor(k,(k+1)//2)[3]==0;checks+=1
    print('PASS:',checks,'exact identities, inequalities, and exhaustive checks')
    for k in [3,4,5,7,9]:
        print('width',k,'rank, lag1, lagk:',[(j,str(theor(k,j)[2]),str(theor(k,j)[3])) for j in range(1,k+1)])

if __name__=='__main__': main()
