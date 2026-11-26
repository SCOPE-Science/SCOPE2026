"""Independent exact determinant check of all 1128 line-pair incidence conditions.
The coefficient ring is Z[zeta_8] = Z[t]/(t^4+1); no external libraries.
"""
from itertools import product, permutations

ONE=(1,0,0,0)
ZERO=(0,0,0,0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def mul(a,b):
    c=[0]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            k=i+j;c[k%4]+= (-1 if k>=4 else 1)*x*y
    return tuple(c)
def zpow(k):
    k%=8
    c=[0]*4;c[k%4]=1 if k<4 else -1
    return tuple(c)

def row(i,j,k):
    r=[ZERO for _ in range(4)]
    r[i]=ONE;r[j]=neg(zpow(k))
    return r

def define_line(t,m,n):
    x=2*m+int(t==1);y=2*n+int(t==1)
    if t==0:return [row(0,1,x),row(2,3,y)]
    if t==1:return [row(0,2,x),row(1,3,y)]
    return [row(0,3,x),row(1,2,y)]

def det4(M):
    s=ZERO
    for p in permutations(range(4)):
        v=ONE
        for i,j in enumerate(p):v=mul(v,M[i][j])
        inversion=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        s=add(s,neg(v) if inversion%2 else v)
    return s

def criterion(a,b):
    t,m,n=a;u,p,q=b
    if t==u:return (m==p or n==q)
    if t>u:a,b=b,a;t,u=u,t
    _,m,n=a;_,p,q=b
    x=2*m+int(t==1);y=2*n+int(t==1)
    v=2*p+int(u==1);w=2*q+int(u==1)
    if (t,u)==(0,1):return (x+w-y-v)%8==0
    if (t,u)==(0,2):return (x+w+y-v)%8==0
    assert (t,u)==(1,2)
    return (x+y-v-w)%8==0

labels=[(t,m,n) for t in range(3) for m,n in product(range(4),repeat=2)]
planes=[define_line(*label) for label in labels]
for i in range(48):
    for j in range(i+1,48):
        check=det4(planes[i]+planes[j])==ZERO
        assert check==criterion(labels[i],labels[j]),(i,j,check)
print('PASS: all 1128 exact determinant tests agree with combinatorial incidence')
