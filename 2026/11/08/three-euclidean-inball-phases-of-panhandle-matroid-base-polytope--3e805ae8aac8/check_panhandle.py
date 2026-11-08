"""Reproducible finite checks for the intrinsic Euclidean insphere of panhandle base polytopes.

Run: python check_panhandle.py (requires numpy and scipy).
"""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def theorem(rank,s,t):
    n=s+t
    delta=sqrt(s*t/(n-1))
    u=min(rank/n,1/(t+delta),(s+1-rank)/(s+delta))
    return u, sqrt(n/(n-1))*u


def solve_full_lp(rank,s,t):
    n=s+t
    q=sqrt((n-1)/n)
    beta=sqrt(s*t/n)
    rows=[]; rhs=[]
    for i in range(n):
        a=np.zeros(n+1); a[i]=-1; a[-1]=q
        rows.append(a); rhs.append(0)
    for i in range(s):
        a=np.zeros(n+1); a[i]=1; a[-1]=q
        rows.append(a); rhs.append(1)
    a=np.zeros(n+1); a[s:n]=1; a[-1]=beta
    rows.append(a);rhs.append(1)
    eq=np.zeros((1,n+1)); eq[0,:n]=1
    c=np.zeros(n+1); c[-1]=-1
    sol=linprog(c,A_ub=rows,b_ub=rhs,A_eq=eq,b_eq=[rank],bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert sol.success, (rank,s,t,sol.message)
    return sol, np.asarray(rows), np.asarray(rhs)


def verify_vertices(rank,s,t):
    n=s+t
    B=[z for z in combinations(range(n),rank) if sum(v>=s for v in z)<=1]
    V=np.zeros((len(B),n))
    for i,b in enumerate(B): V[i,list(b)]=1
    assert np.linalg.matrix_rank(V[1:]-V[0],tol=1e-9)==n-1
    # Check genuine facets, not merely valid inequalities.  Affine codimension is 1
    # inside the rank hyperplane, so the face-vertex difference rank must be n-2.
    facets=[]
    for i in range(n):
        facets.append(V[V[:,i]==0])
    for i in range(s):
        facets.append(V[V[:,i]==1])
    facets.append(V[V[:,s:].sum(axis=1)==1])
    for face in facets:
        assert len(face)>=n-1 and np.linalg.matrix_rank(face[1:]-face[0],tol=1e-9)==n-2, (rank,s,t)
    # compare full-lattice convex hull with the halfspace representation from the source.
    if n<=8:
        U=np.eye(n)[:n-1]-np.eye(n)[n-1:]
        W=V@U.T
        hull=ConvexHull(W)
        assert len(hull.vertices)==len(B), (rank,s,t,len(B),len(hull.vertices))
    return len(B)


def main():
    runs=0;verts=0;by_phase=[0,0,0]; tie=0
    for s in range(4,14):
        for t in range(2,11):
            for rank in range(3,s):
                n=s+t;d=sqrt(s*t/(n-1))
                bars=[rank/n,1/(t+d),(s+1-rank)/(s+d)]
                u,exact=theorem(rank,s,t)
                sol,A,b=solve_full_lp(rank,s,t)
                assert abs(sol.x[-1]-exact)<1e-8, (rank,s,t,sol.x[-1],exact)
                # Explicit symmetric center satisfying every original inequality.
                tail_low=max(u,(rank-s+s*u)/t)
                tail_high=min((1-d*u)/t,(rank-s*u)/t)
                assert tail_low <= tail_high+5e-13, (rank,s,t,u,tail_low,tail_high)
                bmean=(tail_low+tail_high)/2
                amean=(rank-t*bmean)/s
                center=np.array([amean]*s+[bmean]*t)
                q=sqrt((n-1)/n); beta=sqrt(s*t/n)
                v=np.r_[center,exact]
                assert max(A@v-b)<1e-10
                assert abs(center.sum()-rank)<1e-10
                winner=int(np.argmin(bars)); by_phase[winner]+=1
                if len([x for x in bars if abs(x-u)<1e-10])>1: tie+=1
                runs+=1
    for r,s,t in [(3,4,2),(3,9,2),(5,6,2),(3,8,2),(149,154,22)]:
        u,rad=theorem(r,s,t)
        d=sqrt(s*t/(s+t-1));B=[r/(s+t),1/(t+d),(s+1-r)/(s+d)]
        if (r,s,t)==(149,154,22):
            assert abs(B[1]-B[2])<1e-14
        if s+t<=12:verts+=verify_vertices(r,s,t)
        print('representative',r,s,t,'radius',rad,'barriers',B)
    print('PANHANDLE_INBALL_TESTS_PASSED',runs,'cases, phase counts',by_phase,'tied',tie,'small-hull vertices',verts)

if __name__=='__main__':main()
