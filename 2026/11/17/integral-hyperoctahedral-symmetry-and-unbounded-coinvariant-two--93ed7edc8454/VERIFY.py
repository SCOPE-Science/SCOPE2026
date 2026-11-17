"""Exact small-case combinatorial checks of magnitude-homology shuffle cycles and signed coordinate actions."""
from itertools import product, permutations
from collections import defaultdict,Counter
from math import comb

def comps(n,k):
 if n==1:
  yield (k,);return
 for j in range(k+1):
  for t in comps(n-1,k-j):yield (j,)+t

def words(a):
 def rec(a,p):
  if not sum(a):
   yield tuple(p);return
  for i,c in enumerate(a):
   if c:
    b=list(a);b[i]-=1
    yield from rec(tuple(b),p+[i])
 yield from rec(tuple(a),[])

def invsgn(w):
 return (-1)**sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))

def route(eps,w):
 v=sum((eps[i]&1)<<i for i in range(len(eps)))
 out=[v]
 for i in w:v^=1<<i;out.append(v)
 return tuple(out)

def cycle(eps,a):
 return {route(eps,w):invsgn(w) for w in words(a)}

def boundary(c):
 b=defaultdict(int)
 for p,coeff in c.items():
  for j in range(1,len(p)-1):
   u,v,t=p[j-1:j+2]
   if (u^t).bit_count()==2:
    b[p[:j]+p[j+1:]]+=((-1)**(j-1))*coeff
 return {x:v for x,v in b.items() if v}

def permute_bits(v,p,n):
 return sum((v>>i&1)<<p[i] for i in range(n))

def action(c,p,t):
 n=len(p)
 return {tuple(permute_bits(x,p,n)^t for x in path):coef for path,coef in c.items()}

def signs_perm(a,p):
 return (-1)**sum(a[i]*a[j] for i in range(len(a)) for j in range(i+1,len(a)) if p[i]>p[j])

def partitions(n,k):
 return {tuple(sorted((x for x in a if x),reverse=True)) for a in comps(n,k)}

def expected_counts(n,k):
 ps=partitions(n,k)
 bad=[p for p in ps if any(t%2 and p.count(t)>1 for t in p)]
 return len(ps)-len(bad),len(bad)

for n in range(1,5):
 for k in range(0,5):
  if n==4 and k==4:pass
  for a in comps(n,k):
   eps=(0,)*n
   c=cycle(eps,a)
   assert len(c)==sum(1 for _ in words(a))
   assert not boundary(c),(n,k,a,boundary(c))
   for i in range(n-1):
    p=list(range(n));p[i],p[i+1]=p[i+1],p[i]
    b=tuple(a[p.index(j)] for j in range(n))
    exp=cycle(tuple(eps[p.index(j)] for j in range(n)),b)
    res=action(c,p,0)
    s=signs_perm(a,p)
    assert res=={x:s*z for x,z in exp.items()},(n,k,a,p,s)
   e0=(1,)+ (0,)*(n-1)
   c2=cycle(e0,a)
   assert action(c,list(range(n)),1)==c2
  if n<=3:
   rank=2**n*comb(n+k-1,n-1)
   good,bad=expected_counts(n,k)
   print('n',n,'k',k,'rank',rank,'coinvariants free',good,'Z/2',bad)
print('all small shuffle-boundary and action assertions passed')

# Optional exact Smith reductions of the action-relation matrix.
# Usage: python VERIFY.py --smith  (requires SymPy)
if __name__=='__main__' and '--smith' in __import__('sys').argv:
 from sympy import zeros, ZZ
 from sympy.matrices.normalforms import smith_normal_form
 def coinvariant_snf(n,k):
  basis=[(eps,a) for eps in product(range(2),repeat=n) for a in comps(n,k)]
  idx={b:i for i,b in enumerate(basis)}
  gen=2*n-1
  mat=zeros(len(basis),len(basis)*gen)
  for col,(eps,a) in enumerate(basis):
   for j in range(n):
    ep=tuple(v^(i==j) for i,v in enumerate(eps))
    mat[idx[(ep,a)],col*gen+j]+=1
    mat[col,col*gen+j]-=1
   for j in range(n-1):
    p=list(range(n));p[j],p[j+1]=p[j+1],p[j]
    ep=tuple(eps[p.index(i)] for i in range(n))
    ap=tuple(a[p.index(i)] for i in range(n))
    mat[idx[(ep,ap)],col*gen+n+j]+=signs_perm(a,p)
    mat[col,col*gen+n+j]-=1
  D=smith_normal_form(mat,domain=ZZ)
  nz=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
  return (len(basis)-len(nz),tuple(sorted(x for x in nz if x>1)))
 for n,k in [(2,2),(2,6),(3,2),(3,3),(3,4)]:
  got=coinvariant_snf(n,k)
  free,bad=expected_counts(n,k)
  assert got==(free,(2,)*bad),(n,k,got,free,bad)
  print('smith',n,k,'free',got[0],'torsion',got[1])
 print('exact integer Smith checks passed')
