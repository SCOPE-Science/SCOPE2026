"""Exact checking of best-response absorption on two cospectral graph families."""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache

def H(k): return sum((F(1,j) for j in range(1,k+1)), F(0))
def beta(k,q): return F(factorial(k-1)*factorial(q), factorial(k+q))
def closed(m):
    n=m*m+1; q=(m-1)**2
    aa=[F((-1)**k*comb(m-1,k)*2*m,2*m-k) for k in range(m)]
    excess=sum((-aa[k]*beta(k,q) for k in range(1,m)),F(0))+sum(aa)*beta(2*m,q)
    return m*m*H(m*m), n*(H(q)+excess)

def independent_dp(m):
    n=m*m+1; q=(m-1)**2; s=m*m
    @lru_cache(None)
    def A(k,center):
        if center: return F(0)
        if k==s:return F(0)
        if k==0:
            return (F(n)+s*A(1,False))/(n) # either center selected first or leaf
        return (F(n)+(s-k)*A(k+1,False))/(s-k) # all else unchanged
    @lru_cache(None)
    def B(i,j):
        if i==q and j==m:return F(0)
        den=(q-i)+(m-j)
        return (F(n)+((q-i)*B(i+1,j) if i<q else 0) + ((m-j)*B(i,j+1) if j<m else 0))/den
    @lru_cache(None)
    def B0(i):
        den=(q-i)+2*m
        return (F(n)+((q-i)*B0(i+1) if i<q else 0)+2*m*B(i,1))/den
    return A(0,False),B0(0)

if __name__=='__main__':
    for m in range(2,9):
        a,b=closed(m); ap,bp=independent_dp(m)
        assert a==ap and b==bp,(m,a,ap,b,bp)
        print('m=',m,'N=',m*m+1,'E_star=',float(a),'E_biclique_plus_isolates=',float(b),'gap=',float(a-b),'exact_gap=',str(a-b)[:120])
    print('PASS 7 exact independent comparisons')

def graph_recurrence(m,kind):
    n=m*m+1; edges=[]
    if kind=='star':
        edges=[(0,i) for i in range(1,n)]
    else:
        for i in range(m):
            for j in range(m,2*m): edges.append((i,j))
    adj=[0]*n
    for i,j in edges:
        adj[i]|=1<<j;adj[j]|=1<<i
    @lru_cache(None)
    def solve(mask):
        targets=[i for i in range(n) if not (mask>>i)&1 and not (adj[i]&mask)]
        if not targets:return F(0)
        return (F(n)+sum((solve(mask|(1<<i)) for i in targets),F(0)))/len(targets)
    return solve(0)

if __name__=='__main__':
    for m in (2,3):
        expA,expB=closed(m)
        assert expA==graph_recurrence(m,'star')
        assert expB==graph_recurrence(m,'biclique')
        print('PASS explicit graph state recursion m',m)
