#!/usr/bin/env python3
"""Direct independent vertex-bit verification of matching deletion pulse.
Graph on A0,...,A(n-1),B0,...,B(n-1); missing (Ai,Bi), i<k.
"""
from math import comb

def count_direct(n,k):
    block=(1<<n)-1
    fixed=period2=0
    def F(s):
        A=s&block;B=(s>>n)&block
        a=A.bit_count();b=B.bit_count()
        A1=B1=0
        for i in range(n):
            missing=int(i<k)
            ai=(A>>i)&1;bi=(B>>i)&1
            d=n-missing
            sA=b-missing*bi;sB=a-missing*ai
            if 2*sA>d or (2*sA==d and ai):A1 |=1<<i
            if 2*sB>d or (2*sB==d and bi):B1 |=1<<i
        return A1|(B1<<n)
    for s in range(1<<(2*n)):
        t=F(s)
        if F(t)==s:
            period2+=1
            fixed+=(t==s)
    assert (period2-fixed)%2==0
    return fixed,period2,(period2-fixed)//2

def test():
    cells=0;rows=0
    for n in (3,5,7):
        for k in range(n+1):
            h,p,c=count_direct(n,k);cells+=1<<(2*n);rows+=1
            expected=3*comb(n-1,(n-1)//2)+1 if k==n-1 else 1
            assert c==expected,(n,k,h,p,c,expected)
            print(f'n={n:02d}, k={k:02d}, fixed={h}, two_periodic={p}, cycles={c}')
    for k in (0,7,8,9):
        n=9;h,p,c=count_direct(n,k);cells+=1<<(2*n);rows+=1
        expected=3*comb(n-1,4)+1 if k==n-1 else 1
        assert c==expected,(n,k,h,p,c,expected)
        print(f'n={n:02d}, k={k:02d}, fixed={h}, two_periodic={p}, cycles={c}')
    print(f'Independent direct enumeration: {rows} graphs, {cells} labelled configurations, all PASS')
if __name__=='__main__':test()
