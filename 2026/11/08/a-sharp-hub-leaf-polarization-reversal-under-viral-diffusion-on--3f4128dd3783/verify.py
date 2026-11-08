#!/usr/bin/env python3
"""Reproduce exact star-cascade polarization comparisons by rational enumeration."""
from fractions import Fraction as F
from itertools import product
from math import comb

def solve(A, b):
    n = len(b)
    M = [[F(v) for v in A[i]] + [F(b[i])] for i in range(n)]
    for k in range(n):
        q = next(i for i in range(k,n) if M[i][k])
        M[k],M[q]=M[q],M[k]
        pivot=M[k][k]
        M[k]=[v/pivot for v in M[k]]
        for i in range(n):
            if i!=k:
                q=M[i][k]
                if q:
                    M[i]=[M[i][j]-q*M[k][j] for j in range(n+1)]
    return [r[-1] for r in M]

def matrix(m,w):
    n=m+1
    a=[[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(1,n):
        a[0][0]+=w; a[0][j]-=w
        a[j][j]+=w; a[j][0]-=w
    return a

def pol(m,w,bits):
    z=solve(matrix(m,w),bits)
    avg=sum(z)/len(z)
    return sum((v-avg)**2 for v in z)

def formulas(m,w,p):
    a=1/(1+w)**2
    b=F(m,m+1)/(1+(m+1)*w)**2
    H=a*(m-1)*p*(1-p)+b*((1-p)**2+p*(1-p)/m)
    D=F(m-1,m*m)*(1-p)**2*(a*m*((m-2)*p-1)+b*(m+1-(m-2)*p))
    return H,H-D,D

def brute(m,w,p):
    h=l=F(0)
    for leaf in product((0,1),repeat=m):
        k=sum(leaf)
        h+=p**k*(1-p)**(m-k)*pol(m,w,[1]+list(leaf))
    l+=(1-p)*pol(m,w,[0]+[1]+[0]*(m-1))
    for others in product((0,1),repeat=m-1):
        k=sum(others)
        l+=p*p**k*(1-p)**(m-1-k)*pol(m,w,[1,1]+list(others))
    return h,l

def run():
    checks=0
    for m in range(1,7):
        for w in (F(1,3),F(1),F(2)):
            for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                H,L,D=formulas(m,w,p)
                eH,eL=brute(m,w,p)
                assert H==eH and L==eL and H-L==D,(m,w,p,H,L,eH,eL)
                reachH=1+m*p
                reachL=1+p+(m-1)*p*p
                assert reachH-reachL==(m-1)*p*(1-p)
                if m==1: assert D==0
                if m==2 and p<1: assert D<0
                if m>=3:
                    a=1/(1+w)**2
                    b=F(m,m+1)/(1+(m+1)*w)**2
                    threshold=(m*a-(m+1)*b)/((m-2)*(m*a-b))
                    assert 0<threshold<1
                    if p<1:
                        assert (D>0)-(D<0)==(p>threshold)-(p<threshold)
                checks+=2
    m,w=4,F(1)
    a=1/(1+w)**2;b=F(m,m+1)/(1+(m+1)*w)**2
    assert (m*a-(m+1)*b)/((m-2)*(m*a-b))==F(5,11)
    print('PASS:',checks,'exact rational Markov-cascade and FJ comparisons; m=1..6, 3 weights, 5 probabilities; example p*=5/11.')
if __name__=='__main__':run()
