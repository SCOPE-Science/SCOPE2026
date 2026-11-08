"""Exact rational checks for the two-star uniform-spanning-tree degree law.
Run: python VERIFY.py (Python 3.10+, standard library only).
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

checks=0

def require(condition,label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def exact_formula(d,x,y):
    x,y=F(x),F(y);q=F(1,2**d);m=d-1
    p=2*(1-q)/d;c=(1-p)/m
    aa=p-2*c
    bb=F(d-4+2*(d+2)*q,d*(d-1)*(d-2))
    beta=p-c;delta=aa-bb;h=aa+(m-1)*bb
    z=[x*y-1,x-1,y-1]
    k=[[p,m*c,-m*c],[c,p+(m-1)*c,h],[-c,h,p+(m-1)*c]]
    block=[[F(i==j)+k[i][j]*z[j] for j in range(3)] for i in range(3)]
    rest=(1+beta*z[1])*(1+beta*z[2])-delta*delta*z[1]*z[2]
    return det3(block)*rest**(d-2)

def integer_determinant(mat):
    # Fraction-free Bareiss, exact for integer matrices, zero pivots allowed by row swaps.
    a=[r[:] for r in mat];n=len(a);old=1;sign=1
    if not n:return 1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%old==0
                a[i][j]=num//old
            a[i][k]=0
        old=pivot
    return sign*a[n-1][n-1]

def tree_weight_partition(d,x,y):
    n=2**d;lap=[[0]*n for _ in range(n)]
    for v in range(n):
        for i in range(d):
            w=v^(1<<i)
            if v>=w:continue
            wt=(x if v==0 or w==0 else 1)*(y if v==1 or w==1 else 1)
            lap[v][v]+=wt;lap[w][w]+=wt;lap[v][w]-=wt;lap[w][v]-=wt
    return integer_determinant([r[1:] for r in lap[1:]])

for d in (3,4,5):
    baseline=tree_weight_partition(d,1,1)
    require(baseline>0,('connected',d))
    for x,y in ((0,0),(0,1),(1,0),(1,1),(2,2),(2,3),(3,2),(3,5),(5,3),(1,4),(4,1)):
        require(F(tree_weight_partition(d,x,y),baseline)==exact_formula(d,x,y),('matrix_tree',d,x,y))

# Independently enumerate all spanning trees of Q_3, not just edge weights.
d=3;n=1<<d
edges=[(v,v^(1<<i)) for v in range(n) for i in range(d) if v < (v^(1<<i))]
counts=Counter();total=0
for subset in combinations(edges,n-1):
    par=list(range(n))
    def root(v):
        while v!=par[v]:v=par[v]
        return v
    good=True
    for u,v in subset:
        a,b=root(u),root(v)
        if a==b:good=False;break
        par[a]=b
    if good:
        total+=1
        du=sum(u==0 or v==0 for u,v in subset)
        dv=sum(u==1 or v==1 for u,v in subset)
        counts[(du,dv)]+=1
require(total==384,('Q3_trees',total))
for x,y in ((0,0),(0,1),(1,0),(1,1),(2,2),(2,3),(3,2),(3,5),(5,3)):
    direct=sum(F(c,total)*x**a*y**b for (a,b),c in counts.items())
    require(direct==exact_formula(d,x,y),('Q3_exhaustive',x,y))

# Direct Walsh sums independently verify every entry type, across more dimensions.
for d in range(3,11):
    N=2**d; q=F(1,N); p=2*(1-q)/d;c=(1-p)/(d-1)
    aa=p-2*c;bb=F(d-4+2*(d+2)*q,d*(d-1)*(d-2))
    def kernel(i,a,j,b):
        return F(2,N)*sum((F(-1 if ((s&a).bit_count()+(s&b).bit_count())%2 else 1,s.bit_count()) for s in range(1,N) if (s&(1<<i)) and (s&(1<<j))),F(0))
    require(kernel(0,0,0,0)==p,('self',d))
    require(kernel(0,0,1,0)==c,('same_star',d))
    require(kernel(0,0,1,1)==-c,('shared_cross',d))
    require(kernel(1,0,1,1)==aa,('aligned_cross',d))
    require(kernel(1,0,2,1)==bb,('unaligned_cross',d))
print('VERIFY_OK',checks,'assertions; Q3 trees',total)
