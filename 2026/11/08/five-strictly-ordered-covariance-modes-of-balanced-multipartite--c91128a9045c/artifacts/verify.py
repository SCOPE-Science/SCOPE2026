"""Exact checks of the vertex-uniform edge covariance of balanced multipartite spanning-tree polytopes.

Python 3, NumPy for independent numerical diagonalization; exact formulas use fractions.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
import math


def edges(k,n):
    return [(i*n+a,j*n+b) for i in range(k) for j in range(i+1,k) for a in range(n) for b in range(n)]


def expected_spectrum(k,n):
    assert k>=3 and n>=2
    x=Q(k*k*n-2*k+1,k*n*n*(k-1)**2)
    y=Q(2*(k*k*n-2*k+1),k*k*n*n*(k-1))
    u=Q(k*n-2,k*n*n*(k-1))
    v=2*u
    t=Q(2*(k*k*n-k*n-2*k+1),k*n*n*(k-1)**2)
    out=Counter({Q(0):1,x:k-1,u:k*(n-1),v:k*(k-2)*(n-1),t:k*(k-1)*(n-1)**2//2})
    if k>=4:out[y]+=k*(k-3)//2
    assert sum(out.values())==k*(k-1)*n*n//2
    assert 0<u<x<t<v and (k==3 or v<y)
    assert y==v+Q(2,k*k*n*n*(k-1))
    return out


def pair_covariance(k,n):
    es=edges(k,n)
    a=Q(1,(k-1)*n)
    q=Q(1,k*(k-1)*n*n)
    r=2*(a-q)
    c=[]
    for idx,(u,v) in enumerate(es):
        types={u//n:1,v//n:-1}
        row=[]
        for jdx,(w,z) in enumerate(es):
            other={w//n:1,z//n:-1}
            dot=int(u==w)-int(u==z)-int(v==w)+int(v==z)
            classdot=sum(types[t]*other.get(t,0) for t in types)
            y=a*dot-q*classdot
            row.append(r-y*y if idx==jdx else -y*y)
        c.append(row)
    return es,c


def rank_tree(edges_,size,subset):
    par=list(range(size))
    def root(i):
        while par[i]!=i:
            par[i]=par[par[i]]
            i=par[i]
        return i
    for idx in subset:
        u,v=edges_[idx]; x,y=root(u),root(v)
        if x==y:return False
        par[x]=y
    return len({root(i) for i in range(size)})==1


def brute_covariance(k,n):
    es=edges(k,n);N=k*n;E=len(es)
    sums=[0]*E; pairs=[[0]*E for _ in range(E)];count=0
    for comb in combinations(range(E),N-1):
        if not rank_tree(es,N,comb):continue
        count+=1
        for i in comb:sums[i]+=1
        for i in comb:
            for j in comb:pairs[i][j]+=1
    output=[[Q(pairs[i][j],count)-Q(sums[i]*sums[j],count*count) for j in range(E)] for i in range(E)]
    return count,output


def spectral_check(k,n):
    import numpy as np
    es,C=pair_covariance(k,n)
    got=np.linalg.eigvalsh(np.array([[float(x) for x in row] for row in C]))
    intended=[]
    for eig,mul in expected_spectrum(k,n).items():
        intended.extend([float(eig)]*mul)
    assert len(got)==len(intended)
    assert np.max(np.abs(got-np.array(sorted(intended)))) < 1e-10,(k,n,got,intended)


def main():
    checks=0
    for k,n in [(3,2),(4,2),(3,3),(5,2),(4,3)]:
        spectral_check(k,n)
        checks+=1
    for k in range(3,25):
        for n in range(2,75):
            expected_spectrum(k,n)
            checks+=1
    for k,n in [(3,2),(4,2)]:
        if k==4:continue # larger edge set enumeration not required
        count,actual=brute_covariance(k,n)
        es,formula=pair_covariance(k,n)
        assert actual==formula,(k,n,count)
        assert count==(k*n)**(k-2)*((k-1)*n)**(k*(n-1))
        checks+=len(es)**2
        print('exhaustive',k,n,'trees',count,'entries',len(es)**2)
    print('BALANCED_MULTIPARTITE_COVARIANCE_CHECKS_PASSED',checks)

if __name__=='__main__':main()
