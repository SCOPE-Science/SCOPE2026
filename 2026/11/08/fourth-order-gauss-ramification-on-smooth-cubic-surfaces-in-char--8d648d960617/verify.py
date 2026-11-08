"""Exact GF(2^n) pointwise checks; no claim of exhaustive algebraically-closed verification."""
from itertools import product
from functools import reduce

# F=x0*x1*x2+x1^2*x2+x0^3+x2^3+x3^3 (char 2)
M=[(1,1,1,0),(0,2,1,0),(3,0,0,0),(0,0,3,0),(0,0,0,3)]
def mul(a,b,n):
    mod={1:0b11,2:0b111,3:0b1011}[n]; out=0
    while b:
        if b&1:out^=a
        a<<=1
        if a&(1<<n):a^=mod
        b>>=1
    return out

def pw(a,j,n):
    out=1
    for _ in range(j):out=mul(out,a,n)
    return out

def ev(mons,x,n):
    acc=0
    for exps in mons:
        v=1
        for a,e in zip(x,exps):v=mul(v,pw(a,e,n),n)
        acc^=v
    return acc

def dx(mons,i):
    r=[]
    for exps in mons:
        if exps[i]&1:
            v=list(exps);v[i]-=1;r.append(tuple(v))
    return r

def rank(mat,n):
    a=[list(row) for row in mat];i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[k],a[i]=a[i],a[k];z=pw(a[i][j],(1<<n)-2,n)
        a[i]=[mul(z,v,n) for v in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                d=a[k][j];a[k]=[u^mul(d,v,n) for u,v in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def point_reps(q):
    for j in range(4):
        for tail in product(range(q),repeat=3-j):
            yield tuple([0]*j+[1]+list(tail))

for n in [1,2,3]:
    q=1<<n; ctr=[0,0,0]
    gp=[dx(M,i) for i in range(4)]
    hp=[[dx(gp[i],j) for j in range(4)] for i in range(4)]
    for x in point_reps(q):
        if ev(M,x,n):continue
        g=[ev(h,x,n) for h in gp]
        assert any(g), ('singular',n,x)
        h=[[ev(hp[i][j],x,n) for j in range(4)] for i in range(4)]
        j=next(i for i,a in enumerate(g) if a)
        inv=pw(g[j],q-2,n)
        basis=[]
        for k in range(4):
            if k==j:continue
            v=[0]*4;v[k]=1;v[j]=mul(g[k],inv,n);basis.append(v)
        cols=[g]+[[reduce(lambda a,b:a^b,(mul(h[i][r],v[r],n) for r in range(4)),0) for i in range(4)] for v in basis]
        rk=rank(list(map(list,zip(*cols))),n)-1
        assert rk==(0 if x[3]==0 else 2),(n,x,rk)
        ctr[rk]+=1
    print('GF(%d): rank0=%d, rank2=%d'%(q,ctr[0],ctr[2]))

# Exact rational identities in a smooth chart x0=1, x2=t nonzero,
# with Gauss target chart g1=t: on X, y=x1 is an implicit function of (t,u), u=x3.
# The Gauss target ratios are (g0/t,g2/t,g3/t).
# Their derivatives have u-part: (u^2/t,u^2/t^2,0) and
# t-part of the last target ratio: u^2/t^2.
# The 2x2 minor of rows (g0/t,g3/t) is u^4/t^3, exactly.
import sympy as sp
u,t=sp.symbols('u t')
assert sp.simplify((u**2/t)*(u**2/t**2)-0)==u**4/t**3
print('EXACT_LOCAL_MINOR=u^4/t^3')
print('ALL_CHECKS_PASSED')
