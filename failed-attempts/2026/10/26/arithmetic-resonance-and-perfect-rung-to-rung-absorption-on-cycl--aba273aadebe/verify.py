#!/usr/bin/env python3
"""Finite checks for a single absorbing vertex on an unweighted prism."""
import math
import numpy as np

def algebraic_formula(n):
    d = n//2 + 1
    overlaps = 2 * (n % 4 == 0) + (n % 6 == 0)
    R = 2*d - overlaps
    S = (8/(3*n))*(n%4==0) + (2/n)*(n%6==0)
    return R, S

def adjacency(n):
    A = np.zeros((2*n,2*n),dtype=float)
    for j in range(n):
        for ell in range(2):
            a,b=2*j+ell,2*((j+1)%n)+ell
            A[a,b]=A[b,a]=1
        A[2*j,2*j+1]=A[2*j+1,2*j]=1
    return A

def projection_checks(n):
    eigen,vec=np.linalg.eigh(adjacency(n))
    groups=[]
    for i,e in enumerate(eigen):
        if not groups or abs(e-groups[-1][0])>1e-7:groups.append([e,[i]])
        else:groups[-1][1].append(i)
    source=np.zeros(2*n);source[1]=1
    trap=np.zeros(2*n);trap[0]=1
    bright_count=0
    survival=0.
    for e,idx in groups:
        mat=vec[:,idx]
        p=mat.T@trap
        z=mat.T@source
        norm=float(p@p)
        if norm>1e-8:
            bright_count+=1
            survival+=float(z@z-(p@z)**2/norm)
        else:survival+=float(z@z)
    return bright_count,survival

def trig_collision_checks(n):
    A=[2*math.cos(2*math.pi*j/n) for j in range(n//2+1)]
    ans=[]
    for j,a in enumerate(A):
        for k,b in enumerate(A):
            if abs(a-b-2)<1e-9:
                ans.append((j,k))
    want=[]
    if n%4==0:
        want.extend([(0,n//4),(n//4,n//2)])
    if n%6==0:
        want.append((n//6,n//3))
    assert sorted(ans)==sorted(want),(n,ans,want)

def run():
    count=0
    for n in range(3,43):
        trig_collision_checks(n); count+=1
        r,s=algebraic_formula(n)
        rr,ss=projection_checks(n)
        assert rr==r,(n,rr,r)
        assert abs(ss-s)<1e-8,(n,ss,s)
        count+=2
    # A few independently exact rational Krylov ranks from integer matrices.
    import sympy as sp
    for n in (3,4,5,6,7,8,9,10):
        A=sp.Matrix(adjacency(n).astype(int))
        x=sp.zeros(2*n,1);x[0]=1
        cols=[]
        for k in range(2*n):
            cols.append(x)
            x=A*x
        rank=sp.Matrix.hstack(*cols).rank()
        assert rank==algebraic_formula(n)[0],(n,rank)
        count+=1
    print("PASS", count, "analytic/spectral/independent-integer-Krylov checks")
if __name__=="__main__":run()
