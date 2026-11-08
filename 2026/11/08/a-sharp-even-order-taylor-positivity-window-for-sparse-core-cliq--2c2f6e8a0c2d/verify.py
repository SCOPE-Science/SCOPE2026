"""Exact rational checks for even Taylor heat maps on clique joins.

The infinite statement follows from the algebraic proof, not this finite test.
Python 3 standard library only.
"""
from fractions import Fraction as Q
from math import factorial
from random import Random

BRACKETS = {2:(1999,2001),4:(2785,2786),6:(3553,3554),8:(4313,4314),10:(5069,5070)}

def f(p,x):
    return sum(((-x)**j / factorial(j) for j in range(p+1)),Q(0))

def mm(A,B):
    n=len(A); q=len(B); r=len(B[0])
    return [[sum((A[i][a]*B[a][j] for a in range(q)),Q(0)) for j in range(r)] for i in range(n)]

def identity(n):
    return [[Q(i==j) for j in range(n)] for i in range(n)]

def poly(L,p,h):
    n=len(L); V=identity(n); S=[[Q(0) for j in range(n)] for i in range(n)]
    for a in range(p+1):
        c=(-h)**a/factorial(a)
        for i in range(n):
            for j in range(n):S[i][j]+=c*V[i][j]
        if a<p:V=mm(V,L)
    return S

def lap(n,E):
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for a,b in E:
        L[a][a]+=1; L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    return L

def joined_lap(k,m,E):
    E2=[(a+k,b+k) for a,b in E]
    E2 += [(a,b) for a in range(k) for b in range(a+1,k)]
    E2 += [(a,k+b) for a in range(k) for b in range(m)]
    return lap(k+m,E2)

def base_graph(m,kind,seed,degree):
    if kind=='path':return [(i,i+1) for i in range(m-1)]
    if kind=='cycle':return [(i,(i+1)%m) for i in range(m)]
    if kind=='empty':return []
    R=Random(seed); edges=[(i,j) for i in range(m) for j in range(i+1,m)]
    R.shuffle(edges); E=[]; d=[0]*m
    for i,j in edges:
        if d[i]<degree and d[j]<degree and R.randrange(3)==0:
            E.append((i,j));d[i]+=1;d[j]+=1
    return E

def check(p,k,m,E,lo,hi):
    n=k+m; deg=[0]*m
    for i,j in E:deg[i]+=1;deg[j]+=1
    D=max(deg)
    assert hi*(k+D)<=n,(p,k,m,D)
    L=joined_lap(k,m,E); LH=lap(m,E)
    for t,inside in [(Q(0),True),(Q(1),True),(lo,True),(hi,False)]:
        h=t/n; M=poly(L,p,h); z=f(p,t)
        c=(1-z)/n
        q=(m+k*z-n*f(p,k*h))/(m*n)
        BL=[[LH[i][j]+Q(k*(i==j)) for j in range(m)] for i in range(m)]
        base=poly(BL,p,h)
        for i in range(n):assert sum(M[i])==1,(p,k,m,'row')
        for i in range(k):
            for j in range(k):assert M[i][j]==Q(i==j)*z+c,(p,k,m,'apex')
            for j in range(k,n):assert M[i][j]==M[j][i]==c,(p,k,m,'cross')
        for i in range(m):
            for j in range(m):assert M[k+i][k+j]==base[i][j]+q,(p,k,m,'base')
        if inside:assert min(min(row) for row in M)>=0,(p,k,m,'inside')
        else:assert M[0][k]<0,(p,k,m,'outside')
    return 4*n*n

def main():
    graphs=0;entry_tests=0
    configs=[(1,7,1),(1,8,2),(1,10,2),(1,12,2),(1,16,2),
             (2,10,2),(2,13,2),(2,16,2),(2,19,2),
             (3,11,2),(3,15,2),(4,19,3)]
    for p,(a,b) in BRACKETS.items():
        lo,hi=Q(a,1000),Q(b,1000)
        assert f(p,lo)<1<f(p,hi),(p,lo,hi)
        for k,m,D in configs:
            if hi*(k+D)>k+m:continue
            for kind in ['path','cycle','empty','random']:
                if kind in ('path','cycle') and D<2:continue
                for seed in range(3 if kind=='random' else 1):
                    E=base_graph(m,kind,seed+21*m+2*p,D)
                    entry_tests+=check(p,k,m,E,lo,hi);graphs+=1
    print('VERIFIED',graphs,'graph/order cases and',entry_tests,'exact entry comparisons')
    print('All beta brackets, block identities, row sums, and signs passed.')

if __name__=='__main__':main()
