#!/usr/bin/env python3
"""Independent exact-rational checks for cograph stable-set moment statements.

Delaunay simplex integration uses indicator vertices and integer determinants;
no cotree volume/moment recurrence is used in its integration path.
"""
import itertools, random, math
from fractions import Fraction as F
import numpy as np
from scipy.spatial import Delaunay


def components(A, complement=False):
    n=len(A); unseen=set(range(n)); result=[]
    while unseen:
        seed=min(unseen); unseen.remove(seed); comp={seed}; stack=[seed]
        while stack:
            u=stack.pop()
            near=[v for v in sorted(unseen) if ((not bool(A[u][v])) if complement else bool(A[u][v]))]
            comp.update(near); unseen.difference_update(near); stack.extend(near)
        result.append(sorted(comp))
    return result

def moments(A):
    n=len(A)
    if n==1:return F(1),[F(1,2)],[[F(1,3)]]
    comps=components(A);op='union'
    if len(comps)==1:
        comps=components(A,True); op='join'
    assert len(comps)>1
    C=[moments([[A[i][j] for j in q] for i in q]) for q in comps]
    nsize=[len(q) for q in comps];mu=[F(0)]*n; sec=[[F(0)]*n for _ in range(n)]
    if op=='union':
        vol=F(1)
        for (q,(v,m,s)) in zip(comps,C):
            vol*=v
            for a,i in enumerate(q):
                mu[i]=m[a]
                for b,j in enumerate(q):sec[i][j]=s[a][b]
        for i in range(n):
            for j in range(n):
                if sec[i][j]==0:sec[i][j]=mu[i]*mu[j]
    else:
        vol=F(math.prod(math.factorial(len(q)) for q in comps),math.factorial(n))
        for (q,(v,m,s)) in zip(comps,C):
            vol*=v
            t=len(q)
            for a,i in enumerate(q):
                mu[i]=m[a]*F(t+1,n+1)
                for b,j in enumerate(q):sec[i][j]=s[a][b]*F((t+1)*(t+2),(n+1)*(n+2))
        for i in range(n):
            for j in range(n):
                if sec[i][j]==0:sec[i][j]=mu[i]*mu[j]*F(n+1,n+2)
    return vol,mu,sec

def det_integer(a):
    n=len(a); a=[list(map(int,row)) for row in a]; sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            idx=next((i for i in range(k+1,n) if a[i][k]),None)
            if idx is None:return 0
            a[k],a[idx]=a[idx],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=a[i][j]*p-a[i][k]*a[k][j]
                assert x%prev==0
                a[i][j]=x//prev
            a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def full_moment(A, alpha):
    n=len(A)
    if n==1:return F(1,alpha[0]+1)
    parts=components(A);join=False
    if len(parts)==1:
        parts=components(A,True);join=True
    assert len(parts)>1
    val=F(1);total=sum(alpha)
    if join:
        val=F(1,math.prod(n+1+j for j in range(total)))
    for q in parts:
        sub=[alpha[i] for i in q]
        val*=full_moment([[A[i][j] for j in q] for i in q],sub)
        if join:
            for j in range(sum(sub)):
                val*=len(q)+1+j
    return val

def cubic_geometry_moment(A,alpha):
    n=len(A);V=[]
    for v in itertools.product((0,1),repeat=n):
        if all(not (v[i] and v[j] and A[i][j]) for i in range(n) for j in range(i)):
            V.append(v)
    triangles=([list(range(n+1))] if len(V)==n+1 else
        Delaunay(np.asarray(V,dtype=float),qhull_options='QJ Qbb Qc Q12').simplices)
    factors=[i for i,e in enumerate(alpha) for _ in range(e)]
    assert len(factors)==3
    num=den=0
    for simp in triangles:
        verts=[V[int(t)] for t in simp]
        wt=abs(det_integer([[verts[k][i]-verts[0][i] for k in range(1,n+1)] for i in range(n)]))
        if not wt:continue
        den+=wt
        accum=0
        for ix in itertools.product(range(n+1),repeat=3):
            if not all(verts[ix[j]][factors[j]] for j in range(3)):continue
            counts=[ix.count(k) for k in range(n+1)]
            accum+=math.prod(math.factorial(c) for c in counts)
        num+=wt*accum
    return F(num,den*(n+1)*(n+2)*(n+3))

def geometry(A):
    n=len(A)
    V=[]
    for v in itertools.product((0,1),repeat=n):
        if all(not (v[i] and v[j] and A[i][j]) for i in range(n) for j in range(i)):
            V.append(v)
    if n==1:return F(1),[F(1,2)],[[F(1,3)]],1
    arr=np.asarray(V,dtype=float)
    triangles=([list(range(n+1))] if len(V)==n+1 else Delaunay(arr,qhull_options='QJ Qbb Qc Q12').simplices)
    W=0;sumM=[0]*n;sumE=[[0]*n for _ in range(n)];used=0
    for simp in triangles:
        verts=[V[int(t)] for t in simp]
        det=abs(det_integer([[verts[k][i]-verts[0][i] for k in range(1,n+1)] for i in range(n)]))
        if det==0:continue
        used+=1;W+=det
        S=[sum(v[i] for v in verts) for i in range(n)]
        for i in range(n):
            sumM[i]+=det*S[i]
            for j in range(n):
                sumE[i][j]+=det*(S[i]*S[j]+sum(v[i]*v[j] for v in verts))
    assert W>0
    vol=F(W,math.factorial(n))
    mean=[F(m,W*(n+1)) for m in sumM]
    sec=[[F(s,W*(n+1)*(n+2)) for s in row] for row in sumE]
    return vol,mean,sec,used

def adj(n,mask):
    a=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(itertools.combinations(range(n),2)):
        a[i][j]=a[j][i]=bool(mask>>k&1)
    return a

def is_cograph(a):
    n=len(a)
    for t in itertools.combinations(range(n),4):
        deg=[sum(a[i][j] for j in t) for i in t]
        if sorted(deg)==[1,1,2,2] and sum(deg)//2==3:return False
    return True

def check(A):
    n=len(A);v,m,s=moments(A);gv,gm,gs,ns=geometry(A)
    assert gv==v,(n,'volume',gv,v)
    assert gm==m,(n,'mean',gm,m)
    assert gs==s,(n,'second')
    edges=nonedges=zero=0
    for i in range(n):
        for j in range(i):
            cov=s[i][j]-m[i]*m[j]
            assert (cov<0)==A[i][j],(n,'edge sign',i,j,cov)
            if A[i][j]:
                edges+=1
                assert s[i][j]*F(n+2)<=m[i]*m[j]*(n+1)
            elif cov>0:nonedges+=1
            else:
                zero+=1
                c=components(A)
                assert not any(i in q and j in q for q in c)
    return ns,edges,nonedges,zero

def run():
    count=tri=edges=nonedges=zeros=0
    for n in range(2,6):
        for mask in range(1<<(n*(n-1)//2)):
            A=adj(n,mask)
            if not is_cograph(A):continue
            t,e,p,z=check(A)
            count+=1;tri+=t;edges+=e;nonedges+=p;zeros+=z
    rng=random.Random(24593)
    for z in range(30):
        # random cotree, moderate dimension, check against independent triangulation
        n=6; A=[[False]*n for _ in range(n)]
        groups=[[i] for i in range(n)]
        while len(groups)>1:
            ii,jj=rng.sample(range(len(groups)),2)
            b=groups.pop(max(ii,jj));a=groups.pop(min(ii,jj))
            if rng.choice((False,True)):
                for i in a:
                    for j in b:A[i][j]=A[j][i]=True
            groups.append(a+b)
        t,e,p,z=check(A)
        count+=1;tri+=t;edges+=e;nonedges+=p;zeros+=z
    cubic=0
    for n in (3,4):
        subset=0
        for mask in range(1<<(n*(n-1)//2)):
            A=adj(n,mask)
            if not is_cograph(A):continue
            for index_tuple in itertools.combinations_with_replacement(range(n),3):
                alpha=[index_tuple.count(i) for i in range(n)]
                assert cubic_geometry_moment(A,alpha)==full_moment(A,alpha),(A,alpha)
                cubic+=1
            subset+=1
    # Noncograph P4: exact counterexample derived via direct nested integration
    import sympy as sp
    x,y=sp.symbols('x y')
    integ=lambda f:sp.integrate(sp.integrate(f*(1-x)*(1-y),(y,0,1-x)),(x,0,1))
    W=integ(1); mean=integ(x)/W; pair=integ(x*y)/W
    assert W==sp.Rational(5,24) and sp.factor((pair-mean*mean)/4)==-sp.Rational(11,3750)
    print('COGRAPH_COTREE_MOMENTS_CHECKS_PASSED',count,tri,edges,nonedges,zeros,'CUBIC',cubic,'P4_NONEDGE_COV=-11/3750')
if __name__=='__main__':run()
