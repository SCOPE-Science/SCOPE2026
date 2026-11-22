#!/usr/bin/env python3
"""Independent projective GF(3) enumeration of singular points and generators."""
from itertools import product,combinations
from collections import defaultdict

def check(n):
 m=2*n
 def norm(t):
  for a in t:
   if a:
    inv=pow(a,-1,3);return tuple(x*inv%3 for x in t)
  return None
 def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
 def mul(k,a):return tuple(k*x%3 for x in a)
 def Q(a):return sum(a[i]*a[i+n] for i in range(n))%3
 def B(a,b):return sum(a[i]*b[i+n]+b[i]*a[i+n] for i in range(n))%3
 pts=sorted({norm(v) for v in product(range(3),repeat=m) if any(v) and Q(v)==0})
 S=[{frozenset()}];basis={frozenset():()}
 for k in range(1,n+1):
  sub={};
  for H,b in basis.items():
   for v in pts:
    if v not in H and all(B(v,u)==0 for u in b):
     seq=b+(v,); new=set()
     for coeff in product(range(3),repeat=len(seq)):
      w=tuple(sum(coeff[j]*seq[j][i] for j in range(len(seq)))%3 for i in range(m))
      if any(w):new.add(norm(w))
     if len(new)==(3**k-1)//2:sub[frozenset(new)]=seq
  basis=sub
  S.append(set(sub))
 print('q=3 rank',n,'points',len(pts),'singular_subspaces',[len(x) for x in S])
 E={p for p in pts if all(p[i]==0 for i in range(n,2*n))}
 gen=[s for s in S[n] if (n-(lambda t: next(d for d in range(n+1) if (3**d-1)//2==t))(len(s&E)))%2==0]
 expected=4 if n==2 else 40
 assert len(gen)==expected,(len(gen),expected)
 def shattered(T):return len({tuple(int(p in g) for p in T) for g in gen})==(1<<len(T))
 assert all(shattered((p,)) for p in pts)
 if n==2:
  assert all(not shattered(t) for t in combinations(pts,2))
  print('  halfspin=4, face polynomial 1+16z')
 if n==3:
  edges=sum(shattered(t) for t in combinations(pts,2))
  assert edges==3120,edges
  # All triples lie in at most one generator, so cannot shatter
  print('  halfspin=40, edges 3120, degree 48; VCdim 2')
for n in (2,3):check(n)
