#!/usr/bin/env python3
"""Independent dense-matrix verifier of characteristic-two incidence-wave clocks."""
from itertools import combinations

def matmul(X,Y):
    n=len(X);m=len(Y[0]);k=len(Y)
    out=[[0]*m for _ in range(n)]
    for i in range(n):
        for a in range(k):
            if X[i][a]:
                for j in range(m):out[i][j]^=Y[a][j]
    return out

def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def rank(M):
    a=[x[:] for x in M]
    r=0
    for c in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        for j in range(len(a)):
            if j!=r and a[j][c]:a[j]=[x^y for x,y in zip(a[j],a[r])]
        r+=1
    return r

def power(X,k):
    P=eye(len(X))
    while k:
        if k&1:P=matmul(P,X)
        X=matmul(X,X);k>>=1
    return P

def wave(edges,np,nl):
    n=np+nl
    A=[[0]*n for _ in range(n)]
    for p,l in edges:
        A[p][np+l]=A[np+l][p]=1
    T=[[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        T[i][:n]=A[i][:]
        T[i][n+i]=1
        T[n+i][i]=1
    return A,T

def duads_synthemes():
    pts=list(combinations(range(6),2)); lines=set()
    for trio in combinations(range(len(pts)),3):
        if len(set().union(*(set(pts[i]) for i in trio)))==6:lines.add(trio)
    lines=sorted(lines)
    assert len(pts)==len(lines)==15
    return [(i,j) for j,L in enumerate(lines) for i in L],15,15

def grid(s):
    a=s+1;np=a*a;nl=2*a
    pairs=[]
    for i in range(a):
        for j in range(a):
            p=i*a+j
            pairs.extend([(p,i),(p,a+j)])
    return pairs,np,nl

def inspect(label,config,period):
    A,T=wave(*config);n=len(A)
    assert power(T,period)==eye(2*n)
    for t in range(1,period):
        if period%t==0:assert power(T,t)!=eye(2*n)
    E=power(A,4)
    assert matmul(E,E)==E
    Z=[[int(i==j)^E[i][j] for j in range(n)] for i in range(n)]
    def rkprod(X,Y):return rank(matmul(X,Y))
    e=rank(E)
    U=[[A[i][j]^int(i==j) for j in range(n)] for i in range(n)]
    c2=rkprod(U,E);c1=e-2*c2
    d=[rank(Z)]
    Ak=eye(n)
    for k in range(1,5):
        Ak=matmul(A,Ak)
        d.append(rkprod(Ak,Z))
    b4=d[3];b3=d[2]-2*d[3];b2=d[1]-2*d[2]+d[3];b1=d[0]-2*d[1]+d[2]
    assert d[4]==0 and min(b1,b2,b3,b4,c1,c2)>=0
    for k in [1,2,3,4,6,8,12,16,24]:
        twopower=k&-k
        pred=sum(b*min(2*j,twopower) for j,b in enumerate([0,b1,b2,b3,b4]) if j)
        if k%3==0:pred+=2*c1+2*c2*min(2,twopower)
        Tk=power(T,k)
        diff=[[Tk[i][j]^int(i==j) for j in range(2*n)] for i in range(2*n)]
        actual=2*n-rank(diff)
        assert pred==actual,(label,k,actual,pred)
    print(label, 'vertices',n,'period',period,'E-rank',e,'1-blocks',(c1,c2),'0-blocks',(b1,b2,b3,b4))

if __name__=='__main__':
    inspect('GQ(2,2): duads/synthemes',duads_synthemes(),24)
    inspect('GQ(2,1): rectangular grid',grid(2),24)
    inspect('GQ(3,1): rectangular grid',grid(3),8)
