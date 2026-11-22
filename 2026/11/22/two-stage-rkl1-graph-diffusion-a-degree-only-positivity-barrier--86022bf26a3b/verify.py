"""Exact arithmetic verification of a two-stage Legendre graph-heat update.
No external dependencies. All checks enumerate finite cases; the proof of the
all-graph theorem is analytic and is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import sqrt


def matrix(n, edges):
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i,j in edges:
        L[i][i]+=1; L[j][j]+=1
        L[i][j]-=1; L[j][i]-=1
    return L


def multiply(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0)) for j in range(n)] for i in range(n)]


def direct(L,t):
    L2=multiply(L,L);n=len(L)
    return [[Q(int(i==j)) - t*L[i][j]+t*t*L2[i][j]/6 for j in range(n)] for i in range(n)]


def local(L,t):
    n=len(L)
    d=[L[i][i] for i in range(n)]
    ans=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                ans[i][j]=1-d[i]*t+(d[i]*d[i]+d[i])*t*t/6
            else:
                common=sum(1 for k in range(n) if k!=i and k!=j and L[i][k]<0 and L[k][j]<0)
                ans[i][j]=t*(1-t*(d[i]+d[j]-common)/6) if L[i][j]<0 else t*t*common/6
    return ans


def permitted(L,t):
    n=len(L)
    d=[L[i][i] for i in range(n)]
    for i in range(n):
        if 1-d[i]*t+(d[i]*d[i]+d[i])*t*t/6<0: return False
        for j in range(i+1,n):
            if L[i][j]<0:
                common=sum(1 for k in range(n) if L[i][k]<0 and L[j][k]<0)
                if t*(d[i]+d[j]-common)>6:return False
    return True

count=0
graphs=0
steps=[Q(0),Q(1,100),Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(2),Q(3),Q(5)]
for n in range(1,6):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        edges=[e for k,e in enumerate(pairs) if mask>>k&1]
        L=matrix(n,edges);graphs+=1
        for t in steps:
            M=direct(L,t); E=local(L,t)
            assert M==E,(n,edges,t,'matrix mismatch')
            assert all(sum(row)==1 for row in M),(n,edges,t,'mass')
            assert (all(z>=0 for row in M for z in row)==permitted(L,t)),(n,edges,t,'positivity')
            count+=3
for m in range(1,101):
    tmax=Q(6,m+1)
    for t in (Q(0),Q(3,m+1),tmax,Q(1,m+1),Q(5,m+1)):
        # Exact star entry orbits: hub diagonal, leaf diagonal,
        # hub-to-leaf, and leaf-to-leaf. No large dense matrices.
        hub=1-m*t+Q(m*(m+1),6)*t*t
        leaf=1-t+t*t/Q(3)
        spoke=t*(1-Q(m+1,6)*t)
        other=t*t/Q(6)
        assert hub + m*spoke==1
        assert leaf + spoke + (m-1)*other==1
        expected=(m<=2 or t<=Q(3,m+1)*(1-sqrt((m-2)/(3*m))) or t>=Q(3,m+1)*(1+sqrt((m-2)/(3*m)))) if m>=3 else True
        # Avoid near-root floating conclusions; all chosen rational trial points stay away from roots.
        assert (all(z>=0 for z in (hub,leaf,spoke,other))==expected),(m,t,'star')
        count+=2
assert direct(matrix(4,[(0,1),(0,2),(0,3)]),Q(3,4))[0][0]==Q(-1,8)
count+=1
print('PASS',graphs,'labelled simple graphs with n<=5,',count,'exact checks; 100 star sizes and exact witness -1/8')
