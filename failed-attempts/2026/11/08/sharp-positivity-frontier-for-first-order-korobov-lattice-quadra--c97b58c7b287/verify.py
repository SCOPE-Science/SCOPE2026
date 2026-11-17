#!/usr/bin/env python3
"""Independent real-arithmetic checks for one-dimensional Korobov quadrature.

Requires Python 3.9+ standard library.  These finite tests supplement, but do
not replace, the general analytic proof accompanying the theorem.
"""
import math
from math import pi, sin, cos, tan


def int_polynomial_sine(coeff, a, b):
    """Integral (A*y*y+B*y+C)*sin(2*pi*y) dy on [a,b]."""
    A, B, C = coeff
    w = 2*pi
    def primitive(y):
        P = A*y*y + B*y + C
        Pp = 2*A*y+B
        return -P*cos(w*y)/w + Pp*sin(w*y)/(w*w) + 2*A*cos(w*y)/(w*w*w)
    return primitive(b)-primitive(a)


def weighted_polynomial(coeff, a, b):
    """Integral polynomial times mu=(pi/2)*abs(sin(2*pi*y))."""
    if a >= b:
        return 0.0
    if a < 0.5 < b:
        return weighted_polynomial(coeff,a,0.5)+weighted_polynomial(coeff,0.5,b)
    sign = 1.0 if (a+b)/2 < 0.5 else -1.0
    return (pi/2)*sign*int_polynomial_sine(coeff,a,b)


def b2(x):
    x=x%1.0
    return x*x-x+1/6


def kernel(t,y,gamma):
    return 1+2*pi*pi*gamma*b2(t-y)


def kappa(t,gamma):
    knots=sorted(set([0.0,0.5,1.0,t]))
    out=0.0
    for a,b in zip(knots,knots[1:]):
        if b==a:continue
        d=t if (a+b)/2 <t else t+1
        # 1+2*pi*pi*gamma*B2(d-y)
        coeff=(2*pi*pi*gamma, 2*pi*pi*gamma*(1-2*d),
               1+2*pi*pi*gamma*(d*d-d+1/6))
        out+=weighted_polynomial(coeff,a,b)
    return out


def hat_integral(N,j):
    h=1/N
    t=j*h
    def hat(y):
        d=abs(y-t)
        d=min(d,1-d)
        return max(0.,1-d/h)
    knots=sorted(set([0.,.5,1.,t,(t-h)%1,(t+h)%1]))
    val=0.
    for a,b in zip(knots,knots[1:]):
        if a==b:continue
        A=(hat(b)-hat(a))/(b-a)
        C=hat(a)-A*a
        val+=weighted_polynomial((0.,A,C),a,b)
    return val


def bubble_integral(N):
    h=1/N
    knots=sorted(set([k*h for k in range(N+1)]+[0.5]))
    total=0.
    for a,b in zip(knots,knots[1:]):
        if a==b:continue
        k=min(N-1,int(((a+b)/2)*N))
        # 1/2*(y-k*h)*((k+1)*h-y)
        coeff=(-0.5,(k+0.5)*h,-0.5*k*(k+1)*h*h)
        total+=weighted_polynomial(coeff,a,b)
    return total


def B_closed(N):
    if N%2==0:
        return (1-(pi/N)/tan(pi/N))/(4*pi*pi)
    return 1/(4*pi*pi)-1/(8*pi*N*tan(pi/(2*N)))+1/(16*N*N)


def H0_closed(N):
    return 0.5-(N/(4*pi))*sin(2*pi/N)


def gamma_critical(N):
    H=H0_closed(N)
    B=B_closed(N)
    denominator=4*pi*pi*B/N - pi*pi*H/(3*N*N)
    assert denominator>0
    return H/denominator


def solve(A,b):
    n=len(b)
    A=[r[:] for r in A]
    b=b[:]
    for j in range(n):
        p=max(range(j,n),key=lambda k:abs(A[k][j]))
        if p!=j:A[j],A[p]=A[p],A[j];b[j],b[p]=b[p],b[j]
        assert abs(A[j][j])>1e-14
        pivot=A[j][j]
        for k in range(j+1,n):
            c=A[k][j]/pivot
            for r in range(j+1,n):A[k][r]-=c*A[j][r]
            b[k]-=c*b[j]
            A[k][j]=0
    x=[0.]*n
    for j in reversed(range(n)):
        x[j]=(b[j]-sum(A[j][k]*x[k] for k in range(j+1,n)))/A[j][j]
    return x


def run():
    cases=0
    for N in range(2,13):
        B=bubble_integral(N)
        H=[hat_integral(N,j) for j in range(N)]
        H0=H0_closed(N)
        assert abs(H0-H[0]) < 8e-11, (N,H0,H[0])
        assert abs(B-B_closed(N)) < 8e-11, (N,B,B_closed(N))
        assert all(h>=H0-2e-12 for h in H)
        crit=gamma_critical(N)
        for mult in (0.5,0.9,1.1,2.0):
            gamma=crit*mult
            corr=(4*pi*pi*gamma*B/N)/(1+pi*pi*gamma/(3*N*N))
            w_formula=[hj-corr for hj in H]
            K=[[kernel(i/N,j/N,gamma) for j in range(N)] for i in range(N)]
            kapp=[kappa(i/N,gamma) for i in range(N)]
            w_solved=solve(K,kapp)
            residual=max(abs(sum(K[i][j]*w_formula[j] for j in range(N))-kapp[i]) for i in range(N))
            discrepancy=max(abs(w_formula[i]-w_solved[i]) for i in range(N))
            assert residual<4e-9, (N,mult,residual)
            assert discrepancy<4e-9, (N,mult,discrepancy)
            if mult<1:
                assert min(w_solved) > -3e-9
            else:
                assert w_solved[0] < 3e-9
            cases+=1
    for N in (100,200,400,800):
        gap=gamma_critical(N)-N
        assert abs(gap-pi*pi/3)<0.1, (N,gap)
    print('VERIFY_OK',cases,'direct linear-system comparisons; asymptotic checks passed')

if __name__ == '__main__':
    run()
