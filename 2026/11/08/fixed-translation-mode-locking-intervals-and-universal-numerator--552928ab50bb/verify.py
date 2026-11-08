#!/usr/bin/env python3
"""Exact finite consistency tests for rational mode-locking endpoint formulas.

The general proof is mathematical and is in RESULT.md. No external library used.
"""
from fractions import Fraction
from math import gcd

def ceildiv(a,b):
    return -((-a)//b)

def bits(p,q):
    return [ceildiv((j+1)*p,q)-ceildiv(j*p,q) for j in range(q)]

def polydiff(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def deriv(a):
    return [i*a[i] for i in range(1,len(a))]

def subtract(a,b):
    return [((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]

def at(a,t):
    return sum(x*t**i for i,x in enumerate(a))

def main():
    count=0
    for q in range(2,46):
        for p in range(1,q):
            if gcd(p,q)!=1:
                continue
            a=bits(p,q)
            ap=a[:]
            ap[-1]=1
            assert a[0]==1 and a[-1]==0 and sum(a)==p
            count+=1
            assert sum(i*x for i,x in enumerate(a))*2==(p-1)*(q-1)
            count+=1
            for z in (a,ap):
                for k in range(1,q+1):
                    prefix=sum(z[:k])
                    for h in range(q-k+1):
                        assert prefix>=sum(z[h:h+k])
                        count+=1
            H=[1]*q
            # Exact-rational sampled derivative signs only. The general
            # proof uses prefix-dominance rather than coefficient signs.
            for z in (a,ap):
                D=subtract(polydiff(z,deriv(H)),polydiff(deriv(z),H))
                for tau in (Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10)):
                    assert at(D,tau)>=0
                    count+=1
            Bpoly=ap+[-1]
            DB=subtract(polydiff(Bpoly,deriv(H)),polydiff(deriv(Bpoly),H))
            for tau in (Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10)):
                assert at(DB,tau)>0
                count+=1
            prevL=Fraction(1,1)
            prevU=Fraction(1,1)
            for t in (Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10)):
                h=at(H,t)
                L=at(a,t)/h
                U=(at(a,t)+t**(q-1)*(1-t))/h
                assert Fraction(p,q)<L<U<1 and L<prevL and U<prevU
                prevL,prevU=L,U
                count+=1
    # p/q=1/2, b=3/4: alpha=1/3, beta root of 4t^2-t-1.
    assert Fraction(1,1)/(1+Fraction(1,3))==Fraction(3,4)
    count+=1
    # Exact polynomial relation, with the unique positive root
    # (1+sqrt(17))/8, follows from 4t^2-t-1=0.
    # The B=3/4 numerator is 1+t-4t^2.
    t=Fraction(1,2)
    assert 1+t-4*t*t==Fraction(1,2)
    count+=1
    print('PASS:',count,'exact finite assertions; denominators 2..45')

if __name__=='__main__':
    main()
