#!/usr/bin/env python3
"""Exhaustive finite-field tests for reversal-inner algebra anti-involutions."""
from itertools import product

def mul(a,b,n,q):
    c=[0]*(n*n)
    for i in range(n):
      for j in range(n):
        c[i*n+j]=sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
    return tuple(c)

def flip(a,n):
    return tuple(a[(n-1-j)*n+(n-1-i)] for i in range(n) for j in range(n))

def inverse(a,n,q):
    res=[0]*(n*n)
    for i in range(n-1,-1,-1):
      res[i*n+i]=pow(a[i*n+i],-1,q)
      for j in range(i+1,n):
        res[i*n+j]=(-res[i*n+i]*sum(a[i*n+k]*res[k*n+j] for k in range(i+1,j+1)))%q
    return tuple(res)

def all_g(n,q):
    coords=[(i,j) for i in range(n) for j in range(i,n)]
    allowed=[range(1,q) if i==j else range(q) for i,j in coords]
    for vals in product(*allowed):
      a=[0]*(n*n)
      for (i,j),v in zip(coords,vals):a[i*n+j]=v
      yield tuple(a)

def predicted(n,q):
    if n%2:
      m=(n-1)//2
      return (q-1)**m*q**(m*(m+1))
    m=n//2
    plus=(q-1)**(m-1)*q**(m*m)
    minus=(q-1)**(m-1)*q**(m*(m-1)) if q%2 else 0
    return plus+minus

def run(n,q):
    basis=[]
    for i in range(n):
      for j in range(i,n):
        a=[0]*(n*n);a[i*n+j]=1;basis.append(tuple(a))
    counts={}; maps=set(); rep=[]
    for g in all_g(n,q):
      gs=flip(g,n)
      # g^*=c g using the (0,0) entry; all scalars are nonzero.
      c=(gs[0]*pow(g[0],-1,q))%q
      if c==0 or any((v-c*w)%q for v,w in zip(gs,g)):continue
      counts[c]=counts.get(c,0)+1
      # canonical projective representative; upper triangular center is scalar
      v=pow(g[0],-1,q)
      can=tuple((v*z)%q for z in g)
      maps.add(can)
      if len(rep)<12: rep.append(g)
    # Explicitly verify involution on all matrix units for each projective class.
    for g in maps:
      gi=inverse(g,n,q)
      def anti(a):return mul(mul(gi,flip(a,n),n,q),g,n,q)
      for e in basis:
        assert anti(anti(e))==e, (n,q,g,e)
      for a in basis:
        for b in basis:
          lhs=anti(mul(a,b,n,q))
          rhs=mul(anti(b),anti(a),n,q)
          assert lhs==rhs, (n,q,g,a,b)
    assert sum(counts.values())==(q-1)*predicted(n,q)
    assert len(maps)==predicted(n,q)
    print(f'n={n} q={q} scalar-types={counts} projective-involutions={len(maps)} prediction={predicted(n,q)} PASS')

if __name__=='__main__':
    for n,q in ((2,2),(2,3),(2,5),(3,2),(3,3),(4,2),(4,3)):
      run(n,q)
    print('REVERSAL_INNER_INVOLUTION_CENSUS_OK')
