"""Exact binary checks for incidence-wave orders on finite partial geometries.

Standard library only. Matrices are lists of bit-packed rows; arithmetic is GF(2).
All numerical conclusions are finite checks, distinct from the all-geometry proof.
"""
from itertools import product
from math import gcd


def ident(n): return [1 << i for i in range(n)]

def matmul(X,Y):
    Z=[]
    for row in X:
        a=0
        while row:
            bit=row & -row; j=bit.bit_length()-1; a^=Y[j];row^=bit
        Z.append(a)
    return Z

def plus(X,Y): return [a^b for a,b in zip(X,Y)]

def rank(X):
    basis={}
    for x in X:
        while x:
            j=x.bit_length()-1
            if j in basis: x^=basis[j]
            else: basis[j]=x;break
    return len(basis)

def kernel(X): return len(X)-rank(X)

def power(X,k):
    a=ident(len(X)); b=X
    while k:
        if k&1:a=matmul(a,b)
        b=matmul(b,b);k>>=1
    return a

def norm(vec,q):
    inv=pow(next(a for a in vec if a),-1,q)
    return tuple(a*inv%q for a in vec)

def projective(q):
    pts=sorted({norm(p,q) for p in product(range(q),repeat=3) if any(p)})
    return [[int(sum(a*b for a,b in zip(p,l))%q==0) for l in pts] for p in pts],q,q,q+1

def net(q,r):
    pts=list(product(range(q),repeat=2)); lines=[]
    for slope in (list(range(q))+[None])[:r]:
        for c in range(q):
            lines.append({(c,y) for y in range(q)} if slope is None else
                         {(x,(slope*x+c)%q) for x in range(q)})
    return [[int(p in line) for line in lines] for p in pts],q-1,r-1,r-1

def symplectic(q):
    pts=sorted({norm(p,q) for p in product(range(q),repeat=4) if any(p)})
    def perp(u,v):return (u[0]*v[1]-u[1]*v[0]+u[2]*v[3]-u[3]*v[2])%q==0
    lines=set()
    for i,u in enumerate(pts):
        for v in pts[i+1:]:
            if perp(u,v):
                lines.add(frozenset(norm(tuple((a*x+b*y)%q for x,y in zip(u,v)),q)
                                    for a,b in product(range(q),repeat=2) if a or b))
    return [[int(p in line) for line in sorted(lines)] for p in pts],q,q,1

def triangle():
    return [[1,1,0],[0,1,1],[1,0,1]],1,1,2

def graph(B):
    v=len(B);b=len(B[0]);A=[0]*(v+b)
    for i,row in enumerate(B):
        for j,a in enumerate(row):
            if a: A[i]|=1<<(v+j);A[v+j]|=1<<i
    return A

def two_row(A):
    n=len(A);T=[]
    for i,a in enumerate(A):T.append(a|(1<<(n+i)))
    for i in range(n): T.append(1<<i)
    return T

def verify(B,s,t,alpha,name):
    v=len(B);b=len(B[0]);assert v> s+1 and b>t+1
    assert all(len(row)==b and sum(row)==t+1 for row in B)
    assert all(sum(B[i][j] for i in range(v))==s+1 for j in range(b))
    for i in range(v):
        for j in range(i+1,v):assert sum(B[i][k]*B[j][k] for k in range(b))<=1
        for j in range(b):
            if B[i][j]==0:
                assert sum(B[i][k]*B[u][k]*B[u][j] for k in range(b) for u in range(v))==alpha
    A=graph(B);n=len(A);I=ident(n)
    K=[sum(1<<(v+j) for j in range(b)) for i in range(v)]+[(1<<v)-1 for j in range(b)]
    c=(s+t+1-alpha)%2; a=alpha%2
    A2=matmul(A,A);A3=matmul(A2,A);A4=matmul(A3,A);A5=matmul(A4,A)
    assert A3==plus(A if c else [0]*n,K if a else [0]*n)
    proj=(s==t and s%2==0 and alpha==s+1)
    if not a:
        L=6 if s%2==t%2 else 8
    elif s%2 and t%2: L=8
    elif proj:L=12
    else:L=24
    if a and not(s%2 and t%2):assert A5==A3
    if a and s%2 and t%2:assert A4==[0]*n and A3==K
    if proj:assert A4==A2
    if a and s%2==t%2==0 and not proj:assert A4!=A2
    P=[I]
    for j in range(1,6):P.append(matmul(P[-1],A))
    d=[kernel(M) for M in P]
    a_mult=[2*d[j]-d[j-1]-d[j+1] for j in range(1,5)]
    if any(z<0 for z in a_mult):raise AssertionError(a_mult)
    IplusA=plus(A,I); e1=kernel(IplusA);e2=kernel(matmul(IplusA,IplusA))
    b_mult=[2*e1-e2,e2-e1]
    assert all(z>=0 for z in b_mult)
    assert sum((j+1)*a_mult[j] for j in range(4))+b_mult[0]+2*b_mult[1]==n
    T=two_row(A);IdT=ident(2*n);cur=IdT;order=None
    for k in range(1,25):
        cur=matmul(cur,T)
        two= k & -k
        E=sum(a_mult[j]*min(2*(j+1),two) for j in range(4))
        if k%3==0: E+=2*sum(b_mult[j]*min(j+1,two) for j in range(2))
        assert kernel(plus(cur,IdT))==E,(name,k,E,kernel(plus(cur,IdT)))
        if order is None and cur==IdT:order=k
    assert order==L,(name,order,L)
    print(f'{name}: pg({s},{t},{alpha}), incidence={v}x{b}, rank={rank(graph(B))//2}, order={order}, J0={a_mult}, J1={b_mult}, fixedspace(1,2,3,4,6,8,12,24)='+str([fixedspace(A,k) for k in (1,2,3,4,6,8,12,24)]))

def fixedspace(A,k):
    T=two_row(A)
    return kernel(plus(power(T,k),ident(2*len(A))))

if __name__=='__main__':
    samples=[('triangle pg(1,1,2)',triangle()),('net(2,2)',net(2,2)),('net(2,3)',net(2,3)),('net(3,2)',net(3,2)),('net(3,3)',net(3,3)),('net(3,4)',net(3,4)),('net(5,2)',net(5,2)),('net(5,3)',net(5,3)),('net(5,4)',net(5,4)),('PG(2,2)',projective(2)),('PG(2,3)',projective(3)),('W(2)',symplectic(2)),('W(3)',symplectic(3))]
    for name,sample in samples:verify(*sample,name)
    print('PASS: 13 independently constructed incidences; axioms, cubic identity, exact order, 312 fixed-space rank comparisons.')
