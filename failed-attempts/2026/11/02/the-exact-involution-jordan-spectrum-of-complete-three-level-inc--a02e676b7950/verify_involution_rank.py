#!/usr/bin/env python3
"""Independent finite-field census for the square-zero radical of a 3-layer incidence algebra."""
import itertools,math,collections

def gb(n,r,q):
    if r<0 or r>n:return 0
    num=math.prod(q**(n-i)-1 for i in range(r))
    den=math.prod(q**(r-i)-1 for i in range(r))
    return num//den

def rankcount(m,n,r,q):
    if r<0 or r>min(m,n):return 0
    return gb(m,r,q)*math.prod(q**n-q**i for i in range(r))

def spectrum(a,b,c,q):
    out=collections.Counter()
    for alpha in range(min(a,b)+1):
      for beta in range(min(b-alpha,c)+1):
        for rho in range(min(a-alpha,c-beta)+1):
          value=rankcount(a,b,alpha,q)*rankcount(b-alpha,c,beta,q)*q**(alpha*(c-beta)+a*beta)*rankcount(a-alpha,c-beta,rho,q)
          out[alpha+beta+rho]+=value
    return dict(sorted(out.items()))

def rk(mat,q):
    m=[v[:] for v in mat]
    n=len(m); p=len(m[0]); row=0
    for j in range(p):
      k=next((i for i in range(row,n) if m[i][j]),None)
      if k is None:continue
      m[row],m[k]=m[k],m[row]
      z=pow(m[row][j],-1,q)
      m[row]=[(x*z)%q for x in m[row]]
      for i in range(row+1,n):
        t=m[i][j]
        if t:m[i]=[(x-t*y)%q for x,y in zip(m[i],m[row])]
      row+=1
      if row==n:break
    return row

def enumerate_spectrum(a,b,c,q):
    n=a+b+c
    indices=[(i,j) for i in range(a) for j in range(a,a+b)] +[(i,j) for i in range(a,a+b) for j in range(a+b,n)]+[(i,j) for i in range(a) for j in range(a+b,n)]
    cnt=collections.Counter()
    for v in itertools.product(range(q),repeat=len(indices)):
      x=[[0]*n for _ in range(n)]
      for (i,j),z in zip(indices,v):x[i][j]=z
      if any(sum(x[i][k]*x[k][j] for k in range(n))%q for i in range(n) for j in range(n)):continue
      cnt[rk(x,q)]+=1
    return dict(sorted(cnt.items()))

if __name__=='__main__':
    N=0
    for q,params in [(2,[(1,1,1),(1,2,1),(2,1,2),(2,2,2),(1,2,2),(2,3,1),(3,1,1)]),
                     (3,[(1,1,1),(1,2,1),(1,1,2),(2,1,1)]),
                     (5,[(1,1,1)])]:
      for a,b,c in params:
        pred=spectrum(a,b,c,q)
        obs=enumerate_spectrum(a,b,c,q)
        assert pred==obs,(q,a,b,c,pred,obs)
        N+=1
        print(q,(a,b,c),pred)
    print('THREE_LEVEL_INCIDENCE_INVOLUTION_RANK_OK',N)
