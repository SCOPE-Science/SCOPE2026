from itertools import product
from collections import defaultdict
from math import prod
from verify import matmul,matvec,gaussian

def gl(n,q):return prod(q**n-q**i for i in range(n))
def count_pairs(n,k,u,c,q):
 return gaussian(n,k,q)*gaussian(k,c,q)*gaussian(n-k,u-c,q)*q**((k-c)*(u-c))
def stab(n,k,u,c,q):
 d=n-k-u+c
 return q**(c*(u-c)+u*d)*gl(u-c,q)
def order(n,q):
 G=gl(n,q)//(q-1)
 total=1+G
 items=[]
 for k in range(1,n):
  for u in range(1,n):
   for c in range(max(0,k+u-n),min(k,u)+1):
    N=count_pairs(n,k,u,c,q); K=stab(n,k,u,c,q)
    assert G%K==0
    total+=N*(G//K)
    items.append((k,u,c,N,G//K))
 return total,items

# Exhaustive actual elementary generator on all matrices and all conjugations for q=2 n=2.
def run_direct(n,q):
 V=list(product(range(q),repeat=n));M=list(product(range(q),repeat=n*n));I=tuple(1 if i==j else 0 for i in range(n) for j in range(n))
 GL=[Q for Q in M if len({matvec(Q,v,n,q) for v in V})==q**n]
 inv={Q:next(R for R in GL if matmul(Q,R,n,q)==I) for Q in GL}
 for g in M:
  for h in M:
   T=matmul(g,h,n,q)
   D=tuple(A for A in M if matmul(T,A,n,q)==A and matmul(A,T,n,q)==A)
   phi=tuple(matmul(matmul(h,A,n,q),g,n,q) for A in D)
   assert any(tuple(matmul(matmul(inv[Q],A,n,q),Q,n,q) for A in D)==phi for Q in GL),(g,h,D)
 print('ALL_ELEMENTARY_EXTEND',n,q,'pairs=',len(M)**2)

for n in (2,3,4):
 for q in (2,3):
  v,st=order(n,q)
  print('ORDER_PREDICTION',n,q,v,'STRATA',len(st))
run_direct(2,2)
run_direct(2,3)

# Independent full-monoid order by enumerating all restrictions of actual conjugations.
def verify_full_order_3_binary():
 n=3;q=2
 V=list(product(range(q),repeat=n));M=list(product(range(q),repeat=n*n))
 I=tuple(1 if i==j else 0 for i in range(n) for j in range(n))
 GL=[Q for Q in M if len({matvec(Q,v,n,q) for v in V})==q**n]
 inverse={Q:next(R for R in GL if matmul(Q,R,n,q)==I) for Q in GL}
 spaces=set()
 for A in M:spaces.add(frozenset(matvec(A,v,n,q) for v in V))
 all_domains=[]
 for F in spaces:
  if len(F)<=1 or len(F)==len(V):continue
  for U in spaces:
   if len(U)<=1 or len(U)==len(V):continue
   D=tuple(A for A in M if all(matvec(A,v,n,q) in F for v in V) and all(matvec(A,v,n,q)==(0,)*n for v in U))
   all_domains.append((F,U,D))
 total=1+len(GL)
 for F,U,D in all_domains:
  signatures={tuple(matmul(matmul(inverse[Q],A,n,q),Q,n,q) for A in D) for Q in GL}
  total+=len(signatures)
  k=next(k for k in range(1,n) if len(F)==q**k)
  u=next(u for u in range(1,n) if len(U)==q**u)
  c=next(c for c in range(n+1) if len(F&U)==q**c)
  assert len(signatures)==len(GL)//stab(n,k,u,c,q), (k,u,c,len(signatures))
 assert total==order(n,q)[0]==15506, total
 print('FULL_ORDER_DIRECT_OK',n,q,'domains=',len(all_domains),'elements=',total)
verify_full_order_3_binary()
