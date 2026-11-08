#!/usr/bin/env python3
"""Independent finite-field checks for the stated fixed-point-free count."""
from math import gcd
from random import Random

PAIRS = {
 (0,1):[(2,-1)], (1,0):[(2,1)],(1,1):[(3,1)],
 (1,2):[(4,1)],(3,0):[(4,1)],(3,1):[(5,1)],
 (3,2):[(6,1)],(4,1):[(6,1)],(5,0):[(6,2)],
 (5,1):[(6,1)],(4,2):[(7,3)],(5,2):[(7,1)],
 (6,0):[(7,3)],(6,1):[(7,1)]
}

def mat(p,a,b,alpha,beta,gamma,mu,nu):
    i2=pow(2,-1,p);i3=pow(3,-1,p);i6=pow(6,-1,p)
    C=[[0]*8 for _ in range(8)]
    def col(j,d):
        for k,x in d.items(): C[k][j]=x%p
    col(0,{0:a,2:a*alpha,7:mu})
    col(1,{0:(a-b)*i3,1:b,2:beta,3:-alpha*b,4:gamma,
           5:alpha**2*b*i2,6:-alpha*gamma-alpha**3*b*i6,7:nu})
    col(2,{2:a*b})
    col(3,{3:b*b,4:b*(beta+alpha*(b-a)*i3),5:-alpha*b*b,
           6:a*alpha**2*b*i3-alpha*b*beta+b*gamma+alpha**2*b*b*i6,
           7:-a*alpha**3*b*i6-a*alpha*gamma+alpha**2*b*beta*i2+3*beta*gamma})
    col(4,{4:a*b*b,6:-alpha*a*b*b,7:3*a*b*gamma+a*b*b*alpha**2*i2})
    col(5,{4:(a*b*b-b**3)*i3,5:b**3,6:2*b*b*beta-alpha*a*b*b,
           7:-2*a*b*alpha*beta+a*b*gamma+a*b*b*alpha**2*i6+a*a*b*alpha**2*i3+3*b*beta**2})
    col(6,{6:a*b**3,7:3*a*b*b*beta-alpha*a*a*b*b})
    col(7,{7:a*a*b**3})
    return C

def mul(u,v,p):
    out=[0]*8
    for (i,j), terms in PAIRS.items():
        for k,c in terms:out[k]+=u[i]*v[j]*c
    return [x%p for x in out]

def dotcol(M,x,p):return [sum(M[i][j]*x[j] for j in range(8))%p for i in range(8)]

def rank(A,p):
    A=[row[:] for row in A];r=0
    for j in range(len(A[0])):
        ix=next((i for i in range(r,len(A)) if A[i][j]%p),None)
        if ix is None:continue
        A[r],A[ix]=A[ix],A[r]
        v=pow(A[r][j],-1,p);A[r]=[(t*v)%p for t in A[r]]
        for i in range(len(A)):
            if i!=r:
                v=A[i][j]
                A[i]=[(x-v*y)%p for x,y in zip(A[i],A[r])]
        r+=1
    return r

def cyc(n):
    count=0
    for i in range(n):
      for j in range(n):
        if all(x%n for x in [i,j,i+j,2*j,i+2*j,3*j,i+3*j,2*i+3*j]):count+=1
    return count

def closed(n):
    assert n%2==0
    g=gcd(n,3);d=int(n%4==0)
    return n*n-(6+g)*n+4+6*g+2*d

rng=Random(4937); tested=0;matrices=0
for p in (5,7,11,13,17):
 n=p-1
 assert cyc(n)==closed(n)
 for a in range(1,p):
  for b in range(1,p):
   params=[(0,0,0,0,0),tuple(rng.randrange(p) for _ in range(5))]
   for al,be,ga,mu,nu in params:
    M=mat(p,a,b,al,be,ga,mu,nu)
    E=[[int(i==j) for i in range(8)] for j in range(8)]
    for i in range(8):
      for j in range(8):
        lhs=mul(dotcol(M,E[i],p),dotcol(M,E[j],p),p)
        rhs=dotcol(M,mul(E[i],E[j],p),p)
        assert lhs==rhs,(p,a,b,(al,be,ga,mu,nu),i,j,lhs,rhs)
        tested+=1
    assert rank(M,p)==8
    ident=[[M[i][j]-int(i==j) for j in range(8)] for i in range(8)]
    zero=rank(ident,p)==8
    predicted=all(pow(a,x,p)*pow(b,y,p)%p!=1 for x,y in [(1,0),(0,1),(1,1),(0,2),(1,2),(0,3),(1,3),(2,3)])
    assert zero==predicted
    matrices+=1
for n in (6,8,12,18,24,30,36,48,60,72,120):
    assert cyc(n)==closed(n)
print(f'VERIFY_OK bracket_pairs={tested} matrices={matrices} cyclic_orders=16 fixed_point_rank=yes')
