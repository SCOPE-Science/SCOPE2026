"""Exact and numerical checks for the nonlinear diffusion EIN comparison threshold.

Runs with Python 3, using only the standard library. Finite tests supplement,
not replace, the all-dimensional proof.
"""
from fractions import Fraction as F
from math import tanh, cosh, log
from random import Random

checks = 0

def check(b, msg):
    global checks
    checks += 1
    if not b:
        raise AssertionError(msg)

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def mm(a,v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]

def inverse(m):
    n=len(m)
    a=[row[:] + idrow for row,idrow in zip(m,eye(n))]
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None: raise ValueError('singular')
        a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        a[j]=[x/pivot for x in a[j]]
        for k in range(n):
            if k!=j:
                f=a[k][j]
                a[k]=[x-f*y for x,y in zip(a[k],a[j])]
    return [row[n:] for row in a]

def makeq(rates):
    n=len(rates)
    q=[r[:] for r in rates]
    for i in range(n):
        q[i][i]=-sum(q[i][j] for j in range(n) if j!=i)
    return q

def stationary(q):
    n=len(q)
    a=[[q[j][i] for j in range(n)] for i in range(n)]
    a[-1]=[F(1)]*n
    return mm(inverse(a),[F(0)]*(n-1)+[F(1)])

def resolvent(q,t):
    n=len(q)
    return inverse([[F(int(i==j))-t*q[i][j] for j in range(n)] for i in range(n)])

def update_linear(p, alpha, A, u):
    return [u[i]+(A/alpha)*sum((p[i][j]-F(int(i==j)))*u[j] for j in range(len(u))) for i in range(len(u))]

samples=[
    [[F(0),F(2)],[F(5),F(0)]],
    [[F(0),F(3),F(0)],[F(0),F(0),F(5)],[F(7),F(0),F(0)]],
    [[F(0),F(2),F(1)],[F(1),F(0),F(4)],[F(6),F(2),F(0)]],
    [[F(0),F(3),F(0),F(1)],[F(4),F(0),F(2),F(0)],
     [F(0),F(5),F(0),F(7)],[F(3),F(0),F(6),F(0)]],
]
A=F(3)
for rates in samples:
    q=makeq(rates)
    n=len(q)
    pi=stationary(q)
    check(sum(pi)==1 and all(x>0 for x in pi),'stationary probabilities')
    check(all(z==0 for z in mm([[q[j][i] for j in range(n)] for i in range(n)],pi)),'stationarity')
    for t in [F(1,200),F(1,2),F(1),F(3),F(10),F(120),F(10000)]:
        p=resolvent(q,t)
        check(all(sum(row)==1 and all(z>=0 for z in row) for row in p),'stochastic resolvent')
        check(all(p[i][i]>=pi[i] for i in range(n)),'return bound')
        for a in [A/2, A*(1-min(pi)), A*(1-min(pi))+F(1,10)]:
            H=[[F(int(i==j))+(A/a)*(p[i][j]-F(int(i==j))) for j in range(n)] for i in range(n)]
            check(all(sum(r)==1 for r in H),'constant preservation')
            u=[F(j-n//2) for j in range(n)]
            check(update_linear(p,a,A,u)==mm(H,u),'linear update')
            if a>=A*(1-min(pi)):
                check(all(z>=0 for row in H for z in row),'order threshold sufficiency')
            if a>=A/2:
                v=mm(H,u)
                energy=lambda v:sum(pi[i]*v[i]*v[i] for i in range(n))
                check(energy(v)<=energy(u),'linear energy dissipation')
    a=A*(1-min(pi))-F(1,20)
    if a>0:
        p=resolvent(q,F(10**8))
        i=min(range(n),key=lambda j:pi[j])
        Hii=1+(A/a)*(p[i][i]-1)
        check(Hii<0,'sharp negative self derivative')

rng=Random(20261106)
for rates in samples:
    q=makeq(rates)
    n=len(q)
    pi=stationary(q)
    a=float(A*(1-min(pi)))
    # Scalar monotone flux A*tanh(s) has derivative in [0,A].
    for _ in range(50):
        u=[rng.uniform(-2,2) for j in range(n)]
        v=[rng.uniform(-2,2) for j in range(n)]
        t=F(rng.randint(1,25),10)
        p=resolvent(q,t)
        def nonlinear(x):
            return [x[i]+sum(float(p[i][j]-F(int(i==j)))*3*tanh(x[j])/a for j in range(n)) for i in range(n)]
        E=lambda x:sum(float(pi[i])*3*log(cosh(x[i])) for i in range(n))
        y=nonlinear(u)
        check(E(y)<=E(u)+1.e-11,'nonlinear potential energy')
        w=[max(u[i],v[i]) for i in range(n)]
        U=nonlinear(w)
        for x in (u,v):
            Y=nonlinear(x)
            check(all(Y[j]<=U[j]+1.e-11 for j in range(n)),'nonlinear order preserving')
print(f'PASS: {checks} exact-rational and nonlinear numerical assertions')
