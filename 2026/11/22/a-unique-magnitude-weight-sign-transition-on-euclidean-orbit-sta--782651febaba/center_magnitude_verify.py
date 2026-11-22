"""Numerical sanity checks for center-and-transitive-rim magnitude sign laws.
Not a proof of the all-scale/all-order statements. Python 3 standard library only.
"""
import math


def distances(n):
    return [2*math.sin(math.pi*j/n) for j in range(n)]


def q(n, t):
    return sum(math.exp(-t*d) for d in distances(n))


def h(n, t):
    return q(n, t)/n - math.exp(-t)


def bisect(func, lo, hi, count=90):
    assert func(lo)<0 and func(hi)>0
    for _ in range(count):
        mid=(lo+hi)/2
        if func(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def simpson(func, N=32768):
    assert N%2==0
    h=1/N
    total=func(0)+func(1)
    for j in range(1,N):
        total+=(4 if j%2 else 2)*func(j*h)
    return h*total/3


def fi(t):
    return simpson(lambda x: math.exp(-2*t*math.sin(math.pi*x)))


def ginf(t):
    return fi(t)-math.exp(-t)


def solve(A, b):
    n=len(b)
    A=[list(row)+[b[i]] for i,row in enumerate(A)]
    for j in range(n):
        k=max(range(j,n),key=lambda i: abs(A[i][j]))
        A[k],A[j]=A[j],A[k]
        v=A[j][j]
        assert abs(v)>1e-10
        for i in range(j+1,n):
            c=A[i][j]/v
            for l in range(j,n+1): A[i][l]-=c*A[j][l]
    x=[0.0]*n
    for j in range(n-1,-1,-1):
        x[j]=(A[j][n]-sum(A[j][k]*x[k] for k in range(j+1,n)))/A[j][j]
    return x


def direct_weights(n, t):
    pts=[(0.0,0.0)]+[(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n)) for j in range(n)]
    A=[[math.exp(-t*math.hypot(xi-xj,yi-yj)) for xj,yj in pts] for xi,yi in pts]
    return solve(A,[1.0]*len(pts))


count=0
# A three-point orbit on a unit sphere in R^3, with central site the origin:
# pairwise rim chord = sqrt(3) sin(theta), covering both positive-only regimes.
for theta in (0.2, math.pi/3):
    delta=math.sqrt(3)*math.sin(theta)
    mean=2*delta/3
    assert mean<=1+1e-14
    for t in (0.005,0.05,0.3,1.5,4.0,8.0):
        Q=1+2*math.exp(-delta*t)
        E=math.exp(-t)
        a=(1-E)/(Q-3*E*E)
        b=(Q-3*E)/(Q-3*E*E)
        M=[[1,E,E,E],[E,1,math.exp(-delta*t),math.exp(-delta*t)],
           [E,math.exp(-delta*t),1,math.exp(-delta*t)],
           [E,math.exp(-delta*t),math.exp(-delta*t),1]]
        direct=solve(M,[1]*4)
        assert b>0 and a>0 and abs(direct[0]-b)<1e-8
        assert all(abs(w-a)<1e-8 for w in direct[1:])
        count+=1
for n in range(3,20):
    mean=sum(distances(n))/n
    assert mean>1
    tn=bisect(lambda t:h(n,t),1e-6,6.0)
    for mult in [0.04,0.3,0.8,1.0,1.3,2.4]:
        t=tn*mult
        E=math.exp(-t);Q=q(n,t);den=Q-n*E*E
        assert den>0
        a=(1-E)/den;b=(Q-n*E)/den
        weights=direct_weights(n,t)
        assert abs(weights[0]-b)<2e-8,(n,t,weights[0],b)
        assert all(abs(w-a)<2e-8 for w in weights[1:])
        if mult<1:assert b<1e-7
        if mult>1:assert b> -1e-7
        count+=1

inf=bisect(ginf, 1e-5, 4)
D=simpson(lambda x: -2*math.sin(math.pi*x)*math.exp(-2*inf*math.sin(math.pi*x)))+math.exp(-inf)
assert D>0
K=math.pi*inf/(3*D)
for n in [3,4,5,6,8,12,16,24,48,96,192,384,768]:
    tn=bisect(lambda t:h(n,t),1e-6,5)
    assert 0<tn<inf
    for factor in [2,3]:
        tm=bisect(lambda t:h(n*factor,t),1e-6,5)
        assert tn<tm<inf,(n,factor,tn,tm,inf)
    if n>=192:
        assert abs((inf-tn)*n*n-K)<0.07, (n,tn,(inf-tn)*n*n,K)
    count+=1
print('passed:',count,'direct inversion and root comparisons')
print('limit t:',repr(inf),'D:',repr(D),'K:',repr(K))
