#!/usr/bin/env python3
"""Finite computational checks for the Euclidean inball of clique-joined odd-cycle stable-set polytopes."""
import math
import numpy as np
from scipy.optimize import linprog

def graph_vertices(a, t):
    m = 2*a+1
    pts=[]
    for mask in range(1<<m):
        if any((mask>>i)&1 and (mask>>((i+1)%m))&1 for i in range(m)):
            continue
        pts.append([int(bool(mask&(1<<i))) for i in range(m)]+[0]*t)
    for j in range(t):
        v=[0]*(m+t); v[m+j]=1
        pts.append(v)
    return np.asarray(pts,dtype=float)

def inequalities(a,t):
    m=2*a+1; d=m+t
    A=[]; b=[]; lab=[]
    for i in range(d):
        v=np.zeros(d);v[i]=-1
        A.append(v);b.append(0);lab.append(("coordinate",i))
    for i in range(m):
        v=np.zeros(d);v[i]=v[(i+1)%m]=1;v[m:]=1
        A.append(v);b.append(1);lab.append(("clique",i))
    v=np.ones(d);v[m:]=a
    A.append(v);b.append(a);lab.append(("odd_cycle",0))
    return np.asarray(A),np.asarray(b),lab

def check(a,t):
    m=2*a+1; d=m+t
    verts=graph_vertices(a,t)
    A,b,labels=inequalities(a,t)
    assert len(verts)>d and np.linalg.matrix_rank(verts-verts[0])==d
    assert np.max(A@verts.T-b[:,None])<=1e-9
    # Every asserted inequality is a genuine facet: tight vertices span dimension d-1.
    for h,beta in zip(A,b):
        tight=verts[np.abs(verts@h-beta)<1e-9]
        assert len(tight)>=d
        assert np.linalg.matrix_rank(tight-tight[0],tol=1e-8)==d-1
    C=np.column_stack([A, np.linalg.norm(A,axis=1)])
    sol=linprog(-np.r_[np.zeros(d),1.],A_ub=C,b_ub=b,
         bounds=[(None,None)]*(d+1),method="highs")
    assert sol.success
    r_edge=1/(t+2+math.sqrt(t+2))
    r_odd=a/(m+a*t+math.sqrt(m+a*a*t))
    r=min(r_edge,r_odd)
    assert abs(sol.x[-1]-r)<1e-8
    assert np.max(np.abs(sol.x[:d]-r))<1e-7
    gap=b-C@np.r_[np.ones(d)*r,r]
    assert min(gap)>-1e-9
    contacts=sum(abs(u)<1e-8 for u in gap)
    tcrit=a*a-2*a-1
    expected=d+(m if t<=tcrit else 0)+(1 if t>=tcrit else 0)
    assert contacts==expected,(a,t,contacts,expected)
    if t==tcrit: assert abs(r-1/(a*(a-1)))<1e-12
    return len(verts),len(A),contacts

def main():
    tested=0; totalvert=0; totalfac=0
    cases=[]
    for a in range(2,7):
        s=a*a-2*a-1
        for t in sorted(set([1,2,3,max(1,s-1),max(1,s),max(1,s+1)])):
            cases.append((a,t))
    for a,t in cases:
        nv,nf,nc=check(a,t)
        tested+=1; totalvert+=nv; totalfac+=nf
    print("ODD_WHEEL_JOIN_INBALL_CHECKS_PASSED",tested,totalvert,totalfac)

if __name__=="__main__":
    main()
