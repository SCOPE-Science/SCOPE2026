#!/usr/bin/env python3
"""Reproduce scalar and finite-matrix checks for a clipped rank-two base polytope."""
from decimal import Decimal, getcontext
from itertools import combinations
getcontext().prec = 70
D = Decimal
TOL = D('1e-45')

def root(a,b):
    a,b=D(a),D(b)
    def derivative(p):
        return a/p - D(1)/(D(1)-p) + (b-D(1))*(D(3)-b)/(D(2)*(b-D(2))+(D(3)-b)*p)
    lo=D('1e-65'); hi=D(1)-lo
    for _ in range(290):
        mid=(lo+hi)/2
        if derivative(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def check(a,b, matrix=False):
    a0,b0=a,b
    a,b=D(a),D(b)
    n=int(a+b); d=n-1
    p=root(a,b)
    qA=p/a
    qB=(D(2)*(b-D(2))+(D(3)-b)*p)/(b*(b-D(1)))
    kap=D(1)/a+D(1)/b
    qT=p*(D(1)-p)*kap
    assert all(v>0 for v in (qA,qB,qT))
    X=(a-D(1))/a/qA+(b-D(1))/b/qB+(D(1)-p)**2*kap/qT
    Y=D(2)*(b-D(2))/b/qB+p*p*kap/qT
    assert abs(X-D(d))<TOL and abs(Y-D(d))<TOL,(a,b,p,X,Y)
    if b==2: assert abs(p-D(int(a)+1)/D(int(a)+2))<TOL
    if b==3: assert abs(p-a/(a+D(1)))<TOL
    if b>=4:
        A=(a+b)*(b-D(3))
        B=-((a+b-D(1))*(b-D(3))+D(2)*(a+D(1))*(b-D(2)))
        C=D(2)*a*(b-D(2))
        assert abs(A*p*p+B*p+C)<TOL
    if not matrix: return
    # Independent full covariance computed from all embedded vertices.
    orbitX=[tuple(int(i in pair) for i in range(n)) for pair in ((i,j) for i in range(int(a)) for j in range(int(a),n))]
    orbitY=[tuple(int(i in pair) for i in range(n)) for pair in ((i,j) for i in range(int(a),n) for j in range(i+1,n))]
    weighted=[(v,p/D(len(orbitX))) for v in orbitX]+[(v,(D(1)-p)/D(len(orbitY))) for v in orbitY]
    mean=[sum(D(v[i])*w for v,w in weighted) for i in range(n)]
    expect=[p/a]*int(a)+[(D(2)-p)/b]*int(b)
    assert max(abs(x-y) for x,y in zip(mean,expect))<TOL
    C=[[sum((D(v[i])-mean[i])*(D(v[j])-mean[j])*w for v,w in weighted) for j in range(n)] for i in range(n)]
    # Direct covariance matrix must match three orthogonal projector expression.
    u=[(D(1)/a if i<int(a) else -D(1)/b)/kap.sqrt() for i in range(n)]
    for i in range(n):
        for j in range(n):
            PA=(D(int(i==j))-D(1)/a) if i<int(a) and j<int(a) else D(0)
            PB=(D(int(i==j))-D(1)/b) if i>=int(a) and j>=int(a) else D(0)
            expected=qA*PA+qB*PB+qT*u[i]*u[j]
            assert abs(C[i][j]-expected)<TOL,(i,j,C[i][j],expected)
    # Every individual contact, evaluated in a second independent route.
    for v,w in weighted:
        wA=[D(v[i])-D(sum(v[:int(a)]))/a for i in range(int(a))]
        wB=[D(v[i])-D(sum(v[int(a):]))/b for i in range(int(a),n)]
        axis=sum((D(v[i])-mean[i])*u[i] for i in range(n))
        mahal=sum(x*x for x in wA)/qA+sum(x*x for x in wB)/qB+axis*axis/qT
        assert abs(mahal-D(d))<TOL,(a,b,mahal)

if __name__=='__main__':
    scalar=matrices=0
    for a in range(2,21):
        for b in range(2,21):
            check(a,b,False);scalar+=1
    for a in range(2,9):
        for b in range(2,9):
            check(a,b,True);matrices+=1
    print(f'CLIPPED_RANK2_LOEWNER_PASS scalar={scalar} full_covariance_and_contacts={matrices}')
