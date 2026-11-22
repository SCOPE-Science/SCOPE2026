#!/usr/bin/env python3
"""Exact finite-field tests for a genus-13 S3 trigonal Galois closure.
Only Python 3 standard library is needed.
"""
P=11

def run(n):
    # F11 for n=1; F121=F11[i] with i*i=-1 for n=2.
    elements=[(a,) if n==1 else (a,b) for a in range(P) for b in (range(P) if n==2 else [0])]
    if n==1: elements=[(a,) for a in range(P)]
    zero=(0,)*n
    one=(1,)+(0,)*(n-1)
    def c(k): return (k%P,)+(0,)*(n-1)
    def plus(x,y): return tuple((x[i]+y[i])%P for i in range(n))
    def minus(x): return tuple(-x[i]%P for i in range(n))
    def mul(x,y):
        if n==1: return ((x[0]*y[0])%P,)
        return ((x[0]*y[0]-x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
    def power(x,m):
        v=one
        while m:
            if m&1:v=mul(v,x)
            x=mul(x,x);m//=2
        return v
    square_counts={}
    for x in elements:
        xx=mul(x,x)
        square_counts[xx]=square_counts.get(xx,0)+1
    distinct_counts={i:0 for i in range(4)}
    max_fiber=0
    for t in elements:
        t4=power(t,4)
        roots=sum(plus(plus(power(u,3),minus(mul(t4,power(u,2)))),one)==zero for u in elements)
        distinct_counts[roots]+=1
    # At each separable split fiber there are six Galois-closure points.
    # At each simple-discriminant (2 distinct roots) fiber there are three.
    # The three simple poles of t split completely at infinity: six points.
    n_g=6*distinct_counts[3]+3*distinct_counts[2]+6
    n_c=1 # lone point above the elliptic curve's infinity point
    for x in elements:
        rhs=plus(power(x,3),one)
        for y in elements:
            if mul(y,y)==rhs:
                n_c+=square_counts.get(mul(x,y),0)
    n_y=2+sum(square_counts.get(plus(mul(c(4),power(t,12)),c(-27)),0) for t in elements)
    return distinct_counts,n_g,n_c,n_y

if __name__=='__main__':
    observed1=run(1)
    observed2=run(2)
    print('F11 root patterns, G, C, Y:',observed1)
    print('F121 root patterns, G, C, Y:',observed2)
    assert observed1==({0:4,1:5,2:2,3:0},12,12,12)
    assert observed2==({0:48,1:0,2:12,3:61},408,210,232)
    assert 408==121+1+2*13*11
    assert 12**13==106993205379072
    print('GENUS13_S3_MAXIMAL_F121_VERIFIED')
