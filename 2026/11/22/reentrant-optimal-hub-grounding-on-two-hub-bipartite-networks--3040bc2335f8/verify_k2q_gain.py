#!/usr/bin/env python3
"""Exact and numerical checks for two-hub bipartite grounding allocation.

Uses Python standard library. Finite tests corroborate, but do not replace,
the all-size matrix and convexity proof in the accompanying result.
"""
from fractions import Fraction as Q
from math import sqrt

checks=0

def check(statement, why='failed'):
    global checks
    assert statement,why
    checks+=1

def f(q,x,y):
    D=2*x+q*y+x*y
    return 1/(q+x)+(q-1)/(2+y)+(q+2+x+y)/D

def fx(q,x,y):
    D=2*x+q*y+x*y;N=q+2+x+y
    return -1/(q+x)**2 +(D-N*(2+y))/D**2

def fy(q,x,y):
    D=2*x+q*y+x*y;N=q+2+x+y
    return -(q-1)/(2+y)**2 +(D-N*(q+x))/D**2

def inverse(A):
    n=len(A)
    M=[[Q(v) for v in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if M[i][j])
        M[j],M[k]=M[k],M[j]
        z=M[j][j];M[j]=[v/z for v in M[j]]
        for i in range(n):
            if i!=j:
                z=M[i][j];M[i]=[v-z*w for v,w in zip(M[i],M[j])]
    return [row[n:] for row in M]

def lap_plus(q,x,y):
    n=q+2;M=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(2):M[i][i]=q+x
    for j in range(2,n):
        M[j][j]=2+y
        for i in range(2):M[i][j]=M[j][i]=-1
    return M

def hub_boundary(q,t):
    return fx(q,Q(0),t)-Q(2,q)*fy(q,Q(0),t)

def periphery_boundary(q,t):
    return fy(q,t,Q(0))-Q(q,2)*fx(q,t,Q(0))

def roots(q):
    # (t+2)^3=q(q-1)t, exactly two roots when q>=6.
    def H(t):return q*(q-1)*t-(t+2)**3
    if q<=5:return None
    lo,hi=0.,1.
    for _ in range(75):
        mid=(lo+hi)/2
        if H(mid)>=0:hi=mid
        else:lo=mid
    minus=(lo+hi)/2
    lo,hi=1.,float(q+10)
    for _ in range(75):
        mid=(lo+hi)/2
        if H(mid)>=0:lo=mid
        else:hi=mid
    return minus,(lo+hi)/2

def optimal(q,B):
    # Strictly convex one-dimensional reduced cost, derivative bisection.
    B=float(B)
    def deriv(y):
        x=(B-q*y)/2
        return float(fy(q,x,y)-q/2*fx(q,x,y))
    if deriv(B/q)<=0:return 0.,B/q
    if deriv(0)>=0:raise ArithmeticError('zero-peripheral endpoint must be excluded')
    lo,hi=0.,B/q
    for _ in range(70):
        mid=(lo+hi)/2
        if deriv(mid)<0:lo=mid
        else:hi=mid
    y=(lo+hi)/2
    return (B-q*y)/2,y

# Independent complete-matrix inverse, exact rational arithmetic.
for q in range(3,11):
    for x in [Q(0),Q(1,4),Q(1),Q(5)]:
        for y in [Q(0),Q(1,3),Q(1),Q(4)]:
            if x==0 and y==0:continue
            Z=inverse(lap_plus(q,x,y))
            check(sum(Z[i][i] for i in range(q+2)) == f(q,x,y),
                  f'inverse trace identity q={q}, x={x}, y={y}')
            check(all(Z[i][i]>0 for i in range(q+2)))

# Independent rational derivative identities for both endpoints.
for q in range(3,121):
    for t in [Q(1,11),Q(2,5),Q(1),Q(7,3),Q(12)]:
        h=hub_boundary(q,t)
        expected=2*(q*(q-1)*t-(t+2)**3)/(q*q*t*(t+2)**2)
        check(h==expected,f'hub marginal identity q={q},t={t}')
        check(periphery_boundary(q,t)<0,'peripheral-only support cannot vanish')

# Exactly no zero-hub regime at q=3,4,5; one interval at every q>=6.
for q in range(3,101):
    R=roots(q)
    if q<=5:
        check(R is None)
        check(q*(q-1)<27)
    else:
        a,b=R
        check(0<a<1<b)
        check(abs(q*(q-1)*a-(a+2)**3)<1e-8*max(1.,q*q*a))
        check(abs(q*(q-1)*b-(b+2)**3)<1e-8*max(1.,q*q*b))
        for t in [0.5*a,0.5*(a+1),0.5*(b+1),b+3]:
            check((hub_boundary(q,t)>=0)==(a<t<b))

# Compute optimal gains by bisection and compare their support and costs.
for q in range(3,41):
    R=roots(q)
    for B in [0.02,0.1,0.5,1.,2.,3.,5.,10.,30.,100.,1000.]:
        x,y=optimal(q,B)
        check(abs(2*x+q*y-B)<1e-9)
        check(x>=-1e-8 and y>0)
        predicted=R is not None and q*R[0]<=B<=q*R[1]
        check((abs(x)<1e-8)==predicted, f'support q={q}, B={B}')
        for other_y in [B/(q+2),B/(2*q),B/q]:
            ox=(B-q*other_y)/2
            if ox>=0:check(f(q,x,y)<=f(q,ox,other_y)+1e-9)

# Exact integer transition in q and two differing asymptotic budget scales.
check(5*4<27<6*5)
for q in [1000,10000,100000]:
    a,b=roots(q)
    check(abs((q*a)*q/8-1)<0.012)
    check(abs((q*b)/(q*q)-1)<0.012)
check(abs(6*roots(6)[0]-3.346799653263696)<1e-9)
check(abs(6*roots(6)[1]-10.38249485813736)<1e-9)
print('PASS:',checks,'rational and numerical assertions')
