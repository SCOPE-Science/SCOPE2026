"""Finite diagnostics for the stated sharp spectral-window envelope.

Requires Python 3 standard library only. The analytic proof establishes the theorem.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose
from random import Random


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def rank_one(x, y):
    return [[a * b for b in y] for a in x]


def apply(a, x):
    return [dot(row, x) for row in a]


def near(a, b, tol=3e-11):
    assert abs(a-b) <= tol * (1 + abs(a) + abs(b)), (a, b)


assertions = 0
for uv in [(F(3,13),F(4,13),F(12,13)),
           (F(1,5),F(2,5),F(2,5),F(4,5))]:
    n=len(uv)
    assert dot(uv,uv)==1
    P=rank_one(uv,uv)
    Q=[[(F(i==j)-P[i][j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert dot(Q[i], [Q[k][j] for k in range(n)])==Q[i][j]
            assert dot(P[i], [P[k][j] for k in range(n)])==P[i][j]
            assert dot(P[i], [Q[k][j] for k in range(n)])==0
            assertions += 3
    for i in range(n):
        for j in range(i+1,n):
            vi=[float(Q[k][i]) for k in range(n)]
            vj=[float(Q[k][j]) for k in range(n)]
            ui,uj=map(float,(uv[i],uv[j]))
            alpha=sqrt(1-ui*ui);beta=sqrt(1-uj*uj)
            c=dot(vi,vj)
            near(c,-ui*uj)
            for sign in (-1,1):
                z=[x/alpha+sign*y/beta for x,y in zip(vi,vj)]
                z=[x/sqrt(dot(z,z)) for x in z]
                # S z = ((c + sign*alpha*beta)/2) z
                Sz=[(vi[k]*dot(vj,z)+vj[k]*dot(vi,z))/2 for k in range(n)]
                eigenvalue=(c+sign*alpha*beta)/2
                for k in range(n):
                    near(Sz[k],eigenvalue*z[k]);assertions+=1
                for t in (0.02,.2,1.,4.):
                    a=exp(-2*t);b=exp(-t)
                    # E = P + aQ + (b-a)zz^T
                    Eij=ui*uj+a*float(Q[i][j])+(b-a)*z[i]*z[j]
                    endpoint=ui*uj*(1-(a+b)/2)+sign*(b-a)*alpha*beta/2
                    near(Eij,endpoint);assertions+=1

# Random rank-one effects lie in the spectral order interval and obey both bounds.
rng=Random(2206)
for n in (3,4,7):
    for _ in range(120):
        u=[.03+rng.random() for _ in range(n)]
        norm=sqrt(dot(u,u));u=[v/norm for v in u]
        y=[rng.gauss(0,1) for _ in range(n)]
        proj=dot(u,y);v=[y[k]-proj*u[k] for k in range(n)]
        vnorm=sqrt(dot(v,v));v=[x/vnorm for x in v]
        for t in (.03,.4,1.3,4.5):
            a=exp(-1.8*t);b=exp(-.6*t)
            for i in range(n):
                for j in range(i+1,n):
                    # K=vv^T, E=P+aQ+(b-a)K.
                    entry=u[i]*u[j]*(1-a)+(b-a)*v[i]*v[j]
                    A=sqrt((1-u[i]*u[i])*(1-u[j]*u[j]))
                    lower=u[i]*u[j]*(1-(a+b)/2)-(b-a)*A/2
                    upper=u[i]*u[j]*(1-(a+b)/2)+(b-a)*A/2
                    assert lower-1e-11<=entry<=upper+1e-11
                    assertions+=1

# The time-threshold criterion and the persistent negative witness.
u=[3/13,4/13,12/13]
r=[sqrt(1-x*x)/x for x in u]
R=max(r[i]*r[j] for i in range(3) for j in range(i+1,3))
near(R,sqrt(170))
delta=1.0
T=log((R-1)/2)
for t in (.001,T/2,T,T+1):
    a=exp(-2*t);b=exp(-t)
    lower=u[0]*u[1]*(1-(a+b)/2)-(b-a)*sqrt((1-u[0]**2)*(1-u[1]**2))/2
    if t<T-1e-8: assert lower<0
    if t>T+1e-8: assert lower>0
    if abs(t-T)<1e-8: near(lower,0)
    assertions+=1
print("PASS:",assertions,"exact rational and floating finite diagnostic assertions")
print("Example: R=",R,"sharp onset=",T)
