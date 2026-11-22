#!/usr/bin/env python3
"""Exact finite verification of local successor covariance in binary de Bruijn cycles."""
from fractions import Fraction
from collections import Counter

def selector_tables(n):
    m=n-1; N=1<<m; full=(1<<n)-1; out=[]
    for table in range(1<<N):
        seen=set(); state=0
        for _ in range(1<<n):
            if state in seen: break
            seen.add(state)
            v=state&(N-1)
            outbit=(state>>m)^((table>>v)&1)
            state=((state<<1)&full)|outbit
        if state==0 and len(seen)==1<<n:
            out.append(table)
    return out

def empirical(n, tabs):
    N=1<<(n-1); total=len(tabs)
    marg=[Fraction(sum((t>>i)&1 for t in tabs),total) for i in range(N)]
    cov={}
    for i in range(N):
        for j in range(i+1,N):
            joint=Fraction(sum(((t>>i)&1)*((t>>j)&1) for t in tabs),total)
            cov[i,j]=joint-marg[i]*marg[j]
    return marg,cov

def overlap_kernel(m,x,y):
    return sum((Fraction(1,1<<(t+1)) for t in range(m)
                if (x&((1<<(m-t))-1))==(y>>t)),Fraction())

def matrix(n):
    m=n-1
    trips=((1,2,5),(1<<(m-2),(1<<(m-1))+1,3))
    z=[]
    for i,(a,b,c) in enumerate(trips):
        row=[]
        for j,(aa,bb,cc) in enumerate(trips):
            row.append(Fraction(i==j)+overlap_kernel(m,b,aa)-overlap_kernel(m,b,bb)
                       -overlap_kernel(m,c,aa)+overlap_kernel(m,c,bb))
        z.append(row)
    return z

def main():
    counts={2:1,3:2,4:16,5:2048}
    for n in counts:
        tabs=selector_tables(n)
        assert len(tabs)==counts[n],(n,len(tabs))
        marg,cov=empirical(n,tabs)
        hist=Counter(cov.values())
        print('order',n,'cycles',len(tabs),'covariance histogram',sorted(hist.items()))
        if n<=4:
            assert max(cov.values())<=0
        if n==3:
            assert {p:v for p,v in cov.items() if v}=={(1,2):Fraction(-1,4)}
        if n==4:
            assert {p:v for p,v in cov.items() if v}=={
                (1,4):Fraction(-1,8), (3,6):Fraction(-1,8),
                (2,5):Fraction(-1,16)}
        if n==5:
            assert cov[2,9]==Fraction(1,32)
            assert hist[Fraction(1,32)]==4
            M=matrix(n)
            assert M[0][0]==marg[2] and M[1][1]==marg[9]
            joint=M[0][0]*M[1][1]-M[0][1]*M[1][0]
            direct=Fraction(sum(((t>>2)&1)*((t>>9)&1) for t in tabs),len(tabs))
            assert joint==direct
    for n in range(5,17):
        m=n-1; M=matrix(n)
        assert M==[[Fraction(1,2),Fraction(1,1<<(m-1))],
                   [Fraction(-1,4),Fraction(1,2)+Fraction(1,1<<(m-1))]]
        assert -M[0][1]*M[1][0]==Fraction(1,1<<n)
    print('PASS: full finite selector census through order five and exact kernel checks through sixteen')

if __name__=='__main__':main()
