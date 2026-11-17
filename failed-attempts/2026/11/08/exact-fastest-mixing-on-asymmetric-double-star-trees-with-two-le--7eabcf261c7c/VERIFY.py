#!/usr/bin/env python3
"""Exact-rational reproduction of a fastest-mixing double-star certificate."""
from fractions import Fraction as F
from itertools import permutations

def det4(a):
    total=F(0)
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        z=F(-1 if inv%2 else 1)
        for i in range(4):z*=a[i][p[i]]
        total+=z
    return total

def run(n):
    assert n>=6
    D=(n-1)*(n+2)
    a=F(n*(n-2),2*D);b=F(n-2,D);c=F(3*n-2,D)
    assert 2*a+c==1 and n*b+c==1
    assert F(0)<b<=a<1 and F(0)<c<1
    norm=n*(3*n**3+5*n**2-8*n+4)
    coeff_a=F(8*n*n,norm)
    coeff_b=F(n*(3*n-2)**2,norm)
    coeff_c=F(n*n*(n-2)**2,norm)
    theta=F(3*n**3+5*n**2-8*n+4,n*(n-2)*D)
    alpha=F(4,(n-2)*D);beta=F(n*(n-4),(n-2)*D)
    assert 0<theta<=1 and alpha>0 and beta>0
    assert theta*coeff_a==2*alpha
    assert theta*coeff_b+1-theta==n*beta
    assert theta*coeff_c==alpha+beta
    assert alpha+beta==b
    assert F(n*n,D)==1-b
    T=F(5*n*n+2*n-8,2*D)
    K=F(n*(3*n**3+4*n*n-28*n+16),2*D*D)
    def q(x):return x*x-T*x+K
    assert q(b)==F((n-2)*(3*n**3+5*n*n-8*n+4),2*D*D)
    assert 2*b-T==-F(n*(5*n-2),2*D)
    assert q(2-b)==F((n-2)*(n**3+5*n*n-8*n+4),2*D*D)
    assert 2*(2-b)-T==F(n*(3*n+2),2*D)
    assert q(b)>0 and 2*b-T<0 and q(2-b)>0 and 2*(2-b)-T>0
    assert T*T-4*K>=0
    Q=[[a,-a,F(0),F(0)],[-2*a,2*a+c,-c,F(0)],
       [F(0),-c,n*b+c,-n*b],[F(0),F(0),-b,b]]
    for x in [F(0),b,F(1),2-b,F(3,2)]:
        M=[[(x if i==j else F(0))-Q[i][j] for j in range(4)] for i in range(4)]
        assert det4(M)==x*(x-b)*q(x)
    return True

if __name__=='__main__':
    orders=list(range(6,201))+[256,512,1000]
    for n in orders:run(n)
    print('VERIFY_OK',len(orders),'exact orders')
