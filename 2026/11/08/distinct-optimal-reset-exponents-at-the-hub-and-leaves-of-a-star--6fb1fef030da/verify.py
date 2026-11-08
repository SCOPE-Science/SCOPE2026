#!/usr/bin/env python3
"""Direct finite-matrix and asymptotic checks for reset-walk entropy on stars.
Run: python3 verify.py
Requirements: Python 3 standard library; optional mpmath is not required.
"""
import math
import random


def ent(probs):
    return -sum(x*math.log(x) for x in probs if x>0)

def hub(m,p):
    H=ent((p,1-p))
    return (H+(1-p)*math.log(m))/(2-p)

def leaf(m,p):
    H=ent((p,1-p))
    a=p+(1-p)/m
    b=(1-p)/m
    F=-a*math.log(a)-(m-1)*b*math.log(b)
    return (H+(1-p)*F)/(2-p)

def direct(m,p,r):
    n=m+1
    # center = 0, leaves = 1..m
    P=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            w=1/m if i==0 and j>=1 else (1.0 if i>0 and j==0 else 0.0)
            P[i][j]=(1-p)*w+(p if j==r else 0.0)
    # Solve the stationary linear equations directly, without a renewal formula.
    A=[[P[i][j]-(1.0 if i==j else 0.0) for i in range(n)] for j in range(n)]
    rhs=[0.0]*n
    A[-1]=[1.0]*n
    rhs[-1]=1.0
    for k in range(n):
        t=max(range(k,n),key=lambda j:abs(A[j][k]))
        A[k],A[t]=A[t],A[k]
        rhs[k],rhs[t]=rhs[t],rhs[k]
        assert abs(A[k][k])>1e-14
        v=A[k][k]
        for j in range(k,n):A[k][j]/=v
        rhs[k]/=v
        for i in range(k+1,n):
            z=A[i][k]
            for j in range(k,n):A[i][j]-=z*A[k][j]
            rhs[i]-=z*rhs[k]
    pi=[0.0]*n
    for i in reversed(range(n)):
        pi[i]=rhs[i]-sum(A[i][j]*pi[j] for j in range(i+1,n))
    return sum(pi[i]*ent(P[i]) for i in range(n))

def der_hub(m,p):
    return math.log((1-p)/(m*p*p))/(2-p)**2

def der_leaf(m,p):
    # collision entropy loss expression used in the proof
    b=(1-p)/m
    a=p+b
    G=a*ent((p/a,b/a))
    Gp=math.log1p(b/p)-math.log1p(p/b)/m
    fprime=-(1-p)*(3-p)/(2-p)**2
    return math.log((1-p)/p)+fprime*math.log(m)+G/(2-p)**2-(1-p)/(2-p)*Gp

def optimize_leaf(m):
    lo,hi=1e-15,1-1e-15
    assert der_leaf(m,lo)>0 and der_leaf(m,hi)<0
    for _ in range(115):
        mid=(lo+hi)/2
        if der_leaf(m,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def run():
    count=0
    for m in [2,3,4,7,12,20,40]:
        for p in [0.003,0.019,0.11,0.31,0.63,0.91]:
            assert abs(hub(m,p)-direct(m,p,0))<3e-12
            assert abs(leaf(m,p)-direct(m,p,1))<3e-12
            count+=2
            assert hub(m,p)>leaf(m,p)
            count+=1
        ph=2/(math.sqrt(1+4*m)+1)
        assert abs(der_hub(m,ph))<1e-12
        assert abs(hub(m,ph)+math.log(ph))<1e-12
        count+=2
        pl=optimize_leaf(m)
        h=1e-6*min(pl,1-pl)
        num=(leaf(m,pl+h)-leaf(m,pl-h))/(2*h)
        assert abs(num)<5e-7
        count+=1
    # Analytic derivative against symmetric difference away from singular ends.
    for m in [2,5,20,200,2000]:
        for p in [0.006,0.05,0.2,0.7]:
            h=1e-6*min(p,1-p)
            diff=(leaf(m,p+h)-leaf(m,p-h))/(2*h)
            assert abs(diff-der_leaf(m,p))<2e-7,(m,p,diff,der_leaf(m,p))
            count+=1
    print('Finite-matrix, hub optimum and derivative checks:',count,'PASS')
    print('m    p_hub          p_leaf         scaled_leaf_p  scaled_leaf_gain  scaled_hub_gain')
    for m in [100,1000,10000,100000,1000000,100000000]:
        ph=2/(1+math.sqrt(1+4*m))
        pl=optimize_leaf(m)
        baseline=0.5*math.log(m)
        scaledpl=pl*m**0.75
        sg=(leaf(m,pl)-baseline)*m**0.75
        sh=(hub(m,ph)-baseline)*m**0.5
        print(f'{m:<9d}{ph:<15.9g}{pl:<15.9g}{scaledpl:<15.9g}{sg:<18.9g}{sh:<15.9g}')
        assert 0.6<scaledpl<1.01
        assert 0.6<sg<1.01
        assert .48<sh<.51
        count+=3
    print('Total verifications:',count)
    print('CHECKS_OK')
if __name__=='__main__':run()
