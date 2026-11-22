"""Finite independent checks of Gaussian normal-cone claims for clique graph polytopes."""
from itertools import combinations
from math import comb, atan, sqrt, pi
import numpy as np
from scipy.optimize import linprog


def listed_vertices(n):
    vs=[(0,)*n]
    for i in range(n):
        a=[0.]*n; a[i]=1.; vs.append(tuple(a))
    for k in range(3,n+1):
        for S in combinations(range(n),k):
            a=[0.]*n
            for i in S:a[i]=.5
            vs.append(tuple(a))
    return np.array(vs)


def graph_halfspaces(n):
    A=[]; b=[]
    for i in range(n):
        a=[0]*n;a[i]=-1;A.append(a);b.append(0)
        a=[0]*n;a[i]=1;A.append(a);b.append(1)
    for i,j in combinations(range(n),2):
        a=[0]*n;a[i]=a[j]=1;A.append(a);b.append(1)
    return np.array(A, dtype=float), np.array(b,dtype=float)


def classifier(g):
    pos=np.flatnonzero(g>0)
    if len(pos)==0:return np.zeros(len(g))
    i=int(np.argmax(g))
    if len(pos)>=3 and np.sum(g[pos])>2*g[i]:
        v=np.zeros(len(g));v[pos]=.5;return v
    v=np.zeros(len(g));v[i]=1.;return v


def check():
    rng=np.random.default_rng(242007)
    trials=0
    for n in range(3,9):
        V=listed_vertices(n)
        A,b=graph_halfspaces(n)
        assert len(V)==2**n-n*(n-1)//2  # origin+n singleton+sum_{k>=3} C(n,k)
        assert np.max(A@V.T-b[:,None])<1e-9
        for v in V:
            I=np.flatnonzero(np.isclose(A@v,b))
            assert np.linalg.matrix_rank(A[I])==n
        for _ in range(250):
            g=rng.normal(size=n)
            pred=classifier(g)
            res=linprog(-g, A_ub=A, b_ub=b, bounds=[(0,1)]*n, method='highs')
            assert res.success
            assert abs(res.fun + g@pred)<1e-9
            assert abs(np.max(V@g)-g@pred)<1e-9
            trials+=1
    print('VERTEX_AND_GAUSSIAN_SUPPORT_LP_PASS', trials)
    q3=1-12/pi*atan(3-2*sqrt(2))
    H=abs(rng.normal(size=(200000,3)))
    q3_mc=float(np.mean(np.sum(H,axis=1)>2*np.max(H,axis=1)))
    assert abs(q3-q3_mc)<.006,(q3,q3_mc)
    print('THREE_SUPPORT_ANGLE_PASS',round(q3,9),round(q3_mc,6))
    for n in (6,10,16):
        G=rng.normal(size=(80000,n))
        counts=np.sum(G>0,axis=1)
        maxs=np.max(G,axis=1)
        totals=np.sum(np.maximum(G,0),axis=1)
        half=(counts>=3)&(totals>2*maxs)
        singleton=~half & (counts>0)
        null=(counts==0)
        assert np.all(half|singleton|null)
        print('ANGLE_SAMPLE_COUNTS',n,float(np.mean(half)),float(np.mean(singleton)),float(np.mean(null)))
    print('CLIQUE_GRAPH_POLYTOPE_CHECK_PASS')

if __name__=='__main__':check()
