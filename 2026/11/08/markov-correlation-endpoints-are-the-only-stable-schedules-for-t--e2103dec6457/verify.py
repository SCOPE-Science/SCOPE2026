#!/usr/bin/env python3
"""Exact-rational checks for the two-step Markov geometric integration result.

Standard-library only. Execute: python3 verify.py
"""
from fractions import Fraction as F


def mm(h):
    return [[1-h*h,h],[-h,F(1)]]


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(x) for x in zip(*a)]


def transfer(h):
    one=F(1);a=one-h*h
    return [[a*a,2*h*a,h*h],[-h*a,one-2*h*h,h],[h*h,-2*h,one]]


def block(p,ha,hb):
    a=transfer(ha);b=transfer(hb);q=1-p
    return [[(p*a[i][j] if j<3 else q*a[i][j-3]) for j in range(6)] for i in range(3)] + [
            [(q*b[i][j] if j<3 else p*b[i][j-3]) for j in range(6)] for i in range(3)]


def det(a):
    a=[row[:] for row in a];n=len(a);out=F(1)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return F(0)
        if k!=j:a[j],a[k]=a[k],a[j];out=-out
        z=a[j][j];out*=z
        for i in range(j+1,n):
            r=a[i][j]/z
            for q in range(j+1,n):a[i][q]-=r*a[j][q]
            a[i][j]=F(0)
    return out


def trace(a):return sum(a[i][i] for i in range(len(a)))


def run():
    checks=0
    for numerator in range(1,18):
        h=F(numerator,10)
        m=mm(h);q=[[F(1),h/2],[h/2,F(1)]]
        assert matmul(matmul(m,q),transpose(m))==q
        assert det(m)==1
        assert F(4)-h*h>0
        checks+=3
    a,b=F(1,2),F(3,2)
    assert trace(matmul(mm(b),mm(a)))==-F(23,16);checks+=1
    for k in range(7):
        p=F(k,7);l=block(p,a,b)
        iml=[[(F(1) if i==j else F(0))-l[i][j] for j in range(6)] for i in range(6)]
        assert det(iml)==-F(9,4)*p*(1-p)**2
        checks+=1
    # Degree <= 6 in p: seven exact evaluations certify the polynomial identity.
    for x,y in [(F(1,2),F(3,2)),(F(1,4),F(7,4)),(F(2,5),F(6,5)),(F(1,3),F(2,3))]:
        inv=[[mm(y)[1][1],-mm(y)[0][1]],[-mm(y)[1][0],mm(y)[0][0]]]
        rel=matmul(inv,mm(x))
        assert trace(rel)==2-(x-y)**2
        assert (trace(rel))**2<4
        checks+=2
    print('PASS:',checks,'exact rational assertions; 7-point degree-six determinant identity certified')

if __name__=='__main__':run()
