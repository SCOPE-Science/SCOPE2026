"""Independent finite checks for spectral-cone semigroup sign and norm formulas."""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np
from scipy.linalg import eigh

def compositions(n):
    for cuts in product((0, 1), repeat=n-1):
        out=[]; p=1
        for cut in cuts:
            if cut:out.append(p);p=1
            else:p+=1
        out.append(p)
        if len(out)>=2:yield out

def graph(sizes):
    n=1+sum(sizes); a=np.zeros((n,n)); start=1
    for p in sizes:
        for x in range(start,start+p):
            a[0,x]=a[x,0]=1
            for y in range(start,start+p):
                if x!=y:a[x,y]=1
        start+=p
    L=np.diag(a.sum(axis=1))-a
    return L

def formula(sizes, t, psi):
    n=1+sum(sizes); m=n-1
    a=float(psi(1)); c=float(psi(n));
    A=math.exp(-a*t); C=math.exp(-c*t)
    D=(m+C-n*A)/(n*m); E=(1-C)/n
    M=np.zeros((n,n)); M[0,1:]=E;M[1:,0]=E
    start=1
    for p in sizes:
        W=D+(A-math.exp(-float(psi(p+1))*t))/p
        for x in range(start,start+p):
            for y in range(1,n):
                if x!=y:M[x,y]= W if start<=y<start+p else D
        start+=p
    for i in range(n):M[i,i]=1-sum(M[i,j] for j in range(n) if j!=i)
    return M,D

def matmul(A,B):
    n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def exact_projectors(sizes):
    n=1+sum(sizes);m=n-1
    P0=[[F(1,n) for j in range(n)] for i in range(n)]
    PN=[[F(0) for j in range(n)] for i in range(n)]
    PN[0][0]=F(m,n)
    for i in range(1,n):
        PN[0][i]=PN[i][0]=-F(1,n)
        for j in range(1,n):PN[i][j]=F(1,n*m)
    P1=[[F(0) for j in range(n)] for i in range(n)]
    Pblocks=[]
    start=1
    for p in sizes:
        Pi=[[F(0) for j in range(n)] for i in range(n)]
        for x in range(start,start+p):
            for y in range(start,start+p):
                Pi[x][y]=F(int(x==y))-F(1,p)
        Pblocks.append((p+1,Pi))
        for x in range(start,start+p):
            for y in range(1,n):
                P1[x][y]+=F(1,p) if start<=y<start+p else F(0)
        start+=p
    for x in range(1,n):
        for y in range(1,n):P1[x][y]-=F(1,m)
    Ps=[(0,P0),(n,PN),(1,P1)]+Pblocks
    I=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n): assert sum(P[i][j] for _,P in Ps)==I[i][j]
    for u,(lam,P) in enumerate(Ps):
        PP=matmul(P,P);assert PP==P
        for lam2,Q in Ps[u+1:]:assert all(v==0 for row in matmul(P,Q) for v in row)
    return len(Ps)

def main():
    exact=0; tests=0; signs=0; ranks=0; extrema=0
    for sizes in compositions(8):
        exact+=exact_projectors(sizes)
    for k in range(3,11):
        for sizes in compositions(k-1):
            n=k
            L=graph(sizes)
            lam,U=eigh(L)
            for psi in (lambda x:x**0.6, lambda x:x, lambda x:x**1.07,lambda x:x*x,lambda x:x**3,
                        lambda x:math.log1p(x),lambda x: 1+0.2*(x-1) if x>=1 else x):
                a=psi(1); c=psi(n)
                tstar=math.log(c/(n*a))/(c-a) if c>n*a else None
                for t in (0.0003,0.008,0.1,0.45,2.0):
                    G=U@np.diag(np.exp(-t*np.array([psi(0.0 if abs(v)<1e-9 else max(0,v)) for v in lam])))@U.T
                    E,D=formula(sizes,t,psi)
                    assert np.max(np.abs(G-E))<2e-12,(sizes,t, np.max(abs(G-E)))
                    norm=max(abs(G).sum(axis=1));bound=1+2*(n-2)*max(-D,0)
                    assert norm <= bound+2e-11
                    if 1 in sizes:assert abs(norm-bound)<2e-11
                    if min(sizes)>1 and D<-1e-9:assert norm<bound-1e-10
                    tests+=1
                if c>n*a:
                    assert tstar is not None
                    _,D=formula(sizes,tstar,psi)
                    assert D<0
                    lo=tstar;hi=1.1*math.log(n/(n-1))/a
                    assert formula(sizes,hi,psi)[1]>0
                    for z in range(80):
                        mid=(lo+hi)/2
                        if formula(sizes,mid,psi)[1]<0:lo=mid
                        else:hi=mid
                    T=(lo+hi)/2
                    assert formula(sizes,T*0.4,psi)[1]<0
                    assert formula(sizes,T*1.1,psi)[1]>0
                    signs+=1
                    maxenv=1+2*(n-2)*(-D)
                    for t in (tstar*.8, tstar, tstar*1.2, T*1.1):
                        G,dd=formula(sizes,t,psi)
                        assert max(abs(G).sum(axis=1)) <=maxenv+1e-9
                    extrema+=1
                else:
                    assert formula(sizes,.0001,psi)[1]>0
                    signs+=1
    print('VERIFY_OK exact_projector_checks=',exact,'matrix_and_norm_tests=',tests,'sign_phase_tests=',signs,'peak_bound_tests=',extrema)

if __name__=='__main__':main()
