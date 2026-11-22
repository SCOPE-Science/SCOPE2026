"""Exact integer verification of the Ceva-four resolved boundary."""
from math import prod
from collections import Counter

def graph(n=4):
    V=[('line',c,a) for c in range(3) for a in range(n)]
    V += [('pencil',c) for c in range(3)]
    V += [('base',a,b) for a in range(n) for b in range(n)]
    I={v:j for j,v in enumerate(V)}
    L=[[0]*len(V) for v in V]
    def link(v,w):
        i,j=I[v],I[w];assert i!=j
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    for c in range(3):
        for a in range(n):link(('line',c,a),('pencil',c))
    for a in range(n):
        for b in range(n):
            for c,d in enumerate((a,b,(-a-b)%n)):
                link(('base',a,b),('line',c,d))
    assert [L[i][i] for i in range(len(V))].count(n+1)==3*n
    assert [L[i][i] for i in range(len(V))].count(3)==n*n
    assert [L[i][i] for i in range(len(V))].count(n)==3
    assert sum(L[i][i] for i in range(len(V)))==2*(3*n*n+3*n)
    assert all(sum(row)==0 for row in L)
    return L

def determinant(A):
    a=[row[:] for row in A];N=len(a);sign=1;prev=1
    for k in range(N-1):
        if a[k][k]==0:
            t=next((r for r in range(k+1,N) if a[r][k]),None)
            if t is None:return 0
            a[k],a[t]=a[t],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                num=a[i][j]*p-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,N):a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def smith(A):
    a=[row[:] for row in A];N=len(a)
    for k in range(N):
        nz=next(((i,j) for i in range(k,N) for j in range(k,N) if a[i][j]),None)
        if nz is None:break
        i,j=nz
        a[k],a[i]=a[i],a[k]
        for r in range(N):a[r][k],a[r][j]=a[r][j],a[r][k]
        while True:
            assert a[k][k]
            changed=False
            for i in range(k+1,N):
                if a[i][k]:
                    q,rem=divmod(a[i][k],a[k][k])
                    a[i]=[u-q*v for u,v in zip(a[i],a[k])]
                    if rem:
                        a[i],a[k]=a[k],a[i]
                    changed=True
                    break
            if changed:continue
            for j in range(k+1,N):
                if a[k][j]:
                    q,rem=divmod(a[k][j],a[k][k])
                    for i in range(N):a[i][j]-=q*a[i][k]
                    if rem:
                        for i in range(N):a[i][j],a[i][k]=a[i][k],a[i][j]
                    changed=True
                    break
            if changed:continue
            p=a[k][k]
            off=next(((i,j) for i in range(k+1,N) for j in range(k+1,N) if a[i][j]%p),None)
            if off is None:break
            i,j=off
            a[k]=[u+v for u,v in zip(a[k],a[i])]
        if a[k][k]<0:a[k]=[-u for u in a[k]]
        assert all(a[i][k]==0 for i in range(k+1,N))
        assert all(a[k][j]==0 for j in range(k+1,N))
    assert all(a[i][j]==0 for i in range(N) for j in range(N) if i!=j)
    d=[a[i][i] for i in range(N)]
    assert all(d[i]>0 for i in range(N))
    assert all(y%x==0 for x,y in zip(d,d[1:]))
    return d


def poly_mul(P,Q):
    Z=[0]*(len(P)+len(Q)-1)
    for i,u in enumerate(P):
        for j,v in enumerate(Q):Z[i+j]+=u*v
    return Z

def poly_power(P,k):
    Z=[1]
    for _ in range(k):Z=poly_mul(Z,P)
    return Z

def characteristic_coefficients(L):
    n=len(L);B=[[int(i==j) for j in range(n)] for i in range(n)];coef=[1]
    for k in range(1,n+1):
        B=[[sum(L[i][h]*B[h][j] for h in range(n)) for j in range(n)] for i in range(n)]
        tr=sum(B[i][i] for i in range(n));assert tr%k==0
        c=-tr//k
        for i in range(n):B[i][i]+=c
        coef.append(c)
    assert all(u==0 for row in B for u in row)
    return coef

def main():
    L=graph();N=len(L)
    expected={11:3,33:4,528:2}
    target=440049629885184
    factors=[([0,1],1),([-3,1],6),([31,-12,1],1),([16,-9,1],2),([11,-8,1],9)]
    cp=[1]
    for f,e in factors:cp=poly_mul(cp,poly_power(f,e))
    assert characteristic_coefficients(L)==list(reversed(cp))
    for root in [N-1,0,13,20]:
        B=[[L[i][j] for j in range(N) if j!=root] for i in range(N) if i!=root]
        d=smith(B)
        assert Counter(v for v in d if v!=1)==Counter(expected)
        assert prod(d)==target
        assert abs(determinant(B))==target
    print('CEVA4_RESOLVED_INTEGRAL_CRITICAL_GROUP_OK')
if __name__=='__main__':main()
