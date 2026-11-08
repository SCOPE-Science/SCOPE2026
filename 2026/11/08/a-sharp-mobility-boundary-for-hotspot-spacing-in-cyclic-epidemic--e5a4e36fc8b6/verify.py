#!/usr/bin/env python3
"""Standalone exact-rational checks for the cyclic two-hotspot theorem.

Run: python3 verify.py
No external packages. The mathematical proof covers all admissible parameters;
these finite checks exercise matrix identities, ordering, and a threshold witness.
"""
from fractions import Fraction as F
from itertools import product

def ring(n, h):
    p = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        p[i][i] = 1 - 2*h
        p[i][(i-1) % n] = h
        p[i][(i+1) % n] = h
    return p

def multiply(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def solve(a,b):
    n=len(b)
    m=[list(a[i])+[b[i]] for i in range(n)]
    for j in range(n):
        row=next(i for i in range(j,n) if m[i][j])
        m[j],m[row]=m[row],m[j]
        pivot=m[j][j]
        m[j]=[x/pivot for x in m[j]]
        for i in range(n):
            if i!=j:
                f=m[i][j]
                if f:
                    m[i]=[m[i][k]-f*m[j][k] for k in range(n+1)]
    return [m[i][-1] for i in range(n)]

def green_column(n,h,beta,lam):
    q=multiply(ring(n,h),ring(n,h))
    z=[[ (lam if i==j else F(0))-beta*q[i][j] for j in range(n)] for i in range(n)]
    return solve(z,[q[i][0] for i in range(n)])

def ball(n,r):
    return [F(int(min(i,n-i)<=r)) for i in range(n)]

def convolution(f,g):
    n=len(f)
    return [sum((f[k]*g[(i-k)%n] for k in range(n)),F(0)) for i in range(n)]

def monotone(f):
    return all(f[i]>=f[i+1] for i in range(len(f)//2))

def main():
    checks=0
    for n in range(5,18):
        for r,s in product(range(n//2+1),repeat=2):
            assert monotone(convolution(ball(n,r),ball(n,s)))
            checks+=1
    for n in range(5,13):
        for h in [F(1,20),F(1,4),F(1,3),F(39,100)]:
            q=multiply(ring(n,h),ring(n,h))
            assert all(sum(row)==1 for row in q)
            assert q[0][0]==(1-2*h)**2+2*h*h
            assert q[0][1]==2*h*(1-2*h)
            assert q[0][2]==h*h
            col=green_column(n,h,F(4,5),F(1))
            assert all(col[i]>col[i+1] for i in range(n//2))
            checks+=1
    for h in [F(1,10),F(1,4),F(2,5),F(9,20),F(1,2)]:
        n=5;beta=F(4,5);lam=F(1)
        col=green_column(n,h,beta,lam)
        p=ring(n,h)
        q=multiply(p,p)
        # The Fourier eigenvalues satisfy u^2-v^2=sqrt(5)*h*(2-5*h).
        # The radicals cancel in the following rational resolvent identity:
        # Algebraic squared multipliers as conjugates:
        # p1 = 1-((5-sqrt5)/2)*h, p2=1-((5+sqrt5)/2)*h.
        # (lam-beta*p1^2)(lam-beta*p2^2) is rational:
        ss=2*(1-F(5,2)*h)**2+F(5,2)*h*h
        pp=((1-F(5,2)*h)**2-F(5,4)*h*h)**2
        den=lam*lam-beta*lam*ss+beta*beta*pp
        assert col[1]-col[2]==h*(2-5*h)*lam/den
        checks+=1
    # The C5 'mobility erasure' matrix identity is exact.
    q=multiply(ring(5,F(2,5)),ring(5,F(2,5)))
    assert all(q[i][j]==(F(1,5) if i==j else F(0))+F(4,25)
               for i in range(5) for j in range(5))
    checks+=1
    # Fully exact rational threshold tests, beta0=4/5, recovery=1.
    cr={F(1,4):(F(348,815),F(348,715)),
        F(2,5):(F(7,15),F(7,15)),
        F(9,20):(F(24244,51605),F(24244,56105))}
    for h,(t1,t2) in cr.items():
        g=green_column(5,h,F(4,5),F(1))
        assert 1/(g[0]+g[1])==t1
        assert 1/(g[0]+g[2])==t2
        checks+=2
    delta=F(9,20)
    assert cr[F(1,4)][0]<delta<cr[F(1,4)][1]
    assert cr[F(9,20)][1]<delta<cr[F(9,20)][0]
    checks+=2
    print('PASS:',checks,'exact-rational kernel, convolution, resolvent and threshold checks')
    print('At flux 1/4, adjacent hotspots invade while distance-two hotspots do not.')
    print('At flux 9/20, the same hotspots reverse these threshold outcomes.')

if __name__=='__main__':main()
