"""Exact finite checks for an odd-cycle graph with pendant edges.
Run: python3 verify_matching_cap.py (Python standard library only).
"""
from itertools import product
from math import comb

def edges(n, attached):
    # Vertex 0,...,n-1 on cyclic rim; leaf vertices n+j.
    return [(i,(i+1)%n) for i in range(n)] + [(v,n+j) for j,v in enumerate(attached)]

def brute(n,attached,k):
    E=edges(n,attached)
    count=0; bad=0
    for z in product(range(k+1),repeat=len(E)):
        d=[0]*(n+len(attached))
        for j,(u,v) in enumerate(E):d[u]+=z[j];d[v]+=z[j]
        if max(d)>k:continue
        count+=1
        if 2*sum(z[:n])>(n-1)*k:bad+=1
    return bad

def predicted(N,k):
    return sum(comb(N+j-1,N-1) for j in range(k) if (k-j)%2==0)

def test():
    cases=[(3,[]),(3,[0]),(3,[0,0]),(3,[0,1]),(3,[0,1,2]),(5,[]),(5,[0]),(5,[0,2]),(5,[0,0]),(7,[])]
    total=0
    for n,a in cases:
        N=n+len(a)
        for k in range(0,5 if N<=6 else 4):
            observed=brute(n,a,k)
            expected=predicted(N,k)
            assert observed==expected,(n,a,k,observed,expected)
            total+=1
    # Confirm fractional cap map in exact halves for every simplex vertex:
    from fractions import Fraction as F
    for n,a in cases:
        N=n+len(a)
        for which in range(N+1):
            slack=[0]*n; leaves=[0]*len(a)
            if which<n:slack[which]=1
            elif which<N: leaves[which-n]=1
            u=[slack[i]+sum(leaves[j] for j,v in enumerate(a) if v==i) for i in range(n)]
            # cycle a_{i-1}+a_i=1-u_i solve via alternating linear system
            cyc=[]
            # a_{n-1}=alpha; a_0=(1-u_0)-alpha, etc
            # a_{n-1}=[(1-u_0)-(1-u_1)+...+(1-u_{n-1})]/2
            alpha=F(sum(((-1)**i)*(1-u[i]) for i in range(n)),2)
            cyc=[None]*n; cyc[-1]=alpha
            for i in range(n-1):cyc[i]=F(1-u[i])-cyc[i-1]
            assert cyc[-2]+cyc[-1]==1-u[-1]
            if which==N:
                assert all(x==F(1,2) for x in cyc) and all(y==0 for y in leaves)
            else:
                assert all(x in [0,1] for x in cyc) and sum(cyc)+sum(leaves)==(n-1)//2+(which>=n)
    print('ODD_UNICYCLE_MATCHING_CAP_PASS',total,'integer_dilations_cases; all simplex vertices exact')
if __name__=='__main__':test()
