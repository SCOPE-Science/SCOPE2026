#!/usr/bin/env python3
"""Exact characteristic-two ranks for two cubic ladder graph families."""
from collections import Counter

def graph_rows(n, twist):
    N=2*n
    rows=[]
    for i in range(N):
        if twist:
            neigh=[(i-1)%N,(i+1)%N,(i+n)%N]
        else:
            layer,r=divmod(i,n)
            neigh=[layer*n+(r-1)%n,layer*n+(r+1)%n,(1-layer)*n+r]
        row=0
        for j in neigh: row^=1<<j
        rows.append(row)
    return rows

def rank2(rows):
    piv={}
    for row in rows:
        while row:
            p=row.bit_length()-1
            if p not in piv:
                piv[p]=row
                break
            row ^= piv[p]
    return len(piv)

def matmul(A,B):
    out=[]
    for row in A:
        x=0
        while row:
            z=row&-row
            x^=B[z.bit_length()-1]
            row^=z
        out.append(x)
    return out

def expected_nullity(n,twist,j):
    if n%3: return 0
    h=n&-n
    if n%2:
        return 4*min(j,1) if twist else 2*min(j,2)
    return 2*min(j,2*h) if twist else 4*min(j,h)

def check():
    count=0
    for n in list(range(3,73)) + [78,81,84,90,96]:
        for twist in (False,True):
            N=2*n
            M=graph_rows(n,twist)
            P=[1<<i for i in range(N)]
            h=n&-n
            jmax=min(2*h+3,36) if n%3==0 else 6
            for j in range(jmax+1):
                d=N-rank2(P)
                e=expected_nullity(n,twist,j)
                assert d==e,('nullity',n,twist,j,d,e)
                count+=1
                P=matmul(P,M)
    print('CHECK_MATRIX_OK',count,'exact power-kernel comparisons')
if __name__=='__main__':check()
