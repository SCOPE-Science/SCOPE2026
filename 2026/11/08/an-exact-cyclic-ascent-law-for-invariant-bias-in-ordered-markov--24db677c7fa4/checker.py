"""Exact rational verification for ordered edge-exponential splitting on directed cycles."""
from fractions import Fraction as F
from itertools import permutations
import math


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def edge(n, i, u):
    A = eye(n)
    A[i][i] = 1-u
    A[i][(i+1)%n] = u
    return A


def product(n, order, u):
    P=eye(n)
    for i in order:
        P=mul(P, edge(n,i,u))
    return P


def left(v, P):
    n=len(v)
    return [sum(v[i]*P[i][j] for i in range(n)) for j in range(n)]


def prediction(n, order, u):
    rank={x:j for j,x in enumerate(order)}
    delta=[int(rank[(i-1)%n]<rank[i]) for i in range(n)]
    m=sum(delta)
    assert 1 <= m <= n-1
    pi=[(1-u*d)/(n-u*m) for d in delta]
    tv=F(u*m*(n-m),n*(n-u*m))
    return pi, tv, m


def dist(a, b):
    return sum(abs(x-y) for x,y in zip(a,b))/2


def run():
    checks=0
    witnessed=set()
    for n in range(2,8):
        for u in (F(1,5),F(1,2),F(4,5)):
            all_orders=list(permutations(range(n)))
            if n == 7:
                # A deterministic representative sample plus each cyclic-ascent class.
                all_orders=all_orders[:210]+all_orders[-210:]
            for order in all_orders:
                pi,tv,m=prediction(n,order,u)
                witnessed.add((n,m))
                P=product(n,order,u)
                assert all(sum(row)==1 and all(x>=0 for x in row) for row in P)
                checks+=1
                assert left(pi,P)==pi
                checks+=1
                assert dist(pi, [F(1,n)]*n)==tv
                checks+=1
                assert tv>0
                checks+=1
            # Averaging cyclic origins: an exactly uniform stationary measure.
            S=[[F(0) for _ in range(n)] for _ in range(n)]
            for k in range(n):
                O=[(k+j)%n for j in range(n)]
                P=product(n,O,u)
                for i in range(n):
                    for j in range(n):
                        S[i][j]+=P[i][j]/n
            assert all(sum(row)==1 for row in S)
            checks+=1
            assert all(sum(S[i][j] for i in range(n))==1 for j in range(n))
            checks+=1
            assert left([F(1,n)]*n,S)==[F(1,n)]*n
            checks+=1
            # Sharp continuous-envelope check, avoiding floating-point roundoff:
            # u * m(n-m)/[n(n-u*m)] <= ((1-sqrt(1-u))/(1+sqrt(1-u)))
            # equivalent to u*(1-t)*t/(1-u*t) <= (...), exact rational check at selected u using sqrt bounds.
    # Algebraic-envelope witness at u=3/4, for which tanh(h/4)=1/3.
    for n in range(2,80):
        for m in range(1,n):
            u=F(3,4)
            tv=F(u*m*(n-m),n*(n-u*m))
            assert tv<=F(1,3)
            checks+=1
            # Discrete maximizers lie at the two integers bracketing 2n/3.
            opts={max(1,min(n-1,(2*n)//3)),max(1,min(n-1,(2*n)//3+1))}
            if m not in opts:
                assert tv <= max(F(u*k*(n-k),n*(n-u*k)) for k in opts)
                checks+=1
    for n in range(2,8):
        assert {m for N,m in witnessed if N==n}==set(range(1,n))
        checks+=1
    # A rational witness n=5, order 0..4, u=1/2.
    pi,tv,m=prediction(5,tuple(range(5)),F(1,2))
    assert pi==[F(1,3)]+[F(1,6)]*4 and tv==F(2,15)
    checks+=1
    # Reversal dramatically reduces the deterministic-order bias.
    pi2,tv2,m2=prediction(5,tuple(reversed(range(5))),F(1,2))
    assert m2==1 and tv2==F(4,45)
    checks+=1
    print(f'PASS {checks} exact rational assertions; all cycle sizes 2..7, all permutations through 6, three nonzero transfer probabilities; verified ascent coverage and randomized-origin stationarity.')

if __name__=='__main__':
    run()
