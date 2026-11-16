#!/usr/bin/env python3
"""Exact arithmetic independent state transfer and low-support enumeration.
Mathematical objects: Young diagrams in 2-by-n rectangles.
"""
from collections import defaultdict
from math import comb

def tri(z): return z*(z+1)//2

def cell_count(n,row,col):
    N=comb(n+2,2)
    return N-tri(col) if row==0 else tri(n-col+1)

def both(n,c,d):
    (r,i),(t,j)=c,d
    if r==t:
        return cell_count(n,r,max(i,j)) if r==0 else cell_count(n,r,max(i,j))
    if r==1:
        (r,i),(t,j)=(t,j),(r,i)
    # top i, bottom j
    if i<=j: return cell_count(n,1,j)
    return (i-j)*(n-i+1)+tri(n-i+1)

def zero1zero2(n):
    N=comb(n+2,2)
    coords=[(r,j) for r in range(2) for j in range(1,n+1)]
    singles=[c for c in coords if N==2*cell_count(n,*c)]
    pairs=[]
    for a,c in enumerate(coords):
        for d in coords[a+1:]:
            xor=cell_count(n,*c)+cell_count(n,*d)-2*both(n,c,d)
            if 2*xor==N: pairs.append((c,d))
    return singles,pairs

def transfer(n):
    D={(1,1):1}
    for _ in range(n):
        E=defaultdict(int)
        for (s,w),count in D.items():
            for y in (-1,1):
                ss=s+y
                for x in (-1,1): E[ss,w+x*ss]+=count
        D=E
    assert sum(D.values())==4**n
    return sum(v for (s,w),v in D.items() if w==0),min(abs(w) for s,w in D if w)

def independent_spectrum(n):
    N=1<<(2*n)
    f=[0]*N
    for a in range(n+1):
        for b in range(a+1):
            mask=sum(1<<i for i in range(a))+sum(1<<(n+i) for i in range(b))
            f[mask]=1
    block=1
    while block<N:
        for i in range(0,N,2*block):
            for j in range(i,i+block):
                u=f[j];v=f[j+block];f[j]=u+v;f[j+block]=u-v
        block*=2
    zeros=sum(v==0 for v in f)
    gap=min(abs(v) for v in f if v)
    first=min((x.bit_count() for x,v in enumerate(f) if not v),default=-1)
    z1=[x for x,v in enumerate(f) if v==0 and x.bit_count()==1]
    z2=[x for x,v in enumerate(f) if v==0 and x.bit_count()==2]
    assert sum(v*v for v in f)==N*comb(n+2,2)
    return zeros,gap,first,len(z1),len(z2)

if __name__=='__main__':
    for n in range(1,11):
        one,two=zero1zero2(n)
        Z,gap=transfer(n)
        if n<=9:
            zz,gg,first,z1,z2=independent_spectrum(n)
            assert (Z,gap,len(one),len(two))==(zz,gg,z1,z2)
        else:
            first=1 if one else 2 if two else -1
        assert (Z>0)==(n%4 in (2,3))
        assert gap==(2 if n%4 in (2,3) else 1)
        if Z: assert first==(1 if one else 2)
        print(f'n={n} zero={Z} gap={gap} first={first} single={len(one)} double={len(two)}')
    # Pell is exact characterization for any n, test finite boundary including first nontrivial large solution.
    for n in range(1,151):
        one,_=zero1zero2(n)
        expect=(n in (2,19,118))
        assert bool(one)==expect,(n,one)
        assert len(one)==(2 if expect else 0)
    print('PASS: independent Walsh enumeration, transfer recurrence, low-support/Pell checks')
