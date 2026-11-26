from itertools import product
from collections import Counter
from math import factorial

def canon(s):
 return min(s[i:]+s[:i] for i in range(len(s)))

def good(s,n):
 m=len(s)
 return len({tuple(s[(i+j)%m] for j in range(n)) for i in range(m)})==m

def constpos(s,n):
 m=len(s)
 return { (i+j)%m for i in range(m) if all(s[(i+t)%m]==s[i] for t in range(n)) for j in range(n)}

def run(q,n):
 N=q**n; B=set(); C=set(); safechecks=0
 for s in product(range(q),repeat=N):
  if not good(s,n):continue
  s=canon(s);B.add(s)
 for b in B:
  safe={i for i in range(N) if good(b[:i]+b[i+1:],n)}
  exp=constpos(b,n)
  assert safe==exp, (q,n,b,safe,exp)
  assert len(safe)==q*n
  for i in safe:C.add(canon(b[:i]+b[i+1:]))
  safechecks+=len(safe)
 # exhaustive cutdown words and balanced missing edge
 allC={canon(s) for s in product(range(q),repeat=N-1) if good(s,n)}
 assert allC==C, (q,n,len(allC),len(C))
 expected=factorial(q)**(q**(n-1))//q**n
 assert len(B)==expected
 assert len(C)*(q-1)==q*len(B)
 print('PASS q=%d n=%d debruijn_cycles=%d cutdown_cycles=%d safe_indexed_deletions=%d' %(q,n,len(B),len(C),safechecks))
for q,n in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1)]:run(q,n)
