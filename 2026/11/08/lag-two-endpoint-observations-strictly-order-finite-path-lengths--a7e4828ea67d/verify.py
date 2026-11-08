"""Exact finite-size checks for endpoint observations of synchronous noisy voter paths.
Standalone: Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product


def solve(a,b):
    a=[list(row)+[b[i]] for i,row in enumerate(a)]; n=len(a)
    for k in range(n):
        j=next(i for i in range(k,n) if a[i][k])
        a[k],a[j]=a[j],a[k]
        z=a[k][k]
        for h in range(k,n+1): a[k][h]/=z
        for i in range(n):
            if i==k or not a[i][k]: continue
            z=a[i][k]
            for h in range(k,n+1): a[i][h]-=z*a[k][h]
    return [a[i][-1] for i in range(n)]


def walk(n):
    P=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        neigh=[j for j in (i-1,i+1) if 0<=j<n]
        for j in neigh: P[i][j]=F(1,len(neigh))
    return P


def square_exit(n,c):
    L=n-1
    ss=[(i,j) for i in range(1,L) for j in range(-L+1,0)]
    ix={s:k for k,s in enumerate(ss)}
    mat=[[F(int(i==j)) for j in range(len(ss))] for i in range(len(ss))]
    vec=[F(0) for _ in ss]
    for k,(x,y) in enumerate(ss):
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            v=(x+dx,y+dy); w=c*c/4
            if v in ix: mat[k][ix[v]]-=w
            else:vec[k]+=w
    return solve(mat,vec)[ix[(1,-1)]]


def pair_meet(n,c):
    P=walk(n)
    ss=[(i,j) for i in range(n) for j in range(n) if i!=j and (i-j)%2==0]
    ix={s:k for k,s in enumerate(ss)}
    mat=[[F(int(i==j)) for j in range(len(ss))] for i in range(len(ss))]
    vec=[F(0) for _ in ss]
    for k,(i,j) in enumerate(ss):
        for a in range(n):
            for b in range(n):
                w=c*c*P[i][a]*P[j][b]
                if not w:continue
                if a==b:vec[k]+=w
                else:mat[k][ix[a,b]]-=w
    return solve(mat,vec)[ix[(0,2)]]


def covariance(n,c):
    P=walk(n)
    ss=[(i,j) for i in range(n) for j in range(i+1,n)]
    ix={s:k for k,s in enumerate(ss)}
    mat=[[F(int(i==j)) for j in range(len(ss))] for i in range(len(ss))]
    vec=[F(0) for _ in ss]
    for k,(i,j) in enumerate(ss):
        for a in range(n):
            for b in range(n):
                w=c*c*P[i][a]*P[j][b]
                if not w:continue
                if a==b:vec[k]+=w
                else:mat[k][ix[tuple(sorted((a,b)))]]-=w
    vals=solve(mat,vec)
    return {(i,j):v for (i,j),v in zip(ss,vals)}


def full_stationary(n,c):
    # Synchronous independent updates, exact full binary-state transition matrix.
    P=walk(n); bits=list(product((0,1),repeat=n)); N=len(bits)
    matrix=[[F(0) for _ in range(N)] for _ in range(N)]
    for i,s in enumerate(bits):
        q=[(1-c)/2+c*sum(P[v][w]*s[w] for w in range(n)) for v in range(n)]
        for j,t in enumerate(bits):
            z=F(1)
            for v in range(n):z*=q[v] if t[v] else 1-q[v]
            matrix[i][j]=z
        assert sum(matrix[i])==1
    eq=[[matrix[j][i]-F(int(i==j)) for j in range(N)] for i in range(N-1)]
    eq.append([F(1)]*N)
    pi=solve(eq,[F(0)]*(N-1)+[F(1)])
    assert sum(pi)==1 and all(p>0 for p in pi)
    P2=[[sum(P[i][k]*P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    h=F(0)
    for s,w in zip(bits,pi):
        prob_one=(1-c*c)/2+c*c*sum(P2[0][j]*s[j] for j in range(n))
        h+=w*(prob_one if s[0] else 1-prob_one)
    return h


def predicted(n,c):
    if n==2:return (1+c*c)/2
    return F(1,2)+c*c*(1+square_exit(n,c))/4


def main():
    count=0
    for c in (F(1,2),F(2,3)):
        h=[]
        for n in range(2,8):
            z=predicted(n,c)
            h.append(z)
            if n>=3:
                assert square_exit(n,c)==pair_meet(n,c);count+=1
                assert covariance(n,c)[(0,2)]==square_exit(n,c);count+=1
            if n<=4:
                assert full_stationary(n,c)==z;count+=1
            if n>2:
                lower=c*c/F(4)*(c*c/F(4))**(n-3)*(1-c*c)
                assert h[-2]-h[-1]>=lower;count+=1
        assert all(h[i]>h[i+1] for i in range(len(h)-1));count+=1
    print('VERIFY_OK; exact independent stationary, pair-coalescence, square-exit checks:',count)

if __name__=='__main__':main()
