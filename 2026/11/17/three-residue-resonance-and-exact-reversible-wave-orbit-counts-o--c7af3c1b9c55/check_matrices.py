#!/usr/bin/env python3
"""Independent finite checks of graph-wave fixed-space formulas; Python standard library."""
from math import gcd

def matmul(A,B):
    return [[sum(x*y for x,y in zip(r,c))%3 for c in zip(*B)] for r in A]

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def rank(A):
    a=[r[:] for r in A]; m=len(a); n=len(a[0]); q=0
    for c in range(n):
        p=next((i for i in range(q,m) if a[i][c]),None)
        if p is None:continue
        a[q],a[p]=a[p],a[q]
        t=1 if a[q][c]==1 else 2
        a[q]=[(x*t)%3 for x in a[q]]
        for i in range(m):
            if i!=q and a[i][c]:
                v=a[i][c]
                a[i]=[(x-v*y)%3 for x,y in zip(a[i],a[q])]
        q+=1
        if q==m:break
    return q

def wave(k):
    n=2*k+1
    a=[[0]*n for _ in range(n)]
    for i in range(k):
        u,v=2*i+1,2*i+2
        for x,y in ((0,u),(0,v),(u,v)):
            a[x][y]=a[y][x]=1
    w=[[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):w[i][j]=a[i][j]
        w[i][n+i]=2 # minus old layer
        w[n+i][i]=1
    return w

def dimension(k,t):
    v=t
    while v%3==0: v//=3
    e=t//v
    b=min(2,e)
    if k%3==0:
        return 2*int(t%4==0) + int(t%2==0)*(min(4,e)+(k-2)*b)+k*b
    if k%3==1:
        return min(4,e) +k*b+int(t%2==0)*(k-1)*b
    return 4*int(t%10==0)+k*b+int(t%2==0)*(k-1)*b

def order(k):
    if k==1:return 9
    return {0:36,1:18,2:30}[k%3]

def main():
    comparisons=0
    for k in range(2,11):
        w=wave(k);n=len(w);idn=eye(n);cur=eye(n)
        for t in range(1,order(k)+1):
            cur=matmul(cur,w)
            d=n-rank([[(cur[i][j]-idn[i][j])%3 for j in range(n)] for i in range(n)])
            assert d==dimension(k,t),(k,t,d,dimension(k,t))
            comparisons+=1
            if t==order(k):assert cur==idn
        for t in range(1,order(k)):
            if order(k)%t==0:
                # Dimension less than full confirms exact order.
                assert dimension(k,t)<n
        print('k',k,'order',order(k),'dim',n,'fixed-dimension samples',[(t,dimension(k,t)) for t in [1,2,3,6,9,10,12,18,30,36]])
    print('OK matrix-rank comparisons',comparisons)

if __name__=='__main__':main()
