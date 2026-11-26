#!/usr/bin/env python3
"""Reproducible calculations for the powered graph-distance threshold of K_{m,n}-e.
All code uses the Python standard library. This is auxiliary finite testing;
the proof of the all-order statement is analytic.
"""
from collections import deque
from fractions import Fraction
from math import exp, log, isclose
import random


def graph_distances(m, n):
    assert min(m,n)>=2
    k=m+n
    nbr=[[] for _ in range(k)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0: continue
            u,v=i,m+j
            nbr[u].append(v); nbr[v].append(u)
    D=[]
    for source in range(k):
        dist=[-1]*k; dist[source]=0; que=deque([source])
        while que:
            u=que.popleft()
            for v in nbr[u]:
                if dist[v]<0: dist[v]=dist[u]+1;que.append(v)
        assert all(v>=0 for v in dist)
        D.append(dist)
    return D


def schur(m, n, p):
    M,N=m-1,n-1
    a=2.0**p; h=3.0**p-1
    den=a*a*m*n-h*h*M*N
    assert den>0 or p>1
    return a*(1/M+1/N)-2*(a-1)-a*a*(a*n/M+a*m/N-2*h)/den


def critical(m,n):
    assert min(m,n)>=2 and m+n>=5
    lo,hi=0.0,1.0
    assert schur(m,n,lo)>0
    assert schur(m,n,hi)<1e-12
    for _ in range(90):
        mid=(lo+hi)/2
        if schur(m,n,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def form_from_dist(D, p, z):
    assert abs(sum(z))<1e-9
    return sum(z[i]*z[j]*D[i][j]**p for i in range(len(z)) for j in range(len(z)) if i!=j)


def form_reduced(m,n,p,S,x,y):
    M,N=m-1,n-1
    a=2**p;h=3**p-1
    norm=x*x+(S-x)**2/M+y*y+(-S-y)**2/N
    return -a*norm+2*(a-1)*S*S+2*h*x*y


def jacobi_eig(A):
    A=[row[:] for row in A]
    N=len(A)
    for _ in range(50*N*N):
        p,q=max(((i,j) for i in range(N) for j in range(i+1,N)),key=lambda ij:abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<1e-11:break
        from math import atan2,cos,sin
        theta=0.5*atan2(2*A[p][q], A[q][q]-A[p][p])
        c,s=cos(theta),sin(theta)
        app,aqq,apq=A[p][p],A[q][q],A[p][q]
        A[p][p]=c*c*app-2*c*s*apq+s*s*aqq
        A[q][q]=s*s*app+2*c*s*apq+c*c*aqq
        A[p][q]=A[q][p]=0.0
        for i in range(N):
            if i==p or i==q:continue
            aip,aiq=A[i][p],A[i][q]
            A[i][p]=A[p][i]=c*aip-s*aiq
            A[i][q]=A[q][i]=s*aip+c*aiq
    else: raise AssertionError('Jacobi did not converge')
    return sorted(A[i][i] for i in range(N))


def projected_eig(D,p):
    k=len(D); base=k-1
    # Standard zero-mass difference basis e_i-e_base
    K=[[(D[i][j]**p-D[i][base]**p-D[base][j]**p)/(-2.0)
        if i!=j else D[i][base]**p for j in range(k-1)] for i in range(k-1)]
    return jacobi_eig(K)


def balanced_eq(n,p):
    a=2**p;h=3**p-1
    return (n-1-(n-2)*a)*(n*a+(n-1)*h)-a*a


def run():
    count=0
    rng=random.Random(733175)
    for m in range(2,10):
        for n in range(m,10):
            D=graph_distances(m,n)
            for i in range(m+n):
                for j in range(m+n):
                    expected=(0 if i==j else (2 if (i<m)==(j<m) else (3 if {i,j}=={0,m} else 1)))
                    assert D[i][j]==expected
                    count+=1
            if m+n==4: continue
            root=critical(m,n)
            if m+n==5: assert abs(root-1)<1e-10
            else: assert 0<root<1
            for p in [0.0, min(root*.65, .8),root, min(root+min(.04,(1-root)/2),1.0)]:
                vals=projected_eig(D,p)
                if p<root-1e-8: assert vals[0]>-2e-8, (m,n,p,vals[0])
                elif abs(p-root)<1e-8: assert abs(vals[0])<5e-8, (m,n,p,vals[0])
                elif p>root+1e-8: assert vals[0]<-2e-8, (m,n,p,vals[0])
                count+=1
            for _ in range(12):
                p=rng.random()
                S,x,y=[rng.uniform(-2,2) for _ in range(3)]
                z=[x]+[(S-x)/(m-1)]*(m-1)+[y]+[(-S-y)/(n-1)]*(n-1)
                v=form_from_dist(D,p,z)
                w=form_reduced(m,n,p,S,x,y)
                assert abs(v-w)<1e-9*(1+abs(w)),(m,n,p,v,w)
                count+=1
            # Verify the endpoint identity and positive finite denominator directly
            assert abs(schur(m,n,1) +2*(m+n-5)/(m+n-1))<1e-12
            assert abs(schur(m,n,0) -(1/m+1/n))<1e-12
            count+=2
    c=log(3)/(log(2)**2)
    for n in (3,4,5,8,10,30,100,300):
        p=critical(n,n)
        assert abs(balanced_eq(n,p))<1e-9
        p0=log(n/(n-1))/log(2)
        assert p>p0
        if n>=100:
            assert abs((p-p0)*n**3-c)<.04
        count+=1
    print('PASS checks:',count)
    print('p*(K_2,3-e):',critical(2,3))
    for n in (3,4,5,8,10): print('balanced',n,'p*=',f'{critical(n,n):.12f}')
    print('balanced n^-3 excess coefficient:',f'{c:.12f}')

if __name__=='__main__': run()
