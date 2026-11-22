#!/usr/bin/env python3
"""Exact modular checks accompanying the ternary Fubini residue theorem."""
import math
from collections import Counter

def weight_mod(k):
    m = 3**k
    w = [pow(2, m-1-r, m)*pow(pow(2,m,m)-1,-1,m) % m for r in range(m)]
    assert sum(w)%m==1
    return m,w

def moment(k, eps, j):
    m,w=weight_mod(k)
    return sum(w[r]*pow(r,eps,m)*pow((r*r-1)%m,j,m) for r in range(m) if r%3) %m

def fubini_mod(m,n_max):
    J=1
    while math.factorial(J)%m: J+=1
    factorials=[math.factorial(j)%m for j in range(J)]
    S=[0]*J; S[0]=1
    output=[]
    for n in range(n_max+1):
        output.append(sum(S[j]*factorials[j] for j in range(J))%m)
        S=[(j*S[j]+(S[j-1] if j else 0))%m for j in range(J)]
    return output

def run():
    tests=0
    target=[[12,72,0,0],[52,15,54,54]]
    for eps in (0,1):
        for j in range(4):
            assert moment(4,eps,j)==target[eps][j]
            tests+=1
    for k in range(1,7):
        m,w=weight_mod(k)
        vals=fubini_mod(m,max(2*3**(k-1)+k+3,40))
        for n in range(0,min(36,len(vals))):
            assert sum(w[r]*pow(r,n,m) for r in range(m))%m==vals[n]
            tests+=1
        if k>1:
            T=2*3**(k-1)
            tail=vals[k:k+T]
            counts=Counter(tail)
            assert set(counts)==({r for r in range(m) if r%3==1}|{r for r in range(m) if r%9==3})
            for r in range(m):
                assert counts.get(r,0)==(1 if r%3==1 else (3 if r%9==3 else 0))
                tests+=1
            for n in range(k, min(k+T+3,len(vals)-T)):
                assert vals[n]==vals[n+T]
                tests+=1
        else:
            assert set(vals[1:])=={0,1}
        if k<=5:
            # Check the 3-adic unit-branch interpolation independently
            T0=3**max(0,k-2)
            T1=3**(k-1)
            for eps,Tbranch,a in ((0,T0,2),(1,T1,1)):
                arr=[]
                for t in range(Tbranch):
                    g=sum(w[r]*pow(r,eps+2*t,m) for r in range(m) if r%3)%m
                    arr.append(g)
                assert len(set(arr))==Tbranch
                assert all(x%(3**min(a,k))==(3 if eps==0 else 1)%(3**min(a,k)) for x in arr)
                for t in range(Tbranch):
                    for u in range(t):
                        x=arr[t]-arr[u];y=t-u
                        while y%3==0:
                            assert x%3==0
                            x//=3;y//=3
                        assert x%(3**a)==0 and (x//(3**a))%3!=0
                        tests+=1
    print('PASS: exact residue/moment/period/isometry checks; assertions:',tests)
if __name__=='__main__':run()
