#!/usr/bin/env python3
"""Exact arithmetic spot checks for an RK4 weighted-star positivity theorem.

The all-size statements follow from the accompanying algebraic proof,
not from this finite certificate. Python 3 standard library only.
"""
from fractions import Fraction as F
from random import Random

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def matrix(w,h):
    m=len(w); n=m+1
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,v in enumerate(w,1):
        L[0][0]+=v;L[0][i]-=v;L[i][0]-=v;L[i][i]+=v
    T=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    P=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(1,5):
        P=mm(P,L)
        coeff=(-h)**k/F([1,1,2,6,24][k])
        for i in range(n):
            for j in range(n):
                T[i][j]+=coeff*P[i][j]
    return T

def coeff(w,a):
    S=sum(w);V=sum(x*x for x in w);W=sum(x*x*x for x in w)
    A=S+a
    B=S*S+V+S*a+a*a
    C=S**3+2*S*V+W+S*S*a+V*a+S*a*a+a**3
    return A,B,C

def Q(w,a,h):
    A,B,C=coeff(w,a)
    return 1-A*h/2+B*h*h/6-C*h**3/24

def D(w,a,b):
    S=sum(w);V=sum(x*x for x in w)
    return S*S+V+S*(a+b)+a*a+a*b+b*b

def root(w):
    a=max(w)
    hi=F(1)
    while Q(w,a,hi)>0: hi*=2
    lo=F(0)
    for _ in range(72):
        mid=(lo+hi)/2
        if Q(w,a,mid)>0:lo=mid
        else:hi=mid
    return lo,hi

def run():
    rng=Random(73119);count=0
    samples=[[F(1),F(2)],[F(1),F(1)],[F(1),F(2),F(3)],
             [F(1),F(1),F(2)],[F(1),F(3),F(3)],
             [F(2),F(4),F(8),F(16)]]
    for m in range(2,8):
        for _ in range(14):
            samples.append([F(rng.randint(1,24),rng.randint(1,8)) for _ in range(m)])
    for w in samples:
        m=len(w)
        lo,hi=root(w)
        for a in w:
            A,B,C=coeff(w,a)
            assert 9*A*C>4*B*B
            count+=1
        assert Q(w,max(w),lo)>=0 and Q(w,max(w),hi)<=0
        count+=2
        for h in [F(1,10),F(1,2),F(1),F(2),F(4),lo,hi,hi+F(1,100)]:
            T=matrix(w,h)
            S=sum(w);V=sum(x*x for x in w)
            for i,a in enumerate(w,1):
                assert T[0][i]==h*a*Q(w,a,h)
                assert T[i][0]==T[0][i]
                count+=2
                if a<max(w):
                    assert Q(w,a,h)>=Q(w,max(w),h)
                    count+=1
            for i in range(1,m+1):
                for j in range(i+1,m+1):
                    a,b=w[i-1],w[j-1]
                    A=S+a+b
                    d=D(w,a,b)
                    pred=h*h*a*b*(12-4*h*A+h*h*d)/24
                    assert T[i][j]==pred and T[j][i]==pred
                    assert 3*d>A*A
                    if h>0:assert T[i][j]>0
                    count+=4
            for i in range(m+1):
                assert sum(T[i])==1
                assert T[i][i]>0
                count+=2
        assert all(matrix(w,lo)[0][i]>=0 for i in range(1,m+1))
        assert matrix(w,hi+F(1,100))[0][1+w.index(max(w))]<0
        count+=2
    print('VERIFY_OK',count,'rational matrix identities and signs;',len(samples),'weight configurations')

if __name__=='__main__':run()
