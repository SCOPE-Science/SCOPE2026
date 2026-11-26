#!/usr/bin/env python3
"""Exact direct Cartier calculation and independent residue-count check for a scalar quotient.
Only Python standard library is required.
"""
from itertools import product
from math import comb, factorial, prod

def predicted_rank(p,h):
    assert p%2 and h%2==0 and h>=2
    value=(p+1)*(2*p**(h-1)+p-3)
    assert value%24==0
    return value//24

def residue_count(p,h):
    d=2*(p-1)
    q=p**(h-2)
    answer=0
    for s in range(p-1):
      for t in range(p-1-s):
        num=q*(p-1-s-t)
        residue=(-p**(h-1)*t-2*s-1)%d
        if residue<num:
          answer+=1+(num-1-residue)//d
    return answer

def basis(p,h):
    d=2*(p-1)
    return [(i,j) for j in range(p-1) for i in range(p**(h-1)*(p-1-j))
            if (i+2*j+1)%d==0]

def compositions(n,r):
    if r==1:
      yield (n,)
    else:
      for v in range(n+1):
        for rem in compositions(n-v,r-1):
          yield (v,)+rem

def rank_mod_p(rows,p):
    r=0
    if not rows:return 0
    n=len(rows)
    m=len(rows[0])
    for j in range(m):
      k=next((k for k in range(r,n) if rows[k][j]%p),None)
      if k is None:continue
      rows[r],rows[k]=rows[k],rows[r]
      inv=pow(rows[r][j]%p,-1,p)
      rows[r]=[v*inv%p for v in rows[r]]
      for i in range(r+1,n):
        c=rows[i][j]%p
        if c:
          # pivot calculation only after the pivot
          for k2 in range(j+1,m):
            rows[i][k2]=(rows[i][k2]-c*rows[r][k2])%p
          rows[i][j]=0
      r+=1
      if r==n:break
    return r

def direct_rank(p,h):
    d=2*(p-1)
    bas=basis(p,h); g=len(bas)
    assert g==(p**h-1)//4,(p,h,g)
    index={x:k for k,x in enumerate(bas)}
    mat=[[0]*g for _ in range(g)]
    support=list(range(0,h+1,2))
    for col,(i,j) in enumerate(bas):
      for tau in range(j+1):
        n=j-tau
        for cts in compositions(n,len(support)):
          exponent=i+sum(z*(p**nu+1) for z,nu in zip(cts,support))
          if exponent%p !=p-1:continue
          output=((exponent-(p-1))//p,tau)
          assert output in index,(p,h,(i,j),output)
          multinom=factorial(n)//prod(factorial(z) for z in cts)
          coef=(-1 if n%2 else 1)*comb(j,tau)*multinom
          row=index[output]
          mat[row][col]=(mat[row][col]+coef)%p
    return rank_mod_p(mat,p)

if __name__=='__main__':
    for p,h in [(3,2),(3,4),(3,6),(5,2),(5,4),(7,2),(11,2),(13,2)]:
        wanted=predicted_rank(p,h)
        by_residue=residue_count(p,h)
        by_matrix=direct_rank(p,h)
        assert wanted==by_residue==by_matrix, (p,h,wanted,by_residue,by_matrix)
        print(f'p={p}, h={h}, genus={(p**h-1)//4}, Cartier_rank={wanted}, a_number={(p**h-1)//4-wanted}')
    print('VERIFY_OK')
