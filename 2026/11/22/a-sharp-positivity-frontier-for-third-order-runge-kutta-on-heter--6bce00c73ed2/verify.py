#!/usr/bin/env python3
"""Exact-rational checks for third-order heat/Markov stepping on directed triangles.

These finite tests check the algebra; the parameter-uniform theorem uses the
Bernstein-coefficient and Descartes-rule arguments in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def step(a, b, c, h):
    Q = [[-a,a,F(0)], [F(0),-b,b], [c,F(0),-c]]
    Q2 = matmul(Q,Q)
    Q3 = matmul(Q2,Q)
    return [[(F(i==j)+h*Q[i][j]+h*h*Q2[i][j]/2+h**3*Q3[i][j]/6) for j in range(3)] for i in range(3)]

def r(z):
    return 1-z+z*z/2-z**3/6

def g(a,b,c,h):
    return r(max(a,b,c)*h)+a*b*c*h**3/6

def formula(a,b,c,h):
    s=a+b+c
    rates=(a,b,c)
    out=[[F(0)]*3 for _ in range(3)]
    for i in range(3):
        x,y=rates[i],rates[(i+1)%3]
        out[i][i]=r(x*h)+a*b*c*h**3/6
        out[i][(i+1)%3]=x*h*(6-3*(x+y)*h+(x*x+x*y+y*y)*h*h)/6
        out[i][(i+2)%3]=x*y*h*h*(3-s*h)/6
    return out

def check():
    count=0
    for A,B,C in product(range(1,8),repeat=3):
        a,b,c=map(F,(A,B,C))
        s=a+b+c
        H=F(3)/s
        M=max(a,b,c)
        phi=g(a,b,c,H)
        beta1=1-M/s
        beta2=1-2*M/s+F(3,2)*(M/s)**2
        assert beta1>0 and beta2>0
        count+=2
        for h in (F(0),F(1,M),H/2,H,H+F(1,7)):
            P=step(a,b,c,h)
            E=formula(a,b,c,h)
            assert P==E
            assert all(sum(row)==1 for row in P)
            assert P[0][0]+P[1][1]+P[2][2] == sum(r(x*h)+a*b*c*h**3/6 for x in (a,b,c))
            assert all(P[i][(i+1)%3]>0 for i in range(3)) if h>0 else True
            assert (all(P[i][(i+2)%3]>=0 for i in range(3))) == (h<=H)
            assert min(P[i][i] for i in range(3)) == g(a,b,c,h)
            count+=6
            if h == H:
                assert (all(z>=0 for row in P for z in row)) == (phi>=0)
                count+=1
        if phi < 0:
            lo,hi=F(0),H
            for _ in range(20):
                mid=(lo+hi)/2
                if g(a,b,c,mid)>0:
                    lo=mid
                else:
                    hi=mid
            assert g(a,b,c,lo)>0 and g(a,b,c,hi)<0
            assert all(z>=0 for row in step(a,b,c,lo) for z in row)
            assert min(z for row in step(a,b,c,hi) for z in row)<0
            count+=3
        else:
            assert all(z>=0 for row in step(a,b,c,H) for z in row)
            count+=1
    # Sign transition in the natural one-rate imbalance family.
    for a,sgn in ((F(2),1),(F(3),-1)):
        assert (g(a,F(1),F(1),F(3,a+2))>0)==(sgn==1)
        count+=1
    print('VERIFY_OK exact_checks',count,'rate_triples',7**3)

if __name__=='__main__':
    check()
