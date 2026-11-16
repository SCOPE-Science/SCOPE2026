#!/usr/bin/env python3
"""Exhaustive cyclotomic coefficients for proper 3-colorings of K_(m,n)."""
from itertools import product
from math import comb

W=((1,0),(0,1),(-1,-1))

def transformed(m,n,alpha,beta):
    if (sum(alpha)+sum(beta))%3: return (0,0)
    z=sum(x==0 for x in alpha); w=sum(x==0 for x in beta)
    e=(-1)**(m-z)*2**z+(-1)**(n-w)*2**w+1-3*(sum(alpha)%3==0)
    return (3*e,0)

def direct(alpha,beta,cols):
    a=b=0
    for l,r in cols:
        p=(sum(x*y for x,y in zip(alpha,l))+sum(x*y for x,y in zip(beta,r)))%3
        x,y=W[p];a+=x;b+=y
    return a,b

def count_zero(m,n):
    if m%2 or n%2:return 0
    def Z(r):return (2**r+2*(-1)**r)//3
    def N(r):return (2**r-(-1)**r)//3
    return (Z(m)*Z(n)+m*comb(n,2)*Z(m-1)*Z(n-2)+comb(m,2)*n*Z(m-2)*Z(n-1)
     +2*n*N(m)*N(n-1)+2*m*N(m-1)*N(n))

def main():
    for m,n in [(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(4,2)]:
        configs=[(l,r) for l in product(range(3),repeat=m) for r in product(range(3),repeat=n)
                 if all(a!=b for a in l for b in r)]
        assert len(configs)==3*(2**m+2**n-2)
        z=0;ct=0
        for freq in product(range(3),repeat=m+n):
            aa=freq[:m];bb=freq[m:]
            x=direct(aa,bb,configs)
            y=transformed(m,n,aa,bb)
            assert x==y,(m,n,freq,x,y)
            if sum(freq)%3==0:
                ct+=1
                if x==(0,0):z+=1
        exp=count_zero(m,n)
        assert z==exp,(m,n,z,exp)
        print(f'm,n={m},{n}: colorings={len(configs)}, support={ct-z}, extra zeros={z}, frequencies={3**(m+n)}')
if __name__=='__main__':main()
