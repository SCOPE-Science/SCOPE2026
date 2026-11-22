#!/usr/bin/env python3
"""Independent, finite algebraic and numerical diagnostics; not a proof of global counts."""
from fractions import Fraction as Q
from math import isclose, sqrt


def mat(a, b):
    return ((Q(1), a, b), (b, Q(1), a), (a, b, Q(1)))


def F(p, R, a, b):
    C = mat(a, b)
    return tuple(p[i]*(Q(1)+R-R*sum(C[i][j]*p[j] for j in range(3)))
                 for i in range(3))


def J(p, R, a, b):
    C = mat(a, b)
    return tuple(tuple((Q(1)+R-R*sum(C[i][k]*p[k] for k in range(3)) if i == j else Q(0))
                       -R*p[i]*C[i][j] for j in range(3)) for i in range(3))


def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def zero_roots(R, a, b):
    h = Q(1)+Q(1)/R
    points = [(Q(0), Q(0), Q(0))]
    for i in range(3):
        p=[Q(0)]*3; p[i]=h; points.append(tuple(p))
    if (a-Q(1))*(b-Q(1))>0:
        x = h*(Q(1)-a)/(Q(1)-a*b)
        y = h*(Q(1)-b)/(Q(1)-a*b)
        for i in range(3):
            p=[Q(0)]*3; p[i]=x; p[(i+1)%3]=y; points.append(tuple(p))
    points.append((h/(Q(1)+a+b),)*3)
    return points


def solve3(A, v):
    M=[list(map(float,A[i]))+[float(v[i])] for i in range(3)]
    for k in range(3):
        pivot=max(range(k,3),key=lambda i:abs(M[i][k]))
        M[k],M[pivot]=M[pivot],M[k]
        assert abs(M[k][k])>1e-10
        t=M[k][k]
        for j in range(k,4):M[k][j]/=t
        for i in range(3):
            if i!=k:
                t=M[i][k]
                for j in range(k,4): M[i][j]-=t*M[k][j]
    return [M[i][3] for i in range(3)]


def local_inverse(q, R, a, b, u):
    p=list(map(float,q))
    for _ in range(20):
        f=F(p,R,a,b)
        step=solve3(J(p,R,a,b), [f[i]-u[i] for i in range(3)])
        p=[p[i]-step[i] for i in range(3)]
        if max(map(abs,step))<1e-12: break
    assert max(abs(float(F(p,R,a,b)[i])-u[i]) for i in range(3))<1e-9
    return p


def run():
    R=Q(7,5)
    u=[1e-6,2e-6,3e-6]
    for a,b,zero_count,positive_count in [
       (Q(1,2),Q(3,4),8,8),
       (Q(2),Q(3),8,2),
       (Q(1,2),Q(3,2),5,2),
    ]:
        points=zero_roots(R,a,b)
        assert len(set(points))==zero_count
        assert all(all(t==0 for t in F(q,R,a,b)) for q in points)
        assert all(det(J(q,R,a,b))!=0 for q in points)
        D=((a-Q(1))**2+(b-Q(1))**2+(a-b)**2)/2
        assert D>0
        if zero_count==8:
            h=Q(1)+Q(1)/R
            for q in points:
                if sum(int(v>0) for v in q)==2:
                    m=[i for i,v in enumerate(q) if v==0][0]
                    assert J(q,R,a,b)[m][m]==(R+1)*D/(1-a*b)
        ancestors=[local_inverse(q,R,a,b,u) for q in points]
        assert sum(all(t>0 for t in q) for q in ancestors)==positive_count
        print(f'a={a}, b={b}: zero-fiber={zero_count}; small-positive-target={positive_count}')
    R=float(R)
    T=sum(u)
    qplus=(1+R+sqrt((1+R)**2-4*R*T))/2
    qminus=(1+R-sqrt((1+R)**2-4*R*T))/2
    assert qplus>0 and qminus>0
    for q in [qplus,qminus]:
        p=[v/q for v in u]
        assert max(abs(float(F(p,R,1.,1.)[i])-u[i]) for i in range(3))<1e-9
    print('Equal-interaction endpoint: two positive inverse branches verified.')
    print('All finite diagnostics passed; uniformity follows from the analytic proof.')

if __name__=='__main__':run()
