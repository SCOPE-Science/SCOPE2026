#!/usr/bin/env python3
"""Reproduce finite tests for the weighted circular-ladder controllability theorem.
Uses Python standard library only. The all-size proof is in RESULT.md.
"""
from fractions import Fraction
from math import cos, sin, pi

def rank(A, tol=0):
    if not A:return 0
    B=[list(row) for row in A]; nr=len(B); nc=len(B[0]); rr=0
    for j in range(nc):
        if rr==nr:break
        i=max(range(rr,nr),key=lambda z:abs(B[z][j]))
        if abs(B[i][j])<=tol:continue
        B[rr],B[i]=B[i],B[rr]
        q=B[rr][j]
        B[rr]=[v/q for v in B[rr]]
        for k in range(rr+1,nr):
            q=B[k][j]
            if q:
                B[k]=[v-q*w for v,w in zip(B[k],B[rr])]
        rr+=1
    return rr

def analytic_cycle(m):
    out=[]
    for j in range(m//2+1):
        theta=2*pi*j/m
        nu=2-2*cos(theta)
        if j==0:vectors=[[1.0]*m]
        elif m%2==0 and j==m//2:vectors=[[(-1.0)**x for x in range(m)]]
        else:vectors=[[cos(theta*x) for x in range(m)],[sin(theta*x) for x in range(m)]]
        out.append((nu,vectors))
    return out

def restricted_spectrum(m,t,cyc):
    spec=[]
    for j,(nu,vecs) in enumerate(cyc):
        for b in (0,1):
            cols=[]
            for v in vecs:
                cols.append((nu+2*b*t,[v[x]*((-1)**(b*y)) for x in range(m) for y in range(2)],j,b))
            spec+=cols
    return spec

def grouped(spec,eps):
    gs=[]
    for rec in spec:
        for g in gs:
            if abs(g[0][0]-rec[0])<eps:
                g.append(rec);break
        else:gs.append([rec])
    return gs

def apply_l(m,t,v):
    return [2*v[2*x+y]-v[2*((x+1)%m)+y]-v[2*((x-1)%m)+y]+t*(v[2*x+y]-v[2*x+1-y]) for x in range(m) for y in (0,1)]

def float_tests():
    cases=0; ranks=0; modes=0
    for m in range(3,24):
        cyc=analytic_cycle(m)
        nu=[s[0] for s in cyc]
        ts={0.371} | {(nu[k]-nu[j])/2 for j in range(len(nu)) for k in range(j+1,len(nu))}
        for t in ts:
            spec=restricted_spectrum(m,t,cyc)
            gs=grouped(spec,1e-9)
            k=max(len(g) for g in gs)
            k=max(2,k)
            if k==2: sites=[(0,0),(1,0)]
            elif k==3:sites=[(0,0),(1,0),(0,1)]
            elif k==4:sites=[(0,0),(1,0),(0,1),(1,1)]
            else:raise AssertionError((m,t,k))
            rr=[2*x+y for x,y in sites]
            for g in gs:
                A=[[rec[1][i] for rec in g] for i in rr]
                if rank(A,1e-8)!=len(g):raise AssertionError(('PBH',m,t,k,len(g),A))
                ranks+=1
            # For each modal column, independently check the graph eigen-equation.
            for eig,v,_,_ in spec:
                w=apply_l(m,t,v)
                if max(abs(a-eig*b) for a,b in zip(w,v))>1e-9:
                    raise AssertionError(('eigenvector',m,t,eig))
                modes+=1
            cases+=1
    return cases,ranks,modes

# Entire eigenspaces and actuator PBH ranks over rationals for spectra of 3,4,6-cycles.
cycle_basis={
 3:{0:(0,[[1,1,1]]),1:(3,[[2,-1,-1],[0,1,-1]])},
 4:{0:(0,[[1,1,1,1]]),1:(2,[[1,0,-1,0],[0,1,0,-1]]),2:(4,[[1,-1,1,-1]])},
 6:{0:(0,[[1]*6]),1:(1,[[2,1,-1,-2,-1,1],[0,1,1,0,-1,-1]]),2:(3,[[2,-1,-1,2,-1,-1],[0,1,-1,0,1,-1]]),3:(4,[[1,-1,1,-1,1,-1]])}
}

def exact_tests():
    cases=ranks=modes=0
    for m,cycles in cycle_basis.items():
        nu=[cycles[j][0] for j in cycles]
        ts={Fraction(7,10)}|{Fraction(nu[k]-nu[j],2) for j in range(len(nu)) for k in range(j+1,len(nu))}
        for t in ts:
            spec=[]
            for j,(nu_j,vecs) in cycles.items():
                for b in (0,1):
                    for v in vecs:
                        spec.append((Fraction(nu_j)+2*b*t,[Fraction(v[x]*((-1)**(b*y))) for x in range(m) for y in (0,1)]))
            if rank([[v[i] for _,v in spec] for i in range(2*m)])!=2*m:raise AssertionError(('basis',m))
            for eig,v in spec:
                if apply_l(m,t,v)!=[eig*vi for vi in v]:raise AssertionError(('exact eigenequation',m,t))
                modes+=1
            gs=[]
            for rec in spec:
                for g in gs:
                    if g[0][0]==rec[0]:g.append(rec);break
                else:gs.append([rec])
            k=max(2,max(len(g) for g in gs))
            sites={2:[(0,0),(1,0)],3:[(0,0),(1,0),(0,1)],4:[(0,0),(1,0),(0,1),(1,1)]}[k]
            for g in gs:
                mat=[[col[1][2*x+y] for col in g] for x,y in sites]
                assert rank(mat)==len(g),(m,t,len(g),mat)
                ranks+=1
            cases+=1
    return cases,ranks,modes

if __name__=='__main__':
    a=exact_tests();b=float_tests()
    print('EXACT_CASES=%d EXACT_PBH_RANKS=%d EXACT_EIGENVECTORS=%d'%a)
    print('FLOAT_CASES=%d FLOAT_PBH_RANKS=%d FLOAT_EIGENVECTORS=%d'%b)
    print('VERIFY_OK')
