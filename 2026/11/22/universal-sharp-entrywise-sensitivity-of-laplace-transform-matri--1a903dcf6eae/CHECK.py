#!/usr/bin/env python3
"""Supplementary numerical checks for sharp entrywise Laplace-filter sensitivity.
All mathematical proofs are in RESULT.md. Standard library only.
"""
import math
import random


def c(n):
    return (1.0 + math.sqrt(n)) / 2.0


def extremal_vector(n):
    p = (1.0 + 1.0 / math.sqrt(n)) / 2.0
    return [math.sqrt(p)] + [math.sqrt((1.0-p)/(n-1))] * (n-1) if n > 1 else [1.0]


def projector(u):
    return [[a*b for b in u] for a in u]


def row_norm(M):
    return max(sum(abs(x) for x in row) for row in M)


def matrix_complement(P):
    return [[(1.0 if i==j else 0.0)-P[i][j] for j in range(len(P))] for i in range(len(P))]


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]


def scale(A,s):
    return [[s*x for x in row] for row in A]


def inner(A,B):
    return sum(A[i][j]*B[i][j] for i in range(len(A)) for j in range(len(A)))


def derivative_witness(n,mu,delta,M,g,deriv):
    P=projector(extremal_vector(n)); Q=matrix_complement(P)
    J=[[1.0]*n for _ in range(n)]
    pj=matmul(P,J);qj=matmul(Q,J)
    a=-deriv(mu+delta)
    b=(g(mu+delta)-g(mu+delta+M))/M
    d=-deriv(mu+delta+M)
    F=add(add(scale(matmul(pj,P),a),scale(add(matmul(pj,Q),matmul(qj,P)),b)),scale(matmul(qj,Q),d))
    return F[0][0]


def main():
    count=0
    for n in range(1,33):
        u=extremal_vector(n)
        P=projector(u)
        assert abs(sum(x*x for x in u)-1)<2e-14
        assert abs(row_norm(P)-c(n))<3e-13
        assert abs((u[0]*sum(u))**2-c(n)**2)<3e-12
        count+=3
    rng=random.Random(23841)
    for n in range(2,17):
        for _ in range(100):
            # Construct symmetric positive contractions as a sum of weighted orthogonal projectors.
            V=[]
            while len(V)<n:
                v=[rng.gauss(0,1) for _ in range(n)]
                for q in V:
                    d=sum(v[i]*q[i] for i in range(n))
                    v=[v[i]-d*q[i] for i in range(n)]
                h=math.sqrt(sum(x*x for x in v))
                if h>1e-8: V.append([x/h for x in v])
            B=[[0.0]*n for _ in range(n)]
            for v in V:
                w=rng.random()
                for i in range(n):
                    for j in range(n): B[i][j]+=w*v[i]*v[j]
            assert row_norm(B) <= c(n)+1e-11
            count+=1
    for n in [1,2,3,5,9,16]:
        for mu in [0.0,0.5,2.0]:
            for name,g,dg in [
                ('heat',lambda x:math.exp(-1.3*x),lambda x:-1.3*math.exp(-1.3*x)),
                ('resolvent',lambda x:1.0/(x+1.2),lambda x:-1.0/(x+1.2)**2),
                ('fractional',lambda x:(x+0.8)**(-0.4),lambda x:-0.4*(x+0.8)**(-1.4)),
                ('mix',lambda x:0.7*math.exp(-1.3*x)+0.3/(x+1.2),
                         lambda x:-0.91*math.exp(-1.3*x)-0.3/(x+1.2)**2)
            ]:
                goal=c(n)**2*(-dg(mu))
                last=0.0
                for delta,M in [(0.2,10.0),(0.03,100.0),(0.002,2000.0)]:
                    val=derivative_witness(n,mu,delta,M,g,dg)
                    assert val>0 and val<=goal+1e-10,(n,mu,name,delta,M,val,goal)
                    assert val>=last-1e-9,(n,mu,name,val,last)
                    last=val
                    count+=2
                assert (goal-last)/goal < 0.01,(n,mu,name,goal,last)
                count+=1
    print('CHECK_OK',count,'supplementary assertions; ranks, scalar filters and dimensional cases checked.')

if __name__=='__main__':
    main()
