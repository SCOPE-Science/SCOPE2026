from fractions import Fraction as F
from itertools import combinations

def inv_solve(A,b):
    n=len(b); a=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
        z=a[k][k];a[k]=[u/z for u in a[k]]
        for i in range(n):
            if i!=k and a[i][k]:
                z=a[i][k];a[i]=[a[i][j]-z*a[k][j] for j in range(n+1)]
    return [row[-1] for row in a]

def lap(n,edges):
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,l in edges:
        c=1/l;A[u][u]+=c;A[v][v]+=c;A[u][v]-=c;A[v][u]-=c
    return A

def pin_solve(n,es,src):
    A=lap(n,es);assert sum(src)==0
    sol=inv_solve([r[1:] for r in A[1:]],src[1:]);return [F(0)]+sol

def make(n,es):
    T=sum((l for _,_,l in es),F(0));R={}
    for u,v in combinations(range(n),2):
        b=[F(0)]*n;b[u]=1;b[v]=-1;z=pin_solve(n,es,b)
        R[u,v]=R[v,u]=z[u]-z[v]
    for i in range(n):R[i,i]=F(0)
    Fv=[]
    for x in range(n):
        Fv.append(sum((l*(R[x,u]+R[x,v])/2+l*(l-R[u,v])/6 for u,v,l in es),F(0)))
    J=sum((l*((Fv[u]+Fv[v])/2+(T*(l-R[u,v])-l*l)/6) for u,v,l in es),F(0))
    Qv=[fv/T-J/(2*T*T) for fv in Fv]
    C=[l-R[u,v]-l*l/T for u,v,l in es]
    opt=max(Qv)
    for (u,v,l),c in zip(es,C):
        if c>0:
            t=F(1,2)+(Qv[v]-Qv[u])/(2*c)
            if 0<t<1:opt=max(opt,Qv[u]*(1-t)+Qv[v]*t+c*t*(1-t))
    assert sum((c/l for c,(_,_,l) in zip(C,es)),F(0))==len(es)-n
    return T,R,Fv,J,Qv,C,opt

def independent_q(n,es,eidx,t):
    T=sum((e[2] for e in es),F(0));u,v,l=es[eidx]
    if t==0: pt=u;newes=es;nn=n
    elif t==1:pt=v;newes=es;nn=n
    else:
        pt=n;nn=n+1;newes=es[:eidx]+[(u,pt,l*t),(pt,v,l*(1-t))]+es[eidx+1:]
    bb=[F(0) for _ in range(nn)];bb[pt]+=1
    for a,b,s in newes:bb[a]-=s/(2*T);bb[b]-=s/(2*T)
    z=pin_solve(nn,newes,bb)
    mean=(sum((s*(z[a]+z[b])/2 - s**3/(12*T) for a,b,s in newes),F(0)))/T
    return z[pt]-mean

cases=[
 (2,[(0,1,F(3,2))]),
 (3,[(0,1,F(2)),(1,2,F(3)),(0,2,F(4))]),
 (4,[(0,1,F(1)),(1,2,F(2)),(2,3,F(3)),(3,0,F(4)),(0,2,F(5,2))]),
 (4,[(0,1,F(1)),(0,2,F(2)),(0,3,F(3))]),
 (4,[(0,1,F(1)),(1,2,F(3,2)),(2,3,F(2)),(3,0,F(1)),(0,2,F(4)),(1,3,F(5,2))]),
 (6,[(i,j,F(1+(i+j)%4,2)) for i in range(3) for j in range(3,6)]),
 (5,[(0,1,F(1)),(1,2,F(2)),(2,0,F(3)),(2,3,F(5)),(3,4,F(1)),(4,2,F(2))]),
 (6,[(0,1,F(1)),(1,2,F(1)),(2,0,F(1)),(3,4,F(1)),(4,5,F(1)),(5,3,F(1)),(0,3,F(2))]),
 (5,[(0,1,F(1)),(1,2,F(1)),(2,3,F(1)),(3,4,F(1))]),
 (4,[(0,1,F(1)),(0,1,F(2)),(1,2,F(3)),(2,3,F(1)),(3,0,F(4))]),
]
count=0
for n,edges in cases:
    T,R,Fv,J,Qv,C,K=make(n,edges)
    for i,(u,v,l) in enumerate(edges):
        for t in (F(0),F(1,7),F(1,3),F(1,2),F(4,5),F(1)):
            q=independent_q(n,edges,i,t)
            a=(1-t)*Qv[u]+t*Qv[v]+C[i]*t*(1-t)
            assert q==a,(n,i,t,q,a)
            assert K>=q
            count+=1
print('EXACT_INDEPENDENT_CONTINUUM_EDGE_EVALUATIONS_PASSED',count)
print('FOSTER_TOPOLOGICAL_CURVATURE_IDENTITIES_PASSED',len(cases))
print('ALL_UNIVERSAL_GRAPH_ENVELOPE_CHECKS_PASSED')
