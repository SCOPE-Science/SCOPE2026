#!/usr/bin/env python3
"""Independent finite matrix enumeration for square-zero Heisenberg derivations."""
from itertools import product
from math import prod

def rank(mat,q):
    a=[list(map(lambda x:x%q,row)) for row in mat]
    if not a:return 0
    n=len(a);cols=len(a[0]);k=0
    for j in range(cols):
        pivot=next((i for i in range(k,n) if a[i][j]%q),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        t=pow(a[k][j],-1,q)
        a[k]=[(v*t)%q for v in a[k]]
        for i in range(n):
            if i!=k:
                x=a[i][j]
                if x:a[i]=[(v-x*w)%q for v,w in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k

def mul(A,B,q):
    return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*B)] for row in A]

def zero(A):return all(v==0 for row in A for v in row)

def isocount(m,r,q):
    if not 0<=r<=m:return 0
    v=1
    # Gaussian binomial times product (q^(m-i)+1)
    v=prod(q**(m-i)-1 for i in range(r))*prod(q**(m-i)+1 for i in range(r))
    v//=prod(q**(r-i)-1 for i in range(r))
    return v

def symcount(r,q):
    if r==0:return 1
    return q**(r*(r+1)//2-sum(2*i-1 for i in range(1,(r+1)//2+1)))*prod(q**(2*i-1)-1 for i in range(1,(r+1)//2+1))

def formula(m,q):
    out=[0]*(m+1)
    for r in range(m+1):
        a=isocount(m,r,q)*symcount(r,q)
        out[r]+=a*q**r
        if r+1<=m:out[r+1]+=a*(q**(2*m-r)-q**r)
    return out

def brute(m,q):
    n=2*m;count=[0]*(m+1)
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    Acount=[0]*(m+1)
    tested=0
    # J with blocks [[0,I],[-I,0]]; JA=B -> A=-JB
    for values in product(range(q),repeat=len(pairs)):
        B=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,values):B[i][j]=B[j][i]=v
        J=[[0]*n for _ in range(n)]
        for i in range(m):J[i][m+i]=1;J[m+i][i]=-1%q
        A=[[-sum(J[i][k]*B[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]
        if not zero(mul(A,A,q)):continue
        r=rank(A,q);Acount[r]+=1
        for ph in product(range(q),repeat=n):
            if any(sum(ph[i]*A[i][j] for i in range(n))%q for j in range(n)):continue
            D=[row+[0] for row in A]+[list(ph)+[0]]
            s=rank(D,q)
            assert s<=m
            assert zero(mul(D,D,q))
            count[s]+=1
        tested+=1
    return count,Acount,tested

if __name__=='__main__':
    for m,q in [(1,2),(1,3),(1,5),(2,2),(2,3)]:
        got,Ac,nt=brute(m,q)
        want=formula(m,q)
        assert got==want,(m,q,got,want)
        Af=[isocount(m,r,q)*symcount(r,q) for r in range(m+1)]
        assert Ac==Af,(m,q,Ac,Af)
        print('m',m,'q',q,'derivation_rank_counts',got,'squarezero_sp_rank_counts',Ac,'tested_A',nt)

def gf4_mul(a,b):
    t=0
    for i in (0,1):
        for j in (0,1):
            if (a>>i)&1 and (b>>j)&1:t^=1<<(i+j)
    if t&4:t^=7 # x^2=x+1
    return t

def gf4_dot(x,y):
    z=0
    for a,b in zip(x,y):z^=gf4_mul(a,b)
    return z

def gf4_product(A,B):
    return [[gf4_dot(row,col) for col in zip(*B)] for row in A]

def gf4_rank(A):
    a=[row[:] for row in A]
    n=len(a);d=len(a[0]);k=0
    for j in range(d):
        ii=next((i for i in range(k,n) if a[i][j]),None)
        if ii is None:continue
        a[ii],a[k]=a[k],a[ii]
        inv={1:1,2:3,3:2}[a[k][j]]
        a[k]=[gf4_mul(x,inv) for x in a[k]]
        for i in range(n):
            if i!=k:
                y=a[i][j]
                if y:a[i]=[x^gf4_mul(y,t) for x,t in zip(a[i],a[k])]
        k+=1
    return k

def brute_gf4_m1():
    count=[0,0];a_count=[0,0]
    for x,y,z in product(range(4),repeat=3):
        B=[[x,y],[y,z]]
        A=[[y,z],[x,y]] # J inverse =J in characteristic 2
        if not zero(gf4_product(A,A)):continue
        r=gf4_rank(A);a_count[r]+=1
        for u,v in product(range(4),repeat=2):
            if gf4_dot([u,v],[A[0][0],A[1][0]]) or gf4_dot([u,v],[A[0][1],A[1][1]]):continue
            D=[row+[0] for row in A]+[[u,v,0]]
            assert zero(gf4_product(D,D))
            count[gf4_rank(D)]+=1
    assert a_count==[isocount(1,r,4)*symcount(r,4) for r in range(2)]
    assert count==formula(1,4)
    print('m 1 q 4 derivation_rank_counts',count,'squarezero_sp_rank_counts',a_count)

if __name__=='__main__':
    brute_gf4_m1()

from fractions import Fraction

def exact_simplified(m,r,q):
    exponent=r*(2*m-r+1)
    C=Fraction(1)
    for t in range(m-r+1,m+1):C*=Fraction(q**(2*t)-1,q**(2*t))
    for t in range(1,r//2+1):C/=Fraction(q**(2*t)-1,q**(2*t))
    ans=q**exponent*C
    assert ans.denominator==1
    return ans.numerator

def direct_lie_check(m,q):
    assert m==1 and q in (2,3)
    # Basis (e,f,z). Bilinear bracket [e,f]=z, [f,e]=-z.
    count=[0,0]
    for cells in product(range(q),repeat=9):
        D=[list(cells[i*3:(i+1)*3]) for i in range(3)]
        if not zero(mul(D,D,q)):continue
        # columns represent images of basis vectors
        def bracket(a,b):return [0,0,(a[0]*b[1]-a[1]*b[0])%q]
        cols=list(zip(*D))
        good=True
        for i in range(3):
            for j in range(3):
                lhs=[sum(D[t][k]*bracket([int(k==i) for k in range(3)],[int(k==j) for k in range(3)])[k] for k in range(3))%q for t in range(3)]
                a=bracket(cols[i],[int(k==j) for k in range(3)])
                b=bracket([int(k==i) for k in range(3)],cols[j])
                rhs=[(a[t]+b[t])%q for t in range(3)]
                if lhs!=rhs:good=False
        if good:count[rank(D,q)]+=1
    assert count==formula(m,q),(count,formula(m,q))
    print('direct_all_linear_maps',q,count)

if __name__=='__main__':
    direct_lie_check(1,2)
    direct_lie_check(1,3)
    for q in (2,3,5):
        for m in range(1,8):
            assert [exact_simplified(m,r,q) for r in range(m+1)]==[isocount(m,r,q)*symcount(r,q) for r in range(m+1)]
    for q in (2,3,5):
        for m in (8,12,16):
            arr=formula(m,q)
            p=Fraction(arr[-1],sum(arr))
            from math import prod
            weights=[]
            c=1.0
            for j in range(16):
                if j:c*=1-q**(-2*j)
                weights.append((q**(-j*(j+2))+q**(-(j+1)**2))/c)
            print('limit_maxrank',q,'m',m,'finite',round(float(p),9),'limit',round(weights[0]/sum(weights),9))
    print('VERIFY_OK')
