#!/usr/bin/env python3
"""Exact cyclotomic multidimensional DFT of the proper-coloring indicator."""
from itertools import product
from math import comb
W=((1,0),(0,1),(-1,-1))

def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def dft3(v):
    out=[]
    for k in range(3):
        z=(0,0)
        for j in range(3): z=plus(z,mul(v[j],W[(k*j)%3]))
        out.append(z)
    return out

def transform(m,n):
    N=m+n;size=3**N
    coeff=[]
    for x in product(range(3),repeat=N):
        a=x[:m]; b=x[m:]
        coeff.append((int(set(a).isdisjoint(set(b))),0))
    for dim in range(N):
        stride=3**(N-dim-1)
        for block in range(0,size,3*stride):
            for lower in range(stride):
                inds=[block+lower+j*stride for j in range(3)]
                vals=dft3([coeff[k] for k in inds])
                for k,v in zip(inds,vals):coeff[k]=v
    return coeff

def expected(m,n,f):
    if sum(f)%3:return (0,0)
    L=f[:m];R=f[m:]
    z=L.count(0);w=R.count(0)
    return (3*((-1)**(m-z)*2**z+(-1)**(n-w)*2**w+1-3*(sum(L)%3==0)),0)

def main():
    for m,n in [(1,1),(2,2),(2,4),(3,3),(3,4),(4,4)]:
        arr=transform(m,n);z=0
        for f,x in zip(product(range(3),repeat=m+n),arr):
            assert x==expected(m,n,f),(m,n,f,x,expected(m,n,f))
            if x==(0,0) and sum(f)%3==0:z+=1
        print(f'3-POINT_DFT_OK m={m} n={n} total={len(arr)} extra_zeros={z}')
if __name__=='__main__':main()
