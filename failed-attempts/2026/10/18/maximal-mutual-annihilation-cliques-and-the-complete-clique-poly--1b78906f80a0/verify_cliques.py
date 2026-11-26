#!/usr/bin/env python3
"""Exact finite-field checks for the rank-one mutual-annihilation graph."""
import itertools,math
from collections import Counter

def gauss(n,k,q):
    if k<0 or k>n:return 0
    v=1
    for i in range(k):v=v*(q**(n-i)-1)//(q**(i+1)-1) if False else v
    a=1;b=1
    for i in range(k):a*=q**(n-i)-1;b*=q**(k-i)-1
    return a//b

def mu(d,q):return (-1)**d*q**(d*(d-1)//2)
def predicted(n,q):
    coeff=Counter()
    for r in range(1,n):
      for s in range(1,n-r+1):
        x=gauss(n,r,q)*gauss(n-r,s,q)
        for i in range(r+1):
          for j in range(s+1):
            w=x*gauss(r,i,q)*gauss(s,j,q)*mu(r-i,q)*mu(s-j,q)
            c=(q**i-1)*(q**j-1)//(q-1)
            for k in range(c+1):coeff[k]+=w*math.comb(c,k)
    coeff[0]+=1
    return {k:v for k,v in coeff.items() if v}

def dyad_matrices(n,q):
    vlist=list(itertools.product(range(q),repeat=n)); zero=(0,)*n
    mats={}
    for u in vlist:
      if u==zero:continue
      for f in vlist:
        if f==zero or sum(x*y for x,y in zip(u,f))%q:continue
        mat=tuple((a*b)%q for a in u for b in f)
        mats[mat]=(u,f)
    return sorted(mats)

def maximal_cliques(n,q):
    mats=dyad_matrices(n,q);N=len(mats)
    adj=[0]*N
    # Explicit matrix-products AB and BA, not projective/incidence criterion.
    for i,a in enumerate(mats):
      for j in range(i):
        b=mats[j]
        if all(sum(a[x*n+y]*b[y*n+z] for y in range(n))%q==0 and sum(b[x*n+y]*a[y*n+z] for y in range(n))%q==0 for x in range(n) for z in range(n)):
          adj[i]|=1<<j;adj[j]|=1<<i
    answer=[]
    def bk(R,P,X):
      if not P and not X:
        answer.append(R);return
      ux=P|X
      pivot=max((i for i in range(N) if ux>>i&1),key=lambda i:(P&adj[i]).bit_count()) if ux else -1
      choices=P & (~adj[pivot] if pivot>=0 else P)
      while choices:
        b=choices & -choices;v=b.bit_length()-1
        bk(R|b,P&adj[v],X&adj[v]);P^=b;X|=b;choices^=b
    bk(0,(1<<N)-1,0)
    return mats,answer

def spaces(n,q):
    # independent enumeration of all row-reduced subspaces over prime fields
    out=[]
    for d in range(n+1):
      for piv in itertools.combinations(range(n),d):
        slots=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
        for values in itertools.product(range(q),repeat=len(slots)):
          rows=[[0]*n for _ in range(d)]
          for i,p in enumerate(piv):rows[i][p]=1
          for (i,j),value in zip(slots,values):rows[i][j]=value
          out.append((d,tuple(tuple(v) for v in rows)))
    return out

def image_span_rank(indices,mats,n,q):
    # Independent Gaussian elimination on columns of literal matrices.
    basis=[]
    for i in indices:
      a=mats[i]
      # find first nonzero column
      col=next((j for j in range(n) if any(a[r*n+j] for r in range(n))),None)
      if col is None:continue
      u=[a[r*n+col] for r in range(n)]
      for p,b in basis:
        c=u[p];u=[(u[t]-c*b[t])%q for t in range(n)]
      if any(u):
        p=next(t for t in range(n) if u[t]);inv=pow(u[p],-1,q)
        u=[(v*inv)%q for v in u];basis.append((p,u));basis.sort()
    return len(basis)

def check(n,q):
    mats,cliques=maximal_cliques(n,q)
    actual=Counter();seen=set()
    for c in cliques:
      vertices=[i for i in range(len(mats)) if c>>i&1]
      for d in range(len(vertices)+1):
        for chosen in itertools.combinations(vertices,d):seen.add(tuple(chosen))
    for v in seen:actual[len(v)]+=1
    expect=predicted(n,q)
    assert dict(actual)==expect,(n,q,dict(actual),expect)
    sizes=Counter(c.bit_count() for c in cliques)
    pred_sizes=Counter()
    for r in range(1,n):pred_sizes[(q**r-1)*(q**(n-r)-1)//(q-1)]+=gauss(n,r,q)
    assert sizes==pred_sizes,(n,q,sizes,pred_sizes)
    # every maximal clique is the complete dyad family of its image span
    for c in cliques:
      inds=[i for i in range(len(mats)) if c>>i&1]
      r=image_span_rank(inds,mats,n,q)
      assert c.bit_count()==(q**r-1)*(q**(n-r)-1)//(q-1)
    print('PASS',f'n={n}',f'q={q}',f'vertices={len(mats)}',f'maximal={len(cliques)}',f'cliques={len(seen)}',f'sizes={dict(sorted(sizes.items()))}')

if __name__=='__main__':
  for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:check(n,q)
  print('VERIFY_OK_MAXIMAL_ZERO_PRODUCT_CLIQUES')
